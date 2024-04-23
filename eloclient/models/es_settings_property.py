from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EsSettingsProperty")


@_attrs_define
class EsSettingsProperty:
    """Properties of ESInstanceSettings

    Attributes:
        possible_values (Union[Unset, List[str]]):
        default_value (Union[Unset, str]): Default value of property.
        value (Union[Unset, str]): Value of property as set in database. If empty, default value is used.
    """

    possible_values: Union[Unset, List[str]] = UNSET
    default_value: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        possible_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.possible_values, Unset):
            possible_values = self.possible_values

        default_value = self.default_value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if possible_values is not UNSET:
            field_dict["possibleValues"] = possible_values
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        possible_values = cast(List[str], d.pop("possibleValues", UNSET))

        default_value = d.pop("defaultValue", UNSET)

        value = d.pop("value", UNSET)

        es_settings_property = cls(
            possible_values=possible_values,
            default_value=default_value,
            value=value,
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
