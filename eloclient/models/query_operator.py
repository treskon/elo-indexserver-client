from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operator_type import OperatorType


T = TypeVar("T", bound="QueryOperator")


@_attrs_define
class QueryOperator:
    """A QueryOperator is used to include or exclude QueryObjects from a search and to concatenate
    QueryObjects.<br>
     Like this, complex queries can be build.

        Attributes:
            operator_type (Union[Unset, OperatorType]): Operator type to combine search terms.
    """

    operator_type: Union[Unset, "OperatorType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operator_type, Unset):
            operator_type = self.operator_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operator_type is not UNSET:
            field_dict["operatorType"] = operator_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operator_type import OperatorType

        d = src_dict.copy()
        _operator_type = d.pop("operatorType", UNSET)
        operator_type: Union[Unset, OperatorType]
        if isinstance(_operator_type, Unset):
            operator_type = UNSET
        else:
            operator_type = OperatorType.from_dict(_operator_type)

        query_operator = cls(
            operator_type=operator_type,
        )

        query_operator.additional_properties = d
        return query_operator

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
