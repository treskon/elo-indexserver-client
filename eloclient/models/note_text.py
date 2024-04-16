from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.font_info import FontInfo


T = TypeVar("T", bound="NoteText")


@_attrs_define
class NoteText:
    """This class conatins additional information for textual notes.
    NoteText objects can be used in
     NoteTemplate and Note objects.

        Attributes:
            font_info (Union[Unset, FontInfo]): This class describes a font.
            text (Union[Unset, str]): Stamp text. The maximum length is NoteDataC.
                lnDesc - 50, if the NoteText object is used in a
                 Note object. The length for a text of a NoteTemplate object is defined by NoteTemplateC.lnText
    """

    font_info: Union[Unset, "FontInfo"] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        font_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.font_info, Unset):
            font_info = self.font_info.to_dict()

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if font_info is not UNSET:
            field_dict["fontInfo"] = font_info
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.font_info import FontInfo

        d = src_dict.copy()
        _font_info = d.pop("fontInfo", UNSET)
        font_info: Union[Unset, FontInfo]
        if isinstance(_font_info, Unset):
            font_info = UNSET
        else:
            font_info = FontInfo.from_dict(_font_info)

        text = d.pop("text", UNSET)

        note_text = cls(
            font_info=font_info,
            text=text,
        )

        note_text.additional_properties = d
        return note_text

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
