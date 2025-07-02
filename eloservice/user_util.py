import logging

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_get_user_names, ix_service_port_if_checkout_user, \
    ix_service_port_if_checkin_user, ix_service_port_if_create_user, ix_service_port_if_delete_user, \
    ix_service_port_if_checkout_users
from eloclient.models import BRequestIXServicePortIFGetUserNames, BResult1001617329, UserName, \
    BRequestIXServicePortIFCheckoutUser, BResult1485735592, UserInfo, BRequestIXServicePortIFCheckinUser, BResult5, \
    BRequestIXServicePortIFCreateUser, BRequestIXServicePortIFDeleteUser, BResult19, \
    BRequestIXServicePortIFCheckoutUsers, BResult1132956238, MapToString
from eloclient.types import Response, Unset
from eloservice.eloconstants import CHECKOUT_USERS_Z_ALL_BY_ID, LOCK_Z_NO, CHECKIN_USER_UPDATE, CHECKIN_USER_CREATE, \
    CHECKOUT_USERS_Z_MEMBERS_OF_GROUP
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


class UserUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def get_user_base(self, *user_identifier: str) -> [UserName]:
        """
        Loads base info for a user
        :param user_identifier: can either be the username 'Max Mustermann' or an id '16' or a guid '(5330D865-5082-1CF3-B58A-75CCAEAB9B26)'
        :return: List of dataclasses of type UserName or None if one of the users does not exist.
        """
        body = BRequestIXServicePortIFGetUserNames(
            ids=list(user_identifier),
            checkout_users_z=CHECKOUT_USERS_Z_ALL_BY_ID
        )
        res: Response[BResult1001617329] = ix_service_port_if_get_user_names.sync_detailed(
            client=self.elo_client,
            body=body
        )
        userNotExistLog = '[ELOIX:5023]Unknown user or key;'
        # check if this string is contained in the non parsed response
        if userNotExistLog in res.content.decode('utf-8'):
            return None
        _check_response(res)
        return res.parsed.result

    def get_user_details(self, user_identifier: str) -> UserInfo:
        """
        Loads the user details.
        :param user_identifier:id or guid
        :return:
        """
        body = BRequestIXServicePortIFCheckoutUser(
            id=user_identifier,
            checkout_users_z=CHECKOUT_USERS_Z_ALL_BY_ID,
            lock_z=LOCK_Z_NO
        )
        res: Response[BResult1485735592] = ix_service_port_if_checkout_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        return res.parsed.result

    def update_user_details(self, user_info: UserInfo) -> int:
        """
        Saves the user details.
        :param user_info: UserInfo object
        :return: userid
        """
        body = BRequestIXServicePortIFCheckinUser(
            user_info=user_info,
            checkin_users_z=CHECKIN_USER_UPDATE
        )
        res: Response[BResult5] = ix_service_port_if_checkin_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        return res.parsed.result

    def create_user(self, user_info: UserInfo) -> int:
        """
        Creates a new user

        The following attributes are set
        * name
        * pwd
        * desc
        * group_list
        * internal_user
        * superior_id
        * user_props
        * ldap_properties
        * flags
        * flags2

        rights if 'flag2' is not set we automatically set it to 5 which means:
            # FLAG2_VISIBLE_USER = 4;
            # FLAG2_INTERACTIVE_LOGIN = 1

        rights if 'flag' is not set we automatically set it to 0 which means:
            # default allow nothing

        user_props: the order defines what property is set. Important you can either set None property or a list with 7
        properties! Otherwise, the server throws an ArrayIndexOutOfBoundsException.
        prop[0] = Windows NET User
        prop[1] = email address
        prop[2] = "Eigenschaft 5"
        prop[3] = "Aktion"
        prop[4] = "Eigenschaft 1"
        prop[5] = "Eigenschaft 2"
        prop[6] = "Eigenschaft 3"
        prop[7] = "Eigenschaft 4"

        ldap_properties:
            "givenname":
            "extensionattribute3":
            "extensionattribute2":
            "sn":
            "samaccountname":
            "manager":
            "department":

        :param user_info: UserInfo object
        :return: guid of user
        """
        body = BRequestIXServicePortIFCreateUser()
        res: Response[BResult1485735592] = ix_service_port_if_create_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        new_user_info = self._init_user_info(res, user_info)

        body = BRequestIXServicePortIFCheckinUser(
            user_info=new_user_info,
            checkin_users_z=CHECKIN_USER_CREATE
        )
        res: Response[BResult5] = ix_service_port_if_checkin_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        return res.parsed.result

    def delete_user(self, user_identifier: str):
        """
        Deletes a user
        :param user_identifier: id or guid
        """
        body = BRequestIXServicePortIFDeleteUser(
            id=user_identifier,
            unlock_z=LOCK_Z_NO
        )
        res: Response[BResult19] = ix_service_port_if_delete_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)

    def delete_group(self, group_identifier: str):
        """
        Deletes a group
        :param group_identifier: id or guid
        """
        # ELO does not differentiate between deleting a user or a group
        self.delete_user(group_identifier)

    def create_group(self, group_info: UserInfo) -> int:
        """
        Creates a new group

        The following attributes are set
        * name
        * desc
        * group_list
        * user_props
        * flags
        * flags2

        rights if 'flag2' is not set we automatically set it to 4 which means:
           # FLAG2_VISIBLE_USER = 4;

        rights if 'flag' is not set we automatically set it to 0 which means:
            # default allow nothing

        user_props: the order defines what property is set. Important you can either set None property or a list with 7 properties! Otherwise, the server throws an ArrayIndexOutOfBoundsException.
        prop[0] = Unknown
        prop[1] = email address
        prop[2] = "Eigenschaft 5"
        prop[3] = Unknown
        prop[4] = "Eigenschaft 1"
        prop[5] = "Eigenschaft 2"
        prop[6] = "Eigenschaft 3"
        prop[7] = "Eigenschaft 4"

        :param group_info: GroupInfo object
        :return: guid of group
        """
        body = BRequestIXServicePortIFCreateUser()
        res: Response[BResult1485735592] = ix_service_port_if_create_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        new_user_info = self._init_group_info(res, group_info)

        body = BRequestIXServicePortIFCheckinUser(
            user_info=new_user_info,
            checkin_users_z=CHECKIN_USER_CREATE,
        )
        res: Response[BResult5] = ix_service_port_if_checkin_user.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        return res.parsed.result

    def _init_user_info(self, res, user_info):
        new_user_info: UserInfo = res.parsed.result
        new_user_info.name = user_info.name
        new_user_info.pwd = user_info.pwd
        new_user_info.desc = user_info.desc
        new_user_info.group_list = user_info.group_list
        new_user_info.internal_user = user_info.internal_user
        new_user_info.superior_id = user_info.superior_id

        self._set_user_props(new_user_info, user_info)
        self._set_ldap_props(new_user_info, user_info)

        new_user_info.type = 1  # 1 = user, 0 = group
        if user_info.flags2 is None or type(user_info.flags2) is Unset:
            # FLAG2_VISIBLE_USER = 4;
            # FLAG2_INTERACTIVE_LOGIN = 1
            # default allow this
            new_user_info.flags2 = 5
        else:
            new_user_info.flags2 = user_info.flags2

        if user_info.flags is None or type(user_info.flags2) is Unset:
            # default allow nothing
            new_user_info.flags = 0
        else:
            new_user_info.flags = user_info.flags
        return new_user_info

    def _set_user_props(self, new_user_info, user_info):
        if type(user_info.user_props) == list and len(user_info.user_props) != 8:
            user_info.user_props = user_info.user_props[:8]
            actual_len = len(user_info.user_props)
            missing = 8 - actual_len
            if missing > 0:
                for i in range(missing):
                    user_info.user_props.append("")
        new_user_info.user_props = user_info.user_props

    def _set_ldap_props(self, new_user_info, user_info):
        if (
            user_info.ldap_properties is not Unset
            and isinstance(user_info.ldap_properties, MapToString)
        ):
            for key in user_info.ldap_properties.additional_keys:
                new_user_info.ldap_properties[key] = user_info.ldap_properties[key]

    def _init_group_info(self, res, group_info):
        new_group_info: UserInfo = res.parsed.result
        new_group_info.name = group_info.name
        new_group_info.desc = group_info.desc
        new_group_info.group_list = group_info.group_list

        self._set_user_props(new_group_info, group_info)

        new_group_info.type = 0  # 1 = user, 0 = group
        if group_info.flags2 is None or type(group_info.flags2) is Unset:
            # default allow nothing
            # FLAG2_VISIBLE_USER = 4;
            new_group_info.flags2 = 4
        else:
            new_group_info.flags2 = group_info.flags2

        if group_info.flags is None or type(group_info.flags2) is Unset:
            # default allow nothing
            new_group_info.flags = 0
        else:
            new_group_info.flags = group_info.flags
        return new_group_info

    def get_group_base(self, *group_identifier: str) -> [UserName]:
        """
        Loads base info for a user
        :param user_identifier: can either be the groupname 'Verwaltung' or an id '16' or a guid '(5330D865-5082-1CF3-B58A-75CCAEAB9B26)'
        :return: List of dataclasses of type UserName or None if one of the groups does not exist.
        """
        body = BRequestIXServicePortIFGetUserNames(
            ids=list(group_identifier),
            checkout_users_z=CHECKOUT_USERS_Z_ALL_BY_ID
        )
        res: Response[BResult1001617329] = ix_service_port_if_get_user_names.sync_detailed(
            client=self.elo_client,
            body=body
        )
        userNotExistLog = '[ELOIX:5023]Unknown user or key;'
        # check if this string is contained in the non parsed response
        if userNotExistLog in res.content.decode('utf-8'):
            return None
        _check_response(res)
        return res.parsed.result

    def get_group_details(self, group_identifier: str) -> UserInfo:
        """
        Loads the group details.
        :param group_identifier: id or guid
        :return:
        """
        return self.get_user_details(group_identifier)

    def get_group_members(self, group_identifier: str) -> list[UserInfo]:
        """
        Loads all members of a given group.
        :param group_identifier: id or guid of the group
        :return: List of UserInfo objects representing group members
        """
        body = BRequestIXServicePortIFCheckoutUsers(
            ids=[group_identifier],
            checkout_users_z=CHECKOUT_USERS_Z_MEMBERS_OF_GROUP,
            lock_z=LOCK_Z_NO
        )
        res: Response[BResult1132956238] = ix_service_port_if_checkout_users.sync_detailed(
            client=self.elo_client,
            body=body
        )
        _check_response(res)
        return res.parsed.result

    def user_add_to_group(self, user_identifier: str, group_identifier: str):
        """
        Adds a user to a group
        :param user_identifier: id or guid
        :param group_identifier: id or guid
        """
        # we retrieve the user details in order to make sure we have the ID and not the GUID
        user = self.get_user_details(user_identifier)
        group = self.get_group_details(group_identifier)

        if user.group_list is None or type(user.group_list) is Unset:
            user.group_list = []
        if group.id in user.group_list:
            logging.warning(f"User {user.name} is already in group {group.name} skipping")
            return

        user.group_list.append(group.id)
        self.update_user_details(user)

    def user_remove_from_group(self, user_identifier: str, group_identifier: str):
        """
        Removes a user from a group
        :param user_identifier: id or guid
        :param group_identifier: id or guid
        """
        # we retrieve the user details in order to make sure we have the ID and not the GUID
        user = self.get_user_details(user_identifier)
        group = self.get_group_details(group_identifier)

        if user.group_list is None or type(user.group_list) is Unset:
            user.group_list = []
        if group.id not in user.group_list:
            logging.warning(f"User {user.name} is not in group {group.name} skipping")
            return

        user.group_list.remove(group.id)
        self.update_user_details(user)
