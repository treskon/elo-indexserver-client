from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HashTagDataC")


@_attrs_define
class HashTagDataC:
    """<p>
    Bit constants for members of HashTag
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_hstg_guid (Union[Unset, str]): Member bit: HashTag GUID.
                DB column: hstgguid
            ln_hstg_guid (Union[Unset, int]): Column length: HashTag GUID.
                DB column: hstgguid
            mb_hstg_name (Union[Unset, str]): Member bit: HashTag Name.
                DB column: hstgname
            ln_hstg_name (Union[Unset, int]): Column length: HashTag Name.
                DB column: hstgname
            mb_create_date_iso (Union[Unset, str]): Member bit: Create date.
                DB column: createdateiso
            ln_create_date_iso (Union[Unset, int]): Column length: Create date.
                DB column: createdateiso
            mb_last_used_iso (Union[Unset, str]): Member bit: Last used.
                DB column: lastusediso
            ln_last_used_iso (Union[Unset, int]): Column length: Last used.
                DB column: lastusediso
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp for replication.
                DB column: tstamp
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp for replication.
                DB column: tstamp
            mb_status (Union[Unset, str]): Member bit: Status.
                DB column: status
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_hstg_guid: Union[Unset, str] = UNSET
    ln_hstg_guid: Union[Unset, int] = UNSET
    mb_hstg_name: Union[Unset, str] = UNSET
    ln_hstg_name: Union[Unset, int] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_last_used_iso: Union[Unset, str] = UNSET
    ln_last_used_iso: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_hstg_guid = self.mb_hstg_guid
        ln_hstg_guid = self.ln_hstg_guid
        mb_hstg_name = self.mb_hstg_name
        ln_hstg_name = self.ln_hstg_name
        mb_create_date_iso = self.mb_create_date_iso
        ln_create_date_iso = self.ln_create_date_iso
        mb_last_used_iso = self.mb_last_used_iso
        ln_last_used_iso = self.ln_last_used_iso
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_status = self.mb_status
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_hstg_guid is not UNSET:
            field_dict["mbHstgGuid"] = mb_hstg_guid
        if ln_hstg_guid is not UNSET:
            field_dict["lnHstgGuid"] = ln_hstg_guid
        if mb_hstg_name is not UNSET:
            field_dict["mbHstgName"] = mb_hstg_name
        if ln_hstg_name is not UNSET:
            field_dict["lnHstgName"] = ln_hstg_name
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_last_used_iso is not UNSET:
            field_dict["mbLastUsedIso"] = mb_last_used_iso
        if ln_last_used_iso is not UNSET:
            field_dict["lnLastUsedIso"] = ln_last_used_iso
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_hstg_guid = d.pop("mbHstgGuid", UNSET)

        ln_hstg_guid = d.pop("lnHstgGuid", UNSET)

        mb_hstg_name = d.pop("mbHstgName", UNSET)

        ln_hstg_name = d.pop("lnHstgName", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_last_used_iso = d.pop("mbLastUsedIso", UNSET)

        ln_last_used_iso = d.pop("lnLastUsedIso", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        hash_tag_data_c = cls(
            mb_hstg_guid=mb_hstg_guid,
            ln_hstg_guid=ln_hstg_guid,
            mb_hstg_name=mb_hstg_name,
            ln_hstg_name=ln_hstg_name,
            mb_create_date_iso=mb_create_date_iso,
            ln_create_date_iso=ln_create_date_iso,
            mb_last_used_iso=mb_last_used_iso,
            ln_last_used_iso=ln_last_used_iso,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_status=mb_status,
            mb_all_members=mb_all_members,
        )

        hash_tag_data_c.additional_properties = d
        return hash_tag_data_c

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
