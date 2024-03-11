from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EsSettingsProperty")


@_attrs_define
class EsSettingsProperty:
    """Properties of ESInstanceSettings

    Attributes:
        value (Union[Unset, str]): Value of property as set in database. If empty, default value is used.
        default_value (Union[Unset, str]): Default value of property.
        possible_values (Union[Unset, List[str]]):
    """

    value: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    possible_values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        default_value = self.default_value
        possible_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.possible_values, Unset):
            possible_values = self.possible_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if possible_values is not UNSET:
            field_dict["possibleValues"] = possible_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        possible_values = cast(List[str], d.pop("possibleValues", UNSET))

        es_settings_property = cls(
            value=value,
            default_value=default_value,
            possible_values=possible_values,
        )

        es_settings_property.additional_properties = d
        return es_settings_property

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
