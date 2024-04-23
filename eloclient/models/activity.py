from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """This class represents an activity.
    <p>
     An activity is a task delegated to an instance outside the ELO system. It is created when the
     task is sent to the instance and deleted, if it is received back. An activity defines a date for
     expecting the response, <code>dueDateIso</code>. At this date, the activity appears in the task
     list of the initiator. If the task is finished, the initiator sets the <code>backAt</code> member
     and the activity is closed.
     </p>
     <p>
     Activities can be used to observe a document or a folder. For each modification, a ELO_NOTIFY
     activity is created and displayed in the task list of the user that wants to observe the object.
     </p>
     <p>
     An activity object is an instance on an activity project. The project defines the properties the
     user can edit or select to provide more information to the task.
     </p>

        Attributes:
            ud0 (Union[Unset, str]): First application defined value.
            file_name (Union[Unset, str]): Application defined purpose.
            ud2 (Union[Unset, str]): Third application defined value.
            ud1 (Union[Unset, str]): Second application defined value.
            ud4 (Union[Unset, str]): Fifth application defined value.
            ud3 (Union[Unset, str]): Fourth application defined value.
            ud6 (Union[Unset, str]): Seventh application defined value.
            trans_id (Union[Unset, str]): Application defined value.
            ud5 (Union[Unset, str]): Sixth application defined value.
            destination (Union[Unset, str]): Application defined purpose.
            ud8 (Union[Unset, str]): Ninth application defined value.
            project (Union[Unset, str]): Project name for the activity.
            ud7 (Union[Unset, str]): Eighth application defined value.
            ud9 (Union[Unset, str]): Tenth application defined value.
            back_mode (Union[Unset, str]): Application defined purpose.
            t_stamp (Union[Unset, str]): Date and time of the last update.
                Readonly
            sender_id (Union[Unset, int]): ID of the user who created the activity.
            sender_name (Union[Unset, str]): Activity was created by this user. Readonly.
            receiver_id (Union[Unset, int]): The ID of the recipient.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            prio (Union[Unset, int]): Priority for the activity. Priority A has value 0, UserTaskPriorityC.
                HIGHEST Priority B has
                 value 1. Priority C has value 2, UserTaskPriorityC#LOWEST
            obj_type (Union[Unset, int]): Object type of the associated folder or document. Read-only.
            sent_mode (Union[Unset, str]): Application defined purpose.
            sent_at_iso (Union[Unset, str]): Date the activity was sent in ISO format. This value does not contain a time
                portion.
            obj_guid (Union[Unset, str]): GUID of the assigned archive entry.
            receiver_name (Union[Unset, str]): Activity was created for this user. Readonly.
            due_date_iso (Union[Unset, str]): Date when activity object is expected to be returned.
                This value does not contain a time
                 portion.
            rev_vers (Union[Unset, str]): Revision version of the activity object.
            name (Union[Unset, str]): Short name/description of the activity object.
            obj_id (Union[Unset, int]): Object ID of the associated folder or document. Read-only.
            guid (Union[Unset, str]): GUID of the activity object.
            back_at (Union[Unset, str]): Date when activity object was returned, ISO format. This value does not contain a
                time portion.
            comment (Union[Unset, str]): Comment for the activity.
    """

    ud0: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    ud2: Union[Unset, str] = UNSET
    ud1: Union[Unset, str] = UNSET
    ud4: Union[Unset, str] = UNSET
    ud3: Union[Unset, str] = UNSET
    ud6: Union[Unset, str] = UNSET
    trans_id: Union[Unset, str] = UNSET
    ud5: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    ud8: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    ud7: Union[Unset, str] = UNSET
    ud9: Union[Unset, str] = UNSET
    back_mode: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    sender_id: Union[Unset, int] = UNSET
    sender_name: Union[Unset, str] = UNSET
    receiver_id: Union[Unset, int] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    obj_type: Union[Unset, int] = UNSET
    sent_mode: Union[Unset, str] = UNSET
    sent_at_iso: Union[Unset, str] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    receiver_name: Union[Unset, str] = UNSET
    due_date_iso: Union[Unset, str] = UNSET
    rev_vers: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    back_at: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ud0 = self.ud0

        file_name = self.file_name

        ud2 = self.ud2

        ud1 = self.ud1

        ud4 = self.ud4

        ud3 = self.ud3

        ud6 = self.ud6

        trans_id = self.trans_id

        ud5 = self.ud5

        destination = self.destination

        ud8 = self.ud8

        project = self.project

        ud7 = self.ud7

        ud9 = self.ud9

        back_mode = self.back_mode

        t_stamp = self.t_stamp

        sender_id = self.sender_id

        sender_name = self.sender_name

        receiver_id = self.receiver_id

        t_stamp_sync = self.t_stamp_sync

        prio = self.prio

        obj_type = self.obj_type

        sent_mode = self.sent_mode

        sent_at_iso = self.sent_at_iso

        obj_guid = self.obj_guid

        receiver_name = self.receiver_name

        due_date_iso = self.due_date_iso

        rev_vers = self.rev_vers

        name = self.name

        obj_id = self.obj_id

        guid = self.guid

        back_at = self.back_at

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ud0 is not UNSET:
            field_dict["ud0"] = ud0
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if ud2 is not UNSET:
            field_dict["ud2"] = ud2
        if ud1 is not UNSET:
            field_dict["ud1"] = ud1
        if ud4 is not UNSET:
            field_dict["ud4"] = ud4
        if ud3 is not UNSET:
            field_dict["ud3"] = ud3
        if ud6 is not UNSET:
            field_dict["ud6"] = ud6
        if trans_id is not UNSET:
            field_dict["transId"] = trans_id
        if ud5 is not UNSET:
            field_dict["ud5"] = ud5
        if destination is not UNSET:
            field_dict["destination"] = destination
        if ud8 is not UNSET:
            field_dict["ud8"] = ud8
        if project is not UNSET:
            field_dict["project"] = project
        if ud7 is not UNSET:
            field_dict["ud7"] = ud7
        if ud9 is not UNSET:
            field_dict["ud9"] = ud9
        if back_mode is not UNSET:
            field_dict["backMode"] = back_mode
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if receiver_id is not UNSET:
            field_dict["receiverId"] = receiver_id
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if prio is not UNSET:
            field_dict["prio"] = prio
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if sent_mode is not UNSET:
            field_dict["sentMode"] = sent_mode
        if sent_at_iso is not UNSET:
            field_dict["sentAtIso"] = sent_at_iso
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if receiver_name is not UNSET:
            field_dict["receiverName"] = receiver_name
        if due_date_iso is not UNSET:
            field_dict["dueDateIso"] = due_date_iso
        if rev_vers is not UNSET:
            field_dict["revVers"] = rev_vers
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if back_at is not UNSET:
            field_dict["backAt"] = back_at
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ud0 = d.pop("ud0", UNSET)

        file_name = d.pop("fileName", UNSET)

        ud2 = d.pop("ud2", UNSET)

        ud1 = d.pop("ud1", UNSET)

        ud4 = d.pop("ud4", UNSET)

        ud3 = d.pop("ud3", UNSET)

        ud6 = d.pop("ud6", UNSET)

        trans_id = d.pop("transId", UNSET)

        ud5 = d.pop("ud5", UNSET)

        destination = d.pop("destination", UNSET)

        ud8 = d.pop("ud8", UNSET)

        project = d.pop("project", UNSET)

        ud7 = d.pop("ud7", UNSET)

        ud9 = d.pop("ud9", UNSET)

        back_mode = d.pop("backMode", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        sender_id = d.pop("senderId", UNSET)

        sender_name = d.pop("senderName", UNSET)

        receiver_id = d.pop("receiverId", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        prio = d.pop("prio", UNSET)

        obj_type = d.pop("objType", UNSET)

        sent_mode = d.pop("sentMode", UNSET)

        sent_at_iso = d.pop("sentAtIso", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        receiver_name = d.pop("receiverName", UNSET)

        due_date_iso = d.pop("dueDateIso", UNSET)

        rev_vers = d.pop("revVers", UNSET)

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        guid = d.pop("guid", UNSET)

        back_at = d.pop("backAt", UNSET)

        comment = d.pop("comment", UNSET)

        activity = cls(
            ud0=ud0,
            file_name=file_name,
            ud2=ud2,
            ud1=ud1,
            ud4=ud4,
            ud3=ud3,
            ud6=ud6,
            trans_id=trans_id,
            ud5=ud5,
            destination=destination,
            ud8=ud8,
            project=project,
            ud7=ud7,
            ud9=ud9,
            back_mode=back_mode,
            t_stamp=t_stamp,
            sender_id=sender_id,
            sender_name=sender_name,
            receiver_id=receiver_id,
            t_stamp_sync=t_stamp_sync,
            prio=prio,
            obj_type=obj_type,
            sent_mode=sent_mode,
            sent_at_iso=sent_at_iso,
            obj_guid=obj_guid,
            receiver_name=receiver_name,
            due_date_iso=due_date_iso,
            rev_vers=rev_vers,
            name=name,
            obj_id=obj_id,
            guid=guid,
            back_at=back_at,
            comment=comment,
        )

        activity.additional_properties = d
        return activity

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
