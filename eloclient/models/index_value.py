from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexValue")


@_attrs_define
class IndexValue:
    """This class is a container for one value of a serializable type.
    It represents the value of an
     index line in aspect objects.

        Attributes:
            string_value (Union[Unset, str]): String value.
                <br>
                 This internal field is shared between several types.<br>
            int_value (Union[Unset, int]): Integer value.
            double_value (Union[Unset, float]): Double value.
            display_data (Union[Unset, str]): Human readable representation of value.
                This member is read-only and might not be set in
                 server-side events.<br>
                 For index fields of type {@link DocMaskLineC#TYPE_RELATION}, this member contains the
                 {@link Sord#name} of the referenced Sord.<br>
                 For index fields of type {@link AspectLineC#TYPE_STATUS}, this member contains, if present, the
                 translated value according to the client's locale.
            type (Union[Unset, int]): Type. One of the type constants given in IndexValueC.
    """

    string_value: Union[Unset, str] = UNSET
    int_value: Union[Unset, int] = UNSET
    double_value: Union[Unset, float] = UNSET
    display_data: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        string_value = self.string_value

        int_value = self.int_value

        double_value = self.double_value

        display_data = self.display_data

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if int_value is not UNSET:
            field_dict["intValue"] = int_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if display_data is not UNSET:
            field_dict["displayData"] = display_data
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        string_value = d.pop("stringValue", UNSET)

        int_value = d.pop("intValue", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        display_data = d.pop("displayData", UNSET)

        type = d.pop("type", UNSET)

        index_value = cls(
            string_value=string_value,
            int_value=int_value,
            double_value=double_value,
            display_data=display_data,
            type=type,
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
