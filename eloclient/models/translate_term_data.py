from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTermData")


@_attrs_define
class TranslateTermData:
    """
    Attributes:
        guid (Union[Unset, str]): GUID
        t_stamp (Union[Unset, str]): Timestamp. Last mofified time, ISO date with dots measured in UTC The format is
            JJJJ.MM.DD.hh.mm.
            ss
        status (Union[Unset, int]): Status. The object is not deleted, if <code>status</code> is -1.
        lang1 (Union[Unset, str]): Language 1. System language.
        lang2 (Union[Unset, str]): Language 2
        lang3 (Union[Unset, str]): Language 3
        lang4 (Union[Unset, str]): Language 4
        lang5 (Union[Unset, str]): Language 5
        lang6 (Union[Unset, str]): Language 6
        lang7 (Union[Unset, str]): Language 7
        lang8 (Union[Unset, str]): Language 8
        lang9 (Union[Unset, str]): Language 9
        t_stamp_sync (Union[Unset, str]): Timestamp. Timestamp of this object's last export by the replication. The
            format is JJJJ.MM.DD.hh.mm.
            ss
    """

    guid: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    lang1: Union[Unset, str] = UNSET
    lang2: Union[Unset, str] = UNSET
    lang3: Union[Unset, str] = UNSET
    lang4: Union[Unset, str] = UNSET
    lang5: Union[Unset, str] = UNSET
    lang6: Union[Unset, str] = UNSET
    lang7: Union[Unset, str] = UNSET
    lang8: Union[Unset, str] = UNSET
    lang9: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        t_stamp = self.t_stamp
        status = self.status
        lang1 = self.lang1
        lang2 = self.lang2
        lang3 = self.lang3
        lang4 = self.lang4
        lang5 = self.lang5
        lang6 = self.lang6
        lang7 = self.lang7
        lang8 = self.lang8
        lang9 = self.lang9
        t_stamp_sync = self.t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if status is not UNSET:
            field_dict["status"] = status
        if lang1 is not UNSET:
            field_dict["lang1"] = lang1
        if lang2 is not UNSET:
            field_dict["lang2"] = lang2
        if lang3 is not UNSET:
            field_dict["lang3"] = lang3
        if lang4 is not UNSET:
            field_dict["lang4"] = lang4
        if lang5 is not UNSET:
            field_dict["lang5"] = lang5
        if lang6 is not UNSET:
            field_dict["lang6"] = lang6
        if lang7 is not UNSET:
            field_dict["lang7"] = lang7
        if lang8 is not UNSET:
            field_dict["lang8"] = lang8
        if lang9 is not UNSET:
            field_dict["lang9"] = lang9
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("guid", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        status = d.pop("status", UNSET)

        lang1 = d.pop("lang1", UNSET)

        lang2 = d.pop("lang2", UNSET)

        lang3 = d.pop("lang3", UNSET)

        lang4 = d.pop("lang4", UNSET)

        lang5 = d.pop("lang5", UNSET)

        lang6 = d.pop("lang6", UNSET)

        lang7 = d.pop("lang7", UNSET)

        lang8 = d.pop("lang8", UNSET)

        lang9 = d.pop("lang9", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        translate_term_data = cls(
            guid=guid,
            t_stamp=t_stamp,
            status=status,
            lang1=lang1,
            lang2=lang2,
            lang3=lang3,
            lang4=lang4,
            lang5=lang5,
            lang6=lang6,
            lang7=lang7,
            lang8=lang8,
            lang9=lang9,
            t_stamp_sync=t_stamp_sync,
        )

        translate_term_data.additional_properties = d
        return translate_term_data

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
