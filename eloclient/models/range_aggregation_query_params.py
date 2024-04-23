from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.double_range_value import DoubleRangeValue
    from ..models.map_to_aggregation_query import MapToAggregationQuery


T = TypeVar("T", bound="RangeAggregationQueryParams")


@_attrs_define
class RangeAggregationQueryParams:
    """Defines parameters to run an aggregation of type "Range" (a multi-bucket-aggregation).
    <br>
     This aggregation query allows sub-aggregations.

        Attributes:
            ranges (Union[Unset, List['DoubleRangeValue']]):
            sub_aggregations (Union[Unset, MapToAggregationQuery]):
    """

    ranges: Union[Unset, List["DoubleRangeValue"]] = UNSET
    sub_aggregations: Union[Unset, "MapToAggregationQuery"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ranges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for componentsschemas_list_of_double_range_value_item_data in self.ranges:
                componentsschemas_list_of_double_range_value_item = (
                    componentsschemas_list_of_double_range_value_item_data.to_dict()
                )
                ranges.append(componentsschemas_list_of_double_range_value_item)

        sub_aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_aggregations, Unset):
            sub_aggregations = self.sub_aggregations.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if sub_aggregations is not UNSET:
            field_dict["subAggregations"] = sub_aggregations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.double_range_value import DoubleRangeValue
        from ..models.map_to_aggregation_query import MapToAggregationQuery

        d = src_dict.copy()
        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for componentsschemas_list_of_double_range_value_item_data in _ranges or []:
            componentsschemas_list_of_double_range_value_item = DoubleRangeValue.from_dict(
                componentsschemas_list_of_double_range_value_item_data
            )

            ranges.append(componentsschemas_list_of_double_range_value_item)

        _sub_aggregations = d.pop("subAggregations", UNSET)
        sub_aggregations: Union[Unset, MapToAggregationQuery]
        if isinstance(_sub_aggregations, Unset):
            sub_aggregations = UNSET
        else:
            sub_aggregations = MapToAggregationQuery.from_dict(_sub_aggregations)

        range_aggregation_query_params = cls(
            ranges=ranges,
            sub_aggregations=sub_aggregations,
        )

        range_aggregation_query_params.additional_properties = d
        return range_aggregation_query_params

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
