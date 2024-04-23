from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysDel")


@_attrs_define
class PhysDel:
    """This class represents one row in the database table physdel.
    This table contains the guids of
     physically deleted objects. Those objects can be any objects with a guid: e.g. folders,
     documents, versions, users, workflows...

        Attributes:
            t_stamp (Union[Unset, str]): The object is deleted at this timestamp. Measured in the UTC time-zone.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            guid (Union[Unset, str]): GUID of deleted object.
            type (Union[Unset, int]): Type of deleted object.
    """

    t_stamp: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp

        t_stamp_sync = self.t_stamp_sync

        guid = self.guid

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if guid is not UNSET:
            field_dict["guid"] = guid
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t_stamp = d.pop("TStamp", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        guid = d.pop("guid", UNSET)

        type = d.pop("type", UNSET)

        phys_del = cls(
            t_stamp=t_stamp,
            t_stamp_sync=t_stamp_sync,
            guid=guid,
            type=type,
        )

        phys_del.additional_properties = d
        return phys_del

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
