from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowActiveDoc")


@_attrs_define
class WorkFlowActiveDoc:
    """Internal class.

    Attributes:
        alert_from_begin (Union[Unset, int]): Time-limt for the entire workflow in minutes. This value is only valid for
            the begin node.
            DB
             column: wf_alert_from_begin
        succ_11 (Union[Unset, int]): DB column: wf_succ_11
        succ_10 (Union[Unset, int]): DB column: wf_succ_10
        on_exit_handle_rollback (Union[Unset, str]): Name of script to be executed when the node encounters an error
            (exception).
            DB column:
             wf_ev_on_exception_after_exit
        succ_13 (Union[Unset, int]): DB column: wf_succ_13
        succ_12 (Union[Unset, int]): DB column: wf_succ_12
        active_acl (Union[Unset, str]): Contains the ACL of the workflow. Only valid for begin nodes.
        template_id (Union[Unset, int]): Workflow template ID. Not valid for template workflows.
            For active and finished workflows this
             member specifies the template ID that was used to start the workflow. If the workflow is
             started as an adhoc workflow, this member is 0 and flags contains the bit FLAG_ROOT_ADHOC. DB
             column: wf_template
        version_name (Union[Unset, str]): Version comment.
        ret_val (Union[Unset, int]): Return value of an end node.
        on_activate (Union[Unset, str]): Name of script to be executed, if the node is activated (entered).
            DB column: wf_ev_on_activate
        alert_wait_2 (Union[Unset, int]): Second Time-limit for a person node or begin node.
        department2 (Union[Unset, int]): A group ID to constrain access to the node.
            Only members of this group are allowed to see and
             process the node. Only valid for person nodes. DB column: wf_department2
        is_next (Union[Unset, int]): Contains 1, if this node is active.
            DB column: wf_is_next
        tag (Union[Unset, int]): reserved.
            DB column: wf_tag
        alert_wait_3 (Union[Unset, int]): Third Time-limit for a person node or begin node.
        locked (Union[Unset, int]): If node is locked, it contains 1 otherwise 0 DB column: wf_locked
        prio (Union[Unset, int]): Workflow priority: 0...high, 1...medium, 2...low.
            DB column: wf_prio
        succ_9 (Union[Unset, int]): DB column: wf_succ_9
        icon_id (Union[Unset, str]): Object-GUID of an icon file that is displayed in the designer.
        department_group (Union[Unset, int]): Grouping of nodes for function takeWorkFlowNode.
        succ_5 (Union[Unset, int]): DB column: wf_succ_5
        form_spec (Union[Unset, str]): User defined data to be stored in the database.
        succ_6 (Union[Unset, int]): DB column: wf_succ_6
        succ_7 (Union[Unset, int]): DB column: wf_succ_7
        alert_wait (Union[Unset, int]): Time-limit for a single node. This value is only valid for person nodes.
            DB column:
             wf_alert_wait
        succ_8 (Union[Unset, int]): DB column: wf_succ_8
        succ_1 (Union[Unset, int]): DB column: wf_succ_1
        succ_2 (Union[Unset, int]): DB column: wf_succ_2
        succ_3 (Union[Unset, int]): DB column: wf_succ_3
        version_tag (Union[Unset, str]): Version number.
        succ_4 (Union[Unset, int]): DB column: wf_succ_4
        node_type (Union[Unset, int]): Node type (begin node, split node, etc.).
            DB column: wf_node_type
        move_cycle_pos_x (Union[Unset, int]): If a cycle is re-entered, the nodes in the cycle are duplicated.
            The copied nodes will be
             placed in the designer moved by this value to the right. If this value is 0, the nodes are
             moved 60 points right and 20 points up. DB column: wf_dx
        flow_name (Union[Unset, str]): Workflow name.
            DB column: wf_flow_name
        succ_0 (Union[Unset, int]): Successor node(s) succ_0 ...
            Succ 19 DB column: wf_succ_0 This mebers are moved into
             WorkFlowNodeMatrix. They are still here due to compatibiltiy with older stream versions.
        pos_x (Union[Unset, int]): Node X position in designer view.
            DB column: pos_x
        lock_id (Union[Unset, int]): User ID of the owner of the lock.
            DB column: wf_locked_owner
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#name}.
        pos_y (Union[Unset, int]): Node Y position in designer view.
            DB column: pos_y
        y_n_condition (Union[Unset, str]): IF-Nodes: test condition, person nodes: index values or scripts, split nodes:
            workflow status.
            DB column: wf_yesnocondition
        condition (Union[Unset, str]): Contains the ACL of the workflow template. Only valid for begin nodes.
            DB column: wf_condition
        version_id (Union[Unset, int]): Version ID.
        name (Union[Unset, str]): Node name (work instruction).
            DB column: wf_name
        activate (Union[Unset, int]): ELO-date when the node was entered.
            DB column: wf_activate
        design_department (Union[Unset, int]): A group ID or user ID that was originally assigned in the designer.
            DB column:
             wf_designdepartment
        alert_to (Union[Unset, int]): ID of user who should be informed, if a time-limit exceeds.
            It might be the time-limit for the
             entire workflow or for a signle person node. DB column: wf_alert_to
        terminate (Union[Unset, int]): ELO-date when the node was exited.
            DB column: wf_terminate
        version_user_id (Union[Unset, int]): ID of the user who created the workflow version.
        node_id (Union[Unset, int]): Node ID.
            DB column: wf_nodeid
        user_terminate (Union[Unset, str]): The ID of the user who has forwarded the node. Not valid for template
            workflows.
            Only valid for
             person nodes. DB column: wf_userterminate
        in_use_date (Union[Unset, int]): ELO-date when the node was visited the last time.
            DB column: wf_in_use_date
        elo_obj_id (Union[Unset, int]): Associated object ID. Only valid for non-template workflows.
            DB column: wf_eloobjid
        return_value (Union[Unset, str]): Return value of an end node.
        sub_workflow_template (Union[Unset, int]): ID of the sub-workflow template.
        on_terminate (Union[Unset, str]): Name of script to be executed, if the node is leaved (exited).
            DB column: wf_ev_on_terminate
        delay_date (Union[Unset, int]): Activate + DelayDays. Not valid for template workflows. Only valid for person
            nodes.
            DB column:
             wf_duedate
        alert_to_2 (Union[Unset, int]): ID of user who should be informed, if the time-limit alertWait2 exceeds.
        user_delay_date (Union[Unset, int]): The workflow node is deferred until this date. ELO date format.
            DB column: wf_user_delaydate
        alert_to_3 (Union[Unset, int]): ID of user who should be informed, if the time-limit alertWait2 exceeds.
        package_name (Union[Unset, str]): PackageName of a Workflow, only used for workflow templates
        department (Union[Unset, int]): ID of user who has to process the node. Might be a group ID too. Only valid for
            person nodes.
            DB column: wf_department
        flow_id (Union[Unset, int]): Workflow ID.
            DB column: wf_flowid
        next_server_id (Union[Unset, str]): Next server name.
            This value is used in replication environments and defines the ID of the next
             server (resp. replication branch) where the workflow continues processing.
        version_create_date (Union[Unset, int]): ID of the user who created the workflow version.
        comment_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#comment}.
        sub_workflow (Union[Unset, int]): ID of the active sub-workflow.
        label (Union[Unset, str]): Display name by forwarding.
        succ_19 (Union[Unset, int]): DB column: wf_succ_19
        succ_18 (Union[Unset, int]): DB column: wf_succ_18
        deleted (Union[Unset, int]): Flag that indicates whether the workflow template is deleted.
            If the value is not 0, the
             workflow template is deleted. Only valid for template workflows. DB column: wf_deleted
        succ_15 (Union[Unset, int]): DB column: wf_succ_15
        succ_14 (Union[Unset, int]): DB column: wf_succ_14
        succ_17 (Union[Unset, int]): DB column: wf_succ_17
        succ_type (Union[Unset, int]): This value depends on the node type and is not processed anymore by Indexserver.
            It is written
             for compability with workflows of older CLIENT versions. DB column: wf_succ_type
        succ_16 (Union[Unset, int]): DB column: wf_succ_16
        delay_days (Union[Unset, int]): An active person node (Activate is set) might be displayed to the user delayed
            by this number
            of days. Only valid for person nodes. DB column: wf_delaydays
        comment (Union[Unset, str]): Comment, only valid for person nodes.
            DB column: wf_comment
        node_flags (Union[Unset, int]): Node flags.
            DB column: wf_nodeflags
        completion_date (Union[Unset, int]): ELO-date when the workflow was finished. All nodes contain the same value.
            DB column:
             wf_completion_date
        on_enter_handle_rollback (Union[Unset, str]): Name of script to be executed when the node encounters an error
            (exception).
            DB column:
             wf_ev_on_exception_after_enter
        flow_name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFDiagram#name}.
        properties (Union[Unset, str]): Properties field of node.
        label_translation_key (Union[Unset, str]): Translation-keyword for {@link WorkFlowActiveDoc#label}.
    """

    alert_from_begin: Union[Unset, int] = UNSET
    succ_11: Union[Unset, int] = UNSET
    succ_10: Union[Unset, int] = UNSET
    on_exit_handle_rollback: Union[Unset, str] = UNSET
    succ_13: Union[Unset, int] = UNSET
    succ_12: Union[Unset, int] = UNSET
    active_acl: Union[Unset, str] = UNSET
    template_id: Union[Unset, int] = UNSET
    version_name: Union[Unset, str] = UNSET
    ret_val: Union[Unset, int] = UNSET
    on_activate: Union[Unset, str] = UNSET
    alert_wait_2: Union[Unset, int] = UNSET
    department2: Union[Unset, int] = UNSET
    is_next: Union[Unset, int] = UNSET
    tag: Union[Unset, int] = UNSET
    alert_wait_3: Union[Unset, int] = UNSET
    locked: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    succ_9: Union[Unset, int] = UNSET
    icon_id: Union[Unset, str] = UNSET
    department_group: Union[Unset, int] = UNSET
    succ_5: Union[Unset, int] = UNSET
    form_spec: Union[Unset, str] = UNSET
    succ_6: Union[Unset, int] = UNSET
    succ_7: Union[Unset, int] = UNSET
    alert_wait: Union[Unset, int] = UNSET
    succ_8: Union[Unset, int] = UNSET
    succ_1: Union[Unset, int] = UNSET
    succ_2: Union[Unset, int] = UNSET
    succ_3: Union[Unset, int] = UNSET
    version_tag: Union[Unset, str] = UNSET
    succ_4: Union[Unset, int] = UNSET
    node_type: Union[Unset, int] = UNSET
    move_cycle_pos_x: Union[Unset, int] = UNSET
    flow_name: Union[Unset, str] = UNSET
    succ_0: Union[Unset, int] = UNSET
    pos_x: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    pos_y: Union[Unset, int] = UNSET
    y_n_condition: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    version_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    activate: Union[Unset, int] = UNSET
    design_department: Union[Unset, int] = UNSET
    alert_to: Union[Unset, int] = UNSET
    terminate: Union[Unset, int] = UNSET
    version_user_id: Union[Unset, int] = UNSET
    node_id: Union[Unset, int] = UNSET
    user_terminate: Union[Unset, str] = UNSET
    in_use_date: Union[Unset, int] = UNSET
    elo_obj_id: Union[Unset, int] = UNSET
    return_value: Union[Unset, str] = UNSET
    sub_workflow_template: Union[Unset, int] = UNSET
    on_terminate: Union[Unset, str] = UNSET
    delay_date: Union[Unset, int] = UNSET
    alert_to_2: Union[Unset, int] = UNSET
    user_delay_date: Union[Unset, int] = UNSET
    alert_to_3: Union[Unset, int] = UNSET
    package_name: Union[Unset, str] = UNSET
    department: Union[Unset, int] = UNSET
    flow_id: Union[Unset, int] = UNSET
    next_server_id: Union[Unset, str] = UNSET
    version_create_date: Union[Unset, int] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    sub_workflow: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    succ_19: Union[Unset, int] = UNSET
    succ_18: Union[Unset, int] = UNSET
    deleted: Union[Unset, int] = UNSET
    succ_15: Union[Unset, int] = UNSET
    succ_14: Union[Unset, int] = UNSET
    succ_17: Union[Unset, int] = UNSET
    succ_type: Union[Unset, int] = UNSET
    succ_16: Union[Unset, int] = UNSET
    delay_days: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    node_flags: Union[Unset, int] = UNSET
    completion_date: Union[Unset, int] = UNSET
    on_enter_handle_rollback: Union[Unset, str] = UNSET
    flow_name_translation_key: Union[Unset, str] = UNSET
    properties: Union[Unset, str] = UNSET
    label_translation_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_from_begin = self.alert_from_begin

        succ_11 = self.succ_11

        succ_10 = self.succ_10

        on_exit_handle_rollback = self.on_exit_handle_rollback

        succ_13 = self.succ_13

        succ_12 = self.succ_12

        active_acl = self.active_acl

        template_id = self.template_id

        version_name = self.version_name

        ret_val = self.ret_val

        on_activate = self.on_activate

        alert_wait_2 = self.alert_wait_2

        department2 = self.department2

        is_next = self.is_next

        tag = self.tag

        alert_wait_3 = self.alert_wait_3

        locked = self.locked

        prio = self.prio

        succ_9 = self.succ_9

        icon_id = self.icon_id

        department_group = self.department_group

        succ_5 = self.succ_5

        form_spec = self.form_spec

        succ_6 = self.succ_6

        succ_7 = self.succ_7

        alert_wait = self.alert_wait

        succ_8 = self.succ_8

        succ_1 = self.succ_1

        succ_2 = self.succ_2

        succ_3 = self.succ_3

        version_tag = self.version_tag

        succ_4 = self.succ_4

        node_type = self.node_type

        move_cycle_pos_x = self.move_cycle_pos_x

        flow_name = self.flow_name

        succ_0 = self.succ_0

        pos_x = self.pos_x

        lock_id = self.lock_id

        name_translation_key = self.name_translation_key

        pos_y = self.pos_y

        y_n_condition = self.y_n_condition

        condition = self.condition

        version_id = self.version_id

        name = self.name

        activate = self.activate

        design_department = self.design_department

        alert_to = self.alert_to

        terminate = self.terminate

        version_user_id = self.version_user_id

        node_id = self.node_id

        user_terminate = self.user_terminate

        in_use_date = self.in_use_date

        elo_obj_id = self.elo_obj_id

        return_value = self.return_value

        sub_workflow_template = self.sub_workflow_template

        on_terminate = self.on_terminate

        delay_date = self.delay_date

        alert_to_2 = self.alert_to_2

        user_delay_date = self.user_delay_date

        alert_to_3 = self.alert_to_3

        package_name = self.package_name

        department = self.department

        flow_id = self.flow_id

        next_server_id = self.next_server_id

        version_create_date = self.version_create_date

        comment_translation_key = self.comment_translation_key

        sub_workflow = self.sub_workflow

        label = self.label

        succ_19 = self.succ_19

        succ_18 = self.succ_18

        deleted = self.deleted

        succ_15 = self.succ_15

        succ_14 = self.succ_14

        succ_17 = self.succ_17

        succ_type = self.succ_type

        succ_16 = self.succ_16

        delay_days = self.delay_days

        comment = self.comment

        node_flags = self.node_flags

        completion_date = self.completion_date

        on_enter_handle_rollback = self.on_enter_handle_rollback

        flow_name_translation_key = self.flow_name_translation_key

        properties = self.properties

        label_translation_key = self.label_translation_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_from_begin is not UNSET:
            field_dict["alertFromBegin"] = alert_from_begin
        if succ_11 is not UNSET:
            field_dict["succ_11"] = succ_11
        if succ_10 is not UNSET:
            field_dict["succ_10"] = succ_10
        if on_exit_handle_rollback is not UNSET:
            field_dict["onExitHandleRollback"] = on_exit_handle_rollback
        if succ_13 is not UNSET:
            field_dict["succ_13"] = succ_13
        if succ_12 is not UNSET:
            field_dict["succ_12"] = succ_12
        if active_acl is not UNSET:
            field_dict["activeAcl"] = active_acl
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if ret_val is not UNSET:
            field_dict["retVal"] = ret_val
        if on_activate is not UNSET:
            field_dict["onActivate"] = on_activate
        if alert_wait_2 is not UNSET:
            field_dict["alertWait2"] = alert_wait_2
        if department2 is not UNSET:
            field_dict["department2"] = department2
        if is_next is not UNSET:
            field_dict["isNext"] = is_next
        if tag is not UNSET:
            field_dict["tag"] = tag
        if alert_wait_3 is not UNSET:
            field_dict["alertWait3"] = alert_wait_3
        if locked is not UNSET:
            field_dict["locked"] = locked
        if prio is not UNSET:
            field_dict["prio"] = prio
        if succ_9 is not UNSET:
            field_dict["succ_9"] = succ_9
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if department_group is not UNSET:
            field_dict["departmentGroup"] = department_group
        if succ_5 is not UNSET:
            field_dict["succ_5"] = succ_5
        if form_spec is not UNSET:
            field_dict["formSpec"] = form_spec
        if succ_6 is not UNSET:
            field_dict["succ_6"] = succ_6
        if succ_7 is not UNSET:
            field_dict["succ_7"] = succ_7
        if alert_wait is not UNSET:
            field_dict["alertWait"] = alert_wait
        if succ_8 is not UNSET:
            field_dict["succ_8"] = succ_8
        if succ_1 is not UNSET:
            field_dict["succ_1"] = succ_1
        if succ_2 is not UNSET:
            field_dict["succ_2"] = succ_2
        if succ_3 is not UNSET:
            field_dict["succ_3"] = succ_3
        if version_tag is not UNSET:
            field_dict["versionTag"] = version_tag
        if succ_4 is not UNSET:
            field_dict["succ_4"] = succ_4
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if move_cycle_pos_x is not UNSET:
            field_dict["moveCyclePosX"] = move_cycle_pos_x
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if succ_0 is not UNSET:
            field_dict["succ_0"] = succ_0
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if y_n_condition is not UNSET:
            field_dict["yNCondition"] = y_n_condition
        if condition is not UNSET:
            field_dict["condition"] = condition
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if name is not UNSET:
            field_dict["name"] = name
        if activate is not UNSET:
            field_dict["activate"] = activate
        if design_department is not UNSET:
            field_dict["designDepartment"] = design_department
        if alert_to is not UNSET:
            field_dict["alertTo"] = alert_to
        if terminate is not UNSET:
            field_dict["terminate"] = terminate
        if version_user_id is not UNSET:
            field_dict["versionUserId"] = version_user_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if user_terminate is not UNSET:
            field_dict["userTerminate"] = user_terminate
        if in_use_date is not UNSET:
            field_dict["inUseDate"] = in_use_date
        if elo_obj_id is not UNSET:
            field_dict["eloObjId"] = elo_obj_id
        if return_value is not UNSET:
            field_dict["returnValue"] = return_value
        if sub_workflow_template is not UNSET:
            field_dict["subWorkflowTemplate"] = sub_workflow_template
        if on_terminate is not UNSET:
            field_dict["onTerminate"] = on_terminate
        if delay_date is not UNSET:
            field_dict["delayDate"] = delay_date
        if alert_to_2 is not UNSET:
            field_dict["alertTo2"] = alert_to_2
        if user_delay_date is not UNSET:
            field_dict["userDelayDate"] = user_delay_date
        if alert_to_3 is not UNSET:
            field_dict["alertTo3"] = alert_to_3
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if department is not UNSET:
            field_dict["department"] = department
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if next_server_id is not UNSET:
            field_dict["nextServerId"] = next_server_id
        if version_create_date is not UNSET:
            field_dict["versionCreateDate"] = version_create_date
        if comment_translation_key is not UNSET:
            field_dict["commentTranslationKey"] = comment_translation_key
        if sub_workflow is not UNSET:
            field_dict["subWorkflow"] = sub_workflow
        if label is not UNSET:
            field_dict["label"] = label
        if succ_19 is not UNSET:
            field_dict["succ_19"] = succ_19
        if succ_18 is not UNSET:
            field_dict["succ_18"] = succ_18
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if succ_15 is not UNSET:
            field_dict["succ_15"] = succ_15
        if succ_14 is not UNSET:
            field_dict["succ_14"] = succ_14
        if succ_17 is not UNSET:
            field_dict["succ_17"] = succ_17
        if succ_type is not UNSET:
            field_dict["succType"] = succ_type
        if succ_16 is not UNSET:
            field_dict["succ_16"] = succ_16
        if delay_days is not UNSET:
            field_dict["delayDays"] = delay_days
        if comment is not UNSET:
            field_dict["comment"] = comment
        if node_flags is not UNSET:
            field_dict["nodeFlags"] = node_flags
        if completion_date is not UNSET:
            field_dict["completionDate"] = completion_date
        if on_enter_handle_rollback is not UNSET:
            field_dict["onEnterHandleRollback"] = on_enter_handle_rollback
        if flow_name_translation_key is not UNSET:
            field_dict["flowNameTranslationKey"] = flow_name_translation_key
        if properties is not UNSET:
            field_dict["properties"] = properties
        if label_translation_key is not UNSET:
            field_dict["labelTranslationKey"] = label_translation_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_from_begin = d.pop("alertFromBegin", UNSET)

        succ_11 = d.pop("succ_11", UNSET)

        succ_10 = d.pop("succ_10", UNSET)

        on_exit_handle_rollback = d.pop("onExitHandleRollback", UNSET)

        succ_13 = d.pop("succ_13", UNSET)

        succ_12 = d.pop("succ_12", UNSET)

        active_acl = d.pop("activeAcl", UNSET)

        template_id = d.pop("templateId", UNSET)

        version_name = d.pop("versionName", UNSET)

        ret_val = d.pop("retVal", UNSET)

        on_activate = d.pop("onActivate", UNSET)

        alert_wait_2 = d.pop("alertWait2", UNSET)

        department2 = d.pop("department2", UNSET)

        is_next = d.pop("isNext", UNSET)

        tag = d.pop("tag", UNSET)

        alert_wait_3 = d.pop("alertWait3", UNSET)

        locked = d.pop("locked", UNSET)

        prio = d.pop("prio", UNSET)

        succ_9 = d.pop("succ_9", UNSET)

        icon_id = d.pop("iconId", UNSET)

        department_group = d.pop("departmentGroup", UNSET)

        succ_5 = d.pop("succ_5", UNSET)

        form_spec = d.pop("formSpec", UNSET)

        succ_6 = d.pop("succ_6", UNSET)

        succ_7 = d.pop("succ_7", UNSET)

        alert_wait = d.pop("alertWait", UNSET)

        succ_8 = d.pop("succ_8", UNSET)

        succ_1 = d.pop("succ_1", UNSET)

        succ_2 = d.pop("succ_2", UNSET)

        succ_3 = d.pop("succ_3", UNSET)

        version_tag = d.pop("versionTag", UNSET)

        succ_4 = d.pop("succ_4", UNSET)

        node_type = d.pop("nodeType", UNSET)

        move_cycle_pos_x = d.pop("moveCyclePosX", UNSET)

        flow_name = d.pop("flowName", UNSET)

        succ_0 = d.pop("succ_0", UNSET)

        pos_x = d.pop("posX", UNSET)

        lock_id = d.pop("lockId", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        pos_y = d.pop("posY", UNSET)

        y_n_condition = d.pop("yNCondition", UNSET)

        condition = d.pop("condition", UNSET)

        version_id = d.pop("versionId", UNSET)

        name = d.pop("name", UNSET)

        activate = d.pop("activate", UNSET)

        design_department = d.pop("designDepartment", UNSET)

        alert_to = d.pop("alertTo", UNSET)

        terminate = d.pop("terminate", UNSET)

        version_user_id = d.pop("versionUserId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        user_terminate = d.pop("userTerminate", UNSET)

        in_use_date = d.pop("inUseDate", UNSET)

        elo_obj_id = d.pop("eloObjId", UNSET)

        return_value = d.pop("returnValue", UNSET)

        sub_workflow_template = d.pop("subWorkflowTemplate", UNSET)

        on_terminate = d.pop("onTerminate", UNSET)

        delay_date = d.pop("delayDate", UNSET)

        alert_to_2 = d.pop("alertTo2", UNSET)

        user_delay_date = d.pop("userDelayDate", UNSET)

        alert_to_3 = d.pop("alertTo3", UNSET)

        package_name = d.pop("packageName", UNSET)

        department = d.pop("department", UNSET)

        flow_id = d.pop("flowId", UNSET)

        next_server_id = d.pop("nextServerId", UNSET)

        version_create_date = d.pop("versionCreateDate", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        sub_workflow = d.pop("subWorkflow", UNSET)

        label = d.pop("label", UNSET)

        succ_19 = d.pop("succ_19", UNSET)

        succ_18 = d.pop("succ_18", UNSET)

        deleted = d.pop("deleted", UNSET)

        succ_15 = d.pop("succ_15", UNSET)

        succ_14 = d.pop("succ_14", UNSET)

        succ_17 = d.pop("succ_17", UNSET)

        succ_type = d.pop("succType", UNSET)

        succ_16 = d.pop("succ_16", UNSET)

        delay_days = d.pop("delayDays", UNSET)

        comment = d.pop("comment", UNSET)

        node_flags = d.pop("nodeFlags", UNSET)

        completion_date = d.pop("completionDate", UNSET)

        on_enter_handle_rollback = d.pop("onEnterHandleRollback", UNSET)

        flow_name_translation_key = d.pop("flowNameTranslationKey", UNSET)

        properties = d.pop("properties", UNSET)

        label_translation_key = d.pop("labelTranslationKey", UNSET)

        work_flow_active_doc = cls(
            alert_from_begin=alert_from_begin,
            succ_11=succ_11,
            succ_10=succ_10,
            on_exit_handle_rollback=on_exit_handle_rollback,
            succ_13=succ_13,
            succ_12=succ_12,
            active_acl=active_acl,
            template_id=template_id,
            version_name=version_name,
            ret_val=ret_val,
            on_activate=on_activate,
            alert_wait_2=alert_wait_2,
            department2=department2,
            is_next=is_next,
            tag=tag,
            alert_wait_3=alert_wait_3,
            locked=locked,
            prio=prio,
            succ_9=succ_9,
            icon_id=icon_id,
            department_group=department_group,
            succ_5=succ_5,
            form_spec=form_spec,
            succ_6=succ_6,
            succ_7=succ_7,
            alert_wait=alert_wait,
            succ_8=succ_8,
            succ_1=succ_1,
            succ_2=succ_2,
            succ_3=succ_3,
            version_tag=version_tag,
            succ_4=succ_4,
            node_type=node_type,
            move_cycle_pos_x=move_cycle_pos_x,
            flow_name=flow_name,
            succ_0=succ_0,
            pos_x=pos_x,
            lock_id=lock_id,
            name_translation_key=name_translation_key,
            pos_y=pos_y,
            y_n_condition=y_n_condition,
            condition=condition,
            version_id=version_id,
            name=name,
            activate=activate,
            design_department=design_department,
            alert_to=alert_to,
            terminate=terminate,
            version_user_id=version_user_id,
            node_id=node_id,
            user_terminate=user_terminate,
            in_use_date=in_use_date,
            elo_obj_id=elo_obj_id,
            return_value=return_value,
            sub_workflow_template=sub_workflow_template,
            on_terminate=on_terminate,
            delay_date=delay_date,
            alert_to_2=alert_to_2,
            user_delay_date=user_delay_date,
            alert_to_3=alert_to_3,
            package_name=package_name,
            department=department,
            flow_id=flow_id,
            next_server_id=next_server_id,
            version_create_date=version_create_date,
            comment_translation_key=comment_translation_key,
            sub_workflow=sub_workflow,
            label=label,
            succ_19=succ_19,
            succ_18=succ_18,
            deleted=deleted,
            succ_15=succ_15,
            succ_14=succ_14,
            succ_17=succ_17,
            succ_type=succ_type,
            succ_16=succ_16,
            delay_days=delay_days,
            comment=comment,
            node_flags=node_flags,
            completion_date=completion_date,
            on_enter_handle_rollback=on_enter_handle_rollback,
            flow_name_translation_key=flow_name_translation_key,
            properties=properties,
            label_translation_key=label_translation_key,
        )

        work_flow_active_doc.additional_properties = d
        return work_flow_active_doc

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
