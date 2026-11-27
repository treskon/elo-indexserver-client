import unittest
import os
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

    def test_rename(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        og = service.checkout("162399")
        og_name = og.name
        new_name = "NewName"
        service.rename("162399", new_name)
        new = service.checkout("162399")
        self.assertEqual(new.name, new_name)
        service.rename("162399", og_name)
        self.assertEqual(og.name, og_name)

    def test_add_reference(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        service.add_reference("162468", "¶EIWECK_INTEGRATION_TEST¶PythonAPI¶test-references-ref")
        service.add_reference("162479", "¶EIWECK_INTEGRATION_TEST¶PythonAPI¶test-references-ref")

    def test_get_group_members(self):
        service = elo_service.EloService(self.url, self.user, self.password)
        group = service.get_group_base("TestACUser")
        group_member = service.get_group_members(group[0].id)
        self.assertEqual(group_member[0].name, "K33 MUSTER Max")


class TestUpdateFileKeepsIndexFields(unittest.TestCase):
    """update_file adds a version without clearing the document's index fields. Self-contained: creates a folder,
    uploads a document with mask E-Mail (part of every ELO repository), and removes the folder at the end."""

    def test_update_file_keeps_index_fields(self):
        import time
        service = elo_service.EloService(url=os.environ["TEST_ELO_IX_URL"], user=os.environ["TEST_ELO_IX_USER"],
                             password=os.environ["TEST_ELO_IX_PASSWORD"])
        folder = service.create_folder(f"¶update-file-test-{int(time.time() * 1000)}")
        try:
            sord_id = service.upload_file(TEST_ROOT_DIR + "/resources/testFile.png", folder, filename="index-fields")
            service.overwrite_mask_fields(sord_id, "E-Mail", {"ELOOUTL1": "first value", "ELOOUTL2": "second value"})
            service.update_file(sord_id, TEST_ROOT_DIR + "/resources/mona.jpeg", filename="index-fields")
            fields = service.get_mask_fields(sord_id)
            sord = service.checkout(sord_id)
            self.assertEqual("E-Mail", sord.mask_name)
            self.assertEqual("first value", fields["ELOOUTL1"])
            self.assertEqual("second value", fields["ELOOUTL2"])
            self.assertEqual(["mona.jpeg"], next(key.data for key in sord.obj_keys if key.name == "ELO_FNAME"))
        finally:
            service.remove(folder)


class TestUploadUnknownFileType(unittest.TestCase):
    """upload_file works for files whose mimetype can't be guessed (falls back to application/octet-stream).
    https://github.com/treskon/elo-indexserver-client/issues/33"""

    def test_upload_file_with_unknown_extension(self):
        import tempfile
        import time
        service = elo_service.EloService(url=os.environ["TEST_ELO_IX_URL"], user=os.environ["TEST_ELO_IX_USER"],
                                         password=os.environ["TEST_ELO_IX_PASSWORD"])
        folder = service.create_folder(f"¶unknown-mimetype-test-{int(time.time() * 1000)}")
        try:
            with tempfile.TemporaryDirectory() as tmp:
                file_path = os.path.join(tmp, "data.unknownextension")
                with open(file_path, "wb") as f:
                    f.write(b"some content of an unknown file type")
                sord_id = service.upload_file(file_path, folder, filename="unknown-mimetype")
                self.assertIsNotNone(sord_id)
                download_path = os.path.join(tmp, "downloaded")
                service.download_file(sord_id, download_path)
                with open(download_path, "rb") as f:
                    self.assertEqual(b"some content of an unknown file type", f.read())
        finally:
            service.remove(folder)
