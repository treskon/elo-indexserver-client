from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """This class represents a LDAP server.

    Attributes:
        last_exception (Union[Unset, str]): An exception message if connection to {@link #ldapUrl} failed.
        ldap_url (Union[Unset, str]): URL to access the LDAP directory.
        last_login_duration_millis (Union[Unset, str]): Duration of last login. Read only.
        priority (Union[Unset, float]): Priority for using this URL compared to others. Higher value means more
            preferred.
    """

    last_exception: Union[Unset, str] = UNSET
    ldap_url: Union[Unset, str] = UNSET
    last_login_duration_millis: Union[Unset, str] = UNSET
    priority: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_exception = self.last_exception

        ldap_url = self.ldap_url

        last_login_duration_millis = self.last_login_duration_millis

        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_exception is not UNSET:
            field_dict["lastException"] = last_exception
        if ldap_url is not UNSET:
            field_dict["ldapUrl"] = ldap_url
        if last_login_duration_millis is not UNSET:
            field_dict["lastLoginDurationMillis"] = last_login_duration_millis
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_exception = d.pop("lastException", UNSET)

        ldap_url = d.pop("ldapUrl", UNSET)

        last_login_duration_millis = d.pop("lastLoginDurationMillis", UNSET)

        priority = d.pop("priority", UNSET)

        server = cls(
            last_exception=last_exception,
            ldap_url=ldap_url,
            last_login_duration_millis=last_login_duration_millis,
            priority=priority,
        )

        server.additional_properties = d
        return server

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
