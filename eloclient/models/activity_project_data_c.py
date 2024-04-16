from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityProjectDataC")


@_attrs_define
class ActivityProjectDataC:
    """<p>Bit constants for members of ActivityProject</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_minor (Union[Unset, str]): DB column: minor
            ln_opt_value (Union[Unset, int]): DB column: optvalue
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_major (Union[Unset, str]): DB column: major
            mb_opt_value (Union[Unset, str]): DB column: optvalue
            mb_project (Union[Unset, str]): DB column: project
            ln_project (Union[Unset, int]): DB column: project
    """

    mb_minor: Union[Unset, str] = UNSET
    ln_opt_value: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_major: Union[Unset, str] = UNSET
    mb_opt_value: Union[Unset, str] = UNSET
    mb_project: Union[Unset, str] = UNSET
    ln_project: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_minor = self.mb_minor

        ln_opt_value = self.ln_opt_value

        mb_all_members = self.mb_all_members

        mb_major = self.mb_major

        mb_opt_value = self.mb_opt_value

        mb_project = self.mb_project

        ln_project = self.ln_project

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_minor is not UNSET:
            field_dict["mbMinor"] = mb_minor
        if ln_opt_value is not UNSET:
            field_dict["lnOptValue"] = ln_opt_value
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_major is not UNSET:
            field_dict["mbMajor"] = mb_major
        if mb_opt_value is not UNSET:
            field_dict["mbOptValue"] = mb_opt_value
        if mb_project is not UNSET:
            field_dict["mbProject"] = mb_project
        if ln_project is not UNSET:
            field_dict["lnProject"] = ln_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_minor = d.pop("mbMinor", UNSET)

        ln_opt_value = d.pop("lnOptValue", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_major = d.pop("mbMajor", UNSET)

        mb_opt_value = d.pop("mbOptValue", UNSET)

        mb_project = d.pop("mbProject", UNSET)

        ln_project = d.pop("lnProject", UNSET)

        activity_project_data_c = cls(
            mb_minor=mb_minor,
            ln_opt_value=ln_opt_value,
            mb_all_members=mb_all_members,
            mb_major=mb_major,
            mb_opt_value=mb_opt_value,
            mb_project=mb_project,
            ln_project=ln_project,
        )

        activity_project_data_c.additional_properties = d
        return activity_project_data_c

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
