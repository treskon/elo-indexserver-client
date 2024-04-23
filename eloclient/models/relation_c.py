from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationC")


@_attrs_define
class RelationC:
    """<p>Bit constants for members of Relation</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_ordinal (Union[Unset, str]): DB column: ordinal
            mb_t_stamp (Union[Unset, str]): DB column: reltstamp
            mb_parent_id (Union[Unset, str]): DB column: parentid
            mb_delete_date (Union[Unset, str]): Member bit: The Relation is deleted at this date. ClientInfo determines the
                Timezone.
                DB column: reldeletedate
            ln_guid (Union[Unset, int]): Column length: GUID
                DB column: relguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: reltstampsync
            mb_status (Union[Unset, str]): DB column: relstatus
            mb_obj_id (Union[Unset, str]): DB column: objectid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_rel_main (Union[Unset, str]): Member bit: This Relation represents the main relation of an object, if this
                value is <code>true</code>.
                DB column: relmain
            mb_guid (Union[Unset, str]): Member bit: GUID
                DB column: relguid
            ln_t_stamp (Union[Unset, int]): DB column: reltstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: reltstampsync
    """

    mb_ordinal: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_parent_id: Union[Unset, str] = UNSET
    mb_delete_date: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_rel_main: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_ordinal = self.mb_ordinal

        mb_t_stamp = self.mb_t_stamp

        mb_parent_id = self.mb_parent_id

        mb_delete_date = self.mb_delete_date

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_status = self.mb_status

        mb_obj_id = self.mb_obj_id

        mb_all_members = self.mb_all_members

        mb_rel_main = self.mb_rel_main

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_ordinal is not UNSET:
            field_dict["mbOrdinal"] = mb_ordinal
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_parent_id is not UNSET:
            field_dict["mbParentId"] = mb_parent_id
        if mb_delete_date is not UNSET:
            field_dict["mbDeleteDate"] = mb_delete_date
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_rel_main is not UNSET:
            field_dict["mbRelMain"] = mb_rel_main
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_ordinal = d.pop("mbOrdinal", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_parent_id = d.pop("mbParentId", UNSET)

        mb_delete_date = d.pop("mbDeleteDate", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_rel_main = d.pop("mbRelMain", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        relation_c = cls(
            mb_ordinal=mb_ordinal,
            mb_t_stamp=mb_t_stamp,
            mb_parent_id=mb_parent_id,
            mb_delete_date=mb_delete_date,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_status=mb_status,
            mb_obj_id=mb_obj_id,
            mb_all_members=mb_all_members,
            mb_rel_main=mb_rel_main,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
        )

        relation_c.additional_properties = d
        return relation_c

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
