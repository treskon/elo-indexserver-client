from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportExtOptionsC")


@_attrs_define
class ExportExtOptionsC:
    """Constant class for the ExportExtOptions class.
    (The default value are always 0)

        Attributes:
            export_src_type_archive (Union[Unset, int]): Objects from archive are exported
            export_date_type_depot (Union[Unset, int]): Export filtered according depot date
            export_date_type_doc (Union[Unset, int]): Export filtered according document date
            export_src_type_search (Union[Unset, int]): Search results are exported
    """

    export_src_type_archive: Union[Unset, int] = UNSET
    export_date_type_depot: Union[Unset, int] = UNSET
    export_date_type_doc: Union[Unset, int] = UNSET
    export_src_type_search: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_src_type_archive = self.export_src_type_archive

        export_date_type_depot = self.export_date_type_depot

        export_date_type_doc = self.export_date_type_doc

        export_src_type_search = self.export_src_type_search

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_src_type_archive is not UNSET:
            field_dict["EXPORT_SRC_TYPE_ARCHIVE"] = export_src_type_archive
        if export_date_type_depot is not UNSET:
            field_dict["EXPORT_DATE_TYPE_DEPOT"] = export_date_type_depot
        if export_date_type_doc is not UNSET:
            field_dict["EXPORT_DATE_TYPE_DOC"] = export_date_type_doc
        if export_src_type_search is not UNSET:
            field_dict["EXPORT_SRC_TYPE_SEARCH"] = export_src_type_search

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_src_type_archive = d.pop("EXPORT_SRC_TYPE_ARCHIVE", UNSET)

        export_date_type_depot = d.pop("EXPORT_DATE_TYPE_DEPOT", UNSET)

        export_date_type_doc = d.pop("EXPORT_DATE_TYPE_DOC", UNSET)

        export_src_type_search = d.pop("EXPORT_SRC_TYPE_SEARCH", UNSET)

        export_ext_options_c = cls(
            export_src_type_archive=export_src_type_archive,
            export_date_type_depot=export_date_type_depot,
            export_date_type_doc=export_date_type_doc,
            export_src_type_search=export_src_type_search,
        )

        export_ext_options_c.additional_properties = d
        return export_ext_options_c

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
