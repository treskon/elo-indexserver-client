from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.begin_forward_workflow_node_info import BeginForwardWorkflowNodeInfo
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFBeginForwardWorkflowNode")


@_attrs_define
class BRequestIXServicePortIFBeginForwardWorkflowNode:
    """
    Attributes:
        fwd_info (Union[Unset, BeginForwardWorkflowNodeInfo]):
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
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        flow_id (Union[Unset, int]):
        node_id (Union[Unset, int]):
    """

    fwd_info: Union[Unset, "BeginForwardWorkflowNodeInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    flow_id: Union[Unset, int] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fwd_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fwd_info, Unset):
            fwd_info = self.fwd_info.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        flow_id = self.flow_id

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fwd_info is not UNSET:
            field_dict["fwdInfo"] = fwd_info
        if ci is not UNSET:
            field_dict["ci"] = ci
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.begin_forward_workflow_node_info import BeginForwardWorkflowNodeInfo
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _fwd_info = d.pop("fwdInfo", UNSET)
        fwd_info: Union[Unset, BeginForwardWorkflowNodeInfo]
        if isinstance(_fwd_info, Unset):
            fwd_info = UNSET
        else:
            fwd_info = BeginForwardWorkflowNodeInfo.from_dict(_fwd_info)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        flow_id = d.pop("flowId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        b_request_ix_service_port_if_begin_forward_workflow_node = cls(
            fwd_info=fwd_info,
            ci=ci,
            lock_z=lock_z,
            flow_id=flow_id,
            node_id=node_id,
        )

        b_request_ix_service_port_if_begin_forward_workflow_node.additional_properties = d
        return b_request_ix_service_port_if_begin_forward_workflow_node

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
