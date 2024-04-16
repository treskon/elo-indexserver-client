from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigRecordC")


@_attrs_define
class ConfigRecordC:
    """Constants for configuration entries.

    Attributes:
        package_teamspaces (Union[Unset, str]): Package name for teamspace entries as {@link ConfigRecord#packageName}.
        component_teamspaces (Union[Unset, str]): Used as {@link ConfigRecord#component} for teamspace entries.
        component_flows (Union[Unset, str]): Used as {@link ConfigRecord#component} for flows entries.
        package_workspaces (Union[Unset, str]): Package name for workspace entries used as {@link
            ConfigRecord#packageName}.
        max_value_length (Union[Unset, int]): Maximum length of {@link ConfigRecord#value}. The maximum length is 1
            million characters.
        component_workspaces (Union[Unset, str]): Used as {@link ConfigRecord#component} for workspace entries.
    """

    package_teamspaces: Union[Unset, str] = UNSET
    component_teamspaces: Union[Unset, str] = UNSET
    component_flows: Union[Unset, str] = UNSET
    package_workspaces: Union[Unset, str] = UNSET
    max_value_length: Union[Unset, int] = UNSET
    component_workspaces: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_teamspaces = self.package_teamspaces

        component_teamspaces = self.component_teamspaces

        component_flows = self.component_flows

        package_workspaces = self.package_workspaces

        max_value_length = self.max_value_length

        component_workspaces = self.component_workspaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_teamspaces is not UNSET:
            field_dict["PACKAGE_TEAMSPACES"] = package_teamspaces
        if component_teamspaces is not UNSET:
            field_dict["COMPONENT_TEAMSPACES"] = component_teamspaces
        if component_flows is not UNSET:
            field_dict["COMPONENT_FLOWS"] = component_flows
        if package_workspaces is not UNSET:
            field_dict["PACKAGE_WORKSPACES"] = package_workspaces
        if max_value_length is not UNSET:
            field_dict["MAX_VALUE_LENGTH"] = max_value_length
        if component_workspaces is not UNSET:
            field_dict["COMPONENT_WORKSPACES"] = component_workspaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package_teamspaces = d.pop("PACKAGE_TEAMSPACES", UNSET)

        component_teamspaces = d.pop("COMPONENT_TEAMSPACES", UNSET)

        component_flows = d.pop("COMPONENT_FLOWS", UNSET)

        package_workspaces = d.pop("PACKAGE_WORKSPACES", UNSET)

        max_value_length = d.pop("MAX_VALUE_LENGTH", UNSET)

        component_workspaces = d.pop("COMPONENT_WORKSPACES", UNSET)

        config_record_c = cls(
            package_teamspaces=package_teamspaces,
            component_teamspaces=component_teamspaces,
            component_flows=component_flows,
            package_workspaces=package_workspaces,
            max_value_length=max_value_length,
            component_workspaces=component_workspaces,
        )

        config_record_c.additional_properties = d
        return config_record_c

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
