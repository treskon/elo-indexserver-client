from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.map_to_string import MapToString
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="IXServerEventsContext")


@_attrs_define
class IXServerEventsContext:
    """Execution context of server events. An object of this class is passed to every server event and registered function.
    On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking, conversion of
     date values and numeric values, etc.

        Attributes:
            admin_context (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class
                is passed to every server event and registered function.
                On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
                conversion of
                 date values and numeric values, etc.
            url (Union[Unset, str]): Indexserver URL.
            ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
                Each Indexserver interface function, except the
                 login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            user (Union[Unset, UserInfo]): <p>
                Data class containing the user information data for the user logged in to the Index server. User information
                includes
                 ID, name, rights, parent, etc.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            session_options (Union[Unset, MapToString]):
            client_computer (Union[Unset, str]): Parameter clientComputer from login function.
    """

    admin_context: Union[Unset, "IXServerEventsContext"] = UNSET
    url: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    user: Union[Unset, "UserInfo"] = UNSET
    session_options: Union[Unset, "MapToString"] = UNSET
    client_computer: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin_context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.admin_context, Unset):
            admin_context = self.admin_context.to_dict()

        url = self.url
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        session_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_options, Unset):
            session_options = self.session_options.to_dict()

        client_computer = self.client_computer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_context is not UNSET:
            field_dict["ADMIN_CONTEXT"] = admin_context
        if url is not UNSET:
            field_dict["url"] = url
        if ci is not UNSET:
            field_dict["ci"] = ci
        if user is not UNSET:
            field_dict["user"] = user
        if session_options is not UNSET:
            field_dict["sessionOptions"] = session_options
        if client_computer is not UNSET:
            field_dict["clientComputer"] = client_computer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.map_to_string import MapToString
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _admin_context = d.pop("ADMIN_CONTEXT", UNSET)
        admin_context: Union[Unset, IXServerEventsContext]
        if isinstance(_admin_context, Unset):
            admin_context = UNSET
        else:
            admin_context = IXServerEventsContext.from_dict(_admin_context)

        url = d.pop("url", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserInfo]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserInfo.from_dict(_user)

        _session_options = d.pop("sessionOptions", UNSET)
        session_options: Union[Unset, MapToString]
        if isinstance(_session_options, Unset):
            session_options = UNSET
        else:
            session_options = MapToString.from_dict(_session_options)

        client_computer = d.pop("clientComputer", UNSET)

        ix_server_events_context = cls(
            admin_context=admin_context,
            url=url,
            ci=ci,
            user=user,
            session_options=session_options,
            client_computer=client_computer,
        )

        ix_server_events_context.additional_properties = d
        return ix_server_events_context

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
