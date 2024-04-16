from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.forward_workflow_node_info import ForwardWorkflowNodeInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFForwardWorkflowNode")


@_attrs_define
class BRequestIXServicePortIFForwardWorkflowNode:
    """
    Attributes:
        fwd_info (Union[Unset, ForwardWorkflowNodeInfo]): This class controls workflow node forwarding in
            {@link IXServicePortIF#forwardWorkflowNode(ClientInfo, int, int, ForwardWorkflowNodeInfo, LockZ)}.
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        flow_id (Union[Unset, int]):
        node_id (Union[Unset, int]):
    """

    fwd_info: Union[Unset, "ForwardWorkflowNodeInfo"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    flow_id: Union[Unset, int] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fwd_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fwd_info, Unset):
            fwd_info = self.fwd_info.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        flow_id = self.flow_id

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fwd_info is not UNSET:
            field_dict["fwdInfo"] = fwd_info
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.forward_workflow_node_info import ForwardWorkflowNodeInfo
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _fwd_info = d.pop("fwdInfo", UNSET)
        fwd_info: Union[Unset, ForwardWorkflowNodeInfo]
        if isinstance(_fwd_info, Unset):
            fwd_info = UNSET
        else:
            fwd_info = ForwardWorkflowNodeInfo.from_dict(_fwd_info)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        flow_id = d.pop("flowId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        b_request_ix_service_port_if_forward_workflow_node = cls(
            fwd_info=fwd_info,
            unlock_z=unlock_z,
            ci=ci,
            flow_id=flow_id,
            node_id=node_id,
        )

        b_request_ix_service_port_if_forward_workflow_node.additional_properties = d
        return b_request_ix_service_port_if_forward_workflow_node

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
