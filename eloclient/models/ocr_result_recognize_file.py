from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="OcrResultRecognizeFile")


@_attrs_define
class OcrResultRecognizeFile:
    """This class contains the result of an OCR analysis.

    Attributes:
        text_data (Union[Unset, FileData]): Class for the data contained in a file.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        text (Union[Unset, str]): Recognized text. This member is set, if {@link OcrInfoRecognizeFile#outputFormat} was
            set to {@link OcrInfoC#TEXT}.
        skew_angle (Union[Unset, float]): Skew angle. Only valid if a single page was analyzed, see {@link
            OcrInfoRecognizeFile#pageNo}.
        width (Union[Unset, int]): Page width. Only valid if a single page was analyzed, see {@link
            OcrInfoRecognizeFile#pageNo}.
        height (Union[Unset, int]): Page height. Only valid if a single page was analyzed, see {@link
            OcrInfoRecognizeFile#pageNo}.
    """

    text_data: Union[Unset, "FileData"] = UNSET
    text: Union[Unset, str] = UNSET
    skew_angle: Union[Unset, float] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text_data, Unset):
            text_data = self.text_data.to_dict()

        text = self.text
        skew_angle = self.skew_angle
        width = self.width
        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text_data is not UNSET:
            field_dict["textData"] = text_data
        if text is not UNSET:
            field_dict["text"] = text
        if skew_angle is not UNSET:
            field_dict["skewAngle"] = skew_angle
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        _text_data = d.pop("textData", UNSET)
        text_data: Union[Unset, FileData]
        if isinstance(_text_data, Unset):
            text_data = UNSET
        else:
            text_data = FileData.from_dict(_text_data)

        text = d.pop("text", UNSET)

        skew_angle = d.pop("skewAngle", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        ocr_result_recognize_file = cls(
            text_data=text_data,
            text=text,
            skew_angle=skew_angle,
            width=width,
            height=height,
        )

        ocr_result_recognize_file.additional_properties = d
        return ocr_result_recognize_file

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
