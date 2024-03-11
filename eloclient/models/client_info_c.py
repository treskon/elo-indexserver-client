from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientInfoC")


@_attrs_define
class ClientInfoC:
    """Constants for ClientInfo. These constanse are only for internal usage.

    Attributes:
        option_replication_request (Union[Unset, int]): Replication requests are marked with this bit.
    """

    option_replication_request: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        option_replication_request = self.option_replication_request

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_replication_request is not UNSET:
            field_dict["OPTION_REPLICATION_REQUEST"] = option_replication_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        option_replication_request = d.pop("OPTION_REPLICATION_REQUEST", UNSET)

        client_info_c = cls(
            option_replication_request=option_replication_request,
        )

        client_info_c.additional_properties = d
        return client_info_c

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
