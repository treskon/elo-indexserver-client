import base64
import logging
from typing import Type

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_checkin_map, ix_service_port_if_checkout_map
from eloclient.models import BRequestIXServicePortIFCheckinMap, KeyValue, MapValue, FileData
from eloclient.models import BRequestIXServicePortIFCheckoutMap, LockZ, LockC
from eloclient.types import Unset
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


def _convert_key_value(key: str, value: str) -> KeyValue:
    key_value = KeyValue()
    key_value.key = key
    key_value.value = value
    return key_value


def _convert_map_value(key: str, value: str, content_type) -> MapValue:
    map_value = MapValue()
    map_value.key = key

    file_data = FileData()
    file_data.content_type = content_type
    file_data.data = to_base64(value)  # according to docs 'File data as byte array.'
    map_value.blob_value = file_data
    return map_value


def _convert_map_value_blob(key: str, value: object, content_type) -> MapValue:
    # detect if value is a filepath or bytes
    if isinstance(value, str):
        with open(value, "rb") as file:
            value_bytes: bytes = file.read()
    elif isinstance(value, bytes):
        value_bytes: bytes = value
    else:
        raise ValueError("Value must be a either a string (filepath) or bytes")

    map_value = MapValue()
    map_value.key = key

    file_data = FileData()
    file_data.content_type = content_type
    file_data.data = to_base64_bytes(value_bytes)  # according to docs 'File data as byte array.'
    map_value.blob_value = file_data
    return map_value


def to_base64(value: str):
    return to_base64_bytes(value.encode("ISO_8859_1"))


def to_base64_bytes(value: bytes):
    # We have to encode toBase64 according to
    # https://github.com/wolfgangimig/byps/blob/7521b79e39df2e577821c6fa37487c24757385e7/java/bypshttp/src/byps/http/rest/BytesSerializer.java#L29
    # and in Java 'Base64.getDecoder().decode(base64) uses 'ISO_8859_1'
    base64_bytes = base64.b64encode(value)
    return base64_bytes.decode("ISO_8859_1")


def too_large_for_string(fields: dict):
    for key, value in fields.items():
        if len(key) > 255 or len(value) > 255:
            logging.warning(f"Key or value too large for string: {key} {value}")
            return True
    return False

class MapUtil:
    class ValueType:
        string = "string"
        blob_string = "blob_string"
        blob_file = "blob_file"

    class MapValue:
        type: Type['MapUtil.ValueType']
        value: str
        mime_type: str
        blob_value: bytes

    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def write_map_fields(self, sord_id: str, fields: dict, map_domain: str = "Objekte",
                         value_type: ValueType = ValueType.string,
                         content_type="text/plain; charset=ISO_8859_1"):
        if value_type == MapUtil.ValueType.string and too_large_for_string(fields):
            logging.warning("Fields too large for string, using blob_string instead")
            value_type = MapUtil.ValueType.blob_string

        if value_type == MapUtil.ValueType.string:
            self._write_map_field_string(sord_id, map_domain, fields)
        elif value_type == MapUtil.ValueType.blob_string:
            self._write_map_field_blob_string(sord_id, map_domain, fields, content_type)
        else:
            self._write_map_field_blob_file(sord_id, map_domain, fields, content_type)

    def _write_map_field_string(self, sord_id, map_domain, fields: dict):

        body = BRequestIXServicePortIFCheckinMap(
            domain_name=map_domain,
            id=sord_id,
            obj_id=sord_id,
            data=[_convert_key_value(key, value) for key, value in fields.items()]
        )
        res = ix_service_port_if_checkin_map.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)

    def _write_map_field_blob_string(self, sord_id, map_domain, fields: dict, content_type):
        body = BRequestIXServicePortIFCheckinMap(
            domain_name=map_domain,
            id=sord_id,
            obj_id=sord_id,
            data=[_convert_map_value(key, value, content_type) for key, value in fields.items()]
        )
        res = ix_service_port_if_checkin_map.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)

    def _write_map_field_blob_file(self, sord_id, map_domain, fields, content_type):
        body = BRequestIXServicePortIFCheckinMap(
            domain_name=map_domain,
            id=sord_id,
            obj_id=sord_id,
            data=[_convert_map_value_blob(key, value, content_type) for key, value in fields.items()]
        )
        res = ix_service_port_if_checkin_map.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)

    def read_map_fields(self, sord_id: str, keys: list[str] = None, map_domain: str = "Objekte") -> dict[str, MapValue]:
        if not keys or len(keys) == 0:
            keys = None
        body = BRequestIXServicePortIFCheckoutMap(
            domain_name=map_domain,
            id=sord_id,
            key_names=keys, # if keys is None, all fields are read
            lock_z=LockZ(LockC().bset_no)
        )
        res = ix_service_port_if_checkout_map.sync_detailed(client=self.elo_client, body=body)
        _check_response(res)
        return self._process_checkout_map(res, sord_id)

    def _process_checkout_map(self, res, sord_id):
        map_items = res.parsed.result.map_items
        map_items_keys = map_items.additional_keys
        result: dict[str, MapValue] = {}
        for map_key in map_items_keys:
            map_item = map_items.additional_properties[map_key]  # type: MapValue
            if not map_item and not isinstance(map_item, Unset):
                logging.debug(f"Skipping map item with key {map_key} on sord with ID {sord_id}")
            result[map_key] = self._process_map_item(map_item, map_key, sord_id)
        return result

    def _process_map_item(self, map_item, map_key, sord_id) -> MapValue:
        map_value = MapUtil.MapValue()
        # Order is important: if blob_value is set, it will be used instead of value, sometimes value is filled with
        # an empty string
        if 'value' in set(map_item.additional_keys):
            map_value.type = MapUtil.ValueType.string
            map_value.key = map_key
            map_value.value = map_item.additional_properties['value']
        if map_item.blob_value and not isinstance(map_item.blob_value, Unset):
            map_value.type = MapUtil.ValueType.blob_file
            map_value.key = map_key
            map_value.value = map_item.blob_value.stream.url
            map_value.mime_type = map_item.blob_value.content_type
            try:
                map_value.blob_value = self._load_file_from_stream(map_value.value)
                map_value.value = None
            except ValueError as e:
                logging.warning(f"Could not load file from stream {map_value.value}: {e} sordID {sord_id}")
            if map_value.blob_value:
                if isinstance(map_value.blob_value, bytes):
                    map_value.type = MapUtil.ValueType.blob_file
                    map_value.value = None
                elif isinstance(map_value.blob_value, str):
                    map_value.type = MapUtil.ValueType.blob_string
                    map_value.value = map_value.blob_value
        return map_value

    def _load_file_from_stream(self, stream_url: str) -> bytes:
        full_url = self.elo_connection.url + ("/" if self.elo_connection.url[-1] != "/" else "") + stream_url
        res = self.elo_client.get_httpx_client().get(full_url)
        if res.status_code != 200:
            raise ValueError(f"Could not load file from stream {stream_url}")
        return res.content

