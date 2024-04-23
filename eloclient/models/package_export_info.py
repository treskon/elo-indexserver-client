from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageExportInfo")


@_attrs_define
class PackageExportInfo:
    """Describe export criteria for
    {@link PackageService#exportPackageContent(ClientInfo ci, PackageExportInfo exportInfo)}.
     EIX-1895

        Attributes:
            name_or_guids (Union[Unset, List[str]]):
    """

    name_or_guids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name_or_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.name_or_guids, Unset):
            name_or_guids = self.name_or_guids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_or_guids is not UNSET:
            field_dict["nameOrGuids"] = name_or_guids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name_or_guids = cast(List[str], d.pop("nameOrGuids", UNSET))

        package_export_info = cls(
            name_or_guids=name_or_guids,
        )

        package_export_info.additional_properties = d
        return package_export_info

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
