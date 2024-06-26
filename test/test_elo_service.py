import os
import unittest
from datetime import datetime

from eloclient.models import Sord
from eloservice import elo_service
from test import TEST_ROOT_DIR


class TestService(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def test_create_folder(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        folderid = service.create_folder(path="¶EIWECK_INTEGRATION_TEST¶PythonAPI¶test_elo_service¶test_create_folder",
                                         separator="¶")
        assert folderid is not None
        assert folderid != ""

    def test_overwrite_mask_fields(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        service.overwrite_mask_fields(sord_id="134699", mask_name="Images", metadata={
            "LATITUDE": "35.732554",
            "LONGITUDE": "139.714302",
            "ITEMDOCDATE": "2023-12-26"
        })

    def test_split_path_elements(self):
        service = elo_service.EloService(self.url, self.user, self.password)

        # default separator is ¶
        path = "Alpha AG¶Eingangsrechnungen¶2023¶November¶20"
        expected_result = [Sord(name="Alpha AG"), Sord(name="Eingangsrechnungen"), Sord(name="2023"),
                           Sord(name="November"), Sord(name="20")]
        result = service._split_path_elements(path)
        self.assertEqual(result, expected_result)

        # separator /
        path = "/Alpha AG/Eingangsrechnungen/2023/November/20/"
        expected_result = [Sord(name="Alpha AG"), Sord(name="Eingangsrechnungen"), Sord(name="2023"),
                           Sord(name="November"), Sord(name="20")]
        result = service._split_path_elements(path, "/")

        self.assertEqual(result, expected_result)

    def test_move(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        currentTimestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        path = "¶EIWECK_INTEGRATION_TEST¶PythonAPI¶test_elo_service¶testMove¶" + currentTimestamp
        folder_id = service.create_folder(path=path + "¶before", separator="¶")
        sordID = service.upload_file(file_path=TEST_ROOT_DIR + "/resources/testFile.png", parent_id=folder_id)
        service.move(source_sord_id=sordID, path=path + "¶after", separator="¶")

    def test_remove(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        id_elo = service.create_folder(path="¶EIWECK_INTEGRATION_TEST¶PythonAPI¶test_elo_service¶testRemove",
                                       separator="¶")
        service.remove(id_elo)