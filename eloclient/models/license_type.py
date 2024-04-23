from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseType")


@_attrs_define
class LicenseType:
    """This enumeration defines constants for the license type.
    The license type is set during
     installation as production, test or development.

        Attributes:
            test (Union[Unset, LicenseType]): This enumeration defines constants for the license type.
                The license type is set during
                 installation as production, test or development.
            development (Union[Unset, LicenseType]): This enumeration defines constants for the license type.
                The license type is set during
                 installation as production, test or development.
            production (Union[Unset, LicenseType]): This enumeration defines constants for the license type.
                The license type is set during
                 installation as production, test or development.
    """

    test: Union[Unset, "LicenseType"] = UNSET
    development: Union[Unset, "LicenseType"] = UNSET
    production: Union[Unset, "LicenseType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        test: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.test, Unset):
            test = self.test.to_dict()

        development: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.development, Unset):
            development = self.development.to_dict()

        production: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test is not UNSET:
            field_dict["TEST"] = test
        if development is not UNSET:
            field_dict["DEVELOPMENT"] = development
        if production is not UNSET:
            field_dict["PRODUCTION"] = production

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _test = d.pop("TEST", UNSET)
        test: Union[Unset, LicenseType]
        if isinstance(_test, Unset):
            test = UNSET
        else:
            test = LicenseType.from_dict(_test)

        _development = d.pop("DEVELOPMENT", UNSET)
        development: Union[Unset, LicenseType]
        if isinstance(_development, Unset):
            development = UNSET
        else:
            development = LicenseType.from_dict(_development)

        _production = d.pop("PRODUCTION", UNSET)
        production: Union[Unset, LicenseType]
        if isinstance(_production, Unset):
            production = UNSET
        else:
            production = LicenseType.from_dict(_production)

        license_type = cls(
            test=test,
            development=development,
            production=production,
        )

        license_type.additional_properties = d
        return license_type

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
