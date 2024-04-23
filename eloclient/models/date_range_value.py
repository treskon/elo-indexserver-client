from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_single_value import DateSingleValue


T = TypeVar("T", bound="DateRangeValue")


@_attrs_define
class DateRangeValue:
    """<p>
    Perform a range query with date values.
     </p>

     <p>
     Range queries for dates:<br>
     <ul>
     <li>If from contains a value for roundTo, it is always rounded down by roundTo.</li>
     <li>If to contains a value for roundTo, it is always rounded up by roundTo.</li>
     <li>If one of from or to is of type DateNowValue and contains a value for relative, it is always
     ignored for range queries.</li>
     <li>To perform an open range query (e.g. from now to infinite), only submit either a value for
     from or to</li>
     </ul>
     </p>

        Attributes:
            from_ (Union[Unset, DateSingleValue]):
            to (Union[Unset, DateSingleValue]):
    """

    from_: Union[Unset, "DateSingleValue"] = UNSET
    to: Union[Unset, "DateSingleValue"] = UNSET
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
        from ..models.date_single_value import DateSingleValue

        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, DateSingleValue]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = DateSingleValue.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, DateSingleValue]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = DateSingleValue.from_dict(_to)

        date_range_value = cls(
            from_=from_,
            to=to,
        )

        date_range_value.additional_properties = d
        return date_range_value

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
