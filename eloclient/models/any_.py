from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_class import ValueClass


T = TypeVar("T", bound="Any")


@_attrs_define
class Any:
    """This class is a container for one value of a serializable type.

    Attributes:
        string_value (Union[Unset, str]): String value.
        int_value (Union[Unset, int]): Integer value.
        byte_array (Union[Unset, str]): Byte array.
        boolean_value (Union[Unset, bool]): Boolean value.
        object_value (Union[Unset, ValueClass]):
        double_value (Union[Unset, float]): Double value.
        type (Union[Unset, int]): Type. One of the type constants given in AnyC.
        long_value (Union[Unset, str]): Long value.
        any_array (Union[Unset, List['Any']]):
    """

    string_value: Union[Unset, str] = UNSET
    int_value: Union[Unset, int] = UNSET
    byte_array: Union[Unset, str] = UNSET
    boolean_value: Union[Unset, bool] = UNSET
    object_value: Union[Unset, "ValueClass"] = UNSET
    double_value: Union[Unset, float] = UNSET
    type: Union[Unset, int] = UNSET
    long_value: Union[Unset, str] = UNSET
    any_array: Union[Unset, List["Any"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        string_value = self.string_value

        int_value = self.int_value

        byte_array = self.byte_array

        boolean_value = self.boolean_value

        object_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.object_value, Unset):
            object_value = self.object_value.to_dict()

        double_value = self.double_value

        type = self.type

        long_value = self.long_value

        any_array: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.any_array, Unset):
            any_array = []
            for any_array_item_data in self.any_array:
                any_array_item = any_array_item_data.to_dict()
                any_array.append(any_array_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if int_value is not UNSET:
            field_dict["intValue"] = int_value
        if byte_array is not UNSET:
            field_dict["byteArray"] = byte_array
        if boolean_value is not UNSET:
            field_dict["booleanValue"] = boolean_value
        if object_value is not UNSET:
            field_dict["objectValue"] = object_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if type is not UNSET:
            field_dict["type"] = type
        if long_value is not UNSET:
            field_dict["longValue"] = long_value
        if any_array is not UNSET:
            field_dict["anyArray"] = any_array

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.value_class import ValueClass

        d = src_dict.copy()
        string_value = d.pop("stringValue", UNSET)

        int_value = d.pop("intValue", UNSET)

        byte_array = d.pop("byteArray", UNSET)

        boolean_value = d.pop("booleanValue", UNSET)

        _object_value = d.pop("objectValue", UNSET)
        object_value: Union[Unset, ValueClass]
        if isinstance(_object_value, Unset):
            object_value = UNSET
        else:
            object_value = ValueClass.from_dict(_object_value)

        double_value = d.pop("doubleValue", UNSET)

        type = d.pop("type", UNSET)

        long_value = d.pop("longValue", UNSET)

        any_array = []
        _any_array = d.pop("anyArray", UNSET)
        for any_array_item_data in _any_array or []:
            any_array_item = Any.from_dict(any_array_item_data)

            any_array.append(any_array_item)

        any_ = cls(
            string_value=string_value,
            int_value=int_value,
            byte_array=byte_array,
            boolean_value=boolean_value,
            object_value=object_value,
            double_value=double_value,
            type=type,
            long_value=long_value,
            any_array=any_array,
        )

        any_.additional_properties = d
        return any_

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
