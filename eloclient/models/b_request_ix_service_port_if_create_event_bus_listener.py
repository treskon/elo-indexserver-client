from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.event_listener import EventListener


T = TypeVar("T", bound="BRequestIXServicePortIFCreateEventBusListener")


@_attrs_define
class BRequestIXServicePortIFCreateEventBusListener:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        subs_id (Union[Unset, str]):
        event_listener (Union[Unset, EventListener]): This class describes an event bus listener.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    subs_id: Union[Unset, str] = UNSET
    event_listener: Union[Unset, "EventListener"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        subs_id = self.subs_id
        event_listener: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_listener, Unset):
            event_listener = self.event_listener.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if subs_id is not UNSET:
            field_dict["subsId"] = subs_id
        if event_listener is not UNSET:
            field_dict["eventListener"] = event_listener

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.event_listener import EventListener

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        subs_id = d.pop("subsId", UNSET)

        _event_listener = d.pop("eventListener", UNSET)
        event_listener: Union[Unset, EventListener]
        if isinstance(_event_listener, Unset):
            event_listener = UNSET
        else:
            event_listener = EventListener.from_dict(_event_listener)

        b_request_ix_service_port_if_create_event_bus_listener = cls(
            ci=ci,
            subs_id=subs_id,
            event_listener=event_listener,
        )

        b_request_ix_service_port_if_create_event_bus_listener.additional_properties = d
        return b_request_ix_service_port_if_create_event_bus_listener

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
