from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_node_z import WFNodeZ


T = TypeVar("T", bound="WFNodeC")


@_attrs_define
class WFNodeC:
    """<p>
    Constants for <code>WorkFlowNode</code>.
     </p>

        Attributes:
            mb_ret_val (Union[Unset, str]): Member bit: retVal
            deactivate_all_preds (Union[Unset, str]): Indicates that all predecessor of the collect node should be
                terminated.
            type_collectnode (Union[Unset, int]): Node type: Collects many workflow paths.
            ln_comment (Union[Unset, int]): Maximum length of comment.
            mb_in_use_date_iso (Union[Unset, str]):
            flag_not_valid (Union[Unset, int]): Node flag: Not released.
                A personal node of an Adhoc workflow has this flag set, if the user
                 has not released the node. The Indexserver does not use this flag anywhere.
            mb_exit_date_iso (Union[Unset, str]):
            type_call_sub_workflow (Union[Unset, int]): Note type: Call sub workflow.
            mb_sub_template_id (Union[Unset, str]): Member bit: subTemplateId
            ln_yes_no_condition (Union[Unset, int]):
            mb_user_terminate (Union[Unset, str]): Member bit: The ID of the user who has forwarded the node. Not valid for
                template workflows.
                Only valid for person nodes. DB column: wf_userterminate
            flag_delegated (Union[Unset, int]): Node flag: This flag indicates whether the person node was delegated.
                This flag is only used
                 for the person node.
            mb_department_2 (Union[Unset, str]): Member bit: A group ID to constrain access to the node.
                Only members of this group are allowed
                 to see and process the node. Only valid for person nodes. DB column: wf_department2
            flag_error (Union[Unset, int]): Node flag: This flag indicates that this node is an error node, which is
                generated after an
                error occurred while executing the plugin node.
            mb_pos_y (Union[Unset, str]): Member bit: y position in designer view.
            mb_pos_x (Union[Unset, str]): Member bit: x position in designer view.
            mb_nb_of_dones_to_exit (Union[Unset, str]): Member bit: number of predecessor nodes that must be processed to
                forward this node.
            ln_on_enter (Union[Unset, int]):
            ln_form_spec (Union[Unset, int]): Maximum length of form spec.
            mb_script_names (Union[Unset, str]): Member bit: scriptNames
            mb_is_next (Union[Unset, str]): Member bit: (to be defined)
            flag_workingdays (Union[Unset, int]): Node flag: This flag indicates that weekend days should be skipped when
                evaluating time limits.
            mb_comment (Union[Unset, str]): Member bit: Node comment.
            ln_on_exit_handle_rollback (Union[Unset, int]):
            flag_hidden (Union[Unset, int]): Node flag: Hide this workflow from default searches and listings.
            mb_name (Union[Unset, str]): Member bit: Name
            mb_delay_date (Union[Unset, str]): Member bit: DelayDaye. Not valid for template workflows. Only valid for
                person nodes.
                DB
                 column: wf_duedate
            mb_enter_date (Union[Unset, str]): Member bit: Activated at this date.
            mb_icon_id (Union[Unset, str]): Member bit: Icon GUID.
            flag_resetadhocnode (Union[Unset, int]): Node flag: Reset all person nodes. This flag is only used for parallel
                for validation workflow.
            ln_name (Union[Unset, int]): Maximum length of node name.
            mb_department_group (Union[Unset, str]): Member bit: departmentGroup
            ln_on_exit (Union[Unset, int]):
            mb_prio (Union[Unset, str]): Member bit: returnValue
            mb_return_value (Union[Unset, str]): Member bit: returnValue
            mb_sub_template_name (Union[Unset, str]): reserved.
            ln_on_enter_handle_rollback (Union[Unset, int]):
            flag_copy_children (Union[Unset, int]): Node flag: This flag indicates that all nodes in the cycle should be
                copied when entering the
                begin cycle node. This flag is only used for the begin cycle node.
            mb_comment_translation_key (Union[Unset, str]): Member bit: CommentTranslationKey
            mb_exit_date (Union[Unset, str]): Member bit: Leaved at this date.
            mb_lock_id (Union[Unset, str]): Member bit: locked from user.
            mb_sub_flow_id (Union[Unset, str]): Member bit: subFlowId
            mb_properties (Union[Unset, str]): Member bit: properties
            type_pluginnode (Union[Unset, int]): Note type: Plugin node.
                This node is intended to trigger external events or to address external
                 systems. OnEnter is handled synchronously. It waits for a result of the event. OnExit is
                 handled asynchronously. The WF continues without waiting for the event. DB transaction is
                 terminated before OnEnter is executed.
            flag_terminate_user (Union[Unset, int]): Node flag: End of workflow. This flag is set to the end node of an
                Adhoc workflow.
                The
                 Indexserver does not need this flag but maybe the ELO Windows Client.
            type_set_server_id (Union[Unset, int]): Note type: Set the server ID where the WF can be continued.
                This node is used in replicated
                 workflows.
            ln_properties (Union[Unset, int]): Maximum length of the properties.
            mb_name_translation_key (Union[Unset, str]): Member bit: NameTranslationKey
            flag_do_not_start_manually (Union[Unset, int]): Node flag: This flag indicates whether the sub workflow can be
                started manually.
                The sub
                 workflow of. This flag is used for sub workflows.
            mb_on_exit (Union[Unset, str]): Member bit: script to execute when node is leaved.
            mb_design_department (Union[Unset, str]): Member bit: A group ID or user ID that was originally assigned in the
                designer.
                DB column:
                 wf_designdepartment
            flag_root_adhoc (Union[Unset, int]): Node flag: The start node of an Adhoc workflow has this flag.
            mb_delay_days (Union[Unset, str]): Member bit: An active person node (Activate is set) might be displayed to the
                user delayed by
                this number of days. Only valid for person nodes. DB column: wf_deldays
            ln_condition (Union[Unset, int]):
            mb_condition (Union[Unset, str]): Member bit: condition, is only internally used
            ln_label (Union[Unset, int]): Maximum length of the label.
            mb_id (Union[Unset, str]): Member bit: Node ID
            mb_move_cycle_pos_x (Union[Unset, str]): Member bit: If a cycle is re-entered, the nodes in the cycle are
                duplicated.
                The copied nodes
                 will be placed in the designer moved by this value to the right. If this value is 0, the nodes
                 are moved 60 points right and 20 points up. DB column: wf_dx
            mb_result (Union[Unset, str]): Member bit: Condition result.
            userid_superior (Union[Unset, int]): This ID is a placeholder for the superior of the workflow owner.
            mb_user_id (Union[Unset, str]): Member bit: User ID
            type_beginnode (Union[Unset, int]): Node type: Start of workflow.
            userid_ignore (Union[Unset, int]): This value can be used in Node.department2 to make clear, that Node.
                department2 has to be
                 ignored.
            mb_delay_date_iso (Union[Unset, str]):
            mb_user_delay_date (Union[Unset, str]): Member bit: UserDelayDate. Not valid for template workflows. Only valid
                for person nodes.
                DB
                 column: wf_duedate
            mb_flags (Union[Unset, str]): Member bit: control flags.
            mb_on_exit_handle_rollback (Union[Unset, str]): Member bit: script to execute when node encounters an error.
            mb_yes_no_condition (Union[Unset, str]): Member bit: yes/no condition
            mb_enter_date_iso (Union[Unset, str]):
            mb_label (Union[Unset, str]): Member bit: label
            ln_comment_translation_key (Union[Unset, int]): Maximum length of the comment's translation key.
            type_cycle (Union[Unset, int]): Node type: Cycle Cycle nodes are contained in pairs in a workflow.
                One cycle node denotes the
                 beginning of a cycle and an associated cycle node marks the end. Both cycle nodes must have the
                 same name (WFNode.name). The begin node must be flagged with FLAG_CYCLE_END.
            mb_process_on_server_id (Union[Unset, str]): Member bit: processOnServerId;
            mb_user_name (Union[Unset, str]):
            type_personnode (Union[Unset, int]): Node type: Personal node. A user must edit the node to continue the
                workflow.
            flag_reset_children (Union[Unset, int]): Node flag: Reset the ExitDate of the following nodes, if this node is
                activated.
            type_splitnode (Union[Unset, int]): Node type: Distribute to many following nodes.
            flag_one_successor (Union[Unset, int]): Node flag: Only one user can receive this node.
            ln_name_translation_key (Union[Unset, int]): Maximum length of the name's translation key.
            flag_cycle_x (Union[Unset, int]): Node flag: This is a copied start node of a cylce. Do not use this flag in
                workflow templates.
                The workflow engine will mark copied cycle. nodes with this flag.
            mb_time_limit_iso (Union[Unset, str]):
            mb_time_limit (Union[Unset, str]): Member bit: (to be defined)
            mb_all_members (Union[Unset, str]): All members.
            mb_form_spec (Union[Unset, str]): Member bit: FormSpec.
            mb_time_limit_escalations (Union[Unset, str]): Member bit: timeLimitEscalation
            mb_on_enter_handle_rollback (Union[Unset, str]): Member bit: script to execute when node encounters an error.
            flag_cycle_end (Union[Unset, int]): Node flag: This flag denotes, whether a cycle node (TYPE_CYCLE) is the end
                of a cycle.
            type_nothing (Union[Unset, int]): Node type: undefined or deleted
            mb_all (Union[Unset, WFNodeZ]): This class encapsulates the constants of the WFNodeC class.
                <p>
                 Copyright: Copyright (c) 2011
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_type (Union[Unset, str]): Member bit: Type
            ln_label_translation_key (Union[Unset, int]): Maximum length of the labelTranslationKey.
            type_ifnode (Union[Unset, int]): Node type: Decision node.
            mb_tag (Union[Unset, str]): Member bit: reserved.
                DB column: wf_tag
            mb_label_translation_key (Union[Unset, str]): Member bit: labelTranslationKey
            mb_user_delay_date_iso (Union[Unset, str]):
            userid_owner (Union[Unset, int]): Set WFNode.
                userId to this value, if a workflow node should belong to the user who starts the
                 workflow.
            mb_on_enter (Union[Unset, str]): Member bit: script to execute when node is activated.
            type_endnode (Union[Unset, int]): Node type: End of workflow.
            ln_process_on_server_id (Union[Unset, int]): Maximum length of processOnServerId.
            mb_obj_key_names (Union[Unset, str]): Member bit: objKeyNames
            mb_in_use_date (Union[Unset, str]): Member bit: In use at this date.
    """

    mb_ret_val: Union[Unset, str] = UNSET
    deactivate_all_preds: Union[Unset, str] = UNSET
    type_collectnode: Union[Unset, int] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    mb_in_use_date_iso: Union[Unset, str] = UNSET
    flag_not_valid: Union[Unset, int] = UNSET
    mb_exit_date_iso: Union[Unset, str] = UNSET
    type_call_sub_workflow: Union[Unset, int] = UNSET
    mb_sub_template_id: Union[Unset, str] = UNSET
    ln_yes_no_condition: Union[Unset, int] = UNSET
    mb_user_terminate: Union[Unset, str] = UNSET
    flag_delegated: Union[Unset, int] = UNSET
    mb_department_2: Union[Unset, str] = UNSET
    flag_error: Union[Unset, int] = UNSET
    mb_pos_y: Union[Unset, str] = UNSET
    mb_pos_x: Union[Unset, str] = UNSET
    mb_nb_of_dones_to_exit: Union[Unset, str] = UNSET
    ln_on_enter: Union[Unset, int] = UNSET
    ln_form_spec: Union[Unset, int] = UNSET
    mb_script_names: Union[Unset, str] = UNSET
    mb_is_next: Union[Unset, str] = UNSET
    flag_workingdays: Union[Unset, int] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    ln_on_exit_handle_rollback: Union[Unset, int] = UNSET
    flag_hidden: Union[Unset, int] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_delay_date: Union[Unset, str] = UNSET
    mb_enter_date: Union[Unset, str] = UNSET
    mb_icon_id: Union[Unset, str] = UNSET
    flag_resetadhocnode: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_department_group: Union[Unset, str] = UNSET
    ln_on_exit: Union[Unset, int] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_return_value: Union[Unset, str] = UNSET
    mb_sub_template_name: Union[Unset, str] = UNSET
    ln_on_enter_handle_rollback: Union[Unset, int] = UNSET
    flag_copy_children: Union[Unset, int] = UNSET
    mb_comment_translation_key: Union[Unset, str] = UNSET
    mb_exit_date: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_sub_flow_id: Union[Unset, str] = UNSET
    mb_properties: Union[Unset, str] = UNSET
    type_pluginnode: Union[Unset, int] = UNSET
    flag_terminate_user: Union[Unset, int] = UNSET
    type_set_server_id: Union[Unset, int] = UNSET
    ln_properties: Union[Unset, int] = UNSET
    mb_name_translation_key: Union[Unset, str] = UNSET
    flag_do_not_start_manually: Union[Unset, int] = UNSET
    mb_on_exit: Union[Unset, str] = UNSET
    mb_design_department: Union[Unset, str] = UNSET
    flag_root_adhoc: Union[Unset, int] = UNSET
    mb_delay_days: Union[Unset, str] = UNSET
    ln_condition: Union[Unset, int] = UNSET
    mb_condition: Union[Unset, str] = UNSET
    ln_label: Union[Unset, int] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_move_cycle_pos_x: Union[Unset, str] = UNSET
    mb_result: Union[Unset, str] = UNSET
    userid_superior: Union[Unset, int] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    type_beginnode: Union[Unset, int] = UNSET
    userid_ignore: Union[Unset, int] = UNSET
    mb_delay_date_iso: Union[Unset, str] = UNSET
    mb_user_delay_date: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_on_exit_handle_rollback: Union[Unset, str] = UNSET
    mb_yes_no_condition: Union[Unset, str] = UNSET
    mb_enter_date_iso: Union[Unset, str] = UNSET
    mb_label: Union[Unset, str] = UNSET
    ln_comment_translation_key: Union[Unset, int] = UNSET
    type_cycle: Union[Unset, int] = UNSET
    mb_process_on_server_id: Union[Unset, str] = UNSET
    mb_user_name: Union[Unset, str] = UNSET
    type_personnode: Union[Unset, int] = UNSET
    flag_reset_children: Union[Unset, int] = UNSET
    type_splitnode: Union[Unset, int] = UNSET
    flag_one_successor: Union[Unset, int] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    flag_cycle_x: Union[Unset, int] = UNSET
    mb_time_limit_iso: Union[Unset, str] = UNSET
    mb_time_limit: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_form_spec: Union[Unset, str] = UNSET
    mb_time_limit_escalations: Union[Unset, str] = UNSET
    mb_on_enter_handle_rollback: Union[Unset, str] = UNSET
    flag_cycle_end: Union[Unset, int] = UNSET
    type_nothing: Union[Unset, int] = UNSET
    mb_all: Union[Unset, "WFNodeZ"] = UNSET
    mb_type: Union[Unset, str] = UNSET
    ln_label_translation_key: Union[Unset, int] = UNSET
    type_ifnode: Union[Unset, int] = UNSET
    mb_tag: Union[Unset, str] = UNSET
    mb_label_translation_key: Union[Unset, str] = UNSET
    mb_user_delay_date_iso: Union[Unset, str] = UNSET
    userid_owner: Union[Unset, int] = UNSET
    mb_on_enter: Union[Unset, str] = UNSET
    type_endnode: Union[Unset, int] = UNSET
    ln_process_on_server_id: Union[Unset, int] = UNSET
    mb_obj_key_names: Union[Unset, str] = UNSET
    mb_in_use_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_ret_val = self.mb_ret_val

        deactivate_all_preds = self.deactivate_all_preds

        type_collectnode = self.type_collectnode

        ln_comment = self.ln_comment

        mb_in_use_date_iso = self.mb_in_use_date_iso

        flag_not_valid = self.flag_not_valid

        mb_exit_date_iso = self.mb_exit_date_iso

        type_call_sub_workflow = self.type_call_sub_workflow

        mb_sub_template_id = self.mb_sub_template_id

        ln_yes_no_condition = self.ln_yes_no_condition

        mb_user_terminate = self.mb_user_terminate

        flag_delegated = self.flag_delegated

        mb_department_2 = self.mb_department_2

        flag_error = self.flag_error

        mb_pos_y = self.mb_pos_y

        mb_pos_x = self.mb_pos_x

        mb_nb_of_dones_to_exit = self.mb_nb_of_dones_to_exit

        ln_on_enter = self.ln_on_enter

        ln_form_spec = self.ln_form_spec

        mb_script_names = self.mb_script_names

        mb_is_next = self.mb_is_next

        flag_workingdays = self.flag_workingdays

        mb_comment = self.mb_comment

        ln_on_exit_handle_rollback = self.ln_on_exit_handle_rollback

        flag_hidden = self.flag_hidden

        mb_name = self.mb_name

        mb_delay_date = self.mb_delay_date

        mb_enter_date = self.mb_enter_date

        mb_icon_id = self.mb_icon_id

        flag_resetadhocnode = self.flag_resetadhocnode

        ln_name = self.ln_name

        mb_department_group = self.mb_department_group

        ln_on_exit = self.ln_on_exit

        mb_prio = self.mb_prio

        mb_return_value = self.mb_return_value

        mb_sub_template_name = self.mb_sub_template_name

        ln_on_enter_handle_rollback = self.ln_on_enter_handle_rollback

        flag_copy_children = self.flag_copy_children

        mb_comment_translation_key = self.mb_comment_translation_key

        mb_exit_date = self.mb_exit_date

        mb_lock_id = self.mb_lock_id

        mb_sub_flow_id = self.mb_sub_flow_id

        mb_properties = self.mb_properties

        type_pluginnode = self.type_pluginnode

        flag_terminate_user = self.flag_terminate_user

        type_set_server_id = self.type_set_server_id

        ln_properties = self.ln_properties

        mb_name_translation_key = self.mb_name_translation_key

        flag_do_not_start_manually = self.flag_do_not_start_manually

        mb_on_exit = self.mb_on_exit

        mb_design_department = self.mb_design_department

        flag_root_adhoc = self.flag_root_adhoc

        mb_delay_days = self.mb_delay_days

        ln_condition = self.ln_condition

        mb_condition = self.mb_condition

        ln_label = self.ln_label

        mb_id = self.mb_id

        mb_move_cycle_pos_x = self.mb_move_cycle_pos_x

        mb_result = self.mb_result

        userid_superior = self.userid_superior

        mb_user_id = self.mb_user_id

        type_beginnode = self.type_beginnode

        userid_ignore = self.userid_ignore

        mb_delay_date_iso = self.mb_delay_date_iso

        mb_user_delay_date = self.mb_user_delay_date

        mb_flags = self.mb_flags

        mb_on_exit_handle_rollback = self.mb_on_exit_handle_rollback

        mb_yes_no_condition = self.mb_yes_no_condition

        mb_enter_date_iso = self.mb_enter_date_iso

        mb_label = self.mb_label

        ln_comment_translation_key = self.ln_comment_translation_key

        type_cycle = self.type_cycle

        mb_process_on_server_id = self.mb_process_on_server_id

        mb_user_name = self.mb_user_name

        type_personnode = self.type_personnode

        flag_reset_children = self.flag_reset_children

        type_splitnode = self.type_splitnode

        flag_one_successor = self.flag_one_successor

        ln_name_translation_key = self.ln_name_translation_key

        flag_cycle_x = self.flag_cycle_x

        mb_time_limit_iso = self.mb_time_limit_iso

        mb_time_limit = self.mb_time_limit

        mb_all_members = self.mb_all_members

        mb_form_spec = self.mb_form_spec

        mb_time_limit_escalations = self.mb_time_limit_escalations

        mb_on_enter_handle_rollback = self.mb_on_enter_handle_rollback

        flag_cycle_end = self.flag_cycle_end

        type_nothing = self.type_nothing

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_type = self.mb_type

        ln_label_translation_key = self.ln_label_translation_key

        type_ifnode = self.type_ifnode

        mb_tag = self.mb_tag

        mb_label_translation_key = self.mb_label_translation_key

        mb_user_delay_date_iso = self.mb_user_delay_date_iso

        userid_owner = self.userid_owner

        mb_on_enter = self.mb_on_enter

        type_endnode = self.type_endnode

        ln_process_on_server_id = self.ln_process_on_server_id

        mb_obj_key_names = self.mb_obj_key_names

        mb_in_use_date = self.mb_in_use_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_ret_val is not UNSET:
            field_dict["mbRetVal"] = mb_ret_val
        if deactivate_all_preds is not UNSET:
            field_dict["DEACTIVATE_ALL_PREDS"] = deactivate_all_preds
        if type_collectnode is not UNSET:
            field_dict["TYPE_COLLECTNODE"] = type_collectnode
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if mb_in_use_date_iso is not UNSET:
            field_dict["mbInUseDateIso"] = mb_in_use_date_iso
        if flag_not_valid is not UNSET:
            field_dict["FLAG_NOT_VALID"] = flag_not_valid
        if mb_exit_date_iso is not UNSET:
            field_dict["mbExitDateIso"] = mb_exit_date_iso
        if type_call_sub_workflow is not UNSET:
            field_dict["TYPE_CALL_SUB_WORKFLOW"] = type_call_sub_workflow
        if mb_sub_template_id is not UNSET:
            field_dict["mbSubTemplateId"] = mb_sub_template_id
        if ln_yes_no_condition is not UNSET:
            field_dict["lnYesNoCondition"] = ln_yes_no_condition
        if mb_user_terminate is not UNSET:
            field_dict["mbUserTerminate"] = mb_user_terminate
        if flag_delegated is not UNSET:
            field_dict["FLAG_DELEGATED"] = flag_delegated
        if mb_department_2 is not UNSET:
            field_dict["mbDepartment2"] = mb_department_2
        if flag_error is not UNSET:
            field_dict["FLAG_ERROR"] = flag_error
        if mb_pos_y is not UNSET:
            field_dict["mbPosY"] = mb_pos_y
        if mb_pos_x is not UNSET:
            field_dict["mbPosX"] = mb_pos_x
        if mb_nb_of_dones_to_exit is not UNSET:
            field_dict["mbNbOfDonesToExit"] = mb_nb_of_dones_to_exit
        if ln_on_enter is not UNSET:
            field_dict["lnOnEnter"] = ln_on_enter
        if ln_form_spec is not UNSET:
            field_dict["lnFormSpec"] = ln_form_spec
        if mb_script_names is not UNSET:
            field_dict["mbScriptNames"] = mb_script_names
        if mb_is_next is not UNSET:
            field_dict["mbIsNext"] = mb_is_next
        if flag_workingdays is not UNSET:
            field_dict["FLAG_WORKINGDAYS"] = flag_workingdays
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment
        if ln_on_exit_handle_rollback is not UNSET:
            field_dict["lnOnExitHandleRollback"] = ln_on_exit_handle_rollback
        if flag_hidden is not UNSET:
            field_dict["FLAG_HIDDEN"] = flag_hidden
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_delay_date is not UNSET:
            field_dict["mbDelayDate"] = mb_delay_date
        if mb_enter_date is not UNSET:
            field_dict["mbEnterDate"] = mb_enter_date
        if mb_icon_id is not UNSET:
            field_dict["mbIconId"] = mb_icon_id
        if flag_resetadhocnode is not UNSET:
            field_dict["FLAG_RESETADHOCNODE"] = flag_resetadhocnode
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_department_group is not UNSET:
            field_dict["mbDepartmentGroup"] = mb_department_group
        if ln_on_exit is not UNSET:
            field_dict["lnOnExit"] = ln_on_exit
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_return_value is not UNSET:
            field_dict["mbReturnValue"] = mb_return_value
        if mb_sub_template_name is not UNSET:
            field_dict["mbSubTemplateName"] = mb_sub_template_name
        if ln_on_enter_handle_rollback is not UNSET:
            field_dict["lnOnEnterHandleRollback"] = ln_on_enter_handle_rollback
        if flag_copy_children is not UNSET:
            field_dict["FLAG_COPY_CHILDREN"] = flag_copy_children
        if mb_comment_translation_key is not UNSET:
            field_dict["mbCommentTranslationKey"] = mb_comment_translation_key
        if mb_exit_date is not UNSET:
            field_dict["mbExitDate"] = mb_exit_date
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_sub_flow_id is not UNSET:
            field_dict["mbSubFlowId"] = mb_sub_flow_id
        if mb_properties is not UNSET:
            field_dict["mbProperties"] = mb_properties
        if type_pluginnode is not UNSET:
            field_dict["TYPE_PLUGINNODE"] = type_pluginnode
        if flag_terminate_user is not UNSET:
            field_dict["FLAG_TERMINATE_USER"] = flag_terminate_user
        if type_set_server_id is not UNSET:
            field_dict["TYPE_SET_SERVER_ID"] = type_set_server_id
        if ln_properties is not UNSET:
            field_dict["lnProperties"] = ln_properties
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if flag_do_not_start_manually is not UNSET:
            field_dict["FLAG_DO_NOT_START_MANUALLY"] = flag_do_not_start_manually
        if mb_on_exit is not UNSET:
            field_dict["mbOnExit"] = mb_on_exit
        if mb_design_department is not UNSET:
            field_dict["mbDesignDepartment"] = mb_design_department
        if flag_root_adhoc is not UNSET:
            field_dict["FLAG_ROOT_ADHOC"] = flag_root_adhoc
        if mb_delay_days is not UNSET:
            field_dict["mbDelayDays"] = mb_delay_days
        if ln_condition is not UNSET:
            field_dict["lnCondition"] = ln_condition
        if mb_condition is not UNSET:
            field_dict["mbCondition"] = mb_condition
        if ln_label is not UNSET:
            field_dict["lnLabel"] = ln_label
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_move_cycle_pos_x is not UNSET:
            field_dict["mbMoveCyclePosX"] = mb_move_cycle_pos_x
        if mb_result is not UNSET:
            field_dict["mbResult"] = mb_result
        if userid_superior is not UNSET:
            field_dict["USERID_SUPERIOR"] = userid_superior
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if type_beginnode is not UNSET:
            field_dict["TYPE_BEGINNODE"] = type_beginnode
        if userid_ignore is not UNSET:
            field_dict["USERID_IGNORE"] = userid_ignore
        if mb_delay_date_iso is not UNSET:
            field_dict["mbDelayDateIso"] = mb_delay_date_iso
        if mb_user_delay_date is not UNSET:
            field_dict["mbUserDelayDate"] = mb_user_delay_date
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_on_exit_handle_rollback is not UNSET:
            field_dict["mbOnExitHandleRollback"] = mb_on_exit_handle_rollback
        if mb_yes_no_condition is not UNSET:
            field_dict["mbYesNoCondition"] = mb_yes_no_condition
        if mb_enter_date_iso is not UNSET:
            field_dict["mbEnterDateIso"] = mb_enter_date_iso
        if mb_label is not UNSET:
            field_dict["mbLabel"] = mb_label
        if ln_comment_translation_key is not UNSET:
            field_dict["lnCommentTranslationKey"] = ln_comment_translation_key
        if type_cycle is not UNSET:
            field_dict["TYPE_CYCLE"] = type_cycle
        if mb_process_on_server_id is not UNSET:
            field_dict["mbProcessOnServerId"] = mb_process_on_server_id
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if type_personnode is not UNSET:
            field_dict["TYPE_PERSONNODE"] = type_personnode
        if flag_reset_children is not UNSET:
            field_dict["FLAG_RESET_CHILDREN"] = flag_reset_children
        if type_splitnode is not UNSET:
            field_dict["TYPE_SPLITNODE"] = type_splitnode
        if flag_one_successor is not UNSET:
            field_dict["FLAG_ONE_SUCCESSOR"] = flag_one_successor
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if flag_cycle_x is not UNSET:
            field_dict["FLAG_CYCLE_X"] = flag_cycle_x
        if mb_time_limit_iso is not UNSET:
            field_dict["mbTimeLimitIso"] = mb_time_limit_iso
        if mb_time_limit is not UNSET:
            field_dict["mbTimeLimit"] = mb_time_limit
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_form_spec is not UNSET:
            field_dict["mbFormSpec"] = mb_form_spec
        if mb_time_limit_escalations is not UNSET:
            field_dict["mbTimeLimitEscalations"] = mb_time_limit_escalations
        if mb_on_enter_handle_rollback is not UNSET:
            field_dict["mbOnEnterHandleRollback"] = mb_on_enter_handle_rollback
        if flag_cycle_end is not UNSET:
            field_dict["FLAG_CYCLE_END"] = flag_cycle_end
        if type_nothing is not UNSET:
            field_dict["TYPE_NOTHING"] = type_nothing
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if ln_label_translation_key is not UNSET:
            field_dict["lnLabelTranslationKey"] = ln_label_translation_key
        if type_ifnode is not UNSET:
            field_dict["TYPE_IFNODE"] = type_ifnode
        if mb_tag is not UNSET:
            field_dict["mbTag"] = mb_tag
        if mb_label_translation_key is not UNSET:
            field_dict["mbLabelTranslationKey"] = mb_label_translation_key
        if mb_user_delay_date_iso is not UNSET:
            field_dict["mbUserDelayDateIso"] = mb_user_delay_date_iso
        if userid_owner is not UNSET:
            field_dict["USERID_OWNER"] = userid_owner
        if mb_on_enter is not UNSET:
            field_dict["mbOnEnter"] = mb_on_enter
        if type_endnode is not UNSET:
            field_dict["TYPE_ENDNODE"] = type_endnode
        if ln_process_on_server_id is not UNSET:
            field_dict["lnProcessOnServerId"] = ln_process_on_server_id
        if mb_obj_key_names is not UNSET:
            field_dict["mbObjKeyNames"] = mb_obj_key_names
        if mb_in_use_date is not UNSET:
            field_dict["mbInUseDate"] = mb_in_use_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_node_z import WFNodeZ

        d = src_dict.copy()
        mb_ret_val = d.pop("mbRetVal", UNSET)

        deactivate_all_preds = d.pop("DEACTIVATE_ALL_PREDS", UNSET)

        type_collectnode = d.pop("TYPE_COLLECTNODE", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        mb_in_use_date_iso = d.pop("mbInUseDateIso", UNSET)

        flag_not_valid = d.pop("FLAG_NOT_VALID", UNSET)

        mb_exit_date_iso = d.pop("mbExitDateIso", UNSET)

        type_call_sub_workflow = d.pop("TYPE_CALL_SUB_WORKFLOW", UNSET)

        mb_sub_template_id = d.pop("mbSubTemplateId", UNSET)

        ln_yes_no_condition = d.pop("lnYesNoCondition", UNSET)

        mb_user_terminate = d.pop("mbUserTerminate", UNSET)

        flag_delegated = d.pop("FLAG_DELEGATED", UNSET)

        mb_department_2 = d.pop("mbDepartment2", UNSET)

        flag_error = d.pop("FLAG_ERROR", UNSET)

        mb_pos_y = d.pop("mbPosY", UNSET)

        mb_pos_x = d.pop("mbPosX", UNSET)

        mb_nb_of_dones_to_exit = d.pop("mbNbOfDonesToExit", UNSET)

        ln_on_enter = d.pop("lnOnEnter", UNSET)

        ln_form_spec = d.pop("lnFormSpec", UNSET)

        mb_script_names = d.pop("mbScriptNames", UNSET)

        mb_is_next = d.pop("mbIsNext", UNSET)

        flag_workingdays = d.pop("FLAG_WORKINGDAYS", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        ln_on_exit_handle_rollback = d.pop("lnOnExitHandleRollback", UNSET)

        flag_hidden = d.pop("FLAG_HIDDEN", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_delay_date = d.pop("mbDelayDate", UNSET)

        mb_enter_date = d.pop("mbEnterDate", UNSET)

        mb_icon_id = d.pop("mbIconId", UNSET)

        flag_resetadhocnode = d.pop("FLAG_RESETADHOCNODE", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_department_group = d.pop("mbDepartmentGroup", UNSET)

        ln_on_exit = d.pop("lnOnExit", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_return_value = d.pop("mbReturnValue", UNSET)

        mb_sub_template_name = d.pop("mbSubTemplateName", UNSET)

        ln_on_enter_handle_rollback = d.pop("lnOnEnterHandleRollback", UNSET)

        flag_copy_children = d.pop("FLAG_COPY_CHILDREN", UNSET)

        mb_comment_translation_key = d.pop("mbCommentTranslationKey", UNSET)

        mb_exit_date = d.pop("mbExitDate", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_sub_flow_id = d.pop("mbSubFlowId", UNSET)

        mb_properties = d.pop("mbProperties", UNSET)

        type_pluginnode = d.pop("TYPE_PLUGINNODE", UNSET)

        flag_terminate_user = d.pop("FLAG_TERMINATE_USER", UNSET)

        type_set_server_id = d.pop("TYPE_SET_SERVER_ID", UNSET)

        ln_properties = d.pop("lnProperties", UNSET)

        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        flag_do_not_start_manually = d.pop("FLAG_DO_NOT_START_MANUALLY", UNSET)

        mb_on_exit = d.pop("mbOnExit", UNSET)

        mb_design_department = d.pop("mbDesignDepartment", UNSET)

        flag_root_adhoc = d.pop("FLAG_ROOT_ADHOC", UNSET)

        mb_delay_days = d.pop("mbDelayDays", UNSET)

        ln_condition = d.pop("lnCondition", UNSET)

        mb_condition = d.pop("mbCondition", UNSET)

        ln_label = d.pop("lnLabel", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_move_cycle_pos_x = d.pop("mbMoveCyclePosX", UNSET)

        mb_result = d.pop("mbResult", UNSET)

        userid_superior = d.pop("USERID_SUPERIOR", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        type_beginnode = d.pop("TYPE_BEGINNODE", UNSET)

        userid_ignore = d.pop("USERID_IGNORE", UNSET)

        mb_delay_date_iso = d.pop("mbDelayDateIso", UNSET)

        mb_user_delay_date = d.pop("mbUserDelayDate", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_on_exit_handle_rollback = d.pop("mbOnExitHandleRollback", UNSET)

        mb_yes_no_condition = d.pop("mbYesNoCondition", UNSET)

        mb_enter_date_iso = d.pop("mbEnterDateIso", UNSET)

        mb_label = d.pop("mbLabel", UNSET)

        ln_comment_translation_key = d.pop("lnCommentTranslationKey", UNSET)

        type_cycle = d.pop("TYPE_CYCLE", UNSET)

        mb_process_on_server_id = d.pop("mbProcessOnServerId", UNSET)

        mb_user_name = d.pop("mbUserName", UNSET)

        type_personnode = d.pop("TYPE_PERSONNODE", UNSET)

        flag_reset_children = d.pop("FLAG_RESET_CHILDREN", UNSET)

        type_splitnode = d.pop("TYPE_SPLITNODE", UNSET)

        flag_one_successor = d.pop("FLAG_ONE_SUCCESSOR", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        flag_cycle_x = d.pop("FLAG_CYCLE_X", UNSET)

        mb_time_limit_iso = d.pop("mbTimeLimitIso", UNSET)

        mb_time_limit = d.pop("mbTimeLimit", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_form_spec = d.pop("mbFormSpec", UNSET)

        mb_time_limit_escalations = d.pop("mbTimeLimitEscalations", UNSET)

        mb_on_enter_handle_rollback = d.pop("mbOnEnterHandleRollback", UNSET)

        flag_cycle_end = d.pop("FLAG_CYCLE_END", UNSET)

        type_nothing = d.pop("TYPE_NOTHING", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, WFNodeZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = WFNodeZ.from_dict(_mb_all)

        mb_type = d.pop("mbType", UNSET)

        ln_label_translation_key = d.pop("lnLabelTranslationKey", UNSET)

        type_ifnode = d.pop("TYPE_IFNODE", UNSET)

        mb_tag = d.pop("mbTag", UNSET)

        mb_label_translation_key = d.pop("mbLabelTranslationKey", UNSET)

        mb_user_delay_date_iso = d.pop("mbUserDelayDateIso", UNSET)

        userid_owner = d.pop("USERID_OWNER", UNSET)

        mb_on_enter = d.pop("mbOnEnter", UNSET)

        type_endnode = d.pop("TYPE_ENDNODE", UNSET)

        ln_process_on_server_id = d.pop("lnProcessOnServerId", UNSET)

        mb_obj_key_names = d.pop("mbObjKeyNames", UNSET)

        mb_in_use_date = d.pop("mbInUseDate", UNSET)

        wf_node_c = cls(
            mb_ret_val=mb_ret_val,
            deactivate_all_preds=deactivate_all_preds,
            type_collectnode=type_collectnode,
            ln_comment=ln_comment,
            mb_in_use_date_iso=mb_in_use_date_iso,
            flag_not_valid=flag_not_valid,
            mb_exit_date_iso=mb_exit_date_iso,
            type_call_sub_workflow=type_call_sub_workflow,
            mb_sub_template_id=mb_sub_template_id,
            ln_yes_no_condition=ln_yes_no_condition,
            mb_user_terminate=mb_user_terminate,
            flag_delegated=flag_delegated,
            mb_department_2=mb_department_2,
            flag_error=flag_error,
            mb_pos_y=mb_pos_y,
            mb_pos_x=mb_pos_x,
            mb_nb_of_dones_to_exit=mb_nb_of_dones_to_exit,
            ln_on_enter=ln_on_enter,
            ln_form_spec=ln_form_spec,
            mb_script_names=mb_script_names,
            mb_is_next=mb_is_next,
            flag_workingdays=flag_workingdays,
            mb_comment=mb_comment,
            ln_on_exit_handle_rollback=ln_on_exit_handle_rollback,
            flag_hidden=flag_hidden,
            mb_name=mb_name,
            mb_delay_date=mb_delay_date,
            mb_enter_date=mb_enter_date,
            mb_icon_id=mb_icon_id,
            flag_resetadhocnode=flag_resetadhocnode,
            ln_name=ln_name,
            mb_department_group=mb_department_group,
            ln_on_exit=ln_on_exit,
            mb_prio=mb_prio,
            mb_return_value=mb_return_value,
            mb_sub_template_name=mb_sub_template_name,
            ln_on_enter_handle_rollback=ln_on_enter_handle_rollback,
            flag_copy_children=flag_copy_children,
            mb_comment_translation_key=mb_comment_translation_key,
            mb_exit_date=mb_exit_date,
            mb_lock_id=mb_lock_id,
            mb_sub_flow_id=mb_sub_flow_id,
            mb_properties=mb_properties,
            type_pluginnode=type_pluginnode,
            flag_terminate_user=flag_terminate_user,
            type_set_server_id=type_set_server_id,
            ln_properties=ln_properties,
            mb_name_translation_key=mb_name_translation_key,
            flag_do_not_start_manually=flag_do_not_start_manually,
            mb_on_exit=mb_on_exit,
            mb_design_department=mb_design_department,
            flag_root_adhoc=flag_root_adhoc,
            mb_delay_days=mb_delay_days,
            ln_condition=ln_condition,
            mb_condition=mb_condition,
            ln_label=ln_label,
            mb_id=mb_id,
            mb_move_cycle_pos_x=mb_move_cycle_pos_x,
            mb_result=mb_result,
            userid_superior=userid_superior,
            mb_user_id=mb_user_id,
            type_beginnode=type_beginnode,
            userid_ignore=userid_ignore,
            mb_delay_date_iso=mb_delay_date_iso,
            mb_user_delay_date=mb_user_delay_date,
            mb_flags=mb_flags,
            mb_on_exit_handle_rollback=mb_on_exit_handle_rollback,
            mb_yes_no_condition=mb_yes_no_condition,
            mb_enter_date_iso=mb_enter_date_iso,
            mb_label=mb_label,
            ln_comment_translation_key=ln_comment_translation_key,
            type_cycle=type_cycle,
            mb_process_on_server_id=mb_process_on_server_id,
            mb_user_name=mb_user_name,
            type_personnode=type_personnode,
            flag_reset_children=flag_reset_children,
            type_splitnode=type_splitnode,
            flag_one_successor=flag_one_successor,
            ln_name_translation_key=ln_name_translation_key,
            flag_cycle_x=flag_cycle_x,
            mb_time_limit_iso=mb_time_limit_iso,
            mb_time_limit=mb_time_limit,
            mb_all_members=mb_all_members,
            mb_form_spec=mb_form_spec,
            mb_time_limit_escalations=mb_time_limit_escalations,
            mb_on_enter_handle_rollback=mb_on_enter_handle_rollback,
            flag_cycle_end=flag_cycle_end,
            type_nothing=type_nothing,
            mb_all=mb_all,
            mb_type=mb_type,
            ln_label_translation_key=ln_label_translation_key,
            type_ifnode=type_ifnode,
            mb_tag=mb_tag,
            mb_label_translation_key=mb_label_translation_key,
            mb_user_delay_date_iso=mb_user_delay_date_iso,
            userid_owner=userid_owner,
            mb_on_enter=mb_on_enter,
            type_endnode=type_endnode,
            ln_process_on_server_id=ln_process_on_server_id,
            mb_obj_key_names=mb_obj_key_names,
            mb_in_use_date=mb_in_use_date,
        )

        wf_node_c.additional_properties = d
        return wf_node_c

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
