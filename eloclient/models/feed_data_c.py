from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedDataC")


@_attrs_define
class FeedDataC:
    """<p>Bit constants for members of Feed</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_guid (Union[Unset, int]): Column length: Feed GUID.
                DB column: feedguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: feedtstampsync
            ln_obj_guid (Union[Unset, int]): Column length: GUID of the associated Sord object.
                DB column: objguid
            ln_create_date_iso (Union[Unset, int]): Column length: Create date. It holds the ISO formatted create date in
                the time zone of the client application.
                DB column: createdateiso
            mb_t_stamp (Union[Unset, str]): Member bit: Time stamp. Time stamp of creation or modification.
                DB column: feedtstamp
            mb_create_date_iso (Union[Unset, str]): Member bit: Create date. It holds the ISO formatted create date in the
                time zone of the client application.
                DB column: createdateiso
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_guid (Union[Unset, str]): Member bit: Feed GUID.
                DB column: feedguid
            ln_t_stamp (Union[Unset, int]): Column length: Time stamp. Time stamp of creation or modification.
                DB column: feedtstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: feedtstampsync
            mb_obj_guid (Union[Unset, str]): Member bit: GUID of the associated Sord object.
                DB column: objguid
    """

    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_obj_guid: Union[Unset, int] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_obj_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_obj_guid = self.ln_obj_guid

        ln_create_date_iso = self.ln_create_date_iso

        mb_t_stamp = self.mb_t_stamp

        mb_create_date_iso = self.mb_create_date_iso

        mb_all_members = self.mb_all_members

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_obj_guid = self.mb_obj_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_obj_guid is not UNSET:
            field_dict["lnObjGuid"] = ln_obj_guid
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_obj_guid is not UNSET:
            field_dict["mbObjGuid"] = mb_obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_obj_guid = d.pop("lnObjGuid", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_obj_guid = d.pop("mbObjGuid", UNSET)

        feed_data_c = cls(
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_obj_guid=ln_obj_guid,
            ln_create_date_iso=ln_create_date_iso,
            mb_t_stamp=mb_t_stamp,
            mb_create_date_iso=mb_create_date_iso,
            mb_all_members=mb_all_members,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_obj_guid=mb_obj_guid,
        )

        feed_data_c.additional_properties = d
        return feed_data_c

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
