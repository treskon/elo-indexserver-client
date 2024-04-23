from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocVersionC")


@_attrs_define
class DocVersionC:
    """
    Attributes:
        ln_comment (Union[Unset, int]): Length of version comment.
        upload_result_error (Union[Unset, str]): This value should be set in DocVersion.uploadResult, if preview
            creation fails.
        url_param_last_update (Union[Unset, str]): URL parameter last write date. Used to set the last write time of the
            file.
            ISO date in UTC
             timezone. Example: String writeUrl = docVersion.url + "&amp;" + URL_PARAM_LAST_UPDATE + "=" +
             20010203040506;
        type_attachment (Union[Unset, int]):
        url_param_create_date (Union[Unset, str]): URL parameter create date. Used to set the create date of the file.
            ISO date in UTC timezone.
            Example: String writeUrl = docVersion.url + "&amp;" + URL_PARAM_CREATE_DATE + "=" +
             20010203040506;
        url_param_last_access (Union[Unset, str]): URL parameter last access date. Used to set the last access time of
            the file.
            ISO date in UTC
             timezone. Example: String writeUrl = docVersion.url + "&amp;" + URL_PARAM_LAST_ACCESS + "=" +
             20010203040506;
        url_param_offset (Union[Unset, str]): URL parameter offset. Used to read a file at a particular offset.
            Do not position offset after
             the length of the file. Example: String readUrl = docVersion.url + "&amp;" + URL_PARAM_OFFSET +
             "=" + 123;
        ln_version (Union[Unset, int]): Length of version number (like 1.0).
        ln_ext (Union[Unset, int]): Length of file extension.
        url_param_length (Union[Unset, str]): URL parameter length. Used to read length bytes from a file.
            Do not read more bytes than the
             legnth of the file. Example: String readUrl = docVersion.url + "&amp;" + URL_PARAM_LENGTH + "="
             + 123;
        flag_milestone (Union[Unset, int]): Document versions marked with this flag cannot be deleted.
        type_docversion (Union[Unset, int]):
    """

    ln_comment: Union[Unset, int] = UNSET
    upload_result_error: Union[Unset, str] = UNSET
    url_param_last_update: Union[Unset, str] = UNSET
    type_attachment: Union[Unset, int] = UNSET
    url_param_create_date: Union[Unset, str] = UNSET
    url_param_last_access: Union[Unset, str] = UNSET
    url_param_offset: Union[Unset, str] = UNSET
    ln_version: Union[Unset, int] = UNSET
    ln_ext: Union[Unset, int] = UNSET
    url_param_length: Union[Unset, str] = UNSET
    flag_milestone: Union[Unset, int] = UNSET
    type_docversion: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_comment = self.ln_comment

        upload_result_error = self.upload_result_error

        url_param_last_update = self.url_param_last_update

        type_attachment = self.type_attachment

        url_param_create_date = self.url_param_create_date

        url_param_last_access = self.url_param_last_access

        url_param_offset = self.url_param_offset

        ln_version = self.ln_version

        ln_ext = self.ln_ext

        url_param_length = self.url_param_length

        flag_milestone = self.flag_milestone

        type_docversion = self.type_docversion

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if upload_result_error is not UNSET:
            field_dict["UPLOAD_RESULT_ERROR"] = upload_result_error
        if url_param_last_update is not UNSET:
            field_dict["URL_PARAM_LAST_UPDATE"] = url_param_last_update
        if type_attachment is not UNSET:
            field_dict["TYPE_ATTACHMENT"] = type_attachment
        if url_param_create_date is not UNSET:
            field_dict["URL_PARAM_CREATE_DATE"] = url_param_create_date
        if url_param_last_access is not UNSET:
            field_dict["URL_PARAM_LAST_ACCESS"] = url_param_last_access
        if url_param_offset is not UNSET:
            field_dict["URL_PARAM_OFFSET"] = url_param_offset
        if ln_version is not UNSET:
            field_dict["lnVersion"] = ln_version
        if ln_ext is not UNSET:
            field_dict["lnExt"] = ln_ext
        if url_param_length is not UNSET:
            field_dict["URL_PARAM_LENGTH"] = url_param_length
        if flag_milestone is not UNSET:
            field_dict["FLAG_MILESTONE"] = flag_milestone
        if type_docversion is not UNSET:
            field_dict["TYPE_DOCVERSION"] = type_docversion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_comment = d.pop("lnComment", UNSET)

        upload_result_error = d.pop("UPLOAD_RESULT_ERROR", UNSET)

        url_param_last_update = d.pop("URL_PARAM_LAST_UPDATE", UNSET)

        type_attachment = d.pop("TYPE_ATTACHMENT", UNSET)

        url_param_create_date = d.pop("URL_PARAM_CREATE_DATE", UNSET)

        url_param_last_access = d.pop("URL_PARAM_LAST_ACCESS", UNSET)

        url_param_offset = d.pop("URL_PARAM_OFFSET", UNSET)

        ln_version = d.pop("lnVersion", UNSET)

        ln_ext = d.pop("lnExt", UNSET)

        url_param_length = d.pop("URL_PARAM_LENGTH", UNSET)

        flag_milestone = d.pop("FLAG_MILESTONE", UNSET)

        type_docversion = d.pop("TYPE_DOCVERSION", UNSET)

        doc_version_c = cls(
            ln_comment=ln_comment,
            upload_result_error=upload_result_error,
            url_param_last_update=url_param_last_update,
            type_attachment=type_attachment,
            url_param_create_date=url_param_create_date,
            url_param_last_access=url_param_last_access,
            url_param_offset=url_param_offset,
            ln_version=ln_version,
            ln_ext=ln_ext,
            url_param_length=url_param_length,
            flag_milestone=flag_milestone,
            type_docversion=type_docversion,
        )

        doc_version_c.additional_properties = d
        return doc_version_c

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
