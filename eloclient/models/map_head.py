from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapHead")


@_attrs_define
class MapHead:
    """Internal class.

    Attributes:
        lock_id (Union[Unset, int]): Lock status. -1: unlocked, &gt;=0 user-ID.
        t_stamp (Union[Unset, str]): Timestamp.
        t_stamp_sync (Union[Unset, str]): EIX-3097: TimeStampSync
        obj_id (Union[Unset, int]): Associated object ID or 0.
        guid (Union[Unset, str]): GUID.
        id (Union[Unset, str]): Map id.
    """

    lock_id: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lock_id = self.lock_id

        t_stamp = self.t_stamp

        t_stamp_sync = self.t_stamp_sync

        obj_id = self.obj_id

        guid = self.guid

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lock_id = d.pop("lockId", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        obj_id = d.pop("objId", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        map_head = cls(
            lock_id=lock_id,
            t_stamp=t_stamp,
            t_stamp_sync=t_stamp_sync,
            obj_id=obj_id,
            guid=guid,
            id=id,
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
