from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewImageInfo")


@_attrs_define
class PreviewImageInfo:
    """
    Attributes:
        object_id (Union[Unset, str]): <p>
            ID of the objects to query preview images for. The ID must point to a document. Otherwise, an exception is
            thrown.
             </p>
        document_id (Union[Unset, str]): <p>
            Id of the document(-version) to query preview images for. If set, <code>objectId</code> is ignored.
             </p>
        start_page (Union[Unset, int]): <p>
            First page number of the document to process a preview image for. The number of the first page of a document is
            1.
             If this value is &le; 0, 1 is assumed.
             </p>
        end_page (Union[Unset, int]): <p>
            Last page number of the document to process a preview image for. If this value is &le; 0, all pages of the
            document
             &ge; startPage are process. If 0 &lt; endPage &le; startPage holds, only the startPage will be processed.
             </p>
        preview_size (Union[Unset, int]): Desired size of the preview images. Valid values are defined in {@link
            PreviewImageInfoC}.
        process_document (Union[Unset, bool]): <p>
            If processDocument is true, not only the URLs for each page are generated but also preview images are processed
            for
             the pages (startPage+1) to endPage in the background.
             </p>
        render_annotations (Union[Unset, bool]): <p>
            Enables rendering of annotations. If <code>renderAnnotations</code> is <b>true</b>, the preview images will also
             contain the annotations. If the preview images should contain the annotations but not the preview of the
            document
             page itself, also set <code>renderOnlyAnnotations</code> to <b>true</b>.
             </p>
        render_annotations_only (Union[Unset, bool]): <p>
            Does only has an effect, if <code>renderAnnotations</code> is <b>true</b>. If set to <b>true</b> the annotations
             will be rendered but the rendering of document pages will be omitted.
             </p>
        render_annotations_data (Union[Unset, bool]): <p>
            Does only has an effect, if <code>renderAnnotations</code> is <b>true</b>. If set to <b>true</b> there will be
             details rendered near the annotations. Details are the annotation's author and create date.
             </p>
    """

    object_id: Union[Unset, str] = UNSET
    document_id: Union[Unset, str] = UNSET
    start_page: Union[Unset, int] = UNSET
    end_page: Union[Unset, int] = UNSET
    preview_size: Union[Unset, int] = UNSET
    process_document: Union[Unset, bool] = UNSET
    render_annotations: Union[Unset, bool] = UNSET
    render_annotations_only: Union[Unset, bool] = UNSET
    render_annotations_data: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_id = self.object_id
        document_id = self.document_id
        start_page = self.start_page
        end_page = self.end_page
        preview_size = self.preview_size
        process_document = self.process_document
        render_annotations = self.render_annotations
        render_annotations_only = self.render_annotations_only
        render_annotations_data = self.render_annotations_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if start_page is not UNSET:
            field_dict["startPage"] = start_page
        if end_page is not UNSET:
            field_dict["endPage"] = end_page
        if preview_size is not UNSET:
            field_dict["previewSize"] = preview_size
        if process_document is not UNSET:
            field_dict["processDocument"] = process_document
        if render_annotations is not UNSET:
            field_dict["renderAnnotations"] = render_annotations
        if render_annotations_only is not UNSET:
            field_dict["renderAnnotationsOnly"] = render_annotations_only
        if render_annotations_data is not UNSET:
            field_dict["renderAnnotationsData"] = render_annotations_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_id = d.pop("objectId", UNSET)

        document_id = d.pop("documentId", UNSET)

        start_page = d.pop("startPage", UNSET)

        end_page = d.pop("endPage", UNSET)

        preview_size = d.pop("previewSize", UNSET)

        process_document = d.pop("processDocument", UNSET)

        render_annotations = d.pop("renderAnnotations", UNSET)

        render_annotations_only = d.pop("renderAnnotationsOnly", UNSET)

        render_annotations_data = d.pop("renderAnnotationsData", UNSET)

        preview_image_info = cls(
            object_id=object_id,
            document_id=document_id,
            start_page=start_page,
            end_page=end_page,
            preview_size=preview_size,
            process_document=process_document,
            render_annotations=render_annotations,
            render_annotations_only=render_annotations_only,
            render_annotations_data=render_annotations_data,
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
