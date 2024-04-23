from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContextTermReturnTypeE")


@_attrs_define
class ContextTermReturnTypeE:
    """Specifies the return type for context terms.

    Attributes:
        tokenized (Union[Unset, ContextTermReturnTypeE]): Specifies the return type for context terms.
        numeric_single_values (Union[Unset, ContextTermReturnTypeE]): Specifies the return type for context terms.
        numeric_buckets (Union[Unset, ContextTermReturnTypeE]): Specifies the return type for context terms.
        date_year_buckets (Union[Unset, ContextTermReturnTypeE]): Specifies the return type for context terms.
        not_tokenized (Union[Unset, ContextTermReturnTypeE]): Specifies the return type for context terms.
    """

    tokenized: Union[Unset, "ContextTermReturnTypeE"] = UNSET
    numeric_single_values: Union[Unset, "ContextTermReturnTypeE"] = UNSET
    numeric_buckets: Union[Unset, "ContextTermReturnTypeE"] = UNSET
    date_year_buckets: Union[Unset, "ContextTermReturnTypeE"] = UNSET
    not_tokenized: Union[Unset, "ContextTermReturnTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tokenized: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tokenized, Unset):
            tokenized = self.tokenized.to_dict()

        numeric_single_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.numeric_single_values, Unset):
            numeric_single_values = self.numeric_single_values.to_dict()

        numeric_buckets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.numeric_buckets, Unset):
            numeric_buckets = self.numeric_buckets.to_dict()

        date_year_buckets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_year_buckets, Unset):
            date_year_buckets = self.date_year_buckets.to_dict()

        not_tokenized: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.not_tokenized, Unset):
            not_tokenized = self.not_tokenized.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tokenized is not UNSET:
            field_dict["tokenized"] = tokenized
        if numeric_single_values is not UNSET:
            field_dict["numericSingleValues"] = numeric_single_values
        if numeric_buckets is not UNSET:
            field_dict["numericBuckets"] = numeric_buckets
        if date_year_buckets is not UNSET:
            field_dict["dateYearBuckets"] = date_year_buckets
        if not_tokenized is not UNSET:
            field_dict["notTokenized"] = not_tokenized

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tokenized = d.pop("tokenized", UNSET)
        tokenized: Union[Unset, ContextTermReturnTypeE]
        if isinstance(_tokenized, Unset):
            tokenized = UNSET
        else:
            tokenized = ContextTermReturnTypeE.from_dict(_tokenized)

        _numeric_single_values = d.pop("numericSingleValues", UNSET)
        numeric_single_values: Union[Unset, ContextTermReturnTypeE]
        if isinstance(_numeric_single_values, Unset):
            numeric_single_values = UNSET
        else:
            numeric_single_values = ContextTermReturnTypeE.from_dict(_numeric_single_values)

        _numeric_buckets = d.pop("numericBuckets", UNSET)
        numeric_buckets: Union[Unset, ContextTermReturnTypeE]
        if isinstance(_numeric_buckets, Unset):
            numeric_buckets = UNSET
        else:
            numeric_buckets = ContextTermReturnTypeE.from_dict(_numeric_buckets)

        _date_year_buckets = d.pop("dateYearBuckets", UNSET)
        date_year_buckets: Union[Unset, ContextTermReturnTypeE]
        if isinstance(_date_year_buckets, Unset):
            date_year_buckets = UNSET
        else:
            date_year_buckets = ContextTermReturnTypeE.from_dict(_date_year_buckets)

        _not_tokenized = d.pop("notTokenized", UNSET)
        not_tokenized: Union[Unset, ContextTermReturnTypeE]
        if isinstance(_not_tokenized, Unset):
            not_tokenized = UNSET
        else:
            not_tokenized = ContextTermReturnTypeE.from_dict(_not_tokenized)

        context_term_return_type_e = cls(
            tokenized=tokenized,
            numeric_single_values=numeric_single_values,
            numeric_buckets=numeric_buckets,
            date_year_buckets=date_year_buckets,
            not_tokenized=not_tokenized,
        )

        context_term_return_type_e.additional_properties = d
        return context_term_return_type_e

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
