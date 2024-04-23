from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_node import WFNode


T = TypeVar("T", bound="ForwardWorkflowNodeInfo")


@_attrs_define
class ForwardWorkflowNodeInfo:
    """This class controls workflow node forwarding in
    {@link IXServicePortIF#forwardWorkflowNode(ClientInfo, int, int, ForwardWorkflowNodeInfo, LockZ)}.

        Attributes:
            terminate_workflow (Union[Unset, bool]): Terminate the workflow instead of forwarding.
                If this member is true,
                 {@link #successorNodesToActivate} and {@link #node} are ignored.
            node (Union[Unset, WFNode]): <p>
                Objects of this class represent a workflow node.
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            successor_nodes_to_activate (Union[Unset, List[int]]):
    """

    terminate_workflow: Union[Unset, bool] = UNSET
    node: Union[Unset, "WFNode"] = UNSET
    successor_nodes_to_activate: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        terminate_workflow = self.terminate_workflow

        node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        successor_nodes_to_activate: Union[Unset, List[int]] = UNSET
        if not isinstance(self.successor_nodes_to_activate, Unset):
            successor_nodes_to_activate = self.successor_nodes_to_activate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terminate_workflow is not UNSET:
            field_dict["terminateWorkflow"] = terminate_workflow
        if node is not UNSET:
            field_dict["node"] = node
        if successor_nodes_to_activate is not UNSET:
            field_dict["successorNodesToActivate"] = successor_nodes_to_activate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_node import WFNode

        d = src_dict.copy()
        terminate_workflow = d.pop("terminateWorkflow", UNSET)

        _node = d.pop("node", UNSET)
        node: Union[Unset, WFNode]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = WFNode.from_dict(_node)

        successor_nodes_to_activate = cast(List[int], d.pop("successorNodesToActivate", UNSET))

        forward_workflow_node_info = cls(
            terminate_workflow=terminate_workflow,
            node=node,
            successor_nodes_to_activate=successor_nodes_to_activate,
        )

        forward_workflow_node_info.additional_properties = d
        return forward_workflow_node_info

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
