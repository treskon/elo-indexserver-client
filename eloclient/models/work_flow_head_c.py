from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowHeadC")


@_attrs_define
class WorkFlowHeadC:
    """<p>Bit constants for members of WorkFlowHead</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_flow_id (Union[Unset, str]): Member bit: Workflow ID
                DB column: wfflowid
            mb_type (Union[Unset, str]): Member bit: Workflow type.
                DB column: wftype
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp The format is JJJJ.MM.DD.hh.mm.
                ss
                 DB column: wftstamp
            mb_act_server_id (Union[Unset, str]): Member bit: The current sever ID (resp. replication branch) where the
                workflow can be condinued.
                DB column: actserverid
            ln_act_server_id (Union[Unset, int]): Column length: The current sever ID (resp. replication branch) where the
                workflow can be condinued.
                DB column: actserverid
            mb_call_node_id (Union[Unset, str]): Member bit: The call node id of the main workflow, which call this sub
                workflow.
                DB column: callnodeid
            ln_guid (Union[Unset, int]): Column length: GUID
                DB column: wfguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: wftstampsync
            mb_status (Union[Unset, str]): Member bit: Status, != 0 means deleted
                DB column: wfstatus
            mb_parent_workflow (Union[Unset, str]): Member bit: Id of the main workflow.
                DB column: wfParent
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_guid (Union[Unset, str]): Member bit: GUID
                DB column: wfguid
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp The format is JJJJ.MM.DD.hh.mm.
                ss
                 DB column: wftstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: wftstampsync
    """

    mb_flow_id: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_act_server_id: Union[Unset, str] = UNSET
    ln_act_server_id: Union[Unset, int] = UNSET
    mb_call_node_id: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_parent_workflow: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_flow_id = self.mb_flow_id

        mb_type = self.mb_type

        mb_t_stamp = self.mb_t_stamp

        mb_act_server_id = self.mb_act_server_id

        ln_act_server_id = self.ln_act_server_id

        mb_call_node_id = self.mb_call_node_id

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_status = self.mb_status

        mb_parent_workflow = self.mb_parent_workflow

        mb_all_members = self.mb_all_members

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_flow_id is not UNSET:
            field_dict["mbFlowId"] = mb_flow_id
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_act_server_id is not UNSET:
            field_dict["mbActServerId"] = mb_act_server_id
        if ln_act_server_id is not UNSET:
            field_dict["lnActServerId"] = ln_act_server_id
        if mb_call_node_id is not UNSET:
            field_dict["mbCallNodeId"] = mb_call_node_id
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_parent_workflow is not UNSET:
            field_dict["mbParentWorkflow"] = mb_parent_workflow
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_flow_id = d.pop("mbFlowId", UNSET)

        mb_type = d.pop("mbType", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_act_server_id = d.pop("mbActServerId", UNSET)

        ln_act_server_id = d.pop("lnActServerId", UNSET)

        mb_call_node_id = d.pop("mbCallNodeId", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_parent_workflow = d.pop("mbParentWorkflow", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        work_flow_head_c = cls(
            mb_flow_id=mb_flow_id,
            mb_type=mb_type,
            mb_t_stamp=mb_t_stamp,
            mb_act_server_id=mb_act_server_id,
            ln_act_server_id=ln_act_server_id,
            mb_call_node_id=mb_call_node_id,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_status=mb_status,
            mb_parent_workflow=mb_parent_workflow,
            mb_all_members=mb_all_members,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
        )

        work_flow_head_c.additional_properties = d
        return work_flow_head_c

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
