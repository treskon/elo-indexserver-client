from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcrRect")


@_attrs_define
class OcrRect:
    """This class contains the coordinates of a rectangle and is used by the {@link OcrInfoRecognizeFile} class.

    Attributes:
        left (Union[Unset, int]):
        top (Union[Unset, int]):
        right (Union[Unset, int]):
        bottom (Union[Unset, int]):
    """

    left: Union[Unset, int] = UNSET
    top: Union[Unset, int] = UNSET
    right: Union[Unset, int] = UNSET
    bottom: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        left = self.left
        top = self.top
        right = self.right
        bottom = self.bottom

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left is not UNSET:
            field_dict["left"] = left
        if top is not UNSET:
            field_dict["top"] = top
        if right is not UNSET:
            field_dict["right"] = right
        if bottom is not UNSET:
            field_dict["bottom"] = bottom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        left = d.pop("left", UNSET)

        top = d.pop("top", UNSET)

        right = d.pop("right", UNSET)

        bottom = d.pop("bottom", UNSET)

        ocr_rect = cls(
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        ocr_rect.additional_properties = d
        return ocr_rect

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
