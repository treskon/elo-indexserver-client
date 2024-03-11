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
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        key (Union[Unset, str]):
        data (Union[Unset, str]):
        encrypt_not_decrypt (Union[Unset, bool]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    key: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    encrypt_not_decrypt: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        key = self.key
        data = self.data
        encrypt_not_decrypt = self.encrypt_not_decrypt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if key is not UNSET:
            field_dict["key"] = key
        if data is not UNSET:
            field_dict["data"] = data
        if encrypt_not_decrypt is not UNSET:
            field_dict["encryptNotDecrypt"] = encrypt_not_decrypt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        key = d.pop("key", UNSET)

        data = d.pop("data", UNSET)

        encrypt_not_decrypt = d.pop("encryptNotDecrypt", UNSET)

        b_request_ix_service_port_if_encrypt_string_rsa = cls(
            ci=ci,
            key=key,
            data=data,
            encrypt_not_decrypt=encrypt_not_decrypt,
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
