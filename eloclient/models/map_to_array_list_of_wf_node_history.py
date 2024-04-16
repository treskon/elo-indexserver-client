from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wf_node_history import WFNodeHistory


T = TypeVar("T", bound="MapToArrayListOfWFNodeHistory")


@_attrs_define
class MapToArrayListOfWFNodeHistory:
    """ """

    additional_properties: Dict[str, List["WFNodeHistory"]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for componentsschemas_array_list_of_wf_node_history_item_data in prop:
                componentsschemas_array_list_of_wf_node_history_item = (
                    componentsschemas_array_list_of_wf_node_history_item_data.to_dict()
                )
                field_dict[prop_name].append(componentsschemas_array_list_of_wf_node_history_item)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_node_history import WFNodeHistory

        d = src_dict.copy()
        map_to_array_list_of_wf_node_history = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemas_array_list_of_wf_node_history_item_data in _additional_property:
                componentsschemas_array_list_of_wf_node_history_item = WFNodeHistory.from_dict(
                    componentsschemas_array_list_of_wf_node_history_item_data
                )

                additional_property.append(componentsschemas_array_list_of_wf_node_history_item)

            additional_properties[prop_name] = additional_property

        map_to_array_list_of_wf_node_history.additional_properties = additional_properties
        return map_to_array_list_of_wf_node_history

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List["WFNodeHistory"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List["WFNodeHistory"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
