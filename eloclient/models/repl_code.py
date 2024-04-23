from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplCode")


@_attrs_define
class ReplCode:
    """Constants for replication codes.

    Attributes:
        arcr_ext_code_undef_s (Union[Unset, str]):
        arcr_docmask_delete_s (Union[Unset, str]):
        arcr_code_sep (Union[Unset, str]):
        arcr_object_data_s (Union[Unset, str]):
        arcr_ignore_broker_optz (Union[Unset, int]): Change code: Ignore the optional broker optimization anyway a)
            selective export b) VDS
        arcr_workflow_data_s (Union[Unset, str]):
        arcr_initial_data (Union[Unset, int]): Change flag: This flag is added to ARCR_OBJECT_DATA if replication
            performs a full export.
        arcr_object_insert_ref (Union[Unset, int]): Change code: Insert a (logical) reference inside an archive entry.
        arcr_translation_s (Union[Unset, str]):
        arcr_control_vds_s (Union[Unset, str]):
        arcr_note_delete (Union[Unset, int]): Change code: Delete a note.
        arcr_document_feed (Union[Unset, int]):
        arcr_object_delete_ref_s (Union[Unset, str]):
        arcr_basedata_verify (Union[Unset, int]): Change code: Master data. Exports the names of storage masks, keys,
            users.
        arcr_swl_data_s (Union[Unset, str]):
        arcr_swl_data (Union[Unset, int]): Change code: A keyword list has been modified Param: 1 für Stichwortliste
            geändert, 2 für
            Stichwortliste gelöscht
        arcr_object_delete_ref (Union[Unset, int]): Change code: Delete a (logical) reference inside an archive entry.
        arcr_document_data (Union[Unset, int]): Change code: Insert a document and change the work version of the
            associated archive entry.
        arcr_object_relations (Union[Unset, int]): Change code: Change all references to children.
        arcr_object_replset (Union[Unset, int]): Change code: Change the replication sets of an archive entry.
        arcr_broker_s (Union[Unset, str]):
        arcr_document_status_s (Union[Unset, str]):
        arcr_object_keys (Union[Unset, int]): Change code: Modify the indexing information (only <code>Sord.
            getObjKeys()</code>) of an
             archive entry (<code>Sord</code>).
        arcr_action (Union[Unset, int]): Change code: Insert, modify, delete activities.
        arcr_user_data (Union[Unset, int]): Change code: Insert or modify user data.
        param_swl_updated (Union[Unset, int]):
        arcr_signature_data_s (Union[Unset, str]):
        arcr_document_data_s (Union[Unset, str]):
        arcr_object_keys_s (Union[Unset, str]):
        arcr_document_switch_s (Union[Unset, str]):
        arcr_document_status (Union[Unset, int]): Change code: Document flags and/or document delete status have been
            changed
        arcr_document_feed_s (Union[Unset, str]):
        arcr_object_delete_phys (Union[Unset, int]): Change code: Delete object finally.
        arcr_signature_data (Union[Unset, int]): Change code: Create a document signature
        arcr_basedata_verify_s (Union[Unset, str]):
        arcr_user_delete (Union[Unset, int]): Change code: Delete a user.
        arcr_trafo_s (Union[Unset, str]):
        arcr_set2 (Union[Unset, int]): Change flag: This flag is contained in some change codes to extend the number of
            possible
            change codes.
        arcr_broker (Union[Unset, int]): Change flag: This flag marks a change record to be a control record for the
            broker.
        arcr_object_replset_s (Union[Unset, str]):
        arcr_object_delete_phys_s (Union[Unset, str]):
        arcr_set16 (Union[Unset, int]): Change flag: This flag is contained in some change codes to extend the number of
            possible
            change codes.
        arcr_map_changed (Union[Unset, int]): Change code: map changed
        arcr_marker (Union[Unset, int]): Change code: Set a replication marker.
        arcr_document_switch (Union[Unset, int]): Change code: Select another work version from the document history.
        arcr_workflow_data (Union[Unset, int]): Change code: Change a workflow.
        arcr_object_hist_s (Union[Unset, str]):
        arcr_trafo (Union[Unset, int]): Change code: Transformation table for master data (broker-to-broker
            replication).
        arcr_document_insert_s (Union[Unset, str]):
        arcr_map_changed_s (Union[Unset, str]):
        arcr_user_data_s (Union[Unset, str]):
        arcr_document_insert (Union[Unset, int]): Change code: Insert a document but do not change the work version of
            the associated archive
            entry.
        arcr_extended_set (Union[Unset, int]): Change flags: Bits of this value are contained in some change codes to
            extend the number of
            possible change codes.
        arcr_version_comment_s (Union[Unset, str]):
        arcr_marker_s (Union[Unset, str]):
        arcr_ignore_broker_optz_s (Union[Unset, str]):
        arcr_attachment_data_s (Union[Unset, str]):
        arcr_docmasks_data (Union[Unset, int]): Change code: Exports the storage masks.
        arcr_object_insert_ref_s (Union[Unset, str]):
        arcr_link_s (Union[Unset, str]):
        arcr_control_vds (Union[Unset, int]): Change code: A VDS has been created
        arcr_action_s (Union[Unset, str]):
        arcr_object_relations_s (Union[Unset, str]):
        arcr_docmask_delete (Union[Unset, int]): Change code: Delete a storage mask.
            (reserved)
        arcr_initial_data_s (Union[Unset, str]):
        arcr_translation (Union[Unset, int]): Change code: Insert or modify storage mask data.
            (reserved)
        param_swl_deleted (Union[Unset, int]):
        arcr_object_hist (Union[Unset, int]): Change code: Create a new entry for the object history
        arcr_link (Union[Unset, int]):
        arcr_version_comment (Union[Unset, int]): Change code: Changed document comment
        arcr_docmasks_data_s (Union[Unset, str]):
        arcr_user_delete_s (Union[Unset, str]):
        arcr_note_data_s (Union[Unset, str]):
        arcr_object_data (Union[Unset, int]): Change code: Modify the indexing information (without <code>Sord.
            getObjKeys()</code>) of an
             archive entry (<code>Sord</code>).
        arcr_note_data (Union[Unset, int]): Change code: Create or modify a note.
        arcr_note_delete_s (Union[Unset, str]):
        arcr_attachment_data (Union[Unset, int]): Change code: Insert or change an attachment.
    """

    arcr_ext_code_undef_s: Union[Unset, str] = UNSET
    arcr_docmask_delete_s: Union[Unset, str] = UNSET
    arcr_code_sep: Union[Unset, str] = UNSET
    arcr_object_data_s: Union[Unset, str] = UNSET
    arcr_ignore_broker_optz: Union[Unset, int] = UNSET
    arcr_workflow_data_s: Union[Unset, str] = UNSET
    arcr_initial_data: Union[Unset, int] = UNSET
    arcr_object_insert_ref: Union[Unset, int] = UNSET
    arcr_translation_s: Union[Unset, str] = UNSET
    arcr_control_vds_s: Union[Unset, str] = UNSET
    arcr_note_delete: Union[Unset, int] = UNSET
    arcr_document_feed: Union[Unset, int] = UNSET
    arcr_object_delete_ref_s: Union[Unset, str] = UNSET
    arcr_basedata_verify: Union[Unset, int] = UNSET
    arcr_swl_data_s: Union[Unset, str] = UNSET
    arcr_swl_data: Union[Unset, int] = UNSET
    arcr_object_delete_ref: Union[Unset, int] = UNSET
    arcr_document_data: Union[Unset, int] = UNSET
    arcr_object_relations: Union[Unset, int] = UNSET
    arcr_object_replset: Union[Unset, int] = UNSET
    arcr_broker_s: Union[Unset, str] = UNSET
    arcr_document_status_s: Union[Unset, str] = UNSET
    arcr_object_keys: Union[Unset, int] = UNSET
    arcr_action: Union[Unset, int] = UNSET
    arcr_user_data: Union[Unset, int] = UNSET
    param_swl_updated: Union[Unset, int] = UNSET
    arcr_signature_data_s: Union[Unset, str] = UNSET
    arcr_document_data_s: Union[Unset, str] = UNSET
    arcr_object_keys_s: Union[Unset, str] = UNSET
    arcr_document_switch_s: Union[Unset, str] = UNSET
    arcr_document_status: Union[Unset, int] = UNSET
    arcr_document_feed_s: Union[Unset, str] = UNSET
    arcr_object_delete_phys: Union[Unset, int] = UNSET
    arcr_signature_data: Union[Unset, int] = UNSET
    arcr_basedata_verify_s: Union[Unset, str] = UNSET
    arcr_user_delete: Union[Unset, int] = UNSET
    arcr_trafo_s: Union[Unset, str] = UNSET
    arcr_set2: Union[Unset, int] = UNSET
    arcr_broker: Union[Unset, int] = UNSET
    arcr_object_replset_s: Union[Unset, str] = UNSET
    arcr_object_delete_phys_s: Union[Unset, str] = UNSET
    arcr_set16: Union[Unset, int] = UNSET
    arcr_map_changed: Union[Unset, int] = UNSET
    arcr_marker: Union[Unset, int] = UNSET
    arcr_document_switch: Union[Unset, int] = UNSET
    arcr_workflow_data: Union[Unset, int] = UNSET
    arcr_object_hist_s: Union[Unset, str] = UNSET
    arcr_trafo: Union[Unset, int] = UNSET
    arcr_document_insert_s: Union[Unset, str] = UNSET
    arcr_map_changed_s: Union[Unset, str] = UNSET
    arcr_user_data_s: Union[Unset, str] = UNSET
    arcr_document_insert: Union[Unset, int] = UNSET
    arcr_extended_set: Union[Unset, int] = UNSET
    arcr_version_comment_s: Union[Unset, str] = UNSET
    arcr_marker_s: Union[Unset, str] = UNSET
    arcr_ignore_broker_optz_s: Union[Unset, str] = UNSET
    arcr_attachment_data_s: Union[Unset, str] = UNSET
    arcr_docmasks_data: Union[Unset, int] = UNSET
    arcr_object_insert_ref_s: Union[Unset, str] = UNSET
    arcr_link_s: Union[Unset, str] = UNSET
    arcr_control_vds: Union[Unset, int] = UNSET
    arcr_action_s: Union[Unset, str] = UNSET
    arcr_object_relations_s: Union[Unset, str] = UNSET
    arcr_docmask_delete: Union[Unset, int] = UNSET
    arcr_initial_data_s: Union[Unset, str] = UNSET
    arcr_translation: Union[Unset, int] = UNSET
    param_swl_deleted: Union[Unset, int] = UNSET
    arcr_object_hist: Union[Unset, int] = UNSET
    arcr_link: Union[Unset, int] = UNSET
    arcr_version_comment: Union[Unset, int] = UNSET
    arcr_docmasks_data_s: Union[Unset, str] = UNSET
    arcr_user_delete_s: Union[Unset, str] = UNSET
    arcr_note_data_s: Union[Unset, str] = UNSET
    arcr_object_data: Union[Unset, int] = UNSET
    arcr_note_data: Union[Unset, int] = UNSET
    arcr_note_delete_s: Union[Unset, str] = UNSET
    arcr_attachment_data: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arcr_ext_code_undef_s = self.arcr_ext_code_undef_s

        arcr_docmask_delete_s = self.arcr_docmask_delete_s

        arcr_code_sep = self.arcr_code_sep

        arcr_object_data_s = self.arcr_object_data_s

        arcr_ignore_broker_optz = self.arcr_ignore_broker_optz

        arcr_workflow_data_s = self.arcr_workflow_data_s

        arcr_initial_data = self.arcr_initial_data

        arcr_object_insert_ref = self.arcr_object_insert_ref

        arcr_translation_s = self.arcr_translation_s

        arcr_control_vds_s = self.arcr_control_vds_s

        arcr_note_delete = self.arcr_note_delete

        arcr_document_feed = self.arcr_document_feed

        arcr_object_delete_ref_s = self.arcr_object_delete_ref_s

        arcr_basedata_verify = self.arcr_basedata_verify

        arcr_swl_data_s = self.arcr_swl_data_s

        arcr_swl_data = self.arcr_swl_data

        arcr_object_delete_ref = self.arcr_object_delete_ref

        arcr_document_data = self.arcr_document_data

        arcr_object_relations = self.arcr_object_relations

        arcr_object_replset = self.arcr_object_replset

        arcr_broker_s = self.arcr_broker_s

        arcr_document_status_s = self.arcr_document_status_s

        arcr_object_keys = self.arcr_object_keys

        arcr_action = self.arcr_action

        arcr_user_data = self.arcr_user_data

        param_swl_updated = self.param_swl_updated

        arcr_signature_data_s = self.arcr_signature_data_s

        arcr_document_data_s = self.arcr_document_data_s

        arcr_object_keys_s = self.arcr_object_keys_s

        arcr_document_switch_s = self.arcr_document_switch_s

        arcr_document_status = self.arcr_document_status

        arcr_document_feed_s = self.arcr_document_feed_s

        arcr_object_delete_phys = self.arcr_object_delete_phys

        arcr_signature_data = self.arcr_signature_data

        arcr_basedata_verify_s = self.arcr_basedata_verify_s

        arcr_user_delete = self.arcr_user_delete

        arcr_trafo_s = self.arcr_trafo_s

        arcr_set2 = self.arcr_set2

        arcr_broker = self.arcr_broker

        arcr_object_replset_s = self.arcr_object_replset_s

        arcr_object_delete_phys_s = self.arcr_object_delete_phys_s

        arcr_set16 = self.arcr_set16

        arcr_map_changed = self.arcr_map_changed

        arcr_marker = self.arcr_marker

        arcr_document_switch = self.arcr_document_switch

        arcr_workflow_data = self.arcr_workflow_data

        arcr_object_hist_s = self.arcr_object_hist_s

        arcr_trafo = self.arcr_trafo

        arcr_document_insert_s = self.arcr_document_insert_s

        arcr_map_changed_s = self.arcr_map_changed_s

        arcr_user_data_s = self.arcr_user_data_s

        arcr_document_insert = self.arcr_document_insert

        arcr_extended_set = self.arcr_extended_set

        arcr_version_comment_s = self.arcr_version_comment_s

        arcr_marker_s = self.arcr_marker_s

        arcr_ignore_broker_optz_s = self.arcr_ignore_broker_optz_s

        arcr_attachment_data_s = self.arcr_attachment_data_s

        arcr_docmasks_data = self.arcr_docmasks_data

        arcr_object_insert_ref_s = self.arcr_object_insert_ref_s

        arcr_link_s = self.arcr_link_s

        arcr_control_vds = self.arcr_control_vds

        arcr_action_s = self.arcr_action_s

        arcr_object_relations_s = self.arcr_object_relations_s

        arcr_docmask_delete = self.arcr_docmask_delete

        arcr_initial_data_s = self.arcr_initial_data_s

        arcr_translation = self.arcr_translation

        param_swl_deleted = self.param_swl_deleted

        arcr_object_hist = self.arcr_object_hist

        arcr_link = self.arcr_link

        arcr_version_comment = self.arcr_version_comment

        arcr_docmasks_data_s = self.arcr_docmasks_data_s

        arcr_user_delete_s = self.arcr_user_delete_s

        arcr_note_data_s = self.arcr_note_data_s

        arcr_object_data = self.arcr_object_data

        arcr_note_data = self.arcr_note_data

        arcr_note_delete_s = self.arcr_note_delete_s

        arcr_attachment_data = self.arcr_attachment_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arcr_ext_code_undef_s is not UNSET:
            field_dict["ARCR_EXT_CODE_UNDEF_S"] = arcr_ext_code_undef_s
        if arcr_docmask_delete_s is not UNSET:
            field_dict["ARCR_DOCMASK_DELETE_S"] = arcr_docmask_delete_s
        if arcr_code_sep is not UNSET:
            field_dict["ARCR_CODE_SEP"] = arcr_code_sep
        if arcr_object_data_s is not UNSET:
            field_dict["ARCR_OBJECT_DATA_S"] = arcr_object_data_s
        if arcr_ignore_broker_optz is not UNSET:
            field_dict["ARCR_IGNORE_BROKER_OPTZ"] = arcr_ignore_broker_optz
        if arcr_workflow_data_s is not UNSET:
            field_dict["ARCR_WORKFLOW_DATA_S"] = arcr_workflow_data_s
        if arcr_initial_data is not UNSET:
            field_dict["ARCR_INITIAL_DATA"] = arcr_initial_data
        if arcr_object_insert_ref is not UNSET:
            field_dict["ARCR_OBJECT_INSERT_REF"] = arcr_object_insert_ref
        if arcr_translation_s is not UNSET:
            field_dict["ARCR_TRANSLATION_S"] = arcr_translation_s
        if arcr_control_vds_s is not UNSET:
            field_dict["ARCR_CONTROL_VDS_S"] = arcr_control_vds_s
        if arcr_note_delete is not UNSET:
            field_dict["ARCR_NOTE_DELETE"] = arcr_note_delete
        if arcr_document_feed is not UNSET:
            field_dict["ARCR_DOCUMENT_FEED"] = arcr_document_feed
        if arcr_object_delete_ref_s is not UNSET:
            field_dict["ARCR_OBJECT_DELETE_REF_S"] = arcr_object_delete_ref_s
        if arcr_basedata_verify is not UNSET:
            field_dict["ARCR_BASEDATA_VERIFY"] = arcr_basedata_verify
        if arcr_swl_data_s is not UNSET:
            field_dict["ARCR_SWL_DATA_S"] = arcr_swl_data_s
        if arcr_swl_data is not UNSET:
            field_dict["ARCR_SWL_DATA"] = arcr_swl_data
        if arcr_object_delete_ref is not UNSET:
            field_dict["ARCR_OBJECT_DELETE_REF"] = arcr_object_delete_ref
        if arcr_document_data is not UNSET:
            field_dict["ARCR_DOCUMENT_DATA"] = arcr_document_data
        if arcr_object_relations is not UNSET:
            field_dict["ARCR_OBJECT_RELATIONS"] = arcr_object_relations
        if arcr_object_replset is not UNSET:
            field_dict["ARCR_OBJECT_REPLSET"] = arcr_object_replset
        if arcr_broker_s is not UNSET:
            field_dict["ARCR_BROKER_S"] = arcr_broker_s
        if arcr_document_status_s is not UNSET:
            field_dict["ARCR_DOCUMENT_STATUS_S"] = arcr_document_status_s
        if arcr_object_keys is not UNSET:
            field_dict["ARCR_OBJECT_KEYS"] = arcr_object_keys
        if arcr_action is not UNSET:
            field_dict["ARCR_ACTION"] = arcr_action
        if arcr_user_data is not UNSET:
            field_dict["ARCR_USER_DATA"] = arcr_user_data
        if param_swl_updated is not UNSET:
            field_dict["PARAM_SWL_UPDATED"] = param_swl_updated
        if arcr_signature_data_s is not UNSET:
            field_dict["ARCR_SIGNATURE_DATA_S"] = arcr_signature_data_s
        if arcr_document_data_s is not UNSET:
            field_dict["ARCR_DOCUMENT_DATA_S"] = arcr_document_data_s
        if arcr_object_keys_s is not UNSET:
            field_dict["ARCR_OBJECT_KEYS_S"] = arcr_object_keys_s
        if arcr_document_switch_s is not UNSET:
            field_dict["ARCR_DOCUMENT_SWITCH_S"] = arcr_document_switch_s
        if arcr_document_status is not UNSET:
            field_dict["ARCR_DOCUMENT_STATUS"] = arcr_document_status
        if arcr_document_feed_s is not UNSET:
            field_dict["ARCR_DOCUMENT_FEED_S"] = arcr_document_feed_s
        if arcr_object_delete_phys is not UNSET:
            field_dict["ARCR_OBJECT_DELETE_PHYS"] = arcr_object_delete_phys
        if arcr_signature_data is not UNSET:
            field_dict["ARCR_SIGNATURE_DATA"] = arcr_signature_data
        if arcr_basedata_verify_s is not UNSET:
            field_dict["ARCR_BASEDATA_VERIFY_S"] = arcr_basedata_verify_s
        if arcr_user_delete is not UNSET:
            field_dict["ARCR_USER_DELETE"] = arcr_user_delete
        if arcr_trafo_s is not UNSET:
            field_dict["ARCR_TRAFO_S"] = arcr_trafo_s
        if arcr_set2 is not UNSET:
            field_dict["ARCR_SET2"] = arcr_set2
        if arcr_broker is not UNSET:
            field_dict["ARCR_BROKER"] = arcr_broker
        if arcr_object_replset_s is not UNSET:
            field_dict["ARCR_OBJECT_REPLSET_S"] = arcr_object_replset_s
        if arcr_object_delete_phys_s is not UNSET:
            field_dict["ARCR_OBJECT_DELETE_PHYS_S"] = arcr_object_delete_phys_s
        if arcr_set16 is not UNSET:
            field_dict["ARCR_SET16"] = arcr_set16
        if arcr_map_changed is not UNSET:
            field_dict["ARCR_MAP_CHANGED"] = arcr_map_changed
        if arcr_marker is not UNSET:
            field_dict["ARCR_MARKER"] = arcr_marker
        if arcr_document_switch is not UNSET:
            field_dict["ARCR_DOCUMENT_SWITCH"] = arcr_document_switch
        if arcr_workflow_data is not UNSET:
            field_dict["ARCR_WORKFLOW_DATA"] = arcr_workflow_data
        if arcr_object_hist_s is not UNSET:
            field_dict["ARCR_OBJECT_HIST_S"] = arcr_object_hist_s
        if arcr_trafo is not UNSET:
            field_dict["ARCR_TRAFO"] = arcr_trafo
        if arcr_document_insert_s is not UNSET:
            field_dict["ARCR_DOCUMENT_INSERT_S"] = arcr_document_insert_s
        if arcr_map_changed_s is not UNSET:
            field_dict["ARCR_MAP_CHANGED_S"] = arcr_map_changed_s
        if arcr_user_data_s is not UNSET:
            field_dict["ARCR_USER_DATA_S"] = arcr_user_data_s
        if arcr_document_insert is not UNSET:
            field_dict["ARCR_DOCUMENT_INSERT"] = arcr_document_insert
        if arcr_extended_set is not UNSET:
            field_dict["ARCR_EXTENDED_SET"] = arcr_extended_set
        if arcr_version_comment_s is not UNSET:
            field_dict["ARCR_VERSION_COMMENT_S"] = arcr_version_comment_s
        if arcr_marker_s is not UNSET:
            field_dict["ARCR_MARKER_S"] = arcr_marker_s
        if arcr_ignore_broker_optz_s is not UNSET:
            field_dict["ARCR_IGNORE_BROKER_OPTZ_S"] = arcr_ignore_broker_optz_s
        if arcr_attachment_data_s is not UNSET:
            field_dict["ARCR_ATTACHMENT_DATA_S"] = arcr_attachment_data_s
        if arcr_docmasks_data is not UNSET:
            field_dict["ARCR_DOCMASKS_DATA"] = arcr_docmasks_data
        if arcr_object_insert_ref_s is not UNSET:
            field_dict["ARCR_OBJECT_INSERT_REF_S"] = arcr_object_insert_ref_s
        if arcr_link_s is not UNSET:
            field_dict["ARCR_LINK_S"] = arcr_link_s
        if arcr_control_vds is not UNSET:
            field_dict["ARCR_CONTROL_VDS"] = arcr_control_vds
        if arcr_action_s is not UNSET:
            field_dict["ARCR_ACTION_S"] = arcr_action_s
        if arcr_object_relations_s is not UNSET:
            field_dict["ARCR_OBJECT_RELATIONS_S"] = arcr_object_relations_s
        if arcr_docmask_delete is not UNSET:
            field_dict["ARCR_DOCMASK_DELETE"] = arcr_docmask_delete
        if arcr_initial_data_s is not UNSET:
            field_dict["ARCR_INITIAL_DATA_S"] = arcr_initial_data_s
        if arcr_translation is not UNSET:
            field_dict["ARCR_TRANSLATION"] = arcr_translation
        if param_swl_deleted is not UNSET:
            field_dict["PARAM_SWL_DELETED"] = param_swl_deleted
        if arcr_object_hist is not UNSET:
            field_dict["ARCR_OBJECT_HIST"] = arcr_object_hist
        if arcr_link is not UNSET:
            field_dict["ARCR_LINK"] = arcr_link
        if arcr_version_comment is not UNSET:
            field_dict["ARCR_VERSION_COMMENT"] = arcr_version_comment
        if arcr_docmasks_data_s is not UNSET:
            field_dict["ARCR_DOCMASKS_DATA_S"] = arcr_docmasks_data_s
        if arcr_user_delete_s is not UNSET:
            field_dict["ARCR_USER_DELETE_S"] = arcr_user_delete_s
        if arcr_note_data_s is not UNSET:
            field_dict["ARCR_NOTE_DATA_S"] = arcr_note_data_s
        if arcr_object_data is not UNSET:
            field_dict["ARCR_OBJECT_DATA"] = arcr_object_data
        if arcr_note_data is not UNSET:
            field_dict["ARCR_NOTE_DATA"] = arcr_note_data
        if arcr_note_delete_s is not UNSET:
            field_dict["ARCR_NOTE_DELETE_S"] = arcr_note_delete_s
        if arcr_attachment_data is not UNSET:
            field_dict["ARCR_ATTACHMENT_DATA"] = arcr_attachment_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        arcr_ext_code_undef_s = d.pop("ARCR_EXT_CODE_UNDEF_S", UNSET)

        arcr_docmask_delete_s = d.pop("ARCR_DOCMASK_DELETE_S", UNSET)

        arcr_code_sep = d.pop("ARCR_CODE_SEP", UNSET)

        arcr_object_data_s = d.pop("ARCR_OBJECT_DATA_S", UNSET)

        arcr_ignore_broker_optz = d.pop("ARCR_IGNORE_BROKER_OPTZ", UNSET)

        arcr_workflow_data_s = d.pop("ARCR_WORKFLOW_DATA_S", UNSET)

        arcr_initial_data = d.pop("ARCR_INITIAL_DATA", UNSET)

        arcr_object_insert_ref = d.pop("ARCR_OBJECT_INSERT_REF", UNSET)

        arcr_translation_s = d.pop("ARCR_TRANSLATION_S", UNSET)

        arcr_control_vds_s = d.pop("ARCR_CONTROL_VDS_S", UNSET)

        arcr_note_delete = d.pop("ARCR_NOTE_DELETE", UNSET)

        arcr_document_feed = d.pop("ARCR_DOCUMENT_FEED", UNSET)

        arcr_object_delete_ref_s = d.pop("ARCR_OBJECT_DELETE_REF_S", UNSET)

        arcr_basedata_verify = d.pop("ARCR_BASEDATA_VERIFY", UNSET)

        arcr_swl_data_s = d.pop("ARCR_SWL_DATA_S", UNSET)

        arcr_swl_data = d.pop("ARCR_SWL_DATA", UNSET)

        arcr_object_delete_ref = d.pop("ARCR_OBJECT_DELETE_REF", UNSET)

        arcr_document_data = d.pop("ARCR_DOCUMENT_DATA", UNSET)

        arcr_object_relations = d.pop("ARCR_OBJECT_RELATIONS", UNSET)

        arcr_object_replset = d.pop("ARCR_OBJECT_REPLSET", UNSET)

        arcr_broker_s = d.pop("ARCR_BROKER_S", UNSET)

        arcr_document_status_s = d.pop("ARCR_DOCUMENT_STATUS_S", UNSET)

        arcr_object_keys = d.pop("ARCR_OBJECT_KEYS", UNSET)

        arcr_action = d.pop("ARCR_ACTION", UNSET)

        arcr_user_data = d.pop("ARCR_USER_DATA", UNSET)

        param_swl_updated = d.pop("PARAM_SWL_UPDATED", UNSET)

        arcr_signature_data_s = d.pop("ARCR_SIGNATURE_DATA_S", UNSET)

        arcr_document_data_s = d.pop("ARCR_DOCUMENT_DATA_S", UNSET)

        arcr_object_keys_s = d.pop("ARCR_OBJECT_KEYS_S", UNSET)

        arcr_document_switch_s = d.pop("ARCR_DOCUMENT_SWITCH_S", UNSET)

        arcr_document_status = d.pop("ARCR_DOCUMENT_STATUS", UNSET)

        arcr_document_feed_s = d.pop("ARCR_DOCUMENT_FEED_S", UNSET)

        arcr_object_delete_phys = d.pop("ARCR_OBJECT_DELETE_PHYS", UNSET)

        arcr_signature_data = d.pop("ARCR_SIGNATURE_DATA", UNSET)

        arcr_basedata_verify_s = d.pop("ARCR_BASEDATA_VERIFY_S", UNSET)

        arcr_user_delete = d.pop("ARCR_USER_DELETE", UNSET)

        arcr_trafo_s = d.pop("ARCR_TRAFO_S", UNSET)

        arcr_set2 = d.pop("ARCR_SET2", UNSET)

        arcr_broker = d.pop("ARCR_BROKER", UNSET)

        arcr_object_replset_s = d.pop("ARCR_OBJECT_REPLSET_S", UNSET)

        arcr_object_delete_phys_s = d.pop("ARCR_OBJECT_DELETE_PHYS_S", UNSET)

        arcr_set16 = d.pop("ARCR_SET16", UNSET)

        arcr_map_changed = d.pop("ARCR_MAP_CHANGED", UNSET)

        arcr_marker = d.pop("ARCR_MARKER", UNSET)

        arcr_document_switch = d.pop("ARCR_DOCUMENT_SWITCH", UNSET)

        arcr_workflow_data = d.pop("ARCR_WORKFLOW_DATA", UNSET)

        arcr_object_hist_s = d.pop("ARCR_OBJECT_HIST_S", UNSET)

        arcr_trafo = d.pop("ARCR_TRAFO", UNSET)

        arcr_document_insert_s = d.pop("ARCR_DOCUMENT_INSERT_S", UNSET)

        arcr_map_changed_s = d.pop("ARCR_MAP_CHANGED_S", UNSET)

        arcr_user_data_s = d.pop("ARCR_USER_DATA_S", UNSET)

        arcr_document_insert = d.pop("ARCR_DOCUMENT_INSERT", UNSET)

        arcr_extended_set = d.pop("ARCR_EXTENDED_SET", UNSET)

        arcr_version_comment_s = d.pop("ARCR_VERSION_COMMENT_S", UNSET)

        arcr_marker_s = d.pop("ARCR_MARKER_S", UNSET)

        arcr_ignore_broker_optz_s = d.pop("ARCR_IGNORE_BROKER_OPTZ_S", UNSET)

        arcr_attachment_data_s = d.pop("ARCR_ATTACHMENT_DATA_S", UNSET)

        arcr_docmasks_data = d.pop("ARCR_DOCMASKS_DATA", UNSET)

        arcr_object_insert_ref_s = d.pop("ARCR_OBJECT_INSERT_REF_S", UNSET)

        arcr_link_s = d.pop("ARCR_LINK_S", UNSET)

        arcr_control_vds = d.pop("ARCR_CONTROL_VDS", UNSET)

        arcr_action_s = d.pop("ARCR_ACTION_S", UNSET)

        arcr_object_relations_s = d.pop("ARCR_OBJECT_RELATIONS_S", UNSET)

        arcr_docmask_delete = d.pop("ARCR_DOCMASK_DELETE", UNSET)

        arcr_initial_data_s = d.pop("ARCR_INITIAL_DATA_S", UNSET)

        arcr_translation = d.pop("ARCR_TRANSLATION", UNSET)

        param_swl_deleted = d.pop("PARAM_SWL_DELETED", UNSET)

        arcr_object_hist = d.pop("ARCR_OBJECT_HIST", UNSET)

        arcr_link = d.pop("ARCR_LINK", UNSET)

        arcr_version_comment = d.pop("ARCR_VERSION_COMMENT", UNSET)

        arcr_docmasks_data_s = d.pop("ARCR_DOCMASKS_DATA_S", UNSET)

        arcr_user_delete_s = d.pop("ARCR_USER_DELETE_S", UNSET)

        arcr_note_data_s = d.pop("ARCR_NOTE_DATA_S", UNSET)

        arcr_object_data = d.pop("ARCR_OBJECT_DATA", UNSET)

        arcr_note_data = d.pop("ARCR_NOTE_DATA", UNSET)

        arcr_note_delete_s = d.pop("ARCR_NOTE_DELETE_S", UNSET)

        arcr_attachment_data = d.pop("ARCR_ATTACHMENT_DATA", UNSET)

        repl_code = cls(
            arcr_ext_code_undef_s=arcr_ext_code_undef_s,
            arcr_docmask_delete_s=arcr_docmask_delete_s,
            arcr_code_sep=arcr_code_sep,
            arcr_object_data_s=arcr_object_data_s,
            arcr_ignore_broker_optz=arcr_ignore_broker_optz,
            arcr_workflow_data_s=arcr_workflow_data_s,
            arcr_initial_data=arcr_initial_data,
            arcr_object_insert_ref=arcr_object_insert_ref,
            arcr_translation_s=arcr_translation_s,
            arcr_control_vds_s=arcr_control_vds_s,
            arcr_note_delete=arcr_note_delete,
            arcr_document_feed=arcr_document_feed,
            arcr_object_delete_ref_s=arcr_object_delete_ref_s,
            arcr_basedata_verify=arcr_basedata_verify,
            arcr_swl_data_s=arcr_swl_data_s,
            arcr_swl_data=arcr_swl_data,
            arcr_object_delete_ref=arcr_object_delete_ref,
            arcr_document_data=arcr_document_data,
            arcr_object_relations=arcr_object_relations,
            arcr_object_replset=arcr_object_replset,
            arcr_broker_s=arcr_broker_s,
            arcr_document_status_s=arcr_document_status_s,
            arcr_object_keys=arcr_object_keys,
            arcr_action=arcr_action,
            arcr_user_data=arcr_user_data,
            param_swl_updated=param_swl_updated,
            arcr_signature_data_s=arcr_signature_data_s,
            arcr_document_data_s=arcr_document_data_s,
            arcr_object_keys_s=arcr_object_keys_s,
            arcr_document_switch_s=arcr_document_switch_s,
            arcr_document_status=arcr_document_status,
            arcr_document_feed_s=arcr_document_feed_s,
            arcr_object_delete_phys=arcr_object_delete_phys,
            arcr_signature_data=arcr_signature_data,
            arcr_basedata_verify_s=arcr_basedata_verify_s,
            arcr_user_delete=arcr_user_delete,
            arcr_trafo_s=arcr_trafo_s,
            arcr_set2=arcr_set2,
            arcr_broker=arcr_broker,
            arcr_object_replset_s=arcr_object_replset_s,
            arcr_object_delete_phys_s=arcr_object_delete_phys_s,
            arcr_set16=arcr_set16,
            arcr_map_changed=arcr_map_changed,
            arcr_marker=arcr_marker,
            arcr_document_switch=arcr_document_switch,
            arcr_workflow_data=arcr_workflow_data,
            arcr_object_hist_s=arcr_object_hist_s,
            arcr_trafo=arcr_trafo,
            arcr_document_insert_s=arcr_document_insert_s,
            arcr_map_changed_s=arcr_map_changed_s,
            arcr_user_data_s=arcr_user_data_s,
            arcr_document_insert=arcr_document_insert,
            arcr_extended_set=arcr_extended_set,
            arcr_version_comment_s=arcr_version_comment_s,
            arcr_marker_s=arcr_marker_s,
            arcr_ignore_broker_optz_s=arcr_ignore_broker_optz_s,
            arcr_attachment_data_s=arcr_attachment_data_s,
            arcr_docmasks_data=arcr_docmasks_data,
            arcr_object_insert_ref_s=arcr_object_insert_ref_s,
            arcr_link_s=arcr_link_s,
            arcr_control_vds=arcr_control_vds,
            arcr_action_s=arcr_action_s,
            arcr_object_relations_s=arcr_object_relations_s,
            arcr_docmask_delete=arcr_docmask_delete,
            arcr_initial_data_s=arcr_initial_data_s,
            arcr_translation=arcr_translation,
            param_swl_deleted=param_swl_deleted,
            arcr_object_hist=arcr_object_hist,
            arcr_link=arcr_link,
            arcr_version_comment=arcr_version_comment,
            arcr_docmasks_data_s=arcr_docmasks_data_s,
            arcr_user_delete_s=arcr_user_delete_s,
            arcr_note_data_s=arcr_note_data_s,
            arcr_object_data=arcr_object_data,
            arcr_note_data=arcr_note_data,
            arcr_note_delete_s=arcr_note_delete_s,
            arcr_attachment_data=arcr_attachment_data,
        )

        repl_code.additional_properties = d
        return repl_code

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
