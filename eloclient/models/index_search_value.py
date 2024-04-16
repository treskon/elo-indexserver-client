from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_search_double_value import IndexSearchDoubleValue
    from ..models.index_search_integer_value import IndexSearchIntegerValue
    from ..models.index_search_string_value import IndexSearchStringValue


T = TypeVar("T", bound="IndexSearchValue")


@_attrs_define
class IndexSearchValue:
    """This class is used to search for index values in aspect objects.
    Regardless of whether the
     search-mode is set to {@link SearchModeC#OR}, all of the conditions defined in this class must be
     met. In other words, the server will evaluate all the conditions in this class in a
     "<tt>???</tt>" manner.<br>
     Please not that you must use the correct field according to the aspect's line type. The
     Indexserver will not evaluate other fields. That means that if the aspect's line type is
     {@link AspectLineC#TYPE_DOUBLE}, the Indexserver will look at {@link #doubleValue} and
     {@link #doubleValues} only.

        Attributes:
            int_values (Union[Unset, List['IndexSearchIntegerValue']]):
            string_value (Union[Unset, IndexSearchStringValue]): This class represents a condition to filter aspect data
                that is not of type
                {@link IndexValueC#TYPE_INT} or {@link IndexValueC#TYPE_DOUBLE} in the database.
            string_values (Union[Unset, List['IndexSearchStringValue']]):
            double_values (Union[Unset, List['IndexSearchDoubleValue']]):
            int_value (Union[Unset, IndexSearchIntegerValue]): This class represents a condition to filter aspect data of
                type {@link IndexValueC#TYPE_INT} in
                the database.
            double_value (Union[Unset, IndexSearchDoubleValue]): This class represents a condition to filter aspect data of
                type {@link IndexValueC#TYPE_DOUBLE}
                in the database.
    """

    int_values: Union[Unset, List["IndexSearchIntegerValue"]] = UNSET
    string_value: Union[Unset, "IndexSearchStringValue"] = UNSET
    string_values: Union[Unset, List["IndexSearchStringValue"]] = UNSET
    double_values: Union[Unset, List["IndexSearchDoubleValue"]] = UNSET
    int_value: Union[Unset, "IndexSearchIntegerValue"] = UNSET
    double_value: Union[Unset, "IndexSearchDoubleValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        int_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.int_values, Unset):
            int_values = []
            for componentsschemas_list_of_index_search_integer_value_item_data in self.int_values:
                componentsschemas_list_of_index_search_integer_value_item = (
                    componentsschemas_list_of_index_search_integer_value_item_data.to_dict()
                )
                int_values.append(componentsschemas_list_of_index_search_integer_value_item)

        string_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.string_value, Unset):
            string_value = self.string_value.to_dict()

        string_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.string_values, Unset):
            string_values = []
            for componentsschemas_list_of_index_search_string_value_item_data in self.string_values:
                componentsschemas_list_of_index_search_string_value_item = (
                    componentsschemas_list_of_index_search_string_value_item_data.to_dict()
                )
                string_values.append(componentsschemas_list_of_index_search_string_value_item)

        double_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.double_values, Unset):
            double_values = []
            for componentsschemas_list_of_index_search_double_value_item_data in self.double_values:
                componentsschemas_list_of_index_search_double_value_item = (
                    componentsschemas_list_of_index_search_double_value_item_data.to_dict()
                )
                double_values.append(componentsschemas_list_of_index_search_double_value_item)

        int_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.int_value, Unset):
            int_value = self.int_value.to_dict()

        double_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.double_value, Unset):
            double_value = self.double_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if int_values is not UNSET:
            field_dict["intValues"] = int_values
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if string_values is not UNSET:
            field_dict["stringValues"] = string_values
        if double_values is not UNSET:
            field_dict["doubleValues"] = double_values
        if int_value is not UNSET:
            field_dict["intValue"] = int_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.index_search_double_value import IndexSearchDoubleValue
        from ..models.index_search_integer_value import IndexSearchIntegerValue
        from ..models.index_search_string_value import IndexSearchStringValue

        d = src_dict.copy()
        int_values = []
        _int_values = d.pop("intValues", UNSET)
        for componentsschemas_list_of_index_search_integer_value_item_data in _int_values or []:
            componentsschemas_list_of_index_search_integer_value_item = IndexSearchIntegerValue.from_dict(
                componentsschemas_list_of_index_search_integer_value_item_data
            )

            int_values.append(componentsschemas_list_of_index_search_integer_value_item)

        _string_value = d.pop("stringValue", UNSET)
        string_value: Union[Unset, IndexSearchStringValue]
        if isinstance(_string_value, Unset):
            string_value = UNSET
        else:
            string_value = IndexSearchStringValue.from_dict(_string_value)

        string_values = []
        _string_values = d.pop("stringValues", UNSET)
        for componentsschemas_list_of_index_search_string_value_item_data in _string_values or []:
            componentsschemas_list_of_index_search_string_value_item = IndexSearchStringValue.from_dict(
                componentsschemas_list_of_index_search_string_value_item_data
            )

            string_values.append(componentsschemas_list_of_index_search_string_value_item)

        double_values = []
        _double_values = d.pop("doubleValues", UNSET)
        for componentsschemas_list_of_index_search_double_value_item_data in _double_values or []:
            componentsschemas_list_of_index_search_double_value_item = IndexSearchDoubleValue.from_dict(
                componentsschemas_list_of_index_search_double_value_item_data
            )

            double_values.append(componentsschemas_list_of_index_search_double_value_item)

        _int_value = d.pop("intValue", UNSET)
        int_value: Union[Unset, IndexSearchIntegerValue]
        if isinstance(_int_value, Unset):
            int_value = UNSET
        else:
            int_value = IndexSearchIntegerValue.from_dict(_int_value)

        _double_value = d.pop("doubleValue", UNSET)
        double_value: Union[Unset, IndexSearchDoubleValue]
        if isinstance(_double_value, Unset):
            double_value = UNSET
        else:
            double_value = IndexSearchDoubleValue.from_dict(_double_value)

        index_search_value = cls(
            int_values=int_values,
            string_value=string_value,
            string_values=string_values,
            double_values=double_values,
            int_value=int_value,
            double_value=double_value,
        )

        index_search_value.additional_properties = d
        return index_search_value

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
