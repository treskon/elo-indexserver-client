from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.wf_diagram_z import WFDiagramZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutWorkflowTemplate")


@_attrs_define
class BRequestIXServicePortIFCheckoutWorkflowTemplate:
    """
    Attributes:
        version_id (Union[Unset, str]):
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
        wf_z (Union[Unset, WFDiagramZ]): This class encapsulates the constants of the WFDiagramC class.
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
        flow_id (Union[Unset, str]):
    """

    version_id: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    wf_z: Union[Unset, "WFDiagramZ"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    flow_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version_id = self.version_id

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        wf_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wf_z, Unset):
            wf_z = self.wf_z.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        flow_id = self.flow_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if ci is not UNSET:
            field_dict["ci"] = ci
        if wf_z is not UNSET:
            field_dict["wfZ"] = wf_z
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.wf_diagram_z import WFDiagramZ

        d = src_dict.copy()
        version_id = d.pop("versionId", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _wf_z = d.pop("wfZ", UNSET)
        wf_z: Union[Unset, WFDiagramZ]
        if isinstance(_wf_z, Unset):
            wf_z = UNSET
        else:
            wf_z = WFDiagramZ.from_dict(_wf_z)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        flow_id = d.pop("flowId", UNSET)

        b_request_ix_service_port_if_checkout_workflow_template = cls(
            version_id=version_id,
            ci=ci,
            wf_z=wf_z,
            lock_z=lock_z,
            flow_id=flow_id,
        )

        b_request_ix_service_port_if_checkout_workflow_template.additional_properties = d
        return b_request_ix_service_port_if_checkout_workflow_template

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
