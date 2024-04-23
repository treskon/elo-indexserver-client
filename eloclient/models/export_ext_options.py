from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportExtOptions")


@_attrs_define
class ExportExtOptions:
    """Options for extended export.

    Attributes:
        export_docs_versions (Union[Unset, bool]):
        export_encryted_docs (Union[Unset, bool]): Export encrypted documents too?
        ignore_empty_folders (Union[Unset, bool]): Do not export empty branches (without any document).
        src_type (Union[Unset, int]): Type of the export's source (archive or search results)
        src_list (Union[Unset, List[str]]):
        date_end_iso (Union[Unset, str]): Ending date for filter in ISO format (null for no date)
        export_structure (Union[Unset, bool]): Export documents to filesystem structure.
            If this member is false, only documents are exported
             and they are all located at the root export folder.
        replace_ref_with_original (Union[Unset, bool]):
        export_keywords (Union[Unset, bool]):
        date_type (Union[Unset, int]): Which type of date must be considered?
        search_id (Union[Unset, str]): If the source is the search and if all results have to be exported, then this
            option must be
            set with the search's ID.
        masks_list (Union[Unset, List[str]]):
        date_start_iso (Union[Unset, str]): Beginning date for filter in ISO format (null for no date)
        export_attachments (Union[Unset, bool]):
        export_reminders (Union[Unset, bool]):
        export_docs (Union[Unset, bool]):
    """

    export_docs_versions: Union[Unset, bool] = UNSET
    export_encryted_docs: Union[Unset, bool] = UNSET
    ignore_empty_folders: Union[Unset, bool] = UNSET
    src_type: Union[Unset, int] = UNSET
    src_list: Union[Unset, List[str]] = UNSET
    date_end_iso: Union[Unset, str] = UNSET
    export_structure: Union[Unset, bool] = UNSET
    replace_ref_with_original: Union[Unset, bool] = UNSET
    export_keywords: Union[Unset, bool] = UNSET
    date_type: Union[Unset, int] = UNSET
    search_id: Union[Unset, str] = UNSET
    masks_list: Union[Unset, List[str]] = UNSET
    date_start_iso: Union[Unset, str] = UNSET
    export_attachments: Union[Unset, bool] = UNSET
    export_reminders: Union[Unset, bool] = UNSET
    export_docs: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_docs_versions = self.export_docs_versions

        export_encryted_docs = self.export_encryted_docs

        ignore_empty_folders = self.ignore_empty_folders

        src_type = self.src_type

        src_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.src_list, Unset):
            src_list = self.src_list

        date_end_iso = self.date_end_iso

        export_structure = self.export_structure

        replace_ref_with_original = self.replace_ref_with_original

        export_keywords = self.export_keywords

        date_type = self.date_type

        search_id = self.search_id

        masks_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.masks_list, Unset):
            masks_list = self.masks_list

        date_start_iso = self.date_start_iso

        export_attachments = self.export_attachments

        export_reminders = self.export_reminders

        export_docs = self.export_docs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_docs_versions is not UNSET:
            field_dict["exportDocsVersions"] = export_docs_versions
        if export_encryted_docs is not UNSET:
            field_dict["exportEncrytedDocs"] = export_encryted_docs
        if ignore_empty_folders is not UNSET:
            field_dict["ignoreEmptyFolders"] = ignore_empty_folders
        if src_type is not UNSET:
            field_dict["srcType"] = src_type
        if src_list is not UNSET:
            field_dict["srcList"] = src_list
        if date_end_iso is not UNSET:
            field_dict["dateEndIso"] = date_end_iso
        if export_structure is not UNSET:
            field_dict["exportStructure"] = export_structure
        if replace_ref_with_original is not UNSET:
            field_dict["replaceRefWithOriginal"] = replace_ref_with_original
        if export_keywords is not UNSET:
            field_dict["exportKeywords"] = export_keywords
        if date_type is not UNSET:
            field_dict["dateType"] = date_type
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if masks_list is not UNSET:
            field_dict["masksList"] = masks_list
        if date_start_iso is not UNSET:
            field_dict["dateStartIso"] = date_start_iso
        if export_attachments is not UNSET:
            field_dict["exportAttachments"] = export_attachments
        if export_reminders is not UNSET:
            field_dict["exportReminders"] = export_reminders
        if export_docs is not UNSET:
            field_dict["exportDocs"] = export_docs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_docs_versions = d.pop("exportDocsVersions", UNSET)

        export_encryted_docs = d.pop("exportEncrytedDocs", UNSET)

        ignore_empty_folders = d.pop("ignoreEmptyFolders", UNSET)

        src_type = d.pop("srcType", UNSET)

        src_list = cast(List[str], d.pop("srcList", UNSET))

        date_end_iso = d.pop("dateEndIso", UNSET)

        export_structure = d.pop("exportStructure", UNSET)

        replace_ref_with_original = d.pop("replaceRefWithOriginal", UNSET)

        export_keywords = d.pop("exportKeywords", UNSET)

        date_type = d.pop("dateType", UNSET)

        search_id = d.pop("searchId", UNSET)

        masks_list = cast(List[str], d.pop("masksList", UNSET))

        date_start_iso = d.pop("dateStartIso", UNSET)

        export_attachments = d.pop("exportAttachments", UNSET)

        export_reminders = d.pop("exportReminders", UNSET)

        export_docs = d.pop("exportDocs", UNSET)

        export_ext_options = cls(
            export_docs_versions=export_docs_versions,
            export_encryted_docs=export_encryted_docs,
            ignore_empty_folders=ignore_empty_folders,
            src_type=src_type,
            src_list=src_list,
            date_end_iso=date_end_iso,
            export_structure=export_structure,
            replace_ref_with_original=replace_ref_with_original,
            export_keywords=export_keywords,
            date_type=date_type,
            search_id=search_id,
            masks_list=masks_list,
            date_start_iso=date_start_iso,
            export_attachments=export_attachments,
            export_reminders=export_reminders,
            export_docs=export_docs,
        )

        export_ext_options.additional_properties = d
        return export_ext_options

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
