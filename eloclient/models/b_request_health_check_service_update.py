from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.health_check_info import HealthCheckInfo


T = TypeVar("T", bound="BRequestHealthCheckServiceUpdate")


@_attrs_define
class BRequestHealthCheckServiceUpdate:
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
        hci (Union[Unset, HealthCheckInfo]): This class represents one value for health check evaluation.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    hci: Union[Unset, "HealthCheckInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        hci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hci, Unset):
            hci = self.hci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if hci is not UNSET:
            field_dict["hci"] = hci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.health_check_info import HealthCheckInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _hci = d.pop("hci", UNSET)
        hci: Union[Unset, HealthCheckInfo]
        if isinstance(_hci, Unset):
            hci = UNSET
        else:
            hci = HealthCheckInfo.from_dict(_hci)

        b_request_health_check_service_update = cls(
            ci=ci,
            hci=hci,
        )

        b_request_health_check_service_update.additional_properties = d
        return b_request_health_check_service_update

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
