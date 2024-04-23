from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectDataC")


@_attrs_define
class AspectDataC:
    """<p>Bit constants for members of Aspect</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_id (Union[Unset, str]): Member bit: Aspect ID. For a new aspect, this value is -1.
                This value cannot be changed for an existing
                 DB column: id
            mb_package_name (Union[Unset, str]): Member bit: Package name of Aspect.
                DB column: packagename
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp of last modification.
                DB column: tstamp
            mb_lock_id (Union[Unset, str]): Member bit: User ID that holds a lock on this object. If -1, the object is
                unlocked.
                DB column: lockid
            mb_translation_key (Union[Unset, str]): Member bit: Translation key. Defines the {@link #displayName} as
                technical resource ID.
                DB column: translationkey
            mb_name (Union[Unset, str]): Member bit: Aspect name.
                <br>
                 DB column: name
            ln_guid (Union[Unset, int]): Column length: Aspect GUID.
                DB column: guid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: tstampsync
            ln_translation_key (Union[Unset, int]): Column length: Translation key. Defines the {@link #displayName} as
                technical resource ID.
                DB column: translationkey
            mb_status (Union[Unset, str]): DB column: status
            ln_name (Union[Unset, int]): Column length: Aspect name.
                <br>
                 DB column: name
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_guid (Union[Unset, str]): Member bit: Aspect GUID.
                DB column: guid
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp of last modification.
                DB column: tstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: tstampsync
            ln_package_name (Union[Unset, int]): Column length: Package name of Aspect.
                DB column: packagename
    """

    mb_id: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_translation_key: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_translation_key: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id

        mb_package_name = self.mb_package_name

        mb_t_stamp = self.mb_t_stamp

        mb_lock_id = self.mb_lock_id

        mb_translation_key = self.mb_translation_key

        mb_name = self.mb_name

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_translation_key = self.ln_translation_key

        mb_status = self.mb_status

        ln_name = self.ln_name

        mb_all_members = self.mb_all_members

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        ln_package_name = self.ln_package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_translation_key is not UNSET:
            field_dict["mbTranslationKey"] = mb_translation_key
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_translation_key is not UNSET:
            field_dict["lnTranslationKey"] = ln_translation_key
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_translation_key = d.pop("mbTranslationKey", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_translation_key = d.pop("lnTranslationKey", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        aspect_data_c = cls(
            mb_id=mb_id,
            mb_package_name=mb_package_name,
            mb_t_stamp=mb_t_stamp,
            mb_lock_id=mb_lock_id,
            mb_translation_key=mb_translation_key,
            mb_name=mb_name,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_translation_key=ln_translation_key,
            mb_status=mb_status,
            ln_name=ln_name,
            mb_all_members=mb_all_members,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            ln_package_name=ln_package_name,
        )

        aspect_data_c.additional_properties = d
        return aspect_data_c

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
