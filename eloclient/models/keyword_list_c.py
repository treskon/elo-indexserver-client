from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordListC")


@_attrs_define
class KeywordListC:
    """<p>Bit constants for members of KeywordList</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link
                KeywordList#displayName}.
                DB column: swlnametrkey
            mb_id (Union[Unset, str]): Member bit: ID
                DB column: swlgroupid
            mb_package_name (Union[Unset, str]): Member bit: Package name of KeywordList
                DB column: packagename
            mb_t_stamp (Union[Unset, str]): Member bit: Last modified, ISO - UTC Read-only.
                DB column: swltstamp
            mb_lock_id (Union[Unset, str]): Member bit: ID of the user who holds a lock on the keyword list.
                DB column: swllock
            mb_user_id (Union[Unset, str]): Member bit: ID of the user that has written the keyword list at last. Read-only.
                DB column: swluser
            ln_id (Union[Unset, int]): Column length: ID
                DB column: swlgroupid
            ln_guid (Union[Unset, int]): Column length: GUID
                DB column: swlguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: swltstampsync
            ln_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link
                KeywordList#displayName}.
                DB column: swlnametrkey
            mb_status (Union[Unset, str]): DB column: swlstatus
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_display_name (Union[Unset, str]): Member bit: The display name of the keyword. This value is displayed in the
                label before the edit field.
                It
                 DB column: swldisplayname
            mb_guid (Union[Unset, str]): Member bit: GUID
                DB column: swlguid
            ln_t_stamp (Union[Unset, int]): Column length: Last modified, ISO - UTC Read-only.
                DB column: swltstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: swltstampsync
            ln_display_name (Union[Unset, int]): Column length: The display name of the keyword. This value is displayed in
                the label before the edit field.
                It
                 DB column: swldisplayname
            ln_package_name (Union[Unset, int]): Column length: Package name of KeywordList
                DB column: packagename
    """

    mb_name_translation_key: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    ln_id: Union[Unset, int] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_display_name: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    ln_display_name: Union[Unset, int] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_name_translation_key = self.mb_name_translation_key

        mb_id = self.mb_id

        mb_package_name = self.mb_package_name

        mb_t_stamp = self.mb_t_stamp

        mb_lock_id = self.mb_lock_id

        mb_user_id = self.mb_user_id

        ln_id = self.ln_id

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_name_translation_key = self.ln_name_translation_key

        mb_status = self.mb_status

        mb_all_members = self.mb_all_members

        mb_display_name = self.mb_display_name

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        ln_display_name = self.ln_display_name

        ln_package_name = self.ln_package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_display_name is not UNSET:
            field_dict["mbDisplayName"] = mb_display_name
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if ln_display_name is not UNSET:
            field_dict["lnDisplayName"] = ln_display_name
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        ln_id = d.pop("lnId", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_display_name = d.pop("mbDisplayName", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        ln_display_name = d.pop("lnDisplayName", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        keyword_list_c = cls(
            mb_name_translation_key=mb_name_translation_key,
            mb_id=mb_id,
            mb_package_name=mb_package_name,
            mb_t_stamp=mb_t_stamp,
            mb_lock_id=mb_lock_id,
            mb_user_id=mb_user_id,
            ln_id=ln_id,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_name_translation_key=ln_name_translation_key,
            mb_status=mb_status,
            mb_all_members=mb_all_members,
            mb_display_name=mb_display_name,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            ln_display_name=ln_display_name,
            ln_package_name=ln_package_name,
        )

        keyword_list_c.additional_properties = d
        return keyword_list_c

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
