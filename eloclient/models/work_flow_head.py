from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowHead")


@_attrs_define
class WorkFlowHead:
    """Helperclass to access the DB table workflowtemplhead, workflowactivedochead, ...

    Attributes:
        flow_id (Union[Unset, int]): Workflow ID
        t_stamp (Union[Unset, str]): Timestamp The format is JJJJ.MM.DD.hh.mm.
            ss
        guid (Union[Unset, str]): GUID
        status (Union[Unset, int]): Status, != 0 means deleted
        type (Union[Unset, int]): Workflow type.
        act_server_id (Union[Unset, str]): The current sever ID (resp. replication branch) where the workflow can be
            condinued.
        parent_workflow (Union[Unset, int]): Id of the main workflow.
        call_node_id (Union[Unset, int]): The call node id of the main workflow, which call this sub workflow.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
    """

    flow_id: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    act_server_id: Union[Unset, str] = UNSET
    parent_workflow: Union[Unset, int] = UNSET
    call_node_id: Union[Unset, int] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flow_id = self.flow_id
        t_stamp = self.t_stamp
        guid = self.guid
        status = self.status
        type = self.type
        act_server_id = self.act_server_id
        parent_workflow = self.parent_workflow
        call_node_id = self.call_node_id
        t_stamp_sync = self.t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if guid is not UNSET:
            field_dict["guid"] = guid
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if act_server_id is not UNSET:
            field_dict["actServerId"] = act_server_id
        if parent_workflow is not UNSET:
            field_dict["parentWorkflow"] = parent_workflow
        if call_node_id is not UNSET:
            field_dict["callNodeId"] = call_node_id
        if t_stamp_sync is not UNSET:
            field_dict["tStampSync"] = t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flow_id = d.pop("flowId", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        guid = d.pop("guid", UNSET)

        status = d.pop("status", UNSET)

        type = d.pop("type", UNSET)

        act_server_id = d.pop("actServerId", UNSET)

        parent_workflow = d.pop("parentWorkflow", UNSET)

        call_node_id = d.pop("callNodeId", UNSET)

        t_stamp_sync = d.pop("tStampSync", UNSET)

        work_flow_head = cls(
            flow_id=flow_id,
            t_stamp=t_stamp,
            guid=guid,
            status=status,
            type=type,
            act_server_id=act_server_id,
            parent_workflow=parent_workflow,
            call_node_id=call_node_id,
            t_stamp_sync=t_stamp_sync,
        )

        work_flow_head.additional_properties = d
        return work_flow_head

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
