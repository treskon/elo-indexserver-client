from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplSetNameC")


@_attrs_define
class ReplSetNameC:
    """<p>Bit constants for members of ReplSetName</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: rsid
            mb_desc (Union[Unset, str]): DB column: rsdesc
            mb_priority (Union[Unset, str]): Member bit: Priority of this replication set.
                DB column: rsprio
            mb_t_stamp (Union[Unset, str]): DB column: rststamp
            mb_mobile (Union[Unset, str]): DB column: rsmobile
            mb_name (Union[Unset, str]): DB column: rsname
            ln_desc (Union[Unset, int]): DB column: rsdesc
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: rststampsync
            ln_name (Union[Unset, int]): DB column: rsname
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_t_stamp (Union[Unset, int]): DB column: rststamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: rststampsync
            mb_image (Union[Unset, str]): DB column: rsimage
    """

    mb_id: Union[Unset, str] = UNSET
    mb_desc: Union[Unset, str] = UNSET
    mb_priority: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_mobile: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_desc: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_image: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id

        mb_desc = self.mb_desc

        mb_priority = self.mb_priority

        mb_t_stamp = self.mb_t_stamp

        mb_mobile = self.mb_mobile

        mb_name = self.mb_name

        ln_desc = self.ln_desc

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_name = self.ln_name

        mb_all_members = self.mb_all_members

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_image = self.mb_image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_desc is not UNSET:
            field_dict["mbDesc"] = mb_desc
        if mb_priority is not UNSET:
            field_dict["mbPriority"] = mb_priority
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_mobile is not UNSET:
            field_dict["mbMobile"] = mb_mobile
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_desc is not UNSET:
            field_dict["lnDesc"] = ln_desc
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_image is not UNSET:
            field_dict["mbImage"] = mb_image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_desc = d.pop("mbDesc", UNSET)

        mb_priority = d.pop("mbPriority", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_mobile = d.pop("mbMobile", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_desc = d.pop("lnDesc", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_image = d.pop("mbImage", UNSET)

        repl_set_name_c = cls(
            mb_id=mb_id,
            mb_desc=mb_desc,
            mb_priority=mb_priority,
            mb_t_stamp=mb_t_stamp,
            mb_mobile=mb_mobile,
            mb_name=mb_name,
            ln_desc=ln_desc,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_name=ln_name,
            mb_all_members=mb_all_members,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_image=mb_image,
        )

        repl_set_name_c.additional_properties = d
        return repl_set_name_c

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
