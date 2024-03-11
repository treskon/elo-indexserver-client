from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapHead")


@_attrs_define
class MapHead:
    """Internal class.

    Attributes:
        id (Union[Unset, str]): Map id.
        lock_id (Union[Unset, int]): Lock status. -1: unlocked, &gt;=0 user-ID.
        obj_id (Union[Unset, int]): Associated object ID or 0.
        t_stamp (Union[Unset, str]): Timestamp.
        guid (Union[Unset, str]): GUID.
    """

    id: Union[Unset, str] = UNSET
    lock_id: Union[Unset, int] = UNSET
    obj_id: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        lock_id = self.lock_id
        obj_id = self.obj_id
        t_stamp = self.t_stamp
        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        lock_id = d.pop("lockId", UNSET)

        obj_id = d.pop("objId", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        guid = d.pop("guid", UNSET)

        map_head = cls(
            id=id,
            lock_id=lock_id,
            obj_id=obj_id,
            t_stamp=t_stamp,
            guid=guid,
        )

        map_head.additional_properties = d
        return map_head

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
