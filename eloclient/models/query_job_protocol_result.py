from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_job_protocol_event import QueryJobProtocolEvent


T = TypeVar("T", bound="QueryJobProtocolResult")


@_attrs_define
class QueryJobProtocolResult:
    """<p>
    This class contains the results from querying the protocol of a background thread.
     </p>

        Attributes:
            download_url (Union[Unset, str]): This String contains a URL where the whole protocol can be downloaded.
                Empty, if no protocol
                 file exists.
            events (Union[Unset, List['QueryJobProtocolEvent']]):
    """

    download_url: Union[Unset, str] = UNSET
    events: Union[Unset, List["QueryJobProtocolEvent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        download_url = self.download_url

        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_job_protocol_event import QueryJobProtocolEvent

        d = src_dict.copy()
        download_url = d.pop("downloadUrl", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = QueryJobProtocolEvent.from_dict(events_item_data)

            events.append(events_item)

        query_job_protocol_result = cls(
            download_url=download_url,
            events=events,
        )

        query_job_protocol_result.additional_properties = d
        return query_job_protocol_result

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
