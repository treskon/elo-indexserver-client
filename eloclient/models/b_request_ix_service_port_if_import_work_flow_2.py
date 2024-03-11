from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.workflow_import_options import WorkflowImportOptions


T = TypeVar("T", bound="BRequestIXServicePortIFImportWorkFlow2")


@_attrs_define
class BRequestIXServicePortIFImportWorkFlow2:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        flow_name (Union[Unset, str]):
        file_data (Union[Unset, str]):
        import_options (Union[Unset, WorkflowImportOptions]): Options for the workflow import.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    flow_name: Union[Unset, str] = UNSET
    file_data: Union[Unset, str] = UNSET
    import_options: Union[Unset, "WorkflowImportOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        flow_name = self.flow_name
        file_data = self.file_data
        import_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_options, Unset):
            import_options = self.import_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if file_data is not UNSET:
            field_dict["fileData"] = file_data
        if import_options is not UNSET:
            field_dict["importOptions"] = import_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.workflow_import_options import WorkflowImportOptions

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        flow_name = d.pop("flowName", UNSET)

        file_data = d.pop("fileData", UNSET)

        _import_options = d.pop("importOptions", UNSET)
        import_options: Union[Unset, WorkflowImportOptions]
        if isinstance(_import_options, Unset):
            import_options = UNSET
        else:
            import_options = WorkflowImportOptions.from_dict(_import_options)

        b_request_ix_service_port_if_import_work_flow_2 = cls(
            ci=ci,
            flow_name=flow_name,
            file_data=file_data,
            import_options=import_options,
        )

        b_request_ix_service_port_if_import_work_flow_2.additional_properties = d
        return b_request_ix_service_port_if_import_work_flow_2

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
