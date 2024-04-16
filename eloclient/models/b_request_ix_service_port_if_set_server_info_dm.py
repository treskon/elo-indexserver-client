from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.server_info_dm import ServerInfoDM


T = TypeVar("T", bound="BRequestIXServicePortIFSetServerInfoDM")


@_attrs_define
class BRequestIXServicePortIFSetServerInfoDM:
    """
    Attributes:
        server_info (Union[Unset, ServerInfoDM]): This class contains infomation about the filing paths of the document
            manager (DM).
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

    server_info: Union[Unset, "ServerInfoDM"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_info, Unset):
            server_info = self.server_info.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_info is not UNSET:
            field_dict["serverInfo"] = server_info
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.server_info_dm import ServerInfoDM

        d = src_dict.copy()
        _server_info = d.pop("serverInfo", UNSET)
        server_info: Union[Unset, ServerInfoDM]
        if isinstance(_server_info, Unset):
            server_info = UNSET
        else:
            server_info = ServerInfoDM.from_dict(_server_info)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_set_server_info_dm = cls(
            server_info=server_info,
            ci=ci,
        )

        b_request_ix_service_port_if_set_server_info_dm.additional_properties = d
        return b_request_ix_service_port_if_set_server_info_dm

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
