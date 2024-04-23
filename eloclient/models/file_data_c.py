from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data_z import FileDataZ


T = TypeVar("T", bound="FileDataC")


@_attrs_define
class FileDataC:
    """Member constants for class FileData.

    Attributes:
        mb_data_stream (Union[Unset, FileDataZ]): Member selector for class FileData.
        ln_content_type (Union[Unset, int]):
        content_type_image_x_icon (Union[Unset, str]): Mime type image/x-icon.
        mb_data_array (Union[Unset, FileDataZ]): Member selector for class FileData.
        content_type_image_bmp (Union[Unset, str]): Mime type image/bmp.
        mb_stream (Union[Unset, str]):
        mb_data (Union[Unset, str]):
        max_blob_length (Union[Unset, str]): Maximum length of BLOB fields. This value is set to 1MB.
        content_type_image_jpeg (Union[Unset, str]): Mime type image/jpeg.
        content_type_image_x_ico (Union[Unset, str]): Mime type image/x-ico.
        mb_content_type (Union[Unset, str]):
        content_type_image_png (Union[Unset, str]): Mime type image/png.
    """

    mb_data_stream: Union[Unset, "FileDataZ"] = UNSET
    ln_content_type: Union[Unset, int] = UNSET
    content_type_image_x_icon: Union[Unset, str] = UNSET
    mb_data_array: Union[Unset, "FileDataZ"] = UNSET
    content_type_image_bmp: Union[Unset, str] = UNSET
    mb_stream: Union[Unset, str] = UNSET
    mb_data: Union[Unset, str] = UNSET
    max_blob_length: Union[Unset, str] = UNSET
    content_type_image_jpeg: Union[Unset, str] = UNSET
    content_type_image_x_ico: Union[Unset, str] = UNSET
    mb_content_type: Union[Unset, str] = UNSET
    content_type_image_png: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_data_stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_data_stream, Unset):
            mb_data_stream = self.mb_data_stream.to_dict()

        ln_content_type = self.ln_content_type

        content_type_image_x_icon = self.content_type_image_x_icon

        mb_data_array: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_data_array, Unset):
            mb_data_array = self.mb_data_array.to_dict()

        content_type_image_bmp = self.content_type_image_bmp

        mb_stream = self.mb_stream

        mb_data = self.mb_data

        max_blob_length = self.max_blob_length

        content_type_image_jpeg = self.content_type_image_jpeg

        content_type_image_x_ico = self.content_type_image_x_ico

        mb_content_type = self.mb_content_type

        content_type_image_png = self.content_type_image_png

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_data_stream is not UNSET:
            field_dict["mbDataStream"] = mb_data_stream
        if ln_content_type is not UNSET:
            field_dict["lnContentType"] = ln_content_type
        if content_type_image_x_icon is not UNSET:
            field_dict["CONTENT_TYPE_IMAGE_X_ICON"] = content_type_image_x_icon
        if mb_data_array is not UNSET:
            field_dict["mbDataArray"] = mb_data_array
        if content_type_image_bmp is not UNSET:
            field_dict["CONTENT_TYPE_IMAGE_BMP"] = content_type_image_bmp
        if mb_stream is not UNSET:
            field_dict["mbStream"] = mb_stream
        if mb_data is not UNSET:
            field_dict["mbData"] = mb_data
        if max_blob_length is not UNSET:
            field_dict["MAX_BLOB_LENGTH"] = max_blob_length
        if content_type_image_jpeg is not UNSET:
            field_dict["CONTENT_TYPE_IMAGE_JPEG"] = content_type_image_jpeg
        if content_type_image_x_ico is not UNSET:
            field_dict["CONTENT_TYPE_IMAGE_X_ICO"] = content_type_image_x_ico
        if mb_content_type is not UNSET:
            field_dict["mbContentType"] = mb_content_type
        if content_type_image_png is not UNSET:
            field_dict["CONTENT_TYPE_IMAGE_PNG"] = content_type_image_png

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data_z import FileDataZ

        d = src_dict.copy()
        _mb_data_stream = d.pop("mbDataStream", UNSET)
        mb_data_stream: Union[Unset, FileDataZ]
        if isinstance(_mb_data_stream, Unset):
            mb_data_stream = UNSET
        else:
            mb_data_stream = FileDataZ.from_dict(_mb_data_stream)

        ln_content_type = d.pop("lnContentType", UNSET)

        content_type_image_x_icon = d.pop("CONTENT_TYPE_IMAGE_X_ICON", UNSET)

        _mb_data_array = d.pop("mbDataArray", UNSET)
        mb_data_array: Union[Unset, FileDataZ]
        if isinstance(_mb_data_array, Unset):
            mb_data_array = UNSET
        else:
            mb_data_array = FileDataZ.from_dict(_mb_data_array)

        content_type_image_bmp = d.pop("CONTENT_TYPE_IMAGE_BMP", UNSET)

        mb_stream = d.pop("mbStream", UNSET)

        mb_data = d.pop("mbData", UNSET)

        max_blob_length = d.pop("MAX_BLOB_LENGTH", UNSET)

        content_type_image_jpeg = d.pop("CONTENT_TYPE_IMAGE_JPEG", UNSET)

        content_type_image_x_ico = d.pop("CONTENT_TYPE_IMAGE_X_ICO", UNSET)

        mb_content_type = d.pop("mbContentType", UNSET)

        content_type_image_png = d.pop("CONTENT_TYPE_IMAGE_PNG", UNSET)

        file_data_c = cls(
            mb_data_stream=mb_data_stream,
            ln_content_type=ln_content_type,
            content_type_image_x_icon=content_type_image_x_icon,
            mb_data_array=mb_data_array,
            content_type_image_bmp=content_type_image_bmp,
            mb_stream=mb_stream,
            mb_data=mb_data,
            max_blob_length=max_blob_length,
            content_type_image_jpeg=content_type_image_jpeg,
            content_type_image_x_ico=content_type_image_x_ico,
            mb_content_type=mb_content_type,
            content_type_image_png=content_type_image_png,
        )

        file_data_c.additional_properties = d
        return file_data_c

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
