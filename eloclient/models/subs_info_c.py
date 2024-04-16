from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubsInfoC")


@_attrs_define
class SubsInfoC:
    """Constants for class SubsInfo.

    Attributes:
        mb_subs_name (Union[Unset, str]):
        mb_user_name (Union[Unset, str]):
        mb_subs_id (Union[Unset, str]):
        mb_user_id (Union[Unset, str]):
        mb_inherit_rights (Union[Unset, str]):
        mb_active_id (Union[Unset, str]):
    """

    mb_subs_name: Union[Unset, str] = UNSET
    mb_user_name: Union[Unset, str] = UNSET
    mb_subs_id: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_inherit_rights: Union[Unset, str] = UNSET
    mb_active_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_subs_name = self.mb_subs_name

        mb_user_name = self.mb_user_name

        mb_subs_id = self.mb_subs_id

        mb_user_id = self.mb_user_id

        mb_inherit_rights = self.mb_inherit_rights

        mb_active_id = self.mb_active_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_subs_name is not UNSET:
            field_dict["mbSubsName"] = mb_subs_name
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if mb_subs_id is not UNSET:
            field_dict["mbSubsId"] = mb_subs_id
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_inherit_rights is not UNSET:
            field_dict["mbInheritRights"] = mb_inherit_rights
        if mb_active_id is not UNSET:
            field_dict["mbActiveId"] = mb_active_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_subs_name = d.pop("mbSubsName", UNSET)

        mb_user_name = d.pop("mbUserName", UNSET)

        mb_subs_id = d.pop("mbSubsId", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_inherit_rights = d.pop("mbInheritRights", UNSET)

        mb_active_id = d.pop("mbActiveId", UNSET)

        subs_info_c = cls(
            mb_subs_name=mb_subs_name,
            mb_user_name=mb_user_name,
            mb_subs_id=mb_subs_id,
            mb_user_id=mb_user_id,
            mb_inherit_rights=mb_inherit_rights,
            mb_active_id=mb_active_id,
        )

        subs_info_c.additional_properties = d
        return subs_info_c

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
