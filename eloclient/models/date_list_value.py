from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_value import DateValue


T = TypeVar("T", bound="DateListValue")


@_attrs_define
class DateListValue:
    """A list of date values which is joined by AND or OR depending on
    <code>andOpeDoubleListrator</code>.<br>
     Defaults to an OR-disjunction.

        Attributes:
            value_list (Union[Unset, List['DateValue']]):
            and_operator (Union[Unset, bool]): Connective of list elements (default is OR (=false) ).
    """

    value_list: Union[Unset, List["DateValue"]] = UNSET
    and_operator: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.value_list, Unset):
            value_list = []
            for componentsschemas_list_of_date_value_item_data in self.value_list:
                componentsschemas_list_of_date_value_item = componentsschemas_list_of_date_value_item_data.to_dict()
                value_list.append(componentsschemas_list_of_date_value_item)

        and_operator = self.and_operator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_list is not UNSET:
            field_dict["valueList"] = value_list
        if and_operator is not UNSET:
            field_dict["andOperator"] = and_operator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_value import DateValue

        d = src_dict.copy()
        value_list = []
        _value_list = d.pop("valueList", UNSET)
        for componentsschemas_list_of_date_value_item_data in _value_list or []:
            componentsschemas_list_of_date_value_item = DateValue.from_dict(
                componentsschemas_list_of_date_value_item_data
            )

            value_list.append(componentsschemas_list_of_date_value_item)

        and_operator = d.pop("andOperator", UNSET)

        date_list_value = cls(
            value_list=value_list,
            and_operator=and_operator,
        )

        date_list_value.additional_properties = d
        return date_list_value

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
