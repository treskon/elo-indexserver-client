from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.b_stream_reference import BStreamReference


T = TypeVar("T", bound="FileData")


@_attrs_define
class FileData:
    """Class for the data contained in a file.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            data (Union[Unset, str]): File data as byte array.
            stream (Union[Unset, BStreamReference]):
            content_type (Union[Unset, str]): MIME-Type/document extension, for example text/xml or image/tiff or txt.
    """

    data: Union[Unset, str] = UNSET
    stream: Union[Unset, "BStreamReference"] = UNSET
    content_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data

        stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.to_dict()

        content_type = self.content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if stream is not UNSET:
            field_dict["stream"] = stream
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.b_stream_reference import BStreamReference

        d = src_dict.copy()
        data = d.pop("data", UNSET)

        _stream = d.pop("stream", UNSET)
        stream: Union[Unset, BStreamReference]
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = BStreamReference.from_dict(_stream)

        content_type = d.pop("contentType", UNSET)

        file_data = cls(
            data=data,
            stream=stream,
            content_type=content_type,
        )

        file_data.additional_properties = d
        return file_data

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
