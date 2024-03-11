from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserName")


@_attrs_define
class UserName:
    """<p>
    Contains user name, ID and type (group or user).
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            id (Union[Unset, int]): User ID
            name (Union[Unset, str]): User name.
            guid (Union[Unset, str]): User GUID.
            type (Union[Unset, int]): User type.
            flags (Union[Unset, int]): User rights. To detect a suspended user, test bit AccessC.FLAG_NOLOGIN.
            flags2 (Union[Unset, int]): User rights, second set. This member is a bit set of AccessC.FLAGS2_* constants.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    flags: Union[Unset, int] = UNSET
    flags2: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        guid = self.guid
        type = self.type
        flags = self.flags
        flags2 = self.flags2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if type is not UNSET:
            field_dict["type"] = type
        if flags is not UNSET:
            field_dict["flags"] = flags
        if flags2 is not UNSET:
            field_dict["flags2"] = flags2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        type = d.pop("type", UNSET)

        flags = d.pop("flags", UNSET)

        flags2 = d.pop("flags2", UNSET)

        user_name = cls(
            id=id,
            name=name,
            guid=guid,
            type=type,
            flags=flags,
            flags2=flags2,
        )

        user_name.additional_properties = d
        return user_name

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
