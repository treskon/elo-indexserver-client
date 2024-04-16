from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.wf_diagram_z import WFDiagramZ
    from ..models.wf_type_z import WFTypeZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutWorkFlow")


@_attrs_define
class BRequestIXServicePortIFCheckoutWorkFlow:
    """
    Attributes:
        work_flow_diagram_z (Union[Unset, WFDiagramZ]): This class encapsulates the constants of the WFDiagramC class.
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
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        type_z (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        flow_id (Union[Unset, str]):
    """

    work_flow_diagram_z: Union[Unset, "WFDiagramZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    type_z: Union[Unset, "WFTypeZ"] = UNSET
    flow_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_flow_diagram_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_flow_diagram_z, Unset):
            work_flow_diagram_z = self.work_flow_diagram_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        type_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type_z, Unset):
            type_z = self.type_z.to_dict()

        flow_id = self.flow_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_flow_diagram_z is not UNSET:
            field_dict["workFlowDiagramZ"] = work_flow_diagram_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if type_z is not UNSET:
            field_dict["typeZ"] = type_z
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.wf_diagram_z import WFDiagramZ
        from ..models.wf_type_z import WFTypeZ

        d = src_dict.copy()
        _work_flow_diagram_z = d.pop("workFlowDiagramZ", UNSET)
        work_flow_diagram_z: Union[Unset, WFDiagramZ]
        if isinstance(_work_flow_diagram_z, Unset):
            work_flow_diagram_z = UNSET
        else:
            work_flow_diagram_z = WFDiagramZ.from_dict(_work_flow_diagram_z)

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

        _type_z = d.pop("typeZ", UNSET)
        type_z: Union[Unset, WFTypeZ]
        if isinstance(_type_z, Unset):
            type_z = UNSET
        else:
            type_z = WFTypeZ.from_dict(_type_z)

        flow_id = d.pop("flowId", UNSET)

        b_request_ix_service_port_if_checkout_work_flow = cls(
            work_flow_diagram_z=work_flow_diagram_z,
            ci=ci,
            lock_z=lock_z,
            type_z=type_z,
            flow_id=flow_id,
        )

        b_request_ix_service_port_if_checkout_work_flow.additional_properties = d
        return b_request_ix_service_port_if_checkout_work_flow

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
