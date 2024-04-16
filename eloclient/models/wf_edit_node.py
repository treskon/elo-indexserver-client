from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_node import WFNode


T = TypeVar("T", bound="WFEditNode")


@_attrs_define
class WFEditNode:
    """Data required for processing a workflow person node.

    Attributes:
        succ_nodes (Union[Unset, List['WFNode']]):
        node (Union[Unset, WFNode]): <p>
            Objects of this class represent a workflow node.
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        flow_id (Union[Unset, int]): Workflow identifier
        node_id (Union[Unset, int]): Node identifier
    """

    succ_nodes: Union[Unset, List["WFNode"]] = UNSET
    node: Union[Unset, "WFNode"] = UNSET
    flow_id: Union[Unset, int] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        succ_nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.succ_nodes, Unset):
            succ_nodes = []
            for succ_nodes_item_data in self.succ_nodes:
                succ_nodes_item = succ_nodes_item_data.to_dict()
                succ_nodes.append(succ_nodes_item)

        node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        flow_id = self.flow_id

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if succ_nodes is not UNSET:
            field_dict["succNodes"] = succ_nodes
        if node is not UNSET:
            field_dict["node"] = node
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_node import WFNode

        d = src_dict.copy()
        succ_nodes = []
        _succ_nodes = d.pop("succNodes", UNSET)
        for succ_nodes_item_data in _succ_nodes or []:
            succ_nodes_item = WFNode.from_dict(succ_nodes_item_data)

            succ_nodes.append(succ_nodes_item)

        _node = d.pop("node", UNSET)
        node: Union[Unset, WFNode]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = WFNode.from_dict(_node)

        flow_id = d.pop("flowId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        wf_edit_node = cls(
            succ_nodes=succ_nodes,
            node=node,
            flow_id=flow_id,
            node_id=node_id,
        )

        wf_edit_node.additional_properties = d
        return wf_edit_node

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
