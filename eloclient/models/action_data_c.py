from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionDataC")


@_attrs_define
class ActionDataC:
    """<p>Bit constants for members of Action</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_user_guid (Union[Unset, str]): Member bit: User GUID. The GUID of the user who has created this action.
                For actions of type
                 DB column: userguid
            ln_user_guid (Union[Unset, int]): Column length: User GUID. The GUID of the user who has created this action.
                For actions of type
                 DB column: userguid
            mb_t_stamp (Union[Unset, str]): Member bit: Time stamp. Time stamp of creation or modification.
                DB column: actiontstamp
            ln_acl (Union[Unset, int]): Column length: Raw ACL representation.
                Only valid for Actions of type {@link EActionType#UserComment} or
                 DB column: actionacl
            ln_text (Union[Unset, int]): Column length: Comment text.
                This element is only valid for {@link EActionType#UserComment}, and
                 DB column: actiontext
            ln_guid (Union[Unset, int]): Column length: Action GUID. Unique identifier.
                DB column: actionguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: actiontstampsync
            ln_create_date_iso (Union[Unset, int]): Column length: Create date. This element is the ISO formatted create
                date of the action.
                When this object is
                 DB column: createdateiso
            ln_update_date_iso (Union[Unset, int]): Column length: Update date. This element is only valid for {@link
                EActionType#UserComment}.
                It holds the ISO
                 DB column: updatedateiso
            mb_update_date_iso (Union[Unset, str]): Member bit: Update date. This element is only valid for {@link
                EActionType#UserComment}.
                It holds the ISO
                 DB column: updatedateiso
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_parent_guid (Union[Unset, int]): Column length: Parent action GUID.
                This element is only valid for user comments,
                 DB column: parentguid
            mb_acl (Union[Unset, str]): Member bit: Raw ACL representation.
                Only valid for Actions of type {@link EActionType#UserComment} or
                 DB column: actionacl
            ln_t_stamp (Union[Unset, int]): Column length: Time stamp. Time stamp of creation or modification.
                DB column: actiontstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: actiontstampsync
            mb_doc_version_guid (Union[Unset, str]): Member bit: GUID of the associated document version.
                This element is only valid for generated actions that
                 DB column: docversionguid
            mb_create_date_iso (Union[Unset, str]): Member bit: Create date. This element is the ISO formatted create date
                of the action.
                When this object is
                 DB column: createdateiso
            mb_feed_guid (Union[Unset, str]): Member bit: Feed GUID. This action belongs to the feed identified by this
                GUID.
                DB column: feedguid
            ln_workflow_guid (Union[Unset, int]): Column length: GUID of the associated workflow.
                This element is valid for action types that belong to a
                 DB column: workflowguid
            ln_feed_guid (Union[Unset, int]): Column length: Feed GUID. This action belongs to the feed identified by this
                GUID.
                DB column: feedguid
            mb_parent_guid (Union[Unset, str]): Member bit: Parent action GUID.
                This element is only valid for user comments,
                 DB column: parentguid
            mb_text (Union[Unset, str]): Member bit: Comment text.
                This element is only valid for {@link EActionType#UserComment}, and
                 DB column: actiontext
            mb_guid (Union[Unset, str]): Member bit: Action GUID. Unique identifier.
                DB column: actionguid
            mb_change_counter (Union[Unset, str]): Member bit: Counts the number of updates. This element is only valid for
                {@link EActionType#UserComment}.
                DB column: changecounter
            mb_raw_type (Union[Unset, str]): Member bit: Action type.
                DB column: actiontype
            mb_workflow_guid (Union[Unset, str]): Member bit: GUID of the associated workflow.
                This element is valid for action types that belong to a
                 DB column: workflowguid
            ln_doc_version_guid (Union[Unset, int]): Column length: GUID of the associated document version.
                This element is only valid for generated actions that
                 DB column: docversionguid
    """

    mb_user_guid: Union[Unset, str] = UNSET
    ln_user_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    ln_text: Union[Unset, int] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    ln_update_date_iso: Union[Unset, int] = UNSET
    mb_update_date_iso: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_parent_guid: Union[Unset, int] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_doc_version_guid: Union[Unset, str] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    mb_feed_guid: Union[Unset, str] = UNSET
    ln_workflow_guid: Union[Unset, int] = UNSET
    ln_feed_guid: Union[Unset, int] = UNSET
    mb_parent_guid: Union[Unset, str] = UNSET
    mb_text: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    mb_change_counter: Union[Unset, str] = UNSET
    mb_raw_type: Union[Unset, str] = UNSET
    mb_workflow_guid: Union[Unset, str] = UNSET
    ln_doc_version_guid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_user_guid = self.mb_user_guid

        ln_user_guid = self.ln_user_guid

        mb_t_stamp = self.mb_t_stamp

        ln_acl = self.ln_acl

        ln_text = self.ln_text

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_create_date_iso = self.ln_create_date_iso

        ln_update_date_iso = self.ln_update_date_iso

        mb_update_date_iso = self.mb_update_date_iso

        mb_all_members = self.mb_all_members

        ln_parent_guid = self.ln_parent_guid

        mb_acl = self.mb_acl

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_doc_version_guid = self.mb_doc_version_guid

        mb_create_date_iso = self.mb_create_date_iso

        mb_feed_guid = self.mb_feed_guid

        ln_workflow_guid = self.ln_workflow_guid

        ln_feed_guid = self.ln_feed_guid

        mb_parent_guid = self.mb_parent_guid

        mb_text = self.mb_text

        mb_guid = self.mb_guid

        mb_change_counter = self.mb_change_counter

        mb_raw_type = self.mb_raw_type

        mb_workflow_guid = self.mb_workflow_guid

        ln_doc_version_guid = self.ln_doc_version_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_user_guid is not UNSET:
            field_dict["mbUserGuid"] = mb_user_guid
        if ln_user_guid is not UNSET:
            field_dict["lnUserGuid"] = ln_user_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if ln_update_date_iso is not UNSET:
            field_dict["lnUpdateDateIso"] = ln_update_date_iso
        if mb_update_date_iso is not UNSET:
            field_dict["mbUpdateDateIso"] = mb_update_date_iso
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_parent_guid is not UNSET:
            field_dict["lnParentGuid"] = ln_parent_guid
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_doc_version_guid is not UNSET:
            field_dict["mbDocVersionGuid"] = mb_doc_version_guid
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if mb_feed_guid is not UNSET:
            field_dict["mbFeedGuid"] = mb_feed_guid
        if ln_workflow_guid is not UNSET:
            field_dict["lnWorkflowGuid"] = ln_workflow_guid
        if ln_feed_guid is not UNSET:
            field_dict["lnFeedGuid"] = ln_feed_guid
        if mb_parent_guid is not UNSET:
            field_dict["mbParentGuid"] = mb_parent_guid
        if mb_text is not UNSET:
            field_dict["mbText"] = mb_text
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_change_counter is not UNSET:
            field_dict["mbChangeCounter"] = mb_change_counter
        if mb_raw_type is not UNSET:
            field_dict["mbRawType"] = mb_raw_type
        if mb_workflow_guid is not UNSET:
            field_dict["mbWorkflowGuid"] = mb_workflow_guid
        if ln_doc_version_guid is not UNSET:
            field_dict["lnDocVersionGuid"] = ln_doc_version_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_user_guid = d.pop("mbUserGuid", UNSET)

        ln_user_guid = d.pop("lnUserGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        ln_text = d.pop("lnText", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        ln_update_date_iso = d.pop("lnUpdateDateIso", UNSET)

        mb_update_date_iso = d.pop("mbUpdateDateIso", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_parent_guid = d.pop("lnParentGuid", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_doc_version_guid = d.pop("mbDocVersionGuid", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        mb_feed_guid = d.pop("mbFeedGuid", UNSET)

        ln_workflow_guid = d.pop("lnWorkflowGuid", UNSET)

        ln_feed_guid = d.pop("lnFeedGuid", UNSET)

        mb_parent_guid = d.pop("mbParentGuid", UNSET)

        mb_text = d.pop("mbText", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        mb_change_counter = d.pop("mbChangeCounter", UNSET)

        mb_raw_type = d.pop("mbRawType", UNSET)

        mb_workflow_guid = d.pop("mbWorkflowGuid", UNSET)

        ln_doc_version_guid = d.pop("lnDocVersionGuid", UNSET)

        action_data_c = cls(
            mb_user_guid=mb_user_guid,
            ln_user_guid=ln_user_guid,
            mb_t_stamp=mb_t_stamp,
            ln_acl=ln_acl,
            ln_text=ln_text,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_create_date_iso=ln_create_date_iso,
            ln_update_date_iso=ln_update_date_iso,
            mb_update_date_iso=mb_update_date_iso,
            mb_all_members=mb_all_members,
            ln_parent_guid=ln_parent_guid,
            mb_acl=mb_acl,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_doc_version_guid=mb_doc_version_guid,
            mb_create_date_iso=mb_create_date_iso,
            mb_feed_guid=mb_feed_guid,
            ln_workflow_guid=ln_workflow_guid,
            ln_feed_guid=ln_feed_guid,
            mb_parent_guid=mb_parent_guid,
            mb_text=mb_text,
            mb_guid=mb_guid,
            mb_change_counter=mb_change_counter,
            mb_raw_type=mb_raw_type,
            mb_workflow_guid=mb_workflow_guid,
            ln_doc_version_guid=ln_doc_version_guid,
        )

        action_data_c.additional_properties = d
        return action_data_c

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
