from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordListC")


@_attrs_define
class KeywordListC:
    """<p>
    Bit constants for members of KeywordList
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_status (Union[Unset, str]): DB column: swlstatus
            mb_id (Union[Unset, str]): Member bit: ID DB column: swlgroupid
            ln_id (Union[Unset, int]): Column length: ID DB column: swlgroupid
            mb_guid (Union[Unset, str]): Member bit: GUID DB column: swlguid
            ln_guid (Union[Unset, int]): Column length: GUID DB column: swlguid
            mb_t_stamp (Union[Unset, str]): Member bit: Last modified, ISO - UTC DB column: swltstamp
            ln_t_stamp (Union[Unset, int]): Column length: Last modified, ISO - UTC DB column: swltstamp
            mb_user_id (Union[Unset, str]): Member bit: ID of the user that has written the keyword list at last.
                DB column: swluser
            mb_lock_id (Union[Unset, str]): Member bit: ID of the user who holds a lock on the keyword list.
                DB column: swllock
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: swltstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: swltstampsync
            mb_package_name (Union[Unset, str]): Member bit: Package name of KeywordList DB column: packagename
            ln_package_name (Union[Unset, int]): Column length: Package name of KeywordList DB column: packagename
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_status: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    ln_id: Union[Unset, int] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_status = self.mb_status
        mb_id = self.mb_id
        ln_id = self.ln_id
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_user_id = self.mb_user_id
        mb_lock_id = self.mb_lock_id
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_package_name = self.mb_package_name
        ln_package_name = self.ln_package_name
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_status = d.pop("mbStatus", UNSET)

        mb_id = d.pop("mbId", UNSET)

        ln_id = d.pop("lnId", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        keyword_list_c = cls(
            mb_status=mb_status,
            mb_id=mb_id,
            ln_id=ln_id,
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_user_id=mb_user_id,
            mb_lock_id=mb_lock_id,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_package_name=mb_package_name,
            ln_package_name=ln_package_name,
            mb_all_members=mb_all_members,
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
