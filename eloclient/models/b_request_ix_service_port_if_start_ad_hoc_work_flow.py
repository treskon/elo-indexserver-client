from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFStartAdHocWorkFlow")


@_attrs_define
class BRequestIXServicePortIFStartAdHocWorkFlow:
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
        name (Union[Unset, str]):
        obj_id (Union[Unset, str]):
        arr_user_ids (Union[Unset, List[str]]):
        node_name (Union[Unset, str]):
        for_validation (Union[Unset, bool]):
        serial_flow (Union[Unset, bool]):
        cancel_user_id (Union[Unset, str]):
        cancel_message (Union[Unset, str]):
        finished_user_id (Union[Unset, str]):
        finished_message (Union[Unset, str]):
        finished_script (Union[Unset, str]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    arr_user_ids: Union[Unset, List[str]] = UNSET
    node_name: Union[Unset, str] = UNSET
    for_validation: Union[Unset, bool] = UNSET
    serial_flow: Union[Unset, bool] = UNSET
    cancel_user_id: Union[Unset, str] = UNSET
    cancel_message: Union[Unset, str] = UNSET
    finished_user_id: Union[Unset, str] = UNSET
    finished_message: Union[Unset, str] = UNSET
    finished_script: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        name = self.name
        obj_id = self.obj_id
        arr_user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.arr_user_ids, Unset):
            arr_user_ids = self.arr_user_ids

        node_name = self.node_name
        for_validation = self.for_validation
        serial_flow = self.serial_flow
        cancel_user_id = self.cancel_user_id
        cancel_message = self.cancel_message
        finished_user_id = self.finished_user_id
        finished_message = self.finished_message
        finished_script = self.finished_script

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if arr_user_ids is not UNSET:
            field_dict["arrUserIds"] = arr_user_ids
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if for_validation is not UNSET:
            field_dict["forValidation"] = for_validation
        if serial_flow is not UNSET:
            field_dict["serialFlow"] = serial_flow
        if cancel_user_id is not UNSET:
            field_dict["cancelUserId"] = cancel_user_id
        if cancel_message is not UNSET:
            field_dict["cancelMessage"] = cancel_message
        if finished_user_id is not UNSET:
            field_dict["finishedUserId"] = finished_user_id
        if finished_message is not UNSET:
            field_dict["finishedMessage"] = finished_message
        if finished_script is not UNSET:
            field_dict["finishedScript"] = finished_script

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

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        arr_user_ids = cast(List[str], d.pop("arrUserIds", UNSET))

        node_name = d.pop("nodeName", UNSET)

        for_validation = d.pop("forValidation", UNSET)

        serial_flow = d.pop("serialFlow", UNSET)

        cancel_user_id = d.pop("cancelUserId", UNSET)

        cancel_message = d.pop("cancelMessage", UNSET)

        finished_user_id = d.pop("finishedUserId", UNSET)

        finished_message = d.pop("finishedMessage", UNSET)

        finished_script = d.pop("finishedScript", UNSET)

        b_request_ix_service_port_if_start_ad_hoc_work_flow = cls(
            ci=ci,
            name=name,
            obj_id=obj_id,
            arr_user_ids=arr_user_ids,
            node_name=node_name,
            for_validation=for_validation,
            serial_flow=serial_flow,
            cancel_user_id=cancel_user_id,
            cancel_message=cancel_message,
            finished_user_id=finished_user_id,
            finished_message=finished_message,
            finished_script=finished_script,
        )

        b_request_ix_service_port_if_start_ad_hoc_work_flow.additional_properties = d
        return b_request_ix_service_port_if_start_ad_hoc_work_flow

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
