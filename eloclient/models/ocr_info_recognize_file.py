from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData
    from ..models.ocr_rect import OcrRect


T = TypeVar("T", bound="OcrInfoRecognizeFile")


@_attrs_define
class OcrInfoRecognizeFile:
    """This class describes an OCR analysis request.

    Attributes:
        original_file_name (Union[Unset, str]): Original Filename. allows tracking through the log files of the
            different modules.
        single_column_mode (Union[Unset, bool]): Disable table recognition.
            Set this member to true, if the OCR should not try to recognized
             columns and rows of tables. Optional.
        image_data (Union[Unset, FileData]): Class for the data contained in a file.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        page_numbers (Union[Unset, List[int]]):
        recognize_rects (Union[Unset, List['OcrRect']]):
        accuracy (Union[Unset, int]): Recognition accuracy.
            A value of 0 activates the fast mode, a value of 1 activates the exact
             mode.
        encoding (Union[Unset, int]): OcrInfoC.
            ENCODING_UTF8 / _UTF16 / _UTF16LE
        min_char_confidence (Union[Unset, int]): Minimum confidence of character recognition in percent.
            Characters that are recognized with a
             lower confidence are replaced by {@link #replaceChar}. Optional.
        pdf_quality (Union[Unset, int]): OcrInfoC.
            PDF_QUALITY_MAXQUALITY / _BALANCED / _MINSIZE / _MAXSPEED
        page_no (Union[Unset, int]): Page number. The first page number is 0. If all pages should be analyzed, set
            pageNo = -1.
        replace_char (Union[Unset, int]): Replacement for characters.
            Characters that are recognized with a lower confidence than
             {@link #minCharConfidence} are replaced this character. Optional.
        obj_id (Union[Unset, str]): Object ID of an archived document to be analyzed. Either imageData or objId must be
            set.
        recognize_langs (Union[Unset, List[str]]):
        spaces (Union[Unset, int]): OcrInfoC.
            NORMAL/TWOSPACES/EXACT
        timeout_seconds (Union[Unset, int]): Recognition timeout. Cancel recognition if it least longer than this number
            of seconds.
            Optional.
        page_timeout (Union[Unset, int]): Recognition timeout for a single page.
            Cancel recognition if it least longer than this number
             of seconds. Optional.
        pdf_compliance (Union[Unset, int]): OcrInfoC.
            COMPLIANCE_PDFA_3U / _3A / _2U / _2A / _1B / _1A / _NONE
        whitespace (Union[Unset, int]): OCR returns whitespace characters.
            <table>
             <tr>
             <td>Name</td>
             <td>HEX code</td>
             </tr>
             <tr>
             <td>Line break</td>
             <td>2028</td>
             </tr>
             <tr>
             <td>Paragraph break</td>
             <td>2029</td>
             </tr>
             <tr>
             <td>Tabulation</td>
             <td>00AC</td>
             </tr>
             <tr>
             <td>Soft hyphen</td>
             <td>0009</td>
             </tr>
             <tr>
             <td>Object replacement character</td>
             <td>FFFC</td>
             </tr>
             </table>
             Must be one of the following: {@link OcrInfoC#WHITESPACE_DEFAULT},
             {@link OcrInfoC#WHITESPACE_REPLACE}
        output_format (Union[Unset, int]): Output format.
            Must be one of the following: {@link OcrInfoC#TEXT},
             {@link OcrInfoC#CHAR_AND_RECT}, {@link OcrInfoC#CHAR_AND_RECT_EX} {@link OcrInfoC#PDF},
             {@link OcrInfoC#XML}
        rect_unit (Union[Unset, int]): Rectangle coordinates are based on this unit. Use on of the constants
            OcrInfoC.UNIT_*.
            Optional.
    """

    original_file_name: Union[Unset, str] = UNSET
    single_column_mode: Union[Unset, bool] = UNSET
    image_data: Union[Unset, "FileData"] = UNSET
    page_numbers: Union[Unset, List[int]] = UNSET
    recognize_rects: Union[Unset, List["OcrRect"]] = UNSET
    accuracy: Union[Unset, int] = UNSET
    encoding: Union[Unset, int] = UNSET
    min_char_confidence: Union[Unset, int] = UNSET
    pdf_quality: Union[Unset, int] = UNSET
    page_no: Union[Unset, int] = UNSET
    replace_char: Union[Unset, int] = UNSET
    obj_id: Union[Unset, str] = UNSET
    recognize_langs: Union[Unset, List[str]] = UNSET
    spaces: Union[Unset, int] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    page_timeout: Union[Unset, int] = UNSET
    pdf_compliance: Union[Unset, int] = UNSET
    whitespace: Union[Unset, int] = UNSET
    output_format: Union[Unset, int] = UNSET
    rect_unit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        original_file_name = self.original_file_name

        single_column_mode = self.single_column_mode

        image_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_data, Unset):
            image_data = self.image_data.to_dict()

        page_numbers: Union[Unset, List[int]] = UNSET
        if not isinstance(self.page_numbers, Unset):
            page_numbers = self.page_numbers

        recognize_rects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recognize_rects, Unset):
            recognize_rects = []
            for recognize_rects_item_data in self.recognize_rects:
                recognize_rects_item = recognize_rects_item_data.to_dict()
                recognize_rects.append(recognize_rects_item)

        accuracy = self.accuracy

        encoding = self.encoding

        min_char_confidence = self.min_char_confidence

        pdf_quality = self.pdf_quality

        page_no = self.page_no

        replace_char = self.replace_char

        obj_id = self.obj_id

        recognize_langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recognize_langs, Unset):
            recognize_langs = self.recognize_langs

        spaces = self.spaces

        timeout_seconds = self.timeout_seconds

        page_timeout = self.page_timeout

        pdf_compliance = self.pdf_compliance

        whitespace = self.whitespace

        output_format = self.output_format

        rect_unit = self.rect_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_file_name is not UNSET:
            field_dict["originalFileName"] = original_file_name
        if single_column_mode is not UNSET:
            field_dict["singleColumnMode"] = single_column_mode
        if image_data is not UNSET:
            field_dict["imageData"] = image_data
        if page_numbers is not UNSET:
            field_dict["pageNumbers"] = page_numbers
        if recognize_rects is not UNSET:
            field_dict["recognizeRects"] = recognize_rects
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if min_char_confidence is not UNSET:
            field_dict["minCharConfidence"] = min_char_confidence
        if pdf_quality is not UNSET:
            field_dict["pdfQuality"] = pdf_quality
        if page_no is not UNSET:
            field_dict["pageNo"] = page_no
        if replace_char is not UNSET:
            field_dict["replaceChar"] = replace_char
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if recognize_langs is not UNSET:
            field_dict["recognizeLangs"] = recognize_langs
        if spaces is not UNSET:
            field_dict["spaces"] = spaces
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if page_timeout is not UNSET:
            field_dict["pageTimeout"] = page_timeout
        if pdf_compliance is not UNSET:
            field_dict["pdfCompliance"] = pdf_compliance
        if whitespace is not UNSET:
            field_dict["whitespace"] = whitespace
        if output_format is not UNSET:
            field_dict["outputFormat"] = output_format
        if rect_unit is not UNSET:
            field_dict["rectUnit"] = rect_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData
        from ..models.ocr_rect import OcrRect

        d = src_dict.copy()
        original_file_name = d.pop("originalFileName", UNSET)

        single_column_mode = d.pop("singleColumnMode", UNSET)

        _image_data = d.pop("imageData", UNSET)
        image_data: Union[Unset, FileData]
        if isinstance(_image_data, Unset):
            image_data = UNSET
        else:
            image_data = FileData.from_dict(_image_data)

        page_numbers = cast(List[int], d.pop("pageNumbers", UNSET))

        recognize_rects = []
        _recognize_rects = d.pop("recognizeRects", UNSET)
        for recognize_rects_item_data in _recognize_rects or []:
            recognize_rects_item = OcrRect.from_dict(recognize_rects_item_data)

            recognize_rects.append(recognize_rects_item)

        accuracy = d.pop("accuracy", UNSET)

        encoding = d.pop("encoding", UNSET)

        min_char_confidence = d.pop("minCharConfidence", UNSET)

        pdf_quality = d.pop("pdfQuality", UNSET)

        page_no = d.pop("pageNo", UNSET)

        replace_char = d.pop("replaceChar", UNSET)

        obj_id = d.pop("objId", UNSET)

        recognize_langs = cast(List[str], d.pop("recognizeLangs", UNSET))

        spaces = d.pop("spaces", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        page_timeout = d.pop("pageTimeout", UNSET)

        pdf_compliance = d.pop("pdfCompliance", UNSET)

        whitespace = d.pop("whitespace", UNSET)

        output_format = d.pop("outputFormat", UNSET)

        rect_unit = d.pop("rectUnit", UNSET)

        ocr_info_recognize_file = cls(
            original_file_name=original_file_name,
            single_column_mode=single_column_mode,
            image_data=image_data,
            page_numbers=page_numbers,
            recognize_rects=recognize_rects,
            accuracy=accuracy,
            encoding=encoding,
            min_char_confidence=min_char_confidence,
            pdf_quality=pdf_quality,
            page_no=page_no,
            replace_char=replace_char,
            obj_id=obj_id,
            recognize_langs=recognize_langs,
            spaces=spaces,
            timeout_seconds=timeout_seconds,
            page_timeout=page_timeout,
            pdf_compliance=pdf_compliance,
            whitespace=whitespace,
            output_format=output_format,
            rect_unit=rect_unit,
        )

        ocr_info_recognize_file.additional_properties = d
        return ocr_info_recognize_file

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
