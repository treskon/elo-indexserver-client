from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportC")


@_attrs_define
class ReportC:
    """<p>Bit constants for members of ReportInfo</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: reportid
            mb_extra_1 (Union[Unset, str]): DB column: extra1
            mb_extra_2 (Union[Unset, str]): DB column: extra2
            mb_user_id (Union[Unset, str]): DB column: userid
            mb_extra_3 (Union[Unset, str]): Member bit: Reserved.
                DB column: extra3
            mb_session_no (Union[Unset, str]): DB column: sessionno
            mb_text (Union[Unset, str]): DB column: addtext
            ln_text (Union[Unset, int]): DB column: addtext
            ln_id (Union[Unset, int]): DB column: reportid
            mb_act_time (Union[Unset, str]): DB column: acttime
            mb_obj_id (Union[Unset, str]): DB column: docid
            mb_action_no (Union[Unset, str]): DB column: actionno
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_extra_3 (Union[Unset, int]): Column length: Reserved.
                DB column: extra3
    """

    mb_id: Union[Unset, str] = UNSET
    mb_extra_1: Union[Unset, str] = UNSET
    mb_extra_2: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_extra_3: Union[Unset, str] = UNSET
    mb_session_no: Union[Unset, str] = UNSET
    mb_text: Union[Unset, str] = UNSET
    ln_text: Union[Unset, int] = UNSET
    ln_id: Union[Unset, int] = UNSET
    mb_act_time: Union[Unset, str] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_action_no: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_extra_3: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id

        mb_extra_1 = self.mb_extra_1

        mb_extra_2 = self.mb_extra_2

        mb_user_id = self.mb_user_id

        mb_extra_3 = self.mb_extra_3

        mb_session_no = self.mb_session_no

        mb_text = self.mb_text

        ln_text = self.ln_text

        ln_id = self.ln_id

        mb_act_time = self.mb_act_time

        mb_obj_id = self.mb_obj_id

        mb_action_no = self.mb_action_no

        mb_all_members = self.mb_all_members

        ln_extra_3 = self.ln_extra_3

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_extra_1 is not UNSET:
            field_dict["mbExtra1"] = mb_extra_1
        if mb_extra_2 is not UNSET:
            field_dict["mbExtra2"] = mb_extra_2
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_extra_3 is not UNSET:
            field_dict["mbExtra3"] = mb_extra_3
        if mb_session_no is not UNSET:
            field_dict["mbSessionNo"] = mb_session_no
        if mb_text is not UNSET:
            field_dict["mbText"] = mb_text
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if mb_act_time is not UNSET:
            field_dict["mbActTime"] = mb_act_time
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_action_no is not UNSET:
            field_dict["mbActionNo"] = mb_action_no
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_extra_3 is not UNSET:
            field_dict["lnExtra3"] = ln_extra_3

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_extra_1 = d.pop("mbExtra1", UNSET)

        mb_extra_2 = d.pop("mbExtra2", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_extra_3 = d.pop("mbExtra3", UNSET)

        mb_session_no = d.pop("mbSessionNo", UNSET)

        mb_text = d.pop("mbText", UNSET)

        ln_text = d.pop("lnText", UNSET)

        ln_id = d.pop("lnId", UNSET)

        mb_act_time = d.pop("mbActTime", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_action_no = d.pop("mbActionNo", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_extra_3 = d.pop("lnExtra3", UNSET)

        report_c = cls(
            mb_id=mb_id,
            mb_extra_1=mb_extra_1,
            mb_extra_2=mb_extra_2,
            mb_user_id=mb_user_id,
            mb_extra_3=mb_extra_3,
            mb_session_no=mb_session_no,
            mb_text=mb_text,
            ln_text=ln_text,
            ln_id=ln_id,
            mb_act_time=mb_act_time,
            mb_obj_id=mb_obj_id,
            mb_action_no=mb_action_no,
            mb_all_members=mb_all_members,
            ln_extra_3=ln_extra_3,
        )

        report_c.additional_properties = d
        return report_c

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
