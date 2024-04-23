from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderDataC")


@_attrs_define
class ReminderDataC:
    """<p>Bit constants for members of Reminder</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: wvident
            mb_action_code (Union[Unset, str]): DB column: action
            mb_desc (Union[Unset, str]): DB column: wvdesc
            mb_receiver_id (Union[Unset, str]): DB column: userowner
            mb_lock_id (Union[Unset, str]): DB column: wvlock
            mb_obj_type (Union[Unset, str]): DB column: parenttype
            mb_create_date (Union[Unset, str]): DB column: createdate
            mb_name (Union[Unset, str]): DB column: short
            ln_desc (Union[Unset, int]): DB column: wvdesc
            mb_prompt_date (Union[Unset, str]): DB column: wvdate
            mb_sender_id (Union[Unset, str]): DB column: userfrom
            ln_name (Union[Unset, int]): DB column: short
            mb_obj_id (Union[Unset, str]): DB column: parentid
            mb_prio (Union[Unset, str]): DB column: prio
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_due_date (Union[Unset, str]): DB column: duedate
    """

    mb_id: Union[Unset, str] = UNSET
    mb_action_code: Union[Unset, str] = UNSET
    mb_desc: Union[Unset, str] = UNSET
    mb_receiver_id: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_obj_type: Union[Unset, str] = UNSET
    mb_create_date: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_desc: Union[Unset, int] = UNSET
    mb_prompt_date: Union[Unset, str] = UNSET
    mb_sender_id: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_due_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id

        mb_action_code = self.mb_action_code

        mb_desc = self.mb_desc

        mb_receiver_id = self.mb_receiver_id

        mb_lock_id = self.mb_lock_id

        mb_obj_type = self.mb_obj_type

        mb_create_date = self.mb_create_date

        mb_name = self.mb_name

        ln_desc = self.ln_desc

        mb_prompt_date = self.mb_prompt_date

        mb_sender_id = self.mb_sender_id

        ln_name = self.ln_name

        mb_obj_id = self.mb_obj_id

        mb_prio = self.mb_prio

        mb_all_members = self.mb_all_members

        mb_due_date = self.mb_due_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_action_code is not UNSET:
            field_dict["mbActionCode"] = mb_action_code
        if mb_desc is not UNSET:
            field_dict["mbDesc"] = mb_desc
        if mb_receiver_id is not UNSET:
            field_dict["mbReceiverId"] = mb_receiver_id
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_obj_type is not UNSET:
            field_dict["mbObjType"] = mb_obj_type
        if mb_create_date is not UNSET:
            field_dict["mbCreateDate"] = mb_create_date
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_desc is not UNSET:
            field_dict["lnDesc"] = ln_desc
        if mb_prompt_date is not UNSET:
            field_dict["mbPromptDate"] = mb_prompt_date
        if mb_sender_id is not UNSET:
            field_dict["mbSenderId"] = mb_sender_id
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_due_date is not UNSET:
            field_dict["mbDueDate"] = mb_due_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_action_code = d.pop("mbActionCode", UNSET)

        mb_desc = d.pop("mbDesc", UNSET)

        mb_receiver_id = d.pop("mbReceiverId", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_obj_type = d.pop("mbObjType", UNSET)

        mb_create_date = d.pop("mbCreateDate", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_desc = d.pop("lnDesc", UNSET)

        mb_prompt_date = d.pop("mbPromptDate", UNSET)

        mb_sender_id = d.pop("mbSenderId", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_due_date = d.pop("mbDueDate", UNSET)

        reminder_data_c = cls(
            mb_id=mb_id,
            mb_action_code=mb_action_code,
            mb_desc=mb_desc,
            mb_receiver_id=mb_receiver_id,
            mb_lock_id=mb_lock_id,
            mb_obj_type=mb_obj_type,
            mb_create_date=mb_create_date,
            mb_name=mb_name,
            ln_desc=ln_desc,
            mb_prompt_date=mb_prompt_date,
            mb_sender_id=mb_sender_id,
            ln_name=ln_name,
            mb_obj_id=mb_obj_id,
            mb_prio=mb_prio,
            mb_all_members=mb_all_members,
            mb_due_date=mb_due_date,
        )

        reminder_data_c.additional_properties = d
        return reminder_data_c

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
