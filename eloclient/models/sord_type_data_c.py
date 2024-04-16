from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SordTypeDataC")


@_attrs_define
class SordTypeDataC:
    """<p>Bit constants for members of SordType</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_guid (Union[Unset, int]): Column length: GUID of SordType EIX-2032
                DB column: guid
            mb_extensions (Union[Unset, str]): DB column: extensions
            mb_id (Union[Unset, str]): DB column: id
            ln_name (Union[Unset, int]): DB column: name
            mb_package_name (Union[Unset, str]): Member bit: Package name of SordType
                DB column: packagename
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_extensions (Union[Unset, int]): DB column: extensions
            mb_guid (Union[Unset, str]): Member bit: GUID of SordType EIX-2032
                DB column: guid
            mb_name (Union[Unset, str]): DB column: name
            ln_package_name (Union[Unset, int]): Column length: Package name of SordType
                DB column: packagename
    """

    ln_guid: Union[Unset, int] = UNSET
    mb_extensions: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_extensions: Union[Unset, int] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_guid = self.ln_guid

        mb_extensions = self.mb_extensions

        mb_id = self.mb_id

        ln_name = self.ln_name

        mb_package_name = self.mb_package_name

        mb_all_members = self.mb_all_members

        ln_extensions = self.ln_extensions

        mb_guid = self.mb_guid

        mb_name = self.mb_name

        ln_package_name = self.ln_package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_extensions is not UNSET:
            field_dict["mbExtensions"] = mb_extensions
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_extensions is not UNSET:
            field_dict["lnExtensions"] = ln_extensions
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_guid = d.pop("lnGuid", UNSET)

        mb_extensions = d.pop("mbExtensions", UNSET)

        mb_id = d.pop("mbId", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_extensions = d.pop("lnExtensions", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        sord_type_data_c = cls(
            ln_guid=ln_guid,
            mb_extensions=mb_extensions,
            mb_id=mb_id,
            ln_name=ln_name,
            mb_package_name=mb_package_name,
            mb_all_members=mb_all_members,
            ln_extensions=ln_extensions,
            mb_guid=mb_guid,
            mb_name=mb_name,
            ln_package_name=ln_package_name,
        )

        sord_type_data_c.additional_properties = d
        return sord_type_data_c

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
