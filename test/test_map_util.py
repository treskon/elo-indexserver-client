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

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
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

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
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

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")

        filepath = TEST_ROOT_DIR + "/resources/testFile.png"
        value_bytes = open(filepath, "rb").read()

        util.write_map_fields(sord_id=folderid,
                              fields={"testFileBlobBytes": value_bytes},
                              content_type="image/png",
                              map_domain="Objekte",
                              value_type=MapUtil.ValueType.blob_file)

    def test_read_all_map_fields(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")
        util.write_map_fields(sord_id=folderid, fields={"mapfieldKey1": "mapfieldValue1",
                                                        "mapfieldKey2": "mapfieldValue2",
                                                        "mapfieldKey3": "mapfieldValue3",
                                                        "mapfieldKey4": "mapfieldValue4"
                                                        }
                              , map_domain="Objekte",
                              value_type=MapUtil.ValueType.string)

        fields = util.read_map_fields(sord_id=folderid)
        self.assertEqual(fields["mapfieldKey1"].value, "mapfieldValue1")
        self.assertEqual(fields["mapfieldKey2"].type, MapUtil.ValueType.string)
        self.assertEqual(fields["mapfieldKey2"].value, "mapfieldValue2")
        self.assertEqual(fields["mapfieldKey3"].value, "mapfieldValue3")
        self.assertEqual(fields["mapfieldKey4"].value, "mapfieldValue4")

    def test_read_specific_map_fields(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")
        util.write_map_fields(sord_id=folderid, fields={"mapfieldKey1": "mapfieldValue1",
                                                        "mapfieldKey2": "mapfieldValue2",
                                                        "mapfieldKey3": "mapfieldValue3",
                                                        "mapfieldKey4": "mapfieldValue4"
                                                        }
                              , map_domain="Objekte",
                              value_type=MapUtil.ValueType.string)

        fields = util.read_map_fields(sord_id=folderid, keys=["mapfieldKey1", "mapfieldKey2"])
        self.assertEqual(fields["mapfieldKey1"].value, "mapfieldValue1")
        self.assertEqual(fields["mapfieldKey2"].value, "mapfieldValue2")
        self.assertNotIn("mapfieldKey3", fields)
        self.assertNotIn("mapfieldKey4", fields)

    def test_read_map_fields_blob_file(self):
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)

        folderid = service.create_folder(path="¶Alpha AG¶IntegrationTests¶test",
                                         separator="¶")

        filepath = TEST_ROOT_DIR + "/resources/testFile.png"
        #read file path as bytes
        filebytes = open(filepath, "rb").read()

        util.write_map_fields(sord_id=folderid,
                              fields={"testFileBlobPath": filebytes},
                              content_type="image/png",
                              map_domain="Objekte",
                              value_type=MapUtil.ValueType.blob_file)
        fields = util.read_map_fields(sord_id=folderid, keys=["testFileBlobPath"])
        self.assertEqual(fields["testFileBlobPath"].mime_type, "image/png")
        self.assertEqual(fields["testFileBlobPath"].type, MapUtil.ValueType.blob_file)
        self.assertEqual(fields["testFileBlobPath"].blob_value, filebytes)


    def test_transform_keyvalue_to_table(self):
        folderid = "115365"
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)
        map_fields = util.read_map_fields(sord_id=folderid)
        col_names = ["ASSIGNMENT", "ELOGUID","ELOOBJID","SHAREHOLDER","SHAREINPERCENT", "SHAREHOLDERID",]
        table_name = "SHARE_PARENT"
        table = util.transform_keyvalue_to_table(map_fields, table_name=table_name, column_names=col_names)
        assert table is not None
        assert len(table) > 0

    def test_transform_table_to_keyvalue(self):
        folderid = "115365"
        elo_connection, elo_client = self._login()
        service = elo_service.EloService(self.url, self.user, self.password)
        util = MapUtil(elo_client, elo_connection)
        map_fields = util.read_map_fields(sord_id=folderid)
        col_names = ["ASSIGNMENT", "ELOGUID","ELOOBJID","SHAREHOLDER","SHAREINPERCENT", "SHAREHOLDERID",]
        table_name = "SHARE_PARENT"
        table = util.transform_keyvalue_to_table(map_fields, table_name=table_name, column_names=col_names)
        assert table is not None
        assert len(table) > 0
        key_values = util.transform_table_to_keyvalue(table, table_name=table_name)
        # assert that all keys from key_values are in map_fields and that the values are the same
        for key, value in key_values.items():
            assert key in map_fields
            assert value.value == map_fields[key].value

