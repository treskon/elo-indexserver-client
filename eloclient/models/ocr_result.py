from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocr_result_query_languages import OcrResultQueryLanguages
    from ..models.ocr_result_recognize_file import OcrResultRecognizeFile


T = TypeVar("T", bound="OcrResult")


@_attrs_define
class OcrResult:
    """This class contains the informations about an OCR result.

    Attributes:
        exception (Union[Unset, str]): Error message. Null or empty, if no error has occurred.
            This value is used only in asynchronous
             processing in order to inform the client application, that an error has occured. In synchronous
             processing, the error is thrown as an exception.
        event_id (Union[Unset, str]): Event ID. The same value as submitted in {@link OcrInfo#eventId}.
        exception_id (Union[Unset, int]): Error id.
            0, if no error has occurred
        recognize_file (Union[Unset, OcrResultRecognizeFile]): This class contains the result of an OCR analysis.
        query_languages (Union[Unset, OcrResultQueryLanguages]): This class contains the result of a
            OcrInfoQueryLanguages request.
    """

    exception: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    exception_id: Union[Unset, int] = UNSET
    recognize_file: Union[Unset, "OcrResultRecognizeFile"] = UNSET
    query_languages: Union[Unset, "OcrResultQueryLanguages"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exception = self.exception

        event_id = self.event_id

        exception_id = self.exception_id

        recognize_file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recognize_file, Unset):
            recognize_file = self.recognize_file.to_dict()

        query_languages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_languages, Unset):
            query_languages = self.query_languages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exception is not UNSET:
            field_dict["exception"] = exception
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if exception_id is not UNSET:
            field_dict["exceptionID"] = exception_id
        if recognize_file is not UNSET:
            field_dict["recognizeFile"] = recognize_file
        if query_languages is not UNSET:
            field_dict["queryLanguages"] = query_languages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ocr_result_query_languages import OcrResultQueryLanguages
        from ..models.ocr_result_recognize_file import OcrResultRecognizeFile

        d = src_dict.copy()
        exception = d.pop("exception", UNSET)

        event_id = d.pop("eventId", UNSET)

        exception_id = d.pop("exceptionID", UNSET)

        _recognize_file = d.pop("recognizeFile", UNSET)
        recognize_file: Union[Unset, OcrResultRecognizeFile]
        if isinstance(_recognize_file, Unset):
            recognize_file = UNSET
        else:
            recognize_file = OcrResultRecognizeFile.from_dict(_recognize_file)

        _query_languages = d.pop("queryLanguages", UNSET)
        query_languages: Union[Unset, OcrResultQueryLanguages]
        if isinstance(_query_languages, Unset):
            query_languages = UNSET
        else:
            query_languages = OcrResultQueryLanguages.from_dict(_query_languages)

        ocr_result = cls(
            exception=exception,
            event_id=event_id,
            exception_id=exception_id,
            recognize_file=recognize_file,
            query_languages=query_languages,
        )

        ocr_result.additional_properties = d
        return ocr_result

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
