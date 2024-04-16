from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportOptionsC")


@_attrs_define
class ExportOptionsC:
    """Constants class for the ExportOptions class.
    Contains constants used when exporting objects from
     the ELO archive.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            export_referenced_documents (Union[Unset, str]): Include refereced documents in the export.
            export_all_versions (Union[Unset, str]): Include other versions in the export.
                The default is to only export the current active
                 document.
            export_keywords (Union[Unset, str]): Include the used keyword-lists in the export.
            export_documents (Union[Unset, str]): Include the document-files in the export.
    """

    export_referenced_documents: Union[Unset, str] = UNSET
    export_all_versions: Union[Unset, str] = UNSET
    export_keywords: Union[Unset, str] = UNSET
    export_documents: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_referenced_documents = self.export_referenced_documents

        export_all_versions = self.export_all_versions

        export_keywords = self.export_keywords

        export_documents = self.export_documents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_referenced_documents is not UNSET:
            field_dict["EXPORT_REFERENCED_DOCUMENTS"] = export_referenced_documents
        if export_all_versions is not UNSET:
            field_dict["EXPORT_ALL_VERSIONS"] = export_all_versions
        if export_keywords is not UNSET:
            field_dict["EXPORT_KEYWORDS"] = export_keywords
        if export_documents is not UNSET:
            field_dict["EXPORT_DOCUMENTS"] = export_documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_referenced_documents = d.pop("EXPORT_REFERENCED_DOCUMENTS", UNSET)

        export_all_versions = d.pop("EXPORT_ALL_VERSIONS", UNSET)

        export_keywords = d.pop("EXPORT_KEYWORDS", UNSET)

        export_documents = d.pop("EXPORT_DOCUMENTS", UNSET)

        export_options_c = cls(
            export_referenced_documents=export_referenced_documents,
            export_all_versions=export_all_versions,
            export_keywords=export_keywords,
            export_documents=export_documents,
        )

        export_options_c.additional_properties = d
        return export_options_c

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
