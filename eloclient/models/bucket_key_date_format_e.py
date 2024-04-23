from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BucketKeyDateFormatE")


@_attrs_define
class BucketKeyDateFormatE:
    """Date formats of the bucket key in return buckets of aggregations of type DATE_HISTOGRAM and
    DATE_RANGE.

        Attributes:
            elo_iso_date_format_year (Union[Unset, BucketKeyDateFormatE]): Date formats of the bucket key in return buckets
                of aggregations of type DATE_HISTOGRAM and
                DATE_RANGE.
            elo_iso_date_format_day (Union[Unset, BucketKeyDateFormatE]): Date formats of the bucket key in return buckets
                of aggregations of type DATE_HISTOGRAM and
                DATE_RANGE.
            elo_tstamp_format (Union[Unset, BucketKeyDateFormatE]): Date formats of the bucket key in return buckets of
                aggregations of type DATE_HISTOGRAM and
                DATE_RANGE.
            elo_iso_date_format_seconds (Union[Unset, BucketKeyDateFormatE]): Date formats of the bucket key in return
                buckets of aggregations of type DATE_HISTOGRAM and
                DATE_RANGE.
            elo_iso_date_format_millis (Union[Unset, BucketKeyDateFormatE]): Date formats of the bucket key in return
                buckets of aggregations of type DATE_HISTOGRAM and
                DATE_RANGE.
    """

    elo_iso_date_format_year: Union[Unset, "BucketKeyDateFormatE"] = UNSET
    elo_iso_date_format_day: Union[Unset, "BucketKeyDateFormatE"] = UNSET
    elo_tstamp_format: Union[Unset, "BucketKeyDateFormatE"] = UNSET
    elo_iso_date_format_seconds: Union[Unset, "BucketKeyDateFormatE"] = UNSET
    elo_iso_date_format_millis: Union[Unset, "BucketKeyDateFormatE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elo_iso_date_format_year: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.elo_iso_date_format_year, Unset):
            elo_iso_date_format_year = self.elo_iso_date_format_year.to_dict()

        elo_iso_date_format_day: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.elo_iso_date_format_day, Unset):
            elo_iso_date_format_day = self.elo_iso_date_format_day.to_dict()

        elo_tstamp_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.elo_tstamp_format, Unset):
            elo_tstamp_format = self.elo_tstamp_format.to_dict()

        elo_iso_date_format_seconds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.elo_iso_date_format_seconds, Unset):
            elo_iso_date_format_seconds = self.elo_iso_date_format_seconds.to_dict()

        elo_iso_date_format_millis: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.elo_iso_date_format_millis, Unset):
            elo_iso_date_format_millis = self.elo_iso_date_format_millis.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elo_iso_date_format_year is not UNSET:
            field_dict["ELO_ISO_DATE_FORMAT_YEAR"] = elo_iso_date_format_year
        if elo_iso_date_format_day is not UNSET:
            field_dict["ELO_ISO_DATE_FORMAT_DAY"] = elo_iso_date_format_day
        if elo_tstamp_format is not UNSET:
            field_dict["ELO_TSTAMP_FORMAT"] = elo_tstamp_format
        if elo_iso_date_format_seconds is not UNSET:
            field_dict["ELO_ISO_DATE_FORMAT_SECONDS"] = elo_iso_date_format_seconds
        if elo_iso_date_format_millis is not UNSET:
            field_dict["ELO_ISO_DATE_FORMAT_MILLIS"] = elo_iso_date_format_millis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _elo_iso_date_format_year = d.pop("ELO_ISO_DATE_FORMAT_YEAR", UNSET)
        elo_iso_date_format_year: Union[Unset, BucketKeyDateFormatE]
        if isinstance(_elo_iso_date_format_year, Unset):
            elo_iso_date_format_year = UNSET
        else:
            elo_iso_date_format_year = BucketKeyDateFormatE.from_dict(_elo_iso_date_format_year)

        _elo_iso_date_format_day = d.pop("ELO_ISO_DATE_FORMAT_DAY", UNSET)
        elo_iso_date_format_day: Union[Unset, BucketKeyDateFormatE]
        if isinstance(_elo_iso_date_format_day, Unset):
            elo_iso_date_format_day = UNSET
        else:
            elo_iso_date_format_day = BucketKeyDateFormatE.from_dict(_elo_iso_date_format_day)

        _elo_tstamp_format = d.pop("ELO_TSTAMP_FORMAT", UNSET)
        elo_tstamp_format: Union[Unset, BucketKeyDateFormatE]
        if isinstance(_elo_tstamp_format, Unset):
            elo_tstamp_format = UNSET
        else:
            elo_tstamp_format = BucketKeyDateFormatE.from_dict(_elo_tstamp_format)

        _elo_iso_date_format_seconds = d.pop("ELO_ISO_DATE_FORMAT_SECONDS", UNSET)
        elo_iso_date_format_seconds: Union[Unset, BucketKeyDateFormatE]
        if isinstance(_elo_iso_date_format_seconds, Unset):
            elo_iso_date_format_seconds = UNSET
        else:
            elo_iso_date_format_seconds = BucketKeyDateFormatE.from_dict(_elo_iso_date_format_seconds)

        _elo_iso_date_format_millis = d.pop("ELO_ISO_DATE_FORMAT_MILLIS", UNSET)
        elo_iso_date_format_millis: Union[Unset, BucketKeyDateFormatE]
        if isinstance(_elo_iso_date_format_millis, Unset):
            elo_iso_date_format_millis = UNSET
        else:
            elo_iso_date_format_millis = BucketKeyDateFormatE.from_dict(_elo_iso_date_format_millis)

        bucket_key_date_format_e = cls(
            elo_iso_date_format_year=elo_iso_date_format_year,
            elo_iso_date_format_day=elo_iso_date_format_day,
            elo_tstamp_format=elo_tstamp_format,
            elo_iso_date_format_seconds=elo_iso_date_format_seconds,
            elo_iso_date_format_millis=elo_iso_date_format_millis,
        )

        bucket_key_date_format_e.additional_properties = d
        return bucket_key_date_format_e

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
