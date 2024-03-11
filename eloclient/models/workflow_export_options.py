from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowExportOptions")


@_attrs_define
class WorkflowExportOptions:
    """Structure for the options for the workflow-export.
    <p>
     Copyright: Copyright (c) 2009
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            flow_id (Union[Unset, str]): Id of the workflow, that will be exported.
            flow_vers_id (Union[Unset, str]): Reserved.
            character_set (Union[Unset, str]): Character set for the export-data.
            word_wrap (Union[Unset, str]): Word wrap for the export-data.
            format_ (Union[Unset, int]): Export format.
    """

    flow_id: Union[Unset, str] = UNSET
    flow_vers_id: Union[Unset, str] = UNSET
    character_set: Union[Unset, str] = UNSET
    word_wrap: Union[Unset, str] = UNSET
    format_: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flow_id = self.flow_id
        flow_vers_id = self.flow_vers_id
        character_set = self.character_set
        word_wrap = self.word_wrap
        format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if flow_vers_id is not UNSET:
            field_dict["flowVersId"] = flow_vers_id
        if character_set is not UNSET:
            field_dict["characterSet"] = character_set
        if word_wrap is not UNSET:
            field_dict["wordWrap"] = word_wrap
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flow_id = d.pop("flowId", UNSET)

        flow_vers_id = d.pop("flowVersId", UNSET)

        character_set = d.pop("characterSet", UNSET)

        word_wrap = d.pop("wordWrap", UNSET)

        format_ = d.pop("format", UNSET)

        workflow_export_options = cls(
            flow_id=flow_id,
            flow_vers_id=flow_vers_id,
            character_set=character_set,
            word_wrap=word_wrap,
            format_=format_,
        )

        workflow_export_options.additional_properties = d
        return workflow_export_options

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
