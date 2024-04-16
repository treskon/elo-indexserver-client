from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderC")


@_attrs_define
class ReminderC:
    """
    Attributes:
        mb_all (Union[Unset, str]): All valid member bits.
        mb_receiver_name (Union[Unset, str]):
        mb_sender_name (Union[Unset, str]):
        mb_notify_on_delete (Union[Unset, str]):
        mb_create_date_iso (Union[Unset, str]):
        mb_prompt_date_iso (Union[Unset, str]):
        mb_due_date_iso (Union[Unset, str]):
        mb_lock_name (Union[Unset, str]):
        mb_notify_on_view (Union[Unset, str]):
        mb_deleted (Union[Unset, str]):
        mb_obj_guid (Union[Unset, str]): Sord guid.
    """

    mb_all: Union[Unset, str] = UNSET
    mb_receiver_name: Union[Unset, str] = UNSET
    mb_sender_name: Union[Unset, str] = UNSET
    mb_notify_on_delete: Union[Unset, str] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    mb_prompt_date_iso: Union[Unset, str] = UNSET
    mb_due_date_iso: Union[Unset, str] = UNSET
    mb_lock_name: Union[Unset, str] = UNSET
    mb_notify_on_view: Union[Unset, str] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    mb_obj_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all = self.mb_all

        mb_receiver_name = self.mb_receiver_name

        mb_sender_name = self.mb_sender_name

        mb_notify_on_delete = self.mb_notify_on_delete

        mb_create_date_iso = self.mb_create_date_iso

        mb_prompt_date_iso = self.mb_prompt_date_iso

        mb_due_date_iso = self.mb_due_date_iso

        mb_lock_name = self.mb_lock_name

        mb_notify_on_view = self.mb_notify_on_view

        mb_deleted = self.mb_deleted

        mb_obj_guid = self.mb_obj_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_receiver_name is not UNSET:
            field_dict["mbReceiverName"] = mb_receiver_name
        if mb_sender_name is not UNSET:
            field_dict["mbSenderName"] = mb_sender_name
        if mb_notify_on_delete is not UNSET:
            field_dict["mbNotifyOnDelete"] = mb_notify_on_delete
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if mb_prompt_date_iso is not UNSET:
            field_dict["mbPromptDateIso"] = mb_prompt_date_iso
        if mb_due_date_iso is not UNSET:
            field_dict["mbDueDateIso"] = mb_due_date_iso
        if mb_lock_name is not UNSET:
            field_dict["mbLockName"] = mb_lock_name
        if mb_notify_on_view is not UNSET:
            field_dict["mbNotifyOnView"] = mb_notify_on_view
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if mb_obj_guid is not UNSET:
            field_dict["mbObjGuid"] = mb_obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_all = d.pop("mbAll", UNSET)

        mb_receiver_name = d.pop("mbReceiverName", UNSET)

        mb_sender_name = d.pop("mbSenderName", UNSET)

        mb_notify_on_delete = d.pop("mbNotifyOnDelete", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        mb_prompt_date_iso = d.pop("mbPromptDateIso", UNSET)

        mb_due_date_iso = d.pop("mbDueDateIso", UNSET)

        mb_lock_name = d.pop("mbLockName", UNSET)

        mb_notify_on_view = d.pop("mbNotifyOnView", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        mb_obj_guid = d.pop("mbObjGuid", UNSET)

        reminder_c = cls(
            mb_all=mb_all,
            mb_receiver_name=mb_receiver_name,
            mb_sender_name=mb_sender_name,
            mb_notify_on_delete=mb_notify_on_delete,
            mb_create_date_iso=mb_create_date_iso,
            mb_prompt_date_iso=mb_prompt_date_iso,
            mb_due_date_iso=mb_due_date_iso,
            mb_lock_name=mb_lock_name,
            mb_notify_on_view=mb_notify_on_view,
            mb_deleted=mb_deleted,
            mb_obj_guid=mb_obj_guid,
        )

        reminder_c.additional_properties = d
        return reminder_c

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
