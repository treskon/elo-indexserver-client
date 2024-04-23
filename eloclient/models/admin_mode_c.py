from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminModeC")


@_attrs_define
class AdminModeC:
    """Constants for the administration mode.

    Attributes:
        query (Union[Unset, int]): Query administration mode
        off (Union[Unset, int]): Administration mode is inactive
        on (Union[Unset, int]): Administration mode is active
    """

    query: Union[Unset, int] = UNSET
    off: Union[Unset, int] = UNSET
    on: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        off = self.off

        on = self.on

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["QUERY"] = query
        if off is not UNSET:
            field_dict["OFF"] = off
        if on is not UNSET:
            field_dict["ON"] = on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("QUERY", UNSET)

        off = d.pop("OFF", UNSET)

        on = d.pop("ON", UNSET)

        admin_mode_c = cls(
            query=query,
            off=off,
            on=on,
        )

        admin_mode_c.additional_properties = d
        return admin_mode_c

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
