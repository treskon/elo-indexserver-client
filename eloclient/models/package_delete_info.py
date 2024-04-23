from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageDeleteInfo")


@_attrs_define
class PackageDeleteInfo:
    """Describe delete criteria for
    {@link PackageService#deletePackages(ClientInfo ci, PackageDeleteInfo deleteInfo, LockZ unlockZ)}.
     EIX-1895

        Attributes:
            delete_package_content (Union[Unset, bool]): if true then archive elements belonging to that package will be
                deleted as well
            name_or_guids (Union[Unset, List[str]]):
    """

    delete_package_content: Union[Unset, bool] = UNSET
    name_or_guids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delete_package_content = self.delete_package_content

        name_or_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.name_or_guids, Unset):
            name_or_guids = self.name_or_guids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_package_content is not UNSET:
            field_dict["deletePackageContent"] = delete_package_content
        if name_or_guids is not UNSET:
            field_dict["nameOrGuids"] = name_or_guids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delete_package_content = d.pop("deletePackageContent", UNSET)

        name_or_guids = cast(List[str], d.pop("nameOrGuids", UNSET))

        package_delete_info = cls(
            delete_package_content=delete_package_content,
            name_or_guids=name_or_guids,
        )

        package_delete_info.additional_properties = d
        return package_delete_info

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
