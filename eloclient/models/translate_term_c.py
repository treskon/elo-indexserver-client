from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTermC")


@_attrs_define
class TranslateTermC:
    """Constants for class TranslateTerm.

    Attributes:
        guid_system_languages (Union[Unset, str]): Use this value in parameter <code>termIds[.]</code> to retrieve the
            system languages.
        ln_term_lang (Union[Unset, int]): Maximum term length;
        taskids_for_system_languages (Union[Unset, List[str]]):
        translation_key_regex (Union[Unset, str]): Allowed characters for {@link TranslateTerm#translationKey}.
            Only a-z, A-Z, 0-9 and forward
             slash, hyphen, underscore and colon are allowed.
        opt_languages (Union[Unset, str]): This user profile key stores the registered languages.
            The items are separated by dot and the
             order corresponds to the langN-fields in table &qt;translations&qt;. Example: &qt;de.en.fr&qt;
             EIX-3037
        default_languages (Union[Unset, List[str]]):
    """

    guid_system_languages: Union[Unset, str] = UNSET
    ln_term_lang: Union[Unset, int] = UNSET
    taskids_for_system_languages: Union[Unset, List[str]] = UNSET
    translation_key_regex: Union[Unset, str] = UNSET
    opt_languages: Union[Unset, str] = UNSET
    default_languages: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid_system_languages = self.guid_system_languages

        ln_term_lang = self.ln_term_lang

        taskids_for_system_languages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.taskids_for_system_languages, Unset):
            taskids_for_system_languages = self.taskids_for_system_languages

        translation_key_regex = self.translation_key_regex

        opt_languages = self.opt_languages

        default_languages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.default_languages, Unset):
            default_languages = self.default_languages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid_system_languages is not UNSET:
            field_dict["GUID_SYSTEM_LANGUAGES"] = guid_system_languages
        if ln_term_lang is not UNSET:
            field_dict["lnTermLang"] = ln_term_lang
        if taskids_for_system_languages is not UNSET:
            field_dict["TASKIDS_FOR_SYSTEM_LANGUAGES"] = taskids_for_system_languages
        if translation_key_regex is not UNSET:
            field_dict["TRANSLATION_KEY_REGEX"] = translation_key_regex
        if opt_languages is not UNSET:
            field_dict["OPT_LANGUAGES"] = opt_languages
        if default_languages is not UNSET:
            field_dict["DEFAULT_LANGUAGES"] = default_languages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid_system_languages = d.pop("GUID_SYSTEM_LANGUAGES", UNSET)

        ln_term_lang = d.pop("lnTermLang", UNSET)

        taskids_for_system_languages = cast(List[str], d.pop("TASKIDS_FOR_SYSTEM_LANGUAGES", UNSET))

        translation_key_regex = d.pop("TRANSLATION_KEY_REGEX", UNSET)

        opt_languages = d.pop("OPT_LANGUAGES", UNSET)

        default_languages = cast(List[str], d.pop("DEFAULT_LANGUAGES", UNSET))

        translate_term_c = cls(
            guid_system_languages=guid_system_languages,
            ln_term_lang=ln_term_lang,
            taskids_for_system_languages=taskids_for_system_languages,
            translation_key_regex=translation_key_regex,
            opt_languages=opt_languages,
            default_languages=default_languages,
        )

        translate_term_c.additional_properties = d
        return translate_term_c

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
