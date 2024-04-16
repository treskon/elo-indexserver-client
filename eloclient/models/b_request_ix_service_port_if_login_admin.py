from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFLoginAdmin")


@_attrs_define
class BRequestIXServicePortIFLoginAdmin:
    """
    Attributes:
        client_computer (Union[Unset, str]):
        report_as_user (Union[Unset, str]):
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
        user_pwd (Union[Unset, str]):
        user_name (Union[Unset, str]):
    """

    client_computer: Union[Unset, str] = UNSET
    report_as_user: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    user_pwd: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_computer = self.client_computer

        report_as_user = self.report_as_user

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        user_pwd = self.user_pwd

        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_computer is not UNSET:
            field_dict["clientComputer"] = client_computer
        if report_as_user is not UNSET:
            field_dict["reportAsUser"] = report_as_user
        if ci is not UNSET:
            field_dict["ci"] = ci
        if user_pwd is not UNSET:
            field_dict["userPwd"] = user_pwd
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        client_computer = d.pop("clientComputer", UNSET)

        report_as_user = d.pop("reportAsUser", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        user_pwd = d.pop("userPwd", UNSET)

        user_name = d.pop("userName", UNSET)

        b_request_ix_service_port_if_login_admin = cls(
            client_computer=client_computer,
            report_as_user=report_as_user,
            ci=ci,
            user_pwd=user_pwd,
            user_name=user_name,
        )

        b_request_ix_service_port_if_login_admin.additional_properties = d
        return b_request_ix_service_port_if_login_admin

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
