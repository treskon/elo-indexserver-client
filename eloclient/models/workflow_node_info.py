from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowNodeInfo")


@_attrs_define
class WorkflowNodeInfo:
    """
    Attributes:
        node_name (Union[Unset, str]): The node name
        workflow (Union[Unset, str]): The template ID of the subworkflow to start.
        flags (Union[Unset, int]): Control flags for the node, a combination of WFNode.C.FLAG_* constants.
    """

    node_name: Union[Unset, str] = UNSET
    workflow: Union[Unset, str] = UNSET
    flags: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_name = self.node_name

        workflow = self.workflow

        flags = self.flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_name = d.pop("nodeName", UNSET)

        workflow = d.pop("workflow", UNSET)

        flags = d.pop("flags", UNSET)

        workflow_node_info = cls(
            node_name=node_name,
            workflow=workflow,
            flags=flags,
        )

        workflow_node_info.additional_properties = d
        return workflow_node_info

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
