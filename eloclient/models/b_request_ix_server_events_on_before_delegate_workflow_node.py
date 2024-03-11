from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.lock_z import LockZ
    from ..models.wf_delegate_node_info import WFDelegateNodeInfo


T = TypeVar("T", bound="BRequestIXServerEventsOnBeforeDelegateWorkflowNode")


@_attrs_define
class BRequestIXServerEventsOnBeforeDelegateWorkflowNode:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        delegate_node_info (Union[Unset, WFDelegateNodeInfo]): This class is used as a parameter in the function
            {@link IXServicePortIF#delegateWorkFlowNode(ClientInfo, WFDelegateNodeInfo, LockZ)}.
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    delegate_node_info: Union[Unset, "WFDelegateNodeInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        delegate_node_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delegate_node_info, Unset):
            delegate_node_info = self.delegate_node_info.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if delegate_node_info is not UNSET:
            field_dict["delegateNodeInfo"] = delegate_node_info
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.lock_z import LockZ
        from ..models.wf_delegate_node_info import WFDelegateNodeInfo

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _delegate_node_info = d.pop("delegateNodeInfo", UNSET)
        delegate_node_info: Union[Unset, WFDelegateNodeInfo]
        if isinstance(_delegate_node_info, Unset):
            delegate_node_info = UNSET
        else:
            delegate_node_info = WFDelegateNodeInfo.from_dict(_delegate_node_info)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        b_request_ix_server_events_on_before_delegate_workflow_node = cls(
            ec=ec,
            delegate_node_info=delegate_node_info,
            lock_z=lock_z,
        )

        b_request_ix_server_events_on_before_delegate_workflow_node.additional_properties = d
        return b_request_ix_server_events_on_before_delegate_workflow_node

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
