import base64
import logging
import threading
import time
from typing import Optional

import httpx
from attrs import define as define

from eloclient import Client

LOGIN_PATH = "/IXServicePortIF/login"


@define
class Cookie:
    key: str
    value: str


@define
class EloConnection:
    url: str
    user: str
    password: str


def _log_http_response(response: httpx.Response):
    request = response.request
    logging.debug(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")


def _log_http_request(request):
    logging.debug(f"Request event hook: {request.method} {request.url} - Waiting for response")
    if request.url.path.endswith(LOGIN_PATH):
        return  # the body of the login call contains the password
    logging.debug(f"Request headers {request.headers}")
    logging.debug(f"Request detail {request.content}")


def _gen_http_basic_hash(user, pw) -> str:
    return base64.b64encode((user + ":" + pw).encode("utf-8")).decode("utf-8")


def _basic_auth_possible(user: str, password: str) -> bool:
    """
    HTTP Basic auth only works reliably with ASCII credentials. A colon in the user name would also break it, as
    user and password are separated by the first colon.
    """
    return (user or "").isascii() and (password or "").isascii() and ":" not in (user or "")


class EloTicketAuth(httpx.Auth):
    """
    Authentication via an ELO session ticket, used when the user or the password contain non-ASCII characters
    (e.g. umlauts like ä, ö, ü, ß or symbols like §, €).

    HTTP Basic auth has no defined character encoding and the Indexserver does not decode UTF-8 credentials in the
    Authorization header correctly, so the login fails. This class instead logs in with
    IXServicePortIF/login, where user and password are sent in the JSON body (always UTF-8), and authenticates every
    following request with the returned ticket as Bearer token (supported by the Indexserver for services).

    The ticket is renewed automatically: before a request if it was idle for longer than its lifetime, and once
    after a request if the server reports an unknown session ([EIX:2001]) or answers with HTTP 401.
    """
    requires_response_body = True
    # renew the ticket a bit before the idle lifetime that the server returns
    _LIFETIME_SAFETY_FACTOR = 0.8

    def __init__(self, url: str, user: str, password: str, verify_ssl=True, timeout: Optional[httpx.Timeout] = None,
                 transport: Optional[httpx.BaseTransport] = None):
        self._login_url = url.rstrip("/") + LOGIN_PATH
        self._user = user
        self._password = password
        self._verify_ssl = verify_ssl
        self._timeout = timeout if timeout is not None else httpx.Timeout(60.0)
        self._ticket: Optional[str] = None
        self._lifetime_seconds: Optional[float] = None
        self._last_used: float = 0.0
        self._transport = transport  # only needed for tests
        self._lock = threading.Lock()

    def login(self) -> str:
        """
        Logs in at the Indexserver and returns the ticket.
        :raises ValueError: if the login fails
        """
        body = {
            # a dummy ClientInfo is needed, otherwise the server only returns "de.elo.ix.client.ticket_from_cookie"
            "ci": {"callId": "", "country": "", "language": "", "ticket": "", "timeZone": "", "options": 0},
            "userName": self._user,
            "userPwd": self._password,
            "clientComputer": "",
            "runAsUser": "",
        }
        # separate client: the session cookies of the login must not end up in the cookie jar of the main client
        with httpx.Client(verify=self._verify_ssl, timeout=self._timeout, transport=self._transport) as client:
            response = client.post(self._login_url, json=body)
        if response.status_code != 200:
            raise ValueError(f"Login at ELO IX server failed: {response.status_code} - {response.text}")
        try:
            data = response.json()
        except ValueError:
            raise ValueError(f"Login at ELO IX server failed: unexpected response {response.text}")
        if data.get("exception"):
            raise ValueError(f"Login at ELO IX server failed: {data.get('exception')}")
        result = data.get("result") or {}
        ticket = (result.get("clientInfo") or {}).get("ticket")
        if not ticket or ticket == "de.elo.ix.client.ticket_from_cookie":
            raise ValueError(f"Login at ELO IX server failed: no ticket in response {response.text}")
        lifetime = result.get("ticketLifetime")
        self._lifetime_seconds = float(lifetime) if isinstance(lifetime, (int, float)) and lifetime > 0 else None
        self._ticket = ticket
        self._last_used = time.monotonic()
        return ticket

    def _ticket_expired(self) -> bool:
        if self._ticket is None:
            return True
        if self._lifetime_seconds is None:
            return False
        return time.monotonic() - self._last_used > self._lifetime_seconds * self._LIFETIME_SAFETY_FACTOR

    def _current_ticket(self, force_renew=False) -> str:
        with self._lock:
            if force_renew or self._ticket_expired():
                self.login()
            self._last_used = time.monotonic()
            return self._ticket

    @staticmethod
    def _is_session_invalid(response: httpx.Response) -> bool:
        if response.status_code == 401:
            return True
        if response.status_code == 200 and "application/json" in response.headers.get("content-type", ""):
            content = response.text
            return "\"exception\"" in content and "2001]" in content
        return False

    def auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = "Bearer " + self._current_ticket()
        response = yield request
        if self._is_session_invalid(response):
            logging.debug("ELO session ticket is no longer valid, logging in again")
            request.headers["Authorization"] = "Bearer " + self._current_ticket(force_renew=True)
            yield request


def prepare_elo_client(elo_connection) -> Client:
    event_hooks = {"request": [_log_http_request], "response": [_log_http_response]}
    if _basic_auth_possible(elo_connection.user, elo_connection.password):
        # can't use authenticated client here, because elo does not use a token instead HTTP basic or their
        # proprietary ci attribute packaged in the body of each request
        client = Client(base_url=elo_connection.url, httpx_args={"event_hooks": event_hooks})
        return client.with_headers({
            "Authorization": "Basic " + _gen_http_basic_hash(elo_connection.user, elo_connection.password)
        })
    # Basic auth does not work with these credentials -> login via JSON body and use the session ticket
    auth = EloTicketAuth(elo_connection.url, elo_connection.user, elo_connection.password)
    auth.login()  # fail fast on wrong credentials, like the first call with Basic auth would
    return Client(base_url=elo_connection.url, httpx_args={"event_hooks": event_hooks, "auth": auth})


class LoginUtil:
    elo_connection: EloConnection
    url: str
    user: str
    password: str

    def __init__(self, url: str, user: str, password: str):
        """
        User and password may contain special characters (e.g. ä, ö, ü, ß, §, €). Credentials that only contain
        ASCII characters are sent via HTTP Basic auth; otherwise (or if the user name contains a colon) the client
        logs in via IXServicePortIF/login and uses the session ticket (see :class:`EloTicketAuth`).
        :param url: The URL to the ELO IX server rest endpoint e.g. http://eloserver.com:6056/ix-Archive/rest/
        :param user: The user for the ELO IX server e.g. Administrator
        :param password: The password for the ELO IX server user e.g. secret
        """
        self.url = url
        self.user = user
        self.password = password
        self.elo_client = None  # is set in renew_token
        self._gen_client()

    def _gen_client(self) -> EloConnection:
        self.elo_connection = EloConnection(url=self.url, user=self.user, password=self.password)
        self.elo_client = prepare_elo_client(self.elo_connection)
