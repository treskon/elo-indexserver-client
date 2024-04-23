from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_array_list_of_wf_diagram import MapToArrayListOfWFDiagram
    from ..models.map_to_user_name import MapToUserName
    from ..models.map_to_wf_diagram import MapToWFDiagram
    from ..models.wf_diagram import WFDiagram


T = TypeVar("T", bound="WorkflowExchangeInfo")


@_attrs_define
class WorkflowExchangeInfo:
    """This class represents a workflow export data.

    Attributes:
        sub_workflow_version_map (Union[Unset, MapToArrayListOfWFDiagram]):
        workflow (Union[Unset, WFDiagram]): This class represents an active or finished workflow or a workflow template
        workflow_versions (Union[Unset, List['WFDiagram']]):
        user_names (Union[Unset, MapToUserName]):
        sub_workflow_map (Union[Unset, MapToWFDiagram]):
    """

    sub_workflow_version_map: Union[Unset, "MapToArrayListOfWFDiagram"] = UNSET
    workflow: Union[Unset, "WFDiagram"] = UNSET
    workflow_versions: Union[Unset, List["WFDiagram"]] = UNSET
    user_names: Union[Unset, "MapToUserName"] = UNSET
    sub_workflow_map: Union[Unset, "MapToWFDiagram"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_workflow_version_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_workflow_version_map, Unset):
            sub_workflow_version_map = self.sub_workflow_version_map.to_dict()

        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflow_versions, Unset):
            workflow_versions = []
            for workflow_versions_item_data in self.workflow_versions:
                workflow_versions_item = workflow_versions_item_data.to_dict()
                workflow_versions.append(workflow_versions_item)

        user_names: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_names, Unset):
            user_names = self.user_names.to_dict()

        sub_workflow_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_workflow_map, Unset):
            sub_workflow_map = self.sub_workflow_map.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_workflow_version_map is not UNSET:
            field_dict["subWorkflowVersionMap"] = sub_workflow_version_map
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_versions is not UNSET:
            field_dict["workflowVersions"] = workflow_versions
        if user_names is not UNSET:
            field_dict["userNames"] = user_names
        if sub_workflow_map is not UNSET:
            field_dict["subWorkflowMap"] = sub_workflow_map

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_array_list_of_wf_diagram import MapToArrayListOfWFDiagram
        from ..models.map_to_user_name import MapToUserName
        from ..models.map_to_wf_diagram import MapToWFDiagram
        from ..models.wf_diagram import WFDiagram

        d = src_dict.copy()
        _sub_workflow_version_map = d.pop("subWorkflowVersionMap", UNSET)
        sub_workflow_version_map: Union[Unset, MapToArrayListOfWFDiagram]
        if isinstance(_sub_workflow_version_map, Unset):
            sub_workflow_version_map = UNSET
        else:
            sub_workflow_version_map = MapToArrayListOfWFDiagram.from_dict(_sub_workflow_version_map)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WFDiagram]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WFDiagram.from_dict(_workflow)

        workflow_versions = []
        _workflow_versions = d.pop("workflowVersions", UNSET)
        for workflow_versions_item_data in _workflow_versions or []:
            workflow_versions_item = WFDiagram.from_dict(workflow_versions_item_data)

            workflow_versions.append(workflow_versions_item)

        _user_names = d.pop("userNames", UNSET)
        user_names: Union[Unset, MapToUserName]
        if isinstance(_user_names, Unset):
            user_names = UNSET
        else:
            user_names = MapToUserName.from_dict(_user_names)

        _sub_workflow_map = d.pop("subWorkflowMap", UNSET)
        sub_workflow_map: Union[Unset, MapToWFDiagram]
        if isinstance(_sub_workflow_map, Unset):
            sub_workflow_map = UNSET
        else:
            sub_workflow_map = MapToWFDiagram.from_dict(_sub_workflow_map)

        workflow_exchange_info = cls(
            sub_workflow_version_map=sub_workflow_version_map,
            workflow=workflow,
            workflow_versions=workflow_versions,
            user_names=user_names,
            sub_workflow_map=sub_workflow_map,
        )

        workflow_exchange_info.additional_properties = d
        return workflow_exchange_info

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
