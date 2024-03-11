from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.substitution import Substitution
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="LoginResult")


@_attrs_define
class LoginResult:
    """<p>
    Object returned when logging in to the IX. This class contains the information required after the login has been
     carried out.
     </p>

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            client_info (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
                Each Indexserver interface function, except the
                 login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            ticket_lifetime (Union[Unset, int]): <p>
                Contains the lifetime of the ticket in seconds. The connection is terminated once this lifetime has expired.
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
            active_substitutions (Union[Unset, List['Substitution']]):
    """

    client_info: Union[Unset, "ClientInfo"] = UNSET
    ticket_lifetime: Union[Unset, int] = UNSET
    user: Union[Unset, "UserInfo"] = UNSET
    active_substitutions: Union[Unset, List["Substitution"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_info, Unset):
            client_info = self.client_info.to_dict()

        ticket_lifetime = self.ticket_lifetime
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        active_substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.active_substitutions, Unset):
            active_substitutions = []
            for componentsschemas_list_of_substitution_item_data in self.active_substitutions:
                componentsschemas_list_of_substitution_item = componentsschemas_list_of_substitution_item_data.to_dict()

                active_substitutions.append(componentsschemas_list_of_substitution_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_info is not UNSET:
            field_dict["clientInfo"] = client_info
        if ticket_lifetime is not UNSET:
            field_dict["ticketLifetime"] = ticket_lifetime
        if user is not UNSET:
            field_dict["user"] = user
        if active_substitutions is not UNSET:
            field_dict["activeSubstitutions"] = active_substitutions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.substitution import Substitution
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _client_info = d.pop("clientInfo", UNSET)
        client_info: Union[Unset, ClientInfo]
        if isinstance(_client_info, Unset):
            client_info = UNSET
        else:
            client_info = ClientInfo.from_dict(_client_info)

        ticket_lifetime = d.pop("ticketLifetime", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserInfo]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserInfo.from_dict(_user)

        active_substitutions = []
        _active_substitutions = d.pop("activeSubstitutions", UNSET)
        for componentsschemas_list_of_substitution_item_data in _active_substitutions or []:
            componentsschemas_list_of_substitution_item = Substitution.from_dict(
                componentsschemas_list_of_substitution_item_data
            )

            active_substitutions.append(componentsschemas_list_of_substitution_item)

        login_result = cls(
            client_info=client_info,
            ticket_lifetime=ticket_lifetime,
            user=user,
            active_substitutions=active_substitutions,
        )

        login_result.additional_properties = d
        return login_result

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
