from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubstitutionPeriod")


@_attrs_define
class SubstitutionPeriod:
    """A substitution period is used to define time periods for substitutions.
    <p>
     A substitution is automatically activated during a time period if
     {@link SubstitutionSettings#activatePeriodsAutomatically} is set to true.
     </p>
     <p>
     A time period always needs a start date, this date must not be in the past. The earliest start
     date is the current day to start a substitution immediately.<br>
     The end date can be set, then the last day of the substitution is the end date (inclusive). It
     can also be left empty to have an open end for a substitution.
     </p>
     <p>
     A active substitution based on a time period can only be disabled by deleting the corresponding
     SubstitutionPeriod.
     </p>

        Attributes:
            start_isodate (Union[Unset, str]): <p>
                Start date of a substitution period (inclusive)
                 </p>
                 <p>
                 A start date must always be set.
                 </p>
                 <p>
                 Date format must be either 'yyyyMMdd' or 'yyyyMMddHHmmss'. If only a date ('yyyyMMdd') is
                 provided, it is adjusted to 'yyyyMMdd000000' to match the beginning of a day.
                 <p>
                 <p>
                 Dates are always committed and returned in the client's time zone.
                 </p>
            substitution_guid (Union[Unset, str]): GUID of the corresponding {@link Substitution}. Read-only.
            end_isodate (Union[Unset, str]): <p>
                End date of a substitution period (inclusive).
                 </p>
                 <p>
                 If this value if empty, the substitution never ends.
                 </p>
                 <p>
                 Date format must be either 'yyyyMMdd' or 'yyyyMMddHHmmss'. If only a date ('yyyyMMdd') is
                 provided, it is adjusted to 'yyyyMMdd235959' to match the end of a day.
                 <p>
                 <p>
                 Dates are always committed and returned in the client's time zone.
                 </p>
    """

    start_isodate: Union[Unset, str] = UNSET
    substitution_guid: Union[Unset, str] = UNSET
    end_isodate: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_isodate = self.start_isodate

        substitution_guid = self.substitution_guid

        end_isodate = self.end_isodate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_isodate is not UNSET:
            field_dict["startIsodate"] = start_isodate
        if substitution_guid is not UNSET:
            field_dict["substitutionGuid"] = substitution_guid
        if end_isodate is not UNSET:
            field_dict["endIsodate"] = end_isodate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_isodate = d.pop("startIsodate", UNSET)

        substitution_guid = d.pop("substitutionGuid", UNSET)

        end_isodate = d.pop("endIsodate", UNSET)

        substitution_period = cls(
            start_isodate=start_isodate,
            substitution_guid=substitution_guid,
            end_isodate=end_isodate,
        )

        substitution_period.additional_properties = d
        return substitution_period

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
