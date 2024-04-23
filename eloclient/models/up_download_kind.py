from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpDownloadKind")


@_attrs_define
class UpDownloadKind:
    """This enum defines constants to distinguish between different kinds of file data assigned to a
    document.

        Attributes:
            attachment (Union[Unset, UpDownloadKind]): This enum defines constants to distinguish between different kinds of
                file data assigned to a
                document.
            fulltext (Union[Unset, UpDownloadKind]): This enum defines constants to distinguish between different kinds of
                file data assigned to a
                document.
            version (Union[Unset, UpDownloadKind]): This enum defines constants to distinguish between different kinds of
                file data assigned to a
                document.
            preview (Union[Unset, UpDownloadKind]): This enum defines constants to distinguish between different kinds of
                file data assigned to a
                document.
            signature (Union[Unset, UpDownloadKind]): This enum defines constants to distinguish between different kinds of
                file data assigned to a
                document.
    """

    attachment: Union[Unset, "UpDownloadKind"] = UNSET
    fulltext: Union[Unset, "UpDownloadKind"] = UNSET
    version: Union[Unset, "UpDownloadKind"] = UNSET
    preview: Union[Unset, "UpDownloadKind"] = UNSET
    signature: Union[Unset, "UpDownloadKind"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        fulltext: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulltext, Unset):
            fulltext = self.fulltext.to_dict()

        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        signature: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment is not UNSET:
            field_dict["ATTACHMENT"] = attachment
        if fulltext is not UNSET:
            field_dict["FULLTEXT"] = fulltext
        if version is not UNSET:
            field_dict["VERSION"] = version
        if preview is not UNSET:
            field_dict["PREVIEW"] = preview
        if signature is not UNSET:
            field_dict["SIGNATURE"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _attachment = d.pop("ATTACHMENT", UNSET)
        attachment: Union[Unset, UpDownloadKind]
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = UpDownloadKind.from_dict(_attachment)

        _fulltext = d.pop("FULLTEXT", UNSET)
        fulltext: Union[Unset, UpDownloadKind]
        if isinstance(_fulltext, Unset):
            fulltext = UNSET
        else:
            fulltext = UpDownloadKind.from_dict(_fulltext)

        _version = d.pop("VERSION", UNSET)
        version: Union[Unset, UpDownloadKind]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = UpDownloadKind.from_dict(_version)

        _preview = d.pop("PREVIEW", UNSET)
        preview: Union[Unset, UpDownloadKind]
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = UpDownloadKind.from_dict(_preview)

        _signature = d.pop("SIGNATURE", UNSET)
        signature: Union[Unset, UpDownloadKind]
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = UpDownloadKind.from_dict(_signature)

        up_download_kind = cls(
            attachment=attachment,
            fulltext=fulltext,
            version=version,
            preview=preview,
            signature=signature,
        )

        up_download_kind.additional_properties = d
        return up_download_kind

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
