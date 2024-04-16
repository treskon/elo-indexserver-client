from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_order_e import AggregationOrderE
    from ..models.bucket_key_date_format_e import BucketKeyDateFormatE
    from ..models.calendar_interval_e import CalendarIntervalE
    from ..models.date_iso_value import DateIsoValue
    from ..models.date_range_value import DateRangeValue
    from ..models.date_relative import DateRelative
    from ..models.map_to_aggregation_query import MapToAggregationQuery


T = TypeVar("T", bound="DateHistogramAggregationQueryParams")


@_attrs_define
class DateHistogramAggregationQueryParams:
    """Defines parameters to run an aggregation of type "Date_Histogram" (a
    multi-bucket-aggregation).<br>
     This aggregation query allows sub-aggregations.

        Attributes:
            calendar_interval (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of
                type DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            offset (Union[Unset, DateRelative]): <p>
                Can be used in three cases with different meanings:
                 </p>
                 <br>
                 <p>
                 (1) Provides relative time differences for DateNowValues in search queries.
                 </p>
                 <p>
                 If a range query into the past or future is performed, is defined if the biggest delivered value
                 is positive or negative.<br>
                 e.g.: If <code>year=0, month=-2</code>, a range query from now to two months into the past is
                 performed.<br>
                 e.g.: If <code>year=0, month=-2, days=10</code>, a range query from now to one month, 20 days
                 into the past is performed.<br>
                 </p>
                 <br>
                 <p>
                 (2) Provides optional time offset for date histogram aggregations.
                 </p>
                 <p>
                 Here, the time unit must be smaller than the requested calendar interval unit and it is only one
                 field allowed which not equals to zero. So, you cannot add values with different units like in
                 search queries.<br>
                 e.g.: If the requested interval is "day", the offset unit can only be smaller than day, e.g.
                 "hour".
                 </p>
                 <br>
                 <p>
                 (3) Provides date math for optional "extended boundary" and "hard boundary" parameters for date
                 histogram aggregations.
                 </p>
                 <p>
                 Here, it is only one field allowed which not equals to zero. So, you cannot add values with
                 different units like in search queries.<br>
                 </p>
            min_doc_count (Union[Unset, int]): If minDocCount = 0, the response will fill gaps in the histogram with empty
                buckets.
                It is
                 possible change that and request buckets with a higher minimum count by means of the
                 min_doc_count setting.<br>
                 We set the default to a value of 1, to not overload the client with tons of unwanted buckets.
            bucket_key_date_format (Union[Unset, BucketKeyDateFormatE]): Date formats of the bucket key in return buckets of
                aggregations of type DATE_HISTOGRAM and
                DATE_RANGE.
            extended_bounds (Union[Unset, DateRangeValue]): <p>
                Perform a range query with date values.
                 </p>

                 <p>
                 Range queries for dates:<br>
                 <ul>
                 <li>If from contains a value for roundTo, it is always rounded down by roundTo.</li>
                 <li>If to contains a value for roundTo, it is always rounded up by roundTo.</li>
                 <li>If one of from or to is of type DateNowValue and contains a value for relative, it is always
                 ignored for range queries.</li>
                 <li>To perform an open range query (e.g. from now to infinite), only submit either a value for
                 from or to</li>
                 </ul>
                 </p>
            missing_value (Union[Unset, DateIsoValue]): <p>
                Class to commit a date value to iSearch via QueryFilter.
                 </p>
                 <p>
                 Date format: YYYYMMddHHmmss<br>
                 If less than 14 digits are commited, it is converted to a 14 digit numer, e.g.: "2017" ->
                 "20170101000000"
                 </p>
                 <p>
                 If roundTo is null, a search for an exact date is executed.
                 </p>
                 <p>
                 If roundTo is != null, DateIsoValue is converted to a Range query. From is dateIso rounded down,
                 To is dateIso rounded up.
                 </p>
                 <p>
                 <b>Example</b> <code>dateIso=2017, roundTo=DateRoundC.YEAR</code> results in From=01.01.2017
                 00:00:00, To=31.12.2017 23:59:59
                 </p>
                 <p>
                 The delivered date is converted to the time zone submitted in ClientInfo
                 </p>
            hard_bounds (Union[Unset, DateRangeValue]): <p>
                Perform a range query with date values.
                 </p>

                 <p>
                 Range queries for dates:<br>
                 <ul>
                 <li>If from contains a value for roundTo, it is always rounded down by roundTo.</li>
                 <li>If to contains a value for roundTo, it is always rounded up by roundTo.</li>
                 <li>If one of from or to is of type DateNowValue and contains a value for relative, it is always
                 ignored for range queries.</li>
                 <li>To perform an open range query (e.g. from now to infinite), only submit either a value for
                 from or to</li>
                 </ul>
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

    calendar_interval: Union[Unset, "CalendarIntervalE"] = UNSET
    offset: Union[Unset, "DateRelative"] = UNSET
    min_doc_count: Union[Unset, int] = UNSET
    bucket_key_date_format: Union[Unset, "BucketKeyDateFormatE"] = UNSET
    extended_bounds: Union[Unset, "DateRangeValue"] = UNSET
    missing_value: Union[Unset, "DateIsoValue"] = UNSET
    hard_bounds: Union[Unset, "DateRangeValue"] = UNSET
    sub_aggregations: Union[Unset, "MapToAggregationQuery"] = UNSET
    order: Union[Unset, "AggregationOrderE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        calendar_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.calendar_interval, Unset):
            calendar_interval = self.calendar_interval.to_dict()

        offset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset.to_dict()

        min_doc_count = self.min_doc_count

        bucket_key_date_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bucket_key_date_format, Unset):
            bucket_key_date_format = self.bucket_key_date_format.to_dict()

        extended_bounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extended_bounds, Unset):
            extended_bounds = self.extended_bounds.to_dict()

        missing_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.missing_value, Unset):
            missing_value = self.missing_value.to_dict()

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
        if calendar_interval is not UNSET:
            field_dict["calendarInterval"] = calendar_interval
        if offset is not UNSET:
            field_dict["offset"] = offset
        if min_doc_count is not UNSET:
            field_dict["minDocCount"] = min_doc_count
        if bucket_key_date_format is not UNSET:
            field_dict["bucketKeyDateFormat"] = bucket_key_date_format
        if extended_bounds is not UNSET:
            field_dict["extendedBounds"] = extended_bounds
        if missing_value is not UNSET:
            field_dict["missingValue"] = missing_value
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
        from ..models.bucket_key_date_format_e import BucketKeyDateFormatE
        from ..models.calendar_interval_e import CalendarIntervalE
        from ..models.date_iso_value import DateIsoValue
        from ..models.date_range_value import DateRangeValue
        from ..models.date_relative import DateRelative
        from ..models.map_to_aggregation_query import MapToAggregationQuery

        d = src_dict.copy()
        _calendar_interval = d.pop("calendarInterval", UNSET)
        calendar_interval: Union[Unset, CalendarIntervalE]
        if isinstance(_calendar_interval, Unset):
            calendar_interval = UNSET
        else:
            calendar_interval = CalendarIntervalE.from_dict(_calendar_interval)

        _offset = d.pop("offset", UNSET)
        offset: Union[Unset, DateRelative]
        if isinstance(_offset, Unset):
            offset = UNSET
        else:
            offset = DateRelative.from_dict(_offset)

        min_doc_count = d.pop("minDocCount", UNSET)

        _bucket_key_date_format = d.pop("bucketKeyDateFormat", UNSET)
        bucket_key_date_format: Union[Unset, BucketKeyDateFormatE]
        if isinstance(_bucket_key_date_format, Unset):
            bucket_key_date_format = UNSET
        else:
            bucket_key_date_format = BucketKeyDateFormatE.from_dict(_bucket_key_date_format)

        _extended_bounds = d.pop("extendedBounds", UNSET)
        extended_bounds: Union[Unset, DateRangeValue]
        if isinstance(_extended_bounds, Unset):
            extended_bounds = UNSET
        else:
            extended_bounds = DateRangeValue.from_dict(_extended_bounds)

        _missing_value = d.pop("missingValue", UNSET)
        missing_value: Union[Unset, DateIsoValue]
        if isinstance(_missing_value, Unset):
            missing_value = UNSET
        else:
            missing_value = DateIsoValue.from_dict(_missing_value)

        _hard_bounds = d.pop("hardBounds", UNSET)
        hard_bounds: Union[Unset, DateRangeValue]
        if isinstance(_hard_bounds, Unset):
            hard_bounds = UNSET
        else:
            hard_bounds = DateRangeValue.from_dict(_hard_bounds)

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

        date_histogram_aggregation_query_params = cls(
            calendar_interval=calendar_interval,
            offset=offset,
            min_doc_count=min_doc_count,
            bucket_key_date_format=bucket_key_date_format,
            extended_bounds=extended_bounds,
            missing_value=missing_value,
            hard_bounds=hard_bounds,
            sub_aggregations=sub_aggregations,
            order=order,
        )

        date_histogram_aggregation_query_params.additional_properties = d
        return date_histogram_aggregation_query_params

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
