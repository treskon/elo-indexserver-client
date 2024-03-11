from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindTranslateTermInfo")


@_attrs_define
class FindTranslateTermInfo:
    """This class is used to find translations of terms.

    Attributes:
        terms (Union[Unset, List[str]]):
        langs (Union[Unset, List[str]]):
        incl_deleted (Union[Unset, bool]): Reserved - Find deleted terms too (currently not implemented).
        incl_to_be_translated (Union[Unset, bool]): Return those terms too, that should be translated into other
            languages: e.g. Keywording form names (DocMask.
            name),
             index value lables (DocMaskLine.name) and Keywords.
    """

    terms: Union[Unset, List[str]] = UNSET
    langs: Union[Unset, List[str]] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    incl_to_be_translated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        terms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms

        langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.langs, Unset):
            langs = self.langs

        incl_deleted = self.incl_deleted
        incl_to_be_translated = self.incl_to_be_translated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terms is not UNSET:
            field_dict["terms"] = terms
        if langs is not UNSET:
            field_dict["langs"] = langs
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted
        if incl_to_be_translated is not UNSET:
            field_dict["inclToBeTranslated"] = incl_to_be_translated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        terms = cast(List[str], d.pop("terms", UNSET))

        langs = cast(List[str], d.pop("langs", UNSET))

        incl_deleted = d.pop("inclDeleted", UNSET)

        incl_to_be_translated = d.pop("inclToBeTranslated", UNSET)

        find_translate_term_info = cls(
            terms=terms,
            langs=langs,
            incl_deleted=incl_deleted,
            incl_to_be_translated=incl_to_be_translated,
        )

        find_translate_term_info.additional_properties = d
        return find_translate_term_info

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
