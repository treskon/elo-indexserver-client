import os
import unittest

from eloservice.login_util import LoginUtil
from eloservice.user_util import UserUtil


class TestService(unittest.TestCase):
    url = os.environ["TEST_ELO_IX_URL"]
    user = os.environ["TEST_ELO_IX_USER"]
    password = os.environ["TEST_ELO_IX_PASSWORD"]

    if __name__ == '__main__':
        unittest.main()

    def _login(self):
        login_util = LoginUtil(self.url, self.user, self.password)
        return login_util.elo_connection, login_util.elo_client

    def test_get_user_id_by_username(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        users = util.get_user_base("M11 STEIN Martina",
                                   "K33 MUSTER Max",
                                   "L23 TURNER Claudia")
        assert users is not None
        assert len(users) == 3
        assert users[0].name == "M11 STEIN Martina"
        assert users[1].name == "K33 MUSTER Max"
        assert users[2].name == "L23 TURNER Claudia"

    def test_get_user_id_by_id(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        users = util.get_user_base("M11 STEIN Martina",
                                   "(5330D865-5082-1CF3-B58A-75CCAEAB9B26)",
                                   "19")
        assert users is not None
        assert len(users) == 3
        assert users[0].name == "M11 STEIN Martina"
        assert users[1].name == "K33 MUSTER Max"
        assert users[2].name == "L23 TURNER Claudia"
