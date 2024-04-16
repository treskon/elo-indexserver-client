from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInfo")


@_attrs_define
class ConfigInfo:
    """This class defines select criteria for reading configuration data.

    Attributes:
        component (Union[Unset, str]): Component name. Filters {@link ConfigRecord#component} values.
        instance_id (Union[Unset, str]): Instance ID. Filters {@link ConfigRecord#instanceId} values.
        level (Union[Unset, int]): Priority level. Select entries with the highest priority that is lower or equal to
            this value.
        group_id (Union[Unset, str]): Group ID. Filters {@link ConfigRecord#groupId} values.
        package_name (Union[Unset, str]): Package name or GUID. Filters {@link ConfigRecord#packageName} values.
        key (Union[Unset, str]): Entry key. Filters {@link ConfigRecord#key} values. This value supports wildcards at
            its end.
    """

    component: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    group_id: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        component = self.component

        instance_id = self.instance_id

        level = self.level

        group_id = self.group_id

        package_name = self.package_name

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if level is not UNSET:
            field_dict["level"] = level
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        component = d.pop("component", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        level = d.pop("level", UNSET)

        group_id = d.pop("groupId", UNSET)

        package_name = d.pop("packageName", UNSET)

        key = d.pop("key", UNSET)

        config_info = cls(
            component=component,
            instance_id=instance_id,
            level=level,
            group_id=group_id,
            package_name=package_name,
            key=key,
        )

        config_info.additional_properties = d
        return config_info

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
