import os
import unittest
from datetime import datetime

from eloclient.models import UserInfo
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

    def test_get_user_does_not_exist(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        users = util.get_user_base("M11 STEIN Martina", "RandomUserNameThatSurelyDoesNotExistPls")
        assert users is None

    def test_get_user_details(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert user.name == "L23 TURNER Claudia"

    def test_update_user_details(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        # 1. Get user details
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert user.name == "L23 TURNER Claudia"

        # 2. Update user details
        user.name = "L23 TURNER Claudia Updated"
        util.update_user_details(user)
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert user.name == "L23 TURNER Claudia Updated"

        # 3. Revert user details
        user.name = "L23 TURNER Claudia"
        util.update_user_details(user)
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert user.name == "L23 TURNER Claudia"

    # def test_create_new_user(self):
    #     elo_connection, elo_client = self._login()
    #     util = UserUtil(elo_client, elo_connection)
    #     # Craft UserObject
    #     # user = UserInfo()
    #     # dd-mm-yyyy:hh:mm:ss
    #     timestamp = datetime.now().strftime("%d-%m-%Y:%H:%M:%S")
    #     # user.name = "Test User [" + timestamp + "]"
    #     # user.user_props = ["NTNAME"]
    #     # user.internal_user = False
    #     new_user_guid = util.create_new_user()
    #     user = util.get_user_details(new_user_guid)
    #     user.name = "Test User [" + timestamp + "]"
    #     user.user_props = ["NTNAME"]
    #     util.update_user_details(user)


    def test_get_group(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        groups = util.get_group_base("TestACUser")
        assert groups is not None
        assert len(groups) == 1
        assert groups[0].name == "TestACUser"

    def test_get_group_notexists(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        groups = util.get_group_base("TestACUserExistNot")
        assert groups is None

    def test_get_group_details(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        groups = util.get_group_base("TestACUser")
        group = util.get_group_details(groups[0].id)
        assert group is not None
        assert group.name == "TestACUser"


    def test_manually_add_group(self):
        elo_connection, elo_client = self._login()
        util = UserUtil(elo_client, elo_connection)
        groups = util.get_group_base("TestACUser")
        group_id = groups[0].id

        # 1. Get user details
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert user.name == "L23 TURNER Claudia"

        # 2. Remove user from group
        user.group_list.remove(group_id)
        util.update_user_details(user)
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert group_id not in user.group_list

        # 3. Add user to group
        user.group_list.append(group_id)
        util.update_user_details(user)
        user = util.get_user_details("19")
        assert user is not None
        assert user.id == 19
        assert group_id in user.group_list
