from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorType")


@_attrs_define
class OperatorType:
    """Operator type to combine search terms.

    Attributes:
        not_ (Union[Unset, OperatorType]): Operator type to combine search terms.
        or_ (Union[Unset, OperatorType]): Operator type to combine search terms.
        and_ (Union[Unset, OperatorType]): Operator type to combine search terms.
    """

    not_: Union[Unset, "OperatorType"] = UNSET
    or_: Union[Unset, "OperatorType"] = UNSET
    and_: Union[Unset, "OperatorType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        not_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.not_, Unset):
            not_ = self.not_.to_dict()

        or_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.or_, Unset):
            or_ = self.or_.to_dict()

        and_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.and_, Unset):
            and_ = self.and_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if not_ is not UNSET:
            field_dict["NOT"] = not_
        if or_ is not UNSET:
            field_dict["OR"] = or_
        if and_ is not UNSET:
            field_dict["AND"] = and_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _not_ = d.pop("NOT", UNSET)
        not_: Union[Unset, OperatorType]
        if isinstance(_not_, Unset):
            not_ = UNSET
        else:
            not_ = OperatorType.from_dict(_not_)

        _or_ = d.pop("OR", UNSET)
        or_: Union[Unset, OperatorType]
        if isinstance(_or_, Unset):
            or_ = UNSET
        else:
            or_ = OperatorType.from_dict(_or_)

        _and_ = d.pop("AND", UNSET)
        and_: Union[Unset, OperatorType]
        if isinstance(_and_, Unset):
            and_ = UNSET
        else:
            and_ = OperatorType.from_dict(_and_)

        operator_type = cls(
            not_=not_,
            or_=or_,
            and_=and_,
        )

        operator_type.additional_properties = d
        return operator_type

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
