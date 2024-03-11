from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheckInfoC")


@_attrs_define
class HealthCheckInfoC:
    """<p>
    Bit constants for members of HealthCheckInfo
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_name (Union[Unset, str]): Member bit: Value name.
                DB column: name
            ln_name (Union[Unset, int]): Column length: Value name.
                DB column: name
            mb_string_value (Union[Unset, str]): Member bit: String value.
                DB column: stringValue
            ln_string_value (Union[Unset, int]): Column length: String value.
                DB column: stringValue
            mb_double_value (Union[Unset, str]): Member bit: Numeric value.
                DB column: doubleValue
            ln_double_value (Union[Unset, int]): Column length: Numeric value.
                DB column: doubleValue
            mb_sample_size (Union[Unset, str]): Member bit: Sample size for mean values.
                DB column: sampleSize
            ln_sample_size (Union[Unset, int]): Column length: Sample size for mean values.
                DB column: sampleSize
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_name: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_string_value: Union[Unset, str] = UNSET
    ln_string_value: Union[Unset, int] = UNSET
    mb_double_value: Union[Unset, str] = UNSET
    ln_double_value: Union[Unset, int] = UNSET
    mb_sample_size: Union[Unset, str] = UNSET
    ln_sample_size: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_name = self.mb_name
        ln_name = self.ln_name
        mb_string_value = self.mb_string_value
        ln_string_value = self.ln_string_value
        mb_double_value = self.mb_double_value
        ln_double_value = self.ln_double_value
        mb_sample_size = self.mb_sample_size
        ln_sample_size = self.ln_sample_size
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_string_value is not UNSET:
            field_dict["mbStringValue"] = mb_string_value
        if ln_string_value is not UNSET:
            field_dict["lnStringValue"] = ln_string_value
        if mb_double_value is not UNSET:
            field_dict["mbDoubleValue"] = mb_double_value
        if ln_double_value is not UNSET:
            field_dict["lnDoubleValue"] = ln_double_value
        if mb_sample_size is not UNSET:
            field_dict["mbSampleSize"] = mb_sample_size
        if ln_sample_size is not UNSET:
            field_dict["lnSampleSize"] = ln_sample_size
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_name = d.pop("mbName", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_string_value = d.pop("mbStringValue", UNSET)

        ln_string_value = d.pop("lnStringValue", UNSET)

        mb_double_value = d.pop("mbDoubleValue", UNSET)

        ln_double_value = d.pop("lnDoubleValue", UNSET)

        mb_sample_size = d.pop("mbSampleSize", UNSET)

        ln_sample_size = d.pop("lnSampleSize", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        health_check_info_c = cls(
            mb_name=mb_name,
            ln_name=ln_name,
            mb_string_value=mb_string_value,
            ln_string_value=ln_string_value,
            mb_double_value=mb_double_value,
            ln_double_value=ln_double_value,
            mb_sample_size=mb_sample_size,
            ln_sample_size=ln_sample_size,
            mb_all_members=mb_all_members,
        )

        health_check_info_c.additional_properties = d
        return health_check_info_c

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
