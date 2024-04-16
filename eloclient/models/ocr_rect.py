from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcrRect")


@_attrs_define
class OcrRect:
    """This class contains the coordinates of a rectangle and is used by the
    {@link OcrInfoRecognizeFile} class.

        Attributes:
            top (Union[Unset, int]):
            left (Union[Unset, int]):
            bottom (Union[Unset, int]):
            right (Union[Unset, int]):
    """

    top: Union[Unset, int] = UNSET
    left: Union[Unset, int] = UNSET
    bottom: Union[Unset, int] = UNSET
    right: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        top = self.top

        left = self.left

        bottom = self.bottom

        right = self.right

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top is not UNSET:
            field_dict["top"] = top
        if left is not UNSET:
            field_dict["left"] = left
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if right is not UNSET:
            field_dict["right"] = right

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        top = d.pop("top", UNSET)

        left = d.pop("left", UNSET)

        bottom = d.pop("bottom", UNSET)

        right = d.pop("right", UNSET)

        ocr_rect = cls(
            top=top,
            left=left,
            bottom=bottom,
            right=right,
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
