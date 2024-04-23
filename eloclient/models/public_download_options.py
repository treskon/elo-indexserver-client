from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicDownloadOptions")


@_attrs_define
class PublicDownloadOptions:
    """This class contains several options that are used to get the public downloads.
    <p>
     Copyright: Copyright (c) 2014
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            content_disposition_attachment (Union[Unset, bool]): If true, the document is downloaded as an attachment.
                Otherwise it content is shown in-line in
                 the browser.
            doc_id (Union[Unset, str]): The doc id.
            file_name_from_sord_name (Union[Unset, bool]): If true, the short description of the sord is used as file name
                in the download URL.
                Otherwise
                 the original file name is used.
            obj_id (Union[Unset, str]): The obj id.
            expiration (Union[Unset, str]): The expired time.
            remaining (Union[Unset, int]): The remaining download.
            download_ids (Union[Unset, List[str]]):
    """

    content_disposition_attachment: Union[Unset, bool] = UNSET
    doc_id: Union[Unset, str] = UNSET
    file_name_from_sord_name: Union[Unset, bool] = UNSET
    obj_id: Union[Unset, str] = UNSET
    expiration: Union[Unset, str] = UNSET
    remaining: Union[Unset, int] = UNSET
    download_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_disposition_attachment = self.content_disposition_attachment

        doc_id = self.doc_id

        file_name_from_sord_name = self.file_name_from_sord_name

        obj_id = self.obj_id

        expiration = self.expiration

        remaining = self.remaining

        download_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.download_ids, Unset):
            download_ids = self.download_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_disposition_attachment is not UNSET:
            field_dict["contentDispositionAttachment"] = content_disposition_attachment
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if file_name_from_sord_name is not UNSET:
            field_dict["fileNameFromSordName"] = file_name_from_sord_name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if download_ids is not UNSET:
            field_dict["downloadIds"] = download_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_disposition_attachment = d.pop("contentDispositionAttachment", UNSET)

        doc_id = d.pop("docId", UNSET)

        file_name_from_sord_name = d.pop("fileNameFromSordName", UNSET)

        obj_id = d.pop("objId", UNSET)

        expiration = d.pop("expiration", UNSET)

        remaining = d.pop("remaining", UNSET)

        download_ids = cast(List[str], d.pop("downloadIds", UNSET))

        public_download_options = cls(
            content_disposition_attachment=content_disposition_attachment,
            doc_id=doc_id,
            file_name_from_sord_name=file_name_from_sord_name,
            obj_id=obj_id,
            expiration=expiration,
            remaining=remaining,
            download_ids=download_ids,
        )

        public_download_options.additional_properties = d
        return public_download_options

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
