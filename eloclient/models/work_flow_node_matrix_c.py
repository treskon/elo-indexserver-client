from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowNodeMatrixC")


@_attrs_define
class WorkFlowNodeMatrixC:
    """<p>Bit constants for members of WorkFlowNodeMatrix</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_flow_id (Union[Unset, str]): Member bit: Workflow ID
                DB column: wf_flowid
            mb_terminate (Union[Unset, str]): Member bit: ELO-date when the node was exited.
                DB column: wf_terminate
                 DB column: wf_terminate
            ln_edges_ordinals (Union[Unset, int]): Column length: Sort order of edges.
                DB column: wf_edges_ordinals
            mb_node_id (Union[Unset, str]): Member bit: Node ID
                DB column: wf_nodeid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_succ_10 (Union[Unset, str]): DB column: wf_succ_10
            mb_edges_ordinals (Union[Unset, str]): Member bit: Sort order of edges.
                DB column: wf_edges_ordinals
            mb_succ_4 (Union[Unset, str]): DB column: wf_succ_4
            mb_succ_15 (Union[Unset, str]): DB column: wf_succ_15
            mb_succ_5 (Union[Unset, str]): DB column: wf_succ_5
            mb_succ_16 (Union[Unset, str]): DB column: wf_succ_16
            mb_succ_6 (Union[Unset, str]): DB column: wf_succ_6
            mb_succ_17 (Union[Unset, str]): DB column: wf_succ_17
            mb_succ_7 (Union[Unset, str]): DB column: wf_succ_7
            mb_succ_18 (Union[Unset, str]): DB column: wf_succ_18
            mb_succ_type (Union[Unset, str]): Member bit: Type of successor node.
                DB column: wf_succ_type
            mb_succ_0 (Union[Unset, str]): DB column: wf_succ_0
            mb_succ_11 (Union[Unset, str]): DB column: wf_succ_11
            mb_succ_1 (Union[Unset, str]): DB column: wf_succ_1
            mb_succ_12 (Union[Unset, str]): DB column: wf_succ_12
            mb_succ_2 (Union[Unset, str]): DB column: wf_succ_2
            mb_succ_13 (Union[Unset, str]): DB column: wf_succ_13
            mb_version_id (Union[Unset, str]): Member bit: Version ID.
                DB column: wf_version
            mb_succ_3 (Union[Unset, str]): DB column: wf_succ_3
            mb_succ_14 (Union[Unset, str]): DB column: wf_succ_14
            mb_succ_8 (Union[Unset, str]): DB column: wf_succ_8
            mb_succ_19 (Union[Unset, str]): DB column: wf_succ_19
            mb_succ_9 (Union[Unset, str]): DB column: wf_succ_9
            mb_is_next (Union[Unset, str]): Member bit: Contains 1, if this node is active.
                DB column: wf_is_next
                 DB column: wf_is_next
            mb_succ_overtime (Union[Unset, str]): Member bit: Id of successor node, which should be activated by the
                escalation.
                DB column: wf_succ_overtime
    """

    mb_flow_id: Union[Unset, str] = UNSET
    mb_terminate: Union[Unset, str] = UNSET
    ln_edges_ordinals: Union[Unset, int] = UNSET
    mb_node_id: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_succ_10: Union[Unset, str] = UNSET
    mb_edges_ordinals: Union[Unset, str] = UNSET
    mb_succ_4: Union[Unset, str] = UNSET
    mb_succ_15: Union[Unset, str] = UNSET
    mb_succ_5: Union[Unset, str] = UNSET
    mb_succ_16: Union[Unset, str] = UNSET
    mb_succ_6: Union[Unset, str] = UNSET
    mb_succ_17: Union[Unset, str] = UNSET
    mb_succ_7: Union[Unset, str] = UNSET
    mb_succ_18: Union[Unset, str] = UNSET
    mb_succ_type: Union[Unset, str] = UNSET
    mb_succ_0: Union[Unset, str] = UNSET
    mb_succ_11: Union[Unset, str] = UNSET
    mb_succ_1: Union[Unset, str] = UNSET
    mb_succ_12: Union[Unset, str] = UNSET
    mb_succ_2: Union[Unset, str] = UNSET
    mb_succ_13: Union[Unset, str] = UNSET
    mb_version_id: Union[Unset, str] = UNSET
    mb_succ_3: Union[Unset, str] = UNSET
    mb_succ_14: Union[Unset, str] = UNSET
    mb_succ_8: Union[Unset, str] = UNSET
    mb_succ_19: Union[Unset, str] = UNSET
    mb_succ_9: Union[Unset, str] = UNSET
    mb_is_next: Union[Unset, str] = UNSET
    mb_succ_overtime: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_flow_id = self.mb_flow_id

        mb_terminate = self.mb_terminate

        ln_edges_ordinals = self.ln_edges_ordinals

        mb_node_id = self.mb_node_id

        mb_all_members = self.mb_all_members

        mb_succ_10 = self.mb_succ_10

        mb_edges_ordinals = self.mb_edges_ordinals

        mb_succ_4 = self.mb_succ_4

        mb_succ_15 = self.mb_succ_15

        mb_succ_5 = self.mb_succ_5

        mb_succ_16 = self.mb_succ_16

        mb_succ_6 = self.mb_succ_6

        mb_succ_17 = self.mb_succ_17

        mb_succ_7 = self.mb_succ_7

        mb_succ_18 = self.mb_succ_18

        mb_succ_type = self.mb_succ_type

        mb_succ_0 = self.mb_succ_0

        mb_succ_11 = self.mb_succ_11

        mb_succ_1 = self.mb_succ_1

        mb_succ_12 = self.mb_succ_12

        mb_succ_2 = self.mb_succ_2

        mb_succ_13 = self.mb_succ_13

        mb_version_id = self.mb_version_id

        mb_succ_3 = self.mb_succ_3

        mb_succ_14 = self.mb_succ_14

        mb_succ_8 = self.mb_succ_8

        mb_succ_19 = self.mb_succ_19

        mb_succ_9 = self.mb_succ_9

        mb_is_next = self.mb_is_next

        mb_succ_overtime = self.mb_succ_overtime

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_flow_id is not UNSET:
            field_dict["mbFlowId"] = mb_flow_id
        if mb_terminate is not UNSET:
            field_dict["mbTerminate"] = mb_terminate
        if ln_edges_ordinals is not UNSET:
            field_dict["lnEdgesOrdinals"] = ln_edges_ordinals
        if mb_node_id is not UNSET:
            field_dict["mbNodeId"] = mb_node_id
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_succ_10 is not UNSET:
            field_dict["mbSucc_10"] = mb_succ_10
        if mb_edges_ordinals is not UNSET:
            field_dict["mbEdgesOrdinals"] = mb_edges_ordinals
        if mb_succ_4 is not UNSET:
            field_dict["mbSucc_4"] = mb_succ_4
        if mb_succ_15 is not UNSET:
            field_dict["mbSucc_15"] = mb_succ_15
        if mb_succ_5 is not UNSET:
            field_dict["mbSucc_5"] = mb_succ_5
        if mb_succ_16 is not UNSET:
            field_dict["mbSucc_16"] = mb_succ_16
        if mb_succ_6 is not UNSET:
            field_dict["mbSucc_6"] = mb_succ_6
        if mb_succ_17 is not UNSET:
            field_dict["mbSucc_17"] = mb_succ_17
        if mb_succ_7 is not UNSET:
            field_dict["mbSucc_7"] = mb_succ_7
        if mb_succ_18 is not UNSET:
            field_dict["mbSucc_18"] = mb_succ_18
        if mb_succ_type is not UNSET:
            field_dict["mbSuccType"] = mb_succ_type
        if mb_succ_0 is not UNSET:
            field_dict["mbSucc_0"] = mb_succ_0
        if mb_succ_11 is not UNSET:
            field_dict["mbSucc_11"] = mb_succ_11
        if mb_succ_1 is not UNSET:
            field_dict["mbSucc_1"] = mb_succ_1
        if mb_succ_12 is not UNSET:
            field_dict["mbSucc_12"] = mb_succ_12
        if mb_succ_2 is not UNSET:
            field_dict["mbSucc_2"] = mb_succ_2
        if mb_succ_13 is not UNSET:
            field_dict["mbSucc_13"] = mb_succ_13
        if mb_version_id is not UNSET:
            field_dict["mbVersionId"] = mb_version_id
        if mb_succ_3 is not UNSET:
            field_dict["mbSucc_3"] = mb_succ_3
        if mb_succ_14 is not UNSET:
            field_dict["mbSucc_14"] = mb_succ_14
        if mb_succ_8 is not UNSET:
            field_dict["mbSucc_8"] = mb_succ_8
        if mb_succ_19 is not UNSET:
            field_dict["mbSucc_19"] = mb_succ_19
        if mb_succ_9 is not UNSET:
            field_dict["mbSucc_9"] = mb_succ_9
        if mb_is_next is not UNSET:
            field_dict["mbIsNext"] = mb_is_next
        if mb_succ_overtime is not UNSET:
            field_dict["mbSuccOvertime"] = mb_succ_overtime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_flow_id = d.pop("mbFlowId", UNSET)

        mb_terminate = d.pop("mbTerminate", UNSET)

        ln_edges_ordinals = d.pop("lnEdgesOrdinals", UNSET)

        mb_node_id = d.pop("mbNodeId", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_succ_10 = d.pop("mbSucc_10", UNSET)

        mb_edges_ordinals = d.pop("mbEdgesOrdinals", UNSET)

        mb_succ_4 = d.pop("mbSucc_4", UNSET)

        mb_succ_15 = d.pop("mbSucc_15", UNSET)

        mb_succ_5 = d.pop("mbSucc_5", UNSET)

        mb_succ_16 = d.pop("mbSucc_16", UNSET)

        mb_succ_6 = d.pop("mbSucc_6", UNSET)

        mb_succ_17 = d.pop("mbSucc_17", UNSET)

        mb_succ_7 = d.pop("mbSucc_7", UNSET)

        mb_succ_18 = d.pop("mbSucc_18", UNSET)

        mb_succ_type = d.pop("mbSuccType", UNSET)

        mb_succ_0 = d.pop("mbSucc_0", UNSET)

        mb_succ_11 = d.pop("mbSucc_11", UNSET)

        mb_succ_1 = d.pop("mbSucc_1", UNSET)

        mb_succ_12 = d.pop("mbSucc_12", UNSET)

        mb_succ_2 = d.pop("mbSucc_2", UNSET)

        mb_succ_13 = d.pop("mbSucc_13", UNSET)

        mb_version_id = d.pop("mbVersionId", UNSET)

        mb_succ_3 = d.pop("mbSucc_3", UNSET)

        mb_succ_14 = d.pop("mbSucc_14", UNSET)

        mb_succ_8 = d.pop("mbSucc_8", UNSET)

        mb_succ_19 = d.pop("mbSucc_19", UNSET)

        mb_succ_9 = d.pop("mbSucc_9", UNSET)

        mb_is_next = d.pop("mbIsNext", UNSET)

        mb_succ_overtime = d.pop("mbSuccOvertime", UNSET)

        work_flow_node_matrix_c = cls(
            mb_flow_id=mb_flow_id,
            mb_terminate=mb_terminate,
            ln_edges_ordinals=ln_edges_ordinals,
            mb_node_id=mb_node_id,
            mb_all_members=mb_all_members,
            mb_succ_10=mb_succ_10,
            mb_edges_ordinals=mb_edges_ordinals,
            mb_succ_4=mb_succ_4,
            mb_succ_15=mb_succ_15,
            mb_succ_5=mb_succ_5,
            mb_succ_16=mb_succ_16,
            mb_succ_6=mb_succ_6,
            mb_succ_17=mb_succ_17,
            mb_succ_7=mb_succ_7,
            mb_succ_18=mb_succ_18,
            mb_succ_type=mb_succ_type,
            mb_succ_0=mb_succ_0,
            mb_succ_11=mb_succ_11,
            mb_succ_1=mb_succ_1,
            mb_succ_12=mb_succ_12,
            mb_succ_2=mb_succ_2,
            mb_succ_13=mb_succ_13,
            mb_version_id=mb_version_id,
            mb_succ_3=mb_succ_3,
            mb_succ_14=mb_succ_14,
            mb_succ_8=mb_succ_8,
            mb_succ_19=mb_succ_19,
            mb_succ_9=mb_succ_9,
            mb_is_next=mb_is_next,
            mb_succ_overtime=mb_succ_overtime,
        )

        work_flow_node_matrix_c.additional_properties = d
        return work_flow_node_matrix_c

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
