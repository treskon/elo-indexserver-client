from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString


T = TypeVar("T", bound="LanguageConfig")


@_attrs_define
class LanguageConfig:
    """
    Attributes:
        languages (Union[Unset, str]):
        allowed_langs (Union[Unset, str]):
        nb_of_langs (Union[Unset, int]):
        archive_lang (Union[Unset, str]):
        map_language_names (Union[Unset, MapToString]):
    """

    languages: Union[Unset, str] = UNSET
    allowed_langs: Union[Unset, str] = UNSET
    nb_of_langs: Union[Unset, int] = UNSET
    archive_lang: Union[Unset, str] = UNSET
    map_language_names: Union[Unset, "MapToString"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        languages = self.languages

        allowed_langs = self.allowed_langs

        nb_of_langs = self.nb_of_langs

        archive_lang = self.archive_lang

        map_language_names: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_language_names, Unset):
            map_language_names = self.map_language_names.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if languages is not UNSET:
            field_dict["languages"] = languages
        if allowed_langs is not UNSET:
            field_dict["allowedLangs"] = allowed_langs
        if nb_of_langs is not UNSET:
            field_dict["nbOfLangs"] = nb_of_langs
        if archive_lang is not UNSET:
            field_dict["archiveLang"] = archive_lang
        if map_language_names is not UNSET:
            field_dict["mapLanguageNames"] = map_language_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        languages = d.pop("languages", UNSET)

        allowed_langs = d.pop("allowedLangs", UNSET)

        nb_of_langs = d.pop("nbOfLangs", UNSET)

        archive_lang = d.pop("archiveLang", UNSET)

        _map_language_names = d.pop("mapLanguageNames", UNSET)
        map_language_names: Union[Unset, MapToString]
        if isinstance(_map_language_names, Unset):
            map_language_names = UNSET
        else:
            map_language_names = MapToString.from_dict(_map_language_names)

        language_config = cls(
            languages=languages,
            allowed_langs=allowed_langs,
            nb_of_langs=nb_of_langs,
            archive_lang=archive_lang,
            map_language_names=map_language_names,
        )

        language_config.additional_properties = d
        return language_config

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
