from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.health_check_value_operation import HealthCheckValueOperation


T = TypeVar("T", bound="BRequestHealthCheckServiceComputeDoubleValue")


@_attrs_define
class BRequestHealthCheckServiceComputeDoubleValue:
    """
    Attributes:
        hci_update_operation (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a
            value.
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
        hci_value_name (Union[Unset, str]):
        hci_update_value (Union[Unset, float]):
    """

    hci_update_operation: Union[Unset, "HealthCheckValueOperation"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    hci_value_name: Union[Unset, str] = UNSET
    hci_update_value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hci_update_operation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hci_update_operation, Unset):
            hci_update_operation = self.hci_update_operation.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        hci_value_name = self.hci_value_name

        hci_update_value = self.hci_update_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hci_update_operation is not UNSET:
            field_dict["hciUpdateOperation"] = hci_update_operation
        if ci is not UNSET:
            field_dict["ci"] = ci
        if hci_value_name is not UNSET:
            field_dict["hciValueName"] = hci_value_name
        if hci_update_value is not UNSET:
            field_dict["hciUpdateValue"] = hci_update_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.health_check_value_operation import HealthCheckValueOperation

        d = src_dict.copy()
        _hci_update_operation = d.pop("hciUpdateOperation", UNSET)
        hci_update_operation: Union[Unset, HealthCheckValueOperation]
        if isinstance(_hci_update_operation, Unset):
            hci_update_operation = UNSET
        else:
            hci_update_operation = HealthCheckValueOperation.from_dict(_hci_update_operation)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        hci_value_name = d.pop("hciValueName", UNSET)

        hci_update_value = d.pop("hciUpdateValue", UNSET)

        b_request_health_check_service_compute_double_value = cls(
            hci_update_operation=hci_update_operation,
            ci=ci,
            hci_value_name=hci_value_name,
            hci_update_value=hci_update_value,
        )

        b_request_health_check_service_compute_double_value.additional_properties = d
        return b_request_health_check_service_compute_double_value

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
