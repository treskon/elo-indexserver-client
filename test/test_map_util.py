import os
import unittest

from eloservice import elo_service
from eloservice.login_util import LoginUtil
from eloservice.map_util import MapUtil


class TestService(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    lorem = ("ÄÖÜLorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut "
             "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et "
             "ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem "
             "ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
             "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "
             "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor "
             "sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna "
             "aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita "
             "kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.Duis autem vel eum iriure dolor "
             "in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu f")

    if __name__ == '__main__':
        unittest.main()

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        return login_util.elo_connection, login_util.elo_client

    def test_write_map_fields_string(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test", separator="¶")

        util.write_map_fields(sord_id=folderid, fields={"test": "test",
                                                        "test2": "test2",
                                                        "test3": "test3",
                                                        "test4": "test4"
                                                        }
                              , map_domain="Objekte",
                              value_type=MapUtil.ValueType.string)

    def test_write_map_fields_blob_string(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")

        util.write_map_fields(sord_id=folderid, fields={"testBlob": "testBlob",
                                                        "500CharBlob": self.lorem
                                                        # bigger than ELO 255 char limit
                                                        }

                              , map_domain="Objekte",
                              value_type=MapUtil.ValueType.blob_string)
