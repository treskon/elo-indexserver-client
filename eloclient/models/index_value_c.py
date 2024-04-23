from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexValueC")


@_attrs_define
class IndexValueC:
    """This class defines the constants for the type member in IndexValue.

    Attributes:
        type_status (Union[Unset, int]):
        type_user (Union[Unset, int]):
        type_relation (Union[Unset, int]):
        type_int (Union[Unset, int]):
        type_double (Union[Unset, int]):
        type_string (Union[Unset, int]):
        type_iso_date_time (Union[Unset, int]):
        type_iso_date_only (Union[Unset, int]):
    """

    type_status: Union[Unset, int] = UNSET
    type_user: Union[Unset, int] = UNSET
    type_relation: Union[Unset, int] = UNSET
    type_int: Union[Unset, int] = UNSET
    type_double: Union[Unset, int] = UNSET
    type_string: Union[Unset, int] = UNSET
    type_iso_date_time: Union[Unset, int] = UNSET
    type_iso_date_only: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_status = self.type_status

        type_user = self.type_user

        type_relation = self.type_relation

        type_int = self.type_int

        type_double = self.type_double

        type_string = self.type_string

        type_iso_date_time = self.type_iso_date_time

        type_iso_date_only = self.type_iso_date_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_status is not UNSET:
            field_dict["TYPE_STATUS"] = type_status
        if type_user is not UNSET:
            field_dict["TYPE_USER"] = type_user
        if type_relation is not UNSET:
            field_dict["TYPE_RELATION"] = type_relation
        if type_int is not UNSET:
            field_dict["TYPE_INT"] = type_int
        if type_double is not UNSET:
            field_dict["TYPE_DOUBLE"] = type_double
        if type_string is not UNSET:
            field_dict["TYPE_STRING"] = type_string
        if type_iso_date_time is not UNSET:
            field_dict["TYPE_ISO_DATE_TIME"] = type_iso_date_time
        if type_iso_date_only is not UNSET:
            field_dict["TYPE_ISO_DATE_ONLY"] = type_iso_date_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_status = d.pop("TYPE_STATUS", UNSET)

        type_user = d.pop("TYPE_USER", UNSET)

        type_relation = d.pop("TYPE_RELATION", UNSET)

        type_int = d.pop("TYPE_INT", UNSET)

        type_double = d.pop("TYPE_DOUBLE", UNSET)

        type_string = d.pop("TYPE_STRING", UNSET)

        type_iso_date_time = d.pop("TYPE_ISO_DATE_TIME", UNSET)

        type_iso_date_only = d.pop("TYPE_ISO_DATE_ONLY", UNSET)

        index_value_c = cls(
            type_status=type_status,
            type_user=type_user,
            type_relation=type_relation,
            type_int=type_int,
            type_double=type_double,
            type_string=type_string,
            type_iso_date_time=type_iso_date_time,
            type_iso_date_only=type_iso_date_only,
        )

        index_value_c.additional_properties = d
        return index_value_c

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
