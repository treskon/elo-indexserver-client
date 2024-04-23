from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_relative import DateRelative
    from ..models.date_round_e import DateRoundE


T = TypeVar("T", bound="DateNowValue")


@_attrs_define
class DateNowValue:
    """<p>
    Class to commit a time which refers to the current time.
     </p>
     <p>
     Depending on the committed values, different searches are performed:
     <ul>
     <li>If <code>roundTo == null</code> and <code>relative == null</code>, a search for the exact
     current times is performed.
     <li>If <code>roundTo != null</code> and <code>relative == null</code>, a range query is
     performed.<br>
     From is current time rounded down, To is current time rounded up, defined by
     <code>roundTo</code>.
     <li>If <code>relative != null</code>: A range query relative to current time is performed.<br>
     <ul>
     <li>If the biggest relative value is negative, a range query into the past is performed.<br>
     <code>From</code> is current time - <code>relative</code>, rounded down if
     <code>roundTo != null</code>. <code>To</code> is current time, rounded up if
     <code>roundTo != null</code>.
     <li>If the biggest relative value is positive, a range query into the future is performed.<br>
     <code>From</code> is current time, rounded down if <code>roundTo != null</code>. <code>To</code>
     is current time + <code>relative</code>, rounded to if <code>roundTo != null</code>.
     </ul>
     <p>
     The delivered date is converted to the time zone submitted in ClientInfo
     </p>
     </ul>

     <p>
     A time offset to UTC time can be delivered by <code>diffToUtc</code>.<br>
     {@link SearchFieldE#X_DATE}, {@link SearchFieldE#I_DATE}, {@link SearchFieldE#DELETED_DATE} and
     {@link SearchFieldE#TIMESTAMP} are converted to UTC prior to saving them, index lines in date
     format are not converted.<br>
     Therefore, a timezone should always be commited for these four.
     </p>

        Attributes:
            round_to (Union[Unset, DateRoundE]): <p>
                Enum for rounding DateValues.
                 </p>
                 It defines if a date should be rounded to year, month, day, hour or minute.
            relative (Union[Unset, DateRelative]): <p>
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
    """

    round_to: Union[Unset, "DateRoundE"] = UNSET
    relative: Union[Unset, "DateRelative"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        round_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.round_to, Unset):
            round_to = self.round_to.to_dict()

        relative: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relative, Unset):
            relative = self.relative.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if round_to is not UNSET:
            field_dict["roundTo"] = round_to
        if relative is not UNSET:
            field_dict["relative"] = relative

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_relative import DateRelative
        from ..models.date_round_e import DateRoundE

        d = src_dict.copy()
        _round_to = d.pop("roundTo", UNSET)
        round_to: Union[Unset, DateRoundE]
        if isinstance(_round_to, Unset):
            round_to = UNSET
        else:
            round_to = DateRoundE.from_dict(_round_to)

        _relative = d.pop("relative", UNSET)
        relative: Union[Unset, DateRelative]
        if isinstance(_relative, Unset):
            relative = UNSET
        else:
            relative = DateRelative.from_dict(_relative)

        date_now_value = cls(
            round_to=round_to,
            relative=relative,
        )

        date_now_value.additional_properties = d
        return date_now_value

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
