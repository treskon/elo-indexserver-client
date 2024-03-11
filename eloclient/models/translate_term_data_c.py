from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTermDataC")


@_attrs_define
class TranslateTermDataC:
    """<p>
    Bit constants for members of TranslateTermData
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_guid (Union[Unset, str]): Member bit: GUID DB column: guid
            ln_guid (Union[Unset, int]): Column length: GUID DB column: guid
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp.
                DB column: tstamp
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp.
                DB column: tstamp
            mb_status (Union[Unset, str]): Member bit: Status.
                DB column: status
            mb_lang_1 (Union[Unset, str]): Member bit: Language 1. System language.
                DB column: lang1
            ln_lang_1 (Union[Unset, int]): Column length: Language 1. System language.
                DB column: lang1
            mb_lang_2 (Union[Unset, str]): Member bit: Language 2 DB column: lang2
            ln_lang_2 (Union[Unset, int]): Column length: Language 2 DB column: lang2
            mb_lang_3 (Union[Unset, str]): Member bit: Language 3 DB column: lang3
            ln_lang_3 (Union[Unset, int]): Column length: Language 3 DB column: lang3
            mb_lang_4 (Union[Unset, str]): Member bit: Language 4 DB column: lang4
            ln_lang_4 (Union[Unset, int]): Column length: Language 4 DB column: lang4
            mb_lang_5 (Union[Unset, str]): Member bit: Language 5 DB column: lang5
            ln_lang_5 (Union[Unset, int]): Column length: Language 5 DB column: lang5
            mb_lang_6 (Union[Unset, str]): Member bit: Language 6 DB column: lang6
            ln_lang_6 (Union[Unset, int]): Column length: Language 6 DB column: lang6
            mb_lang_7 (Union[Unset, str]): Member bit: Language 7 DB column: lang7
            ln_lang_7 (Union[Unset, int]): Column length: Language 7 DB column: lang7
            mb_lang_8 (Union[Unset, str]): Member bit: Language 8 DB column: lang8
            ln_lang_8 (Union[Unset, int]): Column length: Language 8 DB column: lang8
            mb_lang_9 (Union[Unset, str]): Member bit: Language 9 DB column: lang9
            ln_lang_9 (Union[Unset, int]): Column length: Language 9 DB column: lang9
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp.
                DB column: tstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp.
                DB column: tstampsync
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_lang_1: Union[Unset, str] = UNSET
    ln_lang_1: Union[Unset, int] = UNSET
    mb_lang_2: Union[Unset, str] = UNSET
    ln_lang_2: Union[Unset, int] = UNSET
    mb_lang_3: Union[Unset, str] = UNSET
    ln_lang_3: Union[Unset, int] = UNSET
    mb_lang_4: Union[Unset, str] = UNSET
    ln_lang_4: Union[Unset, int] = UNSET
    mb_lang_5: Union[Unset, str] = UNSET
    ln_lang_5: Union[Unset, int] = UNSET
    mb_lang_6: Union[Unset, str] = UNSET
    ln_lang_6: Union[Unset, int] = UNSET
    mb_lang_7: Union[Unset, str] = UNSET
    ln_lang_7: Union[Unset, int] = UNSET
    mb_lang_8: Union[Unset, str] = UNSET
    ln_lang_8: Union[Unset, int] = UNSET
    mb_lang_9: Union[Unset, str] = UNSET
    ln_lang_9: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_status = self.mb_status
        mb_lang_1 = self.mb_lang_1
        ln_lang_1 = self.ln_lang_1
        mb_lang_2 = self.mb_lang_2
        ln_lang_2 = self.ln_lang_2
        mb_lang_3 = self.mb_lang_3
        ln_lang_3 = self.ln_lang_3
        mb_lang_4 = self.mb_lang_4
        ln_lang_4 = self.ln_lang_4
        mb_lang_5 = self.mb_lang_5
        ln_lang_5 = self.ln_lang_5
        mb_lang_6 = self.mb_lang_6
        ln_lang_6 = self.ln_lang_6
        mb_lang_7 = self.mb_lang_7
        ln_lang_7 = self.ln_lang_7
        mb_lang_8 = self.mb_lang_8
        ln_lang_8 = self.ln_lang_8
        mb_lang_9 = self.mb_lang_9
        ln_lang_9 = self.ln_lang_9
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_lang_1 is not UNSET:
            field_dict["mbLang1"] = mb_lang_1
        if ln_lang_1 is not UNSET:
            field_dict["lnLang1"] = ln_lang_1
        if mb_lang_2 is not UNSET:
            field_dict["mbLang2"] = mb_lang_2
        if ln_lang_2 is not UNSET:
            field_dict["lnLang2"] = ln_lang_2
        if mb_lang_3 is not UNSET:
            field_dict["mbLang3"] = mb_lang_3
        if ln_lang_3 is not UNSET:
            field_dict["lnLang3"] = ln_lang_3
        if mb_lang_4 is not UNSET:
            field_dict["mbLang4"] = mb_lang_4
        if ln_lang_4 is not UNSET:
            field_dict["lnLang4"] = ln_lang_4
        if mb_lang_5 is not UNSET:
            field_dict["mbLang5"] = mb_lang_5
        if ln_lang_5 is not UNSET:
            field_dict["lnLang5"] = ln_lang_5
        if mb_lang_6 is not UNSET:
            field_dict["mbLang6"] = mb_lang_6
        if ln_lang_6 is not UNSET:
            field_dict["lnLang6"] = ln_lang_6
        if mb_lang_7 is not UNSET:
            field_dict["mbLang7"] = mb_lang_7
        if ln_lang_7 is not UNSET:
            field_dict["lnLang7"] = ln_lang_7
        if mb_lang_8 is not UNSET:
            field_dict["mbLang8"] = mb_lang_8
        if ln_lang_8 is not UNSET:
            field_dict["lnLang8"] = ln_lang_8
        if mb_lang_9 is not UNSET:
            field_dict["mbLang9"] = mb_lang_9
        if ln_lang_9 is not UNSET:
            field_dict["lnLang9"] = ln_lang_9
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_lang_1 = d.pop("mbLang1", UNSET)

        ln_lang_1 = d.pop("lnLang1", UNSET)

        mb_lang_2 = d.pop("mbLang2", UNSET)

        ln_lang_2 = d.pop("lnLang2", UNSET)

        mb_lang_3 = d.pop("mbLang3", UNSET)

        ln_lang_3 = d.pop("lnLang3", UNSET)

        mb_lang_4 = d.pop("mbLang4", UNSET)

        ln_lang_4 = d.pop("lnLang4", UNSET)

        mb_lang_5 = d.pop("mbLang5", UNSET)

        ln_lang_5 = d.pop("lnLang5", UNSET)

        mb_lang_6 = d.pop("mbLang6", UNSET)

        ln_lang_6 = d.pop("lnLang6", UNSET)

        mb_lang_7 = d.pop("mbLang7", UNSET)

        ln_lang_7 = d.pop("lnLang7", UNSET)

        mb_lang_8 = d.pop("mbLang8", UNSET)

        ln_lang_8 = d.pop("lnLang8", UNSET)

        mb_lang_9 = d.pop("mbLang9", UNSET)

        ln_lang_9 = d.pop("lnLang9", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        translate_term_data_c = cls(
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_status=mb_status,
            mb_lang_1=mb_lang_1,
            ln_lang_1=ln_lang_1,
            mb_lang_2=mb_lang_2,
            ln_lang_2=ln_lang_2,
            mb_lang_3=mb_lang_3,
            ln_lang_3=ln_lang_3,
            mb_lang_4=mb_lang_4,
            ln_lang_4=ln_lang_4,
            mb_lang_5=mb_lang_5,
            ln_lang_5=ln_lang_5,
            mb_lang_6=mb_lang_6,
            ln_lang_6=ln_lang_6,
            mb_lang_7=mb_lang_7,
            ln_lang_7=ln_lang_7,
            mb_lang_8=mb_lang_8,
            ln_lang_8=ln_lang_8,
            mb_lang_9=mb_lang_9,
            ln_lang_9=ln_lang_9,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_all_members=mb_all_members,
        )

        translate_term_data_c.additional_properties = d
        return translate_term_data_c

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
