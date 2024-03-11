from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcrWorker")


@_attrs_define
class OcrWorker:
    """This class is used to describe an OCR worker process.

    Attributes:
        bus_id (Union[Unset, str]): The worker process listens on this bus ID for events of type {@link
            EventBusC#EVENT_OCR_REQUEST}.
        subs_id (Union[Unset, str]): The worker process is identified by this subscriber ID on the event bus.
        state (Union[Unset, int]): Worker state.
        last_used (Union[Unset, str]): Reserved.
        reserved (Union[Unset, str]): Reserved.
    """

    bus_id: Union[Unset, str] = UNSET
    subs_id: Union[Unset, str] = UNSET
    state: Union[Unset, int] = UNSET
    last_used: Union[Unset, str] = UNSET
    reserved: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bus_id = self.bus_id
        subs_id = self.subs_id
        state = self.state
        last_used = self.last_used
        reserved = self.reserved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bus_id is not UNSET:
            field_dict["busId"] = bus_id
        if subs_id is not UNSET:
            field_dict["subsId"] = subs_id
        if state is not UNSET:
            field_dict["state"] = state
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if reserved is not UNSET:
            field_dict["reserved"] = reserved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bus_id = d.pop("busId", UNSET)

        subs_id = d.pop("subsId", UNSET)

        state = d.pop("state", UNSET)

        last_used = d.pop("lastUsed", UNSET)

        reserved = d.pop("reserved", UNSET)

        ocr_worker = cls(
            bus_id=bus_id,
            subs_id=subs_id,
            state=state,
            last_used=last_used,
            reserved=reserved,
        )

        ocr_worker.additional_properties = d
        return ocr_worker

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
