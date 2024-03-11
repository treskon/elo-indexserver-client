from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFTakeWorkFlowNode")


@_attrs_define
class BRequestIXServicePortIFTakeWorkFlowNode:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        n_flow_id (Union[Unset, int]):
        n_node_id (Union[Unset, int]):
        s_user_id (Union[Unset, str]):
        n_flags (Union[Unset, int]):
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    n_flow_id: Union[Unset, int] = UNSET
    n_node_id: Union[Unset, int] = UNSET
    s_user_id: Union[Unset, str] = UNSET
    n_flags: Union[Unset, int] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        n_flow_id = self.n_flow_id
        n_node_id = self.n_node_id
        s_user_id = self.s_user_id
        n_flags = self.n_flags
        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if n_flow_id is not UNSET:
            field_dict["nFlowId"] = n_flow_id
        if n_node_id is not UNSET:
            field_dict["nNodeId"] = n_node_id
        if s_user_id is not UNSET:
            field_dict["sUserId"] = s_user_id
        if n_flags is not UNSET:
            field_dict["nFlags"] = n_flags
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        n_flow_id = d.pop("nFlowId", UNSET)

        n_node_id = d.pop("nNodeId", UNSET)

        s_user_id = d.pop("sUserId", UNSET)

        n_flags = d.pop("nFlags", UNSET)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        b_request_ix_service_port_if_take_work_flow_node = cls(
            ci=ci,
            n_flow_id=n_flow_id,
            n_node_id=n_node_id,
            s_user_id=s_user_id,
            n_flags=n_flags,
            lock_z=lock_z,
        )

        b_request_ix_service_port_if_take_work_flow_node.additional_properties = d
        return b_request_ix_service_port_if_take_work_flow_node

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
