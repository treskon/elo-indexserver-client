from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_state import PluginState


T = TypeVar("T", bound="PluginInfo")


@_attrs_define
class PluginInfo:
    """OSGi plugin information.

    Attributes:
        symbolic_name (Union[Unset, str]): Plugin name. Symbolic name of OSGi plugin.
        id (Union[Unset, str]): Plugin ID.
            This value is transient and might change after Indexserver has re-loaded or
             re-started.
        state (Union[Unset, PluginState]): State of OSGi plugin.
        service_names (Union[Unset, List[str]]):
    """

    symbolic_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    state: Union[Unset, "PluginState"] = UNSET
    service_names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbolic_name = self.symbolic_name

        id = self.id

        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        service_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_names, Unset):
            service_names = self.service_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbolic_name is not UNSET:
            field_dict["symbolicName"] = symbolic_name
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if service_names is not UNSET:
            field_dict["serviceNames"] = service_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin_state import PluginState

        d = src_dict.copy()
        symbolic_name = d.pop("symbolicName", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PluginState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PluginState.from_dict(_state)

        service_names = cast(List[str], d.pop("serviceNames", UNSET))

        plugin_info = cls(
            symbolic_name=symbolic_name,
            id=id,
            state=state,
            service_names=service_names,
        )

        plugin_info.additional_properties = d
        return plugin_info

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
