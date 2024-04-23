from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.notify_server_info import NotifyServerInfo


T = TypeVar("T", bound="BRequestIXServicePortIFNotifyServer")


@_attrs_define
class BRequestIXServicePortIFNotifyServer:
    """
    Attributes:
        msg (Union[Unset, NotifyServerInfo]): This class is used in IXServicePortIF.
            notifyServer to describe which operation(s) has (have) been
             processed by the client application.
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
    """

    msg: Union[Unset, "NotifyServerInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        msg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.msg, Unset):
            msg = self.msg.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if msg is not UNSET:
            field_dict["msg"] = msg
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.notify_server_info import NotifyServerInfo

        d = src_dict.copy()
        _msg = d.pop("msg", UNSET)
        msg: Union[Unset, NotifyServerInfo]
        if isinstance(_msg, Unset):
            msg = UNSET
        else:
            msg = NotifyServerInfo.from_dict(_msg)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_notify_server = cls(
            msg=msg,
            ci=ci,
        )

        b_request_ix_service_port_if_notify_server.additional_properties = d
        return b_request_ix_service_port_if_notify_server

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
