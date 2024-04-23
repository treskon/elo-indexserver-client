from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryJobProtocolInfo")


@_attrs_define
class QueryJobProtocolInfo:
    """This class contains the parameters for the interface function
    {@link IXServicePortIF#queryJobProtocol(ClientInfo, QueryJobProtocolInfo)}.

        Attributes:
            job_guid (Union[Unset, str]): The GUID of the background thread to query the log informations. Mandatory.
            start_event_id (Union[Unset, int]): If the value of startEventId is &ge;0, only eventIds &ge; that value will be
                returned.
                Optional.
            level (Union[Unset, int]): Filter for the level of log messages.
                If set, it has to be one of
                 {@link QueryJobProtocolC#LOG_LEVEL_ERROR}, {@link QueryJobProtocolC#LOG_LEVEL_WARN}, or
                 {@link QueryJobProtocolC#LOG_LEVEL_INFO}. Multiple values can be set via the bit operation "|".
                 If not set, only messages of LOG_LEVEL_ERROR are returned.
            start_date_iso (Union[Unset, str]): Marks the earliest date at which log information has to be reported.
                As only cached values are
                 returned, the value is ignored, if the oldest cached log information is younger that that date.
                 Optional.
    """

    job_guid: Union[Unset, str] = UNSET
    start_event_id: Union[Unset, int] = UNSET
    level: Union[Unset, int] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_guid = self.job_guid

        start_event_id = self.start_event_id

        level = self.level

        start_date_iso = self.start_date_iso

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_guid is not UNSET:
            field_dict["jobGuid"] = job_guid
        if start_event_id is not UNSET:
            field_dict["startEventId"] = start_event_id
        if level is not UNSET:
            field_dict["level"] = level
        if start_date_iso is not UNSET:
            field_dict["startDateISO"] = start_date_iso

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_guid = d.pop("jobGuid", UNSET)

        start_event_id = d.pop("startEventId", UNSET)

        level = d.pop("level", UNSET)

        start_date_iso = d.pop("startDateISO", UNSET)

        query_job_protocol_info = cls(
            job_guid=job_guid,
            start_event_id=start_event_id,
            level=level,
            start_date_iso=start_date_iso,
        )

        query_job_protocol_info.additional_properties = d
        return query_job_protocol_info

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
