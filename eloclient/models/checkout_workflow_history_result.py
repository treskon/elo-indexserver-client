from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_array_list_of_wf_node_history import MapToArrayListOfWFNodeHistory


T = TypeVar("T", bound="CheckoutWorkflowHistoryResult")


@_attrs_define
class CheckoutWorkflowHistoryResult:
    """This class contains the results returned by the function checkoutWorkflowHistory.

    Attributes:
        node_histories (Union[Unset, MapToArrayListOfWFNodeHistory]):
    """

    node_histories: Union[Unset, "MapToArrayListOfWFNodeHistory"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_histories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node_histories, Unset):
            node_histories = self.node_histories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_histories is not UNSET:
            field_dict["nodeHistories"] = node_histories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_array_list_of_wf_node_history import MapToArrayListOfWFNodeHistory

        d = src_dict.copy()
        _node_histories = d.pop("nodeHistories", UNSET)
        node_histories: Union[Unset, MapToArrayListOfWFNodeHistory]
        if isinstance(_node_histories, Unset):
            node_histories = UNSET
        else:
            node_histories = MapToArrayListOfWFNodeHistory.from_dict(_node_histories)

        checkout_workflow_history_result = cls(
            node_histories=node_histories,
        )

        checkout_workflow_history_result.additional_properties = d
        return checkout_workflow_history_result

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
