from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StringSingleValue")


@_attrs_define
class StringSingleValue:
    r"""
    Attributes:
        value (Union[Unset, str]): <p>
            text value
             </p>
             <p>
             Do not escape any special characters, this is done by IX.<br>
             Exception: if <code>value</code> starts with "=" (PowerSearch), nothing is escaped by IX<br>
             If a value to be searched for actually starts with "=", it has to be escaped manually by "\\"
             </p>
    """

    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        string_single_value = cls(
            value=value,
        )

        string_single_value.additional_properties = d
        return string_single_value

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
