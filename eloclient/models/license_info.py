from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseInfo")


@_attrs_define
class LicenseInfo:
    """License information to be checked with
    {@link IXServicePortIF#checkLicense(ClientInfo, LicenseInfo)}.

        Attributes:
            license_key (Union[Unset, str]): License key.
            module_name (Union[Unset, str]): Module name.
            customer_name (Union[Unset, str]): Customer name.
    """

    license_key: Union[Unset, str] = UNSET
    module_name: Union[Unset, str] = UNSET
    customer_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        license_key = self.license_key

        module_name = self.module_name

        customer_name = self.customer_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_key is not UNSET:
            field_dict["licenseKey"] = license_key
        if module_name is not UNSET:
            field_dict["moduleName"] = module_name
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        license_key = d.pop("licenseKey", UNSET)

        module_name = d.pop("moduleName", UNSET)

        customer_name = d.pop("customerName", UNSET)

        license_info = cls(
            license_key=license_key,
            module_name=module_name,
            customer_name=customer_name,
        )

        license_info.additional_properties = d
        return license_info

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
