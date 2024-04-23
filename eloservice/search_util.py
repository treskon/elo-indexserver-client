import logging

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_find_first_sords
from eloclient.models import FindInfo, FindByIndex, ObjKey, FindOptions, BRequestIXServicePortIFFindFirstSords, SordZ, \
    SordC
from eloclient.types import Unset
from eloservice.login_util import EloConnection


class SearchUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def search(self, search_mask_fields: dict = None, search_mask_id: str = None,
               max_results: int = 100
               ) -> [str]:
        """
        This function searches for objects that match all the given metadata
        :param search_mask_fields: The metadata that should be searched for (default = None)
        :param search_mask_id: The maskID of the mask that should be searched (default = None)
        :param max_results:  The maximum number of results that should be returned (default = 100)
        :return: The sordIDs of the found objects
        """
        find_info = FindInfo()
        find_by_index = FindByIndex()
        find_info.find_by_index = find_by_index

        if search_mask_fields is not None:
            obj_keys = []
            for key, value in search_mask_fields.items():
                obj_key = ObjKey()
                obj_key.name = key
                obj_key.data = [value]
                obj_keys.append(obj_key)
            find_by_index.obj_keys = obj_keys

        if search_mask_id is not None:
            find_by_index.mask_id = search_mask_id

        find_options = FindOptions()
        find_options.total_count = max_results
        find_info.find_options = find_options

        body = BRequestIXServicePortIFFindFirstSords(
           
            find_info=find_info,
            max_=max_results,
            sord_z=SordZ(SordC().mb_only_id)
        )

        res = ix_service_port_if_find_first_sords.sync_detailed(client=self.elo_client, body=body)
        if (res.parsed is None) or (res.parsed.result is None) or isinstance(res.parsed.result, Unset):
            logging.warning(f"No results found got exception {res.content}")
            return []
        return res.parsed.result.ids
