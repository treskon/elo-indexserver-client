from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByPreviewCtrl")


@_attrs_define
class FindByPreviewCtrl:
    """This class can be used to find the documents for which preview files have to be created.
    The main purpose is to
     control the automatic preview generation in a server process.

        Attributes:
            preview_available (Union[Unset, bool]): Finds all documents with previews.
            preview_error (Union[Unset, bool]): Finds all documents for which the preview generation failed.
            file_extensions (Union[Unset, List[str]]):
    """

    preview_available: Union[Unset, bool] = UNSET
    preview_error: Union[Unset, bool] = UNSET
    file_extensions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preview_available = self.preview_available
        preview_error = self.preview_error
        file_extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.file_extensions, Unset):
            file_extensions = self.file_extensions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview_available is not UNSET:
            field_dict["previewAvailable"] = preview_available
        if preview_error is not UNSET:
            field_dict["previewError"] = preview_error
        if file_extensions is not UNSET:
            field_dict["fileExtensions"] = file_extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        preview_available = d.pop("previewAvailable", UNSET)

        preview_error = d.pop("previewError", UNSET)

        file_extensions = cast(List[str], d.pop("fileExtensions", UNSET))

        find_by_preview_ctrl = cls(
            preview_available=preview_available,
            preview_error=preview_error,
            file_extensions=file_extensions,
        )

        find_by_preview_ctrl.additional_properties = d
        return find_by_preview_ctrl

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
