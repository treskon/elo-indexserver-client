from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowActiveDocC")


@_attrs_define
class WorkFlowActiveDocC:
    """<p>
    Bit constants for members of WorkFlowActiveDoc
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_flow_id (Union[Unset, str]): DB column: wf_flowid
            mb_node_id (Union[Unset, str]): DB column: wf_nodeid
            mb_flow_name (Union[Unset, str]): DB column: wf_flow_name
            ln_flow_name (Union[Unset, int]): DB column: wf_flow_name
            mb_name (Union[Unset, str]): DB column: wf_name
            ln_name (Union[Unset, int]): DB column: wf_name
            mb_node_type (Union[Unset, str]): DB column: wf_node_type
            mb_department (Union[Unset, str]): DB column: wf_department
            mb_alert_to (Union[Unset, str]): DB column: wf_alert_to
            mb_alert_from_begin (Union[Unset, str]): DB column: wf_alert_from_begin
            mb_alert_wait (Union[Unset, str]): DB column: wf_alert_wait
            mb_yn_condition (Union[Unset, str]): DB column: wf_yesnocondition
            ln_yn_condition (Union[Unset, int]): DB column: wf_yesnocondition
            mb_condition (Union[Unset, str]): DB column: wf_condition
            ln_condition (Union[Unset, int]): DB column: wf_condition
            mb_comment (Union[Unset, str]): DB column: wf_comment
            ln_comment (Union[Unset, int]): DB column: wf_comment
            mb_locked (Union[Unset, str]): DB column: wf_locked
            mb_pos_x (Union[Unset, str]): DB column: pos_x
            mb_pos_y (Union[Unset, str]): DB column: pos_y
            mb_on_activate (Union[Unset, str]): DB column: wf_ev_on_activate
            ln_on_activate (Union[Unset, int]): DB column: wf_ev_on_activate
            mb_on_terminate (Union[Unset, str]): DB column: wf_ev_on_terminate
            ln_on_terminate (Union[Unset, int]): DB column: wf_ev_on_terminate
            mb_node_flags (Union[Unset, str]): DB column: wf_nodeflags
            mb_elo_obj_id (Union[Unset, str]): DB column: wf_eloobjid
            mb_lock_id (Union[Unset, str]): DB column: wf_locked_owner
            mb_is_next (Union[Unset, str]): DB column: wf_is_next
            mb_activate (Union[Unset, str]): DB column: wf_activate
            mb_terminate (Union[Unset, str]): DB column: wf_terminate
            mb_in_use_date (Union[Unset, str]): DB column: wf_in_use_date
            mb_completion_date (Union[Unset, str]): DB column: wf_completion_date
            mb_template_id (Union[Unset, str]): DB column: wf_template
            mb_user_terminate (Union[Unset, str]): DB column: wf_userterminate
            ln_user_terminate (Union[Unset, int]): DB column: wf_userterminate
            mb_tag (Union[Unset, str]): DB column: wf_tag
            mb_design_department (Union[Unset, str]): DB column: wf_designdepartment
            mb_move_cycle_pos_x (Union[Unset, str]): DB column: wf_dx
            mb_department_2 (Union[Unset, str]): DB column: wf_department2
            mb_delay_days (Union[Unset, str]): DB column: wf_delaydays
            mb_delay_date (Union[Unset, str]): DB column: wf_duedate
            mb_deleted (Union[Unset, str]): DB column: wf_deleted
            mb_prio (Union[Unset, str]): DB column: wf_prio
            mb_user_delay_date (Union[Unset, str]): Member bit: The workflow node is deferred until this date.
                DB column: wf_user_delaydate
            mb_version_id (Union[Unset, str]): Member bit: Version ID.
                DB column: wf_version
            mb_version_name (Union[Unset, str]): Member bit: Version comment.
                DB column: wf_version_name
            ln_version_name (Union[Unset, int]): Column length: Version comment.
                DB column: wf_version_name
            mb_alert_to_2 (Union[Unset, str]): Member bit: ID of user who should be informed, DB column: wf_alert_to2
            mb_alert_wait_2 (Union[Unset, str]): Member bit: Second Time-limit for a person node or begin node.
                DB column: wf_alert_wait2
            mb_alert_to_3 (Union[Unset, str]): Member bit: ID of user who should be informed, DB column: wf_alert_to3
            mb_alert_wait_3 (Union[Unset, str]): Member bit: Third Time-limit for a person node or begin node.
                DB column: wf_alert_wait3
            mb_next_server_id (Union[Unset, str]): Member bit: Next server name.
                This value is used in replication environments DB column: nextserverid
            ln_next_server_id (Union[Unset, int]): Column length: Next server name.
                This value is used in replication environments DB column: nextserverid
            mb_version_tag (Union[Unset, str]): Member bit: Version number.
                DB column: wf_version_tag
            ln_version_tag (Union[Unset, int]): Column length: Version number.
                DB column: wf_version_tag
            mb_version_user_id (Union[Unset, str]): Member bit: ID of the user who created the workflow version.
                DB column: wf_version_userid
            mb_version_create_date (Union[Unset, str]): Member bit: ID of the user who created the workflow version.
                DB column: wf_version_createdate
            mb_icon_id (Union[Unset, str]): Member bit: Object-GUID of an icon file that is displayed in the designer.
                DB column: wf_icon_guid
            ln_icon_id (Union[Unset, int]): Column length: Object-GUID of an icon file that is displayed in the designer.
                DB column: wf_icon_guid
            mb_form_spec (Union[Unset, str]): Member bit: User defined data to be stored in the database.
                DB column: wf_form_spec
            ln_form_spec (Union[Unset, int]): Column length: User defined data to be stored in the database.
                DB column: wf_form_spec
            mb_flow_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link WFDiagram#name}.
                DB column: wf_flownametrkey
            ln_flow_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link WFDiagram#name}.
                DB column: wf_flownametrkey
            mb_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link WFNode#name}.
                DB column: wf_nametrkey
            ln_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link WFNode#name}.
                DB column: wf_nametrkey
            mb_comment_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link WFNode#comment}.
                DB column: wf_commenttrkey
            ln_comment_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link WFNode#comment}.
                DB column: wf_commenttrkey
            mb_label (Union[Unset, str]): Member bit: Display name by forwarding.
                DB column: wf_label
            ln_label (Union[Unset, int]): Column length: Display name by forwarding.
                DB column: wf_label
            mb_properties (Union[Unset, str]): Member bit: Properties field of node.
                DB column: wf_properties
            ln_properties (Union[Unset, int]): Column length: Properties field of node.
                DB column: wf_properties
            mb_department_group (Union[Unset, str]): Member bit: Grouping of nodes for function takeWorkFlowNode.
                DB column: wf_departmentgroup
            mb_ret_val (Union[Unset, str]): Member bit: Return value of an end node.
                DB column: wf_retval
            mb_return_value (Union[Unset, str]): Member bit: Return value of an end node.
                DB column: wf_returnvalue
            ln_return_value (Union[Unset, int]): Column length: Return value of an end node.
                DB column: wf_returnvalue
            mb_sub_workflow (Union[Unset, str]): Member bit: ID of the active sub-workflow.
                DB column: wf_sub_wf
            mb_label_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link
                WorkFlowActiveDoc#label}.
                DB column: wf_labeltrkey
            ln_label_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link
                WorkFlowActiveDoc#label}.
                DB column: wf_labeltrkey
            mb_sub_workflow_template (Union[Unset, str]): Member bit: ID of the sub-workflow template.
                DB column: wf_sub_wf_templ
            mb_active_acl (Union[Unset, str]): Member bit: Contains the ACL of the workflow. Only valid for begin nodes.
                DB column: wf_active_acl
            ln_active_acl (Union[Unset, int]): Column length: Contains the ACL of the workflow. Only valid for begin nodes.
                DB column: wf_active_acl
            mb_package_name (Union[Unset, str]): Member bit: PackageName of a Workflow, only used for workflow templates DB
                column: packagename
            ln_package_name (Union[Unset, int]): Column length: PackageName of a Workflow, only used for workflow templates
                DB column: packagename
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_flow_id: Union[Unset, str] = UNSET
    mb_node_id: Union[Unset, str] = UNSET
    mb_flow_name: Union[Unset, str] = UNSET
    ln_flow_name: Union[Unset, int] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_node_type: Union[Unset, str] = UNSET
    mb_department: Union[Unset, str] = UNSET
    mb_alert_to: Union[Unset, str] = UNSET
    mb_alert_from_begin: Union[Unset, str] = UNSET
    mb_alert_wait: Union[Unset, str] = UNSET
    mb_yn_condition: Union[Unset, str] = UNSET
    ln_yn_condition: Union[Unset, int] = UNSET
    mb_condition: Union[Unset, str] = UNSET
    ln_condition: Union[Unset, int] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    mb_locked: Union[Unset, str] = UNSET
    mb_pos_x: Union[Unset, str] = UNSET
    mb_pos_y: Union[Unset, str] = UNSET
    mb_on_activate: Union[Unset, str] = UNSET
    ln_on_activate: Union[Unset, int] = UNSET
    mb_on_terminate: Union[Unset, str] = UNSET
    ln_on_terminate: Union[Unset, int] = UNSET
    mb_node_flags: Union[Unset, str] = UNSET
    mb_elo_obj_id: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_is_next: Union[Unset, str] = UNSET
    mb_activate: Union[Unset, str] = UNSET
    mb_terminate: Union[Unset, str] = UNSET
    mb_in_use_date: Union[Unset, str] = UNSET
    mb_completion_date: Union[Unset, str] = UNSET
    mb_template_id: Union[Unset, str] = UNSET
    mb_user_terminate: Union[Unset, str] = UNSET
    ln_user_terminate: Union[Unset, int] = UNSET
    mb_tag: Union[Unset, str] = UNSET
    mb_design_department: Union[Unset, str] = UNSET
    mb_move_cycle_pos_x: Union[Unset, str] = UNSET
    mb_department_2: Union[Unset, str] = UNSET
    mb_delay_days: Union[Unset, str] = UNSET
    mb_delay_date: Union[Unset, str] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_user_delay_date: Union[Unset, str] = UNSET
    mb_version_id: Union[Unset, str] = UNSET
    mb_version_name: Union[Unset, str] = UNSET
    ln_version_name: Union[Unset, int] = UNSET
    mb_alert_to_2: Union[Unset, str] = UNSET
    mb_alert_wait_2: Union[Unset, str] = UNSET
    mb_alert_to_3: Union[Unset, str] = UNSET
    mb_alert_wait_3: Union[Unset, str] = UNSET
    mb_next_server_id: Union[Unset, str] = UNSET
    ln_next_server_id: Union[Unset, int] = UNSET
    mb_version_tag: Union[Unset, str] = UNSET
    ln_version_tag: Union[Unset, int] = UNSET
    mb_version_user_id: Union[Unset, str] = UNSET
    mb_version_create_date: Union[Unset, str] = UNSET
    mb_icon_id: Union[Unset, str] = UNSET
    ln_icon_id: Union[Unset, int] = UNSET
    mb_form_spec: Union[Unset, str] = UNSET
    ln_form_spec: Union[Unset, int] = UNSET
    mb_flow_name_translation_key: Union[Unset, str] = UNSET
    ln_flow_name_translation_key: Union[Unset, int] = UNSET
    mb_name_translation_key: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    mb_comment_translation_key: Union[Unset, str] = UNSET
    ln_comment_translation_key: Union[Unset, int] = UNSET
    mb_label: Union[Unset, str] = UNSET
    ln_label: Union[Unset, int] = UNSET
    mb_properties: Union[Unset, str] = UNSET
    ln_properties: Union[Unset, int] = UNSET
    mb_department_group: Union[Unset, str] = UNSET
    mb_ret_val: Union[Unset, str] = UNSET
    mb_return_value: Union[Unset, str] = UNSET
    ln_return_value: Union[Unset, int] = UNSET
    mb_sub_workflow: Union[Unset, str] = UNSET
    mb_label_translation_key: Union[Unset, str] = UNSET
    ln_label_translation_key: Union[Unset, int] = UNSET
    mb_sub_workflow_template: Union[Unset, str] = UNSET
    mb_active_acl: Union[Unset, str] = UNSET
    ln_active_acl: Union[Unset, int] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_flow_id = self.mb_flow_id
        mb_node_id = self.mb_node_id
        mb_flow_name = self.mb_flow_name
        ln_flow_name = self.ln_flow_name
        mb_name = self.mb_name
        ln_name = self.ln_name
        mb_node_type = self.mb_node_type
        mb_department = self.mb_department
        mb_alert_to = self.mb_alert_to
        mb_alert_from_begin = self.mb_alert_from_begin
        mb_alert_wait = self.mb_alert_wait
        mb_yn_condition = self.mb_yn_condition
        ln_yn_condition = self.ln_yn_condition
        mb_condition = self.mb_condition
        ln_condition = self.ln_condition
        mb_comment = self.mb_comment
        ln_comment = self.ln_comment
        mb_locked = self.mb_locked
        mb_pos_x = self.mb_pos_x
        mb_pos_y = self.mb_pos_y
        mb_on_activate = self.mb_on_activate
        ln_on_activate = self.ln_on_activate
        mb_on_terminate = self.mb_on_terminate
        ln_on_terminate = self.ln_on_terminate
        mb_node_flags = self.mb_node_flags
        mb_elo_obj_id = self.mb_elo_obj_id
        mb_lock_id = self.mb_lock_id
        mb_is_next = self.mb_is_next
        mb_activate = self.mb_activate
        mb_terminate = self.mb_terminate
        mb_in_use_date = self.mb_in_use_date
        mb_completion_date = self.mb_completion_date
        mb_template_id = self.mb_template_id
        mb_user_terminate = self.mb_user_terminate
        ln_user_terminate = self.ln_user_terminate
        mb_tag = self.mb_tag
        mb_design_department = self.mb_design_department
        mb_move_cycle_pos_x = self.mb_move_cycle_pos_x
        mb_department_2 = self.mb_department_2
        mb_delay_days = self.mb_delay_days
        mb_delay_date = self.mb_delay_date
        mb_deleted = self.mb_deleted
        mb_prio = self.mb_prio
        mb_user_delay_date = self.mb_user_delay_date
        mb_version_id = self.mb_version_id
        mb_version_name = self.mb_version_name
        ln_version_name = self.ln_version_name
        mb_alert_to_2 = self.mb_alert_to_2
        mb_alert_wait_2 = self.mb_alert_wait_2
        mb_alert_to_3 = self.mb_alert_to_3
        mb_alert_wait_3 = self.mb_alert_wait_3
        mb_next_server_id = self.mb_next_server_id
        ln_next_server_id = self.ln_next_server_id
        mb_version_tag = self.mb_version_tag
        ln_version_tag = self.ln_version_tag
        mb_version_user_id = self.mb_version_user_id
        mb_version_create_date = self.mb_version_create_date
        mb_icon_id = self.mb_icon_id
        ln_icon_id = self.ln_icon_id
        mb_form_spec = self.mb_form_spec
        ln_form_spec = self.ln_form_spec
        mb_flow_name_translation_key = self.mb_flow_name_translation_key
        ln_flow_name_translation_key = self.ln_flow_name_translation_key
        mb_name_translation_key = self.mb_name_translation_key
        ln_name_translation_key = self.ln_name_translation_key
        mb_comment_translation_key = self.mb_comment_translation_key
        ln_comment_translation_key = self.ln_comment_translation_key
        mb_label = self.mb_label
        ln_label = self.ln_label
        mb_properties = self.mb_properties
        ln_properties = self.ln_properties
        mb_department_group = self.mb_department_group
        mb_ret_val = self.mb_ret_val
        mb_return_value = self.mb_return_value
        ln_return_value = self.ln_return_value
        mb_sub_workflow = self.mb_sub_workflow
        mb_label_translation_key = self.mb_label_translation_key
        ln_label_translation_key = self.ln_label_translation_key
        mb_sub_workflow_template = self.mb_sub_workflow_template
        mb_active_acl = self.mb_active_acl
        ln_active_acl = self.ln_active_acl
        mb_package_name = self.mb_package_name
        ln_package_name = self.ln_package_name
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_flow_id is not UNSET:
            field_dict["mbFlowId"] = mb_flow_id
        if mb_node_id is not UNSET:
            field_dict["mbNodeId"] = mb_node_id
        if mb_flow_name is not UNSET:
            field_dict["mbFlowName"] = mb_flow_name
        if ln_flow_name is not UNSET:
            field_dict["lnFlowName"] = ln_flow_name
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_node_type is not UNSET:
            field_dict["mbNodeType"] = mb_node_type
        if mb_department is not UNSET:
            field_dict["mbDepartment"] = mb_department
        if mb_alert_to is not UNSET:
            field_dict["mbAlertTo"] = mb_alert_to
        if mb_alert_from_begin is not UNSET:
            field_dict["mbAlertFromBegin"] = mb_alert_from_begin
        if mb_alert_wait is not UNSET:
            field_dict["mbAlertWait"] = mb_alert_wait
        if mb_yn_condition is not UNSET:
            field_dict["mbYNCondition"] = mb_yn_condition
        if ln_yn_condition is not UNSET:
            field_dict["lnYNCondition"] = ln_yn_condition
        if mb_condition is not UNSET:
            field_dict["mbCondition"] = mb_condition
        if ln_condition is not UNSET:
            field_dict["lnCondition"] = ln_condition
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if mb_locked is not UNSET:
            field_dict["mbLocked"] = mb_locked
        if mb_pos_x is not UNSET:
            field_dict["mbPosX"] = mb_pos_x
        if mb_pos_y is not UNSET:
            field_dict["mbPosY"] = mb_pos_y
        if mb_on_activate is not UNSET:
            field_dict["mbOnActivate"] = mb_on_activate
        if ln_on_activate is not UNSET:
            field_dict["lnOnActivate"] = ln_on_activate
        if mb_on_terminate is not UNSET:
            field_dict["mbOnTerminate"] = mb_on_terminate
        if ln_on_terminate is not UNSET:
            field_dict["lnOnTerminate"] = ln_on_terminate
        if mb_node_flags is not UNSET:
            field_dict["mbNodeFlags"] = mb_node_flags
        if mb_elo_obj_id is not UNSET:
            field_dict["mbEloObjId"] = mb_elo_obj_id
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_is_next is not UNSET:
            field_dict["mbIsNext"] = mb_is_next
        if mb_activate is not UNSET:
            field_dict["mbActivate"] = mb_activate
        if mb_terminate is not UNSET:
            field_dict["mbTerminate"] = mb_terminate
        if mb_in_use_date is not UNSET:
            field_dict["mbInUseDate"] = mb_in_use_date
        if mb_completion_date is not UNSET:
            field_dict["mbCompletionDate"] = mb_completion_date
        if mb_template_id is not UNSET:
            field_dict["mbTemplateId"] = mb_template_id
        if mb_user_terminate is not UNSET:
            field_dict["mbUserTerminate"] = mb_user_terminate
        if ln_user_terminate is not UNSET:
            field_dict["lnUserTerminate"] = ln_user_terminate
        if mb_tag is not UNSET:
            field_dict["mbTag"] = mb_tag
        if mb_design_department is not UNSET:
            field_dict["mbDesignDepartment"] = mb_design_department
        if mb_move_cycle_pos_x is not UNSET:
            field_dict["mbMoveCyclePosX"] = mb_move_cycle_pos_x
        if mb_department_2 is not UNSET:
            field_dict["mbDepartment2"] = mb_department_2
        if mb_delay_days is not UNSET:
            field_dict["mbDelayDays"] = mb_delay_days
        if mb_delay_date is not UNSET:
            field_dict["mbDelayDate"] = mb_delay_date
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_user_delay_date is not UNSET:
            field_dict["mbUserDelayDate"] = mb_user_delay_date
        if mb_version_id is not UNSET:
            field_dict["mbVersionId"] = mb_version_id
        if mb_version_name is not UNSET:
            field_dict["mbVersionName"] = mb_version_name
        if ln_version_name is not UNSET:
            field_dict["lnVersionName"] = ln_version_name
        if mb_alert_to_2 is not UNSET:
            field_dict["mbAlertTo2"] = mb_alert_to_2
        if mb_alert_wait_2 is not UNSET:
            field_dict["mbAlertWait2"] = mb_alert_wait_2
        if mb_alert_to_3 is not UNSET:
            field_dict["mbAlertTo3"] = mb_alert_to_3
        if mb_alert_wait_3 is not UNSET:
            field_dict["mbAlertWait3"] = mb_alert_wait_3
        if mb_next_server_id is not UNSET:
            field_dict["mbNextServerId"] = mb_next_server_id
        if ln_next_server_id is not UNSET:
            field_dict["lnNextServerId"] = ln_next_server_id
        if mb_version_tag is not UNSET:
            field_dict["mbVersionTag"] = mb_version_tag
        if ln_version_tag is not UNSET:
            field_dict["lnVersionTag"] = ln_version_tag
        if mb_version_user_id is not UNSET:
            field_dict["mbVersionUserId"] = mb_version_user_id
        if mb_version_create_date is not UNSET:
            field_dict["mbVersionCreateDate"] = mb_version_create_date
        if mb_icon_id is not UNSET:
            field_dict["mbIconId"] = mb_icon_id
        if ln_icon_id is not UNSET:
            field_dict["lnIconId"] = ln_icon_id
        if mb_form_spec is not UNSET:
            field_dict["mbFormSpec"] = mb_form_spec
        if ln_form_spec is not UNSET:
            field_dict["lnFormSpec"] = ln_form_spec
        if mb_flow_name_translation_key is not UNSET:
            field_dict["mbFlowNameTranslationKey"] = mb_flow_name_translation_key
        if ln_flow_name_translation_key is not UNSET:
            field_dict["lnFlowNameTranslationKey"] = ln_flow_name_translation_key
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if mb_comment_translation_key is not UNSET:
            field_dict["mbCommentTranslationKey"] = mb_comment_translation_key
        if ln_comment_translation_key is not UNSET:
            field_dict["lnCommentTranslationKey"] = ln_comment_translation_key
        if mb_label is not UNSET:
            field_dict["mbLabel"] = mb_label
        if ln_label is not UNSET:
            field_dict["lnLabel"] = ln_label
        if mb_properties is not UNSET:
            field_dict["mbProperties"] = mb_properties
        if ln_properties is not UNSET:
            field_dict["lnProperties"] = ln_properties
        if mb_department_group is not UNSET:
            field_dict["mbDepartmentGroup"] = mb_department_group
        if mb_ret_val is not UNSET:
            field_dict["mbRetVal"] = mb_ret_val
        if mb_return_value is not UNSET:
            field_dict["mbReturnValue"] = mb_return_value
        if ln_return_value is not UNSET:
            field_dict["lnReturnValue"] = ln_return_value
        if mb_sub_workflow is not UNSET:
            field_dict["mbSubWorkflow"] = mb_sub_workflow
        if mb_label_translation_key is not UNSET:
            field_dict["mbLabelTranslationKey"] = mb_label_translation_key
        if ln_label_translation_key is not UNSET:
            field_dict["lnLabelTranslationKey"] = ln_label_translation_key
        if mb_sub_workflow_template is not UNSET:
            field_dict["mbSubWorkflowTemplate"] = mb_sub_workflow_template
        if mb_active_acl is not UNSET:
            field_dict["mbActiveAcl"] = mb_active_acl
        if ln_active_acl is not UNSET:
            field_dict["lnActiveAcl"] = ln_active_acl
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_flow_id = d.pop("mbFlowId", UNSET)

        mb_node_id = d.pop("mbNodeId", UNSET)

        mb_flow_name = d.pop("mbFlowName", UNSET)

        ln_flow_name = d.pop("lnFlowName", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_node_type = d.pop("mbNodeType", UNSET)

        mb_department = d.pop("mbDepartment", UNSET)

        mb_alert_to = d.pop("mbAlertTo", UNSET)

        mb_alert_from_begin = d.pop("mbAlertFromBegin", UNSET)

        mb_alert_wait = d.pop("mbAlertWait", UNSET)

        mb_yn_condition = d.pop("mbYNCondition", UNSET)

        ln_yn_condition = d.pop("lnYNCondition", UNSET)

        mb_condition = d.pop("mbCondition", UNSET)

        ln_condition = d.pop("lnCondition", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        mb_locked = d.pop("mbLocked", UNSET)

        mb_pos_x = d.pop("mbPosX", UNSET)

        mb_pos_y = d.pop("mbPosY", UNSET)

        mb_on_activate = d.pop("mbOnActivate", UNSET)

        ln_on_activate = d.pop("lnOnActivate", UNSET)

        mb_on_terminate = d.pop("mbOnTerminate", UNSET)

        ln_on_terminate = d.pop("lnOnTerminate", UNSET)

        mb_node_flags = d.pop("mbNodeFlags", UNSET)

        mb_elo_obj_id = d.pop("mbEloObjId", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_is_next = d.pop("mbIsNext", UNSET)

        mb_activate = d.pop("mbActivate", UNSET)

        mb_terminate = d.pop("mbTerminate", UNSET)

        mb_in_use_date = d.pop("mbInUseDate", UNSET)

        mb_completion_date = d.pop("mbCompletionDate", UNSET)

        mb_template_id = d.pop("mbTemplateId", UNSET)

        mb_user_terminate = d.pop("mbUserTerminate", UNSET)

        ln_user_terminate = d.pop("lnUserTerminate", UNSET)

        mb_tag = d.pop("mbTag", UNSET)

        mb_design_department = d.pop("mbDesignDepartment", UNSET)

        mb_move_cycle_pos_x = d.pop("mbMoveCyclePosX", UNSET)

        mb_department_2 = d.pop("mbDepartment2", UNSET)

        mb_delay_days = d.pop("mbDelayDays", UNSET)

        mb_delay_date = d.pop("mbDelayDate", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_user_delay_date = d.pop("mbUserDelayDate", UNSET)

        mb_version_id = d.pop("mbVersionId", UNSET)

        mb_version_name = d.pop("mbVersionName", UNSET)

        ln_version_name = d.pop("lnVersionName", UNSET)

        mb_alert_to_2 = d.pop("mbAlertTo2", UNSET)

        mb_alert_wait_2 = d.pop("mbAlertWait2", UNSET)

        mb_alert_to_3 = d.pop("mbAlertTo3", UNSET)

        mb_alert_wait_3 = d.pop("mbAlertWait3", UNSET)

        mb_next_server_id = d.pop("mbNextServerId", UNSET)

        ln_next_server_id = d.pop("lnNextServerId", UNSET)

        mb_version_tag = d.pop("mbVersionTag", UNSET)

        ln_version_tag = d.pop("lnVersionTag", UNSET)

        mb_version_user_id = d.pop("mbVersionUserId", UNSET)

        mb_version_create_date = d.pop("mbVersionCreateDate", UNSET)

        mb_icon_id = d.pop("mbIconId", UNSET)

        ln_icon_id = d.pop("lnIconId", UNSET)

        mb_form_spec = d.pop("mbFormSpec", UNSET)

        ln_form_spec = d.pop("lnFormSpec", UNSET)

        mb_flow_name_translation_key = d.pop("mbFlowNameTranslationKey", UNSET)

        ln_flow_name_translation_key = d.pop("lnFlowNameTranslationKey", UNSET)

        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        mb_comment_translation_key = d.pop("mbCommentTranslationKey", UNSET)

        ln_comment_translation_key = d.pop("lnCommentTranslationKey", UNSET)

        mb_label = d.pop("mbLabel", UNSET)

        ln_label = d.pop("lnLabel", UNSET)

        mb_properties = d.pop("mbProperties", UNSET)

        ln_properties = d.pop("lnProperties", UNSET)

        mb_department_group = d.pop("mbDepartmentGroup", UNSET)

        mb_ret_val = d.pop("mbRetVal", UNSET)

        mb_return_value = d.pop("mbReturnValue", UNSET)

        ln_return_value = d.pop("lnReturnValue", UNSET)

        mb_sub_workflow = d.pop("mbSubWorkflow", UNSET)

        mb_label_translation_key = d.pop("mbLabelTranslationKey", UNSET)

        ln_label_translation_key = d.pop("lnLabelTranslationKey", UNSET)

        mb_sub_workflow_template = d.pop("mbSubWorkflowTemplate", UNSET)

        mb_active_acl = d.pop("mbActiveAcl", UNSET)

        ln_active_acl = d.pop("lnActiveAcl", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        work_flow_active_doc_c = cls(
            mb_flow_id=mb_flow_id,
            mb_node_id=mb_node_id,
            mb_flow_name=mb_flow_name,
            ln_flow_name=ln_flow_name,
            mb_name=mb_name,
            ln_name=ln_name,
            mb_node_type=mb_node_type,
            mb_department=mb_department,
            mb_alert_to=mb_alert_to,
            mb_alert_from_begin=mb_alert_from_begin,
            mb_alert_wait=mb_alert_wait,
            mb_yn_condition=mb_yn_condition,
            ln_yn_condition=ln_yn_condition,
            mb_condition=mb_condition,
            ln_condition=ln_condition,
            mb_comment=mb_comment,
            ln_comment=ln_comment,
            mb_locked=mb_locked,
            mb_pos_x=mb_pos_x,
            mb_pos_y=mb_pos_y,
            mb_on_activate=mb_on_activate,
            ln_on_activate=ln_on_activate,
            mb_on_terminate=mb_on_terminate,
            ln_on_terminate=ln_on_terminate,
            mb_node_flags=mb_node_flags,
            mb_elo_obj_id=mb_elo_obj_id,
            mb_lock_id=mb_lock_id,
            mb_is_next=mb_is_next,
            mb_activate=mb_activate,
            mb_terminate=mb_terminate,
            mb_in_use_date=mb_in_use_date,
            mb_completion_date=mb_completion_date,
            mb_template_id=mb_template_id,
            mb_user_terminate=mb_user_terminate,
            ln_user_terminate=ln_user_terminate,
            mb_tag=mb_tag,
            mb_design_department=mb_design_department,
            mb_move_cycle_pos_x=mb_move_cycle_pos_x,
            mb_department_2=mb_department_2,
            mb_delay_days=mb_delay_days,
            mb_delay_date=mb_delay_date,
            mb_deleted=mb_deleted,
            mb_prio=mb_prio,
            mb_user_delay_date=mb_user_delay_date,
            mb_version_id=mb_version_id,
            mb_version_name=mb_version_name,
            ln_version_name=ln_version_name,
            mb_alert_to_2=mb_alert_to_2,
            mb_alert_wait_2=mb_alert_wait_2,
            mb_alert_to_3=mb_alert_to_3,
            mb_alert_wait_3=mb_alert_wait_3,
            mb_next_server_id=mb_next_server_id,
            ln_next_server_id=ln_next_server_id,
            mb_version_tag=mb_version_tag,
            ln_version_tag=ln_version_tag,
            mb_version_user_id=mb_version_user_id,
            mb_version_create_date=mb_version_create_date,
            mb_icon_id=mb_icon_id,
            ln_icon_id=ln_icon_id,
            mb_form_spec=mb_form_spec,
            ln_form_spec=ln_form_spec,
            mb_flow_name_translation_key=mb_flow_name_translation_key,
            ln_flow_name_translation_key=ln_flow_name_translation_key,
            mb_name_translation_key=mb_name_translation_key,
            ln_name_translation_key=ln_name_translation_key,
            mb_comment_translation_key=mb_comment_translation_key,
            ln_comment_translation_key=ln_comment_translation_key,
            mb_label=mb_label,
            ln_label=ln_label,
            mb_properties=mb_properties,
            ln_properties=ln_properties,
            mb_department_group=mb_department_group,
            mb_ret_val=mb_ret_val,
            mb_return_value=mb_return_value,
            ln_return_value=ln_return_value,
            mb_sub_workflow=mb_sub_workflow,
            mb_label_translation_key=mb_label_translation_key,
            ln_label_translation_key=ln_label_translation_key,
            mb_sub_workflow_template=mb_sub_workflow_template,
            mb_active_acl=mb_active_acl,
            ln_active_acl=ln_active_acl,
            mb_package_name=mb_package_name,
            ln_package_name=ln_package_name,
            mb_all_members=mb_all_members,
        )

        work_flow_active_doc_c.additional_properties = d
        return work_flow_active_doc_c

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
