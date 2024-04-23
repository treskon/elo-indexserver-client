from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFLoginEloProf")


@_attrs_define
class BRequestIXServicePortIFLoginEloProf:
    """
    Attributes:
        client_computer (Union[Unset, str]):
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
        certificate (Union[Unset, str]):
        user_id (Union[Unset, int]):
    """

    client_computer: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    certificate: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_computer = self.client_computer

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        certificate = self.certificate

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_computer is not UNSET:
            field_dict["clientComputer"] = client_computer
        if ci is not UNSET:
            field_dict["ci"] = ci
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        client_computer = d.pop("clientComputer", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        certificate = d.pop("certificate", UNSET)

        user_id = d.pop("userId", UNSET)

        b_request_ix_service_port_if_login_elo_prof = cls(
            client_computer=client_computer,
            ci=ci,
            certificate=certificate,
            user_id=user_id,
        )

        b_request_ix_service_port_if_login_elo_prof.additional_properties = d
        return b_request_ix_service_port_if_login_elo_prof

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
