from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowActiveDoc")


@_attrs_define
class WorkFlowActiveDoc:
    """Internal class.

    Attributes:
        flow_id (Union[Unset, int]): Workflow ID.
            DB column: wf_flowid
        node_id (Union[Unset, int]): Node ID.
            DB column: wf_nodeid
        flow_name (Union[Unset, str]): Workflow name.
            DB column: wf_flow_name
        name (Union[Unset, str]): Node name (work instruction).
            DB column: wf_name
        node_type (Union[Unset, int]): Node type (begin node, split node, etc.).
            DB column: wf_node_type
        succ_type (Union[Unset, int]): This value depends on the node type and is not processed anymore by Indexserver.
            It is written for compability with
             workflows of older CLIENT versions. DB column: wf_succ_type
        department (Union[Unset, int]): ID of user who has to process the node. Might be a group ID too. Only valid for
            person nodes.
            DB column:
             wf_department
        alert_to (Union[Unset, int]): ID of user who should be informed, if a time-limit exceeds.
            It might be the time-limit for the entire workflow or
             for a signle person node. DB column: wf_alert_to
        alert_from_begin (Union[Unset, int]): Time-limt for the entire workflow in minutes. This value is only valid for
            the begin node.
            DB column:
             wf_alert_from_begin
        alert_wait (Union[Unset, int]): Time-limit for a single node. This value is only valid for person nodes.
            DB column: wf_alert_wait
        y_n_condition (Union[Unset, str]): IF-Nodes: test condition, person nodes: index values or scripts, split nodes:
            workflow status.
            DB column:
             wf_yesnocondition
        condition (Union[Unset, str]): Contains the ACL of the workflow template. Only valid for begin nodes.
            DB column: wf_condition
        comment (Union[Unset, str]): Comment, only valid for person nodes.
            DB column: wf_comment
        succ_0 (Union[Unset, int]): Successor node(s) succ_0 ... Succ 19 DB column: wf_succ_0 This mebers are moved into
            WorkFlowNodeMatrix.
            They are
             still here due to compatibiltiy with older stream versions.
        succ_1 (Union[Unset, int]): DB column: wf_succ_1
        succ_2 (Union[Unset, int]): DB column: wf_succ_2
        succ_3 (Union[Unset, int]): DB column: wf_succ_3
        succ_4 (Union[Unset, int]): DB column: wf_succ_4
        succ_5 (Union[Unset, int]): DB column: wf_succ_5
        succ_6 (Union[Unset, int]): DB column: wf_succ_6
        succ_7 (Union[Unset, int]): DB column: wf_succ_7
        succ_8 (Union[Unset, int]): DB column: wf_succ_8
        succ_9 (Union[Unset, int]): DB column: wf_succ_9
        succ_10 (Union[Unset, int]): DB column: wf_succ_10
        succ_11 (Union[Unset, int]): DB column: wf_succ_11
        succ_12 (Union[Unset, int]): DB column: wf_succ_12
        succ_13 (Union[Unset, int]): DB column: wf_succ_13
        succ_14 (Union[Unset, int]): DB column: wf_succ_14
        succ_15 (Union[Unset, int]): DB column: wf_succ_15
        succ_16 (Union[Unset, int]): DB column: wf_succ_16
        succ_17 (Union[Unset, int]): DB column: wf_succ_17
        succ_18 (Union[Unset, int]): DB column: wf_succ_18
        succ_19 (Union[Unset, int]): DB column: wf_succ_19
        locked (Union[Unset, int]): If node is locked, it contains 1 otherwise 0 DB column: wf_locked
        pos_x (Union[Unset, int]): Node X position in designer view.
            DB column: pos_x
        pos_y (Union[Unset, int]): Node Y position in designer view.
            DB column: pos_y
        on_activate (Union[Unset, str]): Name of script to be executed, if the node is activated (entered).
            DB column: wf_ev_on_activate
        on_terminate (Union[Unset, str]): Name of script to be executed, if the node is leaved (exited).
            DB column: wf_ev_on_terminate
        node_flags (Union[Unset, int]): Node flags.
            DB column: wf_nodeflags
        elo_obj_id (Union[Unset, int]): Associated object ID. Only valid for non-template workflows.
            DB column: wf_eloobjid
        lock_id (Union[Unset, int]): User ID of the owner of the lock.
            DB column: wf_locked_owner
        is_next (Union[Unset, int]): Contains 1, if this node is active.
            DB column: wf_is_next
        activate (Union[Unset, int]): ELO-date when the node was entered.
            DB column: wf_activate
        terminate (Union[Unset, int]): ELO-date when the node was exited.
            DB column: wf_terminate
        in_use_date (Union[Unset, int]): ELO-date when the node was visited the last time.
            DB column: wf_in_use_date
        completion_date (Union[Unset, int]): ELO-date when the workflow was finished. All nodes contain the same value.
            DB column: wf_completion_date
        template_id (Union[Unset, int]): Workflow template ID. Not valid for template workflows.
            For active and finished workflows this member specifies the
             template ID that was used to start the workflow. If the workflow is started as an adhoc workflow, this member
            is 0
             and flags contains the bit FLAG_ROOT_ADHOC. DB column: wf_template
        user_terminate (Union[Unset, str]): The ID of the user who has forwarded the node. Not valid for template
            workflows. Only valid for person nodes.
            DB
             column: wf_userterminate
        tag (Union[Unset, int]): reserved.
            DB column: wf_tag
        design_department (Union[Unset, int]): A group ID or user ID that was originally assigned in the designer.
            DB column: wf_designdepartment
        move_cycle_pos_x (Union[Unset, int]): If a cycle is re-entered, the nodes in the cycle are duplicated.
            The copied nodes will be placed in the designer
             moved by this value to the right. If this value is 0, the nodes are moved 60 points right and 20 points up. DB
             column: wf_dx
        department2 (Union[Unset, int]): A group ID to constrain access to the node. Only members of this group are
            allowed to see and process the node.
            Only valid for person nodes. DB column: wf_department2
        delay_days (Union[Unset, int]): An active person node (Activate is set) might be displayed to the user delayed
            by this number of days.
            Only valid
             for person nodes. DB column: wf_delaydays
        delay_date (Union[Unset, int]): Activate + DelayDays. Not valid for template workflows. Only valid for person
            nodes.
            DB column: wf_duedate
        deleted (Union[Unset, int]): Flag that indicates whether the workflow template is deleted.
            If the value is not 0, the workflow template is
             deleted. Only valid for template workflows. DB column: wf_deleted
        prio (Union[Unset, int]): Workflow priority: 0...high, 1...medium, 2...low.
            DB column: wf_prio
        user_delay_date (Union[Unset, int]): The workflow node is deferred until this date. ELO date format.
            DB column: wf_user_delaydate
        version_id (Union[Unset, int]): Version ID.
        version_name (Union[Unset, str]): Version comment.
        alert_to_2 (Union[Unset, int]): ID of user who should be informed, if the time-limit alertWait2 exceeds.
        alert_wait_2 (Union[Unset, int]): Second Time-limit for a person node or begin node.
        alert_to_3 (Union[Unset, int]): ID of user who should be informed, if the time-limit alertWait2 exceeds.
        alert_wait_3 (Union[Unset, int]): Third Time-limit for a person node or begin node.
        next_server_id (Union[Unset, str]): Next server name. This value is used in replication environments and defines
            the ID of the next server (resp.
            replication branch) where the workflow continues processing.
        version_tag (Union[Unset, str]): Version number.
        version_user_id (Union[Unset, int]): ID of the user who created the workflow version.
        version_create_date (Union[Unset, int]): ID of the user who created the workflow version.
        icon_id (Union[Unset, str]): Object-GUID of an icon file that is displayed in the designer.
        form_spec (Union[Unset, str]): User defined data to be stored in the database.
        flow_name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFDiagram#name}.
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#name}.
        comment_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#comment}.
        label (Union[Unset, str]): Display name by forwarding.
        properties (Union[Unset, str]): Properties field of node.
        department_group (Union[Unset, int]): Grouping of nodes for function takeWorkFlowNode.
        ret_val (Union[Unset, int]): Return value of an end node.
        return_value (Union[Unset, str]): Return value of an end node.
        sub_workflow (Union[Unset, int]): ID of the active sub-workflow.
        label_translation_key (Union[Unset, str]): Translation-keyword for {@link WorkFlowActiveDoc#label}.
        sub_workflow_template (Union[Unset, int]): ID of the sub-workflow template.
        active_acl (Union[Unset, str]): Contains the ACL of the workflow. Only valid for begin nodes.
        package_name (Union[Unset, str]): PackageName of a Workflow, only used for workflow templates
    """

    flow_id: Union[Unset, int] = UNSET
    node_id: Union[Unset, int] = UNSET
    flow_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_type: Union[Unset, int] = UNSET
    succ_type: Union[Unset, int] = UNSET
    department: Union[Unset, int] = UNSET
    alert_to: Union[Unset, int] = UNSET
    alert_from_begin: Union[Unset, int] = UNSET
    alert_wait: Union[Unset, int] = UNSET
    y_n_condition: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    succ_0: Union[Unset, int] = UNSET
    succ_1: Union[Unset, int] = UNSET
    succ_2: Union[Unset, int] = UNSET
    succ_3: Union[Unset, int] = UNSET
    succ_4: Union[Unset, int] = UNSET
    succ_5: Union[Unset, int] = UNSET
    succ_6: Union[Unset, int] = UNSET
    succ_7: Union[Unset, int] = UNSET
    succ_8: Union[Unset, int] = UNSET
    succ_9: Union[Unset, int] = UNSET
    succ_10: Union[Unset, int] = UNSET
    succ_11: Union[Unset, int] = UNSET
    succ_12: Union[Unset, int] = UNSET
    succ_13: Union[Unset, int] = UNSET
    succ_14: Union[Unset, int] = UNSET
    succ_15: Union[Unset, int] = UNSET
    succ_16: Union[Unset, int] = UNSET
    succ_17: Union[Unset, int] = UNSET
    succ_18: Union[Unset, int] = UNSET
    succ_19: Union[Unset, int] = UNSET
    locked: Union[Unset, int] = UNSET
    pos_x: Union[Unset, int] = UNSET
    pos_y: Union[Unset, int] = UNSET
    on_activate: Union[Unset, str] = UNSET
    on_terminate: Union[Unset, str] = UNSET
    node_flags: Union[Unset, int] = UNSET
    elo_obj_id: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    is_next: Union[Unset, int] = UNSET
    activate: Union[Unset, int] = UNSET
    terminate: Union[Unset, int] = UNSET
    in_use_date: Union[Unset, int] = UNSET
    completion_date: Union[Unset, int] = UNSET
    template_id: Union[Unset, int] = UNSET
    user_terminate: Union[Unset, str] = UNSET
    tag: Union[Unset, int] = UNSET
    design_department: Union[Unset, int] = UNSET
    move_cycle_pos_x: Union[Unset, int] = UNSET
    department2: Union[Unset, int] = UNSET
    delay_days: Union[Unset, int] = UNSET
    delay_date: Union[Unset, int] = UNSET
    deleted: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    user_delay_date: Union[Unset, int] = UNSET
    version_id: Union[Unset, int] = UNSET
    version_name: Union[Unset, str] = UNSET
    alert_to_2: Union[Unset, int] = UNSET
    alert_wait_2: Union[Unset, int] = UNSET
    alert_to_3: Union[Unset, int] = UNSET
    alert_wait_3: Union[Unset, int] = UNSET
    next_server_id: Union[Unset, str] = UNSET
    version_tag: Union[Unset, str] = UNSET
    version_user_id: Union[Unset, int] = UNSET
    version_create_date: Union[Unset, int] = UNSET
    icon_id: Union[Unset, str] = UNSET
    form_spec: Union[Unset, str] = UNSET
    flow_name_translation_key: Union[Unset, str] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    properties: Union[Unset, str] = UNSET
    department_group: Union[Unset, int] = UNSET
    ret_val: Union[Unset, int] = UNSET
    return_value: Union[Unset, str] = UNSET
    sub_workflow: Union[Unset, int] = UNSET
    label_translation_key: Union[Unset, str] = UNSET
    sub_workflow_template: Union[Unset, int] = UNSET
    active_acl: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flow_id = self.flow_id
        node_id = self.node_id
        flow_name = self.flow_name
        name = self.name
        node_type = self.node_type
        succ_type = self.succ_type
        department = self.department
        alert_to = self.alert_to
        alert_from_begin = self.alert_from_begin
        alert_wait = self.alert_wait
        y_n_condition = self.y_n_condition
        condition = self.condition
        comment = self.comment
        succ_0 = self.succ_0
        succ_1 = self.succ_1
        succ_2 = self.succ_2
        succ_3 = self.succ_3
        succ_4 = self.succ_4
        succ_5 = self.succ_5
        succ_6 = self.succ_6
        succ_7 = self.succ_7
        succ_8 = self.succ_8
        succ_9 = self.succ_9
        succ_10 = self.succ_10
        succ_11 = self.succ_11
        succ_12 = self.succ_12
        succ_13 = self.succ_13
        succ_14 = self.succ_14
        succ_15 = self.succ_15
        succ_16 = self.succ_16
        succ_17 = self.succ_17
        succ_18 = self.succ_18
        succ_19 = self.succ_19
        locked = self.locked
        pos_x = self.pos_x
        pos_y = self.pos_y
        on_activate = self.on_activate
        on_terminate = self.on_terminate
        node_flags = self.node_flags
        elo_obj_id = self.elo_obj_id
        lock_id = self.lock_id
        is_next = self.is_next
        activate = self.activate
        terminate = self.terminate
        in_use_date = self.in_use_date
        completion_date = self.completion_date
        template_id = self.template_id
        user_terminate = self.user_terminate
        tag = self.tag
        design_department = self.design_department
        move_cycle_pos_x = self.move_cycle_pos_x
        department2 = self.department2
        delay_days = self.delay_days
        delay_date = self.delay_date
        deleted = self.deleted
        prio = self.prio
        user_delay_date = self.user_delay_date
        version_id = self.version_id
        version_name = self.version_name
        alert_to_2 = self.alert_to_2
        alert_wait_2 = self.alert_wait_2
        alert_to_3 = self.alert_to_3
        alert_wait_3 = self.alert_wait_3
        next_server_id = self.next_server_id
        version_tag = self.version_tag
        version_user_id = self.version_user_id
        version_create_date = self.version_create_date
        icon_id = self.icon_id
        form_spec = self.form_spec
        flow_name_translation_key = self.flow_name_translation_key
        name_translation_key = self.name_translation_key
        comment_translation_key = self.comment_translation_key
        label = self.label
        properties = self.properties
        department_group = self.department_group
        ret_val = self.ret_val
        return_value = self.return_value
        sub_workflow = self.sub_workflow
        label_translation_key = self.label_translation_key
        sub_workflow_template = self.sub_workflow_template
        active_acl = self.active_acl
        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if succ_type is not UNSET:
            field_dict["succType"] = succ_type
        if department is not UNSET:
            field_dict["department"] = department
        if alert_to is not UNSET:
            field_dict["alertTo"] = alert_to
        if alert_from_begin is not UNSET:
            field_dict["alertFromBegin"] = alert_from_begin
        if alert_wait is not UNSET:
            field_dict["alertWait"] = alert_wait
        if y_n_condition is not UNSET:
            field_dict["yNCondition"] = y_n_condition
        if condition is not UNSET:
            field_dict["condition"] = condition
        if comment is not UNSET:
            field_dict["comment"] = comment
        if succ_0 is not UNSET:
            field_dict["succ_0"] = succ_0
        if succ_1 is not UNSET:
            field_dict["succ_1"] = succ_1
        if succ_2 is not UNSET:
            field_dict["succ_2"] = succ_2
        if succ_3 is not UNSET:
            field_dict["succ_3"] = succ_3
        if succ_4 is not UNSET:
            field_dict["succ_4"] = succ_4
        if succ_5 is not UNSET:
            field_dict["succ_5"] = succ_5
        if succ_6 is not UNSET:
            field_dict["succ_6"] = succ_6
        if succ_7 is not UNSET:
            field_dict["succ_7"] = succ_7
        if succ_8 is not UNSET:
            field_dict["succ_8"] = succ_8
        if succ_9 is not UNSET:
            field_dict["succ_9"] = succ_9
        if succ_10 is not UNSET:
            field_dict["succ_10"] = succ_10
        if succ_11 is not UNSET:
            field_dict["succ_11"] = succ_11
        if succ_12 is not UNSET:
            field_dict["succ_12"] = succ_12
        if succ_13 is not UNSET:
            field_dict["succ_13"] = succ_13
        if succ_14 is not UNSET:
            field_dict["succ_14"] = succ_14
        if succ_15 is not UNSET:
            field_dict["succ_15"] = succ_15
        if succ_16 is not UNSET:
            field_dict["succ_16"] = succ_16
        if succ_17 is not UNSET:
            field_dict["succ_17"] = succ_17
        if succ_18 is not UNSET:
            field_dict["succ_18"] = succ_18
        if succ_19 is not UNSET:
            field_dict["succ_19"] = succ_19
        if locked is not UNSET:
            field_dict["locked"] = locked
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if on_activate is not UNSET:
            field_dict["onActivate"] = on_activate
        if on_terminate is not UNSET:
            field_dict["onTerminate"] = on_terminate
        if node_flags is not UNSET:
            field_dict["nodeFlags"] = node_flags
        if elo_obj_id is not UNSET:
            field_dict["eloObjId"] = elo_obj_id
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if is_next is not UNSET:
            field_dict["isNext"] = is_next
        if activate is not UNSET:
            field_dict["activate"] = activate
        if terminate is not UNSET:
            field_dict["terminate"] = terminate
        if in_use_date is not UNSET:
            field_dict["inUseDate"] = in_use_date
        if completion_date is not UNSET:
            field_dict["completionDate"] = completion_date
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if user_terminate is not UNSET:
            field_dict["userTerminate"] = user_terminate
        if tag is not UNSET:
            field_dict["tag"] = tag
        if design_department is not UNSET:
            field_dict["designDepartment"] = design_department
        if move_cycle_pos_x is not UNSET:
            field_dict["moveCyclePosX"] = move_cycle_pos_x
        if department2 is not UNSET:
            field_dict["department2"] = department2
        if delay_days is not UNSET:
            field_dict["delayDays"] = delay_days
        if delay_date is not UNSET:
            field_dict["delayDate"] = delay_date
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if prio is not UNSET:
            field_dict["prio"] = prio
        if user_delay_date is not UNSET:
            field_dict["userDelayDate"] = user_delay_date
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if alert_to_2 is not UNSET:
            field_dict["alertTo2"] = alert_to_2
        if alert_wait_2 is not UNSET:
            field_dict["alertWait2"] = alert_wait_2
        if alert_to_3 is not UNSET:
            field_dict["alertTo3"] = alert_to_3
        if alert_wait_3 is not UNSET:
            field_dict["alertWait3"] = alert_wait_3
        if next_server_id is not UNSET:
            field_dict["nextServerId"] = next_server_id
        if version_tag is not UNSET:
            field_dict["versionTag"] = version_tag
        if version_user_id is not UNSET:
            field_dict["versionUserId"] = version_user_id
        if version_create_date is not UNSET:
            field_dict["versionCreateDate"] = version_create_date
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if form_spec is not UNSET:
            field_dict["formSpec"] = form_spec
        if flow_name_translation_key is not UNSET:
            field_dict["flowNameTranslationKey"] = flow_name_translation_key
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if comment_translation_key is not UNSET:
            field_dict["commentTranslationKey"] = comment_translation_key
        if label is not UNSET:
            field_dict["label"] = label
        if properties is not UNSET:
            field_dict["properties"] = properties
        if department_group is not UNSET:
            field_dict["departmentGroup"] = department_group
        if ret_val is not UNSET:
            field_dict["retVal"] = ret_val
        if return_value is not UNSET:
            field_dict["returnValue"] = return_value
        if sub_workflow is not UNSET:
            field_dict["subWorkflow"] = sub_workflow
        if label_translation_key is not UNSET:
            field_dict["labelTranslationKey"] = label_translation_key
        if sub_workflow_template is not UNSET:
            field_dict["subWorkflowTemplate"] = sub_workflow_template
        if active_acl is not UNSET:
            field_dict["activeAcl"] = active_acl
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flow_id = d.pop("flowId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        flow_name = d.pop("flowName", UNSET)

        name = d.pop("name", UNSET)

        node_type = d.pop("nodeType", UNSET)

        succ_type = d.pop("succType", UNSET)

        department = d.pop("department", UNSET)

        alert_to = d.pop("alertTo", UNSET)

        alert_from_begin = d.pop("alertFromBegin", UNSET)

        alert_wait = d.pop("alertWait", UNSET)

        y_n_condition = d.pop("yNCondition", UNSET)

        condition = d.pop("condition", UNSET)

        comment = d.pop("comment", UNSET)

        succ_0 = d.pop("succ_0", UNSET)

        succ_1 = d.pop("succ_1", UNSET)

        succ_2 = d.pop("succ_2", UNSET)

        succ_3 = d.pop("succ_3", UNSET)

        succ_4 = d.pop("succ_4", UNSET)

        succ_5 = d.pop("succ_5", UNSET)

        succ_6 = d.pop("succ_6", UNSET)

        succ_7 = d.pop("succ_7", UNSET)

        succ_8 = d.pop("succ_8", UNSET)

        succ_9 = d.pop("succ_9", UNSET)

        succ_10 = d.pop("succ_10", UNSET)

        succ_11 = d.pop("succ_11", UNSET)

        succ_12 = d.pop("succ_12", UNSET)

        succ_13 = d.pop("succ_13", UNSET)

        succ_14 = d.pop("succ_14", UNSET)

        succ_15 = d.pop("succ_15", UNSET)

        succ_16 = d.pop("succ_16", UNSET)

        succ_17 = d.pop("succ_17", UNSET)

        succ_18 = d.pop("succ_18", UNSET)

        succ_19 = d.pop("succ_19", UNSET)

        locked = d.pop("locked", UNSET)

        pos_x = d.pop("posX", UNSET)

        pos_y = d.pop("posY", UNSET)

        on_activate = d.pop("onActivate", UNSET)

        on_terminate = d.pop("onTerminate", UNSET)

        node_flags = d.pop("nodeFlags", UNSET)

        elo_obj_id = d.pop("eloObjId", UNSET)

        lock_id = d.pop("lockId", UNSET)

        is_next = d.pop("isNext", UNSET)

        activate = d.pop("activate", UNSET)

        terminate = d.pop("terminate", UNSET)

        in_use_date = d.pop("inUseDate", UNSET)

        completion_date = d.pop("completionDate", UNSET)

        template_id = d.pop("templateId", UNSET)

        user_terminate = d.pop("userTerminate", UNSET)

        tag = d.pop("tag", UNSET)

        design_department = d.pop("designDepartment", UNSET)

        move_cycle_pos_x = d.pop("moveCyclePosX", UNSET)

        department2 = d.pop("department2", UNSET)

        delay_days = d.pop("delayDays", UNSET)

        delay_date = d.pop("delayDate", UNSET)

        deleted = d.pop("deleted", UNSET)

        prio = d.pop("prio", UNSET)

        user_delay_date = d.pop("userDelayDate", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_name = d.pop("versionName", UNSET)

        alert_to_2 = d.pop("alertTo2", UNSET)

        alert_wait_2 = d.pop("alertWait2", UNSET)

        alert_to_3 = d.pop("alertTo3", UNSET)

        alert_wait_3 = d.pop("alertWait3", UNSET)

        next_server_id = d.pop("nextServerId", UNSET)

        version_tag = d.pop("versionTag", UNSET)

        version_user_id = d.pop("versionUserId", UNSET)

        version_create_date = d.pop("versionCreateDate", UNSET)

        icon_id = d.pop("iconId", UNSET)

        form_spec = d.pop("formSpec", UNSET)

        flow_name_translation_key = d.pop("flowNameTranslationKey", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        label = d.pop("label", UNSET)

        properties = d.pop("properties", UNSET)

        department_group = d.pop("departmentGroup", UNSET)

        ret_val = d.pop("retVal", UNSET)

        return_value = d.pop("returnValue", UNSET)

        sub_workflow = d.pop("subWorkflow", UNSET)

        label_translation_key = d.pop("labelTranslationKey", UNSET)

        sub_workflow_template = d.pop("subWorkflowTemplate", UNSET)

        active_acl = d.pop("activeAcl", UNSET)

        package_name = d.pop("packageName", UNSET)

        work_flow_active_doc = cls(
            flow_id=flow_id,
            node_id=node_id,
            flow_name=flow_name,
            name=name,
            node_type=node_type,
            succ_type=succ_type,
            department=department,
            alert_to=alert_to,
            alert_from_begin=alert_from_begin,
            alert_wait=alert_wait,
            y_n_condition=y_n_condition,
            condition=condition,
            comment=comment,
            succ_0=succ_0,
            succ_1=succ_1,
            succ_2=succ_2,
            succ_3=succ_3,
            succ_4=succ_4,
            succ_5=succ_5,
            succ_6=succ_6,
            succ_7=succ_7,
            succ_8=succ_8,
            succ_9=succ_9,
            succ_10=succ_10,
            succ_11=succ_11,
            succ_12=succ_12,
            succ_13=succ_13,
            succ_14=succ_14,
            succ_15=succ_15,
            succ_16=succ_16,
            succ_17=succ_17,
            succ_18=succ_18,
            succ_19=succ_19,
            locked=locked,
            pos_x=pos_x,
            pos_y=pos_y,
            on_activate=on_activate,
            on_terminate=on_terminate,
            node_flags=node_flags,
            elo_obj_id=elo_obj_id,
            lock_id=lock_id,
            is_next=is_next,
            activate=activate,
            terminate=terminate,
            in_use_date=in_use_date,
            completion_date=completion_date,
            template_id=template_id,
            user_terminate=user_terminate,
            tag=tag,
            design_department=design_department,
            move_cycle_pos_x=move_cycle_pos_x,
            department2=department2,
            delay_days=delay_days,
            delay_date=delay_date,
            deleted=deleted,
            prio=prio,
            user_delay_date=user_delay_date,
            version_id=version_id,
            version_name=version_name,
            alert_to_2=alert_to_2,
            alert_wait_2=alert_wait_2,
            alert_to_3=alert_to_3,
            alert_wait_3=alert_wait_3,
            next_server_id=next_server_id,
            version_tag=version_tag,
            version_user_id=version_user_id,
            version_create_date=version_create_date,
            icon_id=icon_id,
            form_spec=form_spec,
            flow_name_translation_key=flow_name_translation_key,
            name_translation_key=name_translation_key,
            comment_translation_key=comment_translation_key,
            label=label,
            properties=properties,
            department_group=department_group,
            ret_val=ret_val,
            return_value=return_value,
            sub_workflow=sub_workflow,
            label_translation_key=label_translation_key,
            sub_workflow_template=sub_workflow_template,
            active_acl=active_acl,
            package_name=package_name,
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
