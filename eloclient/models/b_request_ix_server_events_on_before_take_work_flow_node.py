from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.lock_z import LockZ
    from ..models.user_info import UserInfo
    from ..models.wf_diagram import WFDiagram
    from ..models.wf_node import WFNode


T = TypeVar("T", bound="BRequestIXServerEventsOnBeforeTakeWorkFlowNode")


@_attrs_define
class BRequestIXServerEventsOnBeforeTakeWorkFlowNode:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        workflow (Union[Unset, WFDiagram]): This class represents an active or finished workflow or a workflow template
        node (Union[Unset, WFNode]): <p>
            Objects of this class represent a workflow node.
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        user (Union[Unset, UserInfo]): <p>
            Data class containing the user information data for the user logged in to the Index server. User information
            includes
             ID, name, rights, parent, etc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        flags (Union[Unset, int]):
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    workflow: Union[Unset, "WFDiagram"] = UNSET
    node: Union[Unset, "WFNode"] = UNSET
    user: Union[Unset, "UserInfo"] = UNSET
    flags: Union[Unset, int] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        flags = self.flags
        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if node is not UNSET:
            field_dict["node"] = node
        if user is not UNSET:
            field_dict["user"] = user
        if flags is not UNSET:
            field_dict["flags"] = flags
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.lock_z import LockZ
        from ..models.user_info import UserInfo
        from ..models.wf_diagram import WFDiagram
        from ..models.wf_node import WFNode

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WFDiagram]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WFDiagram.from_dict(_workflow)

        _node = d.pop("node", UNSET)
        node: Union[Unset, WFNode]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = WFNode.from_dict(_node)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserInfo]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserInfo.from_dict(_user)

        flags = d.pop("flags", UNSET)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        b_request_ix_server_events_on_before_take_work_flow_node = cls(
            ec=ec,
            workflow=workflow,
            node=node,
            user=user,
            flags=flags,
            lock_z=lock_z,
        )

        b_request_ix_server_events_on_before_take_work_flow_node.additional_properties = d
        return b_request_ix_server_events_on_before_take_work_flow_node

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
