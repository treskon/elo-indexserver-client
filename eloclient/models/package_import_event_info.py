from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_data import PackageData


T = TypeVar("T", bound="PackageImportEventInfo")


@_attrs_define
class PackageImportEventInfo:
    """Describe event info for onAfterPackageImport.
    EIX-3085

        Attributes:
            package_data (Union[Unset, PackageData]): This class defines a package.
                EIX-1895
    """

    package_data: Union[Unset, "PackageData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_data, Unset):
            package_data = self.package_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_data is not UNSET:
            field_dict["packageData"] = package_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_data import PackageData

        d = src_dict.copy()
        _package_data = d.pop("packageData", UNSET)
        package_data: Union[Unset, PackageData]
        if isinstance(_package_data, Unset):
            package_data = UNSET
        else:
            package_data = PackageData.from_dict(_package_data)

        package_import_event_info = cls(
            package_data=package_data,
        )

        package_import_event_info.additional_properties = d
        return package_import_event_info

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
