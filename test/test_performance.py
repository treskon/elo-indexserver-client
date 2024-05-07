import os
import unittest
from datetime import datetime

from eloservice.login_util import LoginUtil
from eloservice.mask_util import MaskUtil


class TestPerformance(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        return login_util.elo_connection, login_util.elo_client

    def test_check_cache_mask_util(self):
        # "/Alpha AG/temp rechnungen/test1"
        elo_connection, elo_client = self._login()
        util = MaskUtil(elo_client, elo_connection)

        startTime = datetime.now()
        __stop = 100
        self.update_ntimes(__stop, util)
        endTime = datetime.now()
        time_withCache = endTime - startTime
        print(f"Time taken for {__stop} iterations: ", time_withCache)
        util = MaskUtil(elo_client, elo_connection, cache_enable=False)
        startTime = datetime.now()
        self.update_ntimes(__stop, util)
        endTime = datetime.now()
        time_withoutCache = endTime - startTime
        print(f"Time taken for {__stop} iterations: ", time_withoutCache)
        self.assertLess(time_withCache, time_withoutCache)

    def update_ntimes(self, __stop, util):
        for i in range(__stop):
            if i % 10 == 0:
                print("Iteration: ", i)
            # path in elo: ¶EIWECK_INTEGRATION_TEST¶PythonAPI
            erg = util.overwrite_mask_fields(
                sord_id="139920",
                mask_name="Images",
                metadata={
                    "LATITUDE": "35.732554",
                    "LONGITUDE": "139.714302",
                    "ITEMDOCDATE": "2023-12-26"
                }
            )
            i += 1
