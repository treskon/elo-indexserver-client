from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_class import ValueClass
    from ..models.wf_time_limit import WFTimeLimit


T = TypeVar("T", bound="StartAdHocWorkflowInfo")


@_attrs_define
class StartAdHocWorkflowInfo:
    """This class contains several options that are used to start the AdHocWorkflow

    Attributes:
        for_validation (Union[Unset, bool]): If true, the workflow comes back to the user who started it.
        serial_flow (Union[Unset, bool]): If true, the workflow routes the object from user to user.
            The workflow finishes when the last user has edited
             their node. If <code>serialFlow</code> is false, the workflow routes the object to all users. The first user
            who
             edits their node terminates the workflow.
        cancel_user_id (Union[Unset, str]): If the workflow is canceled, this user receives a message,
            <code>cancelMessage</code>.
        cancel_message (Union[Unset, str]): The message that is send to the user specified with
            <code>cancelUserId</code>, if the workflow is canceled.
        finished_user_id (Union[Unset, str]): If the workflow is finished, this user receives a message,
            <code>finishedMessage</code>.
        finished_message (Union[Unset, str]): The message that is send to the user specified with
            <code>finishedUserId</code>, if the workflow is finished.
        finished_script (Union[Unset, str]): This script is executed, when the workflow is finished.
        node_name (Union[Unset, str]): Start node name.
        workflow_repeat_message (Union[Unset, str]): This message is send to the user who started the workflow if the
            workflow is repeated.
        break_workflow_message (Union[Unset, str]): This message is send to the user who started the workflow if the
            workflow is canceled.
        user_ids_to_deactivate (Union[Unset, List[str]]):
        deactivate_nodes (Union[Unset, bool]): If true, all person nodes are deactivated when the workflow is canceled.
            This option is only used for "parallel for
             validation" workflow. Otherwise this option is ignored.
        accept_message (Union[Unset, str]): This message is shown if the workflow is accepted by a person.
        notice_message (Union[Unset, str]): This message is shown if the a person was informed about the workflow.
        action_reject_message (Union[Unset, str]): This message is shown if the workflow is rejected.
        success_message (Union[Unset, str]): This message is shown if the workflow is successfully processed.
        time_limit (Union[Unset, WFTimeLimit]): This class describes a time limit for a workflow or for a person node of
            a workflow.
        time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
        flags (Union[Unset, int]): Control flags for the node, a combination of WFNode.C.FLAG_* constants.
        node_infos (Union[Unset, List['ValueClass']]):
    """

    for_validation: Union[Unset, bool] = UNSET
    serial_flow: Union[Unset, bool] = UNSET
    cancel_user_id: Union[Unset, str] = UNSET
    cancel_message: Union[Unset, str] = UNSET
    finished_user_id: Union[Unset, str] = UNSET
    finished_message: Union[Unset, str] = UNSET
    finished_script: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    workflow_repeat_message: Union[Unset, str] = UNSET
    break_workflow_message: Union[Unset, str] = UNSET
    user_ids_to_deactivate: Union[Unset, List[str]] = UNSET
    deactivate_nodes: Union[Unset, bool] = UNSET
    accept_message: Union[Unset, str] = UNSET
    notice_message: Union[Unset, str] = UNSET
    action_reject_message: Union[Unset, str] = UNSET
    success_message: Union[Unset, str] = UNSET
    time_limit: Union[Unset, "WFTimeLimit"] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    flags: Union[Unset, int] = UNSET
    node_infos: Union[Unset, List["ValueClass"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        for_validation = self.for_validation
        serial_flow = self.serial_flow
        cancel_user_id = self.cancel_user_id
        cancel_message = self.cancel_message
        finished_user_id = self.finished_user_id
        finished_message = self.finished_message
        finished_script = self.finished_script
        node_name = self.node_name
        workflow_repeat_message = self.workflow_repeat_message
        break_workflow_message = self.break_workflow_message
        user_ids_to_deactivate: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ids_to_deactivate, Unset):
            user_ids_to_deactivate = self.user_ids_to_deactivate

        deactivate_nodes = self.deactivate_nodes
        accept_message = self.accept_message
        notice_message = self.notice_message
        action_reject_message = self.action_reject_message
        success_message = self.success_message
        time_limit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_limit, Unset):
            time_limit = self.time_limit.to_dict()

        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()

                time_limit_escalations.append(time_limit_escalations_item)

        flags = self.flags
        node_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.node_infos, Unset):
            node_infos = []
            for componentsschemas_list_of_value_class_item_data in self.node_infos:
                componentsschemas_list_of_value_class_item = componentsschemas_list_of_value_class_item_data.to_dict()

                node_infos.append(componentsschemas_list_of_value_class_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if for_validation is not UNSET:
            field_dict["forValidation"] = for_validation
        if serial_flow is not UNSET:
            field_dict["serialFlow"] = serial_flow
        if cancel_user_id is not UNSET:
            field_dict["cancelUserId"] = cancel_user_id
        if cancel_message is not UNSET:
            field_dict["cancelMessage"] = cancel_message
        if finished_user_id is not UNSET:
            field_dict["finishedUserId"] = finished_user_id
        if finished_message is not UNSET:
            field_dict["finishedMessage"] = finished_message
        if finished_script is not UNSET:
            field_dict["finishedScript"] = finished_script
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if workflow_repeat_message is not UNSET:
            field_dict["workflowRepeatMessage"] = workflow_repeat_message
        if break_workflow_message is not UNSET:
            field_dict["breakWorkflowMessage"] = break_workflow_message
        if user_ids_to_deactivate is not UNSET:
            field_dict["userIdsToDeactivate"] = user_ids_to_deactivate
        if deactivate_nodes is not UNSET:
            field_dict["deactivateNodes"] = deactivate_nodes
        if accept_message is not UNSET:
            field_dict["acceptMessage"] = accept_message
        if notice_message is not UNSET:
            field_dict["noticeMessage"] = notice_message
        if action_reject_message is not UNSET:
            field_dict["actionRejectMessage"] = action_reject_message
        if success_message is not UNSET:
            field_dict["successMessage"] = success_message
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if flags is not UNSET:
            field_dict["flags"] = flags
        if node_infos is not UNSET:
            field_dict["nodeInfos"] = node_infos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.value_class import ValueClass
        from ..models.wf_time_limit import WFTimeLimit

        d = src_dict.copy()
        for_validation = d.pop("forValidation", UNSET)

        serial_flow = d.pop("serialFlow", UNSET)

        cancel_user_id = d.pop("cancelUserId", UNSET)

        cancel_message = d.pop("cancelMessage", UNSET)

        finished_user_id = d.pop("finishedUserId", UNSET)

        finished_message = d.pop("finishedMessage", UNSET)

        finished_script = d.pop("finishedScript", UNSET)

        node_name = d.pop("nodeName", UNSET)

        workflow_repeat_message = d.pop("workflowRepeatMessage", UNSET)

        break_workflow_message = d.pop("breakWorkflowMessage", UNSET)

        user_ids_to_deactivate = cast(List[str], d.pop("userIdsToDeactivate", UNSET))

        deactivate_nodes = d.pop("deactivateNodes", UNSET)

        accept_message = d.pop("acceptMessage", UNSET)

        notice_message = d.pop("noticeMessage", UNSET)

        action_reject_message = d.pop("actionRejectMessage", UNSET)

        success_message = d.pop("successMessage", UNSET)

        _time_limit = d.pop("timeLimit", UNSET)
        time_limit: Union[Unset, WFTimeLimit]
        if isinstance(_time_limit, Unset):
            time_limit = UNSET
        else:
            time_limit = WFTimeLimit.from_dict(_time_limit)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        flags = d.pop("flags", UNSET)

        node_infos = []
        _node_infos = d.pop("nodeInfos", UNSET)
        for componentsschemas_list_of_value_class_item_data in _node_infos or []:
            componentsschemas_list_of_value_class_item = ValueClass.from_dict(
                componentsschemas_list_of_value_class_item_data
            )

            node_infos.append(componentsschemas_list_of_value_class_item)

        start_ad_hoc_workflow_info = cls(
            for_validation=for_validation,
            serial_flow=serial_flow,
            cancel_user_id=cancel_user_id,
            cancel_message=cancel_message,
            finished_user_id=finished_user_id,
            finished_message=finished_message,
            finished_script=finished_script,
            node_name=node_name,
            workflow_repeat_message=workflow_repeat_message,
            break_workflow_message=break_workflow_message,
            user_ids_to_deactivate=user_ids_to_deactivate,
            deactivate_nodes=deactivate_nodes,
            accept_message=accept_message,
            notice_message=notice_message,
            action_reject_message=action_reject_message,
            success_message=success_message,
            time_limit=time_limit,
            time_limit_escalations=time_limit_escalations,
            flags=flags,
            node_infos=node_infos,
        )

        start_ad_hoc_workflow_info.additional_properties = d
        return start_ad_hoc_workflow_info

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
