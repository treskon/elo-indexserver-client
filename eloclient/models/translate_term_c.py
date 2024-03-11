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
        taskids_for_system_languages (Union[Unset, List[str]]):
        ln_term_lang (Union[Unset, int]): Maximum term length;
    """

    guid_system_languages: Union[Unset, str] = UNSET
    taskids_for_system_languages: Union[Unset, List[str]] = UNSET
    ln_term_lang: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid_system_languages = self.guid_system_languages
        taskids_for_system_languages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.taskids_for_system_languages, Unset):
            taskids_for_system_languages = self.taskids_for_system_languages

        ln_term_lang = self.ln_term_lang

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid_system_languages is not UNSET:
            field_dict["GUID_SYSTEM_LANGUAGES"] = guid_system_languages
        if taskids_for_system_languages is not UNSET:
            field_dict["TASKIDS_FOR_SYSTEM_LANGUAGES"] = taskids_for_system_languages
        if ln_term_lang is not UNSET:
            field_dict["lnTermLang"] = ln_term_lang

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid_system_languages = d.pop("GUID_SYSTEM_LANGUAGES", UNSET)

        taskids_for_system_languages = cast(List[str], d.pop("TASKIDS_FOR_SYSTEM_LANGUAGES", UNSET))

        ln_term_lang = d.pop("lnTermLang", UNSET)

        translate_term_c = cls(
            guid_system_languages=guid_system_languages,
            taskids_for_system_languages=taskids_for_system_languages,
            ln_term_lang=ln_term_lang,
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
