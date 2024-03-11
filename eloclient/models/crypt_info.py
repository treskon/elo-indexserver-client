from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptInfo")


@_attrs_define
class CryptInfo:
    """This class defines an encryption set.

    Attributes:
        id (Union[Unset, int]): Numerical ID of the encryption information. The first ID is 1.
        name (Union[Unset, str]): Name.
        pwd (Union[Unset, str]): External password used for encrypting documents.
            It is empty if this object was returned by
             <code>checkoutCryptInfos</code>.
        key_info (Union[Unset, str]): Only for TwoFish-Encyption! Key material.
            Contains the external and internal password in serialized and encrypted
             format. Only for internal use. This member is ignored in <code>checkinCryptInfos</code>.
        system_pwd (Union[Unset, str]):
        version (Union[Unset, str]):
        aes_user_key_info (Union[Unset, str]):
        aes_system_key_info (Union[Unset, str]):
        aes_user_init_vector (Union[Unset, str]):
        aes_system_init_vector (Union[Unset, str]):
        current_pwd (Union[Unset, str]):
        current_system_pwd (Union[Unset, str]):
        system_user_id (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    pwd: Union[Unset, str] = UNSET
    key_info: Union[Unset, str] = UNSET
    system_pwd: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    aes_user_key_info: Union[Unset, str] = UNSET
    aes_system_key_info: Union[Unset, str] = UNSET
    aes_user_init_vector: Union[Unset, str] = UNSET
    aes_system_init_vector: Union[Unset, str] = UNSET
    current_pwd: Union[Unset, str] = UNSET
    current_system_pwd: Union[Unset, str] = UNSET
    system_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        pwd = self.pwd
        key_info = self.key_info
        system_pwd = self.system_pwd
        version = self.version
        aes_user_key_info = self.aes_user_key_info
        aes_system_key_info = self.aes_system_key_info
        aes_user_init_vector = self.aes_user_init_vector
        aes_system_init_vector = self.aes_system_init_vector
        current_pwd = self.current_pwd
        current_system_pwd = self.current_system_pwd
        system_user_id = self.system_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if pwd is not UNSET:
            field_dict["pwd"] = pwd
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if system_pwd is not UNSET:
            field_dict["systemPwd"] = system_pwd
        if version is not UNSET:
            field_dict["version"] = version
        if aes_user_key_info is not UNSET:
            field_dict["aesUserKeyInfo"] = aes_user_key_info
        if aes_system_key_info is not UNSET:
            field_dict["aesSystemKeyInfo"] = aes_system_key_info
        if aes_user_init_vector is not UNSET:
            field_dict["aesUserInitVector"] = aes_user_init_vector
        if aes_system_init_vector is not UNSET:
            field_dict["aesSystemInitVector"] = aes_system_init_vector
        if current_pwd is not UNSET:
            field_dict["currentPwd"] = current_pwd
        if current_system_pwd is not UNSET:
            field_dict["currentSystemPwd"] = current_system_pwd
        if system_user_id is not UNSET:
            field_dict["systemUserId"] = system_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        pwd = d.pop("pwd", UNSET)

        key_info = d.pop("keyInfo", UNSET)

        system_pwd = d.pop("systemPwd", UNSET)

        version = d.pop("version", UNSET)

        aes_user_key_info = d.pop("aesUserKeyInfo", UNSET)

        aes_system_key_info = d.pop("aesSystemKeyInfo", UNSET)

        aes_user_init_vector = d.pop("aesUserInitVector", UNSET)

        aes_system_init_vector = d.pop("aesSystemInitVector", UNSET)

        current_pwd = d.pop("currentPwd", UNSET)

        current_system_pwd = d.pop("currentSystemPwd", UNSET)

        system_user_id = d.pop("systemUserId", UNSET)

        crypt_info = cls(
            id=id,
            name=name,
            pwd=pwd,
            key_info=key_info,
            system_pwd=system_pwd,
            version=version,
            aes_user_key_info=aes_user_key_info,
            aes_system_key_info=aes_system_key_info,
            aes_user_init_vector=aes_user_init_vector,
            aes_system_init_vector=aes_system_init_vector,
            current_pwd=current_pwd,
            current_system_pwd=current_system_pwd,
            system_user_id=system_user_id,
        )

        crypt_info.additional_properties = d
        return crypt_info

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
