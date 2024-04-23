from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteConfigInfo")


@_attrs_define
class DeleteConfigInfo:
    """Describe what to delete in
    {@link ConfigService#deleteConfiguration2(de.elo.ix.client.ClientInfo, DeleteConfigInfo)}.

        Attributes:
            level (Union[Unset, int]): Layer level. This value defines the priority for the entry.
                If level is 0, all levels of the
                 given {@link #packageName} are deleted.
            package_name (Union[Unset, str]): Package GUID. Delete all configuration entries related to this package.
    """

    level: Union[Unset, int] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level = self.level

        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level = d.pop("level", UNSET)

        package_name = d.pop("packageName", UNSET)

        delete_config_info = cls(
            level=level,
            package_name=package_name,
        )

        delete_config_info.additional_properties = d
        return delete_config_info

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
