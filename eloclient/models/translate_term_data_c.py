from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslateTermDataC")


@_attrs_define
class TranslateTermDataC:
    """<p>Bit constants for members of TranslateTermData</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp.
                Last mofified time, ISO date with dots measured in UTC The format is
                 DB column: tstamp
            ln_lang_10 (Union[Unset, int]): Column length: Language 10
                DB column: lang10
            ln_lang_2 (Union[Unset, int]): Column length: Language 2
                DB column: lang2
            ln_lang_18 (Union[Unset, int]): Column length: Language 18
                DB column: lang18
            ln_lang_3 (Union[Unset, int]): Column length: Language 3
                DB column: lang3
            ln_lang_17 (Union[Unset, int]): Column length: Language 17
                DB column: lang17
            ln_translation_key (Union[Unset, int]): Column length: Language independent translation key.
                DB column: trankey
            ln_lang_16 (Union[Unset, int]): Column length: Language 16
                DB column: lang16
            ln_lang_1 (Union[Unset, int]): Column length: Language 1. System language.
                DB column: lang1
            ln_lang_15 (Union[Unset, int]): Column length: Language 15
                DB column: lang15
            ln_lang_6 (Union[Unset, int]): Column length: Language 6
                DB column: lang6
            ln_lang_14 (Union[Unset, int]): Column length: Language 14
                DB column: lang14
            mb_lang_28 (Union[Unset, str]): Member bit: Language 28
                DB column: lang28
            ln_lang_7 (Union[Unset, int]): Column length: Language 7
                DB column: lang7
            ln_lang_13 (Union[Unset, int]): Column length: Language 13
                DB column: lang13
            mb_lang_27 (Union[Unset, str]): Member bit: Language 27
                DB column: lang27
            ln_lang_4 (Union[Unset, int]): Column length: Language 4
                DB column: lang4
            ln_lang_12 (Union[Unset, int]): Column length: Language 12
                DB column: lang12
            ln_lang_5 (Union[Unset, int]): Column length: Language 5
                DB column: lang5
            ln_lang_11 (Union[Unset, int]): Column length: Language 11
                DB column: lang11
            mb_lang_29 (Union[Unset, str]): Member bit: Language 29
                DB column: lang29
            mb_lang_24 (Union[Unset, str]): Member bit: Language 24
                DB column: lang24
            mb_lang_23 (Union[Unset, str]): Member bit: Language 23
                DB column: lang23
            ln_lang_8 (Union[Unset, int]): Column length: Language 8
                DB column: lang8
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp. Timestamp of this object's last export by the
                replication.
                The format is
                 DB column: tstampsync
            mb_lang_26 (Union[Unset, str]): Member bit: Language 26
                DB column: lang26
            ln_lang_9 (Union[Unset, int]): Column length: Language 9
                DB column: lang9
            mb_lang_25 (Union[Unset, str]): Member bit: Language 25
                DB column: lang25
            mb_lang_20 (Union[Unset, str]): Member bit: Language 20
                DB column: lang20
            mb_lang_22 (Union[Unset, str]): Member bit: Language 22
                DB column: lang22
            ln_lang_19 (Union[Unset, int]): Column length: Language 19
                DB column: lang19
            mb_lang_21 (Union[Unset, str]): Member bit: Language 21
                DB column: lang21
            mb_translation_key (Union[Unset, str]): Member bit: Language independent translation key.
                DB column: trankey
            mb_lang_17 (Union[Unset, str]): Member bit: Language 17
                DB column: lang17
            mb_lang_16 (Union[Unset, str]): Member bit: Language 16
                DB column: lang16
            mb_lang_19 (Union[Unset, str]): Member bit: Language 19
                DB column: lang19
            mb_lang_18 (Union[Unset, str]): Member bit: Language 18
                DB column: lang18
            mb_lang_13 (Union[Unset, str]): Member bit: Language 13
                DB column: lang13
            mb_guid (Union[Unset, str]): Member bit: GUID
                DB column: guid
            mb_lang_12 (Union[Unset, str]): Member bit: Language 12
                DB column: lang12
            mb_lang_15 (Union[Unset, str]): Member bit: Language 15
                DB column: lang15
            mb_lang_14 (Union[Unset, str]): Member bit: Language 14
                DB column: lang14
            mb_lang_11 (Union[Unset, str]): Member bit: Language 11
                DB column: lang11
            ln_package_name (Union[Unset, int]): Column length: Configuration package.
                DB column: pack
            mb_lang_10 (Union[Unset, str]): Member bit: Language 10
                DB column: lang10
            mb_package_name (Union[Unset, str]): Member bit: Configuration package.
                DB column: pack
            ln_lang_30 (Union[Unset, int]): Column length: Language 30
                DB column: lang30
            mb_level (Union[Unset, str]): Member bit: Priority level of this entry.
                DB column: tlevel
            ln_guid (Union[Unset, int]): Column length: GUID
                DB column: guid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp. Timestamp of this object's last export by the
                replication.
                The format is
                 DB column: tstampsync
            mb_status (Union[Unset, str]): Member bit: Status. The object is not deleted, if <code>status</code> is -1.
                DB column: status
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp.
                Last mofified time, ISO date with dots measured in UTC The format is
                 DB column: tstamp
            mb_lang_9 (Union[Unset, str]): Member bit: Language 9
                DB column: lang9
            ln_lang_21 (Union[Unset, int]): Column length: Language 21
                DB column: lang21
            ln_lang_20 (Union[Unset, int]): Column length: Language 20
                DB column: lang20
            mb_lang_7 (Union[Unset, str]): Member bit: Language 7
                DB column: lang7
            mb_lang_8 (Union[Unset, str]): Member bit: Language 8
                DB column: lang8
            mb_lang_5 (Union[Unset, str]): Member bit: Language 5
                DB column: lang5
            mb_lang_6 (Union[Unset, str]): Member bit: Language 6
                DB column: lang6
            mb_lang_3 (Union[Unset, str]): Member bit: Language 3
                DB column: lang3
            mb_lang_4 (Union[Unset, str]): Member bit: Language 4
                DB column: lang4
            mb_lang_1 (Union[Unset, str]): Member bit: Language 1. System language.
                DB column: lang1
            ln_lang_29 (Union[Unset, int]): Column length: Language 29
                DB column: lang29
            mb_lang_2 (Union[Unset, str]): Member bit: Language 2
                DB column: lang2
            ln_lang_28 (Union[Unset, int]): Column length: Language 28
                DB column: lang28
            ln_lang_27 (Union[Unset, int]): Column length: Language 27
                DB column: lang27
            ln_lang_26 (Union[Unset, int]): Column length: Language 26
                DB column: lang26
            ln_lang_25 (Union[Unset, int]): Column length: Language 25
                DB column: lang25
            ln_lang_24 (Union[Unset, int]): Column length: Language 24
                DB column: lang24
            ln_lang_23 (Union[Unset, int]): Column length: Language 23
                DB column: lang23
            ln_lang_22 (Union[Unset, int]): Column length: Language 22
                DB column: lang22
            mb_lang_30 (Union[Unset, str]): Member bit: Language 30
                DB column: lang30
    """

    mb_t_stamp: Union[Unset, str] = UNSET
    ln_lang_10: Union[Unset, int] = UNSET
    ln_lang_2: Union[Unset, int] = UNSET
    ln_lang_18: Union[Unset, int] = UNSET
    ln_lang_3: Union[Unset, int] = UNSET
    ln_lang_17: Union[Unset, int] = UNSET
    ln_translation_key: Union[Unset, int] = UNSET
    ln_lang_16: Union[Unset, int] = UNSET
    ln_lang_1: Union[Unset, int] = UNSET
    ln_lang_15: Union[Unset, int] = UNSET
    ln_lang_6: Union[Unset, int] = UNSET
    ln_lang_14: Union[Unset, int] = UNSET
    mb_lang_28: Union[Unset, str] = UNSET
    ln_lang_7: Union[Unset, int] = UNSET
    ln_lang_13: Union[Unset, int] = UNSET
    mb_lang_27: Union[Unset, str] = UNSET
    ln_lang_4: Union[Unset, int] = UNSET
    ln_lang_12: Union[Unset, int] = UNSET
    ln_lang_5: Union[Unset, int] = UNSET
    ln_lang_11: Union[Unset, int] = UNSET
    mb_lang_29: Union[Unset, str] = UNSET
    mb_lang_24: Union[Unset, str] = UNSET
    mb_lang_23: Union[Unset, str] = UNSET
    ln_lang_8: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_lang_26: Union[Unset, str] = UNSET
    ln_lang_9: Union[Unset, int] = UNSET
    mb_lang_25: Union[Unset, str] = UNSET
    mb_lang_20: Union[Unset, str] = UNSET
    mb_lang_22: Union[Unset, str] = UNSET
    ln_lang_19: Union[Unset, int] = UNSET
    mb_lang_21: Union[Unset, str] = UNSET
    mb_translation_key: Union[Unset, str] = UNSET
    mb_lang_17: Union[Unset, str] = UNSET
    mb_lang_16: Union[Unset, str] = UNSET
    mb_lang_19: Union[Unset, str] = UNSET
    mb_lang_18: Union[Unset, str] = UNSET
    mb_lang_13: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    mb_lang_12: Union[Unset, str] = UNSET
    mb_lang_15: Union[Unset, str] = UNSET
    mb_lang_14: Union[Unset, str] = UNSET
    mb_lang_11: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    mb_lang_10: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    ln_lang_30: Union[Unset, int] = UNSET
    mb_level: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_lang_9: Union[Unset, str] = UNSET
    ln_lang_21: Union[Unset, int] = UNSET
    ln_lang_20: Union[Unset, int] = UNSET
    mb_lang_7: Union[Unset, str] = UNSET
    mb_lang_8: Union[Unset, str] = UNSET
    mb_lang_5: Union[Unset, str] = UNSET
    mb_lang_6: Union[Unset, str] = UNSET
    mb_lang_3: Union[Unset, str] = UNSET
    mb_lang_4: Union[Unset, str] = UNSET
    mb_lang_1: Union[Unset, str] = UNSET
    ln_lang_29: Union[Unset, int] = UNSET
    mb_lang_2: Union[Unset, str] = UNSET
    ln_lang_28: Union[Unset, int] = UNSET
    ln_lang_27: Union[Unset, int] = UNSET
    ln_lang_26: Union[Unset, int] = UNSET
    ln_lang_25: Union[Unset, int] = UNSET
    ln_lang_24: Union[Unset, int] = UNSET
    ln_lang_23: Union[Unset, int] = UNSET
    ln_lang_22: Union[Unset, int] = UNSET
    mb_lang_30: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_t_stamp = self.mb_t_stamp

        ln_lang_10 = self.ln_lang_10

        ln_lang_2 = self.ln_lang_2

        ln_lang_18 = self.ln_lang_18

        ln_lang_3 = self.ln_lang_3

        ln_lang_17 = self.ln_lang_17

        ln_translation_key = self.ln_translation_key

        ln_lang_16 = self.ln_lang_16

        ln_lang_1 = self.ln_lang_1

        ln_lang_15 = self.ln_lang_15

        ln_lang_6 = self.ln_lang_6

        ln_lang_14 = self.ln_lang_14

        mb_lang_28 = self.mb_lang_28

        ln_lang_7 = self.ln_lang_7

        ln_lang_13 = self.ln_lang_13

        mb_lang_27 = self.mb_lang_27

        ln_lang_4 = self.ln_lang_4

        ln_lang_12 = self.ln_lang_12

        ln_lang_5 = self.ln_lang_5

        ln_lang_11 = self.ln_lang_11

        mb_lang_29 = self.mb_lang_29

        mb_lang_24 = self.mb_lang_24

        mb_lang_23 = self.mb_lang_23

        ln_lang_8 = self.ln_lang_8

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_lang_26 = self.mb_lang_26

        ln_lang_9 = self.ln_lang_9

        mb_lang_25 = self.mb_lang_25

        mb_lang_20 = self.mb_lang_20

        mb_lang_22 = self.mb_lang_22

        ln_lang_19 = self.ln_lang_19

        mb_lang_21 = self.mb_lang_21

        mb_translation_key = self.mb_translation_key

        mb_lang_17 = self.mb_lang_17

        mb_lang_16 = self.mb_lang_16

        mb_lang_19 = self.mb_lang_19

        mb_lang_18 = self.mb_lang_18

        mb_lang_13 = self.mb_lang_13

        mb_guid = self.mb_guid

        mb_lang_12 = self.mb_lang_12

        mb_lang_15 = self.mb_lang_15

        mb_lang_14 = self.mb_lang_14

        mb_lang_11 = self.mb_lang_11

        ln_package_name = self.ln_package_name

        mb_lang_10 = self.mb_lang_10

        mb_package_name = self.mb_package_name

        ln_lang_30 = self.ln_lang_30

        mb_level = self.mb_level

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_status = self.mb_status

        mb_all_members = self.mb_all_members

        ln_t_stamp = self.ln_t_stamp

        mb_lang_9 = self.mb_lang_9

        ln_lang_21 = self.ln_lang_21

        ln_lang_20 = self.ln_lang_20

        mb_lang_7 = self.mb_lang_7

        mb_lang_8 = self.mb_lang_8

        mb_lang_5 = self.mb_lang_5

        mb_lang_6 = self.mb_lang_6

        mb_lang_3 = self.mb_lang_3

        mb_lang_4 = self.mb_lang_4

        mb_lang_1 = self.mb_lang_1

        ln_lang_29 = self.ln_lang_29

        mb_lang_2 = self.mb_lang_2

        ln_lang_28 = self.ln_lang_28

        ln_lang_27 = self.ln_lang_27

        ln_lang_26 = self.ln_lang_26

        ln_lang_25 = self.ln_lang_25

        ln_lang_24 = self.ln_lang_24

        ln_lang_23 = self.ln_lang_23

        ln_lang_22 = self.ln_lang_22

        mb_lang_30 = self.mb_lang_30

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_lang_10 is not UNSET:
            field_dict["lnLang10"] = ln_lang_10
        if ln_lang_2 is not UNSET:
            field_dict["lnLang2"] = ln_lang_2
        if ln_lang_18 is not UNSET:
            field_dict["lnLang18"] = ln_lang_18
        if ln_lang_3 is not UNSET:
            field_dict["lnLang3"] = ln_lang_3
        if ln_lang_17 is not UNSET:
            field_dict["lnLang17"] = ln_lang_17
        if ln_translation_key is not UNSET:
            field_dict["lnTranslationKey"] = ln_translation_key
        if ln_lang_16 is not UNSET:
            field_dict["lnLang16"] = ln_lang_16
        if ln_lang_1 is not UNSET:
            field_dict["lnLang1"] = ln_lang_1
        if ln_lang_15 is not UNSET:
            field_dict["lnLang15"] = ln_lang_15
        if ln_lang_6 is not UNSET:
            field_dict["lnLang6"] = ln_lang_6
        if ln_lang_14 is not UNSET:
            field_dict["lnLang14"] = ln_lang_14
        if mb_lang_28 is not UNSET:
            field_dict["mbLang28"] = mb_lang_28
        if ln_lang_7 is not UNSET:
            field_dict["lnLang7"] = ln_lang_7
        if ln_lang_13 is not UNSET:
            field_dict["lnLang13"] = ln_lang_13
        if mb_lang_27 is not UNSET:
            field_dict["mbLang27"] = mb_lang_27
        if ln_lang_4 is not UNSET:
            field_dict["lnLang4"] = ln_lang_4
        if ln_lang_12 is not UNSET:
            field_dict["lnLang12"] = ln_lang_12
        if ln_lang_5 is not UNSET:
            field_dict["lnLang5"] = ln_lang_5
        if ln_lang_11 is not UNSET:
            field_dict["lnLang11"] = ln_lang_11
        if mb_lang_29 is not UNSET:
            field_dict["mbLang29"] = mb_lang_29
        if mb_lang_24 is not UNSET:
            field_dict["mbLang24"] = mb_lang_24
        if mb_lang_23 is not UNSET:
            field_dict["mbLang23"] = mb_lang_23
        if ln_lang_8 is not UNSET:
            field_dict["lnLang8"] = ln_lang_8
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_lang_26 is not UNSET:
            field_dict["mbLang26"] = mb_lang_26
        if ln_lang_9 is not UNSET:
            field_dict["lnLang9"] = ln_lang_9
        if mb_lang_25 is not UNSET:
            field_dict["mbLang25"] = mb_lang_25
        if mb_lang_20 is not UNSET:
            field_dict["mbLang20"] = mb_lang_20
        if mb_lang_22 is not UNSET:
            field_dict["mbLang22"] = mb_lang_22
        if ln_lang_19 is not UNSET:
            field_dict["lnLang19"] = ln_lang_19
        if mb_lang_21 is not UNSET:
            field_dict["mbLang21"] = mb_lang_21
        if mb_translation_key is not UNSET:
            field_dict["mbTranslationKey"] = mb_translation_key
        if mb_lang_17 is not UNSET:
            field_dict["mbLang17"] = mb_lang_17
        if mb_lang_16 is not UNSET:
            field_dict["mbLang16"] = mb_lang_16
        if mb_lang_19 is not UNSET:
            field_dict["mbLang19"] = mb_lang_19
        if mb_lang_18 is not UNSET:
            field_dict["mbLang18"] = mb_lang_18
        if mb_lang_13 is not UNSET:
            field_dict["mbLang13"] = mb_lang_13
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_lang_12 is not UNSET:
            field_dict["mbLang12"] = mb_lang_12
        if mb_lang_15 is not UNSET:
            field_dict["mbLang15"] = mb_lang_15
        if mb_lang_14 is not UNSET:
            field_dict["mbLang14"] = mb_lang_14
        if mb_lang_11 is not UNSET:
            field_dict["mbLang11"] = mb_lang_11
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name
        if mb_lang_10 is not UNSET:
            field_dict["mbLang10"] = mb_lang_10
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if ln_lang_30 is not UNSET:
            field_dict["lnLang30"] = ln_lang_30
        if mb_level is not UNSET:
            field_dict["mbLevel"] = mb_level
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_lang_9 is not UNSET:
            field_dict["mbLang9"] = mb_lang_9
        if ln_lang_21 is not UNSET:
            field_dict["lnLang21"] = ln_lang_21
        if ln_lang_20 is not UNSET:
            field_dict["lnLang20"] = ln_lang_20
        if mb_lang_7 is not UNSET:
            field_dict["mbLang7"] = mb_lang_7
        if mb_lang_8 is not UNSET:
            field_dict["mbLang8"] = mb_lang_8
        if mb_lang_5 is not UNSET:
            field_dict["mbLang5"] = mb_lang_5
        if mb_lang_6 is not UNSET:
            field_dict["mbLang6"] = mb_lang_6
        if mb_lang_3 is not UNSET:
            field_dict["mbLang3"] = mb_lang_3
        if mb_lang_4 is not UNSET:
            field_dict["mbLang4"] = mb_lang_4
        if mb_lang_1 is not UNSET:
            field_dict["mbLang1"] = mb_lang_1
        if ln_lang_29 is not UNSET:
            field_dict["lnLang29"] = ln_lang_29
        if mb_lang_2 is not UNSET:
            field_dict["mbLang2"] = mb_lang_2
        if ln_lang_28 is not UNSET:
            field_dict["lnLang28"] = ln_lang_28
        if ln_lang_27 is not UNSET:
            field_dict["lnLang27"] = ln_lang_27
        if ln_lang_26 is not UNSET:
            field_dict["lnLang26"] = ln_lang_26
        if ln_lang_25 is not UNSET:
            field_dict["lnLang25"] = ln_lang_25
        if ln_lang_24 is not UNSET:
            field_dict["lnLang24"] = ln_lang_24
        if ln_lang_23 is not UNSET:
            field_dict["lnLang23"] = ln_lang_23
        if ln_lang_22 is not UNSET:
            field_dict["lnLang22"] = ln_lang_22
        if mb_lang_30 is not UNSET:
            field_dict["mbLang30"] = mb_lang_30

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_lang_10 = d.pop("lnLang10", UNSET)

        ln_lang_2 = d.pop("lnLang2", UNSET)

        ln_lang_18 = d.pop("lnLang18", UNSET)

        ln_lang_3 = d.pop("lnLang3", UNSET)

        ln_lang_17 = d.pop("lnLang17", UNSET)

        ln_translation_key = d.pop("lnTranslationKey", UNSET)

        ln_lang_16 = d.pop("lnLang16", UNSET)

        ln_lang_1 = d.pop("lnLang1", UNSET)

        ln_lang_15 = d.pop("lnLang15", UNSET)

        ln_lang_6 = d.pop("lnLang6", UNSET)

        ln_lang_14 = d.pop("lnLang14", UNSET)

        mb_lang_28 = d.pop("mbLang28", UNSET)

        ln_lang_7 = d.pop("lnLang7", UNSET)

        ln_lang_13 = d.pop("lnLang13", UNSET)

        mb_lang_27 = d.pop("mbLang27", UNSET)

        ln_lang_4 = d.pop("lnLang4", UNSET)

        ln_lang_12 = d.pop("lnLang12", UNSET)

        ln_lang_5 = d.pop("lnLang5", UNSET)

        ln_lang_11 = d.pop("lnLang11", UNSET)

        mb_lang_29 = d.pop("mbLang29", UNSET)

        mb_lang_24 = d.pop("mbLang24", UNSET)

        mb_lang_23 = d.pop("mbLang23", UNSET)

        ln_lang_8 = d.pop("lnLang8", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_lang_26 = d.pop("mbLang26", UNSET)

        ln_lang_9 = d.pop("lnLang9", UNSET)

        mb_lang_25 = d.pop("mbLang25", UNSET)

        mb_lang_20 = d.pop("mbLang20", UNSET)

        mb_lang_22 = d.pop("mbLang22", UNSET)

        ln_lang_19 = d.pop("lnLang19", UNSET)

        mb_lang_21 = d.pop("mbLang21", UNSET)

        mb_translation_key = d.pop("mbTranslationKey", UNSET)

        mb_lang_17 = d.pop("mbLang17", UNSET)

        mb_lang_16 = d.pop("mbLang16", UNSET)

        mb_lang_19 = d.pop("mbLang19", UNSET)

        mb_lang_18 = d.pop("mbLang18", UNSET)

        mb_lang_13 = d.pop("mbLang13", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        mb_lang_12 = d.pop("mbLang12", UNSET)

        mb_lang_15 = d.pop("mbLang15", UNSET)

        mb_lang_14 = d.pop("mbLang14", UNSET)

        mb_lang_11 = d.pop("mbLang11", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        mb_lang_10 = d.pop("mbLang10", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        ln_lang_30 = d.pop("lnLang30", UNSET)

        mb_level = d.pop("mbLevel", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_lang_9 = d.pop("mbLang9", UNSET)

        ln_lang_21 = d.pop("lnLang21", UNSET)

        ln_lang_20 = d.pop("lnLang20", UNSET)

        mb_lang_7 = d.pop("mbLang7", UNSET)

        mb_lang_8 = d.pop("mbLang8", UNSET)

        mb_lang_5 = d.pop("mbLang5", UNSET)

        mb_lang_6 = d.pop("mbLang6", UNSET)

        mb_lang_3 = d.pop("mbLang3", UNSET)

        mb_lang_4 = d.pop("mbLang4", UNSET)

        mb_lang_1 = d.pop("mbLang1", UNSET)

        ln_lang_29 = d.pop("lnLang29", UNSET)

        mb_lang_2 = d.pop("mbLang2", UNSET)

        ln_lang_28 = d.pop("lnLang28", UNSET)

        ln_lang_27 = d.pop("lnLang27", UNSET)

        ln_lang_26 = d.pop("lnLang26", UNSET)

        ln_lang_25 = d.pop("lnLang25", UNSET)

        ln_lang_24 = d.pop("lnLang24", UNSET)

        ln_lang_23 = d.pop("lnLang23", UNSET)

        ln_lang_22 = d.pop("lnLang22", UNSET)

        mb_lang_30 = d.pop("mbLang30", UNSET)

        translate_term_data_c = cls(
            mb_t_stamp=mb_t_stamp,
            ln_lang_10=ln_lang_10,
            ln_lang_2=ln_lang_2,
            ln_lang_18=ln_lang_18,
            ln_lang_3=ln_lang_3,
            ln_lang_17=ln_lang_17,
            ln_translation_key=ln_translation_key,
            ln_lang_16=ln_lang_16,
            ln_lang_1=ln_lang_1,
            ln_lang_15=ln_lang_15,
            ln_lang_6=ln_lang_6,
            ln_lang_14=ln_lang_14,
            mb_lang_28=mb_lang_28,
            ln_lang_7=ln_lang_7,
            ln_lang_13=ln_lang_13,
            mb_lang_27=mb_lang_27,
            ln_lang_4=ln_lang_4,
            ln_lang_12=ln_lang_12,
            ln_lang_5=ln_lang_5,
            ln_lang_11=ln_lang_11,
            mb_lang_29=mb_lang_29,
            mb_lang_24=mb_lang_24,
            mb_lang_23=mb_lang_23,
            ln_lang_8=ln_lang_8,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_lang_26=mb_lang_26,
            ln_lang_9=ln_lang_9,
            mb_lang_25=mb_lang_25,
            mb_lang_20=mb_lang_20,
            mb_lang_22=mb_lang_22,
            ln_lang_19=ln_lang_19,
            mb_lang_21=mb_lang_21,
            mb_translation_key=mb_translation_key,
            mb_lang_17=mb_lang_17,
            mb_lang_16=mb_lang_16,
            mb_lang_19=mb_lang_19,
            mb_lang_18=mb_lang_18,
            mb_lang_13=mb_lang_13,
            mb_guid=mb_guid,
            mb_lang_12=mb_lang_12,
            mb_lang_15=mb_lang_15,
            mb_lang_14=mb_lang_14,
            mb_lang_11=mb_lang_11,
            ln_package_name=ln_package_name,
            mb_lang_10=mb_lang_10,
            mb_package_name=mb_package_name,
            ln_lang_30=ln_lang_30,
            mb_level=mb_level,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_status=mb_status,
            mb_all_members=mb_all_members,
            ln_t_stamp=ln_t_stamp,
            mb_lang_9=mb_lang_9,
            ln_lang_21=ln_lang_21,
            ln_lang_20=ln_lang_20,
            mb_lang_7=mb_lang_7,
            mb_lang_8=mb_lang_8,
            mb_lang_5=mb_lang_5,
            mb_lang_6=mb_lang_6,
            mb_lang_3=mb_lang_3,
            mb_lang_4=mb_lang_4,
            mb_lang_1=mb_lang_1,
            ln_lang_29=ln_lang_29,
            mb_lang_2=mb_lang_2,
            ln_lang_28=ln_lang_28,
            ln_lang_27=ln_lang_27,
            ln_lang_26=ln_lang_26,
            ln_lang_25=ln_lang_25,
            ln_lang_24=ln_lang_24,
            ln_lang_23=ln_lang_23,
            ln_lang_22=ln_lang_22,
            mb_lang_30=mb_lang_30,
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
