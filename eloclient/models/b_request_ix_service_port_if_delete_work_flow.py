from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.wf_type_z import WFTypeZ


T = TypeVar("T", bound="BRequestIXServicePortIFDeleteWorkFlow")


@_attrs_define
class BRequestIXServicePortIFDeleteWorkFlow:
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
        flow_id (Union[Unset, str]):
        type_z (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    flow_id: Union[Unset, str] = UNSET
    type_z: Union[Unset, "WFTypeZ"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        flow_id = self.flow_id
        type_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type_z, Unset):
            type_z = self.type_z.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if type_z is not UNSET:
            field_dict["typeZ"] = type_z
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.wf_type_z import WFTypeZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        flow_id = d.pop("flowId", UNSET)

        _type_z = d.pop("typeZ", UNSET)
        type_z: Union[Unset, WFTypeZ]
        if isinstance(_type_z, Unset):
            type_z = UNSET
        else:
            type_z = WFTypeZ.from_dict(_type_z)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_service_port_if_delete_work_flow = cls(
            ci=ci,
            flow_id=flow_id,
            type_z=type_z,
            unlock_z=unlock_z,
        )

        b_request_ix_service_port_if_delete_work_flow.additional_properties = d
        return b_request_ix_service_port_if_delete_work_flow

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
