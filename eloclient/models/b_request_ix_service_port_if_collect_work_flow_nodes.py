from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.wf_type_z import WFTypeZ


T = TypeVar("T", bound="BRequestIXServicePortIFCollectWorkFlowNodes")


@_attrs_define
class BRequestIXServicePortIFCollectWorkFlowNodes:
    """
    Attributes:
        node_name (Union[Unset, str]):
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
        only_start_nodes (Union[Unset, bool]):
        user_ids (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):
        obj_id (Union[Unset, str]):
        enter_date_iso (Union[Unset, str]):
        exit_date_iso (Union[Unset, str]):
        node_type (Union[Unset, int]):
        flow_name (Union[Unset, str]):
        wf_type_z (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    node_name: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    only_start_nodes: Union[Unset, bool] = UNSET
    user_ids: Union[Unset, List[str]] = UNSET
    only_active: Union[Unset, bool] = UNSET
    obj_id: Union[Unset, str] = UNSET
    enter_date_iso: Union[Unset, str] = UNSET
    exit_date_iso: Union[Unset, str] = UNSET
    node_type: Union[Unset, int] = UNSET
    flow_name: Union[Unset, str] = UNSET
    wf_type_z: Union[Unset, "WFTypeZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_name = self.node_name

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        only_start_nodes = self.only_start_nodes

        user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        only_active = self.only_active

        obj_id = self.obj_id

        enter_date_iso = self.enter_date_iso

        exit_date_iso = self.exit_date_iso

        node_type = self.node_type

        flow_name = self.flow_name

        wf_type_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wf_type_z, Unset):
            wf_type_z = self.wf_type_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if ci is not UNSET:
            field_dict["ci"] = ci
        if only_start_nodes is not UNSET:
            field_dict["onlyStartNodes"] = only_start_nodes
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if only_active is not UNSET:
            field_dict["onlyActive"] = only_active
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if enter_date_iso is not UNSET:
            field_dict["enterDateIso"] = enter_date_iso
        if exit_date_iso is not UNSET:
            field_dict["exitDateIso"] = exit_date_iso
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if wf_type_z is not UNSET:
            field_dict["wfTypeZ"] = wf_type_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.wf_type_z import WFTypeZ

        d = src_dict.copy()
        node_name = d.pop("nodeName", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        only_start_nodes = d.pop("onlyStartNodes", UNSET)

        user_ids = cast(List[str], d.pop("userIds", UNSET))

        only_active = d.pop("onlyActive", UNSET)

        obj_id = d.pop("objId", UNSET)

        enter_date_iso = d.pop("enterDateIso", UNSET)

        exit_date_iso = d.pop("exitDateIso", UNSET)

        node_type = d.pop("nodeType", UNSET)

        flow_name = d.pop("flowName", UNSET)

        _wf_type_z = d.pop("wfTypeZ", UNSET)
        wf_type_z: Union[Unset, WFTypeZ]
        if isinstance(_wf_type_z, Unset):
            wf_type_z = UNSET
        else:
            wf_type_z = WFTypeZ.from_dict(_wf_type_z)

        b_request_ix_service_port_if_collect_work_flow_nodes = cls(
            node_name=node_name,
            ci=ci,
            only_start_nodes=only_start_nodes,
            user_ids=user_ids,
            only_active=only_active,
            obj_id=obj_id,
            enter_date_iso=enter_date_iso,
            exit_date_iso=exit_date_iso,
            node_type=node_type,
            flow_name=flow_name,
            wf_type_z=wf_type_z,
        )

        b_request_ix_service_port_if_collect_work_flow_nodes.additional_properties = d
        return b_request_ix_service_port_if_collect_work_flow_nodes

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
