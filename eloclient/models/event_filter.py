from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventFilter")


@_attrs_define
class EventFilter:
    """This class describes an event filter.

    Attributes:
        bus_id (Union[Unset, str]): Event bus ID
        type (Union[Unset, str]): Event type.
            This must be one of the predefined event types or an application defined type with
             a larger value than EventBusC.EVENT_TYPE_MAX_SYSTEM.
        param1 (Union[Unset, str]): First event param. Optional. Depends on event type.
        param2 (Union[Unset, str]): Second event param. Optional. Depends on event type.
    """

    bus_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    param1: Union[Unset, str] = UNSET
    param2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bus_id = self.bus_id

        type = self.type

        param1 = self.param1

        param2 = self.param2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bus_id is not UNSET:
            field_dict["busId"] = bus_id
        if type is not UNSET:
            field_dict["type"] = type
        if param1 is not UNSET:
            field_dict["param1"] = param1
        if param2 is not UNSET:
            field_dict["param2"] = param2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bus_id = d.pop("busId", UNSET)

        type = d.pop("type", UNSET)

        param1 = d.pop("param1", UNSET)

        param2 = d.pop("param2", UNSET)

        event_filter = cls(
            bus_id=bus_id,
            type=type,
            param1=param1,
            param2=param2,
        )

        event_filter.additional_properties = d
        return event_filter

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
