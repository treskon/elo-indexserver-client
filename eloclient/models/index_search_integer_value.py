from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_search_operator import IndexSearchOperator


T = TypeVar("T", bound="IndexSearchIntegerValue")


@_attrs_define
class IndexSearchIntegerValue:
    """This class represents a condition to filter aspect data of type {@link IndexValueC#TYPE_INT} in
    the database.

        Attributes:
            operator (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            operand (Union[Unset, int]): Value on the right side of the operation.
                The left side implicitly is the value in the
                 database.
    """

    operator: Union[Unset, "IndexSearchOperator"] = UNSET
    operand: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        operand = self.operand

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operator is not UNSET:
            field_dict["operator"] = operator
        if operand is not UNSET:
            field_dict["operand"] = operand

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.index_search_operator import IndexSearchOperator

        d = src_dict.copy()
        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, IndexSearchOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = IndexSearchOperator.from_dict(_operator)

        operand = d.pop("operand", UNSET)

        index_search_integer_value = cls(
            operator=operator,
            operand=operand,
        )

        index_search_integer_value.additional_properties = d
        return index_search_integer_value

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
