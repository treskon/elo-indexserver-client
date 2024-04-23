from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SortOrderSequenceE")


@_attrs_define
class SortOrderSequenceE:
    """Possible sorting sequences of database searches for aspect data.

    Attributes:
        ascending (Union[Unset, SortOrderSequenceE]): Possible sorting sequences of database searches for aspect data.
        descending (Union[Unset, SortOrderSequenceE]): Possible sorting sequences of database searches for aspect data.
        descending_nulls_last (Union[Unset, SortOrderSequenceE]): Possible sorting sequences of database searches for
            aspect data.
        ascending_nulls_first (Union[Unset, SortOrderSequenceE]): Possible sorting sequences of database searches for
            aspect data.
    """

    ascending: Union[Unset, "SortOrderSequenceE"] = UNSET
    descending: Union[Unset, "SortOrderSequenceE"] = UNSET
    descending_nulls_last: Union[Unset, "SortOrderSequenceE"] = UNSET
    ascending_nulls_first: Union[Unset, "SortOrderSequenceE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ascending: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ascending, Unset):
            ascending = self.ascending.to_dict()

        descending: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descending, Unset):
            descending = self.descending.to_dict()

        descending_nulls_last: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descending_nulls_last, Unset):
            descending_nulls_last = self.descending_nulls_last.to_dict()

        ascending_nulls_first: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ascending_nulls_first, Unset):
            ascending_nulls_first = self.ascending_nulls_first.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ascending is not UNSET:
            field_dict["ASCENDING"] = ascending
        if descending is not UNSET:
            field_dict["DESCENDING"] = descending
        if descending_nulls_last is not UNSET:
            field_dict["DESCENDING_NULLS_LAST"] = descending_nulls_last
        if ascending_nulls_first is not UNSET:
            field_dict["ASCENDING_NULLS_FIRST"] = ascending_nulls_first

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ascending = d.pop("ASCENDING", UNSET)
        ascending: Union[Unset, SortOrderSequenceE]
        if isinstance(_ascending, Unset):
            ascending = UNSET
        else:
            ascending = SortOrderSequenceE.from_dict(_ascending)

        _descending = d.pop("DESCENDING", UNSET)
        descending: Union[Unset, SortOrderSequenceE]
        if isinstance(_descending, Unset):
            descending = UNSET
        else:
            descending = SortOrderSequenceE.from_dict(_descending)

        _descending_nulls_last = d.pop("DESCENDING_NULLS_LAST", UNSET)
        descending_nulls_last: Union[Unset, SortOrderSequenceE]
        if isinstance(_descending_nulls_last, Unset):
            descending_nulls_last = UNSET
        else:
            descending_nulls_last = SortOrderSequenceE.from_dict(_descending_nulls_last)

        _ascending_nulls_first = d.pop("ASCENDING_NULLS_FIRST", UNSET)
        ascending_nulls_first: Union[Unset, SortOrderSequenceE]
        if isinstance(_ascending_nulls_first, Unset):
            ascending_nulls_first = UNSET
        else:
            ascending_nulls_first = SortOrderSequenceE.from_dict(_ascending_nulls_first)

        sort_order_sequence_e = cls(
            ascending=ascending,
            descending=descending,
            descending_nulls_last=descending_nulls_last,
            ascending_nulls_first=ascending_nulls_first,
        )

        sort_order_sequence_e.additional_properties = d
        return sort_order_sequence_e

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
