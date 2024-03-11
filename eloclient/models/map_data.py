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
        domain_name (Union[Unset, str]): Map domain name. An arbitary name or one of the predefined names in MapDomainC.
        id (Union[Unset, str]): Map ID. If the map belongs to a Sord ID, this value is equal to the member objId.
        obj_id (Union[Unset, int]): Object ID. The ID of the associated Sord object or 0, if the map does not belong to
            a Sord object.
        lock_id (Union[Unset, int]): User ID of the user that owns the lock on the map. If the map is not locked, this
            value is -1.
        lock_name (Union[Unset, str]): User name of the user that owns the lock no the map. If the map is not locked,
            this value is an empty string.
        t_stamp (Union[Unset, str]): Timestamp
        items (Union[Unset, List['KeyValue']]):
        guid (Union[Unset, str]): GUID
        map_items (Union[Unset, MapToMapValue]):
    """

    domain_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    items: Union[Unset, List["KeyValue"]] = UNSET
    guid: Union[Unset, str] = UNSET
    map_items: Union[Unset, "MapToMapValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_name = self.domain_name
        id = self.id
        obj_id = self.obj_id
        lock_id = self.lock_id
        lock_name = self.lock_name
        t_stamp = self.t_stamp
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        guid = self.guid
        map_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_items, Unset):
            map_items = self.map_items.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if id is not UNSET:
            field_dict["id"] = id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if items is not UNSET:
            field_dict["items"] = items
        if guid is not UNSET:
            field_dict["guid"] = guid
        if map_items is not UNSET:
            field_dict["mapItems"] = map_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_value import KeyValue
        from ..models.map_to_map_value import MapToMapValue

        d = src_dict.copy()
        domain_name = d.pop("domainName", UNSET)

        id = d.pop("id", UNSET)

        obj_id = d.pop("objId", UNSET)

        lock_id = d.pop("lockId", UNSET)

        lock_name = d.pop("lockName", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = KeyValue.from_dict(items_item_data)

            items.append(items_item)

        guid = d.pop("guid", UNSET)

        _map_items = d.pop("mapItems", UNSET)
        map_items: Union[Unset, MapToMapValue]
        if isinstance(_map_items, Unset):
            map_items = UNSET
        else:
            map_items = MapToMapValue.from_dict(_map_items)

        map_data = cls(
            domain_name=domain_name,
            id=id,
            obj_id=obj_id,
            lock_id=lock_id,
            lock_name=lock_name,
            t_stamp=t_stamp,
            items=items,
            guid=guid,
            map_items=map_items,
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
