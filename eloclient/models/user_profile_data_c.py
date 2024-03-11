from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileDataC")


@_attrs_define
class UserProfileDataC:
    """<p>
    Bit constants for members of UserProfileData
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_user (Union[Unset, str]): DB column: userid
            mb_key (Union[Unset, str]): DB column: optkey
            ln_key (Union[Unset, int]): DB column: optkey
            mb_value (Union[Unset, str]): DB column: optvalue
            ln_value (Union[Unset, int]): DB column: optvalue
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_user: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    mb_value: Union[Unset, str] = UNSET
    ln_value: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_user = self.mb_user
        mb_key = self.mb_key
        ln_key = self.ln_key
        mb_value = self.mb_value
        ln_value = self.ln_value
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_user is not UNSET:
            field_dict["mbUser"] = mb_user
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_user = d.pop("mbUser", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        ln_value = d.pop("lnValue", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        user_profile_data_c = cls(
            mb_user=mb_user,
            mb_key=mb_key,
            ln_key=ln_key,
            mb_value=mb_value,
            ln_value=ln_value,
            mb_all_members=mb_all_members,
        )

        user_profile_data_c.additional_properties = d
        return user_profile_data_c

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
