import logging
from datetime import datetime

import cachetools
from decimal import Decimal

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_create_sord, \
    ix_service_port_if_checkin_sord, ix_service_port_if_checkout_sord
from eloclient.models import BRequestIXServicePortIFCheckinSord, BRequestIXServicePortIFCreateSord, \
    BRequestIXServicePortIFCheckoutSord, LockZ, LockC
from eloclient.models import MaskName, DocMask, Sord, ObjKey
from eloservice import eloconstants as elo_const
from eloservice.eloconstants import SordZ_INFO_MB_MASK_INFOS, LOCK_Z_NO
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


class MaskUtil:
    elo_connection: EloConnection
    elo_client: Client
    # we can't use decorators for caching as we want it to be configurable
    cache_get_all_masks_names: cachetools.TTLCache = None
    cache_get_mask_detail: cachetools.TTLCache = None

    def __init__(self, elo_client: Client, elo_connection: EloConnection,
                 cache_enable: bool = True, cache_ttl: int = 600, cache_maxsize: int = 128):
        self.elo_connection = elo_connection
        self.elo_client = elo_client
        if cache_enable:
            logging.debug("Caching enabled")
            self.cache_get_all_masks_names = cachetools.TTLCache(maxsize=1, ttl=cache_ttl)  # only one entry in cache
            self.cache_get_mask_detail = cachetools.TTLCache(maxsize=cache_maxsize, ttl=cache_ttl)

    def get_all_masks_names(self) -> [MaskName]:
        cache_key = "get_all_masks_names"
        if self.cache_get_all_masks_names is not None:
            logging.debug("Using cache")
            if cache_key in self.cache_get_all_masks_names:
                logging.debug("Cache hit")
                return self.cache_get_all_masks_names[cache_key]
            else:
                logging.debug("Cache miss")
                masks = self._get_all_masks_names()
                self.cache_get_all_masks_names[cache_key] = masks
                return masks
        else:
            return self._get_all_masks_names()

    def _get_all_masks_names(self) -> [MaskName]:
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

    def get_mask_detail(self, mask_id) -> DocMask:
        cache_key = f"get_mask_detail_{mask_id}"
        if self.cache_get_mask_detail is not None:
            logging.debug("Using cache")
            if cache_key in self.cache_get_mask_detail:
                logging.debug("Cache hit")
                return self.cache_get_mask_detail[cache_key]
            else:
                logging.debug("Cache miss")
                mask = self._get_mask_detail(mask_id)
                self.cache_get_mask_detail[cache_key] = mask
                return mask
        else:
            return self._get_mask_detail(mask_id)

    def _get_mask_detail(self, mask_id) -> DocMask:
        # When creating a new Sord, with the correct mask_id we get the DocMask Object as a result.
        # This is a workaround to get the mask details from ELO IX server
        logging.debug(f"Getting mask details for mask_id {mask_id}")
        body = BRequestIXServicePortIFCreateSord(

            parent_id="0",  # "0" (--> root folder in ELO)
            mask_id=mask_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL
        )

        res = ix_service_port_if_create_sord.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        return res.parsed.result.mask

    def overwrite_mask_fields(self, sord_id: str, mask_name: str, metadata: dict, metadata_force: dict = None):
        sord = self._create_local_sord(mask_name, metadata, sord_id, metadata_force)
        body = BRequestIXServicePortIFCheckinSord(
            sord=sord,
            sord_z=SordZ_INFO_MB_MASK_INFOS,
            unlock_z=LOCK_Z_NO
        )
        erg = ix_service_port_if_checkin_sord.sync_detailed(client=self.elo_client, body=body)
        _check_response(erg)

    def _create_local_sord(self, mask_name, metadata, sord_id, metadata_force=None):
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

        if metadata_force is not None:
            for key, value in metadata_force.items():
                sord.obj_keys.append(ObjKey(data=[value], obj_id=sord_id, name=key,
                                            id=key))

        return sord

    def get_mask_name(self, mask_name):
        masks: [MaskName] = self.get_all_masks_names()
        mask: MaskName = next((m for m in masks if m.name == mask_name), None)
        return mask

    def get_mask_fields(self, sord_id) -> dict:
        """
        Get all fields for a certain sord_id. The values are casted according to the configured mask line types.
        :param sord_id:
        :return:
        """
        body = BRequestIXServicePortIFCheckoutSord(
            obj_id=sord_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL,
            lock_z=LOCK_Z_NO
        )
        res = ix_service_port_if_checkout_sord.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        if type(res.parsed.result.sord) is not Sord:
            raise ValueError(f"Sord with ID {sord_id} not found")
        sord:Sord = res.parsed.result.sord
        doc_mask:DocMask = self.get_mask_detail(sord.mask)
        erg = {obj_key.name: self._cast_obj_key(obj_key, doc_mask) for obj_key in sord.obj_keys}
        return erg

    def _get_mask_field_type(self,obj_key:ObjKey, doc_mask:DocMask) -> str:
        for line in doc_mask.lines:
            if line.key == obj_key.name:
                 return self._translate_obj_type_nr_to_str(line.type)
        logging.warning(f"Could not find key '{obj_key.name}' in mask '{doc_mask.name}'")
        return "Not implemented"

    def _cast_obj_key(self, obj_key:ObjKey, doc_mask:DocMask):
        if len(obj_key.data) == 0:
            return None
        obj_type = self._get_mask_field_type(obj_key, doc_mask)
        if obj_type == "TYPE_TEXT":
            return obj_key.data[0]
        elif obj_type == "TYPE_DATE":
            return self._parse_date(obj_key)
        elif obj_type == "TYPE_NUMBER":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_AZ":
            return obj_key.data[0]
        elif obj_type == "TYPE_ISO_DATE":
            return self._parse_date(obj_key)
        elif obj_type == "TYPE_LIST":
            return obj_key.data
        elif obj_type == "TYPE_USER":
            # todo idk, maybe userID ?
            return obj_key.data[0]
        elif obj_type == "TYPE_THES":
            # todo
            return obj_key.data[0]
        elif obj_type == "TYPE_NUMBER_F0":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_NUMBER_F1":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_NUMBER_F2":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_NUMBER_F4":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_NUMBER_F6":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_INTEGER":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_LONG":
            return Decimal(obj_key.data[0])
        elif obj_type == "TYPE_FLOAT":
            return float(obj_key.data[0])
        elif obj_type == "TYPE_DOUBLE":
            return float(obj_key.data[0])
        elif obj_type == "TYPE_DUMMY":
            return obj_key.data[0]
        elif obj_type == "TYPE_RELATION":
            return obj_key.data[0]
        else:
            logging.warning(f"Could not find type number '{obj_type}'")
            return obj_key.data[0]

    def _parse_date(self, obj_key):
        try:  # yyyyMMddHHmmss
            return datetime.strptime(obj_key.data[0], "%Y%m%d%H%M%S")
        except ValueError:
            pass
        try:  # yyyyMMdd
            return datetime.strptime(obj_key.data[0], "%Y%m%d")
        except ValueError:
            pass
        try:  # yyyy-MM-dd HH:mm:ss
            return datetime.strptime(obj_key.data[0], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass
        try:  # yyyy-MM-dd
            return datetime.strptime(obj_key.data[0], "%Y-%m-%d")
        except ValueError:
            pass
        try:  # yyyy-MM-ddTHH:mm:ss
            return datetime.strptime(obj_key.data[0], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            pass
        logging.warning(f"Could not parse date '{obj_key.data[0]}'")
        return obj_key.data[0]

    def _translate_obj_type_nr_to_str(self, nr:int) -> str:
        """
          /**
   * Used to check wether a correct constant is used.
   */
  public static final int _TYPE_TYPE_ID = 3000;
  /**
   * Index line contains text information.
   */
  public static final int TYPE_TEXT = _TYPE_TYPE_ID + 0;
  /**
   * Index line contains a date.
   */
  public static final int TYPE_DATE = _TYPE_TYPE_ID + 1;
  /**
   * Index line contains a number. The number is internally stored as a string
   * value without any padding. Thus it is not possible to search over an interval.
   * Use one of the TYPE_NUMBER_F* types to be able to search over intervals.
   * The number must be formatted according to the locale information of the server.
   * @see #TYPE_NUMBER_F0 TYPE_NUMBER_F0
   */
  public static final int TYPE_NUMBER = _TYPE_TYPE_ID + 2;
  /**
   * Index line contains a reference number ("Aktenzeichen").
   */
  public static final int TYPE_AZ = _TYPE_TYPE_ID + 3;
  /**
   * Index line contains a date in ISO format.
   */
  public static final int TYPE_ISO_DATE = _TYPE_TYPE_ID + 4;
  /**
   * Index line contains a list entry.
   */
  public static final int TYPE_LIST = _TYPE_TYPE_ID + 5;
  /**
   * Index line contains a user name.
   */
  public static final int TYPE_USER = _TYPE_TYPE_ID + 6;
  /**
   * Thesaurus
   */
  public static final int TYPE_THES = _TYPE_TYPE_ID + 7;
  /**
   * Index line contains a number value with an arbitrary number of fraction digits.
   * The value is internally stored with a padding of &amp; (positive numbers)
   * or @ (negative numbers). This gives the possibility to search over an interval
   * of numeric values, e. b. search for "1 ... 12" finds objects with index values 1,2,3,4,...12.
   * The number must be formatted according to the locale information given in the ClientInfo object.
   * With this type, the user is responsible to enter always the same number of fraction digits.
   * Otherwise, a search over a number range will not return the correct results.
   * The meaning of this field was changed in 8.00.032. The meaning before was a field without any fraction digits.
   * @see #TYPE_NUMBER TYPE_NUMBER
   */
  public static final int TYPE_NUMBER_F0 = _TYPE_TYPE_ID + 8;
  /**
   * Index line contains a number value with one digit after the decimal point.
   * @see #TYPE_NUMBER_F0 TYPE_NUMBER_F0
   */
  public static final int TYPE_NUMBER_F1 = _TYPE_TYPE_ID + 9;
  /**
   * Index line contains a number value with one digit after the decimal point.
   * @see #TYPE_NUMBER_F0 TYPE_NUMBER_F0
   */
  public static final int TYPE_NUMBER_F2 = _TYPE_TYPE_ID + 10;
  /**
   * Index line contains a number value of with four digits after the decimal point.
   * @see #TYPE_NUMBER_F0 TYPE_NUMBER_F0
   */
  public static final int TYPE_NUMBER_F4 = _TYPE_TYPE_ID + 11;
  /**
   * Index line contains a number value with six digits after the decimal point.
   * @see #TYPE_NUMBER_F0 TYPE_NUMBER_F0
   */
  public static final int TYPE_NUMBER_F6 = _TYPE_TYPE_ID + 12;
  /**
   * Index line contains a number value without fraction in the range of (-2^31) to (2^31)-1.
   * This type can only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}.
   * @since 9.00.039.001
   */
  public static final int TYPE_INTEGER = _TYPE_TYPE_ID + 13;
  /**
   * Index line contains a number value without fraction in the range of (-2^63) to (2^63)-1.
   * This type can only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}.
   * @since 9.00.039.001
   */
  public static final int TYPE_LONG = _TYPE_TYPE_ID + 14;
  /**
   * Index line contains a floating point number value with 7 significant digits.
   * This type can only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}.
   * To assign a value of this type to {@link ObjKey#data}, the String representation has to conform to the Float.toString() method of Java.
   * Use dot to separate the fraction part and character 'E' to prefix the exponent.
   * @since 9.00.039.001
   */
  public static final int TYPE_FLOAT = _TYPE_TYPE_ID + 15;
  /**
   * Index line contains a floating point number value with 15 significant digits.
   * This type can only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}.
   * To assign a value of this type to {@link ObjKey#data}, the String representation has to conform to the Double.toString() method of Java.
   * Use dot to separate the fraction part and character 'E' to prefix the exponent.
   * @since 9.00.039.001
   */
  public static final int TYPE_DOUBLE = _TYPE_TYPE_ID + 16;

  /**
   * Index line contains a dummy entry which should not be displayed.
   * @since 12.00.000.001
   */
  public static final int TYPE_DUMMY = _TYPE_TYPE_ID + 17;

  /**
   * Index line contains a relation.
   * A Relation consists of a {@link Sord#guid} which references a {@link Sord}.
   * with a allowed DocMask {@link DocMaskDetails#keywordingRelationAllowed}.
   * @since 12.00.000.023
   */
  public static final int TYPE_RELATION = _TYPE_TYPE_ID + 18;
  // EIX-920, EIX-918 Relationen in der Verschlagwortung
        """
        mapping = {
            3000: "TYPE_TEXT",
            3001: "TYPE_DATE",
            3002: "TYPE_NUMBER",
            3003: "TYPE_AZ",
            3004: "TYPE_ISO_DATE",
            3005: "TYPE_LIST",
            3006: "TYPE_USER",
            3007: "TYPE_THES",
            3008: "TYPE_NUMBER_F0",
            3009: "TYPE_NUMBER_F1",
            3010: "TYPE_NUMBER_F2",
            3011: "TYPE_NUMBER_F4",
            3012: "TYPE_NUMBER_F6",
            3013: "TYPE_INTEGER",
            3014: "TYPE_LONG",
            3015: "TYPE_FLOAT",
            3016: "TYPE_DOUBLE",
            3017: "TYPE_DUMMY",
            3018: "TYPE_RELATION"
        }
        res = mapping.get(nr)
        if res is None:
            raise ValueError(f"Could not find type number '{nr}'")
        return res

