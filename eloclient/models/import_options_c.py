from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportOptionsC")


@_attrs_define
class ImportOptionsC:
    """Defines the Options of an Import. Each Option is represented by one bit.
    Several Options can be put together by a
     bit-logic and.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            keep_filing_date (Union[Unset, str]): Use original filing-date (Sord.iDateIso saved in export) when filing
                during import.
            use_exported_path (Union[Unset, str]): Use original filing-path for import (original path of exporting archive
                was saved during export)
            guids_new (Union[Unset, str]): generate new guids during import.
            import_keywords (Union[Unset, str]): Import keywords
            use_parent_acl (Union[Unset, str]): Use parent's ACL in archive
            guids_keep_and_skip (Union[Unset, str]): import only guids that are not already used.
            guids_script (Union[Unset, str]): make a new version for document with this guid.
            create_separate_structure (Union[Unset, str]): Import all data in a new structure.
            guids_keep (Union[Unset, str]): Keep guids on import, generate new guid if guid is already used.
    """

    keep_filing_date: Union[Unset, str] = UNSET
    use_exported_path: Union[Unset, str] = UNSET
    guids_new: Union[Unset, str] = UNSET
    import_keywords: Union[Unset, str] = UNSET
    use_parent_acl: Union[Unset, str] = UNSET
    guids_keep_and_skip: Union[Unset, str] = UNSET
    guids_script: Union[Unset, str] = UNSET
    create_separate_structure: Union[Unset, str] = UNSET
    guids_keep: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keep_filing_date = self.keep_filing_date

        use_exported_path = self.use_exported_path

        guids_new = self.guids_new

        import_keywords = self.import_keywords

        use_parent_acl = self.use_parent_acl

        guids_keep_and_skip = self.guids_keep_and_skip

        guids_script = self.guids_script

        create_separate_structure = self.create_separate_structure

        guids_keep = self.guids_keep

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keep_filing_date is not UNSET:
            field_dict["KEEP_FILING_DATE"] = keep_filing_date
        if use_exported_path is not UNSET:
            field_dict["USE_EXPORTED_PATH"] = use_exported_path
        if guids_new is not UNSET:
            field_dict["GUIDS_NEW"] = guids_new
        if import_keywords is not UNSET:
            field_dict["IMPORT_KEYWORDS"] = import_keywords
        if use_parent_acl is not UNSET:
            field_dict["USE_PARENT_ACL"] = use_parent_acl
        if guids_keep_and_skip is not UNSET:
            field_dict["GUIDS_KEEP_AND_SKIP"] = guids_keep_and_skip
        if guids_script is not UNSET:
            field_dict["GUIDS_SCRIPT"] = guids_script
        if create_separate_structure is not UNSET:
            field_dict["CREATE_SEPARATE_STRUCTURE"] = create_separate_structure
        if guids_keep is not UNSET:
            field_dict["GUIDS_KEEP"] = guids_keep

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keep_filing_date = d.pop("KEEP_FILING_DATE", UNSET)

        use_exported_path = d.pop("USE_EXPORTED_PATH", UNSET)

        guids_new = d.pop("GUIDS_NEW", UNSET)

        import_keywords = d.pop("IMPORT_KEYWORDS", UNSET)

        use_parent_acl = d.pop("USE_PARENT_ACL", UNSET)

        guids_keep_and_skip = d.pop("GUIDS_KEEP_AND_SKIP", UNSET)

        guids_script = d.pop("GUIDS_SCRIPT", UNSET)

        create_separate_structure = d.pop("CREATE_SEPARATE_STRUCTURE", UNSET)

        guids_keep = d.pop("GUIDS_KEEP", UNSET)

        import_options_c = cls(
            keep_filing_date=keep_filing_date,
            use_exported_path=use_exported_path,
            guids_new=guids_new,
            import_keywords=import_keywords,
            use_parent_acl=use_parent_acl,
            guids_keep_and_skip=guids_keep_and_skip,
            guids_script=guids_script,
            create_separate_structure=create_separate_structure,
            guids_keep=guids_keep,
        )

        import_options_c.additional_properties = d
        return import_options_c

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
