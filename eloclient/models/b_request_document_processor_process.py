from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_stream import ContentStream


T = TypeVar("T", bound="BRequestDocumentProcessorProcess")


@_attrs_define
class BRequestDocumentProcessorProcess:
    """
    Attributes:
        original_stream (Union[Unset, ContentStream]): This class contains information about a document related stream.
            Such a stream might be a document version,
             attachment, preview content, fulltext content or signature.
    """

    original_stream: Union[Unset, "ContentStream"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        original_stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_stream, Unset):
            original_stream = self.original_stream.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_stream is not UNSET:
            field_dict["originalStream"] = original_stream

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_stream import ContentStream

        d = src_dict.copy()
        _original_stream = d.pop("originalStream", UNSET)
        original_stream: Union[Unset, ContentStream]
        if isinstance(_original_stream, Unset):
            original_stream = UNSET
        else:
            original_stream = ContentStream.from_dict(_original_stream)

        b_request_document_processor_process = cls(
            original_stream=original_stream,
        )

        b_request_document_processor_process.additional_properties = d
        return b_request_document_processor_process

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
