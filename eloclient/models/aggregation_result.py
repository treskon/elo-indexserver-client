from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_type_e import AggregationTypeE
    from ..models.date_histogram_aggregation_result import DateHistogramAggregationResult
    from ..models.filter_aggregation_result import FilterAggregationResult
    from ..models.histogram_aggregation_result import HistogramAggregationResult
    from ..models.range_aggregation_result import RangeAggregationResult
    from ..models.single_value_metrics_aggregation_result import SingleValueMetricsAggregationResult
    from ..models.terms_aggregation_result import TermsAggregationResult
    from ..models.value_count_aggregation_result import ValueCountAggregationResult


T = TypeVar("T", bound="AggregationResult")


@_attrs_define
class AggregationResult:
    """Return object for AggregationQueries.
    <br>
     Consists of name and type and a type specific part. This type specific part contains actual
     results according to its AggregationType.<br>
     Hence, in each instance of AggregationResult is only one type specific part valid. All other
     parts are not valid and equal to null.

        Attributes:
            histogram_result (Union[Unset, HistogramAggregationResult]): The result object of a histogram aggregation on
                numeric values.
                <br>
                 It consists mainly of buckets and within its inner aggregations results (sub-aggregations).
            single_value_metrics_result (Union[Unset, SingleValueMetricsAggregationResult]): The result object of a single-
                value-metrics aggregation.
                <br>
                 It consists mainly of a result value.<br>
            value_count_result (Union[Unset, ValueCountAggregationResult]): The result object of a value_count aggregation.
                <br>
                 It consists mainly of a result value.<br>
            filter_result (Union[Unset, FilterAggregationResult]): The result object of a filter aggregation.
                <br>
                 It consists mainly of inner aggregations results (sub-aggregations).
            terms_result (Union[Unset, TermsAggregationResult]): The result object of a terms aggregation.
                <br>
                 It consists mainly of buckets and within its inner aggregations results (sub-aggregations).
            name (Union[Unset, str]): Name of the aggregation.
            type (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
            range_result (Union[Unset, RangeAggregationResult]): The result object of a range aggregation.
                <br>
                 It consists mainly of buckets and within its inner aggregations results (sub-aggregations).
            date_histogram_result (Union[Unset, DateHistogramAggregationResult]): The result object of a date_histogram
                aggregation.
                <br>
                 It consists mainly of buckets and within its inner aggregations results (sub-aggregations).
    """

    histogram_result: Union[Unset, "HistogramAggregationResult"] = UNSET
    single_value_metrics_result: Union[Unset, "SingleValueMetricsAggregationResult"] = UNSET
    value_count_result: Union[Unset, "ValueCountAggregationResult"] = UNSET
    filter_result: Union[Unset, "FilterAggregationResult"] = UNSET
    terms_result: Union[Unset, "TermsAggregationResult"] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, "AggregationTypeE"] = UNSET
    range_result: Union[Unset, "RangeAggregationResult"] = UNSET
    date_histogram_result: Union[Unset, "DateHistogramAggregationResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        histogram_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.histogram_result, Unset):
            histogram_result = self.histogram_result.to_dict()

        single_value_metrics_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.single_value_metrics_result, Unset):
            single_value_metrics_result = self.single_value_metrics_result.to_dict()

        value_count_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_count_result, Unset):
            value_count_result = self.value_count_result.to_dict()

        filter_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_result, Unset):
            filter_result = self.filter_result.to_dict()

        terms_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terms_result, Unset):
            terms_result = self.terms_result.to_dict()

        name = self.name

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        range_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_result, Unset):
            range_result = self.range_result.to_dict()

        date_histogram_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_histogram_result, Unset):
            date_histogram_result = self.date_histogram_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if histogram_result is not UNSET:
            field_dict["histogramResult"] = histogram_result
        if single_value_metrics_result is not UNSET:
            field_dict["singleValueMetricsResult"] = single_value_metrics_result
        if value_count_result is not UNSET:
            field_dict["valueCountResult"] = value_count_result
        if filter_result is not UNSET:
            field_dict["filterResult"] = filter_result
        if terms_result is not UNSET:
            field_dict["termsResult"] = terms_result
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if range_result is not UNSET:
            field_dict["rangeResult"] = range_result
        if date_histogram_result is not UNSET:
            field_dict["dateHistogramResult"] = date_histogram_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_type_e import AggregationTypeE
        from ..models.date_histogram_aggregation_result import DateHistogramAggregationResult
        from ..models.filter_aggregation_result import FilterAggregationResult
        from ..models.histogram_aggregation_result import HistogramAggregationResult
        from ..models.range_aggregation_result import RangeAggregationResult
        from ..models.single_value_metrics_aggregation_result import SingleValueMetricsAggregationResult
        from ..models.terms_aggregation_result import TermsAggregationResult
        from ..models.value_count_aggregation_result import ValueCountAggregationResult

        d = src_dict.copy()
        _histogram_result = d.pop("histogramResult", UNSET)
        histogram_result: Union[Unset, HistogramAggregationResult]
        if isinstance(_histogram_result, Unset):
            histogram_result = UNSET
        else:
            histogram_result = HistogramAggregationResult.from_dict(_histogram_result)

        _single_value_metrics_result = d.pop("singleValueMetricsResult", UNSET)
        single_value_metrics_result: Union[Unset, SingleValueMetricsAggregationResult]
        if isinstance(_single_value_metrics_result, Unset):
            single_value_metrics_result = UNSET
        else:
            single_value_metrics_result = SingleValueMetricsAggregationResult.from_dict(_single_value_metrics_result)

        _value_count_result = d.pop("valueCountResult", UNSET)
        value_count_result: Union[Unset, ValueCountAggregationResult]
        if isinstance(_value_count_result, Unset):
            value_count_result = UNSET
        else:
            value_count_result = ValueCountAggregationResult.from_dict(_value_count_result)

        _filter_result = d.pop("filterResult", UNSET)
        filter_result: Union[Unset, FilterAggregationResult]
        if isinstance(_filter_result, Unset):
            filter_result = UNSET
        else:
            filter_result = FilterAggregationResult.from_dict(_filter_result)

        _terms_result = d.pop("termsResult", UNSET)
        terms_result: Union[Unset, TermsAggregationResult]
        if isinstance(_terms_result, Unset):
            terms_result = UNSET
        else:
            terms_result = TermsAggregationResult.from_dict(_terms_result)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AggregationTypeE]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AggregationTypeE.from_dict(_type)

        _range_result = d.pop("rangeResult", UNSET)
        range_result: Union[Unset, RangeAggregationResult]
        if isinstance(_range_result, Unset):
            range_result = UNSET
        else:
            range_result = RangeAggregationResult.from_dict(_range_result)

        _date_histogram_result = d.pop("dateHistogramResult", UNSET)
        date_histogram_result: Union[Unset, DateHistogramAggregationResult]
        if isinstance(_date_histogram_result, Unset):
            date_histogram_result = UNSET
        else:
            date_histogram_result = DateHistogramAggregationResult.from_dict(_date_histogram_result)

        aggregation_result = cls(
            histogram_result=histogram_result,
            single_value_metrics_result=single_value_metrics_result,
            value_count_result=value_count_result,
            filter_result=filter_result,
            terms_result=terms_result,
            name=name,
            type=type,
            range_result=range_result,
            date_histogram_result=date_histogram_result,
        )

        aggregation_result.additional_properties = d
        return aggregation_result

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
