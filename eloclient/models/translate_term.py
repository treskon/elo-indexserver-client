from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTerm")


@_attrs_define
class TranslateTerm:
    """Objects of this class represent one term in different languages.

    Attributes:
        guid (Union[Unset, str]): GUID
        deleted (Union[Unset, bool]): True, if this entry is logically deleted.
        t_stamp (Union[Unset, str]): Last modified. ISO date with seaparator "." measured in UTC.
        term_langs (Union[Unset, List[str]]):
        langs (Union[Unset, List[str]]):
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        translation_key (Union[Unset, str]): Read-only member. The IX sets this member when a client searches for
            translation keys from property files.
    """

    guid: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    term_langs: Union[Unset, List[str]] = UNSET
    langs: Union[Unset, List[str]] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    translation_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        deleted = self.deleted
        t_stamp = self.t_stamp
        term_langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.term_langs, Unset):
            term_langs = self.term_langs

        langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.langs, Unset):
            langs = self.langs

        t_stamp_sync = self.t_stamp_sync
        translation_key = self.translation_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if term_langs is not UNSET:
            field_dict["termLangs"] = term_langs
        if langs is not UNSET:
            field_dict["langs"] = langs
        if t_stamp_sync is not UNSET:
            field_dict["tStampSync"] = t_stamp_sync
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("guid", UNSET)

        deleted = d.pop("deleted", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        term_langs = cast(List[str], d.pop("termLangs", UNSET))

        langs = cast(List[str], d.pop("langs", UNSET))

        t_stamp_sync = d.pop("tStampSync", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        translate_term = cls(
            guid=guid,
            deleted=deleted,
            t_stamp=t_stamp,
            term_langs=term_langs,
            langs=langs,
            t_stamp_sync=t_stamp_sync,
            translation_key=translation_key,
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
