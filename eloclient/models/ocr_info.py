from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocr_info_query_languages import OcrInfoQueryLanguages
    from ..models.ocr_info_recognize_file import OcrInfoRecognizeFile


T = TypeVar("T", bound="OcrInfo")


@_attrs_define
class OcrInfo:
    """This class defines the properties of an OCR request.

    Attributes:
        bus_id (Union[Unset, str]): Return OCR result over this event bus.
            If the OCR request should be performed asynchronously,
             this value must contain the event bus ID on which the result event is sent. If this value is 0,
             the OCR request is performed synchronously.
        event_id (Union[Unset, str]): OCR result should be sent in an event with this event ID.
            This member helps to map the OCR
             request to the OCR result. Optional.
        messages_language (Union[Unset, int]): Language of error messages produced by the OCR engine. One of the
            OcrInfoC.
            MESSAGES_LANGUAGE_
             constants. Optional.
        recognize_file (Union[Unset, OcrInfoRecognizeFile]): This class describes an OCR analysis request.
        query_languages (Union[Unset, OcrInfoQueryLanguages]): This class describes a request for querying the supported
            languages of the OCR.
    """

    bus_id: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    messages_language: Union[Unset, int] = UNSET
    recognize_file: Union[Unset, "OcrInfoRecognizeFile"] = UNSET
    query_languages: Union[Unset, "OcrInfoQueryLanguages"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bus_id = self.bus_id

        event_id = self.event_id

        messages_language = self.messages_language

        recognize_file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recognize_file, Unset):
            recognize_file = self.recognize_file.to_dict()

        query_languages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_languages, Unset):
            query_languages = self.query_languages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bus_id is not UNSET:
            field_dict["busId"] = bus_id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if messages_language is not UNSET:
            field_dict["messagesLanguage"] = messages_language
        if recognize_file is not UNSET:
            field_dict["recognizeFile"] = recognize_file
        if query_languages is not UNSET:
            field_dict["queryLanguages"] = query_languages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ocr_info_query_languages import OcrInfoQueryLanguages
        from ..models.ocr_info_recognize_file import OcrInfoRecognizeFile

        d = src_dict.copy()
        bus_id = d.pop("busId", UNSET)

        event_id = d.pop("eventId", UNSET)

        messages_language = d.pop("messagesLanguage", UNSET)

        _recognize_file = d.pop("recognizeFile", UNSET)
        recognize_file: Union[Unset, OcrInfoRecognizeFile]
        if isinstance(_recognize_file, Unset):
            recognize_file = UNSET
        else:
            recognize_file = OcrInfoRecognizeFile.from_dict(_recognize_file)

        _query_languages = d.pop("queryLanguages", UNSET)
        query_languages: Union[Unset, OcrInfoQueryLanguages]
        if isinstance(_query_languages, Unset):
            query_languages = UNSET
        else:
            query_languages = OcrInfoQueryLanguages.from_dict(_query_languages)

        ocr_info = cls(
            bus_id=bus_id,
            event_id=event_id,
            messages_language=messages_language,
            recognize_file=recognize_file,
            query_languages=query_languages,
        )

        ocr_info.additional_properties = d
        return ocr_info

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
