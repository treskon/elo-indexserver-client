import logging

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_create_sord, \
    ix_service_port_if_checkin_sord, ix_service_port_if_checkout_sord
from eloclient.models import BRequestIXServicePortIFCheckinSord, BRequestIXServicePortIFCreateSord, \
    BRequestIXServicePortIFCheckoutSord
from eloclient.models import MaskName, DocMask, EditInfoC, EditInfoZ, SordZ, SordC, LockZ, LockC, Sord, ObjKey
from eloservice import eloconstants as elo_const
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


class MaskUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def get_all_masks_names(self) -> [MaskName]:
        # When creating a new Sord, the mask names are returned in the response, as we do not checkin the sord
        # afterward, nothing is saved. This is a workaround to get the mask names from ELO IX server
        body = BRequestIXServicePortIFCreateSord(
           
            parent_id="0",  # "0" (--> root folder in ELO)
            mask_id="0",  # "0" (--> mask "Freie Eingabe" = STD mask)
            edit_info_z=elo_const.EDIT_INFO_Z_MASK_NAMES
        )

        res = ix_service_port_if_create_sord.sync_detailed(client=self.elo_client, json_body=body)

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

    def get_mask_detail(self, mask_id) -> DocMask:
        # When creating a new Sord, with the correct mask_id we get the DocMask Object as a result.
        # This is a workaround to get the mask details from ELO IX server
        body = BRequestIXServicePortIFCreateSord(
           
            parent_id="0",  # "0" (--> root folder in ELO)
            mask_id=mask_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL
        )

        res = ix_service_port_if_create_sord.sync_detailed(client=self.elo_client, json_body=body)
        _check_response(res)
        return res.parsed.result.mask

    def overwrite_mask_fields(self, sord_id: str, mask_name: str, metadata: dict):
        mask = self.get_mask_name(mask_name)
        if mask is None:
            raise ValueError(f"Mask '{mask_name}' not found in ELO")
        doc_mask = self.get_mask_detail(mask.id)

        lockZ = LockZ(LockC().yes)
        body = BRequestIXServicePortIFCheckoutSord(
           
            obj_id=sord_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL,
            lock_z=lockZ
        )
        erg = ix_service_port_if_checkout_sord.sync_detailed(client=self.elo_client, json_body=body)
        old_sord: Sord = erg.parsed.result.sord

        old_sord.mask = mask.id
        old_sord.mask_name = mask.name
        old_sord.obj_keys = []
        for key, value in metadata.items():
            try:
                key_id = self._get_objKey_id(doc_mask, key)
                old_sord.obj_keys.append(ObjKey(data=[value], obj_id=sord_id, name=key,
                                                id=key_id))
            except ValueError:
                logging.warning(f"Could not find key '{key}' in mask '{mask.name}', ignoring property and continuing")

            body = BRequestIXServicePortIFCheckinSord(
               
                sord=old_sord,
                sord_z=SordZ(bset=elo_const.ElobitsetEditz.MB_ALL.value),
                unlock_z=LockZ(LockC().bset_yes)
            )
            erg = ix_service_port_if_checkin_sord.sync_detailed(client=self.elo_client, json_body=body)

        _check_response(erg)

    def get_mask_name(self, mask_name):
        masks: [MaskName] = self.get_all_masks_names()
        mask: MaskName = next((m for m in masks if m.name == mask_name), None)
        return mask

