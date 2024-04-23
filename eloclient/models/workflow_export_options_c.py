from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowExportOptionsC")


@_attrs_define
class WorkflowExportOptionsC:
    """Contants related to the workflow export.

    Attributes:
        format_json (Union[Unset, int]): JSON format.
        format_plain_table (Union[Unset, int]): Workflow table format for compatibility with Windows Client.
    """

    format_json: Union[Unset, int] = UNSET
    format_plain_table: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_json = self.format_json

        format_plain_table = self.format_plain_table

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_json is not UNSET:
            field_dict["FORMAT_JSON"] = format_json
        if format_plain_table is not UNSET:
            field_dict["FORMAT_PLAIN_TABLE"] = format_plain_table

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_json = d.pop("FORMAT_JSON", UNSET)

        format_plain_table = d.pop("FORMAT_PLAIN_TABLE", UNSET)

        workflow_export_options_c = cls(
            format_json=format_json,
            format_plain_table=format_plain_table,
        )

        workflow_export_options_c.additional_properties = d
        return workflow_export_options_c

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
