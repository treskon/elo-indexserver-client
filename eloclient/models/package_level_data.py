from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageLevelData")


@_attrs_define
class PackageLevelData:
    """This class defines a package level.
    EIX-2606

        Attributes:
            level (Union[Unset, int]): The level.
            package_guid (Union[Unset, str]): Package GUID.
            name (Union[Unset, str]): Level name.
            guid (Union[Unset, str]): Level GUID.
    """

    level: Union[Unset, int] = UNSET
    package_guid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level = self.level

        package_guid = self.package_guid

        name = self.name

        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if package_guid is not UNSET:
            field_dict["packageGuid"] = package_guid
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level = d.pop("level", UNSET)

        package_guid = d.pop("packageGuid", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        package_level_data = cls(
            level=level,
            package_guid=package_guid,
            name=name,
            guid=guid,
        )

        package_level_data.additional_properties = d
        return package_level_data

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
