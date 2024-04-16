from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepliHistC")


@_attrs_define
class RepliHistC:
    """<p>Bit constants for members of RepliHist</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_ts_begin (Union[Unset, str]): DB column: rhtsbegin
            mb_id (Union[Unset, str]): DB column: rhrowid
            mb_arc_short (Union[Unset, str]): DB column: rharcshort
            mb_im_ex (Union[Unset, str]): DB column: rhimex
            ln_arc_short (Union[Unset, int]): DB column: rharcshort
            ln_ts_end (Union[Unset, int]): DB column: rhtsend
            mb_ts_date (Union[Unset, str]): DB column: rhtsdate
            mb_arc_desc (Union[Unset, str]): DB column: rharcdesc
            ln_arc_guid (Union[Unset, int]): DB column: rharcguid
            mb_arc_guid (Union[Unset, str]): DB column: rharcguid
            mb_ts_end (Union[Unset, str]): DB column: rhtsend
            ln_arc_desc (Union[Unset, int]): DB column: rharcdesc
            mb_arc_priority_local (Union[Unset, str]): DB column: rhpriolocal
            mb_arc_priority_remote (Union[Unset, str]): DB column: rhprioremote
            ln_ts_begin (Union[Unset, int]): DB column: rhtsbegin
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_ts_date (Union[Unset, int]): DB column: rhtsdate
            mb_succ (Union[Unset, str]): DB column: rhsucc
    """

    mb_ts_begin: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_arc_short: Union[Unset, str] = UNSET
    mb_im_ex: Union[Unset, str] = UNSET
    ln_arc_short: Union[Unset, int] = UNSET
    ln_ts_end: Union[Unset, int] = UNSET
    mb_ts_date: Union[Unset, str] = UNSET
    mb_arc_desc: Union[Unset, str] = UNSET
    ln_arc_guid: Union[Unset, int] = UNSET
    mb_arc_guid: Union[Unset, str] = UNSET
    mb_ts_end: Union[Unset, str] = UNSET
    ln_arc_desc: Union[Unset, int] = UNSET
    mb_arc_priority_local: Union[Unset, str] = UNSET
    mb_arc_priority_remote: Union[Unset, str] = UNSET
    ln_ts_begin: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_ts_date: Union[Unset, int] = UNSET
    mb_succ: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_ts_begin = self.mb_ts_begin

        mb_id = self.mb_id

        mb_arc_short = self.mb_arc_short

        mb_im_ex = self.mb_im_ex

        ln_arc_short = self.ln_arc_short

        ln_ts_end = self.ln_ts_end

        mb_ts_date = self.mb_ts_date

        mb_arc_desc = self.mb_arc_desc

        ln_arc_guid = self.ln_arc_guid

        mb_arc_guid = self.mb_arc_guid

        mb_ts_end = self.mb_ts_end

        ln_arc_desc = self.ln_arc_desc

        mb_arc_priority_local = self.mb_arc_priority_local

        mb_arc_priority_remote = self.mb_arc_priority_remote

        ln_ts_begin = self.ln_ts_begin

        mb_all_members = self.mb_all_members

        ln_ts_date = self.ln_ts_date

        mb_succ = self.mb_succ

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_ts_begin is not UNSET:
            field_dict["mbTSBegin"] = mb_ts_begin
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_arc_short is not UNSET:
            field_dict["mbArcShort"] = mb_arc_short
        if mb_im_ex is not UNSET:
            field_dict["mbImEx"] = mb_im_ex
        if ln_arc_short is not UNSET:
            field_dict["lnArcShort"] = ln_arc_short
        if ln_ts_end is not UNSET:
            field_dict["lnTSEnd"] = ln_ts_end
        if mb_ts_date is not UNSET:
            field_dict["mbTSDate"] = mb_ts_date
        if mb_arc_desc is not UNSET:
            field_dict["mbArcDesc"] = mb_arc_desc
        if ln_arc_guid is not UNSET:
            field_dict["lnArcGuid"] = ln_arc_guid
        if mb_arc_guid is not UNSET:
            field_dict["mbArcGuid"] = mb_arc_guid
        if mb_ts_end is not UNSET:
            field_dict["mbTSEnd"] = mb_ts_end
        if ln_arc_desc is not UNSET:
            field_dict["lnArcDesc"] = ln_arc_desc
        if mb_arc_priority_local is not UNSET:
            field_dict["mbArcPriorityLocal"] = mb_arc_priority_local
        if mb_arc_priority_remote is not UNSET:
            field_dict["mbArcPriorityRemote"] = mb_arc_priority_remote
        if ln_ts_begin is not UNSET:
            field_dict["lnTSBegin"] = ln_ts_begin
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_ts_date is not UNSET:
            field_dict["lnTSDate"] = ln_ts_date
        if mb_succ is not UNSET:
            field_dict["mbSucc"] = mb_succ

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_ts_begin = d.pop("mbTSBegin", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_arc_short = d.pop("mbArcShort", UNSET)

        mb_im_ex = d.pop("mbImEx", UNSET)

        ln_arc_short = d.pop("lnArcShort", UNSET)

        ln_ts_end = d.pop("lnTSEnd", UNSET)

        mb_ts_date = d.pop("mbTSDate", UNSET)

        mb_arc_desc = d.pop("mbArcDesc", UNSET)

        ln_arc_guid = d.pop("lnArcGuid", UNSET)

        mb_arc_guid = d.pop("mbArcGuid", UNSET)

        mb_ts_end = d.pop("mbTSEnd", UNSET)

        ln_arc_desc = d.pop("lnArcDesc", UNSET)

        mb_arc_priority_local = d.pop("mbArcPriorityLocal", UNSET)

        mb_arc_priority_remote = d.pop("mbArcPriorityRemote", UNSET)

        ln_ts_begin = d.pop("lnTSBegin", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_ts_date = d.pop("lnTSDate", UNSET)

        mb_succ = d.pop("mbSucc", UNSET)

        repli_hist_c = cls(
            mb_ts_begin=mb_ts_begin,
            mb_id=mb_id,
            mb_arc_short=mb_arc_short,
            mb_im_ex=mb_im_ex,
            ln_arc_short=ln_arc_short,
            ln_ts_end=ln_ts_end,
            mb_ts_date=mb_ts_date,
            mb_arc_desc=mb_arc_desc,
            ln_arc_guid=ln_arc_guid,
            mb_arc_guid=mb_arc_guid,
            mb_ts_end=mb_ts_end,
            ln_arc_desc=ln_arc_desc,
            mb_arc_priority_local=mb_arc_priority_local,
            mb_arc_priority_remote=mb_arc_priority_remote,
            ln_ts_begin=ln_ts_begin,
            mb_all_members=mb_all_members,
            ln_ts_date=ln_ts_date,
            mb_succ=mb_succ,
        )

        repli_hist_c.additional_properties = d
        return repli_hist_c

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
