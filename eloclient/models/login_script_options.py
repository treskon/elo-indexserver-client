from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginScriptOptions")


@_attrs_define
class LoginScriptOptions:
    """Options for function {@link IXServerEvents#onBeforeLogin(IXServerEventsContext, String, LoginScriptOptions)}

    Attributes:
        client_name (Union[Unset, str]): Unified Name for the client application.
            The value of this field must be one value of
             {{@link LoginScriptOptionsC}.CLIENT_NAME_*}.
        tech_user (Union[Unset, str]): User name used for authentication. This member is only valid for run-as logins.
            It contains the
             name of the technical user used for authentication.
    """

    client_name: Union[Unset, str] = UNSET
    tech_user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_name = self.client_name

        tech_user = self.tech_user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if tech_user is not UNSET:
            field_dict["techUser"] = tech_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_name = d.pop("clientName", UNSET)

        tech_user = d.pop("techUser", UNSET)

        login_script_options = cls(
            client_name=client_name,
            tech_user=tech_user,
        )

        login_script_options.additional_properties = d
        return login_script_options

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
