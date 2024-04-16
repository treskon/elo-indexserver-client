from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTerm")


@_attrs_define
class TranslateTerm:
    """Objects of this class represent one term in different languages.

    Attributes:
        deleted (Union[Unset, bool]): True, if this entry is logically deleted.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        translation_key (Union[Unset, str]): Optional language independent translation key.
            This value must match the regular expression
             {@link TranslateTermC#TRANSLATION_KEY_REGEX}.
        term_langs (Union[Unset, List[str]]):
        level (Union[Unset, int]): Priority level of this entry.
        t_stamp (Union[Unset, str]): Last modified. ISO date with seaparator "." measured in UTC.
        guid (Union[Unset, str]): GUID
        langs (Union[Unset, List[str]]):
        package_name (Union[Unset, str]): Configuration package.
    """

    deleted: Union[Unset, bool] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    translation_key: Union[Unset, str] = UNSET
    term_langs: Union[Unset, List[str]] = UNSET
    level: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    langs: Union[Unset, List[str]] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deleted = self.deleted

        t_stamp_sync = self.t_stamp_sync

        translation_key = self.translation_key

        term_langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.term_langs, Unset):
            term_langs = self.term_langs

        level = self.level

        t_stamp = self.t_stamp

        guid = self.guid

        langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.langs, Unset):
            langs = self.langs

        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if t_stamp_sync is not UNSET:
            field_dict["tStampSync"] = t_stamp_sync
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if term_langs is not UNSET:
            field_dict["termLangs"] = term_langs
        if level is not UNSET:
            field_dict["level"] = level
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if guid is not UNSET:
            field_dict["guid"] = guid
        if langs is not UNSET:
            field_dict["langs"] = langs
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deleted = d.pop("deleted", UNSET)

        t_stamp_sync = d.pop("tStampSync", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        term_langs = cast(List[str], d.pop("termLangs", UNSET))

        level = d.pop("level", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        guid = d.pop("guid", UNSET)

        langs = cast(List[str], d.pop("langs", UNSET))

        package_name = d.pop("packageName", UNSET)

        translate_term = cls(
            deleted=deleted,
            t_stamp_sync=t_stamp_sync,
            translation_key=translation_key,
            term_langs=term_langs,
            level=level,
            t_stamp=t_stamp,
            guid=guid,
            langs=langs,
            package_name=package_name,
        )

        translate_term.additional_properties = d
        return translate_term

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
