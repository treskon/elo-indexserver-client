from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapHeadC")


@_attrs_define
class MapHeadC:
    """<p>Bit constants for members of MapHead</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_guid (Union[Unset, int]): DB column: mapguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: EIX-3097: TimeStampSync
                DB column: maptstampsync
            mb_id (Union[Unset, str]): DB column: mapid
            mb_obj_id (Union[Unset, str]): DB column: mapobjid
            mb_t_stamp (Union[Unset, str]): DB column: maptstamp
            mb_lock_id (Union[Unset, str]): DB column: maplockid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_guid (Union[Unset, str]): DB column: mapguid
            ln_t_stamp (Union[Unset, int]): DB column: maptstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: EIX-3097: TimeStampSync
                DB column: maptstampsync
            ln_id (Union[Unset, int]): DB column: mapid
    """

    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    ln_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_id = self.mb_id

        mb_obj_id = self.mb_obj_id

        mb_t_stamp = self.mb_t_stamp

        mb_lock_id = self.mb_lock_id

        mb_all_members = self.mb_all_members

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        ln_id = self.ln_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        ln_id = d.pop("lnId", UNSET)

        map_head_c = cls(
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_id=mb_id,
            mb_obj_id=mb_obj_id,
            mb_t_stamp=mb_t_stamp,
            mb_lock_id=mb_lock_id,
            mb_all_members=mb_all_members,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            ln_id=ln_id,
        )

        map_head_c.additional_properties = d
        return map_head_c

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
