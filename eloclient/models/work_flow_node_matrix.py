from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowNodeMatrix")


@_attrs_define
class WorkFlowNodeMatrix:
    """Helperclass to access the node matrix.

    Attributes:
        succ_11 (Union[Unset, int]):
        succ_10 (Union[Unset, int]):
        succ_13 (Union[Unset, int]):
        succ_12 (Union[Unset, int]):
        is_next (Union[Unset, int]): Contains 1, if this node is active.
            DB column: wf_is_next
        flow_id (Union[Unset, int]): Workflow ID
        succ_9 (Union[Unset, int]):
        succ_overtime (Union[Unset, int]): Id of successor node, which should be activated by the escalation.
        succ_5 (Union[Unset, int]):
        succ_6 (Union[Unset, int]):
        succ_7 (Union[Unset, int]):
        succ_8 (Union[Unset, int]):
        succ_1 (Union[Unset, int]):
        succ_2 (Union[Unset, int]):
        succ_3 (Union[Unset, int]):
        succ_4 (Union[Unset, int]):
        succ_0 (Union[Unset, int]):
        succ_19 (Union[Unset, int]):
        succ_18 (Union[Unset, int]):
        version_id (Union[Unset, int]): Version ID.
        succ_15 (Union[Unset, int]):
        succ_14 (Union[Unset, int]):
        succ_17 (Union[Unset, int]):
        succ_type (Union[Unset, int]): Type of successor node.
        succ_16 (Union[Unset, int]):
        terminate (Union[Unset, int]): ELO-date when the node was exited.
            DB column: wf_terminate
        node_id (Union[Unset, int]): Node ID
    """

    succ_11: Union[Unset, int] = UNSET
    succ_10: Union[Unset, int] = UNSET
    succ_13: Union[Unset, int] = UNSET
    succ_12: Union[Unset, int] = UNSET
    is_next: Union[Unset, int] = UNSET
    flow_id: Union[Unset, int] = UNSET
    succ_9: Union[Unset, int] = UNSET
    succ_overtime: Union[Unset, int] = UNSET
    succ_5: Union[Unset, int] = UNSET
    succ_6: Union[Unset, int] = UNSET
    succ_7: Union[Unset, int] = UNSET
    succ_8: Union[Unset, int] = UNSET
    succ_1: Union[Unset, int] = UNSET
    succ_2: Union[Unset, int] = UNSET
    succ_3: Union[Unset, int] = UNSET
    succ_4: Union[Unset, int] = UNSET
    succ_0: Union[Unset, int] = UNSET
    succ_19: Union[Unset, int] = UNSET
    succ_18: Union[Unset, int] = UNSET
    version_id: Union[Unset, int] = UNSET
    succ_15: Union[Unset, int] = UNSET
    succ_14: Union[Unset, int] = UNSET
    succ_17: Union[Unset, int] = UNSET
    succ_type: Union[Unset, int] = UNSET
    succ_16: Union[Unset, int] = UNSET
    terminate: Union[Unset, int] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        succ_11 = self.succ_11

        succ_10 = self.succ_10

        succ_13 = self.succ_13

        succ_12 = self.succ_12

        is_next = self.is_next

        flow_id = self.flow_id

        succ_9 = self.succ_9

        succ_overtime = self.succ_overtime

        succ_5 = self.succ_5

        succ_6 = self.succ_6

        succ_7 = self.succ_7

        succ_8 = self.succ_8

        succ_1 = self.succ_1

        succ_2 = self.succ_2

        succ_3 = self.succ_3

        succ_4 = self.succ_4

        succ_0 = self.succ_0

        succ_19 = self.succ_19

        succ_18 = self.succ_18

        version_id = self.version_id

        succ_15 = self.succ_15

        succ_14 = self.succ_14

        succ_17 = self.succ_17

        succ_type = self.succ_type

        succ_16 = self.succ_16

        terminate = self.terminate

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if succ_11 is not UNSET:
            field_dict["succ_11"] = succ_11
        if succ_10 is not UNSET:
            field_dict["succ_10"] = succ_10
        if succ_13 is not UNSET:
            field_dict["succ_13"] = succ_13
        if succ_12 is not UNSET:
            field_dict["succ_12"] = succ_12
        if is_next is not UNSET:
            field_dict["isNext"] = is_next
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if succ_9 is not UNSET:
            field_dict["succ_9"] = succ_9
        if succ_overtime is not UNSET:
            field_dict["succOvertime"] = succ_overtime
        if succ_5 is not UNSET:
            field_dict["succ_5"] = succ_5
        if succ_6 is not UNSET:
            field_dict["succ_6"] = succ_6
        if succ_7 is not UNSET:
            field_dict["succ_7"] = succ_7
        if succ_8 is not UNSET:
            field_dict["succ_8"] = succ_8
        if succ_1 is not UNSET:
            field_dict["succ_1"] = succ_1
        if succ_2 is not UNSET:
            field_dict["succ_2"] = succ_2
        if succ_3 is not UNSET:
            field_dict["succ_3"] = succ_3
        if succ_4 is not UNSET:
            field_dict["succ_4"] = succ_4
        if succ_0 is not UNSET:
            field_dict["succ_0"] = succ_0
        if succ_19 is not UNSET:
            field_dict["succ_19"] = succ_19
        if succ_18 is not UNSET:
            field_dict["succ_18"] = succ_18
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
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
        if terminate is not UNSET:
            field_dict["terminate"] = terminate
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        succ_11 = d.pop("succ_11", UNSET)

        succ_10 = d.pop("succ_10", UNSET)

        succ_13 = d.pop("succ_13", UNSET)

        succ_12 = d.pop("succ_12", UNSET)

        is_next = d.pop("isNext", UNSET)

        flow_id = d.pop("flowId", UNSET)

        succ_9 = d.pop("succ_9", UNSET)

        succ_overtime = d.pop("succOvertime", UNSET)

        succ_5 = d.pop("succ_5", UNSET)

        succ_6 = d.pop("succ_6", UNSET)

        succ_7 = d.pop("succ_7", UNSET)

        succ_8 = d.pop("succ_8", UNSET)

        succ_1 = d.pop("succ_1", UNSET)

        succ_2 = d.pop("succ_2", UNSET)

        succ_3 = d.pop("succ_3", UNSET)

        succ_4 = d.pop("succ_4", UNSET)

        succ_0 = d.pop("succ_0", UNSET)

        succ_19 = d.pop("succ_19", UNSET)

        succ_18 = d.pop("succ_18", UNSET)

        version_id = d.pop("versionId", UNSET)

        succ_15 = d.pop("succ_15", UNSET)

        succ_14 = d.pop("succ_14", UNSET)

        succ_17 = d.pop("succ_17", UNSET)

        succ_type = d.pop("succType", UNSET)

        succ_16 = d.pop("succ_16", UNSET)

        terminate = d.pop("terminate", UNSET)

        node_id = d.pop("nodeId", UNSET)

        work_flow_node_matrix = cls(
            succ_11=succ_11,
            succ_10=succ_10,
            succ_13=succ_13,
            succ_12=succ_12,
            is_next=is_next,
            flow_id=flow_id,
            succ_9=succ_9,
            succ_overtime=succ_overtime,
            succ_5=succ_5,
            succ_6=succ_6,
            succ_7=succ_7,
            succ_8=succ_8,
            succ_1=succ_1,
            succ_2=succ_2,
            succ_3=succ_3,
            succ_4=succ_4,
            succ_0=succ_0,
            succ_19=succ_19,
            succ_18=succ_18,
            version_id=version_id,
            succ_15=succ_15,
            succ_14=succ_14,
            succ_17=succ_17,
            succ_type=succ_type,
            succ_16=succ_16,
            terminate=terminate,
            node_id=node_id,
        )

        work_flow_node_matrix.additional_properties = d
        return work_flow_node_matrix

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
