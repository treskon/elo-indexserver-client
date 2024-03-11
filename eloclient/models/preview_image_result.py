from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewImageResult")


@_attrs_define
class PreviewImageResult:
    """
    Attributes:
        urls (Union[Unset, List[str]]):
        dpi (Union[Unset, int]): Dots per inch of the requested preview images.
            If the document source is a multi-page file, this value holds for
             every requested pages.
        dimension_width (Union[Unset, int]): Width of first page. Use this value to get an idea about the dimensions of
            the preview image in general.
            While this
             value is exact for the first page, following pages may have different dimension (e.g. different orientation,
            image
             as a whole page in a PDF document, ...)
        dimension_height (Union[Unset, int]): Height of the first page.
            Please consider the hints at {@link PreviewImageResult#dimensionWidth} with respect to
             multi-page documents.
        progress (Union[Unset, int]): Current progress of processing at the server.
            Processing is finished at server side when this value equals
             {@link PreviewImageResult#progressMax}.
        progress_max (Union[Unset, int]): Estimated value about the workload at the server.
            There is a chance that the server is finished with the processing
             of the request when progress reaches this estimated value. In repeated requests progresMax can increase in
             comparison to calls in earlier times.
        status_message (Union[Unset, str]): Status message about the current processing of preview images at the server.
        pages (Union[Unset, int]): Number of pages.
    """

    urls: Union[Unset, List[str]] = UNSET
    dpi: Union[Unset, int] = UNSET
    dimension_width: Union[Unset, int] = UNSET
    dimension_height: Union[Unset, int] = UNSET
    progress: Union[Unset, int] = UNSET
    progress_max: Union[Unset, int] = UNSET
    status_message: Union[Unset, str] = UNSET
    pages: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        dpi = self.dpi
        dimension_width = self.dimension_width
        dimension_height = self.dimension_height
        progress = self.progress
        progress_max = self.progress_max
        status_message = self.status_message
        pages = self.pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if urls is not UNSET:
            field_dict["urls"] = urls
        if dpi is not UNSET:
            field_dict["dpi"] = dpi
        if dimension_width is not UNSET:
            field_dict["dimensionWidth"] = dimension_width
        if dimension_height is not UNSET:
            field_dict["dimensionHeight"] = dimension_height
        if progress is not UNSET:
            field_dict["progress"] = progress
        if progress_max is not UNSET:
            field_dict["progressMax"] = progress_max
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        urls = cast(List[str], d.pop("urls", UNSET))

        dpi = d.pop("dpi", UNSET)

        dimension_width = d.pop("dimensionWidth", UNSET)

        dimension_height = d.pop("dimensionHeight", UNSET)

        progress = d.pop("progress", UNSET)

        progress_max = d.pop("progressMax", UNSET)

        status_message = d.pop("statusMessage", UNSET)

        pages = d.pop("pages", UNSET)

        preview_image_result = cls(
            urls=urls,
            dpi=dpi,
            dimension_width=dimension_width,
            dimension_height=dimension_height,
            progress=progress,
            progress_max=progress_max,
            status_message=status_message,
            pages=pages,
        )

        preview_image_result.additional_properties = d
        return preview_image_result

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
