from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewImageInfo")


@_attrs_define
class PreviewImageInfo:
    """
    Attributes:
        preview_size (Union[Unset, int]): Desired size of the preview images. Valid values are defined in {@link
            PreviewImageInfoC}.
        render_annotations_data (Union[Unset, bool]): <p>
            Does only has an effect, if <code>renderAnnotations</code> is <b>true</b>. If set to
             <b>true</b> there will be details rendered near the annotations. Details are the annotation's
             author and create date.
             </p>
        start_page (Union[Unset, int]): <p>
            First page number of the document to process a preview image for. The number of the first page
             of a document is 1. If this value is &le; 0, 1 is assumed.
             </p>
        render_annotations_only (Union[Unset, bool]): <p>
            Does only has an effect, if <code>renderAnnotations</code> is <b>true</b>. If set to
             <b>true</b> the annotations will be rendered but the rendering of document pages will be
             omitted.
             </p>
        process_document (Union[Unset, bool]): <p>
            If processDocument is true, not only the URLs for each page are generated but also preview
             images are processed for the pages (startPage+1) to endPage in the background.
             </p>
        document_id (Union[Unset, str]): <p>
            Id of the document(-version) to query preview images for. If set, <code>objectId</code> is
             ignored.
             </p>
        end_page (Union[Unset, int]): <p>
            Last page number of the document to process a preview image for. If this value is &le; 0, all
             pages of the document &ge; startPage are process. If 0 &lt; endPage &le; startPage holds, only
             the startPage will be processed.
             </p>
        object_id (Union[Unset, str]): <p>
            ID of the objects to query preview images for. The ID must point to a document. Otherwise, an
             exception is thrown.
             </p>
        render_annotations (Union[Unset, bool]): <p>
            Enables rendering of annotations. If <code>renderAnnotations</code> is <b>true</b>, the preview
             images will also contain the annotations. If the preview images should contain the annotations
             but not the preview of the document page itself, also set <code>renderOnlyAnnotations</code> to
             <b>true</b>.
             </p>
    """

    preview_size: Union[Unset, int] = UNSET
    render_annotations_data: Union[Unset, bool] = UNSET
    start_page: Union[Unset, int] = UNSET
    render_annotations_only: Union[Unset, bool] = UNSET
    process_document: Union[Unset, bool] = UNSET
    document_id: Union[Unset, str] = UNSET
    end_page: Union[Unset, int] = UNSET
    object_id: Union[Unset, str] = UNSET
    render_annotations: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preview_size = self.preview_size

        render_annotations_data = self.render_annotations_data

        start_page = self.start_page

        render_annotations_only = self.render_annotations_only

        process_document = self.process_document

        document_id = self.document_id

        end_page = self.end_page

        object_id = self.object_id

        render_annotations = self.render_annotations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview_size is not UNSET:
            field_dict["previewSize"] = preview_size
        if render_annotations_data is not UNSET:
            field_dict["renderAnnotationsData"] = render_annotations_data
        if start_page is not UNSET:
            field_dict["startPage"] = start_page
        if render_annotations_only is not UNSET:
            field_dict["renderAnnotationsOnly"] = render_annotations_only
        if process_document is not UNSET:
            field_dict["processDocument"] = process_document
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if end_page is not UNSET:
            field_dict["endPage"] = end_page
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if render_annotations is not UNSET:
            field_dict["renderAnnotations"] = render_annotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        preview_size = d.pop("previewSize", UNSET)

        render_annotations_data = d.pop("renderAnnotationsData", UNSET)

        start_page = d.pop("startPage", UNSET)

        render_annotations_only = d.pop("renderAnnotationsOnly", UNSET)

        process_document = d.pop("processDocument", UNSET)

        document_id = d.pop("documentId", UNSET)

        end_page = d.pop("endPage", UNSET)

        object_id = d.pop("objectId", UNSET)

        render_annotations = d.pop("renderAnnotations", UNSET)

        preview_image_info = cls(
            preview_size=preview_size,
            render_annotations_data=render_annotations_data,
            start_page=start_page,
            render_annotations_only=render_annotations_only,
            process_document=process_document,
            document_id=document_id,
            end_page=end_page,
            object_id=object_id,
            render_annotations=render_annotations,
        )

        preview_image_info.additional_properties = d
        return preview_image_info

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
