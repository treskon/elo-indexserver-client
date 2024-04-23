from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindTranslateTermInfo")


@_attrs_define
class FindTranslateTermInfo:
    """This class is used to find translations of terms.
    Localization information is stored in two kinds of storage: in the database and in property files
     in the repository. The former kind use the database table <code>translations</code> which has a
     column for each language. This localization data can be modified or extended via API function
     {@link IXServicePortIF#checkinTranslateTerms(ClientInfo, TranslateTerm[], LockZ)}. The latter
     kind stores localization as property files under /Administration/Localization. This data can only
     be changed via checkin/out and takes effect only after Indexserver re-start.

     Indexserver function
     {@link IXServicePortIF#findFirstTranslateTerms(ClientInfo, FindTranslateTermInfo, int)} searches
     over both localization sources and returns matches from both. The translations found in the
     database are returned first.

     EIX-2912: Since IX version 21.3, a language is specified as IETF language tag (lang). The
     language part is from ISO 639-1. It is optionally followed by a country tag from ISO 3166-1
     alpha-2. The parts are separated by hyphen. Examples: de-DE, de-CH, de-AT. The function tries to
     find the translation for a given lang in the following order:

     <pre>
     1. lang as defined, e.g. de-CH
     2. lang without country, e.g. de
     3. first lang with the same language tag, e.g. de-DE
     4. first system language
     </pre>

        Attributes:
            disable_fallback (Union[Unset, bool]): Disable fallback to default language if a key in {@link
                #translationKeyPrefixes} is not found.
                If there is no translation term associated to a key for a language in {@link #langs}, an empty
                 String is returned in the corresponding {@link FindResult#translateTerms}.

                 EIX-3008
            translation_key_prefixes (Union[Unset, List[str]]):
            terms (Union[Unset, List[str]]):
            level (Union[Unset, int]): Find terms of this priority level. If 0 (default), return the terms with the highest
                level.
            langs (Union[Unset, List[str]]):
            incl_to_be_translated (Union[Unset, bool]): Return those terms too, that should be translated into other
                languages: e.g.
                Keywording form
                 names (DocMask.name), index value lables (DocMaskLine.name) and Keywords.
            package_name (Union[Unset, str]): Package GUID.
            incl_deleted (Union[Unset, bool]): Reserved - Find deleted terms too (currently not implemented).
    """

    disable_fallback: Union[Unset, bool] = UNSET
    translation_key_prefixes: Union[Unset, List[str]] = UNSET
    terms: Union[Unset, List[str]] = UNSET
    level: Union[Unset, int] = UNSET
    langs: Union[Unset, List[str]] = UNSET
    incl_to_be_translated: Union[Unset, bool] = UNSET
    package_name: Union[Unset, str] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disable_fallback = self.disable_fallback

        translation_key_prefixes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.translation_key_prefixes, Unset):
            translation_key_prefixes = self.translation_key_prefixes

        terms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms

        level = self.level

        langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.langs, Unset):
            langs = self.langs

        incl_to_be_translated = self.incl_to_be_translated

        package_name = self.package_name

        incl_deleted = self.incl_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_fallback is not UNSET:
            field_dict["disableFallback"] = disable_fallback
        if translation_key_prefixes is not UNSET:
            field_dict["translationKeyPrefixes"] = translation_key_prefixes
        if terms is not UNSET:
            field_dict["terms"] = terms
        if level is not UNSET:
            field_dict["level"] = level
        if langs is not UNSET:
            field_dict["langs"] = langs
        if incl_to_be_translated is not UNSET:
            field_dict["inclToBeTranslated"] = incl_to_be_translated
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disable_fallback = d.pop("disableFallback", UNSET)

        translation_key_prefixes = cast(List[str], d.pop("translationKeyPrefixes", UNSET))

        terms = cast(List[str], d.pop("terms", UNSET))

        level = d.pop("level", UNSET)

        langs = cast(List[str], d.pop("langs", UNSET))

        incl_to_be_translated = d.pop("inclToBeTranslated", UNSET)

        package_name = d.pop("packageName", UNSET)

        incl_deleted = d.pop("inclDeleted", UNSET)

        find_translate_term_info = cls(
            disable_fallback=disable_fallback,
            translation_key_prefixes=translation_key_prefixes,
            terms=terms,
            level=level,
            langs=langs,
            incl_to_be_translated=incl_to_be_translated,
            package_name=package_name,
            incl_deleted=incl_deleted,
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
