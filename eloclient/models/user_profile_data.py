from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileData")


@_attrs_define
class UserProfileData:
    """Internal class.

    Attributes:
        user (Union[Unset, int]): User ID.
            DB column: userid
        value (Union[Unset, str]): Option value.
            DB column: optvalue
        key (Union[Unset, str]): Option key.
            DB column: optkey
    """

    user: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user

        value = self.value

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if value is not UNSET:
            field_dict["value"] = value
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        value = d.pop("value", UNSET)

        key = d.pop("key", UNSET)

        user_profile_data = cls(
            user=user,
            value=value,
            key=key,
        )

        user_profile_data.additional_properties = d
        return user_profile_data

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
