from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_workflow_history_params import CheckoutWorkflowHistoryParams
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutWorkflowHistory")


@_attrs_define
class BRequestIXServicePortIFCheckoutWorkflowHistory:
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
        checkout_workflow_history_params (Union[Unset, CheckoutWorkflowHistoryParams]): Parameter class for the method
            checkoutWorkflowHistory.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    checkout_workflow_history_params: Union[Unset, "CheckoutWorkflowHistoryParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        checkout_workflow_history_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_workflow_history_params, Unset):
            checkout_workflow_history_params = self.checkout_workflow_history_params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if checkout_workflow_history_params is not UNSET:
            field_dict["checkoutWorkflowHistoryParams"] = checkout_workflow_history_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_workflow_history_params import CheckoutWorkflowHistoryParams
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _checkout_workflow_history_params = d.pop("checkoutWorkflowHistoryParams", UNSET)
        checkout_workflow_history_params: Union[Unset, CheckoutWorkflowHistoryParams]
        if isinstance(_checkout_workflow_history_params, Unset):
            checkout_workflow_history_params = UNSET
        else:
            checkout_workflow_history_params = CheckoutWorkflowHistoryParams.from_dict(
                _checkout_workflow_history_params
            )

        b_request_ix_service_port_if_checkout_workflow_history = cls(
            ci=ci,
            checkout_workflow_history_params=checkout_workflow_history_params,
        )

        b_request_ix_service_port_if_checkout_workflow_history.additional_properties = d
        return b_request_ix_service_port_if_checkout_workflow_history

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
