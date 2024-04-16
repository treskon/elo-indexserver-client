from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportDesc")


@_attrs_define
class ExportDesc:
    """Descriptor for an Export.
    This class should be the first Entity in an Export/Import-File and provides extra informationen about the Export

        Attributes:
            source_archive (Union[Unset, str]): The name of the source repository of the export
            export_ref_path (Union[Unset, List[str]]):
    """

    source_archive: Union[Unset, str] = UNSET
    export_ref_path: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_archive = self.source_archive

        export_ref_path: Union[Unset, List[str]] = UNSET
        if not isinstance(self.export_ref_path, Unset):
            export_ref_path = self.export_ref_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_archive is not UNSET:
            field_dict["sourceArchive"] = source_archive
        if export_ref_path is not UNSET:
            field_dict["exportRefPath"] = export_ref_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_archive = d.pop("sourceArchive", UNSET)

        export_ref_path = cast(List[str], d.pop("exportRefPath", UNSET))

        export_desc = cls(
            source_archive=source_archive,
            export_ref_path=export_ref_path,
        )

        export_desc.additional_properties = d
        return export_desc

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
