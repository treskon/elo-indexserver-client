from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_order_e import AggregationOrderE
    from ..models.double_range_value import DoubleRangeValue
    from ..models.double_single_value import DoubleSingleValue
    from ..models.map_to_aggregation_query import MapToAggregationQuery


T = TypeVar("T", bound="HistogramAggregationQueryParams")


@_attrs_define
class HistogramAggregationQueryParams:
    """Defines parameters to run an aggregation of type "Histogram" on numeric values (a
    multi-bucket-aggregation).<br>
     This aggregation query allows sub-aggregations.

        Attributes:
            offset (Union[Unset, DoubleSingleValue]):
            min_doc_count (Union[Unset, int]): If minDocCount = 0, the response will fill gaps in the histogram with empty
                buckets.
                It is
                 possible to change that and request buckets with a higher minimum count by means of the
                 min_doc_count setting.<br>
                 We set the default to a value of 1, to not overload the client with tons of unwanted buckets.
            extended_bounds (Union[Unset, DoubleRangeValue]): <p>
                Class to commit a range filter of double values or specify a range aggregation.
                 </p>

                 <p>
                 To perform an open range query (e.g. from now to infinite), only submit either a value for from
                 or to
                 </p>
                 <p>
                 To perform a range aggregation, submit both from/to or at least from or to for each requested
                 bucket (e.g. [from 3.14 to 6.28] or [from 3.14 to infinite]). Note that this aggregation includes
                 the "from"-value and excludes the "to"-value for each range.
                 </p>
            missing_value (Union[Unset, DoubleSingleValue]):
            interval (Union[Unset, DoubleSingleValue]):
            hard_bounds (Union[Unset, DoubleRangeValue]): <p>
                Class to commit a range filter of double values or specify a range aggregation.
                 </p>

                 <p>
                 To perform an open range query (e.g. from now to infinite), only submit either a value for from
                 or to
                 </p>
                 <p>
                 To perform a range aggregation, submit both from/to or at least from or to for each requested
                 bucket (e.g. [from 3.14 to 6.28] or [from 3.14 to infinite]). Note that this aggregation includes
                 the "from"-value and excludes the "to"-value for each range.
                 </p>
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

    offset: Union[Unset, "DoubleSingleValue"] = UNSET
    min_doc_count: Union[Unset, int] = UNSET
    extended_bounds: Union[Unset, "DoubleRangeValue"] = UNSET
    missing_value: Union[Unset, "DoubleSingleValue"] = UNSET
    interval: Union[Unset, "DoubleSingleValue"] = UNSET
    hard_bounds: Union[Unset, "DoubleRangeValue"] = UNSET
    sub_aggregations: Union[Unset, "MapToAggregationQuery"] = UNSET
    order: Union[Unset, "AggregationOrderE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset.to_dict()

        min_doc_count = self.min_doc_count

        extended_bounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extended_bounds, Unset):
            extended_bounds = self.extended_bounds.to_dict()

        missing_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.missing_value, Unset):
            missing_value = self.missing_value.to_dict()

        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        hard_bounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hard_bounds, Unset):
            hard_bounds = self.hard_bounds.to_dict()

        sub_aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_aggregations, Unset):
            sub_aggregations = self.sub_aggregations.to_dict()

        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if min_doc_count is not UNSET:
            field_dict["minDocCount"] = min_doc_count
        if extended_bounds is not UNSET:
            field_dict["extendedBounds"] = extended_bounds
        if missing_value is not UNSET:
            field_dict["missingValue"] = missing_value
        if interval is not UNSET:
            field_dict["interval"] = interval
        if hard_bounds is not UNSET:
            field_dict["hardBounds"] = hard_bounds
        if sub_aggregations is not UNSET:
            field_dict["subAggregations"] = sub_aggregations
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_order_e import AggregationOrderE
        from ..models.double_range_value import DoubleRangeValue
        from ..models.double_single_value import DoubleSingleValue
        from ..models.map_to_aggregation_query import MapToAggregationQuery

        d = src_dict.copy()
        _offset = d.pop("offset", UNSET)
        offset: Union[Unset, DoubleSingleValue]
        if isinstance(_offset, Unset):
            offset = UNSET
        else:
            offset = DoubleSingleValue.from_dict(_offset)

        min_doc_count = d.pop("minDocCount", UNSET)

        _extended_bounds = d.pop("extendedBounds", UNSET)
        extended_bounds: Union[Unset, DoubleRangeValue]
        if isinstance(_extended_bounds, Unset):
            extended_bounds = UNSET
        else:
            extended_bounds = DoubleRangeValue.from_dict(_extended_bounds)

        _missing_value = d.pop("missingValue", UNSET)
        missing_value: Union[Unset, DoubleSingleValue]
        if isinstance(_missing_value, Unset):
            missing_value = UNSET
        else:
            missing_value = DoubleSingleValue.from_dict(_missing_value)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, DoubleSingleValue]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = DoubleSingleValue.from_dict(_interval)

        _hard_bounds = d.pop("hardBounds", UNSET)
        hard_bounds: Union[Unset, DoubleRangeValue]
        if isinstance(_hard_bounds, Unset):
            hard_bounds = UNSET
        else:
            hard_bounds = DoubleRangeValue.from_dict(_hard_bounds)

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

        histogram_aggregation_query_params = cls(
            offset=offset,
            min_doc_count=min_doc_count,
            extended_bounds=extended_bounds,
            missing_value=missing_value,
            interval=interval,
            hard_bounds=hard_bounds,
            sub_aggregations=sub_aggregations,
            order=order,
        )

        histogram_aggregation_query_params.additional_properties = d
        return histogram_aggregation_query_params

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
