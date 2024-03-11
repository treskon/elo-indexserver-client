from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionDataC")


@_attrs_define
class ActionDataC:
    """<p>
    Bit constants for members of Action
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_guid (Union[Unset, str]): Member bit: Action GUID.
                DB column: actionguid
            ln_guid (Union[Unset, int]): Column length: Action GUID.
                DB column: actionguid
            mb_raw_type (Union[Unset, str]): Member bit: Action type.
                DB column: actiontype
            mb_feed_guid (Union[Unset, str]): Member bit: Feed GUID.
                DB column: feedguid
            ln_feed_guid (Union[Unset, int]): Column length: Feed GUID.
                DB column: feedguid
            mb_parent_guid (Union[Unset, str]): Member bit: Parent action GUID.
                DB column: parentguid
            ln_parent_guid (Union[Unset, int]): Column length: Parent action GUID.
                DB column: parentguid
            mb_user_guid (Union[Unset, str]): Member bit: User GUID.
                DB column: userguid
            ln_user_guid (Union[Unset, int]): Column length: User GUID.
                DB column: userguid
            mb_create_date_iso (Union[Unset, str]): Member bit: Create date.
                DB column: createdateiso
            ln_create_date_iso (Union[Unset, int]): Column length: Create date.
                DB column: createdateiso
            mb_update_date_iso (Union[Unset, str]): Member bit: Update date.
                DB column: updatedateiso
            ln_update_date_iso (Union[Unset, int]): Column length: Update date.
                DB column: updatedateiso
            mb_change_counter (Union[Unset, str]): Member bit: Counts the number of updates.
                DB column: changecounter
            mb_text (Union[Unset, str]): Member bit: Comment text.
                DB column: actiontext
            ln_text (Union[Unset, int]): Column length: Comment text.
                DB column: actiontext
            mb_doc_version_guid (Union[Unset, str]): Member bit: GUID of the associated document version.
                DB column: docversionguid
            ln_doc_version_guid (Union[Unset, int]): Column length: GUID of the associated document version.
                DB column: docversionguid
            mb_workflow_guid (Union[Unset, str]): Member bit: GUID of the associated workflow.
                DB column: workflowguid
            ln_workflow_guid (Union[Unset, int]): Column length: GUID of the associated workflow.
                DB column: workflowguid
            mb_t_stamp (Union[Unset, str]): Member bit: Time stamp.
                DB column: actiontstamp
            ln_t_stamp (Union[Unset, int]): Column length: Time stamp.
                DB column: actiontstamp
            mb_acl (Union[Unset, str]): Member bit: Raw ACL representation.
                DB column: actionacl
            ln_acl (Union[Unset, int]): Column length: Raw ACL representation.
                DB column: actionacl
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: actiontstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: actiontstampsync
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_raw_type: Union[Unset, str] = UNSET
    mb_feed_guid: Union[Unset, str] = UNSET
    ln_feed_guid: Union[Unset, int] = UNSET
    mb_parent_guid: Union[Unset, str] = UNSET
    ln_parent_guid: Union[Unset, int] = UNSET
    mb_user_guid: Union[Unset, str] = UNSET
    ln_user_guid: Union[Unset, int] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_update_date_iso: Union[Unset, str] = UNSET
    ln_update_date_iso: Union[Unset, int] = UNSET
    mb_change_counter: Union[Unset, str] = UNSET
    mb_text: Union[Unset, str] = UNSET
    ln_text: Union[Unset, int] = UNSET
    mb_doc_version_guid: Union[Unset, str] = UNSET
    ln_doc_version_guid: Union[Unset, int] = UNSET
    mb_workflow_guid: Union[Unset, str] = UNSET
    ln_workflow_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_raw_type = self.mb_raw_type
        mb_feed_guid = self.mb_feed_guid
        ln_feed_guid = self.ln_feed_guid
        mb_parent_guid = self.mb_parent_guid
        ln_parent_guid = self.ln_parent_guid
        mb_user_guid = self.mb_user_guid
        ln_user_guid = self.ln_user_guid
        mb_create_date_iso = self.mb_create_date_iso
        ln_create_date_iso = self.ln_create_date_iso
        mb_update_date_iso = self.mb_update_date_iso
        ln_update_date_iso = self.ln_update_date_iso
        mb_change_counter = self.mb_change_counter
        mb_text = self.mb_text
        ln_text = self.ln_text
        mb_doc_version_guid = self.mb_doc_version_guid
        ln_doc_version_guid = self.ln_doc_version_guid
        mb_workflow_guid = self.mb_workflow_guid
        ln_workflow_guid = self.ln_workflow_guid
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_acl = self.mb_acl
        ln_acl = self.ln_acl
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_raw_type is not UNSET:
            field_dict["mbRawType"] = mb_raw_type
        if mb_feed_guid is not UNSET:
            field_dict["mbFeedGuid"] = mb_feed_guid
        if ln_feed_guid is not UNSET:
            field_dict["lnFeedGuid"] = ln_feed_guid
        if mb_parent_guid is not UNSET:
            field_dict["mbParentGuid"] = mb_parent_guid
        if ln_parent_guid is not UNSET:
            field_dict["lnParentGuid"] = ln_parent_guid
        if mb_user_guid is not UNSET:
            field_dict["mbUserGuid"] = mb_user_guid
        if ln_user_guid is not UNSET:
            field_dict["lnUserGuid"] = ln_user_guid
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_update_date_iso is not UNSET:
            field_dict["mbUpdateDateIso"] = mb_update_date_iso
        if ln_update_date_iso is not UNSET:
            field_dict["lnUpdateDateIso"] = ln_update_date_iso
        if mb_change_counter is not UNSET:
            field_dict["mbChangeCounter"] = mb_change_counter
        if mb_text is not UNSET:
            field_dict["mbText"] = mb_text
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text
        if mb_doc_version_guid is not UNSET:
            field_dict["mbDocVersionGuid"] = mb_doc_version_guid
        if ln_doc_version_guid is not UNSET:
            field_dict["lnDocVersionGuid"] = ln_doc_version_guid
        if mb_workflow_guid is not UNSET:
            field_dict["mbWorkflowGuid"] = mb_workflow_guid
        if ln_workflow_guid is not UNSET:
            field_dict["lnWorkflowGuid"] = ln_workflow_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
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
        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_raw_type = d.pop("mbRawType", UNSET)

        mb_feed_guid = d.pop("mbFeedGuid", UNSET)

        ln_feed_guid = d.pop("lnFeedGuid", UNSET)

        mb_parent_guid = d.pop("mbParentGuid", UNSET)

        ln_parent_guid = d.pop("lnParentGuid", UNSET)

        mb_user_guid = d.pop("mbUserGuid", UNSET)

        ln_user_guid = d.pop("lnUserGuid", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_update_date_iso = d.pop("mbUpdateDateIso", UNSET)

        ln_update_date_iso = d.pop("lnUpdateDateIso", UNSET)

        mb_change_counter = d.pop("mbChangeCounter", UNSET)

        mb_text = d.pop("mbText", UNSET)

        ln_text = d.pop("lnText", UNSET)

        mb_doc_version_guid = d.pop("mbDocVersionGuid", UNSET)

        ln_doc_version_guid = d.pop("lnDocVersionGuid", UNSET)

        mb_workflow_guid = d.pop("mbWorkflowGuid", UNSET)

        ln_workflow_guid = d.pop("lnWorkflowGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        action_data_c = cls(
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_raw_type=mb_raw_type,
            mb_feed_guid=mb_feed_guid,
            ln_feed_guid=ln_feed_guid,
            mb_parent_guid=mb_parent_guid,
            ln_parent_guid=ln_parent_guid,
            mb_user_guid=mb_user_guid,
            ln_user_guid=ln_user_guid,
            mb_create_date_iso=mb_create_date_iso,
            ln_create_date_iso=ln_create_date_iso,
            mb_update_date_iso=mb_update_date_iso,
            ln_update_date_iso=ln_update_date_iso,
            mb_change_counter=mb_change_counter,
            mb_text=mb_text,
            ln_text=ln_text,
            mb_doc_version_guid=mb_doc_version_guid,
            ln_doc_version_guid=ln_doc_version_guid,
            mb_workflow_guid=mb_workflow_guid,
            ln_workflow_guid=ln_workflow_guid,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_acl=mb_acl,
            ln_acl=ln_acl,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_all_members=mb_all_members,
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
