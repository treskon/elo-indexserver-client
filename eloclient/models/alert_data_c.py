from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertDataC")


@_attrs_define
class AlertDataC:
    """<p>Bit constants for members of Alert</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_dest (Union[Unset, str]): DB column: destination
            mb_type (Union[Unset, str]): DB column: alerttype
            ln_memo (Union[Unset, int]): DB column: alertmemo
            mb_obj_id (Union[Unset, str]): DB column: objid
            mb_extra_1 (Union[Unset, str]): DB column: extra1
            mb_extra_2 (Union[Unset, str]): DB column: extra2
            mb_memo (Union[Unset, str]): DB column: alertmemo
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_source (Union[Unset, str]): DB column: source
            mb_time (Union[Unset, str]): DB column: alerttime
    """

    mb_dest: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    ln_memo: Union[Unset, int] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_extra_1: Union[Unset, str] = UNSET
    mb_extra_2: Union[Unset, str] = UNSET
    mb_memo: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_source: Union[Unset, str] = UNSET
    mb_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_dest = self.mb_dest

        mb_type = self.mb_type

        ln_memo = self.ln_memo

        mb_obj_id = self.mb_obj_id

        mb_extra_1 = self.mb_extra_1

        mb_extra_2 = self.mb_extra_2

        mb_memo = self.mb_memo

        mb_all_members = self.mb_all_members

        mb_source = self.mb_source

        mb_time = self.mb_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_dest is not UNSET:
            field_dict["mbDest"] = mb_dest
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if ln_memo is not UNSET:
            field_dict["lnMemo"] = ln_memo
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_extra_1 is not UNSET:
            field_dict["mbExtra1"] = mb_extra_1
        if mb_extra_2 is not UNSET:
            field_dict["mbExtra2"] = mb_extra_2
        if mb_memo is not UNSET:
            field_dict["mbMemo"] = mb_memo
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_source is not UNSET:
            field_dict["mbSource"] = mb_source
        if mb_time is not UNSET:
            field_dict["mbTime"] = mb_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_dest = d.pop("mbDest", UNSET)

        mb_type = d.pop("mbType", UNSET)

        ln_memo = d.pop("lnMemo", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_extra_1 = d.pop("mbExtra1", UNSET)

        mb_extra_2 = d.pop("mbExtra2", UNSET)

        mb_memo = d.pop("mbMemo", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_source = d.pop("mbSource", UNSET)

        mb_time = d.pop("mbTime", UNSET)

        alert_data_c = cls(
            mb_dest=mb_dest,
            mb_type=mb_type,
            ln_memo=ln_memo,
            mb_obj_id=mb_obj_id,
            mb_extra_1=mb_extra_1,
            mb_extra_2=mb_extra_2,
            mb_memo=mb_memo,
            mb_all_members=mb_all_members,
            mb_source=mb_source,
            mb_time=mb_time,
        )

        alert_data_c.additional_properties = d
        return alert_data_c

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
