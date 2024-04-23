from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.find_user_info import FindUserInfo


T = TypeVar("T", bound="BRequestIXServicePortIFFindFirstUsers")


@_attrs_define
class BRequestIXServicePortIFFindFirstUsers:
    """
    Attributes:
        find_user_info (Union[Unset, FindUserInfo]): This class describes the search criteria for {@link
            IXServicePortIF#findFirstUsers}.
            The wildcards defined by {@link SessionOptionsC#DB_WILDCARDS} can be used for {@link #name},
             {@link #desc}, {@link #property}, and {@link #ldapProperty}.

             Members {@link #name}, {@link #desc}, {@link #property}, and {@link #ldapProperty} are combined
             by OR. Other members are combinded by AND.
        max_ (Union[Unset, int]):
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

    find_user_info: Union[Unset, "FindUserInfo"] = UNSET
    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        find_user_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_user_info, Unset):
            find_user_info = self.find_user_info.to_dict()

        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if find_user_info is not UNSET:
            field_dict["findUserInfo"] = find_user_info
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.find_user_info import FindUserInfo

        d = src_dict.copy()
        _find_user_info = d.pop("findUserInfo", UNSET)
        find_user_info: Union[Unset, FindUserInfo]
        if isinstance(_find_user_info, Unset):
            find_user_info = UNSET
        else:
            find_user_info = FindUserInfo.from_dict(_find_user_info)

        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_find_first_users = cls(
            find_user_info=find_user_info,
            max_=max_,
            ci=ci,
        )

        b_request_ix_service_port_if_find_first_users.additional_properties = d
        return b_request_ix_service_port_if_find_first_users

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
