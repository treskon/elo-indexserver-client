from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_time_limit import WFTimeLimit


T = TypeVar("T", bound="WFCollectNode")


@_attrs_define
class WFCollectNode:
    """<p>
    Data used to display a workflow node int the task view.
     </p>
     <p>
     This class bundles the data which is required for displaying a workflow node. The class is used
     by <code>findFirstTasks</code>
     </p>

        Attributes:
            node_name (Union[Unset, str]): Description/processing instructions for the workflow node
            access (Union[Unset, int]): Access rights to the active workflow for the current user. A combination of LUR_*
                constants.
                Read-only.
            hidden (Union[Unset, bool]): Indicates whether this workflow is hidden.
            process_on_server_id (Union[Unset, str]): Allows the clients to decide whether the workflow is editable or not
                without loading the
                WFDiagram.
            time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
            user_delay_date_iso (Union[Unset, str]): The workflow node is deferred until this date. Not valid for template
                workflows.
                Only valid for
                 person nodes. ELO date format.
            over_time_limit (Union[Unset, bool]): True, if the node exceeds the time limit.
            design_department_id (Union[Unset, int]): ID of the user that was assigned to the node when the workflow
                started.
            over_time_limit_any (Union[Unset, bool]): Indicates whether the workflow is an escalation.
            time_limits_workflow (Union[Unset, List['WFTimeLimit']]):
            workflow_owner_name (Union[Unset, str]): Workflow owner name.
                This member is only valid when this object is returned by the
                 findFirstTasks or findNextTasks functions.
            terminate_date_iso (Union[Unset, str]): Date the node was completed/terminated
            completion_date_iso (Union[Unset, str]): Date the workfow was completed
            activate_date_workflow_iso (Union[Unset, str]): Workflow start date.
            design_department_name (Union[Unset, str]): Name of the user that was assigned to the node when the workflow
                started.
            prio (Union[Unset, int]): Node priority
            flow_id (Union[Unset, int]): Workflow id
            obj_type (Union[Unset, int]): Object type of the object for which the workflow is started.
                (1 for cabinet, 2 for folder,
                 etc.)
            node_name_translation_key (Union[Unset, str]): Translation-keyword for nodeName.
            workflow_owner_id (Union[Unset, int]): Workflow owner ID.
                This member is only valid when this object is returned by the findFirstTasks
                 or findNextTasks functions.
            time_limit_iso (Union[Unset, str]): Node must be completed until this date.
                This member is only valid when this object is returned
                 by the findFirstTasks or findNextTasks functions.
            call_node_id (Union[Unset, int]): The call node id of the main workflow, which call this sub workflow.
            form_spec (Union[Unset, str]): Same as {@link WFNode#formSpec}.
            obj_guid (Union[Unset, str]): Object GUID of the object for which the workflow is started.
                This member will be set only if a
                 search is run via <code>findFirstTasks</code> or <code>findNextTasks</code>. In this case it is
                 equal to the GUID of {@link UserTask#sord}.
            active (Union[Unset, bool]): Is the node active or not?
            obj_name (Union[Unset, str]): Sord name.
            label (Union[Unset, str]): Display name by forwarding
            user_name (Union[Unset, str]): User name of the user for whom the workflow node is intended.
            flow_name (Union[Unset, str]): Workflow name
            in_use_date_iso (Union[Unset, str]): Date the node was set to <i>In Use</i>
            user_id (Union[Unset, int]): User number of the user for whom the workflow node is intended.
            node_comment (Union[Unset, str]): Node description.
            time_limit (Union[Unset, int]): Time limit in minutes.
            parent_flow_id (Union[Unset, int]): ID of the parent workflow.
            time_limit_user_name (Union[Unset, str]): User name for timeLimitUserId; When writing a workflow with
                checkinWorkFlow, this value has
                preceedence before timeLimitUserId. Set timeLimitUserName to an empty string, if
                 timeLimitUserId should be used.
            node_comment_translation_key (Union[Unset, str]): Translation-keyword for nodeComment.
            obj_id (Union[Unset, int]): Object id of the object for which the workflow is started.
            flow_name_translation_key (Union[Unset, str]): Translation-keyword for workflow name.
            flow_status (Union[Unset, str]): Workflow status.
                This member is only valid when this object is returned by the findFirstTasks
                 or findNextTasks functions.
            node_id (Union[Unset, int]): Node identifier
            time_limit_user_id (Union[Unset, int]): The ID of the user that should be informed, if the time-limit is
                exceeded.
                The Indexserver does
                 not send any notification to the user. The client application is responsible for doing this.
            activate_date_iso (Union[Unset, str]): Date the node was activated
            properties (Union[Unset, str]): Node properties
            label_translation_key (Union[Unset, str]): Translation-keyword for {@link WFCollectNode#label}.
    """

    node_name: Union[Unset, str] = UNSET
    access: Union[Unset, int] = UNSET
    hidden: Union[Unset, bool] = UNSET
    process_on_server_id: Union[Unset, str] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    user_delay_date_iso: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    design_department_id: Union[Unset, int] = UNSET
    over_time_limit_any: Union[Unset, bool] = UNSET
    time_limits_workflow: Union[Unset, List["WFTimeLimit"]] = UNSET
    workflow_owner_name: Union[Unset, str] = UNSET
    terminate_date_iso: Union[Unset, str] = UNSET
    completion_date_iso: Union[Unset, str] = UNSET
    activate_date_workflow_iso: Union[Unset, str] = UNSET
    design_department_name: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    flow_id: Union[Unset, int] = UNSET
    obj_type: Union[Unset, int] = UNSET
    node_name_translation_key: Union[Unset, str] = UNSET
    workflow_owner_id: Union[Unset, int] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    call_node_id: Union[Unset, int] = UNSET
    form_spec: Union[Unset, str] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    obj_name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    flow_name: Union[Unset, str] = UNSET
    in_use_date_iso: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    node_comment: Union[Unset, str] = UNSET
    time_limit: Union[Unset, int] = UNSET
    parent_flow_id: Union[Unset, int] = UNSET
    time_limit_user_name: Union[Unset, str] = UNSET
    node_comment_translation_key: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    flow_name_translation_key: Union[Unset, str] = UNSET
    flow_status: Union[Unset, str] = UNSET
    node_id: Union[Unset, int] = UNSET
    time_limit_user_id: Union[Unset, int] = UNSET
    activate_date_iso: Union[Unset, str] = UNSET
    properties: Union[Unset, str] = UNSET
    label_translation_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_name = self.node_name

        access = self.access

        hidden = self.hidden

        process_on_server_id = self.process_on_server_id

        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()
                time_limit_escalations.append(time_limit_escalations_item)

        user_delay_date_iso = self.user_delay_date_iso

        over_time_limit = self.over_time_limit

        design_department_id = self.design_department_id

        over_time_limit_any = self.over_time_limit_any

        time_limits_workflow: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limits_workflow, Unset):
            time_limits_workflow = []
            for time_limits_workflow_item_data in self.time_limits_workflow:
                time_limits_workflow_item = time_limits_workflow_item_data.to_dict()
                time_limits_workflow.append(time_limits_workflow_item)

        workflow_owner_name = self.workflow_owner_name

        terminate_date_iso = self.terminate_date_iso

        completion_date_iso = self.completion_date_iso

        activate_date_workflow_iso = self.activate_date_workflow_iso

        design_department_name = self.design_department_name

        prio = self.prio

        flow_id = self.flow_id

        obj_type = self.obj_type

        node_name_translation_key = self.node_name_translation_key

        workflow_owner_id = self.workflow_owner_id

        time_limit_iso = self.time_limit_iso

        call_node_id = self.call_node_id

        form_spec = self.form_spec

        obj_guid = self.obj_guid

        active = self.active

        obj_name = self.obj_name

        label = self.label

        user_name = self.user_name

        flow_name = self.flow_name

        in_use_date_iso = self.in_use_date_iso

        user_id = self.user_id

        node_comment = self.node_comment

        time_limit = self.time_limit

        parent_flow_id = self.parent_flow_id

        time_limit_user_name = self.time_limit_user_name

        node_comment_translation_key = self.node_comment_translation_key

        obj_id = self.obj_id

        flow_name_translation_key = self.flow_name_translation_key

        flow_status = self.flow_status

        node_id = self.node_id

        time_limit_user_id = self.time_limit_user_id

        activate_date_iso = self.activate_date_iso

        properties = self.properties

        label_translation_key = self.label_translation_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if access is not UNSET:
            field_dict["access"] = access
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if process_on_server_id is not UNSET:
            field_dict["processOnServerId"] = process_on_server_id
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if user_delay_date_iso is not UNSET:
            field_dict["userDelayDateIso"] = user_delay_date_iso
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if design_department_id is not UNSET:
            field_dict["designDepartmentId"] = design_department_id
        if over_time_limit_any is not UNSET:
            field_dict["overTimeLimitAny"] = over_time_limit_any
        if time_limits_workflow is not UNSET:
            field_dict["timeLimitsWorkflow"] = time_limits_workflow
        if workflow_owner_name is not UNSET:
            field_dict["workflowOwnerName"] = workflow_owner_name
        if terminate_date_iso is not UNSET:
            field_dict["terminateDateIso"] = terminate_date_iso
        if completion_date_iso is not UNSET:
            field_dict["completionDateIso"] = completion_date_iso
        if activate_date_workflow_iso is not UNSET:
            field_dict["activateDateWorkflowIso"] = activate_date_workflow_iso
        if design_department_name is not UNSET:
            field_dict["designDepartmentName"] = design_department_name
        if prio is not UNSET:
            field_dict["prio"] = prio
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if node_name_translation_key is not UNSET:
            field_dict["nodeNameTranslationKey"] = node_name_translation_key
        if workflow_owner_id is not UNSET:
            field_dict["workflowOwnerId"] = workflow_owner_id
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if call_node_id is not UNSET:
            field_dict["callNodeId"] = call_node_id
        if form_spec is not UNSET:
            field_dict["formSpec"] = form_spec
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if active is not UNSET:
            field_dict["active"] = active
        if obj_name is not UNSET:
            field_dict["objName"] = obj_name
        if label is not UNSET:
            field_dict["label"] = label
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if in_use_date_iso is not UNSET:
            field_dict["inUseDateIso"] = in_use_date_iso
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if node_comment is not UNSET:
            field_dict["nodeComment"] = node_comment
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if parent_flow_id is not UNSET:
            field_dict["parentFlowId"] = parent_flow_id
        if time_limit_user_name is not UNSET:
            field_dict["timeLimitUserName"] = time_limit_user_name
        if node_comment_translation_key is not UNSET:
            field_dict["nodeCommentTranslationKey"] = node_comment_translation_key
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if flow_name_translation_key is not UNSET:
            field_dict["flowNameTranslationKey"] = flow_name_translation_key
        if flow_status is not UNSET:
            field_dict["flowStatus"] = flow_status
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if time_limit_user_id is not UNSET:
            field_dict["timeLimitUserId"] = time_limit_user_id
        if activate_date_iso is not UNSET:
            field_dict["activateDateIso"] = activate_date_iso
        if properties is not UNSET:
            field_dict["properties"] = properties
        if label_translation_key is not UNSET:
            field_dict["labelTranslationKey"] = label_translation_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_time_limit import WFTimeLimit

        d = src_dict.copy()
        node_name = d.pop("nodeName", UNSET)

        access = d.pop("access", UNSET)

        hidden = d.pop("hidden", UNSET)

        process_on_server_id = d.pop("processOnServerId", UNSET)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        user_delay_date_iso = d.pop("userDelayDateIso", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        design_department_id = d.pop("designDepartmentId", UNSET)

        over_time_limit_any = d.pop("overTimeLimitAny", UNSET)

        time_limits_workflow = []
        _time_limits_workflow = d.pop("timeLimitsWorkflow", UNSET)
        for time_limits_workflow_item_data in _time_limits_workflow or []:
            time_limits_workflow_item = WFTimeLimit.from_dict(time_limits_workflow_item_data)

            time_limits_workflow.append(time_limits_workflow_item)

        workflow_owner_name = d.pop("workflowOwnerName", UNSET)

        terminate_date_iso = d.pop("terminateDateIso", UNSET)

        completion_date_iso = d.pop("completionDateIso", UNSET)

        activate_date_workflow_iso = d.pop("activateDateWorkflowIso", UNSET)

        design_department_name = d.pop("designDepartmentName", UNSET)

        prio = d.pop("prio", UNSET)

        flow_id = d.pop("flowId", UNSET)

        obj_type = d.pop("objType", UNSET)

        node_name_translation_key = d.pop("nodeNameTranslationKey", UNSET)

        workflow_owner_id = d.pop("workflowOwnerId", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        call_node_id = d.pop("callNodeId", UNSET)

        form_spec = d.pop("formSpec", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        active = d.pop("active", UNSET)

        obj_name = d.pop("objName", UNSET)

        label = d.pop("label", UNSET)

        user_name = d.pop("userName", UNSET)

        flow_name = d.pop("flowName", UNSET)

        in_use_date_iso = d.pop("inUseDateIso", UNSET)

        user_id = d.pop("userId", UNSET)

        node_comment = d.pop("nodeComment", UNSET)

        time_limit = d.pop("timeLimit", UNSET)

        parent_flow_id = d.pop("parentFlowId", UNSET)

        time_limit_user_name = d.pop("timeLimitUserName", UNSET)

        node_comment_translation_key = d.pop("nodeCommentTranslationKey", UNSET)

        obj_id = d.pop("objId", UNSET)

        flow_name_translation_key = d.pop("flowNameTranslationKey", UNSET)

        flow_status = d.pop("flowStatus", UNSET)

        node_id = d.pop("nodeId", UNSET)

        time_limit_user_id = d.pop("timeLimitUserId", UNSET)

        activate_date_iso = d.pop("activateDateIso", UNSET)

        properties = d.pop("properties", UNSET)

        label_translation_key = d.pop("labelTranslationKey", UNSET)

        wf_collect_node = cls(
            node_name=node_name,
            access=access,
            hidden=hidden,
            process_on_server_id=process_on_server_id,
            time_limit_escalations=time_limit_escalations,
            user_delay_date_iso=user_delay_date_iso,
            over_time_limit=over_time_limit,
            design_department_id=design_department_id,
            over_time_limit_any=over_time_limit_any,
            time_limits_workflow=time_limits_workflow,
            workflow_owner_name=workflow_owner_name,
            terminate_date_iso=terminate_date_iso,
            completion_date_iso=completion_date_iso,
            activate_date_workflow_iso=activate_date_workflow_iso,
            design_department_name=design_department_name,
            prio=prio,
            flow_id=flow_id,
            obj_type=obj_type,
            node_name_translation_key=node_name_translation_key,
            workflow_owner_id=workflow_owner_id,
            time_limit_iso=time_limit_iso,
            call_node_id=call_node_id,
            form_spec=form_spec,
            obj_guid=obj_guid,
            active=active,
            obj_name=obj_name,
            label=label,
            user_name=user_name,
            flow_name=flow_name,
            in_use_date_iso=in_use_date_iso,
            user_id=user_id,
            node_comment=node_comment,
            time_limit=time_limit,
            parent_flow_id=parent_flow_id,
            time_limit_user_name=time_limit_user_name,
            node_comment_translation_key=node_comment_translation_key,
            obj_id=obj_id,
            flow_name_translation_key=flow_name_translation_key,
            flow_status=flow_status,
            node_id=node_id,
            time_limit_user_id=time_limit_user_id,
            activate_date_iso=activate_date_iso,
            properties=properties,
            label_translation_key=label_translation_key,
        )

        wf_collect_node.additional_properties = d
        return wf_collect_node

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
