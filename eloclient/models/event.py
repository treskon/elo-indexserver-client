from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_ import Any


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """This class represents an event used by the event bus API functions.

    Attributes:
        bus_id (Union[Unset, str]): Bus-ID
        sender_id (Union[Unset, str]): User ID of event sender. Might be used for other IDs in future too. Read-only.
        data (Union[Unset, str]): Event payload data as byte array.
        id (Union[Unset, str]): Event ID.
            If the sender awaits a response to this event, it should set a random number in
             <code>id</code>. The receiver should use the same number in the response.
        acl (Union[Unset, str]): Access control list. An empty ACL means here, that the event is dispatched to everyone.
        type (Union[Unset, str]): Event type. Event filters check this value.
            This must be one of the predefined event types or
             an application defined type with a larger value than EventBusC.EVENT_TYPE_MAX_SYSTEM.
        any_ (Union[Unset, Any]): This class is a container for one value of a serializable type.
        param1 (Union[Unset, str]): Value depends on event type. Event filters check this value.
        param2 (Union[Unset, str]): Value depends on event type. Event filters check this value.
    """

    bus_id: Union[Unset, str] = UNSET
    sender_id: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    any_: Union[Unset, "Any"] = UNSET
    param1: Union[Unset, str] = UNSET
    param2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_ import Any

        bus_id = self.bus_id

        sender_id = self.sender_id

        data = self.data

        id = self.id

        acl = self.acl

        type = self.type

        any_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.any_, Unset):
            any_ = self.any_.to_dict()

        param1 = self.param1

        param2 = self.param2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bus_id is not UNSET:
            field_dict["busId"] = bus_id
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if acl is not UNSET:
            field_dict["acl"] = acl
        if type is not UNSET:
            field_dict["type"] = type
        if any_ is not UNSET:
            field_dict["any"] = any_
        if param1 is not UNSET:
            field_dict["param1"] = param1
        if param2 is not UNSET:
            field_dict["param2"] = param2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_ import Any

        d = src_dict.copy()
        bus_id = d.pop("busId", UNSET)

        sender_id = d.pop("senderId", UNSET)

        data = d.pop("data", UNSET)

        id = d.pop("id", UNSET)

        acl = d.pop("acl", UNSET)

        type = d.pop("type", UNSET)

        _any_ = d.pop("any", UNSET)
        any_: Union[Unset, Any]
        if isinstance(_any_, Unset):
            any_ = UNSET
        else:
            any_ = Any.from_dict(_any_)

        param1 = d.pop("param1", UNSET)

        param2 = d.pop("param2", UNSET)

        event = cls(
            bus_id=bus_id,
            sender_id=sender_id,
            data=data,
            id=id,
            acl=acl,
            type=type,
            any_=any_,
            param1=param1,
            param2=param2,
        )

        event.additional_properties = d
        return event

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
