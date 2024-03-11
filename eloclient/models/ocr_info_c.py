from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcrInfoC")


@_attrs_define
class OcrInfoC:
    r"""Constants for OCR processing.

    Attributes:
        pdf (Union[Unset, int]): PDF output. OCR will convert the output in a PDF format.
        text (Union[Unset, int]): Text output. The OCR result is a UTF-16LE character stream.
        xml (Union[Unset, int]): XML output. The OCR result is a xml style layout.
        char_and_rect (Union[Unset, int]): Compute character positions.
            The OCR result is a binary stream of subsequent records of this layout: <br/>
             <table>
             <tr>
             <td>UTF-16 Character</td>
             <td>2 Bytes</td>
             </tr>
             <tr>
             <td>Horizontal position of upper left corner</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Vertical position of upper left corner</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Horizontal position of bottom right corner</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Vertical position of bottom right corner</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Confidence in percent</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Original UTF-16 Character</td>
             <td>2 Bytes</td>
             </tr>
             </table>
             <p>
             The character and integer byte order is Little Endian.
             </p>
             <p>
             If the recognition confidence is lower than {@link OcrInfoRecognizeFile#minCharConfidence}, the UTF-16
            character is
             equal to {@link OcrInfoRecognizeFile#replaceChar}.
             </p>
             <p>
             The rectangle coordinates are measured in points. The vertical axis points to the bottom in positive direction.
        char_and_rect_ex (Union[Unset, int]): Compute character positions.
            The OCR result is a binary stream as defined in {@link #CHAR_AND_RECT} prefixed by a
             header of this layout:
             <table>
             <tr>
             <td>Magic</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Version</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Skew Angle</td>
             <td>8 Bytes (Double)</td>
             </tr>
             <tr>
             <td>Width</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             <tr>
             <td>Height</td>
             <td>4 Bytes (Integer)</td>
             </tr>
             </table>
             The value of Magic is 0x52434F45. The value of Version is 1. The Integer and Double byte order is Little
            Endian.
             The Double value format is IEEE 754.
        char_and_rect_xml (Union[Unset, int]): Compute character positions and return XML format.
        messages_language_english (Union[Unset, int]):
        messages_language_russian (Union[Unset, int]):
        messages_language_german (Union[Unset, int]):
        messages_language_french (Union[Unset, int]):
        messages_language_ukrainian (Union[Unset, int]):
        messages_language_spanish (Union[Unset, int]):
        messages_language_italian (Union[Unset, int]):
        messages_language_dutchstandard (Union[Unset, int]):
        messages_language_portuguese (Union[Unset, int]):
        messages_language_slovak (Union[Unset, int]):
        messages_language_polish (Union[Unset, int]):
        messages_language_czech (Union[Unset, int]):
        messages_language_hungarian (Union[Unset, int]):
        messages_language_lithuanian (Union[Unset, int]):
        messages_language_latvian (Union[Unset, int]):
        messages_language_estonian (Union[Unset, int]):
        messages_language_bulgarian (Union[Unset, int]):
        unit_point (Union[Unset, int]):
        unit_millimeter (Union[Unset, int]):
        unit_inch (Union[Unset, int]):
        unit_per_thousand (Union[Unset, int]):
        spaces_normal (Union[Unset, int]): Used in SingleCoulmnMode. All words are separated by one blank.
        spaces_twospaces (Union[Unset, int]): Used in SingleCoulmnMode. If the words are separated by a larger distance,
            a second blank is inserted.
        spaces_exact (Union[Unset, int]): Used in SingleCoulmnMode. The OCR tries to insert the correct number of
            blanks.
        all_pages (Union[Unset, int]): OCR will process all pages of the given document.
        even_pages (Union[Unset, int]): Internal Use only. OCR will process all even pages of the given document.
        odd_pages (Union[Unset, int]): Internal Use only. OCR will process all odd pages of the given document.
        encoding_utf8 (Union[Unset, int]):
        encoding_utf16 (Union[Unset, int]):
        encoding_utf16le (Union[Unset, int]):
        pdf_quality_maxquality (Union[Unset, int]): Optimize the PDF (PDF/A) export in order to receive the best quality
            of the resulting file.
        pdf_quality_balanced (Union[Unset, int]): The PDF (PDF/A) export will be balanced between the quality of the
            resulting file, its size and the time of
            processing.
        pdf_quality_minsize (Union[Unset, int]): Optimize the PDF (PDF/A) export in order to receive the minimum size of
            the resulting file.
        pdf_quality_maxspeed (Union[Unset, int]): Optimize the PDF (PDF/A) export in order to receive the highest speed
            of processing.
        pdf_compliance_pdfa_3u (Union[Unset, int]): The recognized text should be exported to PDF/A-3u format.
        pdf_compliance_pdfa_3a (Union[Unset, int]): The recognized text should be exported to PDF/A-3a format.
        pdf_compliance_pdfa_2u (Union[Unset, int]): The recognized text should be exported to PDF/A-2u format.
        pdf_compliance_pdfa_2a (Union[Unset, int]): The recognized text should be exported to PDF/A-2a format.
        pdf_compliance_pdfa_1b (Union[Unset, int]): The recognized text should be exported to PDF/A-1b format.
        pdf_compliance_pdfa_1a (Union[Unset, int]): The recognized text should be exported to PDF/A-1a format.
        pdf_compliance_none (Union[Unset, int]): Compliance with PDF/A standard is not necessary.
        whitespace_default (Union[Unset, int]): Let the OCR Whitespace characters as they are.
        whitespace_replace (Union[Unset, int]): OCR Whitespace characters will be replaced: Line break and Paragraph
            break -> '\n' Tabulation -> '\t' Object
            replacement character -> ' ' Soft hyphen -> '-'
    """

    pdf: Union[Unset, int] = UNSET
    text: Union[Unset, int] = UNSET
    xml: Union[Unset, int] = UNSET
    char_and_rect: Union[Unset, int] = UNSET
    char_and_rect_ex: Union[Unset, int] = UNSET
    char_and_rect_xml: Union[Unset, int] = UNSET
    messages_language_english: Union[Unset, int] = UNSET
    messages_language_russian: Union[Unset, int] = UNSET
    messages_language_german: Union[Unset, int] = UNSET
    messages_language_french: Union[Unset, int] = UNSET
    messages_language_ukrainian: Union[Unset, int] = UNSET
    messages_language_spanish: Union[Unset, int] = UNSET
    messages_language_italian: Union[Unset, int] = UNSET
    messages_language_dutchstandard: Union[Unset, int] = UNSET
    messages_language_portuguese: Union[Unset, int] = UNSET
    messages_language_slovak: Union[Unset, int] = UNSET
    messages_language_polish: Union[Unset, int] = UNSET
    messages_language_czech: Union[Unset, int] = UNSET
    messages_language_hungarian: Union[Unset, int] = UNSET
    messages_language_lithuanian: Union[Unset, int] = UNSET
    messages_language_latvian: Union[Unset, int] = UNSET
    messages_language_estonian: Union[Unset, int] = UNSET
    messages_language_bulgarian: Union[Unset, int] = UNSET
    unit_point: Union[Unset, int] = UNSET
    unit_millimeter: Union[Unset, int] = UNSET
    unit_inch: Union[Unset, int] = UNSET
    unit_per_thousand: Union[Unset, int] = UNSET
    spaces_normal: Union[Unset, int] = UNSET
    spaces_twospaces: Union[Unset, int] = UNSET
    spaces_exact: Union[Unset, int] = UNSET
    all_pages: Union[Unset, int] = UNSET
    even_pages: Union[Unset, int] = UNSET
    odd_pages: Union[Unset, int] = UNSET
    encoding_utf8: Union[Unset, int] = UNSET
    encoding_utf16: Union[Unset, int] = UNSET
    encoding_utf16le: Union[Unset, int] = UNSET
    pdf_quality_maxquality: Union[Unset, int] = UNSET
    pdf_quality_balanced: Union[Unset, int] = UNSET
    pdf_quality_minsize: Union[Unset, int] = UNSET
    pdf_quality_maxspeed: Union[Unset, int] = UNSET
    pdf_compliance_pdfa_3u: Union[Unset, int] = UNSET
    pdf_compliance_pdfa_3a: Union[Unset, int] = UNSET
    pdf_compliance_pdfa_2u: Union[Unset, int] = UNSET
    pdf_compliance_pdfa_2a: Union[Unset, int] = UNSET
    pdf_compliance_pdfa_1b: Union[Unset, int] = UNSET
    pdf_compliance_pdfa_1a: Union[Unset, int] = UNSET
    pdf_compliance_none: Union[Unset, int] = UNSET
    whitespace_default: Union[Unset, int] = UNSET
    whitespace_replace: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pdf = self.pdf
        text = self.text
        xml = self.xml
        char_and_rect = self.char_and_rect
        char_and_rect_ex = self.char_and_rect_ex
        char_and_rect_xml = self.char_and_rect_xml
        messages_language_english = self.messages_language_english
        messages_language_russian = self.messages_language_russian
        messages_language_german = self.messages_language_german
        messages_language_french = self.messages_language_french
        messages_language_ukrainian = self.messages_language_ukrainian
        messages_language_spanish = self.messages_language_spanish
        messages_language_italian = self.messages_language_italian
        messages_language_dutchstandard = self.messages_language_dutchstandard
        messages_language_portuguese = self.messages_language_portuguese
        messages_language_slovak = self.messages_language_slovak
        messages_language_polish = self.messages_language_polish
        messages_language_czech = self.messages_language_czech
        messages_language_hungarian = self.messages_language_hungarian
        messages_language_lithuanian = self.messages_language_lithuanian
        messages_language_latvian = self.messages_language_latvian
        messages_language_estonian = self.messages_language_estonian
        messages_language_bulgarian = self.messages_language_bulgarian
        unit_point = self.unit_point
        unit_millimeter = self.unit_millimeter
        unit_inch = self.unit_inch
        unit_per_thousand = self.unit_per_thousand
        spaces_normal = self.spaces_normal
        spaces_twospaces = self.spaces_twospaces
        spaces_exact = self.spaces_exact
        all_pages = self.all_pages
        even_pages = self.even_pages
        odd_pages = self.odd_pages
        encoding_utf8 = self.encoding_utf8
        encoding_utf16 = self.encoding_utf16
        encoding_utf16le = self.encoding_utf16le
        pdf_quality_maxquality = self.pdf_quality_maxquality
        pdf_quality_balanced = self.pdf_quality_balanced
        pdf_quality_minsize = self.pdf_quality_minsize
        pdf_quality_maxspeed = self.pdf_quality_maxspeed
        pdf_compliance_pdfa_3u = self.pdf_compliance_pdfa_3u
        pdf_compliance_pdfa_3a = self.pdf_compliance_pdfa_3a
        pdf_compliance_pdfa_2u = self.pdf_compliance_pdfa_2u
        pdf_compliance_pdfa_2a = self.pdf_compliance_pdfa_2a
        pdf_compliance_pdfa_1b = self.pdf_compliance_pdfa_1b
        pdf_compliance_pdfa_1a = self.pdf_compliance_pdfa_1a
        pdf_compliance_none = self.pdf_compliance_none
        whitespace_default = self.whitespace_default
        whitespace_replace = self.whitespace_replace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf is not UNSET:
            field_dict["PDF"] = pdf
        if text is not UNSET:
            field_dict["TEXT"] = text
        if xml is not UNSET:
            field_dict["XML"] = xml
        if char_and_rect is not UNSET:
            field_dict["CHAR_AND_RECT"] = char_and_rect
        if char_and_rect_ex is not UNSET:
            field_dict["CHAR_AND_RECT_EX"] = char_and_rect_ex
        if char_and_rect_xml is not UNSET:
            field_dict["CHAR_AND_RECT_XML"] = char_and_rect_xml
        if messages_language_english is not UNSET:
            field_dict["MESSAGES_LANGUAGE_ENGLISH"] = messages_language_english
        if messages_language_russian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_RUSSIAN"] = messages_language_russian
        if messages_language_german is not UNSET:
            field_dict["MESSAGES_LANGUAGE_GERMAN"] = messages_language_german
        if messages_language_french is not UNSET:
            field_dict["MESSAGES_LANGUAGE_FRENCH"] = messages_language_french
        if messages_language_ukrainian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_UKRAINIAN"] = messages_language_ukrainian
        if messages_language_spanish is not UNSET:
            field_dict["MESSAGES_LANGUAGE_SPANISH"] = messages_language_spanish
        if messages_language_italian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_ITALIAN"] = messages_language_italian
        if messages_language_dutchstandard is not UNSET:
            field_dict["MESSAGES_LANGUAGE_DUTCHSTANDARD"] = messages_language_dutchstandard
        if messages_language_portuguese is not UNSET:
            field_dict["MESSAGES_LANGUAGE_PORTUGUESE"] = messages_language_portuguese
        if messages_language_slovak is not UNSET:
            field_dict["MESSAGES_LANGUAGE_SLOVAK"] = messages_language_slovak
        if messages_language_polish is not UNSET:
            field_dict["MESSAGES_LANGUAGE_POLISH"] = messages_language_polish
        if messages_language_czech is not UNSET:
            field_dict["MESSAGES_LANGUAGE_CZECH"] = messages_language_czech
        if messages_language_hungarian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_HUNGARIAN"] = messages_language_hungarian
        if messages_language_lithuanian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_LITHUANIAN"] = messages_language_lithuanian
        if messages_language_latvian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_LATVIAN"] = messages_language_latvian
        if messages_language_estonian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_ESTONIAN"] = messages_language_estonian
        if messages_language_bulgarian is not UNSET:
            field_dict["MESSAGES_LANGUAGE_BULGARIAN"] = messages_language_bulgarian
        if unit_point is not UNSET:
            field_dict["UNIT_POINT"] = unit_point
        if unit_millimeter is not UNSET:
            field_dict["UNIT_MILLIMETER"] = unit_millimeter
        if unit_inch is not UNSET:
            field_dict["UNIT_INCH"] = unit_inch
        if unit_per_thousand is not UNSET:
            field_dict["UNIT_PER_THOUSAND"] = unit_per_thousand
        if spaces_normal is not UNSET:
            field_dict["SPACES_NORMAL"] = spaces_normal
        if spaces_twospaces is not UNSET:
            field_dict["SPACES_TWOSPACES"] = spaces_twospaces
        if spaces_exact is not UNSET:
            field_dict["SPACES_EXACT"] = spaces_exact
        if all_pages is not UNSET:
            field_dict["ALL_PAGES"] = all_pages
        if even_pages is not UNSET:
            field_dict["EVEN_PAGES"] = even_pages
        if odd_pages is not UNSET:
            field_dict["ODD_PAGES"] = odd_pages
        if encoding_utf8 is not UNSET:
            field_dict["ENCODING_UTF8"] = encoding_utf8
        if encoding_utf16 is not UNSET:
            field_dict["ENCODING_UTF16"] = encoding_utf16
        if encoding_utf16le is not UNSET:
            field_dict["ENCODING_UTF16LE"] = encoding_utf16le
        if pdf_quality_maxquality is not UNSET:
            field_dict["PDF_QUALITY_MAXQUALITY"] = pdf_quality_maxquality
        if pdf_quality_balanced is not UNSET:
            field_dict["PDF_QUALITY_BALANCED"] = pdf_quality_balanced
        if pdf_quality_minsize is not UNSET:
            field_dict["PDF_QUALITY_MINSIZE"] = pdf_quality_minsize
        if pdf_quality_maxspeed is not UNSET:
            field_dict["PDF_QUALITY_MAXSPEED"] = pdf_quality_maxspeed
        if pdf_compliance_pdfa_3u is not UNSET:
            field_dict["PDF_COMPLIANCE_PDFA_3U"] = pdf_compliance_pdfa_3u
        if pdf_compliance_pdfa_3a is not UNSET:
            field_dict["PDF_COMPLIANCE_PDFA_3A"] = pdf_compliance_pdfa_3a
        if pdf_compliance_pdfa_2u is not UNSET:
            field_dict["PDF_COMPLIANCE_PDFA_2U"] = pdf_compliance_pdfa_2u
        if pdf_compliance_pdfa_2a is not UNSET:
            field_dict["PDF_COMPLIANCE_PDFA_2A"] = pdf_compliance_pdfa_2a
        if pdf_compliance_pdfa_1b is not UNSET:
            field_dict["PDF_COMPLIANCE_PDFA_1B"] = pdf_compliance_pdfa_1b
        if pdf_compliance_pdfa_1a is not UNSET:
            field_dict["PDF_COMPLIANCE_PDFA_1A"] = pdf_compliance_pdfa_1a
        if pdf_compliance_none is not UNSET:
            field_dict["PDF_COMPLIANCE_NONE"] = pdf_compliance_none
        if whitespace_default is not UNSET:
            field_dict["WHITESPACE_DEFAULT"] = whitespace_default
        if whitespace_replace is not UNSET:
            field_dict["WHITESPACE_REPLACE"] = whitespace_replace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pdf = d.pop("PDF", UNSET)

        text = d.pop("TEXT", UNSET)

        xml = d.pop("XML", UNSET)

        char_and_rect = d.pop("CHAR_AND_RECT", UNSET)

        char_and_rect_ex = d.pop("CHAR_AND_RECT_EX", UNSET)

        char_and_rect_xml = d.pop("CHAR_AND_RECT_XML", UNSET)

        messages_language_english = d.pop("MESSAGES_LANGUAGE_ENGLISH", UNSET)

        messages_language_russian = d.pop("MESSAGES_LANGUAGE_RUSSIAN", UNSET)

        messages_language_german = d.pop("MESSAGES_LANGUAGE_GERMAN", UNSET)

        messages_language_french = d.pop("MESSAGES_LANGUAGE_FRENCH", UNSET)

        messages_language_ukrainian = d.pop("MESSAGES_LANGUAGE_UKRAINIAN", UNSET)

        messages_language_spanish = d.pop("MESSAGES_LANGUAGE_SPANISH", UNSET)

        messages_language_italian = d.pop("MESSAGES_LANGUAGE_ITALIAN", UNSET)

        messages_language_dutchstandard = d.pop("MESSAGES_LANGUAGE_DUTCHSTANDARD", UNSET)

        messages_language_portuguese = d.pop("MESSAGES_LANGUAGE_PORTUGUESE", UNSET)

        messages_language_slovak = d.pop("MESSAGES_LANGUAGE_SLOVAK", UNSET)

        messages_language_polish = d.pop("MESSAGES_LANGUAGE_POLISH", UNSET)

        messages_language_czech = d.pop("MESSAGES_LANGUAGE_CZECH", UNSET)

        messages_language_hungarian = d.pop("MESSAGES_LANGUAGE_HUNGARIAN", UNSET)

        messages_language_lithuanian = d.pop("MESSAGES_LANGUAGE_LITHUANIAN", UNSET)

        messages_language_latvian = d.pop("MESSAGES_LANGUAGE_LATVIAN", UNSET)

        messages_language_estonian = d.pop("MESSAGES_LANGUAGE_ESTONIAN", UNSET)

        messages_language_bulgarian = d.pop("MESSAGES_LANGUAGE_BULGARIAN", UNSET)

        unit_point = d.pop("UNIT_POINT", UNSET)

        unit_millimeter = d.pop("UNIT_MILLIMETER", UNSET)

        unit_inch = d.pop("UNIT_INCH", UNSET)

        unit_per_thousand = d.pop("UNIT_PER_THOUSAND", UNSET)

        spaces_normal = d.pop("SPACES_NORMAL", UNSET)

        spaces_twospaces = d.pop("SPACES_TWOSPACES", UNSET)

        spaces_exact = d.pop("SPACES_EXACT", UNSET)

        all_pages = d.pop("ALL_PAGES", UNSET)

        even_pages = d.pop("EVEN_PAGES", UNSET)

        odd_pages = d.pop("ODD_PAGES", UNSET)

        encoding_utf8 = d.pop("ENCODING_UTF8", UNSET)

        encoding_utf16 = d.pop("ENCODING_UTF16", UNSET)

        encoding_utf16le = d.pop("ENCODING_UTF16LE", UNSET)

        pdf_quality_maxquality = d.pop("PDF_QUALITY_MAXQUALITY", UNSET)

        pdf_quality_balanced = d.pop("PDF_QUALITY_BALANCED", UNSET)

        pdf_quality_minsize = d.pop("PDF_QUALITY_MINSIZE", UNSET)

        pdf_quality_maxspeed = d.pop("PDF_QUALITY_MAXSPEED", UNSET)

        pdf_compliance_pdfa_3u = d.pop("PDF_COMPLIANCE_PDFA_3U", UNSET)

        pdf_compliance_pdfa_3a = d.pop("PDF_COMPLIANCE_PDFA_3A", UNSET)

        pdf_compliance_pdfa_2u = d.pop("PDF_COMPLIANCE_PDFA_2U", UNSET)

        pdf_compliance_pdfa_2a = d.pop("PDF_COMPLIANCE_PDFA_2A", UNSET)

        pdf_compliance_pdfa_1b = d.pop("PDF_COMPLIANCE_PDFA_1B", UNSET)

        pdf_compliance_pdfa_1a = d.pop("PDF_COMPLIANCE_PDFA_1A", UNSET)

        pdf_compliance_none = d.pop("PDF_COMPLIANCE_NONE", UNSET)

        whitespace_default = d.pop("WHITESPACE_DEFAULT", UNSET)

        whitespace_replace = d.pop("WHITESPACE_REPLACE", UNSET)

        ocr_info_c = cls(
            pdf=pdf,
            text=text,
            xml=xml,
            char_and_rect=char_and_rect,
            char_and_rect_ex=char_and_rect_ex,
            char_and_rect_xml=char_and_rect_xml,
            messages_language_english=messages_language_english,
            messages_language_russian=messages_language_russian,
            messages_language_german=messages_language_german,
            messages_language_french=messages_language_french,
            messages_language_ukrainian=messages_language_ukrainian,
            messages_language_spanish=messages_language_spanish,
            messages_language_italian=messages_language_italian,
            messages_language_dutchstandard=messages_language_dutchstandard,
            messages_language_portuguese=messages_language_portuguese,
            messages_language_slovak=messages_language_slovak,
            messages_language_polish=messages_language_polish,
            messages_language_czech=messages_language_czech,
            messages_language_hungarian=messages_language_hungarian,
            messages_language_lithuanian=messages_language_lithuanian,
            messages_language_latvian=messages_language_latvian,
            messages_language_estonian=messages_language_estonian,
            messages_language_bulgarian=messages_language_bulgarian,
            unit_point=unit_point,
            unit_millimeter=unit_millimeter,
            unit_inch=unit_inch,
            unit_per_thousand=unit_per_thousand,
            spaces_normal=spaces_normal,
            spaces_twospaces=spaces_twospaces,
            spaces_exact=spaces_exact,
            all_pages=all_pages,
            even_pages=even_pages,
            odd_pages=odd_pages,
            encoding_utf8=encoding_utf8,
            encoding_utf16=encoding_utf16,
            encoding_utf16le=encoding_utf16le,
            pdf_quality_maxquality=pdf_quality_maxquality,
            pdf_quality_balanced=pdf_quality_balanced,
            pdf_quality_minsize=pdf_quality_minsize,
            pdf_quality_maxspeed=pdf_quality_maxspeed,
            pdf_compliance_pdfa_3u=pdf_compliance_pdfa_3u,
            pdf_compliance_pdfa_3a=pdf_compliance_pdfa_3a,
            pdf_compliance_pdfa_2u=pdf_compliance_pdfa_2u,
            pdf_compliance_pdfa_2a=pdf_compliance_pdfa_2a,
            pdf_compliance_pdfa_1b=pdf_compliance_pdfa_1b,
            pdf_compliance_pdfa_1a=pdf_compliance_pdfa_1a,
            pdf_compliance_none=pdf_compliance_none,
            whitespace_default=whitespace_default,
            whitespace_replace=whitespace_replace,
        )

        ocr_info_c.additional_properties = d
        return ocr_info_c

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
