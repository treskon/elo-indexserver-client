from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value import KeyValue
    from ..models.map_to_map_value import MapToMapValue


T = TypeVar("T", bound="MapData")


@_attrs_define
class MapData:
    """This class represents a map which contains user defined key-value pairs.

    Attributes:
        lock_id (Union[Unset, int]): User ID of the user that owns the lock on the map. If the map is not locked, this
            value is -1.
        t_stamp (Union[Unset, str]): Timestamp
        map_items (Union[Unset, MapToMapValue]):
        t_stamp_sync (Union[Unset, str]): EIX-3097 TimestampSync
        domain_name (Union[Unset, str]): Map domain name. An arbitary name or one of the predefined names in MapDomainC.
        obj_id (Union[Unset, int]): Object ID.
            The ID of the associated Sord object or 0, if the map does not belong to a Sord
             object.
        guid (Union[Unset, str]): GUID
        id (Union[Unset, str]): Map ID. If the map belongs to a Sord ID, this value is equal to the member objId.
        lock_name (Union[Unset, str]): User name of the user that owns the lock no the map.
            If the map is not locked, this value is an
             empty string.
        items (Union[Unset, List['KeyValue']]):
    """

    lock_id: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    map_items: Union[Unset, "MapToMapValue"] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    items: Union[Unset, List["KeyValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lock_id = self.lock_id

        t_stamp = self.t_stamp

        map_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_items, Unset):
            map_items = self.map_items.to_dict()

        t_stamp_sync = self.t_stamp_sync

        domain_name = self.domain_name

        obj_id = self.obj_id

        guid = self.guid

        id = self.id

        lock_name = self.lock_name

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if map_items is not UNSET:
            field_dict["mapItems"] = map_items
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_value import KeyValue
        from ..models.map_to_map_value import MapToMapValue

        d = src_dict.copy()
        lock_id = d.pop("lockId", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        _map_items = d.pop("mapItems", UNSET)
        map_items: Union[Unset, MapToMapValue]
        if isinstance(_map_items, Unset):
            map_items = UNSET
        else:
            map_items = MapToMapValue.from_dict(_map_items)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        domain_name = d.pop("domainName", UNSET)

        obj_id = d.pop("objId", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        lock_name = d.pop("lockName", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = KeyValue.from_dict(items_item_data)

            items.append(items_item)

        map_data = cls(
            lock_id=lock_id,
            t_stamp=t_stamp,
            map_items=map_items,
            t_stamp_sync=t_stamp_sync,
            domain_name=domain_name,
            obj_id=obj_id,
            guid=guid,
            id=id,
            lock_name=lock_name,
            items=items,
        )

        map_data.additional_properties = d
        return map_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
