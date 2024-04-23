from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_aggregation_query import MapToAggregationQuery
    from ..models.query_operator import QueryOperator


T = TypeVar("T", bound="FilterAggregationQueryParams")


@_attrs_define
class FilterAggregationQueryParams:
    """Defines parameters to run an aggregation of type "Filter" (a single-bucket-aggregation).
    <br>
     This aggregation query allows sub-aggregations and this is the main use case.

        Attributes:
            sub_aggregations (Union[Unset, MapToAggregationQuery]):
            query_operator (Union[Unset, QueryOperator]): A QueryOperator is used to include or exclude QueryObjects from a
                search and to concatenate
                QueryObjects.<br>
                 Like this, complex queries can be build.
    """

    sub_aggregations: Union[Unset, "MapToAggregationQuery"] = UNSET
    query_operator: Union[Unset, "QueryOperator"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_aggregations, Unset):
            sub_aggregations = self.sub_aggregations.to_dict()

        query_operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_operator, Unset):
            query_operator = self.query_operator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_aggregations is not UNSET:
            field_dict["subAggregations"] = sub_aggregations
        if query_operator is not UNSET:
            field_dict["queryOperator"] = query_operator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_aggregation_query import MapToAggregationQuery
        from ..models.query_operator import QueryOperator

        d = src_dict.copy()
        _sub_aggregations = d.pop("subAggregations", UNSET)
        sub_aggregations: Union[Unset, MapToAggregationQuery]
        if isinstance(_sub_aggregations, Unset):
            sub_aggregations = UNSET
        else:
            sub_aggregations = MapToAggregationQuery.from_dict(_sub_aggregations)

        _query_operator = d.pop("queryOperator", UNSET)
        query_operator: Union[Unset, QueryOperator]
        if isinstance(_query_operator, Unset):
            query_operator = UNSET
        else:
            query_operator = QueryOperator.from_dict(_query_operator)

        filter_aggregation_query_params = cls(
            sub_aggregations=sub_aggregations,
            query_operator=query_operator,
        )

        filter_aggregation_query_params.additional_properties = d
        return filter_aggregation_query_params

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
