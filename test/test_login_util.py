import unittest

from eloservice.login_util import LoginUtil
import os


class TestService(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        self._assert_login(login_util)
        return login_util

    def _assert_login(self, login_util):
        assert login_util is not None
        assert login_util.elo_client is not None
        assert login_util.elo_connection is not None

    def test_login(self):
        self._login()
