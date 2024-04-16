from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateRoundE")


@_attrs_define
class DateRoundE:
    """<p>
    Enum for rounding DateValues.
     </p>
     It defines if a date should be rounded to year, month, day, hour or minute.

        Attributes:
            month (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
            year (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
            hour (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
            minute (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
            none (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
            day (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
    """

    month: Union[Unset, "DateRoundE"] = UNSET
    year: Union[Unset, "DateRoundE"] = UNSET
    hour: Union[Unset, "DateRoundE"] = UNSET
    minute: Union[Unset, "DateRoundE"] = UNSET
    none: Union[Unset, "DateRoundE"] = UNSET
    day: Union[Unset, "DateRoundE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        month: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.month, Unset):
            month = self.month.to_dict()

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

        day: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month is not UNSET:
            field_dict["MONTH"] = month
        if year is not UNSET:
            field_dict["YEAR"] = year
        if hour is not UNSET:
            field_dict["HOUR"] = hour
        if minute is not UNSET:
            field_dict["MINUTE"] = minute
        if none is not UNSET:
            field_dict["NONE"] = none
        if day is not UNSET:
            field_dict["DAY"] = day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _month = d.pop("MONTH", UNSET)
        month: Union[Unset, DateRoundE]
        if isinstance(_month, Unset):
            month = UNSET
        else:
            month = DateRoundE.from_dict(_month)

        _year = d.pop("YEAR", UNSET)
        year: Union[Unset, DateRoundE]
        if isinstance(_year, Unset):
            year = UNSET
        else:
            year = DateRoundE.from_dict(_year)

        _hour = d.pop("HOUR", UNSET)
        hour: Union[Unset, DateRoundE]
        if isinstance(_hour, Unset):
            hour = UNSET
        else:
            hour = DateRoundE.from_dict(_hour)

        _minute = d.pop("MINUTE", UNSET)
        minute: Union[Unset, DateRoundE]
        if isinstance(_minute, Unset):
            minute = UNSET
        else:
            minute = DateRoundE.from_dict(_minute)

        _none = d.pop("NONE", UNSET)
        none: Union[Unset, DateRoundE]
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = DateRoundE.from_dict(_none)

        _day = d.pop("DAY", UNSET)
        day: Union[Unset, DateRoundE]
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = DateRoundE.from_dict(_day)

        date_round_e = cls(
            month=month,
            year=year,
            hour=hour,
            minute=minute,
            none=none,
            day=day,
        )

        date_round_e.additional_properties = d
        return date_round_e

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
