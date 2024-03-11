import unittest

from eloservice.login_util import LoginUtil
from eloservice.search_util import SearchUtil
import os


class TestService(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        return login_util.elo_connection, login_util.elo_client

    def test_search_maskID(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_id="1", max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 42)

    def test_search_maskID_does_not_exist(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_id="100000", max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 0)

    def test_search_metadata(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_fields={"ITEMOWNER": "PythonAPI-TEST"}, max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 1)

    def test_search_metadata_multiple_fields(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_fields={"ITEMOWNER": "PythonAPI-TEST",
                                                   "ITEMNO": "12345Python"}, max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 1)

    def test_search_metadata_multiple_res(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_fields={"ITEMNO": "12345Python"}, max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 2)

    def test_search_metadata_does_not_exist(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_fields={"ITEMOWNER": "PythonAPI-TEST-DOES-NOT-EXIST"}, max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 0)


    def test_search_metadata_and_maskID(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_fields={"ITEMOWNER": "PythonAPI-TEST"},
                               search_mask_id="376", max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 1)

    def test_search_metadata_and_maskID_does_not_exist(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_fields={"ITEMOWNER": "PythonAPI-TEST-DOES-NOT-EXIST"},
                               search_mask_id="376", max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertEqual(len(mask_ids), 0)

    def test_search_maskID_multiple_res(self):
        elo_connection, elo_client = self._login()
        util = SearchUtil(elo_client, elo_connection)

        mask_ids = util.search(search_mask_id="376", max_results=42)
        self.assertTrue(mask_ids is not None)
        self.assertTrue(len(mask_ids) > 1)