import logging

from cachetools import cached, TTLCache

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_create_sord, \
    ix_service_port_if_checkin_sord
from eloclient.models import BRequestIXServicePortIFCheckinSord, BRequestIXServicePortIFCreateSord
from eloclient.models import MaskName, DocMask, Sord, ObjKey
from eloservice import eloconstants as elo_const
from eloservice.eloconstants import SordZ_INFO_MB_MASK_INFOS, LOCK_Z_NO
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


class MaskUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    # Cache the mask names for 10 minutes
    @cached(cache=TTLCache(maxsize=128, ttl=600))
    def get_all_masks_names(self) -> [MaskName]:
        logging.debug("Getting all mask names")
        # When creating a new Sord, the mask names are returned in the response, as we do not checkin the sord
        # afterward, nothing is saved. This is a workaround to get the mask names from ELO IX server
        body = BRequestIXServicePortIFCreateSord(

            parent_id="0",  # "0" (--> root folder in ELO)
            mask_id="0",  # "0" (--> mask "Freie Eingabe" = STD mask)
            edit_info_z=elo_const.EDIT_INFO_Z_MASK_NAMES
        )

        res = ix_service_port_if_create_sord.sync_detailed(client=self.elo_client, body=body)

        _check_response(res)

        read_access = 1  # = AccessC().lur_read => Access control right for reading an archive entry

        available_elomasks: [MaskName] = [
            mn for mn in res.parsed.result.mask_names
            if mn.access >= read_access
        ]

        return available_elomasks

    def _get_objKey_id(self, doc_mask: DocMask, key: str):
        for line in doc_mask.lines:
            if line.key == key:
                return line.id
        raise ValueError(f"Could not find key '{key}' in mask '{doc_mask.name}'")

    # Cache the mask details for 10 minutes
    @cached(cache=TTLCache(maxsize=128, ttl=600))
    def get_mask_detail(self, mask_id) -> DocMask:
        # When creating a new Sord, with the correct mask_id we get the DocMask Object as a result.
        # This is a workaround to get the mask details from ELO IX server
        logging.debug(f"Getting mask details for mask_id {mask_id}")
        body = BRequestIXServicePortIFCreateSord(

            parent_id="0",  # "0" (--> root folder in ELO)
            mask_id=mask_id,
            # TODO use the correct edit_info_z not MB_ALL
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL
        )

        res = ix_service_port_if_create_sord.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        return res.parsed.result.mask

    def overwrite_mask_fields(self, sord_id: str, mask_name: str, metadata: dict):
        sord = self.create_local_sord(mask_name, metadata, sord_id)
        body = BRequestIXServicePortIFCheckinSord(
            sord=sord,
            sord_z=SordZ_INFO_MB_MASK_INFOS,
            unlock_z=LOCK_Z_NO
        )
        erg = ix_service_port_if_checkin_sord.sync_detailed(client=self.elo_client, body=body)
        _check_response(erg)

    def create_local_sord(self, mask_name, metadata, sord_id):
        mask = self.get_mask_name(mask_name)
        if mask is None:
            raise ValueError(f"Mask '{mask_name}' not found in ELO")
        doc_mask = self.get_mask_detail(mask.id)
        sord: Sord = Sord(
            id=sord_id,
            mask_name=mask.name,
            mask=mask.id,
            obj_keys=[]
        )
        for key, value in metadata.items():
            try:
                key_id = self._get_objKey_id(doc_mask, key)
                sord.obj_keys.append(ObjKey(data=[value], obj_id=sord_id, name=key,
                                            id=key_id))
            except ValueError:
                logging.warning(f"Could not find key '{key}' in mask '{mask.name}', ignoring property and continuing")
        return sord

    def get_mask_name(self, mask_name):
        masks: [MaskName] = self.get_all_masks_names()
        mask: MaskName = next((m for m in masks if m.name == mask_name), None)
        return mask
