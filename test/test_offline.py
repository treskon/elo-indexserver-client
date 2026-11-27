"""
Tests that do not need an ELO server. They also run locally without the TEST_ELO_IX_* environment variables.
"""
import base64
import json
import unittest

import httpx

from eloservice.file_util import _guess_mimetype
from eloservice.login_util import EloTicketAuth, _basic_auth_possible, prepare_elo_client, EloConnection


class TestGuessMimetype(unittest.TestCase):

    def test_unknown_extension_falls_back_to_octet_stream(self):
        # https://github.com/treskon/elo-indexserver-client/issues/33
        self.assertEqual("application/octet-stream", _guess_mimetype("file.unknownextension"))

    def test_no_extension_falls_back_to_octet_stream(self):
        self.assertEqual("application/octet-stream", _guess_mimetype("README"))
        self.assertEqual("application/octet-stream", _guess_mimetype(""))

    def test_jpeg_is_mapped_to_jpg(self):
        self.assertEqual("image/jpg", _guess_mimetype("mona.jpeg"))
        self.assertEqual("image/jpg", _guess_mimetype("mona.JPG"))

    def test_known_types(self):
        self.assertEqual("image/png", _guess_mimetype("testFile.png"))
        self.assertEqual("application/pdf", _guess_mimetype("chicken.pdf"))



class FakeIndexserver:
    """Answers login with a new ticket per call and accepts only the latest ticket as Bearer token."""

    def __init__(self, ticket_lifetime=600):
        self.logins = []
        self.ticket = None
        self.ticket_lifetime = ticket_lifetime
        self.authorizations = []

    def handler(self, request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/IXServicePortIF/login"):
            body = json.loads(request.content.decode("utf-8"))
            self.logins.append((body["userName"], body["userPwd"], body.get("ci")))
            if body["userPwd"] != "Pässwörd§€":
                return httpx.Response(200, json={"exception": "[ELOIX:5023]wrong password"})
            self.ticket = f"TICKET{len(self.logins)}"
            return httpx.Response(200, json={"result": {"clientInfo": {"ticket": self.ticket},
                                                        "ticketLifetime": self.ticket_lifetime}})
        self.authorizations.append(request.headers.get("Authorization"))
        if request.headers.get("Authorization") != f"Bearer {self.ticket}":
            return httpx.Response(200, json={"exception": "[EIX:2001]session unknown"})
        return httpx.Response(200, json={"result": "ok"})


class TestLogin(unittest.TestCase):
    url = "http://elo.example:9090/ix-Archive/rest/"

    def _auth(self, server, password="Pässwörd§€"):
        return EloTicketAuth(self.url, "Jürgen Müller", password, transport=httpx.MockTransport(server.handler))

    def test_basic_auth_only_for_ascii_credentials(self):
        self.assertTrue(_basic_auth_possible("Administrator", "elo_secret!%&"))
        self.assertFalse(_basic_auth_possible("Administrator", "Pässwörd"))
        self.assertFalse(_basic_auth_possible("Jürgen", "secret"))
        self.assertFalse(_basic_auth_possible("domain:user", "secret"))
        self.assertTrue(_basic_auth_possible("user", "pass:word"))

    def test_ascii_credentials_keep_basic_auth(self):
        client = prepare_elo_client(EloConnection(url=self.url, user="Administrator", password="elo"))
        expected = "Basic " + base64.b64encode(b"Administrator:elo").decode("ascii")
        self.assertEqual(expected, client.get_httpx_client().headers["Authorization"])

    def test_login_sends_credentials_utf8_in_json_body(self):
        server = FakeIndexserver()
        self.assertEqual("TICKET1", self._auth(server).login())
        user, password, ci = server.logins[0]
        self.assertEqual(("Jürgen Müller", "Pässwörd§€"), (user, password))
        self.assertIsNotNone(ci)  # without the ci the server does not return a real ticket

    def test_wrong_password_raises(self):
        with self.assertRaises(ValueError):
            self._auth(FakeIndexserver(), password="wrong").login()

    def test_requests_use_bearer_ticket(self):
        server = FakeIndexserver()
        auth = self._auth(server)
        with httpx.Client(auth=auth, transport=httpx.MockTransport(server.handler)) as client:
            self.assertEqual({"result": "ok"}, client.post(self.url + "IXServicePortIF/getServerInfo", json={}).json())
            self.assertEqual({"result": "ok"}, client.post(self.url + "IXServicePortIF/getServerInfo", json={}).json())
        self.assertEqual(1, len(server.logins))
        self.assertEqual(["Bearer TICKET1", "Bearer TICKET1"], server.authorizations)

    def test_relogin_when_session_unknown(self):
        server = FakeIndexserver()
        auth = self._auth(server)
        auth.login()
        server.ticket = "INVALIDATED_BY_SERVER"
        with httpx.Client(auth=auth, transport=httpx.MockTransport(server.handler)) as client:
            response = client.post(self.url + "IXServicePortIF/getServerInfo", json={"a": 1})
        self.assertEqual({"result": "ok"}, response.json())
        self.assertEqual(2, len(server.logins))
        self.assertEqual(["Bearer TICKET1", "Bearer TICKET2"], server.authorizations)

    def test_relogin_after_idle_lifetime(self):
        server = FakeIndexserver(ticket_lifetime=10)
        auth = self._auth(server)
        auth.login()
        auth._last_used -= 60  # idle for a minute
        with httpx.Client(auth=auth, transport=httpx.MockTransport(server.handler)) as client:
            client.post(self.url + "IXServicePortIF/getServerInfo", json={})
        self.assertEqual(2, len(server.logins))
        self.assertEqual(["Bearer TICKET2"], server.authorizations)


if __name__ == '__main__':
    unittest.main()
