from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_order_e import AggregationOrderE
    from ..models.map_to_aggregation_query import MapToAggregationQuery


T = TypeVar("T", bound="TermsAggregationQueryParams")


@_attrs_define
class TermsAggregationQueryParams:
    """Defines parameters to run an aggregation of type "Terms" (a multi-bucket-aggregation).
    <br>
     This aggregation query allows sub-aggregations.

        Attributes:
            use_shard_size_multiplier (Union[Unset, bool]): Each aggregation will run separately on each requested shard.
                The terms aggregations shardSize
                 parameter indicates the number of term buckets each shard will return to the coordinating node.
                 The coordinating node will compute the result buckets with size = "size".<br>
                 To get more accurate results, the terms aggregation fetches more than the top size terms from
                 each shard. It fetches the top shard_size terms, which defaults to size * 1.5 + 10.<br>
                 See also ES documentation:
                 https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-
                aggregation.html#search-aggregations-bucket-terms-aggregation-shard-size
                 <br>
                 This parameter enables providing an alternative multiplier than 1.5<br>
                 Provide this multiplier in field shardSizeMultiplier.<br>
            size (Union[Unset, int]): By default, the terms aggregation returns the top ten terms.
                <br>
                 Use the size parameter to return more terms, up to the search.max_buckets limit.<br>
                 This value must be greater than zero.
            shard_size_multiplier (Union[Unset, int]): Each aggregation will run separately on each requested shard.
                The shardSize parameter indicates
                 the number of term buckets each shard will return to the coordinating node, which will compute
                 the result buckets.<br>
                 To get more accurate results, the terms aggregation fetches more than the top size terms from
                 each shard. It fetches the top shard_size terms, which defaults to size * 1.5 + 10.<br>
                 <br>
                 If useShardSizeMultiplier equals to true, this parameter must contain the multiplier replacing
                 the value 1.5 in above term. The provided value must be greater or equal 1.<br>
                 The resulting term applied is: size * shardSizeMultiplier + 10
            missing_value (Union[Unset, str]): The missing parameter defines how documents that are missing a value should
                be treated.
                By
                 default they will be ignored but it is also possible to treat them as if they had a value.
                 Note: At ELO this is (regarding terms aggregations) currently only supported for string-based
                 values.
            sub_aggregations (Union[Unset, MapToAggregationQuery]):
            order (Union[Unset, AggregationOrderE]): Sort options for ElasticSearch.
                <br>
                 <br>
                 By default, the terms aggregation orders terms by descending document _count. The date_histogram
                 aggregation, however, sorts buckets by default by their key ascending.<br>
                 Use the order parameter to specify a different sort order.<br>
                 <br>
                 We do not offer some sort order types if it is not guaranteed to produce reasonable results. E.g.
                 Due to the way the terms aggregation gets terms from shards, sorting by ascending doc count often
                 produces inaccurate results.<br>
    """

    use_shard_size_multiplier: Union[Unset, bool] = UNSET
    size: Union[Unset, int] = UNSET
    shard_size_multiplier: Union[Unset, int] = UNSET
    missing_value: Union[Unset, str] = UNSET
    sub_aggregations: Union[Unset, "MapToAggregationQuery"] = UNSET
    order: Union[Unset, "AggregationOrderE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_shard_size_multiplier = self.use_shard_size_multiplier

        size = self.size

        shard_size_multiplier = self.shard_size_multiplier

        missing_value = self.missing_value

        sub_aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_aggregations, Unset):
            sub_aggregations = self.sub_aggregations.to_dict()

        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_shard_size_multiplier is not UNSET:
            field_dict["useShardSizeMultiplier"] = use_shard_size_multiplier
        if size is not UNSET:
            field_dict["size"] = size
        if shard_size_multiplier is not UNSET:
            field_dict["shardSizeMultiplier"] = shard_size_multiplier
        if missing_value is not UNSET:
            field_dict["missingValue"] = missing_value
        if sub_aggregations is not UNSET:
            field_dict["subAggregations"] = sub_aggregations
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_order_e import AggregationOrderE
        from ..models.map_to_aggregation_query import MapToAggregationQuery

        d = src_dict.copy()
        use_shard_size_multiplier = d.pop("useShardSizeMultiplier", UNSET)

        size = d.pop("size", UNSET)

        shard_size_multiplier = d.pop("shardSizeMultiplier", UNSET)

        missing_value = d.pop("missingValue", UNSET)

        _sub_aggregations = d.pop("subAggregations", UNSET)
        sub_aggregations: Union[Unset, MapToAggregationQuery]
        if isinstance(_sub_aggregations, Unset):
            sub_aggregations = UNSET
        else:
            sub_aggregations = MapToAggregationQuery.from_dict(_sub_aggregations)

        _order = d.pop("order", UNSET)
        order: Union[Unset, AggregationOrderE]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = AggregationOrderE.from_dict(_order)

        terms_aggregation_query_params = cls(
            use_shard_size_multiplier=use_shard_size_multiplier,
            size=size,
            shard_size_multiplier=shard_size_multiplier,
            missing_value=missing_value,
            sub_aggregations=sub_aggregations,
            order=order,
        )

        terms_aggregation_query_params.additional_properties = d
        return terms_aggregation_query_params

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
