from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageLevelDataC")


@_attrs_define
class PackageLevelDataC:
    """<p>Bit constants for members of PackageLevelData</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_guid (Union[Unset, int]): Column length: Level GUID.
                DB column: guid
            ln_package_guid (Union[Unset, int]): Column length: Package GUID.
                DB column: pkguid
            ln_name (Union[Unset, int]): Column length: Level name.
                DB column: name
            mb_package_guid (Union[Unset, str]): Member bit: Package GUID.
                DB column: pkguid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_guid (Union[Unset, str]): Member bit: Level GUID.
                DB column: guid
            mb_name (Union[Unset, str]): Member bit: Level name.
                DB column: name
            mb_level (Union[Unset, str]): Member bit: The level.
                DB column: pkglevel
    """

    ln_guid: Union[Unset, int] = UNSET
    ln_package_guid: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_package_guid: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_level: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_guid = self.ln_guid

        ln_package_guid = self.ln_package_guid

        ln_name = self.ln_name

        mb_package_guid = self.mb_package_guid

        mb_all_members = self.mb_all_members

        mb_guid = self.mb_guid

        mb_name = self.mb_name

        mb_level = self.mb_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if ln_package_guid is not UNSET:
            field_dict["lnPackageGuid"] = ln_package_guid
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_package_guid is not UNSET:
            field_dict["mbPackageGuid"] = mb_package_guid
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_level is not UNSET:
            field_dict["mbLevel"] = mb_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_guid = d.pop("lnGuid", UNSET)

        ln_package_guid = d.pop("lnPackageGuid", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_package_guid = d.pop("mbPackageGuid", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_level = d.pop("mbLevel", UNSET)

        package_level_data_c = cls(
            ln_guid=ln_guid,
            ln_package_guid=ln_package_guid,
            ln_name=ln_name,
            mb_package_guid=mb_package_guid,
            mb_all_members=mb_all_members,
            mb_guid=mb_guid,
            mb_name=mb_name,
            mb_level=mb_level,
        )

        package_level_data_c.additional_properties = d
        return package_level_data_c

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
