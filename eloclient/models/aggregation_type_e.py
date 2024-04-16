from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationTypeE")


@_attrs_define
class AggregationTypeE:
    """Types of Aggregations for ESearch AggregationQuery.

    Attributes:
        avg (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        filter_ (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        min_ (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        max_ (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        terms (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        histogram (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        sum_ (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        date_histogram (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        value_count (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        range_ (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
    """

    avg: Union[Unset, "AggregationTypeE"] = UNSET
    filter_: Union[Unset, "AggregationTypeE"] = UNSET
    min_: Union[Unset, "AggregationTypeE"] = UNSET
    max_: Union[Unset, "AggregationTypeE"] = UNSET
    terms: Union[Unset, "AggregationTypeE"] = UNSET
    histogram: Union[Unset, "AggregationTypeE"] = UNSET
    sum_: Union[Unset, "AggregationTypeE"] = UNSET
    date_histogram: Union[Unset, "AggregationTypeE"] = UNSET
    value_count: Union[Unset, "AggregationTypeE"] = UNSET
    range_: Union[Unset, "AggregationTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.avg, Unset):
            avg = self.avg.to_dict()

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        min_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_.to_dict()

        max_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_.to_dict()

        terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        histogram: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.histogram, Unset):
            histogram = self.histogram.to_dict()

        sum_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sum_, Unset):
            sum_ = self.sum_.to_dict()

        date_histogram: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_histogram, Unset):
            date_histogram = self.date_histogram.to_dict()

        value_count: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_count, Unset):
            value_count = self.value_count.to_dict()

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg is not UNSET:
            field_dict["AVG"] = avg
        if filter_ is not UNSET:
            field_dict["FILTER"] = filter_
        if min_ is not UNSET:
            field_dict["MIN"] = min_
        if max_ is not UNSET:
            field_dict["MAX"] = max_
        if terms is not UNSET:
            field_dict["TERMS"] = terms
        if histogram is not UNSET:
            field_dict["HISTOGRAM"] = histogram
        if sum_ is not UNSET:
            field_dict["SUM"] = sum_
        if date_histogram is not UNSET:
            field_dict["DATE_HISTOGRAM"] = date_histogram
        if value_count is not UNSET:
            field_dict["VALUE_COUNT"] = value_count
        if range_ is not UNSET:
            field_dict["RANGE"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _avg = d.pop("AVG", UNSET)
        avg: Union[Unset, AggregationTypeE]
        if isinstance(_avg, Unset):
            avg = UNSET
        else:
            avg = AggregationTypeE.from_dict(_avg)

        _filter_ = d.pop("FILTER", UNSET)
        filter_: Union[Unset, AggregationTypeE]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = AggregationTypeE.from_dict(_filter_)

        _min_ = d.pop("MIN", UNSET)
        min_: Union[Unset, AggregationTypeE]
        if isinstance(_min_, Unset):
            min_ = UNSET
        else:
            min_ = AggregationTypeE.from_dict(_min_)

        _max_ = d.pop("MAX", UNSET)
        max_: Union[Unset, AggregationTypeE]
        if isinstance(_max_, Unset):
            max_ = UNSET
        else:
            max_ = AggregationTypeE.from_dict(_max_)

        _terms = d.pop("TERMS", UNSET)
        terms: Union[Unset, AggregationTypeE]
        if isinstance(_terms, Unset):
            terms = UNSET
        else:
            terms = AggregationTypeE.from_dict(_terms)

        _histogram = d.pop("HISTOGRAM", UNSET)
        histogram: Union[Unset, AggregationTypeE]
        if isinstance(_histogram, Unset):
            histogram = UNSET
        else:
            histogram = AggregationTypeE.from_dict(_histogram)

        _sum_ = d.pop("SUM", UNSET)
        sum_: Union[Unset, AggregationTypeE]
        if isinstance(_sum_, Unset):
            sum_ = UNSET
        else:
            sum_ = AggregationTypeE.from_dict(_sum_)

        _date_histogram = d.pop("DATE_HISTOGRAM", UNSET)
        date_histogram: Union[Unset, AggregationTypeE]
        if isinstance(_date_histogram, Unset):
            date_histogram = UNSET
        else:
            date_histogram = AggregationTypeE.from_dict(_date_histogram)

        _value_count = d.pop("VALUE_COUNT", UNSET)
        value_count: Union[Unset, AggregationTypeE]
        if isinstance(_value_count, Unset):
            value_count = UNSET
        else:
            value_count = AggregationTypeE.from_dict(_value_count)

        _range_ = d.pop("RANGE", UNSET)
        range_: Union[Unset, AggregationTypeE]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = AggregationTypeE.from_dict(_range_)

        aggregation_type_e = cls(
            avg=avg,
            filter_=filter_,
            min_=min_,
            max_=max_,
            terms=terms,
            histogram=histogram,
            sum_=sum_,
            date_histogram=date_histogram,
            value_count=value_count,
            range_=range_,
        )

        aggregation_type_e.additional_properties = d
        return aggregation_type_e

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
