from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_aggregation_result import MapToAggregationResult


T = TypeVar("T", bound="FilterAggregationResult")


@_attrs_define
class FilterAggregationResult:
    """The result object of a filter aggregation.
    <br>
     It consists mainly of inner aggregations results (sub-aggregations).

        Attributes:
            doc_count (Union[Unset, str]): Number of documents belonging to the filter's criteria.
            aggregations (Union[Unset, MapToAggregationResult]):
    """

    doc_count: Union[Unset, str] = UNSET
    aggregations: Union[Unset, "MapToAggregationResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_count = self.doc_count

        aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregations, Unset):
            aggregations = self.aggregations.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_count is not UNSET:
            field_dict["docCount"] = doc_count
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_aggregation_result import MapToAggregationResult

        d = src_dict.copy()
        doc_count = d.pop("docCount", UNSET)

        _aggregations = d.pop("aggregations", UNSET)
        aggregations: Union[Unset, MapToAggregationResult]
        if isinstance(_aggregations, Unset):
            aggregations = UNSET
        else:
            aggregations = MapToAggregationResult.from_dict(_aggregations)

        filter_aggregation_result = cls(
            doc_count=doc_count,
            aggregations=aggregations,
        )

        filter_aggregation_result.additional_properties = d
        return filter_aggregation_result

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
