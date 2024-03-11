from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColorDataInternC")


@_attrs_define
class ColorDataInternC:
    """<p>
    Bit constants for members of ColorData
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: colorno
            mb_name (Union[Unset, str]): DB column: colorname
            ln_name (Union[Unset, int]): DB column: colorname
            mb_rgb (Union[Unset, str]): DB column: colorid
            mb_status (Union[Unset, str]): DB column: colorstatus
            mb_guid (Union[Unset, str]): Member bit: GUID DB column: colorguid
            ln_guid (Union[Unset, int]): Column length: GUID DB column: colorguid
            mb_t_stamp (Union[Unset, str]): Member bit: TStamp DB column: colortstamp
            ln_t_stamp (Union[Unset, int]): Column length: TStamp DB column: colortstamp
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: colortstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: colortstampsync
            mb_flags (Union[Unset, str]): Member bit: This color should not be selectable in client applications.
                DB column: colorflags
            mb_package_name (Union[Unset, str]): Member bit: Package name of ColorData DB column: packagename
            ln_package_name (Union[Unset, int]): Column length: Package name of ColorData DB column: packagename
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_id: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_rgb: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id
        mb_name = self.mb_name
        ln_name = self.ln_name
        mb_rgb = self.mb_rgb
        mb_status = self.mb_status
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_flags = self.mb_flags
        mb_package_name = self.mb_package_name
        ln_package_name = self.ln_package_name
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_rgb is not UNSET:
            field_dict["mbRGB"] = mb_rgb
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
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
        mb_id = d.pop("mbId", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_rgb = d.pop("mbRGB", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        color_data_intern_c = cls(
            mb_id=mb_id,
            mb_name=mb_name,
            ln_name=ln_name,
            mb_rgb=mb_rgb,
            mb_status=mb_status,
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_flags=mb_flags,
            mb_package_name=mb_package_name,
            ln_package_name=ln_package_name,
            mb_all_members=mb_all_members,
        )

        color_data_intern_c.additional_properties = d
        return color_data_intern_c

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
