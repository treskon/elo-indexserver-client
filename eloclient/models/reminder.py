from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reminder")


@_attrs_define
class Reminder:
    """
    Attributes:
        obj_guid (Union[Unset, str]): Sord GUID.
        prompt_date_iso (Union[Unset, str]): At this Date the reminder should be made visible to the receiver.
        receiver_name (Union[Unset, str]): Reminder was created for this user.
        notify_on_delete (Union[Unset, bool]): Notify sender if receiver deletes the reminder.
        notify_on_view (Union[Unset, bool]): Notify sender if receiver views the reminder.
        due_date_iso (Union[Unset, str]): On this date the receiver has seen the reminder.
        lock_id (Union[Unset, int]): ID of user who has locked the reminder record in DB
        sender_id (Union[Unset, int]): Reminder was created by this user.
        sender_name (Union[Unset, str]): Reminder was created by this user.
        receiver_id (Union[Unset, int]): Reminder was created for this user.
        deleted (Union[Unset, bool]): Reminder is deleted logically if set. Read-only.
        create_date_iso (Union[Unset, str]): Reminder was created at this date.
        name (Union[Unset, str]): Short description visible in the task list.
        obj_id (Union[Unset, int]): Reminder is linked to this Sord.
        id (Union[Unset, int]): Reminder ID
        prio (Union[Unset, int]): Priority: 0...high, 1...medium, 2...
            low
        obj_type (Union[Unset, int]): Sord type.
        lock_name (Union[Unset, str]): Reminder is locked by this user.
        desc (Union[Unset, str]): Memo text
    """

    obj_guid: Union[Unset, str] = UNSET
    prompt_date_iso: Union[Unset, str] = UNSET
    receiver_name: Union[Unset, str] = UNSET
    notify_on_delete: Union[Unset, bool] = UNSET
    notify_on_view: Union[Unset, bool] = UNSET
    due_date_iso: Union[Unset, str] = UNSET
    lock_id: Union[Unset, int] = UNSET
    sender_id: Union[Unset, int] = UNSET
    sender_name: Union[Unset, str] = UNSET
    receiver_id: Union[Unset, int] = UNSET
    deleted: Union[Unset, bool] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    obj_type: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        obj_guid = self.obj_guid

        prompt_date_iso = self.prompt_date_iso

        receiver_name = self.receiver_name

        notify_on_delete = self.notify_on_delete

        notify_on_view = self.notify_on_view

        due_date_iso = self.due_date_iso

        lock_id = self.lock_id

        sender_id = self.sender_id

        sender_name = self.sender_name

        receiver_id = self.receiver_id

        deleted = self.deleted

        create_date_iso = self.create_date_iso

        name = self.name

        obj_id = self.obj_id

        id = self.id

        prio = self.prio

        obj_type = self.obj_type

        lock_name = self.lock_name

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if prompt_date_iso is not UNSET:
            field_dict["promptDateIso"] = prompt_date_iso
        if receiver_name is not UNSET:
            field_dict["receiverName"] = receiver_name
        if notify_on_delete is not UNSET:
            field_dict["notifyOnDelete"] = notify_on_delete
        if notify_on_view is not UNSET:
            field_dict["notifyOnView"] = notify_on_view
        if due_date_iso is not UNSET:
            field_dict["dueDateIso"] = due_date_iso
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if receiver_id is not UNSET:
            field_dict["receiverId"] = receiver_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if id is not UNSET:
            field_dict["id"] = id
        if prio is not UNSET:
            field_dict["prio"] = prio
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        obj_guid = d.pop("objGuid", UNSET)

        prompt_date_iso = d.pop("promptDateIso", UNSET)

        receiver_name = d.pop("receiverName", UNSET)

        notify_on_delete = d.pop("notifyOnDelete", UNSET)

        notify_on_view = d.pop("notifyOnView", UNSET)

        due_date_iso = d.pop("dueDateIso", UNSET)

        lock_id = d.pop("lockId", UNSET)

        sender_id = d.pop("senderId", UNSET)

        sender_name = d.pop("senderName", UNSET)

        receiver_id = d.pop("receiverId", UNSET)

        deleted = d.pop("deleted", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        id = d.pop("id", UNSET)

        prio = d.pop("prio", UNSET)

        obj_type = d.pop("objType", UNSET)

        lock_name = d.pop("lockName", UNSET)

        desc = d.pop("desc", UNSET)

        reminder = cls(
            obj_guid=obj_guid,
            prompt_date_iso=prompt_date_iso,
            receiver_name=receiver_name,
            notify_on_delete=notify_on_delete,
            notify_on_view=notify_on_view,
            due_date_iso=due_date_iso,
            lock_id=lock_id,
            sender_id=sender_id,
            sender_name=sender_name,
            receiver_id=receiver_id,
            deleted=deleted,
            create_date_iso=create_date_iso,
            name=name,
            obj_id=obj_id,
            id=id,
            prio=prio,
            obj_type=obj_type,
            lock_name=lock_name,
            desc=desc,
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
