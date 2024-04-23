from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcrWorkerC")


@_attrs_define
class OcrWorkerC:
    """
    Attributes:
        unregistered (Union[Unset, int]):
        busy (Union[Unset, int]):
        idle (Union[Unset, int]):
        registered (Union[Unset, int]):
        dead (Union[Unset, int]):
    """

    unregistered: Union[Unset, int] = UNSET
    busy: Union[Unset, int] = UNSET
    idle: Union[Unset, int] = UNSET
    registered: Union[Unset, int] = UNSET
    dead: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unregistered = self.unregistered

        busy = self.busy

        idle = self.idle

        registered = self.registered

        dead = self.dead

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unregistered is not UNSET:
            field_dict["UNREGISTERED"] = unregistered
        if busy is not UNSET:
            field_dict["BUSY"] = busy
        if idle is not UNSET:
            field_dict["IDLE"] = idle
        if registered is not UNSET:
            field_dict["REGISTERED"] = registered
        if dead is not UNSET:
            field_dict["DEAD"] = dead

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unregistered = d.pop("UNREGISTERED", UNSET)

        busy = d.pop("BUSY", UNSET)

        idle = d.pop("IDLE", UNSET)

        registered = d.pop("REGISTERED", UNSET)

        dead = d.pop("DEAD", UNSET)

        ocr_worker_c = cls(
            unregistered=unregistered,
            busy=busy,
            idle=idle,
            registered=registered,
            dead=dead,
        )

        ocr_worker_c.additional_properties = d
        return ocr_worker_c

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
