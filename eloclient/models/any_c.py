from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnyC")


@_attrs_define
class AnyC:
    """This class defines the constants for the type member in Any.

    Attributes:
        type_handle (Union[Unset, int]):
        type_int (Union[Unset, int]):
        type_double (Union[Unset, int]):
        type_array_byte (Union[Unset, int]):
        type_array_any (Union[Unset, int]):
        type_string (Union[Unset, int]):
        type_boolean (Union[Unset, int]):
        type_long (Union[Unset, int]):
        type_object (Union[Unset, int]):
    """

    type_handle: Union[Unset, int] = UNSET
    type_int: Union[Unset, int] = UNSET
    type_double: Union[Unset, int] = UNSET
    type_array_byte: Union[Unset, int] = UNSET
    type_array_any: Union[Unset, int] = UNSET
    type_string: Union[Unset, int] = UNSET
    type_boolean: Union[Unset, int] = UNSET
    type_long: Union[Unset, int] = UNSET
    type_object: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_handle = self.type_handle

        type_int = self.type_int

        type_double = self.type_double

        type_array_byte = self.type_array_byte

        type_array_any = self.type_array_any

        type_string = self.type_string

        type_boolean = self.type_boolean

        type_long = self.type_long

        type_object = self.type_object

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_handle is not UNSET:
            field_dict["TYPE_HANDLE"] = type_handle
        if type_int is not UNSET:
            field_dict["TYPE_INT"] = type_int
        if type_double is not UNSET:
            field_dict["TYPE_DOUBLE"] = type_double
        if type_array_byte is not UNSET:
            field_dict["TYPE_ARRAY_BYTE"] = type_array_byte
        if type_array_any is not UNSET:
            field_dict["TYPE_ARRAY_ANY"] = type_array_any
        if type_string is not UNSET:
            field_dict["TYPE_STRING"] = type_string
        if type_boolean is not UNSET:
            field_dict["TYPE_BOOLEAN"] = type_boolean
        if type_long is not UNSET:
            field_dict["TYPE_LONG"] = type_long
        if type_object is not UNSET:
            field_dict["TYPE_OBJECT"] = type_object

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_handle = d.pop("TYPE_HANDLE", UNSET)

        type_int = d.pop("TYPE_INT", UNSET)

        type_double = d.pop("TYPE_DOUBLE", UNSET)

        type_array_byte = d.pop("TYPE_ARRAY_BYTE", UNSET)

        type_array_any = d.pop("TYPE_ARRAY_ANY", UNSET)

        type_string = d.pop("TYPE_STRING", UNSET)

        type_boolean = d.pop("TYPE_BOOLEAN", UNSET)

        type_long = d.pop("TYPE_LONG", UNSET)

        type_object = d.pop("TYPE_OBJECT", UNSET)

        any_c = cls(
            type_handle=type_handle,
            type_int=type_int,
            type_double=type_double,
            type_array_byte=type_array_byte,
            type_array_any=type_array_any,
            type_string=type_string,
            type_boolean=type_boolean,
            type_long=type_long,
            type_object=type_object,
        )

        any_c.additional_properties = d
        return any_c

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
