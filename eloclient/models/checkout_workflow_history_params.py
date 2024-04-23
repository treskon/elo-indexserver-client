from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutWorkflowHistoryParams")


@_attrs_define
class CheckoutWorkflowHistoryParams:
    """Parameter class for the method checkoutWorkflowHistory.

    Attributes:
        flow_id (Union[Unset, str]): Workflow ID or workflow GUID.
        node_id (Union[Unset, int]): Node ID. If node ID is 0, histories of all node are return.
    """

    flow_id: Union[Unset, str] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flow_id = self.flow_id

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flow_id = d.pop("flowId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        checkout_workflow_history_params = cls(
            flow_id=flow_id,
            node_id=node_id,
        )

        checkout_workflow_history_params.additional_properties = d
        return checkout_workflow_history_params

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
