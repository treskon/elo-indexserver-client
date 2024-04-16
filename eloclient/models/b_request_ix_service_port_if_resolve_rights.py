from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.resolve_rights_info import ResolveRightsInfo
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="BRequestIXServicePortIFResolveRights")


@_attrs_define
class BRequestIXServicePortIFResolveRights:
    """
    Attributes:
        ui (Union[Unset, UserInfo]): <p>
            Data class containing the user information data for the user logged in to the Index server. User
             information includes ID, name, rights, parent, etc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
        info (Union[Unset, ResolveRightsInfo]): Parameter Class for
            {@link IXServicePortIF#resolveRights(ClientInfo, UserInfo, ResolveRightsInfo)} .
    """

    ui: Union[Unset, "UserInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    info: Union[Unset, "ResolveRightsInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ui: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ui, Unset):
            ui = self.ui.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ui is not UNSET:
            field_dict["ui"] = ui
        if ci is not UNSET:
            field_dict["ci"] = ci
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.resolve_rights_info import ResolveRightsInfo
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _ui = d.pop("ui", UNSET)
        ui: Union[Unset, UserInfo]
        if isinstance(_ui, Unset):
            ui = UNSET
        else:
            ui = UserInfo.from_dict(_ui)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _info = d.pop("info", UNSET)
        info: Union[Unset, ResolveRightsInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = ResolveRightsInfo.from_dict(_info)

        b_request_ix_service_port_if_resolve_rights = cls(
            ui=ui,
            ci=ci,
            info=info,
        )

        b_request_ix_service_port_if_resolve_rights.additional_properties = d
        return b_request_ix_service_port_if_resolve_rights

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
