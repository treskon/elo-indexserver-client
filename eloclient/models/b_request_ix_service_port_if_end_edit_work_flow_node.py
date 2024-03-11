from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFEndEditWorkFlowNode")


@_attrs_define
class BRequestIXServicePortIFEndEditWorkFlowNode:
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
        b_terminate (Union[Unset, bool]):
        b_cancel (Union[Unset, bool]):
        s_name (Union[Unset, str]):
        s_comment (Union[Unset, str]):
        arr_enter_nodes_ids (Union[Unset, List[int]]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    n_flow_id: Union[Unset, int] = UNSET
    n_node_id: Union[Unset, int] = UNSET
    b_terminate: Union[Unset, bool] = UNSET
    b_cancel: Union[Unset, bool] = UNSET
    s_name: Union[Unset, str] = UNSET
    s_comment: Union[Unset, str] = UNSET
    arr_enter_nodes_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        n_flow_id = self.n_flow_id
        n_node_id = self.n_node_id
        b_terminate = self.b_terminate
        b_cancel = self.b_cancel
        s_name = self.s_name
        s_comment = self.s_comment
        arr_enter_nodes_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.arr_enter_nodes_ids, Unset):
            arr_enter_nodes_ids = self.arr_enter_nodes_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if n_flow_id is not UNSET:
            field_dict["nFlowId"] = n_flow_id
        if n_node_id is not UNSET:
            field_dict["nNodeId"] = n_node_id
        if b_terminate is not UNSET:
            field_dict["bTerminate"] = b_terminate
        if b_cancel is not UNSET:
            field_dict["bCancel"] = b_cancel
        if s_name is not UNSET:
            field_dict["sName"] = s_name
        if s_comment is not UNSET:
            field_dict["sComment"] = s_comment
        if arr_enter_nodes_ids is not UNSET:
            field_dict["arrEnterNodesIds"] = arr_enter_nodes_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        n_flow_id = d.pop("nFlowId", UNSET)

        n_node_id = d.pop("nNodeId", UNSET)

        b_terminate = d.pop("bTerminate", UNSET)

        b_cancel = d.pop("bCancel", UNSET)

        s_name = d.pop("sName", UNSET)

        s_comment = d.pop("sComment", UNSET)

        arr_enter_nodes_ids = cast(List[int], d.pop("arrEnterNodesIds", UNSET))

        b_request_ix_service_port_if_end_edit_work_flow_node = cls(
            ci=ci,
            n_flow_id=n_flow_id,
            n_node_id=n_node_id,
            b_terminate=b_terminate,
            b_cancel=b_cancel,
            s_name=s_name,
            s_comment=s_comment,
            arr_enter_nodes_ids=arr_enter_nodes_ids,
        )

        b_request_ix_service_port_if_end_edit_work_flow_node.additional_properties = d
        return b_request_ix_service_port_if_end_edit_work_flow_node

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
