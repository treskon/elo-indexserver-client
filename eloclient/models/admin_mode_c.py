from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminModeC")


@_attrs_define
class AdminModeC:
    """Constants for the administration mode.

    Attributes:
        on (Union[Unset, int]): Administration mode is active
        off (Union[Unset, int]): Administration mode is inactive
        query (Union[Unset, int]): Query administration mode
    """

    on: Union[Unset, int] = UNSET
    off: Union[Unset, int] = UNSET
    query: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        on = self.on
        off = self.off
        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on is not UNSET:
            field_dict["ON"] = on
        if off is not UNSET:
            field_dict["OFF"] = off
        if query is not UNSET:
            field_dict["QUERY"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        on = d.pop("ON", UNSET)

        off = d.pop("OFF", UNSET)

        query = d.pop("QUERY", UNSET)

        admin_mode_c = cls(
            on=on,
            off=off,
            query=query,
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
