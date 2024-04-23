from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_aggregation_query import MapToAggregationQuery


T = TypeVar("T", bound="AggregationOptions")


@_attrs_define
class AggregationOptions:
    """<p>
    Use this class if aggregations in general (i.e. not context terms) should be retrieved by
     {@link de.elo.ix.client.IXServicePortIF#findAggregations(de.elo.ix.client.ClientInfo, de.elo.ix.client.FindInfo,
    int)}.<br>
     The overall query is submitted by {@link de.elo.ix.client.esearch.ESearchParams}.
     </p>
     <p>
     Submit a map of AggregationQuerys to retrieve result aggregations for each of them.<br>
     </p>
     <p>
     The resulting list {@link ContextTermResults#contextTerms} is provided in the same order as the
     submitted list contextTermQueries
     </p>
     </p>

        Attributes:
            aggregation_queries (Union[Unset, MapToAggregationQuery]):
    """

    aggregation_queries: Union[Unset, "MapToAggregationQuery"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregation_queries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregation_queries, Unset):
            aggregation_queries = self.aggregation_queries.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_queries is not UNSET:
            field_dict["aggregationQueries"] = aggregation_queries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_aggregation_query import MapToAggregationQuery

        d = src_dict.copy()
        _aggregation_queries = d.pop("aggregationQueries", UNSET)
        aggregation_queries: Union[Unset, MapToAggregationQuery]
        if isinstance(_aggregation_queries, Unset):
            aggregation_queries = UNSET
        else:
            aggregation_queries = MapToAggregationQuery.from_dict(_aggregation_queries)

        aggregation_options = cls(
            aggregation_queries=aggregation_queries,
        )

        aggregation_options.additional_properties = d
        return aggregation_options

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
