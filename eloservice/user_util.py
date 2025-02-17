from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_get_user_names, ix_service_port_if_checkout_user, \
    ix_service_port_if_checkin_user
from eloclient.models import BRequestIXServicePortIFGetUserNames, BResult1001617329, UserName, \
    BRequestIXServicePortIFCheckoutUser, BResult1485735592, UserInfo, BRequestIXServicePortIFCheckinUser, BResult5
from eloclient.types import Response
from eloservice.eloconstants import CHECKOUT_USERS_Z_ALL_BY_ID, LOCK_Z_NO, CHECKIN_USER_UPDATE
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
        body = BRequestIXServicePortIFGetUserNames(ids=list(user_identifier),
                                                   checkout_users_z=CHECKOUT_USERS_Z_ALL_BY_ID)
        res: Response[BResult1001617329] = ix_service_port_if_get_user_names.sync_detailed(client=self.elo_client,
                                                                                           body=body)
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
        res: Response[BResult1485735592] = ix_service_port_if_checkout_user.sync_detailed(client=self.elo_client,
                                                                                          body=body)
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
            checkin_users_z=CHECKIN_USER_UPDATE,
        )
        res: Response[BResult5] = ix_service_port_if_checkin_user.sync_detailed(client=self.elo_client,
                                                                                body=body)
        _check_response(res)
        return res.parsed.result

    # TODO we do not know currently how to create a new user
    # there is a method but it does not create a valid user and only delivers a guid that can not be used for further operations

    # def create_new_user(self):
    #     """
    #     Creates a new user
    #     :param user_info: UserInfo object
    #     :return: guid of user
    #     """
    #     body = BRequestIXServicePortIFCreateUser()
    #     res: Response[BResult1485735592] = ix_service_port_if_create_user.sync_detailed(client=self.elo_client,
    #                                                                                     body=body)
    #     _check_response(res)
    #     return res.parsed.result.guid

    def get_group_base(self, *group_identifier: str) -> [UserName]:
        """
        Loads base info for a user
        :param user_identifier: can either be the groupname 'Verwaltung' or an id '16' or a guid '(5330D865-5082-1CF3-B58A-75CCAEAB9B26)'
        :return: List of dataclasses of type UserName or None if one of the groups does not exist.
        """
        body = BRequestIXServicePortIFGetUserNames(ids=list(group_identifier),
                                                   checkout_users_z=CHECKOUT_USERS_Z_ALL_BY_ID)
        res: Response[BResult1001617329] = ix_service_port_if_get_user_names.sync_detailed(client=self.elo_client,
                                                                                           body=body)
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
