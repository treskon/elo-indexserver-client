import os
import unittest

from eloservice import elo_service
from eloservice.login_util import LoginUtil
from eloservice.map_util import MapUtil
from test import TEST_ROOT_DIR


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

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test2",
                                         separator="¶")

        util.write_map_fields(sord_id=folderid, fields={"testBlob": "testBlob",
                                                        "500CharBlob": self.lorem
                                                        # bigger than ELO 255 char limit
                                                        }

                              , map_domain="Objekte",
                              value_type=MapUtil.ValueType.blob_string)

    def test_write_map_fields_blob_file_withFilepath(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test2",
                                         separator="¶")

        filepath = TEST_ROOT_DIR + "/resources/testFile.png"
        util.write_map_fields(sord_id=folderid,
                              fields={"testFileBlobPath": filepath},
                              content_type="image/png",
                              map_domain="Objekte",
                              value_type=MapUtil.ValueType.blob_file)

    def test_write_map_fields_blob_file_withBytes(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test2",
                                         separator="¶")

        filepath = TEST_ROOT_DIR + "/resources/testFile.png"
        value_bytes = open(filepath, "rb").read()

        util.write_map_fields(sord_id=folderid,
                              fields={"testFileBlobBytes": value_bytes},
                              content_type="image/png",
                              map_domain="Objekte",
                              value_type=MapUtil.ValueType.blob_file)

    # map_value_instance = MapUtil.MapValue(MapUtil.ValueType.blob_string, "example_value", "text/plain", b"Hello, world!")

    def test_read_all_map_fields(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")

        util.read_map_fields(sord_id=folderid,
                             map_domain="Objekte",
                             key='')

    def test_read_map_field(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")

        key = 'test'

        util.read_map_fields(sord_id=folderid,
                             map_domain="Objekte",
                             key=key)
