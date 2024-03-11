from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteDataC")


@_attrs_define
class NoteDataC:
    """<p>
    Bit constants for members of Note
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: noteid
            mb_parent_id (Union[Unset, str]): DB column: parentid
            mb_page_no (Union[Unset, str]): DB column: pageno
            mb_x_pos (Union[Unset, str]): DB column: xpos
            mb_y_pos (Union[Unset, str]): DB column: ypos
            mb_owner_id (Union[Unset, str]): DB column: userid
            mb_type (Union[Unset, str]): DB column: notetype
            mb_h_lock (Union[Unset, str]): DB column: hlock
            mb_create_date (Union[Unset, str]): DB column: createdate
            mb_desc (Union[Unset, str]): DB column: pidesc
            ln_desc (Union[Unset, int]): DB column: pidesc
            mb_guid (Union[Unset, str]): DB column: noteguid
            ln_guid (Union[Unset, int]): DB column: noteguid
            mb_t_stamp (Union[Unset, str]): DB column: notetstamp
            ln_t_stamp (Union[Unset, int]): DB column: notetstamp
            mb_status (Union[Unset, str]): DB column: notestatus
            mb_width (Union[Unset, str]): DB column: width
            mb_height (Union[Unset, str]): DB column: height
            mb_acl (Union[Unset, str]): DB column: noteacl
            ln_acl (Union[Unset, int]): DB column: noteacl
            mb_color (Union[Unset, str]): DB column: color
            mb_delete_date (Union[Unset, str]): Member bit: The Note is deleted at this date. ClientInfo determines the
                Timezone.
                DB column: deletedate
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: notetstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: notetstampsync
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_id: Union[Unset, str] = UNSET
    mb_parent_id: Union[Unset, str] = UNSET
    mb_page_no: Union[Unset, str] = UNSET
    mb_x_pos: Union[Unset, str] = UNSET
    mb_y_pos: Union[Unset, str] = UNSET
    mb_owner_id: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_h_lock: Union[Unset, str] = UNSET
    mb_create_date: Union[Unset, str] = UNSET
    mb_desc: Union[Unset, str] = UNSET
    ln_desc: Union[Unset, int] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_width: Union[Unset, str] = UNSET
    mb_height: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_color: Union[Unset, str] = UNSET
    mb_delete_date: Union[Unset, str] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id
        mb_parent_id = self.mb_parent_id
        mb_page_no = self.mb_page_no
        mb_x_pos = self.mb_x_pos
        mb_y_pos = self.mb_y_pos
        mb_owner_id = self.mb_owner_id
        mb_type = self.mb_type
        mb_h_lock = self.mb_h_lock
        mb_create_date = self.mb_create_date
        mb_desc = self.mb_desc
        ln_desc = self.ln_desc
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_status = self.mb_status
        mb_width = self.mb_width
        mb_height = self.mb_height
        mb_acl = self.mb_acl
        ln_acl = self.ln_acl
        mb_color = self.mb_color
        mb_delete_date = self.mb_delete_date
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_parent_id is not UNSET:
            field_dict["mbParentId"] = mb_parent_id
        if mb_page_no is not UNSET:
            field_dict["mbPageNo"] = mb_page_no
        if mb_x_pos is not UNSET:
            field_dict["mbXPos"] = mb_x_pos
        if mb_y_pos is not UNSET:
            field_dict["mbYPos"] = mb_y_pos
        if mb_owner_id is not UNSET:
            field_dict["mbOwnerId"] = mb_owner_id
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_h_lock is not UNSET:
            field_dict["mbHLock"] = mb_h_lock
        if mb_create_date is not UNSET:
            field_dict["mbCreateDate"] = mb_create_date
        if mb_desc is not UNSET:
            field_dict["mbDesc"] = mb_desc
        if ln_desc is not UNSET:
            field_dict["lnDesc"] = ln_desc
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_width is not UNSET:
            field_dict["mbWidth"] = mb_width
        if mb_height is not UNSET:
            field_dict["mbHeight"] = mb_height
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_color is not UNSET:
            field_dict["mbColor"] = mb_color
        if mb_delete_date is not UNSET:
            field_dict["mbDeleteDate"] = mb_delete_date
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_parent_id = d.pop("mbParentId", UNSET)

        mb_page_no = d.pop("mbPageNo", UNSET)

        mb_x_pos = d.pop("mbXPos", UNSET)

        mb_y_pos = d.pop("mbYPos", UNSET)

        mb_owner_id = d.pop("mbOwnerId", UNSET)

        mb_type = d.pop("mbType", UNSET)

        mb_h_lock = d.pop("mbHLock", UNSET)

        mb_create_date = d.pop("mbCreateDate", UNSET)

        mb_desc = d.pop("mbDesc", UNSET)

        ln_desc = d.pop("lnDesc", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_width = d.pop("mbWidth", UNSET)

        mb_height = d.pop("mbHeight", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_color = d.pop("mbColor", UNSET)

        mb_delete_date = d.pop("mbDeleteDate", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        note_data_c = cls(
            mb_id=mb_id,
            mb_parent_id=mb_parent_id,
            mb_page_no=mb_page_no,
            mb_x_pos=mb_x_pos,
            mb_y_pos=mb_y_pos,
            mb_owner_id=mb_owner_id,
            mb_type=mb_type,
            mb_h_lock=mb_h_lock,
            mb_create_date=mb_create_date,
            mb_desc=mb_desc,
            ln_desc=ln_desc,
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_status=mb_status,
            mb_width=mb_width,
            mb_height=mb_height,
            mb_acl=mb_acl,
            ln_acl=ln_acl,
            mb_color=mb_color,
            mb_delete_date=mb_delete_date,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_all_members=mb_all_members,
        )

        note_data_c.additional_properties = d
        return note_data_c

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
