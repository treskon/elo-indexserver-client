from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarIntervalE")


@_attrs_define
class CalendarIntervalE:
    """Types of calendar intervals used for AggregationQuery of type DATE_HISTOGRAM.
    <br>
     Note: The value NONE exists only to check if this mandatory parameter is given, since API
     serialization may deliver always the first enum value.

        Attributes:
            month (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            quarter (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            year (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            hour (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            minute (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            none (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            week (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
            day (Union[Unset, CalendarIntervalE]): Types of calendar intervals used for AggregationQuery of type
                DATE_HISTOGRAM.
                <br>
                 Note: The value NONE exists only to check if this mandatory parameter is given, since API
                 serialization may deliver always the first enum value.
    """

    month: Union[Unset, "CalendarIntervalE"] = UNSET
    quarter: Union[Unset, "CalendarIntervalE"] = UNSET
    year: Union[Unset, "CalendarIntervalE"] = UNSET
    hour: Union[Unset, "CalendarIntervalE"] = UNSET
    minute: Union[Unset, "CalendarIntervalE"] = UNSET
    none: Union[Unset, "CalendarIntervalE"] = UNSET
    week: Union[Unset, "CalendarIntervalE"] = UNSET
    day: Union[Unset, "CalendarIntervalE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        month: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.month, Unset):
            month = self.month.to_dict()

        quarter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quarter, Unset):
            quarter = self.quarter.to_dict()

        year: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.year, Unset):
            year = self.year.to_dict()

        hour: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hour, Unset):
            hour = self.hour.to_dict()

        minute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.minute, Unset):
            minute = self.minute.to_dict()

        none: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.none, Unset):
            none = self.none.to_dict()

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        day: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month is not UNSET:
            field_dict["MONTH"] = month
        if quarter is not UNSET:
            field_dict["QUARTER"] = quarter
        if year is not UNSET:
            field_dict["YEAR"] = year
        if hour is not UNSET:
            field_dict["HOUR"] = hour
        if minute is not UNSET:
            field_dict["MINUTE"] = minute
        if none is not UNSET:
            field_dict["NONE"] = none
        if week is not UNSET:
            field_dict["WEEK"] = week
        if day is not UNSET:
            field_dict["DAY"] = day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _month = d.pop("MONTH", UNSET)
        month: Union[Unset, CalendarIntervalE]
        if isinstance(_month, Unset):
            month = UNSET
        else:
            month = CalendarIntervalE.from_dict(_month)

        _quarter = d.pop("QUARTER", UNSET)
        quarter: Union[Unset, CalendarIntervalE]
        if isinstance(_quarter, Unset):
            quarter = UNSET
        else:
            quarter = CalendarIntervalE.from_dict(_quarter)

        _year = d.pop("YEAR", UNSET)
        year: Union[Unset, CalendarIntervalE]
        if isinstance(_year, Unset):
            year = UNSET
        else:
            year = CalendarIntervalE.from_dict(_year)

        _hour = d.pop("HOUR", UNSET)
        hour: Union[Unset, CalendarIntervalE]
        if isinstance(_hour, Unset):
            hour = UNSET
        else:
            hour = CalendarIntervalE.from_dict(_hour)

        _minute = d.pop("MINUTE", UNSET)
        minute: Union[Unset, CalendarIntervalE]
        if isinstance(_minute, Unset):
            minute = UNSET
        else:
            minute = CalendarIntervalE.from_dict(_minute)

        _none = d.pop("NONE", UNSET)
        none: Union[Unset, CalendarIntervalE]
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = CalendarIntervalE.from_dict(_none)

        _week = d.pop("WEEK", UNSET)
        week: Union[Unset, CalendarIntervalE]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = CalendarIntervalE.from_dict(_week)

        _day = d.pop("DAY", UNSET)
        day: Union[Unset, CalendarIntervalE]
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = CalendarIntervalE.from_dict(_day)

        calendar_interval_e = cls(
            month=month,
            quarter=quarter,
            year=year,
            hour=hour,
            minute=minute,
            none=none,
            week=week,
            day=day,
        )

        calendar_interval_e.additional_properties = d
        return calendar_interval_e

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
