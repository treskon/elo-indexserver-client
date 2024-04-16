from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewImageInfoC")


@_attrs_define
class PreviewImageInfoC:
    """
    Attributes:
        default_dpi (Union[Unset, int]): Default dots per inch for scalable vector graphics.
        size_large (Union[Unset, int]): Flag that signalizes the server to scale down preview images to a size suitable
            for most
            browser's canvas element. Choosing this settings will scale down only very large images.
        size_tiny (Union[Unset, int]): Flag that signalizes the server to process preview images in a size for
            thumbnails.
        size_medium (Union[Unset, int]): Flag that signalizes the server to process preview images in a medium size.
            Images of this size
             are optimized in memory usage. They lack readability of text smaller than 10 points.
        size_original (Union[Unset, int]): Flag that signalizes the server to process preview images in the size of the
            original document.
            In case scalable documents sources like PDF, {@link PreviewImageInfoC#DEFAULT_DPI} is used.
        size_tinier (Union[Unset, int]): Flag that signalizes the server to process preview images in a size for tiny
            thumbnails.
            The
             maximum length of an edge will be 100 pixels.
    """

    default_dpi: Union[Unset, int] = UNSET
    size_large: Union[Unset, int] = UNSET
    size_tiny: Union[Unset, int] = UNSET
    size_medium: Union[Unset, int] = UNSET
    size_original: Union[Unset, int] = UNSET
    size_tinier: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_dpi = self.default_dpi

        size_large = self.size_large

        size_tiny = self.size_tiny

        size_medium = self.size_medium

        size_original = self.size_original

        size_tinier = self.size_tinier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_dpi is not UNSET:
            field_dict["DEFAULT_DPI"] = default_dpi
        if size_large is not UNSET:
            field_dict["SIZE_LARGE"] = size_large
        if size_tiny is not UNSET:
            field_dict["SIZE_TINY"] = size_tiny
        if size_medium is not UNSET:
            field_dict["SIZE_MEDIUM"] = size_medium
        if size_original is not UNSET:
            field_dict["SIZE_ORIGINAL"] = size_original
        if size_tinier is not UNSET:
            field_dict["SIZE_TINIER"] = size_tinier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_dpi = d.pop("DEFAULT_DPI", UNSET)

        size_large = d.pop("SIZE_LARGE", UNSET)

        size_tiny = d.pop("SIZE_TINY", UNSET)

        size_medium = d.pop("SIZE_MEDIUM", UNSET)

        size_original = d.pop("SIZE_ORIGINAL", UNSET)

        size_tinier = d.pop("SIZE_TINIER", UNSET)

        preview_image_info_c = cls(
            default_dpi=default_dpi,
            size_large=size_large,
            size_tiny=size_tiny,
            size_medium=size_medium,
            size_original=size_original,
            size_tinier=size_tinier,
        )

        preview_image_info_c.additional_properties = d
        return preview_image_info_c

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
