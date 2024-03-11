from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateRelative")


@_attrs_define
class DateRelative:
    """<p>
    Provides relative time differences for DateNowValues.
     </p>
     <p>
     If a range query into the past or future is performed, is defined if the biggest delivered value is positive or
     negative.<br>
     e.g.: If <code>year=0, month=-2</code>, a range query from now to two months into the past is performed.<br>
     e.g.: If <code>year=0, month=-2, days=10</code>, a range query from now to one month, 20 days into the past is
     performed.<br>
     </p>

        Attributes:
            year (Union[Unset, int]): <p>
                Time shift for years.
                 </p>

                 example: -3 means three years to the past. 3 means three years to the future.
            month (Union[Unset, int]): <p>
                Time shift for months.
                 </p>

                 example: -3 means three months to the past. 3 means three months to the future.
            day (Union[Unset, int]): <p>
                Time shift for days.
                 </p>

                 example: -3 means three days to the past. 3 means three days to the future.
            hour (Union[Unset, int]): <p>
                Time shift for hours.
                 </p>

                 example: -3 means three hours to the past. 3 means three hours to the future.
            minute (Union[Unset, int]): <p>
                Time shift for minutes.
                 </p>

                 example: -3 means three minutes to the past. 3 means three minutes to the future.
    """

    year: Union[Unset, int] = UNSET
    month: Union[Unset, int] = UNSET
    day: Union[Unset, int] = UNSET
    hour: Union[Unset, int] = UNSET
    minute: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year
        month = self.month
        day = self.day
        hour = self.hour
        minute = self.minute

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        date_relative = cls(
            year=year,
            month=month,
            day=day,
            hour=hour,
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
