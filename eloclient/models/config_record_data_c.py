from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigRecordDataC")


@_attrs_define
class ConfigRecordDataC:
    """<p>Bit constants for members of ConfigRecord</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_instance_id (Union[Unset, str]): Member bit: Instance ID for workspace.
                For workspace entries, this value is assigned to the related
                 DB column: cfginstance
            mb_id (Union[Unset, str]): Member bit: Row ID. This ID is unique over all entries.
                DB column: cfgid
            mb_package_name (Union[Unset, str]): Member bit: Package name or GUID.
                DB column: cfgpackage
            mb_blob_value (Union[Unset, str]): DB column: cfgvalueblob
            mb_key (Union[Unset, str]): Member bit: Entry key.
                DB column: cfgkey
            mb_group_id (Union[Unset, str]): Member bit: Groups related entries.
                DB column: cfggroup
            ln_acl (Union[Unset, int]): Column length: Access control in raw representation.
                DB column: cfgacl
            ln_group_id (Union[Unset, int]): Column length: Groups related entries.
                DB column: cfggroup
            ln_id (Union[Unset, int]): Column length: Row ID. This ID is unique over all entries.
                DB column: cfgid
            mb_level (Union[Unset, str]): Member bit: Layer level. This value defines the priority for the entry.
                DB column: cfglevel
            ln_component (Union[Unset, int]): Column length: ELO module name or ID.
                DB column: cfgcomponent
            ln_value (Union[Unset, int]): Column length: Entry value. This value can hold up to {@link
                ConfigRecordC#MAX_VALUE_LENGTH} characters.
                DB column: cfgvalue
            mb_component (Union[Unset, str]): Member bit: ELO module name or ID.
                DB column: cfgcomponent
            mb_value (Union[Unset, str]): Member bit: Entry value. This value can hold up to {@link
                ConfigRecordC#MAX_VALUE_LENGTH} characters.
                DB column: cfgvalue
            ln_blob_value (Union[Unset, int]): DB column: cfgvalueblob
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_key (Union[Unset, int]): Column length: Entry key.
                DB column: cfgkey
            mb_acl (Union[Unset, str]): Member bit: Access control in raw representation.
                DB column: cfgacl
            ln_instance_id (Union[Unset, int]): Column length: Instance ID for workspace.
                For workspace entries, this value is assigned to the related
                 DB column: cfginstance
            ln_package_name (Union[Unset, int]): Column length: Package name or GUID.
                DB column: cfgpackage
    """

    mb_instance_id: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_blob_value: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    mb_group_id: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    ln_group_id: Union[Unset, int] = UNSET
    ln_id: Union[Unset, int] = UNSET
    mb_level: Union[Unset, str] = UNSET
    ln_component: Union[Unset, int] = UNSET
    ln_value: Union[Unset, int] = UNSET
    mb_component: Union[Unset, str] = UNSET
    mb_value: Union[Unset, str] = UNSET
    ln_blob_value: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_instance_id: Union[Unset, int] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_instance_id = self.mb_instance_id

        mb_id = self.mb_id

        mb_package_name = self.mb_package_name

        mb_blob_value = self.mb_blob_value

        mb_key = self.mb_key

        mb_group_id = self.mb_group_id

        ln_acl = self.ln_acl

        ln_group_id = self.ln_group_id

        ln_id = self.ln_id

        mb_level = self.mb_level

        ln_component = self.ln_component

        ln_value = self.ln_value

        mb_component = self.mb_component

        mb_value = self.mb_value

        ln_blob_value = self.ln_blob_value

        mb_all_members = self.mb_all_members

        ln_key = self.ln_key

        mb_acl = self.mb_acl

        ln_instance_id = self.ln_instance_id

        ln_package_name = self.ln_package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_instance_id is not UNSET:
            field_dict["mbInstanceId"] = mb_instance_id
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_blob_value is not UNSET:
            field_dict["mbBlobValue"] = mb_blob_value
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if mb_group_id is not UNSET:
            field_dict["mbGroupId"] = mb_group_id
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if ln_group_id is not UNSET:
            field_dict["lnGroupId"] = ln_group_id
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if mb_level is not UNSET:
            field_dict["mbLevel"] = mb_level
        if ln_component is not UNSET:
            field_dict["lnComponent"] = ln_component
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if mb_component is not UNSET:
            field_dict["mbComponent"] = mb_component
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if ln_blob_value is not UNSET:
            field_dict["lnBlobValue"] = ln_blob_value
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_instance_id is not UNSET:
            field_dict["lnInstanceId"] = ln_instance_id
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_instance_id = d.pop("mbInstanceId", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_blob_value = d.pop("mbBlobValue", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        mb_group_id = d.pop("mbGroupId", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        ln_group_id = d.pop("lnGroupId", UNSET)

        ln_id = d.pop("lnId", UNSET)

        mb_level = d.pop("mbLevel", UNSET)

        ln_component = d.pop("lnComponent", UNSET)

        ln_value = d.pop("lnValue", UNSET)

        mb_component = d.pop("mbComponent", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        ln_blob_value = d.pop("lnBlobValue", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_instance_id = d.pop("lnInstanceId", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        config_record_data_c = cls(
            mb_instance_id=mb_instance_id,
            mb_id=mb_id,
            mb_package_name=mb_package_name,
            mb_blob_value=mb_blob_value,
            mb_key=mb_key,
            mb_group_id=mb_group_id,
            ln_acl=ln_acl,
            ln_group_id=ln_group_id,
            ln_id=ln_id,
            mb_level=mb_level,
            ln_component=ln_component,
            ln_value=ln_value,
            mb_component=mb_component,
            mb_value=mb_value,
            ln_blob_value=ln_blob_value,
            mb_all_members=mb_all_members,
            ln_key=ln_key,
            mb_acl=mb_acl,
            ln_instance_id=ln_instance_id,
            ln_package_name=ln_package_name,
        )

        config_record_data_c.additional_properties = d
        return config_record_data_c

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
