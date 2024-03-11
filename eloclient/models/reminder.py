from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reminder")


@_attrs_define
class Reminder:
    """
    Attributes:
        desc (Union[Unset, str]): Memo text
        id (Union[Unset, int]): Reminder ID
        lock_id (Union[Unset, int]): ID of user who has locked the reminder record in DB
        name (Union[Unset, str]): Short description visible in the task list.
        obj_id (Union[Unset, int]): Reminder is linked to this Sord.
        obj_type (Union[Unset, int]): Sord type.
        prio (Union[Unset, int]): Priority: 0...high, 1...medium, 2...
            low
        receiver_id (Union[Unset, int]): Reminder was created for this user.
        sender_id (Union[Unset, int]): Reminder was created by this user.
        create_date_iso (Union[Unset, str]): Reminder was created at this date.
        deleted (Union[Unset, bool]): Reminder is deleted logically if set. Read-only.
        due_date_iso (Union[Unset, str]): On this date the receiver has seen the reminder.
        lock_name (Union[Unset, str]): Reminder is locked by this user.
        notify_on_delete (Union[Unset, bool]): Notify sender if receiver deletes the reminder.
        notify_on_view (Union[Unset, bool]): Notify sender if receiver views the reminder.
        obj_guid (Union[Unset, str]): Sord GUID.
        prompt_date_iso (Union[Unset, str]): At this Date the reminder should be made visible to the receiver.
        receiver_name (Union[Unset, str]): Reminder was created for this user.
        sender_name (Union[Unset, str]): Reminder was created by this user.
    """

    desc: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    obj_type: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    receiver_id: Union[Unset, int] = UNSET
    sender_id: Union[Unset, int] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    due_date_iso: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    notify_on_delete: Union[Unset, bool] = UNSET
    notify_on_view: Union[Unset, bool] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    prompt_date_iso: Union[Unset, str] = UNSET
    receiver_name: Union[Unset, str] = UNSET
    sender_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desc = self.desc
        id = self.id
        lock_id = self.lock_id
        name = self.name
        obj_id = self.obj_id
        obj_type = self.obj_type
        prio = self.prio
        receiver_id = self.receiver_id
        sender_id = self.sender_id
        create_date_iso = self.create_date_iso
        deleted = self.deleted
        due_date_iso = self.due_date_iso
        lock_name = self.lock_name
        notify_on_delete = self.notify_on_delete
        notify_on_view = self.notify_on_view
        obj_guid = self.obj_guid
        prompt_date_iso = self.prompt_date_iso
        receiver_name = self.receiver_name
        sender_name = self.sender_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict["desc"] = desc
        if id is not UNSET:
            field_dict["id"] = id
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if prio is not UNSET:
            field_dict["prio"] = prio
        if receiver_id is not UNSET:
            field_dict["receiverId"] = receiver_id
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if due_date_iso is not UNSET:
            field_dict["dueDateIso"] = due_date_iso
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if notify_on_delete is not UNSET:
            field_dict["notifyOnDelete"] = notify_on_delete
        if notify_on_view is not UNSET:
            field_dict["notifyOnView"] = notify_on_view
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if prompt_date_iso is not UNSET:
            field_dict["promptDateIso"] = prompt_date_iso
        if receiver_name is not UNSET:
            field_dict["receiverName"] = receiver_name
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desc = d.pop("desc", UNSET)

        id = d.pop("id", UNSET)

        lock_id = d.pop("lockId", UNSET)

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        obj_type = d.pop("objType", UNSET)

        prio = d.pop("prio", UNSET)

        receiver_id = d.pop("receiverId", UNSET)

        sender_id = d.pop("senderId", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        deleted = d.pop("deleted", UNSET)

        due_date_iso = d.pop("dueDateIso", UNSET)

        lock_name = d.pop("lockName", UNSET)

        notify_on_delete = d.pop("notifyOnDelete", UNSET)

        notify_on_view = d.pop("notifyOnView", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        prompt_date_iso = d.pop("promptDateIso", UNSET)

        receiver_name = d.pop("receiverName", UNSET)

        sender_name = d.pop("senderName", UNSET)

        reminder = cls(
            desc=desc,
            id=id,
            lock_id=lock_id,
            name=name,
            obj_id=obj_id,
            obj_type=obj_type,
            prio=prio,
            receiver_id=receiver_id,
            sender_id=sender_id,
            create_date_iso=create_date_iso,
            deleted=deleted,
            due_date_iso=due_date_iso,
            lock_name=lock_name,
            notify_on_delete=notify_on_delete,
            notify_on_view=notify_on_view,
            obj_guid=obj_guid,
            prompt_date_iso=prompt_date_iso,
            receiver_name=receiver_name,
            sender_name=sender_name,
        )

        reminder.additional_properties = d
        return reminder

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
