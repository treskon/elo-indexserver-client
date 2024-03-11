from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplSetName")


@_attrs_define
class ReplSetName:
    """Properties of a replication set.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            t_stamp (Union[Unset, str]): Timestamp of the last change. The format is JJJJ.MM.DD.hh.mm.
                ss
            desc (Union[Unset, str]): Descriptive text for the replication set.
            id (Union[Unset, int]): Identifier for the replication set.
            image (Union[Unset, int]): Image used for the replication set in list function in the client application.
            mobile (Union[Unset, int]): Replication set is used for archive synchronisation(ELO MOBIL).
            name (Union[Unset, str]): Name of the replication set.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            priority (Union[Unset, int]): Priority of this replication set.
    """

    t_stamp: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    image: Union[Unset, int] = UNSET
    mobile: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp
        desc = self.desc
        id = self.id
        image = self.image
        mobile = self.mobile
        name = self.name
        t_stamp_sync = self.t_stamp_sync
        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if desc is not UNSET:
            field_dict["desc"] = desc
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if name is not UNSET:
            field_dict["name"] = name
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t_stamp = d.pop("TStamp", UNSET)

        desc = d.pop("desc", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        mobile = d.pop("mobile", UNSET)

        name = d.pop("name", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        priority = d.pop("priority", UNSET)

        repl_set_name = cls(
            t_stamp=t_stamp,
            desc=desc,
            id=id,
            image=image,
            mobile=mobile,
            name=name,
            t_stamp_sync=t_stamp_sync,
            priority=priority,
        )

        repl_set_name.additional_properties = d
        return repl_set_name

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
