from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexValueC")


@_attrs_define
class IndexValueC:
    """This class defines the constants for the type member in IndexValue.

    Attributes:
        type_int (Union[Unset, int]):
        type_double (Union[Unset, int]):
        type_string (Union[Unset, int]):
    """

    type_int: Union[Unset, int] = UNSET
    type_double: Union[Unset, int] = UNSET
    type_string: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_int = self.type_int
        type_double = self.type_double
        type_string = self.type_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_int is not UNSET:
            field_dict["TYPE_INT"] = type_int
        if type_double is not UNSET:
            field_dict["TYPE_DOUBLE"] = type_double
        if type_string is not UNSET:
            field_dict["TYPE_STRING"] = type_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_int = d.pop("TYPE_INT", UNSET)

        type_double = d.pop("TYPE_DOUBLE", UNSET)

        type_string = d.pop("TYPE_STRING", UNSET)

        index_value_c = cls(
            type_int=type_int,
            type_double=type_double,
            type_string=type_string,
        )

        index_value_c.additional_properties = d
        return index_value_c

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
