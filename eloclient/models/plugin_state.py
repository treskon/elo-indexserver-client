from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginState")


@_attrs_define
class PluginState:
    """State of OSGi plugin.

    Attributes:
        uninstalled (Union[Unset, PluginState]): State of OSGi plugin.
        active (Union[Unset, PluginState]): State of OSGi plugin.
        installed (Union[Unset, PluginState]): State of OSGi plugin.
    """

    uninstalled: Union[Unset, "PluginState"] = UNSET
    active: Union[Unset, "PluginState"] = UNSET
    installed: Union[Unset, "PluginState"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uninstalled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.uninstalled, Unset):
            uninstalled = self.uninstalled.to_dict()

        active: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        installed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.installed, Unset):
            installed = self.installed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uninstalled is not UNSET:
            field_dict["UNINSTALLED"] = uninstalled
        if active is not UNSET:
            field_dict["ACTIVE"] = active
        if installed is not UNSET:
            field_dict["INSTALLED"] = installed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _uninstalled = d.pop("UNINSTALLED", UNSET)
        uninstalled: Union[Unset, PluginState]
        if isinstance(_uninstalled, Unset):
            uninstalled = UNSET
        else:
            uninstalled = PluginState.from_dict(_uninstalled)

        _active = d.pop("ACTIVE", UNSET)
        active: Union[Unset, PluginState]
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = PluginState.from_dict(_active)

        _installed = d.pop("INSTALLED", UNSET)
        installed: Union[Unset, PluginState]
        if isinstance(_installed, Unset):
            installed = UNSET
        else:
            installed = PluginState.from_dict(_installed)

        plugin_state = cls(
            uninstalled=uninstalled,
            active=active,
            installed=installed,
        )

        plugin_state.additional_properties = d
        return plugin_state

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
