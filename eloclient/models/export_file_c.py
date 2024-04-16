from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportFileC")


@_attrs_define
class ExportFileC:
    """
    Attributes:
        file_extension (Union[Unset, str]): Filename Extension for export data files
        magic (Union[Unset, int]): Identifier for Export files
        content_type (Union[Unset, str]): Content Type for export data files
        file_version (Union[Unset, str]): The export file version this IX creates.
    """

    file_extension: Union[Unset, str] = UNSET
    magic: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    file_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_extension = self.file_extension

        magic = self.magic

        content_type = self.content_type

        file_version = self.file_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_extension is not UNSET:
            field_dict["FILE_EXTENSION"] = file_extension
        if magic is not UNSET:
            field_dict["MAGIC"] = magic
        if content_type is not UNSET:
            field_dict["CONTENT_TYPE"] = content_type
        if file_version is not UNSET:
            field_dict["FILE_VERSION"] = file_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_extension = d.pop("FILE_EXTENSION", UNSET)

        magic = d.pop("MAGIC", UNSET)

        content_type = d.pop("CONTENT_TYPE", UNSET)

        file_version = d.pop("FILE_VERSION", UNSET)

        export_file_c = cls(
            file_extension=file_extension,
            magic=magic,
            content_type=content_type,
            file_version=file_version,
        )

        export_file_c.additional_properties = d
        return export_file_c

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
