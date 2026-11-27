"""
Tests that do not need an ELO server. They also run locally without the TEST_ELO_IX_* environment variables.
"""
import base64
import json
import unittest

import httpx

from datetime import date, datetime
from decimal import Decimal

from eloservice import aspect_util
from eloservice.aspect_util import build_aspect_search, index_value_to_python, python_to_index_value
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



class TestAspectConversion(unittest.TestCase):

    def test_python_to_index_value(self):
        self.assertEqual({"type": 3, "stringValue": "Grüß Gott"},
                         python_to_index_value("Grüß Gott", aspect_util.ASPECT_LINE_TYPE_TEXT))
        self.assertEqual({"type": 1, "intValue": 42}, python_to_index_value(42, aspect_util.ASPECT_LINE_TYPE_INTEGER))
        self.assertEqual({"type": 2, "doubleValue": 3.5},
                         python_to_index_value(Decimal("3.5"), aspect_util.ASPECT_LINE_TYPE_DOUBLE))
        self.assertEqual({"type": 10, "stringValue": "12.30"},
                         python_to_index_value(Decimal("12.30"), aspect_util.ASPECT_LINE_TYPE_FIXED_POINT_NUMBER))
        self.assertEqual({"type": 4, "stringValue": "20240131"},
                         python_to_index_value(date(2024, 1, 31), aspect_util.ASPECT_LINE_TYPE_ISO_DATE_ONLY))
        self.assertEqual({"type": 5, "stringValue": "20240131134510000"},
                         python_to_index_value(datetime(2024, 1, 31, 13, 45, 10),
                                               aspect_util.ASPECT_LINE_TYPE_ISO_DATE_TIME))
        self.assertEqual({"type": 8, "stringValue": "(GUID)"},
                         python_to_index_value("(GUID)", aspect_util.ASPECT_LINE_TYPE_USER))

    def test_index_value_to_python(self):
        self.assertEqual("text", index_value_to_python({"type": 3, "stringValue": "text"}))
        self.assertEqual(42, index_value_to_python({"type": 1, "intValue": 42}))
        self.assertEqual(3.5, index_value_to_python({"type": 2, "doubleValue": 3.5}))
        self.assertEqual(Decimal("12.30"), index_value_to_python({"type": 10, "stringValue": "12.30"}))
        self.assertEqual(date(2024, 1, 31), index_value_to_python({"type": 4, "stringValue": "20240131"}))
        self.assertEqual(date(2024, 1, 31), index_value_to_python({"type": 4, "stringValue": "2024-01-31"}))
        self.assertEqual(datetime(2024, 1, 31, 13, 45, 10, 123000),
                         index_value_to_python({"type": 5, "stringValue": "20240131134510123"}))
        self.assertEqual(datetime(2024, 1, 31, 13, 45, 10),
                         index_value_to_python({"type": 5, "stringValue": "20240131134510"}))
        self.assertEqual(datetime(2024, 1, 31, 13, 45, 10),
                         index_value_to_python({"type": 5, "stringValue": "2024-01-31T13:45:10"}))
        self.assertEqual("not a date", index_value_to_python({"type": 4, "stringValue": "not a date"}))
        self.assertIsNone(index_value_to_python(None))

    def test_cardinality_name(self):
        self.assertEqual("OPTIONAL_MANY", aspect_util._cardinality_name("OPTIONAL_MANY"))
        self.assertEqual("OPTIONAL_MANY", aspect_util._cardinality_name(3))
        self.assertEqual("OPTIONAL", aspect_util._cardinality_name(0))

    def test_build_aspect_search(self):
        self.assertEqual({
            "A¶ADDRESS¶CITY": {"condition": {"stringValue": {"operator": "EQUALS", "operand": "Graz"}}},
            "¶ADDRESS¶ZIP": {"disjunctConditions": [{"stringValue": {"operator": "EQUALS", "operand": "8010"}},
                                                    {"stringValue": {"operator": "EQUALS", "operand": "8020"}}]},
            "¶POS¶AMOUNT": {"condition": {"intValue": {"operator": "GREATER", "operand": 100}}},
            "¶POS¶PRICE": {"condition": {"doubleValue": {"operator": "LOWER_THAN", "operand": 9.5}}},
            "¶POS¶DAY": {"condition": {"stringValue": {"operator": "EQUALS", "operand": "20240131"}}},
        }, build_aspect_search({
            "A¶ADDRESS¶CITY": "Graz",
            "¶ADDRESS¶ZIP": ["8010", "8020"],
            "¶POS¶AMOUNT": ("GREATER", 100),
            "¶POS¶PRICE": ("LOWER_THAN", 9.5),
            "¶POS¶DAY": date(2024, 1, 31),
        }))

    def test_build_aspect_search_invalid(self):
        with self.assertRaises(ValueError):
            build_aspect_search({"ADDRESS¶CITY": "Graz"})
        with self.assertRaises(ValueError):
            build_aspect_search({"¶ADDRESS¶CITY": ("NOT_AN_OPERATOR", "Graz")})

    def test_search_body_contains_aspects(self):
        from eloclient.models import FindByIndex
        find_by_index = FindByIndex()
        find_by_index.additional_properties["aspects"] = build_aspect_search({"¶A¶B": 1})
        self.assertEqual({"¶A¶B": {"condition": {"intValue": {"operator": "EQUALS", "operand": 1}}}},
                         find_by_index.to_dict()["aspects"])


if __name__ == '__main__':
    unittest.main()
