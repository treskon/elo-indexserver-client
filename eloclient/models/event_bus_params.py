from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventBusParams")


@_attrs_define
class EventBusParams:
    """This class supplies params to control the creation of an event bus ID.
    Only one of the members ticket, userId and
     channelId should be set.

        Attributes:
            ticket (Union[Unset, str]): Create event bus ID based on this ticket.
            user_id (Union[Unset, str]): Get the event bus ID for this user. A numeric ID, GUID or user name can be
                specified.
                The returned bus ID is
                 computed as EventBusC.BUSID_USER + uid, where uid is the numeric user ID.
            channel_id (Union[Unset, str]): Create an event bus ID based on this string. An arbitary string can be supplied.
            no_forward_to_other_ixs (Union[Unset, bool]): Do not open this bus on other Indexservers.
                In load balancing environments, event busses are opened on each
                 Indexserver by default. Set this option to true to open this event bus only on the currently attached
                Indexserver.
    """

    ticket: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    no_forward_to_other_ixs: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ticket = self.ticket
        user_id = self.user_id
        channel_id = self.channel_id
        no_forward_to_other_ixs = self.no_forward_to_other_ixs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if no_forward_to_other_ixs is not UNSET:
            field_dict["noForwardToOtherIxs"] = no_forward_to_other_ixs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ticket = d.pop("ticket", UNSET)

        user_id = d.pop("userId", UNSET)

        channel_id = d.pop("channelId", UNSET)

        no_forward_to_other_ixs = d.pop("noForwardToOtherIxs", UNSET)

        event_bus_params = cls(
            ticket=ticket,
            user_id=user_id,
            channel_id=channel_id,
            no_forward_to_other_ixs=no_forward_to_other_ixs,
        )

        event_bus_params.additional_properties = d
        return event_bus_params

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
