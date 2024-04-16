from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_round_e import DateRoundE


T = TypeVar("T", bound="DateIsoValue")


@_attrs_define
class DateIsoValue:
    """<p>
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

        Attributes:
            date_iso (Union[Unset, str]): <p>
                ISO-Date.
                 </p>

                 Number of digits defines kind of timeunit:
                 <ul>
                 <li>4 digits for year.
                 <li>6 digits for year with month.
                 <li>8 digits for date with days.
                 <li>10 digits for date with hours.
                 <li>12 digits for date with minutes.
                 <li>14 digits for date with seconds
                 </ul>
            round_to (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
    """

    date_iso: Union[Unset, str] = UNSET
    round_to: Union[Unset, "DateRoundE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_iso = self.date_iso

        round_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.round_to, Unset):
            round_to = self.round_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_iso is not UNSET:
            field_dict["dateIso"] = date_iso
        if round_to is not UNSET:
            field_dict["roundTo"] = round_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_round_e import DateRoundE

        d = src_dict.copy()
        date_iso = d.pop("dateIso", UNSET)

        _round_to = d.pop("roundTo", UNSET)
        round_to: Union[Unset, DateRoundE]
        if isinstance(_round_to, Unset):
            round_to = UNSET
        else:
            round_to = DateRoundE.from_dict(_round_to)

        date_iso_value = cls(
            date_iso=date_iso,
            round_to=round_to,
        )

        date_iso_value.additional_properties = d
        return date_iso_value

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
