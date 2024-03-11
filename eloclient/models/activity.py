from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """This class represents an activity.
    <p>
     An activity is a task delegated to an instance outside the ELO system. It is created when the task is sent to the
     instance and deleted, if it is received back. An activity defines a date for expecting the response,
     <code>dueDateIso</code>. At this date, the activity appears in the task list of the initiator. If the task is
     finished, the initiator sets the <code>backAt</code> member and the activity is closed.
     </p>
     <p>
     Activities can be used to observe a document or a folder. For each modification, a ELO_NOTIFY activity is created
    and
     displayed in the task list of the user that wants to observe the object.
     </p>
     <p>
     An activity object is an instance on an activity project. The project defines the properties the user can edit or
     select to provide more information to the task.
     </p>

        Attributes:
            t_stamp (Union[Unset, str]): Date and time of the last update.
                Readonly
            back_at (Union[Unset, str]): Date when activity object was returned, ISO format. This value does not contain a
                time portion.
            back_mode (Union[Unset, str]): Application defined purpose.
            comment (Union[Unset, str]): Comment for the activity.
            destination (Union[Unset, str]): Application defined purpose.
            due_date_iso (Union[Unset, str]): Date when activity object is expected to be returned. This value does not
                contain a time portion.
            file_name (Union[Unset, str]): Application defined purpose.
            guid (Union[Unset, str]): GUID of the activity object.
            name (Union[Unset, str]): Short name/description of the activity object.
            obj_guid (Union[Unset, str]): GUID of the assigned archive entry.
            prio (Union[Unset, int]): Priority for the activity. Priority A has value 0, UserTaskPriorityC.HIGHEST Priority
                B has value 1.
                Priority C has
                 value 2, UserTaskPriorityC#LOWEST
            project (Union[Unset, str]): Project name for the activity.
            receiver_id (Union[Unset, int]): The ID of the recipient.
            rev_vers (Union[Unset, str]): Revision version of the activity object.
            sender_id (Union[Unset, int]): ID of the user who created the activity.
            sent_at_iso (Union[Unset, str]): Date the activity was sent in ISO format. This value does not contain a time
                portion.
            sent_mode (Union[Unset, str]): Application defined purpose.
            ud0 (Union[Unset, str]): First application defined value.
            ud1 (Union[Unset, str]): Second application defined value.
            ud2 (Union[Unset, str]): Third application defined value.
            ud3 (Union[Unset, str]): Fourth application defined value.
            ud4 (Union[Unset, str]): Fifth application defined value.
            ud5 (Union[Unset, str]): Sixth application defined value.
            ud6 (Union[Unset, str]): Seventh application defined value.
            ud7 (Union[Unset, str]): Eighth application defined value.
            ud8 (Union[Unset, str]): Ninth application defined value.
            ud9 (Union[Unset, str]): Tenth application defined value.
            receiver_name (Union[Unset, str]): Activity was created for this user. Readonly.
            sender_name (Union[Unset, str]): Activity was created by this user. Readonly.
            trans_id (Union[Unset, str]): Application defined value.
            obj_id (Union[Unset, int]): Object ID of the associated folder or document. Read-only.
            obj_type (Union[Unset, int]): Object type of the associated folder or document. Read-only.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
    """

    t_stamp: Union[Unset, str] = UNSET
    back_at: Union[Unset, str] = UNSET
    back_mode: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    due_date_iso: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    project: Union[Unset, str] = UNSET
    receiver_id: Union[Unset, int] = UNSET
    rev_vers: Union[Unset, str] = UNSET
    sender_id: Union[Unset, int] = UNSET
    sent_at_iso: Union[Unset, str] = UNSET
    sent_mode: Union[Unset, str] = UNSET
    ud0: Union[Unset, str] = UNSET
    ud1: Union[Unset, str] = UNSET
    ud2: Union[Unset, str] = UNSET
    ud3: Union[Unset, str] = UNSET
    ud4: Union[Unset, str] = UNSET
    ud5: Union[Unset, str] = UNSET
    ud6: Union[Unset, str] = UNSET
    ud7: Union[Unset, str] = UNSET
    ud8: Union[Unset, str] = UNSET
    ud9: Union[Unset, str] = UNSET
    receiver_name: Union[Unset, str] = UNSET
    sender_name: Union[Unset, str] = UNSET
    trans_id: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    obj_type: Union[Unset, int] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp
        back_at = self.back_at
        back_mode = self.back_mode
        comment = self.comment
        destination = self.destination
        due_date_iso = self.due_date_iso
        file_name = self.file_name
        guid = self.guid
        name = self.name
        obj_guid = self.obj_guid
        prio = self.prio
        project = self.project
        receiver_id = self.receiver_id
        rev_vers = self.rev_vers
        sender_id = self.sender_id
        sent_at_iso = self.sent_at_iso
        sent_mode = self.sent_mode
        ud0 = self.ud0
        ud1 = self.ud1
        ud2 = self.ud2
        ud3 = self.ud3
        ud4 = self.ud4
        ud5 = self.ud5
        ud6 = self.ud6
        ud7 = self.ud7
        ud8 = self.ud8
        ud9 = self.ud9
        receiver_name = self.receiver_name
        sender_name = self.sender_name
        trans_id = self.trans_id
        obj_id = self.obj_id
        obj_type = self.obj_type
        t_stamp_sync = self.t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if back_at is not UNSET:
            field_dict["backAt"] = back_at
        if back_mode is not UNSET:
            field_dict["backMode"] = back_mode
        if comment is not UNSET:
            field_dict["comment"] = comment
        if destination is not UNSET:
            field_dict["destination"] = destination
        if due_date_iso is not UNSET:
            field_dict["dueDateIso"] = due_date_iso
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if prio is not UNSET:
            field_dict["prio"] = prio
        if project is not UNSET:
            field_dict["project"] = project
        if receiver_id is not UNSET:
            field_dict["receiverId"] = receiver_id
        if rev_vers is not UNSET:
            field_dict["revVers"] = rev_vers
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if sent_at_iso is not UNSET:
            field_dict["sentAtIso"] = sent_at_iso
        if sent_mode is not UNSET:
            field_dict["sentMode"] = sent_mode
        if ud0 is not UNSET:
            field_dict["ud0"] = ud0
        if ud1 is not UNSET:
            field_dict["ud1"] = ud1
        if ud2 is not UNSET:
            field_dict["ud2"] = ud2
        if ud3 is not UNSET:
            field_dict["ud3"] = ud3
        if ud4 is not UNSET:
            field_dict["ud4"] = ud4
        if ud5 is not UNSET:
            field_dict["ud5"] = ud5
        if ud6 is not UNSET:
            field_dict["ud6"] = ud6
        if ud7 is not UNSET:
            field_dict["ud7"] = ud7
        if ud8 is not UNSET:
            field_dict["ud8"] = ud8
        if ud9 is not UNSET:
            field_dict["ud9"] = ud9
        if receiver_name is not UNSET:
            field_dict["receiverName"] = receiver_name
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if trans_id is not UNSET:
            field_dict["transId"] = trans_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t_stamp = d.pop("TStamp", UNSET)

        back_at = d.pop("backAt", UNSET)

        back_mode = d.pop("backMode", UNSET)

        comment = d.pop("comment", UNSET)

        destination = d.pop("destination", UNSET)

        due_date_iso = d.pop("dueDateIso", UNSET)

        file_name = d.pop("fileName", UNSET)

        guid = d.pop("guid", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        prio = d.pop("prio", UNSET)

        project = d.pop("project", UNSET)

        receiver_id = d.pop("receiverId", UNSET)

        rev_vers = d.pop("revVers", UNSET)

        sender_id = d.pop("senderId", UNSET)

        sent_at_iso = d.pop("sentAtIso", UNSET)

        sent_mode = d.pop("sentMode", UNSET)

        ud0 = d.pop("ud0", UNSET)

        ud1 = d.pop("ud1", UNSET)

        ud2 = d.pop("ud2", UNSET)

        ud3 = d.pop("ud3", UNSET)

        ud4 = d.pop("ud4", UNSET)

        ud5 = d.pop("ud5", UNSET)

        ud6 = d.pop("ud6", UNSET)

        ud7 = d.pop("ud7", UNSET)

        ud8 = d.pop("ud8", UNSET)

        ud9 = d.pop("ud9", UNSET)

        receiver_name = d.pop("receiverName", UNSET)

        sender_name = d.pop("senderName", UNSET)

        trans_id = d.pop("transId", UNSET)

        obj_id = d.pop("objId", UNSET)

        obj_type = d.pop("objType", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        activity = cls(
            t_stamp=t_stamp,
            back_at=back_at,
            back_mode=back_mode,
            comment=comment,
            destination=destination,
            due_date_iso=due_date_iso,
            file_name=file_name,
            guid=guid,
            name=name,
            obj_guid=obj_guid,
            prio=prio,
            project=project,
            receiver_id=receiver_id,
            rev_vers=rev_vers,
            sender_id=sender_id,
            sent_at_iso=sent_at_iso,
            sent_mode=sent_mode,
            ud0=ud0,
            ud1=ud1,
            ud2=ud2,
            ud3=ud3,
            ud4=ud4,
            ud5=ud5,
            ud6=ud6,
            ud7=ud7,
            ud8=ud8,
            ud9=ud9,
            receiver_name=receiver_name,
            sender_name=sender_name,
            trans_id=trans_id,
            obj_id=obj_id,
            obj_type=obj_type,
            t_stamp_sync=t_stamp_sync,
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
