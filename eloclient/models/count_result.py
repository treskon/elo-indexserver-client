from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountResult")


@_attrs_define
class CountResult:
    """Class for the results of one count process.

    Attributes:
        doc_bytes_count (Union[Unset, str]): count of the bytes of the current document version
        other_att_vers_bytes_count (Union[Unset, str]): count of the bytes of other attachment versions
        doc_attach_count (Union[Unset, int]): count of the found document attachments
        other_doc_vers_bytes_count (Union[Unset, str]): count of the bytes of other document versions
        doc_versions_count (Union[Unset, int]): count of the documents in the version history
        other_attach_versions_count (Union[Unset, int]): count of the other attachment versions
        att_bytes_count (Union[Unset, str]): count of the bytes of the current attachment version
        doc_count (Union[Unset, int]): count of the found documents
        struct_count (Union[Unset, int]): count of the found structures
    """

    doc_bytes_count: Union[Unset, str] = UNSET
    other_att_vers_bytes_count: Union[Unset, str] = UNSET
    doc_attach_count: Union[Unset, int] = UNSET
    other_doc_vers_bytes_count: Union[Unset, str] = UNSET
    doc_versions_count: Union[Unset, int] = UNSET
    other_attach_versions_count: Union[Unset, int] = UNSET
    att_bytes_count: Union[Unset, str] = UNSET
    doc_count: Union[Unset, int] = UNSET
    struct_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_bytes_count = self.doc_bytes_count

        other_att_vers_bytes_count = self.other_att_vers_bytes_count

        doc_attach_count = self.doc_attach_count

        other_doc_vers_bytes_count = self.other_doc_vers_bytes_count

        doc_versions_count = self.doc_versions_count

        other_attach_versions_count = self.other_attach_versions_count

        att_bytes_count = self.att_bytes_count

        doc_count = self.doc_count

        struct_count = self.struct_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_bytes_count is not UNSET:
            field_dict["docBytesCount"] = doc_bytes_count
        if other_att_vers_bytes_count is not UNSET:
            field_dict["otherAttVersBytesCount"] = other_att_vers_bytes_count
        if doc_attach_count is not UNSET:
            field_dict["docAttachCount"] = doc_attach_count
        if other_doc_vers_bytes_count is not UNSET:
            field_dict["otherDocVersBytesCount"] = other_doc_vers_bytes_count
        if doc_versions_count is not UNSET:
            field_dict["docVersionsCount"] = doc_versions_count
        if other_attach_versions_count is not UNSET:
            field_dict["otherAttachVersionsCount"] = other_attach_versions_count
        if att_bytes_count is not UNSET:
            field_dict["attBytesCount"] = att_bytes_count
        if doc_count is not UNSET:
            field_dict["docCount"] = doc_count
        if struct_count is not UNSET:
            field_dict["structCount"] = struct_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_bytes_count = d.pop("docBytesCount", UNSET)

        other_att_vers_bytes_count = d.pop("otherAttVersBytesCount", UNSET)

        doc_attach_count = d.pop("docAttachCount", UNSET)

        other_doc_vers_bytes_count = d.pop("otherDocVersBytesCount", UNSET)

        doc_versions_count = d.pop("docVersionsCount", UNSET)

        other_attach_versions_count = d.pop("otherAttachVersionsCount", UNSET)

        att_bytes_count = d.pop("attBytesCount", UNSET)

        doc_count = d.pop("docCount", UNSET)

        struct_count = d.pop("structCount", UNSET)

        count_result = cls(
            doc_bytes_count=doc_bytes_count,
            other_att_vers_bytes_count=other_att_vers_bytes_count,
            doc_attach_count=doc_attach_count,
            other_doc_vers_bytes_count=other_doc_vers_bytes_count,
            doc_versions_count=doc_versions_count,
            other_attach_versions_count=other_attach_versions_count,
            att_bytes_count=att_bytes_count,
            doc_count=doc_count,
            struct_count=struct_count,
        )

        count_result.additional_properties = d
        return count_result

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
