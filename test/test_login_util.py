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


class TestLoginSpecialCharacters(unittest.TestCase):
    """Login of a user whose name and password contain special characters. Self-contained: creates the user and
    deletes it at the end."""

    def test_login_with_special_characters(self):
        from datetime import datetime
        from eloclient.models import UserInfo
        from eloservice.user_util import UserUtil

        admin = LoginUtil(os.environ["TEST_ELO_IX_URL"], os.environ["TEST_ELO_IX_USER"],
                          os.environ["TEST_ELO_IX_PASSWORD"])
        admin_util = UserUtil(admin.elo_client, admin.elo_connection)
        user = UserInfo()
        user.name = "Test Jürgen Größ [" + datetime.now().strftime("%d-%m-%Y:%H:%M:%S") + "]"
        user.pwd = "Pässwörd_§€ß:1"
        user.user_props = ["", "", "", "", "", "", "", ""]
        new_user_id = admin_util.create_user(user)
        try:
            login_util = LoginUtil(os.environ["TEST_ELO_IX_URL"], user.name, user.pwd)
            util = UserUtil(login_util.elo_client, login_util.elo_connection)
            users = util.get_user_base(user.name)
            self.assertEqual(user.name, users[0].name)
            # a second call reuses the ticket
            self.assertEqual(user.name, util.get_user_base(str(users[0].id))[0].name)
            with self.assertRaises(ValueError):
                LoginUtil(os.environ["TEST_ELO_IX_URL"], user.name, "Wrong_Pässwörd")
        finally:
            admin_util.delete_user(str(new_user_id))
