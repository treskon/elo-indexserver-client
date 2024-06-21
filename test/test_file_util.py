import unittest

from eloservice.file_util import FileUtil
from eloservice.login_util import LoginUtil
from test import TEST_ROOT_DIR, _check_not_unset
import os


class TestService(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def _readFile(self, path):
        with open(path, "rb") as file:
            file_content = file.read()
            file_name = file.name
            return file_content, file_name

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        return login_util.elo_connection, login_util.elo_client

    def test_upload_file_to_get_streamID(self):
        elo_connection, elo_client = self._login()
        util = FileUtil(elo_client, elo_connection)
        file_content, file_name = self._readFile(TEST_ROOT_DIR + "/resources/testFile.png")
        streamID = util._upload_file(file_content)
        assert streamID is not None
        assert streamID != ""
        assert len(streamID) > 1

    def test_checkin_doc(self):
        elo_connection, elo_client = self._login()
        util = FileUtil(elo_client, elo_connection)
        parentID = "134698"
        sord = util.upload_file(TEST_ROOT_DIR + "/resources/testFile.png", parentID)
        assert sord is not None
        assert sord != ""

    def test_update_file(self):
        elo_connection, elo_client = self._login()
        util = FileUtil(elo_client, elo_connection)
        sordID = "134699"
        sord = util.update_file(TEST_ROOT_DIR + "/resources/mona.jpeg", sordID, "mona.jpeg")

    def test_checkout_sord(self):
        elo_connection, elo_client = self._login()
        util = FileUtil(elo_client, elo_connection)
        sordID = "134699"
        sord = util.checkout_sord(sordID)
        _check_not_unset(sord)
        _check_not_unset(sord.id)
        _check_not_unset(sord.name)
        _check_not_unset(sord.mask)
        _check_not_unset(sord.guid)
        _check_not_unset(sord.obj_keys)

    def test_upload_file_with_custom_filename(self):
        elo_connection, elo_client = self._login()
        util = FileUtil(elo_client, elo_connection)
        parentID = "134698"
        sord = util.upload_file(TEST_ROOT_DIR + "/resources/chicken.pdf", parentID, filename="importantDokument",
                                filename_objkey="chicken.pdf")
        assert sord is not None
        assert sord != ""
        checkSordID = sord
        sord = util.checkout_sord(checkSordID)
        assert sord.name == "importantDokument"
        assert sord.obj_keys[0].data[0] == "chicken.pdf"
