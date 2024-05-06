import unittest
from datetime import datetime

from eloservice.login_util import LoginUtil
from eloservice.mask_util import MaskUtil
import os

class TestPerformance(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        return login_util.elo_connection, login_util.elo_client

    def test_set_metadata_on_sord_500(self):
        # "/Alpha AG/temp rechnungen/test1"
        elo_connection, elo_client = self._login()
        util = MaskUtil(elo_client, elo_connection)


        startTime = datetime.now()
        i = 0
        __stop = 500
        for i in range(__stop):
            if i % 10 == 0:
                print("Iteration: ", i)
            erg = util.overwrite_mask_fields(
                sord_id="134699",
                mask_name="Images",
                metadata={
                    "LATITUDE": "35.732554",
                    "LONGITUDE": "139.714302",
                    "ITEMDOCDATE": "2023-12-26"
                }
            )
            i += 1
        endTime = datetime.now()
        print(f"Time taken for {__stop} iterations: ", endTime - startTime)


