from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapHistHeadC")


@_attrs_define
class MapHistHeadC:
    """<p>Bit constants for members of MapHist</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_user_name (Union[Unset, int]): DB column: mapusername
            mb_time_stamp_utc (Union[Unset, str]): DB column: maphistts
            mb_time_stamp_local (Union[Unset, str]): DB column: maphistlocts
            ln_hist_guid (Union[Unset, int]): Column length: Serialisation version ID
                DB column: maphistguid
            mb_user_name (Union[Unset, str]): DB column: mapusername
            ln_time_stamp_local (Union[Unset, int]): DB column: maphistlocts
            mb_user_id (Union[Unset, str]): DB column: mapuser
            ln_work_station (Union[Unset, int]): DB column: maphistwks
            mb_hist_source (Union[Unset, str]): DB column: maphistsrc
            ln_map_guid (Union[Unset, int]): DB column: mapguid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_map_guid (Union[Unset, str]): DB column: mapguid
            ln_time_stamp_utc (Union[Unset, int]): DB column: maphistts
            mb_work_station (Union[Unset, str]): DB column: maphistwks
            mb_hist_guid (Union[Unset, str]): Member bit: Serialisation version ID
                DB column: maphistguid
    """

    ln_user_name: Union[Unset, int] = UNSET
    mb_time_stamp_utc: Union[Unset, str] = UNSET
    mb_time_stamp_local: Union[Unset, str] = UNSET
    ln_hist_guid: Union[Unset, int] = UNSET
    mb_user_name: Union[Unset, str] = UNSET
    ln_time_stamp_local: Union[Unset, int] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    ln_work_station: Union[Unset, int] = UNSET
    mb_hist_source: Union[Unset, str] = UNSET
    ln_map_guid: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_map_guid: Union[Unset, str] = UNSET
    ln_time_stamp_utc: Union[Unset, int] = UNSET
    mb_work_station: Union[Unset, str] = UNSET
    mb_hist_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_user_name = self.ln_user_name

        mb_time_stamp_utc = self.mb_time_stamp_utc

        mb_time_stamp_local = self.mb_time_stamp_local

        ln_hist_guid = self.ln_hist_guid

        mb_user_name = self.mb_user_name

        ln_time_stamp_local = self.ln_time_stamp_local

        mb_user_id = self.mb_user_id

        ln_work_station = self.ln_work_station

        mb_hist_source = self.mb_hist_source

        ln_map_guid = self.ln_map_guid

        mb_all_members = self.mb_all_members

        mb_map_guid = self.mb_map_guid

        ln_time_stamp_utc = self.ln_time_stamp_utc

        mb_work_station = self.mb_work_station

        mb_hist_guid = self.mb_hist_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_user_name is not UNSET:
            field_dict["lnUserName"] = ln_user_name
        if mb_time_stamp_utc is not UNSET:
            field_dict["mbTimeStampUTC"] = mb_time_stamp_utc
        if mb_time_stamp_local is not UNSET:
            field_dict["mbTimeStampLocal"] = mb_time_stamp_local
        if ln_hist_guid is not UNSET:
            field_dict["lnHistGuid"] = ln_hist_guid
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if ln_time_stamp_local is not UNSET:
            field_dict["lnTimeStampLocal"] = ln_time_stamp_local
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if ln_work_station is not UNSET:
            field_dict["lnWorkStation"] = ln_work_station
        if mb_hist_source is not UNSET:
            field_dict["mbHistSource"] = mb_hist_source
        if ln_map_guid is not UNSET:
            field_dict["lnMapGuid"] = ln_map_guid
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_map_guid is not UNSET:
            field_dict["mbMapGuid"] = mb_map_guid
        if ln_time_stamp_utc is not UNSET:
            field_dict["lnTimeStampUTC"] = ln_time_stamp_utc
        if mb_work_station is not UNSET:
            field_dict["mbWorkStation"] = mb_work_station
        if mb_hist_guid is not UNSET:
            field_dict["mbHistGuid"] = mb_hist_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_user_name = d.pop("lnUserName", UNSET)

        mb_time_stamp_utc = d.pop("mbTimeStampUTC", UNSET)

        mb_time_stamp_local = d.pop("mbTimeStampLocal", UNSET)

        ln_hist_guid = d.pop("lnHistGuid", UNSET)

        mb_user_name = d.pop("mbUserName", UNSET)

        ln_time_stamp_local = d.pop("lnTimeStampLocal", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        ln_work_station = d.pop("lnWorkStation", UNSET)

        mb_hist_source = d.pop("mbHistSource", UNSET)

        ln_map_guid = d.pop("lnMapGuid", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_map_guid = d.pop("mbMapGuid", UNSET)

        ln_time_stamp_utc = d.pop("lnTimeStampUTC", UNSET)

        mb_work_station = d.pop("mbWorkStation", UNSET)

        mb_hist_guid = d.pop("mbHistGuid", UNSET)

        map_hist_head_c = cls(
            ln_user_name=ln_user_name,
            mb_time_stamp_utc=mb_time_stamp_utc,
            mb_time_stamp_local=mb_time_stamp_local,
            ln_hist_guid=ln_hist_guid,
            mb_user_name=mb_user_name,
            ln_time_stamp_local=ln_time_stamp_local,
            mb_user_id=mb_user_id,
            ln_work_station=ln_work_station,
            mb_hist_source=mb_hist_source,
            ln_map_guid=ln_map_guid,
            mb_all_members=mb_all_members,
            mb_map_guid=mb_map_guid,
            ln_time_stamp_utc=ln_time_stamp_utc,
            mb_work_station=mb_work_station,
            mb_hist_guid=mb_hist_guid,
        )

        map_hist_head_c.additional_properties = d
        return map_hist_head_c

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
