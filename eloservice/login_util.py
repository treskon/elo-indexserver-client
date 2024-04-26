import base64
import logging

import httpx
from attrs import define as define

from eloclient import Client


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
    logging.debug(f"Request headers {request.headers}")
    logging.debug(f"Request detail {request.content}")


def _gen_http_basic_hash(user, pw) -> str:
    return base64.b64encode((user + ":" + pw).encode("utf-8")).decode("utf-8")


def prepare_elo_client(elo_connection) -> Client:
    # can't use authenticated client here, because elo does not use a token instead HTTP basic or their proprietary
    # ci attribute packaged in the body of each request
    client = Client(base_url=elo_connection.url, httpx_args={"event_hooks": {"request": [_log_http_request],
                                                                             "response": [_log_http_response]}})
    client = client.with_headers({
        "Authorization": "Basic " + _gen_http_basic_hash(elo_connection.user, elo_connection.password)
    })

    return client


class LoginUtil:
    elo_connection: EloConnection
    url: str
    user: str
    password: str

    def __init__(self, url: str, user: str, password: str):
        """
        Known issue: Due to encoding issues the user and password should not contain special characters.
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
