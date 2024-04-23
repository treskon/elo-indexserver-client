from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_access_info import AclAccessInfo
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFGetAclAccess")


@_attrs_define
class BRequestIXServicePortIFGetAclAccess:
    """
    Attributes:
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
        aai (Union[Unset, AclAccessInfo]): This class contains the option for the methode getAclAccess
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    aai: Union[Unset, "AclAccessInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        aai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aai, Unset):
            aai = self.aai.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if aai is not UNSET:
            field_dict["aai"] = aai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_access_info import AclAccessInfo
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _aai = d.pop("aai", UNSET)
        aai: Union[Unset, AclAccessInfo]
        if isinstance(_aai, Unset):
            aai = UNSET
        else:
            aai = AclAccessInfo.from_dict(_aai)

        b_request_ix_service_port_if_get_acl_access = cls(
            ci=ci,
            aai=aai,
        )

        b_request_ix_service_port_if_get_acl_access.additional_properties = d
        return b_request_ix_service_port_if_get_acl_access

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
