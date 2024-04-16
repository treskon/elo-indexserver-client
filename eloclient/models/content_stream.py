from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.b_stream_reference import BStreamReference
    from ..models.map_to_list_of_string import MapToListOfString


T = TypeVar("T", bound="ContentStream")


@_attrs_define
class ContentStream:
    """This class contains information about a document related stream.
    Such a stream might be a
     document version, attachment, preview content, fulltext content or signature.

        Attributes:
            headers (Union[Unset, MapToListOfString]):
            stream (Union[Unset, BStreamReference]):
            file_extension (Union[Unset, str]): File extension without dot.
                Either set file extension or {@link #contentType} to describe the
                 stream content.
            content_length (Union[Unset, str]): Stream content length. This member is set to the number of bytes in the
                stream.
                If the length
                 is unknown set {@link ContentStreamC#CONTENT_LENGTH_UNKNOWN}. A wrong content length can client
                 applications cause to hang.
            content_type (Union[Unset, str]): Content type (or MIME type).
                Either set content type or {@link #fileExtension} to describe the
                 stream content.
            response_code (Union[Unset, int]): HTTP response code for streams being downloaded.
                This status should be set as 200 (HTTP OK) if
                 the entire document has been processed. If {@link DocumentProcessor#process(ContentStream)}
                 receives an object that defines byte range headers in {@link ContentStream#headers}, return the
                 appropriate byte range headers and set this member as 206 (HTTP Partial Content). Byte ranges
                 are usually requested for video files. This element is ignored for streams being uploaded.
    """

    headers: Union[Unset, "MapToListOfString"] = UNSET
    stream: Union[Unset, "BStreamReference"] = UNSET
    file_extension: Union[Unset, str] = UNSET
    content_length: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    response_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.to_dict()

        file_extension = self.file_extension

        content_length = self.content_length

        content_type = self.content_type

        response_code = self.response_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if stream is not UNSET:
            field_dict["stream"] = stream
        if file_extension is not UNSET:
            field_dict["fileExtension"] = file_extension
        if content_length is not UNSET:
            field_dict["contentLength"] = content_length
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if response_code is not UNSET:
            field_dict["responseCode"] = response_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.b_stream_reference import BStreamReference
        from ..models.map_to_list_of_string import MapToListOfString

        d = src_dict.copy()
        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, MapToListOfString]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = MapToListOfString.from_dict(_headers)

        _stream = d.pop("stream", UNSET)
        stream: Union[Unset, BStreamReference]
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = BStreamReference.from_dict(_stream)

        file_extension = d.pop("fileExtension", UNSET)

        content_length = d.pop("contentLength", UNSET)

        content_type = d.pop("contentType", UNSET)

        response_code = d.pop("responseCode", UNSET)

        content_stream = cls(
            headers=headers,
            stream=stream,
            file_extension=file_extension,
            content_length=content_length,
            content_type=content_type,
            response_code=response_code,
        )

        content_stream.additional_properties = d
        return content_stream

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
