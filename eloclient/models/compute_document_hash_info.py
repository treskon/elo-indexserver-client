from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputeDocumentHashInfo")


@_attrs_define
class ComputeDocumentHashInfo:
    """This class defines the parameters for computing a document file hash by
    {@link IXServicePortIF#computeDocumentHash(ClientInfo, ComputeDocumentHashInfo)}.

        Attributes:
            doc_id (Union[Unset, int]): Document ID.
    """

    doc_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_id = self.doc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_id = d.pop("docId", UNSET)

        compute_document_hash_info = cls(
            doc_id=doc_id,
        )

        compute_document_hash_info.additional_properties = d
        return compute_document_hash_info

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
