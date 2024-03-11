from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryJobProtocolEvent")


@_attrs_define
class QueryJobProtocolEvent:
    """<p>
    A {@link QueryJobProtocolEvent} represents a event
     </p>

        Attributes:
            date (Union[Unset, str]): The time of generating this event.
            message (Union[Unset, str]): Message of this LogRow.
            level (Union[Unset, int]): The level of log messages to query. Use the | operator to select multiple levels.
            obj_id (Union[Unset, int]): The id of the object currently being processed at the time of this events creation.
                If the objId is not
                 known/available, its value is set to {@link QueryJobProtocolC#OBJID_NOT_SET}.
            event_id (Union[Unset, int]): The id of this QueryJobProtocolEvent. The eventId's value is unique for one
                background thread.
                The value of a
                 background thread's first eventId is 0. The second one is 1 and so on.
    """

    date: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    obj_id: Union[Unset, int] = UNSET
    event_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        message = self.message
        level = self.level
        obj_id = self.obj_id
        event_id = self.event_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if message is not UNSET:
            field_dict["message"] = message
        if level is not UNSET:
            field_dict["level"] = level
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        message = d.pop("message", UNSET)

        level = d.pop("level", UNSET)

        obj_id = d.pop("objId", UNSET)

        event_id = d.pop("eventId", UNSET)

        query_job_protocol_event = cls(
            date=date,
            message=message,
            level=level,
            obj_id=obj_id,
            event_id=event_id,
        )

        query_job_protocol_event.additional_properties = d
        return query_job_protocol_event

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
