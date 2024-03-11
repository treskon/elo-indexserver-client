from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysDelDataC")


@_attrs_define
class PhysDelDataC:
    """<p>
    Bit constants for members of PhysDel
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_guid (Union[Unset, str]): DB column: pdguid
            ln_guid (Union[Unset, int]): DB column: pdguid
            mb_type (Union[Unset, str]): DB column: pdtype
            mb_t_stamp (Union[Unset, str]): DB column: pdtstamp
            ln_t_stamp (Union[Unset, int]): DB column: pdtstamp
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: tstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: tstampsync
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_type = self.mb_type
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
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
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
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

        mb_type = d.pop("mbType", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        phys_del_data_c = cls(
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_type=mb_type,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_all_members=mb_all_members,
        )

        phys_del_data_c.additional_properties = d
        return phys_del_data_c

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
