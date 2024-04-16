from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjHistC")


@_attrs_define
class ObjHistC:
    """<p>Bit constants for members of SordHist</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_user_name (Union[Unset, int]): DB column: username
            mb_time_stamp_utc (Union[Unset, str]): DB column: objhistts
            ln_obj_guid (Union[Unset, int]): DB column: objguid
            mb_time_stamp_local (Union[Unset, str]): DB column: objhistlocts
            ln_hist_guid (Union[Unset, int]): Column length: Serialisation version ID
                DB column: objhistguid
            mb_user_name (Union[Unset, str]): DB column: username
            ln_time_stamp_local (Union[Unset, int]): DB column: objhistlocts
            ln_work_station (Union[Unset, int]): DB column: objhistwks
            mb_hist_source (Union[Unset, str]): DB column: objhistsrc
            mb_user_no (Union[Unset, str]): DB column: objuser
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_time_stamp_utc (Union[Unset, int]): DB column: objhistts
            mb_work_station (Union[Unset, str]): DB column: objhistwks
            mb_hist_guid (Union[Unset, str]): Member bit: Serialisation version ID
                DB column: objhistguid
            mb_obj_guid (Union[Unset, str]): DB column: objguid
    """

    ln_user_name: Union[Unset, int] = UNSET
    mb_time_stamp_utc: Union[Unset, str] = UNSET
    ln_obj_guid: Union[Unset, int] = UNSET
    mb_time_stamp_local: Union[Unset, str] = UNSET
    ln_hist_guid: Union[Unset, int] = UNSET
    mb_user_name: Union[Unset, str] = UNSET
    ln_time_stamp_local: Union[Unset, int] = UNSET
    ln_work_station: Union[Unset, int] = UNSET
    mb_hist_source: Union[Unset, str] = UNSET
    mb_user_no: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_time_stamp_utc: Union[Unset, int] = UNSET
    mb_work_station: Union[Unset, str] = UNSET
    mb_hist_guid: Union[Unset, str] = UNSET
    mb_obj_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_user_name = self.ln_user_name

        mb_time_stamp_utc = self.mb_time_stamp_utc

        ln_obj_guid = self.ln_obj_guid

        mb_time_stamp_local = self.mb_time_stamp_local

        ln_hist_guid = self.ln_hist_guid

        mb_user_name = self.mb_user_name

        ln_time_stamp_local = self.ln_time_stamp_local

        ln_work_station = self.ln_work_station

        mb_hist_source = self.mb_hist_source

        mb_user_no = self.mb_user_no

        mb_all_members = self.mb_all_members

        ln_time_stamp_utc = self.ln_time_stamp_utc

        mb_work_station = self.mb_work_station

        mb_hist_guid = self.mb_hist_guid

        mb_obj_guid = self.mb_obj_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_user_name is not UNSET:
            field_dict["lnUserName"] = ln_user_name
        if mb_time_stamp_utc is not UNSET:
            field_dict["mbTimeStampUTC"] = mb_time_stamp_utc
        if ln_obj_guid is not UNSET:
            field_dict["lnObjGuid"] = ln_obj_guid
        if mb_time_stamp_local is not UNSET:
            field_dict["mbTimeStampLocal"] = mb_time_stamp_local
        if ln_hist_guid is not UNSET:
            field_dict["lnHistGuid"] = ln_hist_guid
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if ln_time_stamp_local is not UNSET:
            field_dict["lnTimeStampLocal"] = ln_time_stamp_local
        if ln_work_station is not UNSET:
            field_dict["lnWorkStation"] = ln_work_station
        if mb_hist_source is not UNSET:
            field_dict["mbHistSource"] = mb_hist_source
        if mb_user_no is not UNSET:
            field_dict["mbUserNo"] = mb_user_no
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_time_stamp_utc is not UNSET:
            field_dict["lnTimeStampUTC"] = ln_time_stamp_utc
        if mb_work_station is not UNSET:
            field_dict["mbWorkStation"] = mb_work_station
        if mb_hist_guid is not UNSET:
            field_dict["mbHistGuid"] = mb_hist_guid
        if mb_obj_guid is not UNSET:
            field_dict["mbObjGuid"] = mb_obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_user_name = d.pop("lnUserName", UNSET)

        mb_time_stamp_utc = d.pop("mbTimeStampUTC", UNSET)

        ln_obj_guid = d.pop("lnObjGuid", UNSET)

        mb_time_stamp_local = d.pop("mbTimeStampLocal", UNSET)

        ln_hist_guid = d.pop("lnHistGuid", UNSET)

        mb_user_name = d.pop("mbUserName", UNSET)

        ln_time_stamp_local = d.pop("lnTimeStampLocal", UNSET)

        ln_work_station = d.pop("lnWorkStation", UNSET)

        mb_hist_source = d.pop("mbHistSource", UNSET)

        mb_user_no = d.pop("mbUserNo", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_time_stamp_utc = d.pop("lnTimeStampUTC", UNSET)

        mb_work_station = d.pop("mbWorkStation", UNSET)

        mb_hist_guid = d.pop("mbHistGuid", UNSET)

        mb_obj_guid = d.pop("mbObjGuid", UNSET)

        obj_hist_c = cls(
            ln_user_name=ln_user_name,
            mb_time_stamp_utc=mb_time_stamp_utc,
            ln_obj_guid=ln_obj_guid,
            mb_time_stamp_local=mb_time_stamp_local,
            ln_hist_guid=ln_hist_guid,
            mb_user_name=mb_user_name,
            ln_time_stamp_local=ln_time_stamp_local,
            ln_work_station=ln_work_station,
            mb_hist_source=mb_hist_source,
            mb_user_no=mb_user_no,
            mb_all_members=mb_all_members,
            ln_time_stamp_utc=ln_time_stamp_utc,
            mb_work_station=mb_work_station,
            mb_hist_guid=mb_hist_guid,
            mb_obj_guid=mb_obj_guid,
        )

        obj_hist_c.additional_properties = d
        return obj_hist_c

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
