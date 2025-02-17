from eloclient import Client
from eloclient.types import Response
from eloservice.eloconstants import CHECKOUT_USERS_Z_ALL_USER, CHECKOUT_USERS_Z_ALL_BY_ID
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection
from eloclient.api.ix_service_port_if import ix_service_port_if_get_user_names, ix_service_port_if_checkout_user
from eloclient.models import BRequestIXServicePortIFGetUserNames, BResult1001617329, UserName


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
        :return: List of dataclasses of type UserName
        """
        body = BRequestIXServicePortIFGetUserNames(ids=list(user_identifier),
                                                   checkout_users_z=CHECKOUT_USERS_Z_ALL_BY_ID)
        res : Response[BResult1001617329] = ix_service_port_if_get_user_names.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        return res.parsed.result
