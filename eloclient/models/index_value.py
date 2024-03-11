from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexValue")


@_attrs_define
class IndexValue:
    """This class is a container for one value of a serializable type.
    It represents the value of an index line in aspect
     objects.

        Attributes:
            type (Union[Unset, int]): Type. One of the type constants given in IndexValueC.
            int_value (Union[Unset, int]): Integer value.
            double_value (Union[Unset, float]): Double value.
            string_value (Union[Unset, str]): String value.
            display_data (Union[Unset, str]): Human readable representation of value. This member is read-only and might not
                be set in server-side events.
                For
                 index lines of type {@link DocMaskLineC#TYPE_RELATION}, this member contains the {@link Sord#name} of the
                 referenced Sord.
    """

    type: Union[Unset, int] = UNSET
    int_value: Union[Unset, int] = UNSET
    double_value: Union[Unset, float] = UNSET
    string_value: Union[Unset, str] = UNSET
    display_data: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        int_value = self.int_value
        double_value = self.double_value
        string_value = self.string_value
        display_data = self.display_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if int_value is not UNSET:
            field_dict["intValue"] = int_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if display_data is not UNSET:
            field_dict["displayData"] = display_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        int_value = d.pop("intValue", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        string_value = d.pop("stringValue", UNSET)

        display_data = d.pop("displayData", UNSET)

        index_value = cls(
            type=type,
            int_value=int_value,
            double_value=double_value,
            string_value=string_value,
            display_data=display_data,
        )

        index_value.additional_properties = d
        return index_value

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
