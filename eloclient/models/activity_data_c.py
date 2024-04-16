from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityDataC")


@_attrs_define
class ActivityDataC:
    """<p>Bit constants for members of Activity</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_ud_1 (Union[Unset, str]): DB column: ud1
            ln_ud_6 (Union[Unset, int]): DB column: ud6
            mb_ud_0 (Union[Unset, str]): DB column: ud0
            ln_ud_5 (Union[Unset, int]): DB column: ud5
            ln_sent_at_iso (Union[Unset, int]): DB column: sentat
            mb_ud_3 (Union[Unset, str]): DB column: ud3
            ln_ud_8 (Union[Unset, int]): DB column: ud8
            ln_comment (Union[Unset, int]): DB column: actcomment
            mb_ud_2 (Union[Unset, str]): DB column: ud2
            ln_ud_7 (Union[Unset, int]): DB column: ud7
            ln_ud_2 (Union[Unset, int]): DB column: ud2
            mb_t_stamp (Union[Unset, str]): DB column: acttstamp
            ln_ud_1 (Union[Unset, int]): DB column: ud1
            ln_ud_4 (Union[Unset, int]): DB column: ud4
            ln_ud_3 (Union[Unset, int]): DB column: ud3
            mb_rev_vers (Union[Unset, str]): DB column: revvers
            ln_sent_mode (Union[Unset, int]): DB column: sentmode
            ln_back_at (Union[Unset, int]): DB column: backat
            ln_ud_9 (Union[Unset, int]): DB column: ud9
            ln_due_date_iso (Union[Unset, int]): DB column: duedate
            mb_obj_id (Union[Unset, str]): Member bit: Object ID of the associated folder or document. Read-only.
                DB column: objid
            mb_ud_9 (Union[Unset, str]): DB column: ud9
            mb_ud_8 (Union[Unset, str]): DB column: ud8
            mb_sent_mode (Union[Unset, str]): DB column: sentmode
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: acttstampsync
            mb_ud_5 (Union[Unset, str]): DB column: ud5
            mb_ud_4 (Union[Unset, str]): DB column: ud4
            mb_ud_7 (Union[Unset, str]): DB column: ud7
            mb_ud_6 (Union[Unset, str]): DB column: ud6
            mb_receiver_id (Union[Unset, str]): DB column: owner
            mb_sent_at_iso (Union[Unset, str]): DB column: sentat
            ln_file_name (Union[Unset, int]): DB column: filename
            mb_file_name (Union[Unset, str]): DB column: filename
            mb_guid (Union[Unset, str]): DB column: actguid
            ln_ud_0 (Union[Unset, int]): DB column: ud0
            mb_comment (Union[Unset, str]): DB column: actcomment
            ln_trans_id (Union[Unset, int]): Column length: Application defined value.
                DB column: transmitid
            mb_destination (Union[Unset, str]): DB column: destination
            mb_back_at (Union[Unset, str]): DB column: backat
            mb_name (Union[Unset, str]): DB column: shortdesc
            ln_guid (Union[Unset, int]): DB column: actguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: acttstampsync
            mb_sender_id (Union[Unset, str]): DB column: creator
            ln_name (Union[Unset, int]): DB column: shortdesc
            mb_prio (Union[Unset, str]): DB column: prio
            mb_due_date_iso (Union[Unset, str]): DB column: duedate
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_t_stamp (Union[Unset, int]): DB column: acttstamp
            mb_project (Union[Unset, str]): DB column: project
            mb_obj_guid (Union[Unset, str]): DB column: docguid
            ln_project (Union[Unset, int]): DB column: project
            ln_obj_guid (Union[Unset, int]): DB column: docguid
            mb_back_mode (Union[Unset, str]): DB column: backmode
            ln_destination (Union[Unset, int]): DB column: destination
            mb_obj_type (Union[Unset, str]): Member bit: Object type of the associated folder or document. Read-only.
                DB column: objtype
            ln_back_mode (Union[Unset, int]): DB column: backmode
            ln_rev_vers (Union[Unset, int]): DB column: revvers
            mb_trans_id (Union[Unset, str]): Member bit: Application defined value.
                DB column: transmitid
    """

    mb_ud_1: Union[Unset, str] = UNSET
    ln_ud_6: Union[Unset, int] = UNSET
    mb_ud_0: Union[Unset, str] = UNSET
    ln_ud_5: Union[Unset, int] = UNSET
    ln_sent_at_iso: Union[Unset, int] = UNSET
    mb_ud_3: Union[Unset, str] = UNSET
    ln_ud_8: Union[Unset, int] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    mb_ud_2: Union[Unset, str] = UNSET
    ln_ud_7: Union[Unset, int] = UNSET
    ln_ud_2: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_ud_1: Union[Unset, int] = UNSET
    ln_ud_4: Union[Unset, int] = UNSET
    ln_ud_3: Union[Unset, int] = UNSET
    mb_rev_vers: Union[Unset, str] = UNSET
    ln_sent_mode: Union[Unset, int] = UNSET
    ln_back_at: Union[Unset, int] = UNSET
    ln_ud_9: Union[Unset, int] = UNSET
    ln_due_date_iso: Union[Unset, int] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_ud_9: Union[Unset, str] = UNSET
    mb_ud_8: Union[Unset, str] = UNSET
    mb_sent_mode: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_ud_5: Union[Unset, str] = UNSET
    mb_ud_4: Union[Unset, str] = UNSET
    mb_ud_7: Union[Unset, str] = UNSET
    mb_ud_6: Union[Unset, str] = UNSET
    mb_receiver_id: Union[Unset, str] = UNSET
    mb_sent_at_iso: Union[Unset, str] = UNSET
    ln_file_name: Union[Unset, int] = UNSET
    mb_file_name: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_ud_0: Union[Unset, int] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    ln_trans_id: Union[Unset, int] = UNSET
    mb_destination: Union[Unset, str] = UNSET
    mb_back_at: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_sender_id: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_due_date_iso: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_project: Union[Unset, str] = UNSET
    mb_obj_guid: Union[Unset, str] = UNSET
    ln_project: Union[Unset, int] = UNSET
    ln_obj_guid: Union[Unset, int] = UNSET
    mb_back_mode: Union[Unset, str] = UNSET
    ln_destination: Union[Unset, int] = UNSET
    mb_obj_type: Union[Unset, str] = UNSET
    ln_back_mode: Union[Unset, int] = UNSET
    ln_rev_vers: Union[Unset, int] = UNSET
    mb_trans_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_ud_1 = self.mb_ud_1

        ln_ud_6 = self.ln_ud_6

        mb_ud_0 = self.mb_ud_0

        ln_ud_5 = self.ln_ud_5

        ln_sent_at_iso = self.ln_sent_at_iso

        mb_ud_3 = self.mb_ud_3

        ln_ud_8 = self.ln_ud_8

        ln_comment = self.ln_comment

        mb_ud_2 = self.mb_ud_2

        ln_ud_7 = self.ln_ud_7

        ln_ud_2 = self.ln_ud_2

        mb_t_stamp = self.mb_t_stamp

        ln_ud_1 = self.ln_ud_1

        ln_ud_4 = self.ln_ud_4

        ln_ud_3 = self.ln_ud_3

        mb_rev_vers = self.mb_rev_vers

        ln_sent_mode = self.ln_sent_mode

        ln_back_at = self.ln_back_at

        ln_ud_9 = self.ln_ud_9

        ln_due_date_iso = self.ln_due_date_iso

        mb_obj_id = self.mb_obj_id

        mb_ud_9 = self.mb_ud_9

        mb_ud_8 = self.mb_ud_8

        mb_sent_mode = self.mb_sent_mode

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_ud_5 = self.mb_ud_5

        mb_ud_4 = self.mb_ud_4

        mb_ud_7 = self.mb_ud_7

        mb_ud_6 = self.mb_ud_6

        mb_receiver_id = self.mb_receiver_id

        mb_sent_at_iso = self.mb_sent_at_iso

        ln_file_name = self.ln_file_name

        mb_file_name = self.mb_file_name

        mb_guid = self.mb_guid

        ln_ud_0 = self.ln_ud_0

        mb_comment = self.mb_comment

        ln_trans_id = self.ln_trans_id

        mb_destination = self.mb_destination

        mb_back_at = self.mb_back_at

        mb_name = self.mb_name

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_sender_id = self.mb_sender_id

        ln_name = self.ln_name

        mb_prio = self.mb_prio

        mb_due_date_iso = self.mb_due_date_iso

        mb_all_members = self.mb_all_members

        ln_t_stamp = self.ln_t_stamp

        mb_project = self.mb_project

        mb_obj_guid = self.mb_obj_guid

        ln_project = self.ln_project

        ln_obj_guid = self.ln_obj_guid

        mb_back_mode = self.mb_back_mode

        ln_destination = self.ln_destination

        mb_obj_type = self.mb_obj_type

        ln_back_mode = self.ln_back_mode

        ln_rev_vers = self.ln_rev_vers

        mb_trans_id = self.mb_trans_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_ud_1 is not UNSET:
            field_dict["mbUd1"] = mb_ud_1
        if ln_ud_6 is not UNSET:
            field_dict["lnUd6"] = ln_ud_6
        if mb_ud_0 is not UNSET:
            field_dict["mbUd0"] = mb_ud_0
        if ln_ud_5 is not UNSET:
            field_dict["lnUd5"] = ln_ud_5
        if ln_sent_at_iso is not UNSET:
            field_dict["lnSentAtIso"] = ln_sent_at_iso
        if mb_ud_3 is not UNSET:
            field_dict["mbUd3"] = mb_ud_3
        if ln_ud_8 is not UNSET:
            field_dict["lnUd8"] = ln_ud_8
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if mb_ud_2 is not UNSET:
            field_dict["mbUd2"] = mb_ud_2
        if ln_ud_7 is not UNSET:
            field_dict["lnUd7"] = ln_ud_7
        if ln_ud_2 is not UNSET:
            field_dict["lnUd2"] = ln_ud_2
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_ud_1 is not UNSET:
            field_dict["lnUd1"] = ln_ud_1
        if ln_ud_4 is not UNSET:
            field_dict["lnUd4"] = ln_ud_4
        if ln_ud_3 is not UNSET:
            field_dict["lnUd3"] = ln_ud_3
        if mb_rev_vers is not UNSET:
            field_dict["mbRevVers"] = mb_rev_vers
        if ln_sent_mode is not UNSET:
            field_dict["lnSentMode"] = ln_sent_mode
        if ln_back_at is not UNSET:
            field_dict["lnBackAt"] = ln_back_at
        if ln_ud_9 is not UNSET:
            field_dict["lnUd9"] = ln_ud_9
        if ln_due_date_iso is not UNSET:
            field_dict["lnDueDateIso"] = ln_due_date_iso
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_ud_9 is not UNSET:
            field_dict["mbUd9"] = mb_ud_9
        if mb_ud_8 is not UNSET:
            field_dict["mbUd8"] = mb_ud_8
        if mb_sent_mode is not UNSET:
            field_dict["mbSentMode"] = mb_sent_mode
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_ud_5 is not UNSET:
            field_dict["mbUd5"] = mb_ud_5
        if mb_ud_4 is not UNSET:
            field_dict["mbUd4"] = mb_ud_4
        if mb_ud_7 is not UNSET:
            field_dict["mbUd7"] = mb_ud_7
        if mb_ud_6 is not UNSET:
            field_dict["mbUd6"] = mb_ud_6
        if mb_receiver_id is not UNSET:
            field_dict["mbReceiverId"] = mb_receiver_id
        if mb_sent_at_iso is not UNSET:
            field_dict["mbSentAtIso"] = mb_sent_at_iso
        if ln_file_name is not UNSET:
            field_dict["lnFileName"] = ln_file_name
        if mb_file_name is not UNSET:
            field_dict["mbFileName"] = mb_file_name
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_ud_0 is not UNSET:
            field_dict["lnUd0"] = ln_ud_0
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment
        if ln_trans_id is not UNSET:
            field_dict["lnTransId"] = ln_trans_id
        if mb_destination is not UNSET:
            field_dict["mbDestination"] = mb_destination
        if mb_back_at is not UNSET:
            field_dict["mbBackAt"] = mb_back_at
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_sender_id is not UNSET:
            field_dict["mbSenderId"] = mb_sender_id
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_due_date_iso is not UNSET:
            field_dict["mbDueDateIso"] = mb_due_date_iso
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_project is not UNSET:
            field_dict["mbProject"] = mb_project
        if mb_obj_guid is not UNSET:
            field_dict["mbObjGuid"] = mb_obj_guid
        if ln_project is not UNSET:
            field_dict["lnProject"] = ln_project
        if ln_obj_guid is not UNSET:
            field_dict["lnObjGuid"] = ln_obj_guid
        if mb_back_mode is not UNSET:
            field_dict["mbBackMode"] = mb_back_mode
        if ln_destination is not UNSET:
            field_dict["lnDestination"] = ln_destination
        if mb_obj_type is not UNSET:
            field_dict["mbObjType"] = mb_obj_type
        if ln_back_mode is not UNSET:
            field_dict["lnBackMode"] = ln_back_mode
        if ln_rev_vers is not UNSET:
            field_dict["lnRevVers"] = ln_rev_vers
        if mb_trans_id is not UNSET:
            field_dict["mbTransId"] = mb_trans_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_ud_1 = d.pop("mbUd1", UNSET)

        ln_ud_6 = d.pop("lnUd6", UNSET)

        mb_ud_0 = d.pop("mbUd0", UNSET)

        ln_ud_5 = d.pop("lnUd5", UNSET)

        ln_sent_at_iso = d.pop("lnSentAtIso", UNSET)

        mb_ud_3 = d.pop("mbUd3", UNSET)

        ln_ud_8 = d.pop("lnUd8", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        mb_ud_2 = d.pop("mbUd2", UNSET)

        ln_ud_7 = d.pop("lnUd7", UNSET)

        ln_ud_2 = d.pop("lnUd2", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_ud_1 = d.pop("lnUd1", UNSET)

        ln_ud_4 = d.pop("lnUd4", UNSET)

        ln_ud_3 = d.pop("lnUd3", UNSET)

        mb_rev_vers = d.pop("mbRevVers", UNSET)

        ln_sent_mode = d.pop("lnSentMode", UNSET)

        ln_back_at = d.pop("lnBackAt", UNSET)

        ln_ud_9 = d.pop("lnUd9", UNSET)

        ln_due_date_iso = d.pop("lnDueDateIso", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_ud_9 = d.pop("mbUd9", UNSET)

        mb_ud_8 = d.pop("mbUd8", UNSET)

        mb_sent_mode = d.pop("mbSentMode", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_ud_5 = d.pop("mbUd5", UNSET)

        mb_ud_4 = d.pop("mbUd4", UNSET)

        mb_ud_7 = d.pop("mbUd7", UNSET)

        mb_ud_6 = d.pop("mbUd6", UNSET)

        mb_receiver_id = d.pop("mbReceiverId", UNSET)

        mb_sent_at_iso = d.pop("mbSentAtIso", UNSET)

        ln_file_name = d.pop("lnFileName", UNSET)

        mb_file_name = d.pop("mbFileName", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_ud_0 = d.pop("lnUd0", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        ln_trans_id = d.pop("lnTransId", UNSET)

        mb_destination = d.pop("mbDestination", UNSET)

        mb_back_at = d.pop("mbBackAt", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_sender_id = d.pop("mbSenderId", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_due_date_iso = d.pop("mbDueDateIso", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_project = d.pop("mbProject", UNSET)

        mb_obj_guid = d.pop("mbObjGuid", UNSET)

        ln_project = d.pop("lnProject", UNSET)

        ln_obj_guid = d.pop("lnObjGuid", UNSET)

        mb_back_mode = d.pop("mbBackMode", UNSET)

        ln_destination = d.pop("lnDestination", UNSET)

        mb_obj_type = d.pop("mbObjType", UNSET)

        ln_back_mode = d.pop("lnBackMode", UNSET)

        ln_rev_vers = d.pop("lnRevVers", UNSET)

        mb_trans_id = d.pop("mbTransId", UNSET)

        activity_data_c = cls(
            mb_ud_1=mb_ud_1,
            ln_ud_6=ln_ud_6,
            mb_ud_0=mb_ud_0,
            ln_ud_5=ln_ud_5,
            ln_sent_at_iso=ln_sent_at_iso,
            mb_ud_3=mb_ud_3,
            ln_ud_8=ln_ud_8,
            ln_comment=ln_comment,
            mb_ud_2=mb_ud_2,
            ln_ud_7=ln_ud_7,
            ln_ud_2=ln_ud_2,
            mb_t_stamp=mb_t_stamp,
            ln_ud_1=ln_ud_1,
            ln_ud_4=ln_ud_4,
            ln_ud_3=ln_ud_3,
            mb_rev_vers=mb_rev_vers,
            ln_sent_mode=ln_sent_mode,
            ln_back_at=ln_back_at,
            ln_ud_9=ln_ud_9,
            ln_due_date_iso=ln_due_date_iso,
            mb_obj_id=mb_obj_id,
            mb_ud_9=mb_ud_9,
            mb_ud_8=mb_ud_8,
            mb_sent_mode=mb_sent_mode,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_ud_5=mb_ud_5,
            mb_ud_4=mb_ud_4,
            mb_ud_7=mb_ud_7,
            mb_ud_6=mb_ud_6,
            mb_receiver_id=mb_receiver_id,
            mb_sent_at_iso=mb_sent_at_iso,
            ln_file_name=ln_file_name,
            mb_file_name=mb_file_name,
            mb_guid=mb_guid,
            ln_ud_0=ln_ud_0,
            mb_comment=mb_comment,
            ln_trans_id=ln_trans_id,
            mb_destination=mb_destination,
            mb_back_at=mb_back_at,
            mb_name=mb_name,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_sender_id=mb_sender_id,
            ln_name=ln_name,
            mb_prio=mb_prio,
            mb_due_date_iso=mb_due_date_iso,
            mb_all_members=mb_all_members,
            ln_t_stamp=ln_t_stamp,
            mb_project=mb_project,
            mb_obj_guid=mb_obj_guid,
            ln_project=ln_project,
            ln_obj_guid=ln_obj_guid,
            mb_back_mode=mb_back_mode,
            ln_destination=ln_destination,
            mb_obj_type=mb_obj_type,
            ln_back_mode=ln_back_mode,
            ln_rev_vers=ln_rev_vers,
            mb_trans_id=mb_trans_id,
        )

        activity_data_c.additional_properties = d
        return activity_data_c

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
