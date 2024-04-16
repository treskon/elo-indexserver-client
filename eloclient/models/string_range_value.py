from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.string_single_value import StringSingleValue


T = TypeVar("T", bound="StringRangeValue")


@_attrs_define
class StringRangeValue:
    """<p>
    Class to commit a range filter of String values.
     </p>

     <p>
     To perform an open range query (e.g. from now to infinite), only submit either a value for from
     or to
     </p>

        Attributes:
            from_ (Union[Unset, StringSingleValue]):
            to (Union[Unset, StringSingleValue]):
    """

    from_: Union[Unset, "StringSingleValue"] = UNSET
    to: Union[Unset, "StringSingleValue"] = UNSET
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
        from ..models.string_single_value import StringSingleValue

        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, StringSingleValue]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = StringSingleValue.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, StringSingleValue]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = StringSingleValue.from_dict(_to)

        string_range_value = cls(
            from_=from_,
            to=to,
        )

        string_range_value.additional_properties = d
        return string_range_value

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
