from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FontInfo")


@_attrs_define
class FontInfo:
    """This class describes a font.

    Attributes:
        face_name (Union[Unset, str]): Font face name
        strike_out (Union[Unset, bool]): Strike out
        underline (Union[Unset, bool]): Underline
        escapement (Union[Unset, int]): Specifies the angle, in tenths of degrees, between the escapement vector and the
            x-axis of the
            device. The escapement vector is parallel to the base line of a row of text.
        height_per_cell (Union[Unset, bool]): The font height is related to the cell height of the font rather than the
            character heigth.
        bold (Union[Unset, bool]): Bold
        rgb (Union[Unset, int]): Read-green-blue value. On byte each color. Read is at the lowest significant byte.
        italic (Union[Unset, bool]): Italic
        height (Union[Unset, int]): Font heigth.
    """

    face_name: Union[Unset, str] = UNSET
    strike_out: Union[Unset, bool] = UNSET
    underline: Union[Unset, bool] = UNSET
    escapement: Union[Unset, int] = UNSET
    height_per_cell: Union[Unset, bool] = UNSET
    bold: Union[Unset, bool] = UNSET
    rgb: Union[Unset, int] = UNSET
    italic: Union[Unset, bool] = UNSET
    height: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        face_name = self.face_name

        strike_out = self.strike_out

        underline = self.underline

        escapement = self.escapement

        height_per_cell = self.height_per_cell

        bold = self.bold

        rgb = self.rgb

        italic = self.italic

        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if face_name is not UNSET:
            field_dict["faceName"] = face_name
        if strike_out is not UNSET:
            field_dict["strikeOut"] = strike_out
        if underline is not UNSET:
            field_dict["underline"] = underline
        if escapement is not UNSET:
            field_dict["escapement"] = escapement
        if height_per_cell is not UNSET:
            field_dict["heightPerCell"] = height_per_cell
        if bold is not UNSET:
            field_dict["bold"] = bold
        if rgb is not UNSET:
            field_dict["RGB"] = rgb
        if italic is not UNSET:
            field_dict["italic"] = italic
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        face_name = d.pop("faceName", UNSET)

        strike_out = d.pop("strikeOut", UNSET)

        underline = d.pop("underline", UNSET)

        escapement = d.pop("escapement", UNSET)

        height_per_cell = d.pop("heightPerCell", UNSET)

        bold = d.pop("bold", UNSET)

        rgb = d.pop("RGB", UNSET)

        italic = d.pop("italic", UNSET)

        height = d.pop("height", UNSET)

        font_info = cls(
            face_name=face_name,
            strike_out=strike_out,
            underline=underline,
            escapement=escapement,
            height_per_cell=height_per_cell,
            bold=bold,
            rgb=rgb,
            italic=italic,
            height=height,
        )

        font_info.additional_properties = d
        return font_info

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
