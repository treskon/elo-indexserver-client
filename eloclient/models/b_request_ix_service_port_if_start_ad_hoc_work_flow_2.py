from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.start_ad_hoc_workflow_info import StartAdHocWorkflowInfo
    from ..models.user_node_info import UserNodeInfo


T = TypeVar("T", bound="BRequestIXServicePortIFStartAdHocWorkFlow2")


@_attrs_define
class BRequestIXServicePortIFStartAdHocWorkFlow2:
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
        name (Union[Unset, str]):
        obj_id (Union[Unset, str]):
        user_node_info (Union[Unset, List['UserNodeInfo']]):
        start_wf_info (Union[Unset, StartAdHocWorkflowInfo]): This class contains several options that are used to start
            the AdHocWorkflow
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    user_node_info: Union[Unset, List["UserNodeInfo"]] = UNSET
    start_wf_info: Union[Unset, "StartAdHocWorkflowInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        name = self.name

        obj_id = self.obj_id

        user_node_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_node_info, Unset):
            user_node_info = []
            for user_node_info_item_data in self.user_node_info:
                user_node_info_item = user_node_info_item_data.to_dict()
                user_node_info.append(user_node_info_item)

        start_wf_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_wf_info, Unset):
            start_wf_info = self.start_wf_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if user_node_info is not UNSET:
            field_dict["userNodeInfo"] = user_node_info
        if start_wf_info is not UNSET:
            field_dict["startWfInfo"] = start_wf_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.start_ad_hoc_workflow_info import StartAdHocWorkflowInfo
        from ..models.user_node_info import UserNodeInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        user_node_info = []
        _user_node_info = d.pop("userNodeInfo", UNSET)
        for user_node_info_item_data in _user_node_info or []:
            user_node_info_item = UserNodeInfo.from_dict(user_node_info_item_data)

            user_node_info.append(user_node_info_item)

        _start_wf_info = d.pop("startWfInfo", UNSET)
        start_wf_info: Union[Unset, StartAdHocWorkflowInfo]
        if isinstance(_start_wf_info, Unset):
            start_wf_info = UNSET
        else:
            start_wf_info = StartAdHocWorkflowInfo.from_dict(_start_wf_info)

        b_request_ix_service_port_if_start_ad_hoc_work_flow_2 = cls(
            ci=ci,
            name=name,
            obj_id=obj_id,
            user_node_info=user_node_info,
            start_wf_info=start_wf_info,
        )

        b_request_ix_service_port_if_start_ad_hoc_work_flow_2.additional_properties = d
        return b_request_ix_service_port_if_start_ad_hoc_work_flow_2

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
