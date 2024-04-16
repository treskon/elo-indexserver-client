from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptInfoC")


@_attrs_define
class CryptInfoC:
    """
    Attributes:
        max_length_encryptionset_name (Union[Unset, int]): Maximum length of encryption set name.
        encryption_version_aes_v1 (Union[Unset, str]): Denotes the current internal version of encryption method used
            for file encryption.
        delete_system_part (Union[Unset, str]): Marker for the action "delete the system part from an encryption set".
            This is used within the
             field {@link CryptInfo#systemPwd} to indicate the above desired action.
    """

    max_length_encryptionset_name: Union[Unset, int] = UNSET
    encryption_version_aes_v1: Union[Unset, str] = UNSET
    delete_system_part: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_length_encryptionset_name = self.max_length_encryptionset_name

        encryption_version_aes_v1 = self.encryption_version_aes_v1

        delete_system_part = self.delete_system_part

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_length_encryptionset_name is not UNSET:
            field_dict["MAX_LENGTH_ENCRYPTIONSET_NAME"] = max_length_encryptionset_name
        if encryption_version_aes_v1 is not UNSET:
            field_dict["ENCRYPTION_VERSION_AES_V1"] = encryption_version_aes_v1
        if delete_system_part is not UNSET:
            field_dict["DELETE_SYSTEM_PART"] = delete_system_part

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_length_encryptionset_name = d.pop("MAX_LENGTH_ENCRYPTIONSET_NAME", UNSET)

        encryption_version_aes_v1 = d.pop("ENCRYPTION_VERSION_AES_V1", UNSET)

        delete_system_part = d.pop("DELETE_SYSTEM_PART", UNSET)

        crypt_info_c = cls(
            max_length_encryptionset_name=max_length_encryptionset_name,
            encryption_version_aes_v1=encryption_version_aes_v1,
            delete_system_part=delete_system_part,
        )

        crypt_info_c.additional_properties = d
        return crypt_info_c

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
