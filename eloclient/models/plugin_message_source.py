from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginMessageSource")


@_attrs_define
class PluginMessageSource:
    """Source of plugin message.

    Attributes:
        ixapi (Union[Unset, PluginMessageSource]): Source of plugin message.
        http (Union[Unset, PluginMessageSource]): Source of plugin message.
        notihng (Union[Unset, PluginMessageSource]): Source of plugin message.
    """

    ixapi: Union[Unset, "PluginMessageSource"] = UNSET
    http: Union[Unset, "PluginMessageSource"] = UNSET
    notihng: Union[Unset, "PluginMessageSource"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ixapi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ixapi, Unset):
            ixapi = self.ixapi.to_dict()

        http: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.http, Unset):
            http = self.http.to_dict()

        notihng: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notihng, Unset):
            notihng = self.notihng.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ixapi is not UNSET:
            field_dict["IXAPI"] = ixapi
        if http is not UNSET:
            field_dict["HTTP"] = http
        if notihng is not UNSET:
            field_dict["NOTIHNG"] = notihng

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ixapi = d.pop("IXAPI", UNSET)
        ixapi: Union[Unset, PluginMessageSource]
        if isinstance(_ixapi, Unset):
            ixapi = UNSET
        else:
            ixapi = PluginMessageSource.from_dict(_ixapi)

        _http = d.pop("HTTP", UNSET)
        http: Union[Unset, PluginMessageSource]
        if isinstance(_http, Unset):
            http = UNSET
        else:
            http = PluginMessageSource.from_dict(_http)

        _notihng = d.pop("NOTIHNG", UNSET)
        notihng: Union[Unset, PluginMessageSource]
        if isinstance(_notihng, Unset):
            notihng = UNSET
        else:
            notihng = PluginMessageSource.from_dict(_notihng)

        plugin_message_source = cls(
            ixapi=ixapi,
            http=http,
            notihng=notihng,
        )

        plugin_message_source.additional_properties = d
        return plugin_message_source

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
