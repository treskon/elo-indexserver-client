from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepliHist")


@_attrs_define
class RepliHist:
    """Internal class

    Attributes:
        arc_short (Union[Unset, str]): DB column: rharcshort
        arc_guid (Union[Unset, str]): DB column: rharcguid
        arc_priority_local (Union[Unset, int]):
        succ (Union[Unset, int]): DB column: rhsucc
        t_s_end (Union[Unset, str]): DB column: rhtsend
        im_ex (Union[Unset, int]): DB column: rhimex
        arc_priority_remote (Union[Unset, int]):
        t_s_date (Union[Unset, str]): DB column: rhtsdate
        id (Union[Unset, int]): DB column: rhrowid
        arc_desc (Union[Unset, str]): DB column: rharcdesc
        t_s_begin (Union[Unset, str]): DB column: rhtsbegin
    """

    arc_short: Union[Unset, str] = UNSET
    arc_guid: Union[Unset, str] = UNSET
    arc_priority_local: Union[Unset, int] = UNSET
    succ: Union[Unset, int] = UNSET
    t_s_end: Union[Unset, str] = UNSET
    im_ex: Union[Unset, int] = UNSET
    arc_priority_remote: Union[Unset, int] = UNSET
    t_s_date: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    arc_desc: Union[Unset, str] = UNSET
    t_s_begin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arc_short = self.arc_short

        arc_guid = self.arc_guid

        arc_priority_local = self.arc_priority_local

        succ = self.succ

        t_s_end = self.t_s_end

        im_ex = self.im_ex

        arc_priority_remote = self.arc_priority_remote

        t_s_date = self.t_s_date

        id = self.id

        arc_desc = self.arc_desc

        t_s_begin = self.t_s_begin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arc_short is not UNSET:
            field_dict["arcShort"] = arc_short
        if arc_guid is not UNSET:
            field_dict["arcGuid"] = arc_guid
        if arc_priority_local is not UNSET:
            field_dict["arcPriorityLocal"] = arc_priority_local
        if succ is not UNSET:
            field_dict["succ"] = succ
        if t_s_end is not UNSET:
            field_dict["tSEnd"] = t_s_end
        if im_ex is not UNSET:
            field_dict["imEx"] = im_ex
        if arc_priority_remote is not UNSET:
            field_dict["arcPriorityRemote"] = arc_priority_remote
        if t_s_date is not UNSET:
            field_dict["tSDate"] = t_s_date
        if id is not UNSET:
            field_dict["id"] = id
        if arc_desc is not UNSET:
            field_dict["arcDesc"] = arc_desc
        if t_s_begin is not UNSET:
            field_dict["tSBegin"] = t_s_begin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        arc_short = d.pop("arcShort", UNSET)

        arc_guid = d.pop("arcGuid", UNSET)

        arc_priority_local = d.pop("arcPriorityLocal", UNSET)

        succ = d.pop("succ", UNSET)

        t_s_end = d.pop("tSEnd", UNSET)

        im_ex = d.pop("imEx", UNSET)

        arc_priority_remote = d.pop("arcPriorityRemote", UNSET)

        t_s_date = d.pop("tSDate", UNSET)

        id = d.pop("id", UNSET)

        arc_desc = d.pop("arcDesc", UNSET)

        t_s_begin = d.pop("tSBegin", UNSET)

        repli_hist = cls(
            arc_short=arc_short,
            arc_guid=arc_guid,
            arc_priority_local=arc_priority_local,
            succ=succ,
            t_s_end=t_s_end,
            im_ex=im_ex,
            arc_priority_remote=arc_priority_remote,
            t_s_date=t_s_date,
            id=id,
            arc_desc=arc_desc,
            t_s_begin=t_s_begin,
        )

        repli_hist.additional_properties = d
        return repli_hist

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
