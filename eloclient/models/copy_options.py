from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyOptions")


@_attrs_define
class CopyOptions:
    """Structure for the options for the copy-process.
    <p>
     Copyright: Copyright (c) 2009
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            copy_structures_and_documents (Union[Unset, bool]): Copy all structures with the documents.
            target_name (Union[Unset, str]): Name of the target archive element.
            copy_only_workversion (Union[Unset, bool]): Do not copy all documents versions but only workversion
            keep_original_permissions (Union[Unset, bool]): Keep the current permissions.
                Only one of the three options keepOriginalPermissions,
                 takeTargetPermissions and acceptChanges can be true.
            incl_attachments (Union[Unset, bool]): Also copy all attachments.
            copy_only_base_element (Union[Unset, bool]): Copy only the base element.
            keep_original_owner (Union[Unset, bool]): Keep the original owner of the archive element.
            keep_references (Union[Unset, bool]): Keep references to original objects in copied parents.
                This member is ignored, if
                 ProcessInfo.inclReferences=false. If this member is true or only the parent is included in the
                 tree, the copied reference links the copied parent to the original object. If this member is
                 false and both the parent and object of a reference is included in the tree, the copied
                 reference links the copied parent to the copied object.
            take_target_permissions (Union[Unset, bool]): Take the target permissions.
                Only one of the three options keepOriginalPermissions,
                 takeTargetPermissions and acceptChanges can be true.
            keep_current_notes (Union[Unset, bool]): Keep the current documentnotes.
            new_parent_id (Union[Unset, int]): ParentId of the new element.
            move_only (Union[Unset, bool]): Only move the element.
            accept_changes (Union[Unset, bool]): Accept the change.
                Only one of the three options keepOriginalPermissions, takeTargetPermissions
                 and acceptChanges can be true.
            adjust_acl_difference (Union[Unset, bool]): The permissions of the moved objects are modified.
                The permissions inherited from the old
                 parent are substracted and the permissions of the new parent are added to the object.
            copy_only_work_attachment (Union[Unset, bool]): If inclAttachments and copyOnlyWorkAttachment are true, copy
                only the work attachments.
                Setting
                 copyOnlyWorkAttachment to true when inclAttachments is false is invalid.
    """

    copy_structures_and_documents: Union[Unset, bool] = UNSET
    target_name: Union[Unset, str] = UNSET
    copy_only_workversion: Union[Unset, bool] = UNSET
    keep_original_permissions: Union[Unset, bool] = UNSET
    incl_attachments: Union[Unset, bool] = UNSET
    copy_only_base_element: Union[Unset, bool] = UNSET
    keep_original_owner: Union[Unset, bool] = UNSET
    keep_references: Union[Unset, bool] = UNSET
    take_target_permissions: Union[Unset, bool] = UNSET
    keep_current_notes: Union[Unset, bool] = UNSET
    new_parent_id: Union[Unset, int] = UNSET
    move_only: Union[Unset, bool] = UNSET
    accept_changes: Union[Unset, bool] = UNSET
    adjust_acl_difference: Union[Unset, bool] = UNSET
    copy_only_work_attachment: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        copy_structures_and_documents = self.copy_structures_and_documents

        target_name = self.target_name

        copy_only_workversion = self.copy_only_workversion

        keep_original_permissions = self.keep_original_permissions

        incl_attachments = self.incl_attachments

        copy_only_base_element = self.copy_only_base_element

        keep_original_owner = self.keep_original_owner

        keep_references = self.keep_references

        take_target_permissions = self.take_target_permissions

        keep_current_notes = self.keep_current_notes

        new_parent_id = self.new_parent_id

        move_only = self.move_only

        accept_changes = self.accept_changes

        adjust_acl_difference = self.adjust_acl_difference

        copy_only_work_attachment = self.copy_only_work_attachment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if copy_structures_and_documents is not UNSET:
            field_dict["copyStructuresAndDocuments"] = copy_structures_and_documents
        if target_name is not UNSET:
            field_dict["targetName"] = target_name
        if copy_only_workversion is not UNSET:
            field_dict["copyOnlyWorkversion"] = copy_only_workversion
        if keep_original_permissions is not UNSET:
            field_dict["keepOriginalPermissions"] = keep_original_permissions
        if incl_attachments is not UNSET:
            field_dict["inclAttachments"] = incl_attachments
        if copy_only_base_element is not UNSET:
            field_dict["copyOnlyBaseElement"] = copy_only_base_element
        if keep_original_owner is not UNSET:
            field_dict["keepOriginalOwner"] = keep_original_owner
        if keep_references is not UNSET:
            field_dict["keepReferences"] = keep_references
        if take_target_permissions is not UNSET:
            field_dict["takeTargetPermissions"] = take_target_permissions
        if keep_current_notes is not UNSET:
            field_dict["keepCurrentNotes"] = keep_current_notes
        if new_parent_id is not UNSET:
            field_dict["newParentId"] = new_parent_id
        if move_only is not UNSET:
            field_dict["moveOnly"] = move_only
        if accept_changes is not UNSET:
            field_dict["acceptChanges"] = accept_changes
        if adjust_acl_difference is not UNSET:
            field_dict["adjustAclDifference"] = adjust_acl_difference
        if copy_only_work_attachment is not UNSET:
            field_dict["copyOnlyWorkAttachment"] = copy_only_work_attachment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        copy_structures_and_documents = d.pop("copyStructuresAndDocuments", UNSET)

        target_name = d.pop("targetName", UNSET)

        copy_only_workversion = d.pop("copyOnlyWorkversion", UNSET)

        keep_original_permissions = d.pop("keepOriginalPermissions", UNSET)

        incl_attachments = d.pop("inclAttachments", UNSET)

        copy_only_base_element = d.pop("copyOnlyBaseElement", UNSET)

        keep_original_owner = d.pop("keepOriginalOwner", UNSET)

        keep_references = d.pop("keepReferences", UNSET)

        take_target_permissions = d.pop("takeTargetPermissions", UNSET)

        keep_current_notes = d.pop("keepCurrentNotes", UNSET)

        new_parent_id = d.pop("newParentId", UNSET)

        move_only = d.pop("moveOnly", UNSET)

        accept_changes = d.pop("acceptChanges", UNSET)

        adjust_acl_difference = d.pop("adjustAclDifference", UNSET)

        copy_only_work_attachment = d.pop("copyOnlyWorkAttachment", UNSET)

        copy_options = cls(
            copy_structures_and_documents=copy_structures_and_documents,
            target_name=target_name,
            copy_only_workversion=copy_only_workversion,
            keep_original_permissions=keep_original_permissions,
            incl_attachments=incl_attachments,
            copy_only_base_element=copy_only_base_element,
            keep_original_owner=keep_original_owner,
            keep_references=keep_references,
            take_target_permissions=take_target_permissions,
            keep_current_notes=keep_current_notes,
            new_parent_id=new_parent_id,
            move_only=move_only,
            accept_changes=accept_changes,
            adjust_acl_difference=adjust_acl_difference,
            copy_only_work_attachment=copy_only_work_attachment,
        )

        copy_options.additional_properties = d
        return copy_options

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
