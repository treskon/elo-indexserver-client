from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.start_workflow_info import StartWorkflowInfo


T = TypeVar("T", bound="BRequestIXServicePortIFStartWorkFlow2")


@_attrs_define
class BRequestIXServicePortIFStartWorkFlow2:
    """
    Attributes:
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
        obj_id (Union[Unset, str]):
        start_workflow_info (Union[Unset, StartWorkflowInfo]): This class is used as a parameter in the function
            {@link IXServicePortIF#startWorkFlow2(ClientInfo, String, StartWorkflowInfo)}.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    obj_id: Union[Unset, str] = UNSET
    start_workflow_info: Union[Unset, "StartWorkflowInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        obj_id = self.obj_id

        start_workflow_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_workflow_info, Unset):
            start_workflow_info = self.start_workflow_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if start_workflow_info is not UNSET:
            field_dict["startWorkflowInfo"] = start_workflow_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.start_workflow_info import StartWorkflowInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        obj_id = d.pop("objId", UNSET)

        _start_workflow_info = d.pop("startWorkflowInfo", UNSET)
        start_workflow_info: Union[Unset, StartWorkflowInfo]
        if isinstance(_start_workflow_info, Unset):
            start_workflow_info = UNSET
        else:
            start_workflow_info = StartWorkflowInfo.from_dict(_start_workflow_info)

        b_request_ix_service_port_if_start_work_flow_2 = cls(
            ci=ci,
            obj_id=obj_id,
            start_workflow_info=start_workflow_info,
        )

        b_request_ix_service_port_if_start_work_flow_2.additional_properties = d
        return b_request_ix_service_port_if_start_work_flow_2

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
