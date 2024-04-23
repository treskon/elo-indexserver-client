from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.int_single_value import IntSingleValue


T = TypeVar("T", bound="IntRangeValue")


@_attrs_define
class IntRangeValue:
    """<p>
    Class to commit a range filter of integer values.
     </p>

     <p>
     To perform an open range query (e.g. from now to infinite), only submit either a value for from
     or to
     </p>

        Attributes:
            from_ (Union[Unset, IntSingleValue]):
            to (Union[Unset, IntSingleValue]):
    """

    from_: Union[Unset, "IntSingleValue"] = UNSET
    to: Union[Unset, "IntSingleValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.int_single_value import IntSingleValue

        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, IntSingleValue]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = IntSingleValue.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, IntSingleValue]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = IntSingleValue.from_dict(_to)

        int_range_value = cls(
            from_=from_,
            to=to,
        )

        int_range_value.additional_properties = d
        return int_range_value

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
