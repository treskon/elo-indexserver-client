from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginHistory")


@_attrs_define
class PluginHistory:
    """OSGi plugin history.

    Attributes:
        plain_text (Union[Unset, str]): The raw text contained in the version file (e.g. version.txt).
        json_text (Union[Unset, str]): The text in form of a json object.
    """

    plain_text: Union[Unset, str] = UNSET
    json_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plain_text = self.plain_text

        json_text = self.json_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plain_text is not UNSET:
            field_dict["plainText"] = plain_text
        if json_text is not UNSET:
            field_dict["jsonText"] = json_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plain_text = d.pop("plainText", UNSET)

        json_text = d.pop("jsonText", UNSET)

        plugin_history = cls(
            plain_text=plain_text,
            json_text=json_text,
        )

        plugin_history.additional_properties = d
        return plugin_history

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
