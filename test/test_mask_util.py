import unittest
from eloservice.login_util import LoginUtil
from eloservice.mask_util import MaskUtil
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

    def test_get_all_masks(self):
        elo_connection, elo_client = self._login()
        util = MaskUtil(elo_client, elo_connection)

        masks = util.get_all_masks_names()

        assert masks is not None
        assert len(masks) > 0
        assert masks[0].name is not None
        assert masks[0].id is not None
        assert masks[0].access is not None

    def test_set_metadata_on_sord(self):
        # "/Alpha AG/temp rechnungen/test1"
        elo_connection, elo_client = self._login()
        util = MaskUtil(elo_client, elo_connection)

        erg = util.overwrite_mask_fields(
            sord_id="134699",
            mask_name="Images",
            metadata={
                "LATITUDE": "35.732554",
                "LONGITUDE": "139.714302",
                "ITEMDOCDATE": "2023-12-26"
            }
        )
