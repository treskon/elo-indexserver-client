from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartWorkflowInfo")


@_attrs_define
class StartWorkflowInfo:
    """This class is used as a parameter in the function
    {@link IXServicePortIF#startWorkFlow2(ClientInfo, String, StartWorkflowInfo)}.

        Attributes:
            templ_flow_id (Union[Unset, str]): Name or ID of the workflow template.
            flow_name (Union[Unset, str]): Name of the new workflow.
            flow_owner (Union[Unset, str]): The flow owner ID.
    """

    templ_flow_id: Union[Unset, str] = UNSET
    flow_name: Union[Unset, str] = UNSET
    flow_owner: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        templ_flow_id = self.templ_flow_id

        flow_name = self.flow_name

        flow_owner = self.flow_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if templ_flow_id is not UNSET:
            field_dict["templFlowId"] = templ_flow_id
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if flow_owner is not UNSET:
            field_dict["flowOwner"] = flow_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        templ_flow_id = d.pop("templFlowId", UNSET)

        flow_name = d.pop("flowName", UNSET)

        flow_owner = d.pop("flowOwner", UNSET)

        start_workflow_info = cls(
            templ_flow_id=templ_flow_id,
            flow_name=flow_name,
            flow_owner=flow_owner,
        )

        start_workflow_info.additional_properties = d
        return start_workflow_info

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
