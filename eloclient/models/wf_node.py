from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_time_limit import WFTimeLimit


T = TypeVar("T", bound="WFNode")


@_attrs_define
class WFNode:
    """<p>
    Objects of this class represent a workflow node.
     </p>

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            delay_date_iso (Union[Unset, str]): The node is displayed to the user at this date.
                This date is computed by enterDateIso +
                 delayDays. This member is only valid for person nodes. Read-only.
            return_value (Union[Unset, str]): Return value of a sub-workflow.
                The value defines the name of the successor node of the
                 call-node {@link WFNodeC#TYPE_CALL_SUB_WORKFLOW} that will be activated when the sub-workflow
                 returns. If the sub-workflow returns a node name that does not exist in the main workflow, a
                 new person node is inserted between the call-node and its successors. This new node is named as
                 the return value and is assigned to the workflow owner.
            on_exit (Union[Unset, str]): A script or plugin name that is called, if a workflow node is exited.
                <p>
                 In order to capture this workflow event in JavaScript, store a script file that defines a
                 function named onExitNode in a sub-folder of "Indexserver Scripting Base/_ALL" or "Indexserver
                 Scripting Base/instancename".

                 <pre>
                 <code class="example">
                 function onExitNode(ci, userId, workflow, nodeId) {
                   // ci       ... ClientInfo object of the user that forwards the workflow.
                   // userId   ... The calling user's ID (Integer)
                   // workflow ... WFDiagram object
                   // nodeId   ... The deactivated node ID (Integer)
                 ...
                 }
                 </code>
                 </pre>

                 See Indexserver Programming Manual for more information.
                 </p>
                 <p>
                 If onExit starts with a plugin's Bundle-SymbolicName, the event is delegated to function
                 {@link de.elo.ix.client.plugin.WorkflowNodeEvents#onExitWorkflowNode} of a
                 <code>WorkflowNodeEvents</code> object returned from a call to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. Optionally, a path can be
                 appended to the Bundle-SymbolicName which is passed to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. This path has to start with a
                 forward slash. E.g. onEnter="com.partner.wfevents/invoice-solution".
                 </p>
                 This member is valid for all node types.
            process_on_server_id (Union[Unset, str]): Server ID (resp. replication branch).
                If the node is activated, the server ID is set to this
                 value. This member is only valid for nodes of type WFNodeC.TYPE_SET_SERVER_ID.
            yes_no_condition (Union[Unset, str]): A value depending on the type of the node.
                <p>
                 {@link WFNodeC#TYPE_IFNODE}: test condition. Numeric values must be formatted according to the servers locale.
                 Date values of {@link AspectLineC#TYPE_ISO_DATE_ONLY} or {@link AspectLineC#TYPE_ISO_DATE_TIME} must be given
                as
                 ISO date values in timezone UTC.
                 </p><p>
                 {@link WFNodeC#TYPE_SPLITNODE}: sets the workflow status to this value.
                 </p><p>
                 {@link WFNodeC#getTYPE_BEGINNODE()}: contains workflow status.
                 </p><p>
                 {@link WFNodeC#TYPE_CYCLE}: condition that evaluates true to leave the cycle.
                 </p>
            time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
            flags (Union[Unset, int]): Control flags for the node, a combination of WFNodeC.FLAG_* constants.
                For start nodes
                 (TYPE_BEGINNODE), the flags should be specified in WFDiagram.flags. To ensure compatibility
                 with older client programs, the WFNode.flags of the start node are or-ed with the
                 WFDiagram.flags. This member is valid for all node types.
            on_exit_handle_rollback (Union[Unset, str]): A script or plugin name that is called when an error occurs inside
                a workflow script.
                All
                 onExitHandleRollback scripts, from one person node to the next person node, are stored in a
                 temporary queue and all will get executed if an error inside a script occurs. The
                 onExitHandleRollback script is not meant for dealing with an error in the onExit Script, the
                 script will only get stored in the temporary queue if the onExit script was executed without
                 any issues.
                 <p>
                 In order to capture this workflow event in JavaScript, store a script file that defines a
                 function named onExitHandleRollbackNode in a sub-folder of "Indexserver Scripting Base/_ALL" or
                 "Indexserver Scripting Base/instancename".

                 <pre>
                 <code class="example">
                 function onExitHandleRollbackNode(ci, userId, workflow, nodeId) {
                   // ci       ... ClientInfo object of the user that forwards the workflow.
                   // userId   ... The calling user's ID (Integer)
                   // workflow ... WFDiagram object
                   // nodeId   ... The deactivated node ID (Integer)
                 ...
                 }
                 </code>
                 </pre>

                 See Indexserver Programming Manual for more information.
                 </p>
                 <p>
                 If onExitHandleRollback starts with a plugin's Bundle-SymbolicName, the event is delegated to
                 function {@link de.elo.ix.client.plugin.WorkflowNodeEvents#onExitHandleRollbackWorkflowNode} of
                 a <code>WorkflowNodeEvents</code> object returned from a call to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. Optionally, a path can be
                 appended to the Bundle-SymbolicName which is passed to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. This path has to start with a
                 forward slash. E.g. onExitHandleRollback="com.partner.wfevents/invoice-solution".
                 </p>
                 This member is valid for all node types.
            user_delay_date_iso (Union[Unset, str]): The workflow node is deferred until this date.
                This member is only valid for person nodes in
                 active or finished workflows. ISO date format.
            over_time_limit (Union[Unset, bool]): True, if the node exceeds the time limit.
                This member is only valid for person nodes in active
                 or finished workflows. Read-only.
            type (Union[Unset, int]): The node type. This member is set to one of the TYPE_* constants in WFNodeC.
            ret_val (Union[Unset, int]): Return value of an end node. Only valid for TYPE_END.
            enter_date_iso (Union[Unset, str]): The node was activated on this date. This member is valid for all node
                types.
            department2 (Union[Unset, int]): A group ID to constrain access to the node.
                Only members of this group are allowed to see and
                 process the node. Only valid for person nodes.
            id (Union[Unset, int]): Node ID. This member is valid for all node types.
            is_next (Union[Unset, int]): The activation state of the node. This member is valid for all node types.
            tag (Union[Unset, int]): reserved.
                DB column: wf_tag
            prio (Union[Unset, int]): Node priortiy: 0...high, 1...medium, 2...low.
                Only valid for person nodes,
                 type=={@link WFNodeC#TYPE_PERSONNODE}. The user assigned to the person node can change this
                 value by conn.ix().forwardWorkflowNode():

                 <pre>
                 <code>
                  WFEditNode editNode = conn.ix().beginForwardWorkflowNode(flowId, nodeId, null, LockC.NO);
                  WFNode activeNode = editNode.getNode();
                  activeNode.setPrio(activeNode.getPrio()-1); // One level higher.
                  ForwardWorkflowNodeInfo fwdInfo = new ForwardWorkflowNodeInfo();
                  fwdInfo.setNode(activeNode);
                  conn.ix().forwardWorkflowNode(wfActive.getId(), activeNode.getId(), fwdInfo, LockC.NO);

                 </code>
                 </pre>
            obj_key_names (Union[Unset, List[str]]):
            icon_id (Union[Unset, str]): Object-GUID of an icon file that is displayed in the designer.
            time_limit_iso (Union[Unset, str]): After this date the node exceeds the time-limit for processing.
                This member is only valid for
                 person nodes. Read-only.
            script_names (Union[Unset, List[str]]):
            department_group (Union[Unset, int]): Grouping of nodes for function takeWorkFlowNode.
                A non-zero value binds nodes with the same
                 value to a group of nodes that is evaluated in
                 {@link IXServicePortIF#takeWorkFlowNode(ClientInfo, int, int, String, int, LockZ)}. The
                 function takeWorkFlowNodes takes - in addition to the given node - all nodes with the same
                 group assignment specified by this member. This member is only used as a marker and is not
                 interpreted as a group or user ID.
            nb_of_dones_to_exit (Union[Unset, int]): The number of predecessor nodes that must be processed to forward this
                collector node.
                A value
                 of -1 means that all predecessor nodes must be processed. If set to 0, the collect node
                 switches when it is activated regardless of the state of the predecessor nodes. This member is
                 only valid for collect nodes.
            form_spec (Union[Unset, str]): Multipurpose field.
                <p>
                 If the node is a collect node (type={@link WFNodeC#TYPE_COLLECTNODE}), formSpec contains a
                 comma separated list of node IDs. This nodes are deactivated when the collect node forwards the
                 workflow. In addition to a list of IDs, the value of {@link WFNodeC#DEACTIVATE_ALL_PREDS}
                 causes to deactivate all predecessor nodes.
                 </p>
                 <p>
                 In case of a person node ({@link WFNodeC#TYPE_PERSONNODE}), formSpec can contain proprietary
                 encoded information about a workflow form.
                 </p>
            comment_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#comment}.
            sub_flow_id (Union[Unset, int]): Id of the active sub-workflow. Only valid for TYPE_CALL_SUB_WORKFLOW.
            label (Union[Unset, str]): Display name by forwarding.
            move_cycle_pos_x (Union[Unset, int]): If a cycle is re-entered, the nodes in the cycle are duplicated.
                The copied nodes will be
                 placed in the designer moved by this value to the right. If this value is 0, the nodes are
                 moved 60 points right and 20 points up. This member is valid for all node types.
            user_name (Union[Unset, str]): The name of the user that has the ID <code>userId</code> This member is only
                valid for person
                nodes.
            in_use_date_iso (Union[Unset, str]): The date when the node was last used(activated or completed).
                This member is valid for all node
                 types.
            user_id (Union[Unset, int]): This user has to edit the node. This member is only valid for person nodes.
            pos_x (Union[Unset, int]): The X position in the designer view. This member is valid for all node types.
            time_limit (Union[Unset, int]): The time-limit to process the node. Measured in minutes.
                This member is only valid for person
                 nodes.
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#name}.
            on_enter (Union[Unset, str]): A script or plugin name that is called, if a workflow node is entered.
                <p>
                 In order to capture this workflow event in JavaScript, store a script file that defines a
                 function named onEnterNode in a sub-folder of "Indexserver Scripting Base/_ALL" or "Indexserver
                 Scripting Base/instancename".

                 <pre>
                 <code class="example">
                 function onEnterNode(ci, userId, workflow, nodeId) {
                   // ci       ... ClientInfo object of the user that forwards the workflow.
                   // userId   ... The calling user's ID (Integer)
                   // workflow ... WFDiagram object
                   // nodeId   ... The activated node ID (Integer)
                 ...
                 }
                 </code>
                 </pre>

                 See Indexserver Programming Manual for more information.
                 </p>
                 <p>
                 If onEnter starts with a plugin's Bundle-SymbolicName, the event is delegated to function
                 <code>onEnterWorkflowNode</code> of a <code>WorkflowNodeEvents</code> object. Such object is
                 created by <code>WorkflowNodeEventsFactory.create</code> implemented in the plugin. Optionally,
                 a path can be appended to the Bundle-SymbolicName which is passed to
                 <code>WorkflowNodeEventsFactory.create</code>. This path has to start with a forward slash.
                 E.g. onEnter="com.partner.wfevents/invoice-solution".
                 </p>
                 This member is valid for all node types.
            pos_y (Union[Unset, int]): The Y position in the designer view. This member is valid for all node types.
            sub_template_id (Union[Unset, int]): ID, GUID or name of the sub-workflow template.
            delay_days (Union[Unset, int]): An active person node (Activate is set) might be displayed to the user delayed
                by this number
                of days. Only valid for person nodes.
            name (Union[Unset, str]): The node description (work instruction). This member is valid for all node types.
            design_department (Union[Unset, int]): <p>
                A group ID or user ID that was originally assigned in the designer.
                 </p>

                 <ul>
                 <li>Only valid for person nodes.</li>
                 <li>If a template is checked in, designDepartment is always set to {@link #userName}
                 respectively {@link #userId}.</li>
                 <li>If a new active workflow is checked in, it it is always set to {@link #userName}
                 respectively {@link #userId}.</li>
                 <li>If an existing active workflow is checked in, the checked in value is saved</li>
                 </ul>
            exit_date_iso (Union[Unset, str]): The node was exited/completed on this date. This member is valid for all node
                types.
            comment (Union[Unset, str]): Comment text for the node. This member is valid for all node types.
            on_enter_handle_rollback (Union[Unset, str]): A script or plugin name that is called when an error occurs inside
                a workflow script.
                All
                 onEnterHandleRollback scripts, from one person node to the next person node, are stored in a
                 temporary queue and all will get executed if an error inside a script occurs. The
                 onEnterHandleRollBack script is not meant for dealing with an error in the onEnter Script, the
                 script will only get stored in the temporary queue if the onEnter script was executed without
                 any issues.
                 <p>
                 In order to capture this workflow event in JavaScript, store a script file that defines a
                 function named onEnterHandleRollbackNode in a sub-folder of "Indexserver Scripting Base/_ALL"
                 or "Indexserver Scripting Base/instancename".

                 <pre>
                 <code class="example">
                 function onEnterHandleRollbackNode(ci, userId, workflow, nodeId) {
                   // ci       ... ClientInfo object of the user that forwards the workflow.
                   // userId   ... The calling user's ID (Integer)
                   // workflow ... WFDiagram object
                   // nodeId   ... The deactivated node ID (Integer)
                 ...
                 }
                 </code>
                 </pre>

                 See Indexserver Programming Manual for more information.
                 </p>
                 <p>
                 If onEnterHandleRollback starts with a plugin's Bundle-SymbolicName, the event is delegated to
                 function {@link de.elo.ix.client.plugin.WorkflowNodeEvents#onEnterHandleRollbackflowNode} of a
                 <code>WorkflowNodeEvents</code> object returned from a call to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. Optionally, a path can be
                 appended to the Bundle-SymbolicName which is passed to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. This path has to start with a
                 forward slash. E.g. onEnterHandleRollback="com.partner.wfevents/invoice-solution".
                 </p>
                 This member is valid for all node types.
            allow_activate (Union[Unset, bool]): Can this node be activated? A script can set this value to prevent the
                activation of the node.
                This member is valid for all node types.
            user_terminate (Union[Unset, str]): The ID of the user who has forwarded the node. Not valid for template
                workflows.
                This member is
                 only valid for person nodes.
            properties (Union[Unset, str]): Node properties.
                Maximum byte size of this string in UTF-8 encoding is constrained to
                 {@link FileDataC#MAX_BLOB_LENGTH}.
            label_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#label}.
    """

    delay_date_iso: Union[Unset, str] = UNSET
    return_value: Union[Unset, str] = UNSET
    on_exit: Union[Unset, str] = UNSET
    process_on_server_id: Union[Unset, str] = UNSET
    yes_no_condition: Union[Unset, str] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    flags: Union[Unset, int] = UNSET
    on_exit_handle_rollback: Union[Unset, str] = UNSET
    user_delay_date_iso: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    type: Union[Unset, int] = UNSET
    ret_val: Union[Unset, int] = UNSET
    enter_date_iso: Union[Unset, str] = UNSET
    department2: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    is_next: Union[Unset, int] = UNSET
    tag: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    obj_key_names: Union[Unset, List[str]] = UNSET
    icon_id: Union[Unset, str] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    script_names: Union[Unset, List[str]] = UNSET
    department_group: Union[Unset, int] = UNSET
    nb_of_dones_to_exit: Union[Unset, int] = UNSET
    form_spec: Union[Unset, str] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    sub_flow_id: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    move_cycle_pos_x: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    in_use_date_iso: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    pos_x: Union[Unset, int] = UNSET
    time_limit: Union[Unset, int] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    on_enter: Union[Unset, str] = UNSET
    pos_y: Union[Unset, int] = UNSET
    sub_template_id: Union[Unset, int] = UNSET
    delay_days: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    design_department: Union[Unset, int] = UNSET
    exit_date_iso: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    on_enter_handle_rollback: Union[Unset, str] = UNSET
    allow_activate: Union[Unset, bool] = UNSET
    user_terminate: Union[Unset, str] = UNSET
    properties: Union[Unset, str] = UNSET
    label_translation_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delay_date_iso = self.delay_date_iso

        return_value = self.return_value

        on_exit = self.on_exit

        process_on_server_id = self.process_on_server_id

        yes_no_condition = self.yes_no_condition

        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()
                time_limit_escalations.append(time_limit_escalations_item)

        flags = self.flags

        on_exit_handle_rollback = self.on_exit_handle_rollback

        user_delay_date_iso = self.user_delay_date_iso

        over_time_limit = self.over_time_limit

        type = self.type

        ret_val = self.ret_val

        enter_date_iso = self.enter_date_iso

        department2 = self.department2

        id = self.id

        is_next = self.is_next

        tag = self.tag

        prio = self.prio

        obj_key_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.obj_key_names, Unset):
            obj_key_names = self.obj_key_names

        icon_id = self.icon_id

        time_limit_iso = self.time_limit_iso

        script_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.script_names, Unset):
            script_names = self.script_names

        department_group = self.department_group

        nb_of_dones_to_exit = self.nb_of_dones_to_exit

        form_spec = self.form_spec

        comment_translation_key = self.comment_translation_key

        sub_flow_id = self.sub_flow_id

        label = self.label

        move_cycle_pos_x = self.move_cycle_pos_x

        user_name = self.user_name

        in_use_date_iso = self.in_use_date_iso

        user_id = self.user_id

        pos_x = self.pos_x

        time_limit = self.time_limit

        name_translation_key = self.name_translation_key

        on_enter = self.on_enter

        pos_y = self.pos_y

        sub_template_id = self.sub_template_id

        delay_days = self.delay_days

        name = self.name

        design_department = self.design_department

        exit_date_iso = self.exit_date_iso

        comment = self.comment

        on_enter_handle_rollback = self.on_enter_handle_rollback

        allow_activate = self.allow_activate

        user_terminate = self.user_terminate

        properties = self.properties

        label_translation_key = self.label_translation_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_date_iso is not UNSET:
            field_dict["delayDateIso"] = delay_date_iso
        if return_value is not UNSET:
            field_dict["returnValue"] = return_value
        if on_exit is not UNSET:
            field_dict["onExit"] = on_exit
        if process_on_server_id is not UNSET:
            field_dict["processOnServerId"] = process_on_server_id
        if yes_no_condition is not UNSET:
            field_dict["yesNoCondition"] = yes_no_condition
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if flags is not UNSET:
            field_dict["flags"] = flags
        if on_exit_handle_rollback is not UNSET:
            field_dict["onExitHandleRollback"] = on_exit_handle_rollback
        if user_delay_date_iso is not UNSET:
            field_dict["userDelayDateIso"] = user_delay_date_iso
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if type is not UNSET:
            field_dict["type"] = type
        if ret_val is not UNSET:
            field_dict["retVal"] = ret_val
        if enter_date_iso is not UNSET:
            field_dict["enterDateIso"] = enter_date_iso
        if department2 is not UNSET:
            field_dict["department2"] = department2
        if id is not UNSET:
            field_dict["id"] = id
        if is_next is not UNSET:
            field_dict["isNext"] = is_next
        if tag is not UNSET:
            field_dict["tag"] = tag
        if prio is not UNSET:
            field_dict["prio"] = prio
        if obj_key_names is not UNSET:
            field_dict["objKeyNames"] = obj_key_names
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if script_names is not UNSET:
            field_dict["scriptNames"] = script_names
        if department_group is not UNSET:
            field_dict["departmentGroup"] = department_group
        if nb_of_dones_to_exit is not UNSET:
            field_dict["nbOfDonesToExit"] = nb_of_dones_to_exit
        if form_spec is not UNSET:
            field_dict["formSpec"] = form_spec
        if comment_translation_key is not UNSET:
            field_dict["commentTranslationKey"] = comment_translation_key
        if sub_flow_id is not UNSET:
            field_dict["subFlowId"] = sub_flow_id
        if label is not UNSET:
            field_dict["label"] = label
        if move_cycle_pos_x is not UNSET:
            field_dict["moveCyclePosX"] = move_cycle_pos_x
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if in_use_date_iso is not UNSET:
            field_dict["inUseDateIso"] = in_use_date_iso
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if on_enter is not UNSET:
            field_dict["onEnter"] = on_enter
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if sub_template_id is not UNSET:
            field_dict["subTemplateId"] = sub_template_id
        if delay_days is not UNSET:
            field_dict["delayDays"] = delay_days
        if name is not UNSET:
            field_dict["name"] = name
        if design_department is not UNSET:
            field_dict["designDepartment"] = design_department
        if exit_date_iso is not UNSET:
            field_dict["exitDateIso"] = exit_date_iso
        if comment is not UNSET:
            field_dict["comment"] = comment
        if on_enter_handle_rollback is not UNSET:
            field_dict["onEnterHandleRollback"] = on_enter_handle_rollback
        if allow_activate is not UNSET:
            field_dict["allowActivate"] = allow_activate
        if user_terminate is not UNSET:
            field_dict["userTerminate"] = user_terminate
        if properties is not UNSET:
            field_dict["properties"] = properties
        if label_translation_key is not UNSET:
            field_dict["labelTranslationKey"] = label_translation_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_time_limit import WFTimeLimit

        d = src_dict.copy()
        delay_date_iso = d.pop("delayDateIso", UNSET)

        return_value = d.pop("returnValue", UNSET)

        on_exit = d.pop("onExit", UNSET)

        process_on_server_id = d.pop("processOnServerId", UNSET)

        yes_no_condition = d.pop("yesNoCondition", UNSET)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        flags = d.pop("flags", UNSET)

        on_exit_handle_rollback = d.pop("onExitHandleRollback", UNSET)

        user_delay_date_iso = d.pop("userDelayDateIso", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        type = d.pop("type", UNSET)

        ret_val = d.pop("retVal", UNSET)

        enter_date_iso = d.pop("enterDateIso", UNSET)

        department2 = d.pop("department2", UNSET)

        id = d.pop("id", UNSET)

        is_next = d.pop("isNext", UNSET)

        tag = d.pop("tag", UNSET)

        prio = d.pop("prio", UNSET)

        obj_key_names = cast(List[str], d.pop("objKeyNames", UNSET))

        icon_id = d.pop("iconId", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        script_names = cast(List[str], d.pop("scriptNames", UNSET))

        department_group = d.pop("departmentGroup", UNSET)

        nb_of_dones_to_exit = d.pop("nbOfDonesToExit", UNSET)

        form_spec = d.pop("formSpec", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        sub_flow_id = d.pop("subFlowId", UNSET)

        label = d.pop("label", UNSET)

        move_cycle_pos_x = d.pop("moveCyclePosX", UNSET)

        user_name = d.pop("userName", UNSET)

        in_use_date_iso = d.pop("inUseDateIso", UNSET)

        user_id = d.pop("userId", UNSET)

        pos_x = d.pop("posX", UNSET)

        time_limit = d.pop("timeLimit", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        on_enter = d.pop("onEnter", UNSET)

        pos_y = d.pop("posY", UNSET)

        sub_template_id = d.pop("subTemplateId", UNSET)

        delay_days = d.pop("delayDays", UNSET)

        name = d.pop("name", UNSET)

        design_department = d.pop("designDepartment", UNSET)

        exit_date_iso = d.pop("exitDateIso", UNSET)

        comment = d.pop("comment", UNSET)

        on_enter_handle_rollback = d.pop("onEnterHandleRollback", UNSET)

        allow_activate = d.pop("allowActivate", UNSET)

        user_terminate = d.pop("userTerminate", UNSET)

        properties = d.pop("properties", UNSET)

        label_translation_key = d.pop("labelTranslationKey", UNSET)

        wf_node = cls(
            delay_date_iso=delay_date_iso,
            return_value=return_value,
            on_exit=on_exit,
            process_on_server_id=process_on_server_id,
            yes_no_condition=yes_no_condition,
            time_limit_escalations=time_limit_escalations,
            flags=flags,
            on_exit_handle_rollback=on_exit_handle_rollback,
            user_delay_date_iso=user_delay_date_iso,
            over_time_limit=over_time_limit,
            type=type,
            ret_val=ret_val,
            enter_date_iso=enter_date_iso,
            department2=department2,
            id=id,
            is_next=is_next,
            tag=tag,
            prio=prio,
            obj_key_names=obj_key_names,
            icon_id=icon_id,
            time_limit_iso=time_limit_iso,
            script_names=script_names,
            department_group=department_group,
            nb_of_dones_to_exit=nb_of_dones_to_exit,
            form_spec=form_spec,
            comment_translation_key=comment_translation_key,
            sub_flow_id=sub_flow_id,
            label=label,
            move_cycle_pos_x=move_cycle_pos_x,
            user_name=user_name,
            in_use_date_iso=in_use_date_iso,
            user_id=user_id,
            pos_x=pos_x,
            time_limit=time_limit,
            name_translation_key=name_translation_key,
            on_enter=on_enter,
            pos_y=pos_y,
            sub_template_id=sub_template_id,
            delay_days=delay_days,
            name=name,
            design_department=design_department,
            exit_date_iso=exit_date_iso,
            comment=comment,
            on_enter_handle_rollback=on_enter_handle_rollback,
            allow_activate=allow_activate,
            user_terminate=user_terminate,
            properties=properties,
            label_translation_key=label_translation_key,
        )

        wf_node.additional_properties = d
        return wf_node

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
