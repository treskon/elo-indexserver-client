from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchTermsC")


@_attrs_define
class SearchTermsC:
    """
    Attributes:
        terms (Union[Unset, int]):
        synonyms (Union[Unset, int]):
        correction (Union[Unset, int]):
    """

    terms: Union[Unset, int] = UNSET
    synonyms: Union[Unset, int] = UNSET
    correction: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        terms = self.terms
        synonyms = self.synonyms
        correction = self.correction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terms is not UNSET:
            field_dict["TERMS"] = terms
        if synonyms is not UNSET:
            field_dict["SYNONYMS"] = synonyms
        if correction is not UNSET:
            field_dict["CORRECTION"] = correction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        terms = d.pop("TERMS", UNSET)

        synonyms = d.pop("SYNONYMS", UNSET)

        correction = d.pop("CORRECTION", UNSET)

        search_terms_c = cls(
            terms=terms,
            synonyms=synonyms,
            correction=correction,
        )

        search_terms_c.additional_properties = d
        return search_terms_c

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
