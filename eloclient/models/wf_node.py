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
            allow_activate (Union[Unset, bool]): Can this node be activated? A script can set this value to prevent the
                activation of the node.
                This member is valid
                 for all node types.
            comment (Union[Unset, str]): Comment text for the node. This member is valid for all node types.
            delay_days (Union[Unset, int]): An active person node (Activate is set) might be displayed to the user delayed
                by this number of days.
                Only valid
                 for person nodes.
            department2 (Union[Unset, int]): A group ID to constrain access to the node. Only members of this group are
                allowed to see and process the node.
                Only valid for person nodes.
            design_department (Union[Unset, int]): <p>
                A group ID or user ID that was originally assigned in the designer.
                 </p>

                 <ul>
                 <li>Only valid for person nodes.</li>
                 <li>If a template is checked in, designDepartment is always set to {@link #userName} respectively
                 {@link #userId}.</li>
                 <li>If a new active workflow is checked in, it it is always set to {@link #userName} respectively
                 {@link #userId}.</li>
                 <li>If an existing active workflow is checked in, the checked in value is saved</li>
                 </ul>
            enter_date_iso (Union[Unset, str]): The node was activated on this date. This member is valid for all node
                types.
            exit_date_iso (Union[Unset, str]): The node was exited/completed on this date. This member is valid for all node
                types.
            flags (Union[Unset, int]): Control flags for the node, a combination of WFNodeC.FLAG_* constants.
                For start nodes (TYPE_BEGINNODE), the flags
                 should be specified in WFDiagram.flags. To ensure compatibility with older client programs, the WFNode.flags of
                the
                 start node are or-ed with the WFDiagram.flags. This member is valid for all node types.
            id (Union[Unset, int]): Node ID. This member is valid for all node types.
            in_use_date_iso (Union[Unset, str]): The date when the node was last used(activated or completed). This member
                is valid for all node types.
            is_next (Union[Unset, int]): The activation state of the node. This member is valid for all node types.
            move_cycle_pos_x (Union[Unset, int]): If a cycle is re-entered, the nodes in the cycle are duplicated.
                The copied nodes will be placed in the designer
                 moved by this value to the right. If this value is 0, the nodes are moved 60 points right and 20 points up.
                This
                 member is valid for all node types.
            name (Union[Unset, str]): The node description (work instruction). This member is valid for all node types.
            nb_of_dones_to_exit (Union[Unset, int]): The number of predecessor nodes that must be processed to forward this
                collector node.
                A value of -1 means that all
                 predecessor nodes must be processed. If set to 0, the collect node switches when it is activated regardless of
                the
                 state of the predecessor nodes. This member is only valid for collect nodes.
            on_enter (Union[Unset, str]): A script or plugin name that is called, if a workflow node is entered.
                <p>
                 In order to capture this workflow event in JavaScript, store a script file that defines a function named
                 onEnterNode in a sub-folder of "Indexserver Scripting Base/_ALL" or "Indexserver Scripting Base/instancename".

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
                 <code>onEnterWorkflowNode</code> of a <code>WorkflowNodeEvents</code> object. Such object is created by
                 <code>WorkflowNodeEventsFactory.create</code> implemented in the plugin. Optionally, a path can be appended to
                the
                 Bundle-SymbolicName which is passed to <code>WorkflowNodeEventsFactory.create</code>. This path has to start
                with a
                 forward slash. E.g. onEnter="com.partner.wfevents/invoice-solution".
                 </p>
                 This member is valid for all node types.
            on_exit (Union[Unset, str]): A script or plugin name that is called, if a workflow node is exited.
                <p>
                 In order to capture this workflow event in JavaScript, store a script file that defines a function named
                onExitNode
                 in a sub-folder of "Indexserver Scripting Base/_ALL" or "Indexserver Scripting Base/instancename".

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
                 {@link de.elo.ix.client.plugin.WorkflowNodeEvents#onExitWorkflowNode} of a <code>WorkflowNodeEvents</code>
                object
                 returned from a call to {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. Optionally, a path
                can be
                 appended to the Bundle-SymbolicName which is passed to
                 {@link de.elo.ix.client.plugin.WorkflowNodeEventsFactory#create}. This path has to start with a forward slash.
                E.g.
                 onEnter="com.partner.wfevents/invoice-solution".
                 </p>
                 This member is valid for all node types.
            pos_x (Union[Unset, int]): The X position in the designer view. This member is valid for all node types.
            pos_y (Union[Unset, int]): The Y position in the designer view. This member is valid for all node types.
            tag (Union[Unset, int]): reserved.
                DB column: wf_tag
            time_limit (Union[Unset, int]): The time-limit to process the node. Measured in minutes. This member is only
                valid for person nodes.
            time_limit_iso (Union[Unset, str]): After this date the node exceeds the time-limit for processing. This member
                is only valid for person nodes.
                Read-only.
            type (Union[Unset, int]): The node type. This member is set to one of the TYPE_* constants in WFNodeC.
            user_id (Union[Unset, int]): This user has to edit the node. This member is only valid for person nodes.
            user_name (Union[Unset, str]): The name of the user that has the ID <code>userId</code> This member is only
                valid for person nodes.
            user_terminate (Union[Unset, str]): The ID of the user who has forwarded the node. Not valid for template
                workflows.
                This member is only valid for
                 person nodes.
            yes_no_condition (Union[Unset, str]): IF node: test condition, numeric values must be formatted according to the
                servers locale.
                split node: sets the
                 workflow status to this value, begin node: contains workflow status cycle node: condition that evaluates true
                to
                 leave the cycle
            delay_date_iso (Union[Unset, str]): The node is displayed to the user at this date. This date is computed by
                enterDateIso + delayDays.
                This member is
                 only valid for person nodes. Read-only.
            over_time_limit (Union[Unset, bool]): True, if the node exceeds the time limit.
                This member is only valid for person nodes in active or finished
                 workflows. Read-only.
            user_delay_date_iso (Union[Unset, str]): The workflow node is deferred until this date.
                This member is only valid for person nodes in active or finished
                 workflows. ISO date format.
            process_on_server_id (Union[Unset, str]): Server ID (resp. replication branch). If the node is activated, the
                server ID is set to this value.
                This member is
                 only valid for nodes of type WFNodeC.TYPE_SET_SERVER_ID.
            time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
            obj_key_names (Union[Unset, List[str]]):
            script_names (Union[Unset, List[str]]):
            icon_id (Union[Unset, str]): Object-GUID of an icon file that is displayed in the designer.
            form_spec (Union[Unset, str]): Multipurpose field.
                <p>
                 If the node is a collect node (type={@link WFNodeC#TYPE_COLLECTNODE}), formSpec contains a comma separated list
                of
                 node IDs. This nodes are deactivated when the collect node forwards the workflow. In addition to a list of IDs,
                the
                 value of {@link WFNodeC#DEACTIVATE_ALL_PREDS} causes to deactivate all predecessor nodes.
                 </p>
                 <p>
                 In case of a person node ({@link WFNodeC#TYPE_PERSONNODE}), formSpec can contain proprietary encoded
                information
                 about a workflow form.
                 </p>
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#name}.
            comment_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#comment}.
            label (Union[Unset, str]): Display name by forwarding.
            properties (Union[Unset, str]): Node properties.
                Maximum byte size of this string in UTF-8 encoding is constrained to {@link FileDataC#MAX_BLOB_LENGTH}.
            department_group (Union[Unset, int]): Grouping of nodes for function takeWorkFlowNode.
                A non-zero value binds nodes with the same value to a group of
                 nodes that is evaluated in {@link IXServicePortIF#takeWorkFlowNode(ClientInfo, int, int, String, int, LockZ)}.
                The
                 function takeWorkFlowNodes takes - in addition to the given node - all nodes with the same group assignment
                 specified by this member. This member is only used as a marker and is not interpreted as a group or user ID.
            sub_flow_id (Union[Unset, int]): Id of the active sub-workflow. Only valid for TYPE_CALL_SUB_WORKFLOW.
            ret_val (Union[Unset, int]): Return value of an end node. Only valid for TYPE_END.
            return_value (Union[Unset, str]): Return value of a sub-workflow.
                The value defines the name of the successor node of the call-node
                 {@link WFNodeC#TYPE_CALL_SUB_WORKFLOW} that will be activated when the sub-workflow returns. If the sub-
                workflow
                 returns a node name that does not exist in the main workflow, a new person node is inserted between the call-
                node
                 and its successors. This new node is named as the return value and is assigned to the workflow owner.
            label_translation_key (Union[Unset, str]): Translation-keyword for {@link WFNode#label}.
            sub_template_id (Union[Unset, int]): ID, GUID or name of the sub-workflow template.
            prio (Union[Unset, int]): Node priortiy: 0...high, 1...medium, 2...low. Only valid for person nodes,
                type=={@link WFNodeC#TYPE_PERSONNODE}.
                The user assigned to the person node can change this value by conn.ix().forwardWorkflowNode():

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
    """

    allow_activate: Union[Unset, bool] = UNSET
    comment: Union[Unset, str] = UNSET
    delay_days: Union[Unset, int] = UNSET
    department2: Union[Unset, int] = UNSET
    design_department: Union[Unset, int] = UNSET
    enter_date_iso: Union[Unset, str] = UNSET
    exit_date_iso: Union[Unset, str] = UNSET
    flags: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    in_use_date_iso: Union[Unset, str] = UNSET
    is_next: Union[Unset, int] = UNSET
    move_cycle_pos_x: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    nb_of_dones_to_exit: Union[Unset, int] = UNSET
    on_enter: Union[Unset, str] = UNSET
    on_exit: Union[Unset, str] = UNSET
    pos_x: Union[Unset, int] = UNSET
    pos_y: Union[Unset, int] = UNSET
    tag: Union[Unset, int] = UNSET
    time_limit: Union[Unset, int] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_terminate: Union[Unset, str] = UNSET
    yes_no_condition: Union[Unset, str] = UNSET
    delay_date_iso: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    user_delay_date_iso: Union[Unset, str] = UNSET
    process_on_server_id: Union[Unset, str] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    obj_key_names: Union[Unset, List[str]] = UNSET
    script_names: Union[Unset, List[str]] = UNSET
    icon_id: Union[Unset, str] = UNSET
    form_spec: Union[Unset, str] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    properties: Union[Unset, str] = UNSET
    department_group: Union[Unset, int] = UNSET
    sub_flow_id: Union[Unset, int] = UNSET
    ret_val: Union[Unset, int] = UNSET
    return_value: Union[Unset, str] = UNSET
    label_translation_key: Union[Unset, str] = UNSET
    sub_template_id: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_activate = self.allow_activate
        comment = self.comment
        delay_days = self.delay_days
        department2 = self.department2
        design_department = self.design_department
        enter_date_iso = self.enter_date_iso
        exit_date_iso = self.exit_date_iso
        flags = self.flags
        id = self.id
        in_use_date_iso = self.in_use_date_iso
        is_next = self.is_next
        move_cycle_pos_x = self.move_cycle_pos_x
        name = self.name
        nb_of_dones_to_exit = self.nb_of_dones_to_exit
        on_enter = self.on_enter
        on_exit = self.on_exit
        pos_x = self.pos_x
        pos_y = self.pos_y
        tag = self.tag
        time_limit = self.time_limit
        time_limit_iso = self.time_limit_iso
        type = self.type
        user_id = self.user_id
        user_name = self.user_name
        user_terminate = self.user_terminate
        yes_no_condition = self.yes_no_condition
        delay_date_iso = self.delay_date_iso
        over_time_limit = self.over_time_limit
        user_delay_date_iso = self.user_delay_date_iso
        process_on_server_id = self.process_on_server_id
        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()

                time_limit_escalations.append(time_limit_escalations_item)

        obj_key_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.obj_key_names, Unset):
            obj_key_names = self.obj_key_names

        script_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.script_names, Unset):
            script_names = self.script_names

        icon_id = self.icon_id
        form_spec = self.form_spec
        name_translation_key = self.name_translation_key
        comment_translation_key = self.comment_translation_key
        label = self.label
        properties = self.properties
        department_group = self.department_group
        sub_flow_id = self.sub_flow_id
        ret_val = self.ret_val
        return_value = self.return_value
        label_translation_key = self.label_translation_key
        sub_template_id = self.sub_template_id
        prio = self.prio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_activate is not UNSET:
            field_dict["allowActivate"] = allow_activate
        if comment is not UNSET:
            field_dict["comment"] = comment
        if delay_days is not UNSET:
            field_dict["delayDays"] = delay_days
        if department2 is not UNSET:
            field_dict["department2"] = department2
        if design_department is not UNSET:
            field_dict["designDepartment"] = design_department
        if enter_date_iso is not UNSET:
            field_dict["enterDateIso"] = enter_date_iso
        if exit_date_iso is not UNSET:
            field_dict["exitDateIso"] = exit_date_iso
        if flags is not UNSET:
            field_dict["flags"] = flags
        if id is not UNSET:
            field_dict["id"] = id
        if in_use_date_iso is not UNSET:
            field_dict["inUseDateIso"] = in_use_date_iso
        if is_next is not UNSET:
            field_dict["isNext"] = is_next
        if move_cycle_pos_x is not UNSET:
            field_dict["moveCyclePosX"] = move_cycle_pos_x
        if name is not UNSET:
            field_dict["name"] = name
        if nb_of_dones_to_exit is not UNSET:
            field_dict["nbOfDonesToExit"] = nb_of_dones_to_exit
        if on_enter is not UNSET:
            field_dict["onEnter"] = on_enter
        if on_exit is not UNSET:
            field_dict["onExit"] = on_exit
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if tag is not UNSET:
            field_dict["tag"] = tag
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if type is not UNSET:
            field_dict["type"] = type
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_terminate is not UNSET:
            field_dict["userTerminate"] = user_terminate
        if yes_no_condition is not UNSET:
            field_dict["yesNoCondition"] = yes_no_condition
        if delay_date_iso is not UNSET:
            field_dict["delayDateIso"] = delay_date_iso
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if user_delay_date_iso is not UNSET:
            field_dict["userDelayDateIso"] = user_delay_date_iso
        if process_on_server_id is not UNSET:
            field_dict["processOnServerId"] = process_on_server_id
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if obj_key_names is not UNSET:
            field_dict["objKeyNames"] = obj_key_names
        if script_names is not UNSET:
            field_dict["scriptNames"] = script_names
        if icon_id is not UNSET:
            field_dict["iconId"] = icon_id
        if form_spec is not UNSET:
            field_dict["formSpec"] = form_spec
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
        if sub_flow_id is not UNSET:
            field_dict["subFlowId"] = sub_flow_id
        if ret_val is not UNSET:
            field_dict["retVal"] = ret_val
        if return_value is not UNSET:
            field_dict["returnValue"] = return_value
        if label_translation_key is not UNSET:
            field_dict["labelTranslationKey"] = label_translation_key
        if sub_template_id is not UNSET:
            field_dict["subTemplateId"] = sub_template_id
        if prio is not UNSET:
            field_dict["prio"] = prio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_time_limit import WFTimeLimit

        d = src_dict.copy()
        allow_activate = d.pop("allowActivate", UNSET)

        comment = d.pop("comment", UNSET)

        delay_days = d.pop("delayDays", UNSET)

        department2 = d.pop("department2", UNSET)

        design_department = d.pop("designDepartment", UNSET)

        enter_date_iso = d.pop("enterDateIso", UNSET)

        exit_date_iso = d.pop("exitDateIso", UNSET)

        flags = d.pop("flags", UNSET)

        id = d.pop("id", UNSET)

        in_use_date_iso = d.pop("inUseDateIso", UNSET)

        is_next = d.pop("isNext", UNSET)

        move_cycle_pos_x = d.pop("moveCyclePosX", UNSET)

        name = d.pop("name", UNSET)

        nb_of_dones_to_exit = d.pop("nbOfDonesToExit", UNSET)

        on_enter = d.pop("onEnter", UNSET)

        on_exit = d.pop("onExit", UNSET)

        pos_x = d.pop("posX", UNSET)

        pos_y = d.pop("posY", UNSET)

        tag = d.pop("tag", UNSET)

        time_limit = d.pop("timeLimit", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        type = d.pop("type", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        user_terminate = d.pop("userTerminate", UNSET)

        yes_no_condition = d.pop("yesNoCondition", UNSET)

        delay_date_iso = d.pop("delayDateIso", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        user_delay_date_iso = d.pop("userDelayDateIso", UNSET)

        process_on_server_id = d.pop("processOnServerId", UNSET)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        obj_key_names = cast(List[str], d.pop("objKeyNames", UNSET))

        script_names = cast(List[str], d.pop("scriptNames", UNSET))

        icon_id = d.pop("iconId", UNSET)

        form_spec = d.pop("formSpec", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        label = d.pop("label", UNSET)

        properties = d.pop("properties", UNSET)

        department_group = d.pop("departmentGroup", UNSET)

        sub_flow_id = d.pop("subFlowId", UNSET)

        ret_val = d.pop("retVal", UNSET)

        return_value = d.pop("returnValue", UNSET)

        label_translation_key = d.pop("labelTranslationKey", UNSET)

        sub_template_id = d.pop("subTemplateId", UNSET)

        prio = d.pop("prio", UNSET)

        wf_node = cls(
            allow_activate=allow_activate,
            comment=comment,
            delay_days=delay_days,
            department2=department2,
            design_department=design_department,
            enter_date_iso=enter_date_iso,
            exit_date_iso=exit_date_iso,
            flags=flags,
            id=id,
            in_use_date_iso=in_use_date_iso,
            is_next=is_next,
            move_cycle_pos_x=move_cycle_pos_x,
            name=name,
            nb_of_dones_to_exit=nb_of_dones_to_exit,
            on_enter=on_enter,
            on_exit=on_exit,
            pos_x=pos_x,
            pos_y=pos_y,
            tag=tag,
            time_limit=time_limit,
            time_limit_iso=time_limit_iso,
            type=type,
            user_id=user_id,
            user_name=user_name,
            user_terminate=user_terminate,
            yes_no_condition=yes_no_condition,
            delay_date_iso=delay_date_iso,
            over_time_limit=over_time_limit,
            user_delay_date_iso=user_delay_date_iso,
            process_on_server_id=process_on_server_id,
            time_limit_escalations=time_limit_escalations,
            obj_key_names=obj_key_names,
            script_names=script_names,
            icon_id=icon_id,
            form_spec=form_spec,
            name_translation_key=name_translation_key,
            comment_translation_key=comment_translation_key,
            label=label,
            properties=properties,
            department_group=department_group,
            sub_flow_id=sub_flow_id,
            ret_val=ret_val,
            return_value=return_value,
            label_translation_key=label_translation_key,
            sub_template_id=sub_template_id,
            prio=prio,
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
