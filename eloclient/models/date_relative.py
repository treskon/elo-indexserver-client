from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateRelative")


@_attrs_define
class DateRelative:
    """<p>
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

        Attributes:
            month (Union[Unset, int]): <p>
                Time shift for months.
                 </p>

                 example: -3 means three months to the past. 3 means three months to the future.
            hour (Union[Unset, int]): <p>
                Time shift for hours.
                 </p>

                 example: -3 means three hours to the past. 3 means three hours to the future.
            year (Union[Unset, int]): <p>
                Time shift for years.
                 </p>

                 example: -3 means three years to the past. 3 means three years to the future.
            day (Union[Unset, int]): <p>
                Time shift for days.
                 </p>

                 example: -3 means three days to the past. 3 means three days to the future.
            minute (Union[Unset, int]): <p>
                Time shift for minutes.
                 </p>

                 example: -3 means three minutes to the past. 3 means three minutes to the future.
    """

    month: Union[Unset, int] = UNSET
    hour: Union[Unset, int] = UNSET
    year: Union[Unset, int] = UNSET
    day: Union[Unset, int] = UNSET
    minute: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        month = self.month

        hour = self.hour

        year = self.year

        day = self.day

        minute = self.minute

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month is not UNSET:
            field_dict["month"] = month
        if hour is not UNSET:
            field_dict["hour"] = hour
        if year is not UNSET:
            field_dict["year"] = year
        if day is not UNSET:
            field_dict["day"] = day
        if minute is not UNSET:
            field_dict["minute"] = minute

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        month = d.pop("month", UNSET)

        hour = d.pop("hour", UNSET)

        year = d.pop("year", UNSET)

        day = d.pop("day", UNSET)

        minute = d.pop("minute", UNSET)

        date_relative = cls(
            month=month,
            hour=hour,
            year=year,
            day=day,
            minute=minute,
        )

        date_relative.additional_properties = d
        return date_relative

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
