from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTermData")


@_attrs_define
class TranslateTermData:
    """
    Attributes:
        lang18 (Union[Unset, str]): Language 18
        lang17 (Union[Unset, str]): Language 17
        lang19 (Union[Unset, str]): Language 19
        translation_key (Union[Unset, str]): Language independent translation key.
        lang14 (Union[Unset, str]): Language 14
        lang13 (Union[Unset, str]): Language 13
        lang16 (Union[Unset, str]): Language 16
        lang15 (Union[Unset, str]): Language 15
        t_stamp (Union[Unset, str]): Timestamp.
            Last mofified time, ISO date with dots measured in UTC The format is
             JJJJ.MM.DD.hh.mm.ss
        lang9 (Union[Unset, str]): Language 9
        lang8 (Union[Unset, str]): Language 8
        t_stamp_sync (Union[Unset, str]): Timestamp. Timestamp of this object's last export by the replication.
            The format is
             JJJJ.MM.DD.hh.mm.ss
        lang7 (Union[Unset, str]): Language 7
        lang6 (Union[Unset, str]): Language 6
        lang5 (Union[Unset, str]): Language 5
        lang10 (Union[Unset, str]): Language 10
        lang4 (Union[Unset, str]): Language 4
        lang3 (Union[Unset, str]): Language 3
        lang12 (Union[Unset, str]): Language 12
        lang2 (Union[Unset, str]): Language 2
        package_name (Union[Unset, str]): Configuration package.
        lang11 (Union[Unset, str]): Language 11
        lang1 (Union[Unset, str]): Language 1. System language.
        lang30 (Union[Unset, str]): Language 30
        lang29 (Union[Unset, str]): Language 29
        lang28 (Union[Unset, str]): Language 28
        lang25 (Union[Unset, str]): Language 25
        level (Union[Unset, int]): Priority level of this entry.
        lang24 (Union[Unset, str]): Language 24
        lang27 (Union[Unset, str]): Language 27
        lang26 (Union[Unset, str]): Language 26
        lang21 (Union[Unset, str]): Language 21
        guid (Union[Unset, str]): GUID
        lang20 (Union[Unset, str]): Language 20
        lang23 (Union[Unset, str]): Language 23
        lang22 (Union[Unset, str]): Language 22
        status (Union[Unset, int]): Status. The object is not deleted, if <code>status</code> is -1.
    """

    lang18: Union[Unset, str] = UNSET
    lang17: Union[Unset, str] = UNSET
    lang19: Union[Unset, str] = UNSET
    translation_key: Union[Unset, str] = UNSET
    lang14: Union[Unset, str] = UNSET
    lang13: Union[Unset, str] = UNSET
    lang16: Union[Unset, str] = UNSET
    lang15: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    lang9: Union[Unset, str] = UNSET
    lang8: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    lang7: Union[Unset, str] = UNSET
    lang6: Union[Unset, str] = UNSET
    lang5: Union[Unset, str] = UNSET
    lang10: Union[Unset, str] = UNSET
    lang4: Union[Unset, str] = UNSET
    lang3: Union[Unset, str] = UNSET
    lang12: Union[Unset, str] = UNSET
    lang2: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    lang11: Union[Unset, str] = UNSET
    lang1: Union[Unset, str] = UNSET
    lang30: Union[Unset, str] = UNSET
    lang29: Union[Unset, str] = UNSET
    lang28: Union[Unset, str] = UNSET
    lang25: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    lang24: Union[Unset, str] = UNSET
    lang27: Union[Unset, str] = UNSET
    lang26: Union[Unset, str] = UNSET
    lang21: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    lang20: Union[Unset, str] = UNSET
    lang23: Union[Unset, str] = UNSET
    lang22: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lang18 = self.lang18

        lang17 = self.lang17

        lang19 = self.lang19

        translation_key = self.translation_key

        lang14 = self.lang14

        lang13 = self.lang13

        lang16 = self.lang16

        lang15 = self.lang15

        t_stamp = self.t_stamp

        lang9 = self.lang9

        lang8 = self.lang8

        t_stamp_sync = self.t_stamp_sync

        lang7 = self.lang7

        lang6 = self.lang6

        lang5 = self.lang5

        lang10 = self.lang10

        lang4 = self.lang4

        lang3 = self.lang3

        lang12 = self.lang12

        lang2 = self.lang2

        package_name = self.package_name

        lang11 = self.lang11

        lang1 = self.lang1

        lang30 = self.lang30

        lang29 = self.lang29

        lang28 = self.lang28

        lang25 = self.lang25

        level = self.level

        lang24 = self.lang24

        lang27 = self.lang27

        lang26 = self.lang26

        lang21 = self.lang21

        guid = self.guid

        lang20 = self.lang20

        lang23 = self.lang23

        lang22 = self.lang22

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lang18 is not UNSET:
            field_dict["lang18"] = lang18
        if lang17 is not UNSET:
            field_dict["lang17"] = lang17
        if lang19 is not UNSET:
            field_dict["lang19"] = lang19
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if lang14 is not UNSET:
            field_dict["lang14"] = lang14
        if lang13 is not UNSET:
            field_dict["lang13"] = lang13
        if lang16 is not UNSET:
            field_dict["lang16"] = lang16
        if lang15 is not UNSET:
            field_dict["lang15"] = lang15
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if lang9 is not UNSET:
            field_dict["lang9"] = lang9
        if lang8 is not UNSET:
            field_dict["lang8"] = lang8
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if lang7 is not UNSET:
            field_dict["lang7"] = lang7
        if lang6 is not UNSET:
            field_dict["lang6"] = lang6
        if lang5 is not UNSET:
            field_dict["lang5"] = lang5
        if lang10 is not UNSET:
            field_dict["lang10"] = lang10
        if lang4 is not UNSET:
            field_dict["lang4"] = lang4
        if lang3 is not UNSET:
            field_dict["lang3"] = lang3
        if lang12 is not UNSET:
            field_dict["lang12"] = lang12
        if lang2 is not UNSET:
            field_dict["lang2"] = lang2
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if lang11 is not UNSET:
            field_dict["lang11"] = lang11
        if lang1 is not UNSET:
            field_dict["lang1"] = lang1
        if lang30 is not UNSET:
            field_dict["lang30"] = lang30
        if lang29 is not UNSET:
            field_dict["lang29"] = lang29
        if lang28 is not UNSET:
            field_dict["lang28"] = lang28
        if lang25 is not UNSET:
            field_dict["lang25"] = lang25
        if level is not UNSET:
            field_dict["level"] = level
        if lang24 is not UNSET:
            field_dict["lang24"] = lang24
        if lang27 is not UNSET:
            field_dict["lang27"] = lang27
        if lang26 is not UNSET:
            field_dict["lang26"] = lang26
        if lang21 is not UNSET:
            field_dict["lang21"] = lang21
        if guid is not UNSET:
            field_dict["guid"] = guid
        if lang20 is not UNSET:
            field_dict["lang20"] = lang20
        if lang23 is not UNSET:
            field_dict["lang23"] = lang23
        if lang22 is not UNSET:
            field_dict["lang22"] = lang22
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lang18 = d.pop("lang18", UNSET)

        lang17 = d.pop("lang17", UNSET)

        lang19 = d.pop("lang19", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        lang14 = d.pop("lang14", UNSET)

        lang13 = d.pop("lang13", UNSET)

        lang16 = d.pop("lang16", UNSET)

        lang15 = d.pop("lang15", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        lang9 = d.pop("lang9", UNSET)

        lang8 = d.pop("lang8", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        lang7 = d.pop("lang7", UNSET)

        lang6 = d.pop("lang6", UNSET)

        lang5 = d.pop("lang5", UNSET)

        lang10 = d.pop("lang10", UNSET)

        lang4 = d.pop("lang4", UNSET)

        lang3 = d.pop("lang3", UNSET)

        lang12 = d.pop("lang12", UNSET)

        lang2 = d.pop("lang2", UNSET)

        package_name = d.pop("packageName", UNSET)

        lang11 = d.pop("lang11", UNSET)

        lang1 = d.pop("lang1", UNSET)

        lang30 = d.pop("lang30", UNSET)

        lang29 = d.pop("lang29", UNSET)

        lang28 = d.pop("lang28", UNSET)

        lang25 = d.pop("lang25", UNSET)

        level = d.pop("level", UNSET)

        lang24 = d.pop("lang24", UNSET)

        lang27 = d.pop("lang27", UNSET)

        lang26 = d.pop("lang26", UNSET)

        lang21 = d.pop("lang21", UNSET)

        guid = d.pop("guid", UNSET)

        lang20 = d.pop("lang20", UNSET)

        lang23 = d.pop("lang23", UNSET)

        lang22 = d.pop("lang22", UNSET)

        status = d.pop("status", UNSET)

        translate_term_data = cls(
            lang18=lang18,
            lang17=lang17,
            lang19=lang19,
            translation_key=translation_key,
            lang14=lang14,
            lang13=lang13,
            lang16=lang16,
            lang15=lang15,
            t_stamp=t_stamp,
            lang9=lang9,
            lang8=lang8,
            t_stamp_sync=t_stamp_sync,
            lang7=lang7,
            lang6=lang6,
            lang5=lang5,
            lang10=lang10,
            lang4=lang4,
            lang3=lang3,
            lang12=lang12,
            lang2=lang2,
            package_name=package_name,
            lang11=lang11,
            lang1=lang1,
            lang30=lang30,
            lang29=lang29,
            lang28=lang28,
            lang25=lang25,
            level=level,
            lang24=lang24,
            lang27=lang27,
            lang26=lang26,
            lang21=lang21,
            guid=guid,
            lang20=lang20,
            lang23=lang23,
            lang22=lang22,
            status=status,
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
