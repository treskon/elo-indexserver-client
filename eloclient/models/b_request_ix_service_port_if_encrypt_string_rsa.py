from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFEncryptStringRsa")


@_attrs_define
class BRequestIXServicePortIFEncryptStringRsa:
    """
    Attributes:
        data (Union[Unset, str]):
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
        encrypt_not_decrypt (Union[Unset, bool]):
        key (Union[Unset, str]):
    """

    data: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    encrypt_not_decrypt: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        encrypt_not_decrypt = self.encrypt_not_decrypt

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if ci is not UNSET:
            field_dict["ci"] = ci
        if encrypt_not_decrypt is not UNSET:
            field_dict["encryptNotDecrypt"] = encrypt_not_decrypt
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        data = d.pop("data", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        encrypt_not_decrypt = d.pop("encryptNotDecrypt", UNSET)

        key = d.pop("key", UNSET)

        b_request_ix_service_port_if_encrypt_string_rsa = cls(
            data=data,
            ci=ci,
            encrypt_not_decrypt=encrypt_not_decrypt,
            key=key,
        )

        b_request_ix_service_port_if_encrypt_string_rsa.additional_properties = d
        return b_request_ix_service_port_if_encrypt_string_rsa

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
