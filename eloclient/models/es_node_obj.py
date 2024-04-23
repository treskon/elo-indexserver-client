from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ESNodeObj")


@_attrs_define
class ESNodeObj:
    """<b><i>Note: For internal use only. Might change in the near future.
    </i></b>

        Attributes:
            status (Union[Unset, str]):
            port (Union[Unset, int]):
            ip (Union[Unset, str]):
            disc_space_usage (Union[Unset, str]):
    """

    status: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    ip: Union[Unset, str] = UNSET
    disc_space_usage: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        port = self.port

        ip = self.ip

        disc_space_usage = self.disc_space_usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if port is not UNSET:
            field_dict["port"] = port
        if ip is not UNSET:
            field_dict["ip"] = ip
        if disc_space_usage is not UNSET:
            field_dict["discSpaceUsage"] = disc_space_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("Status", UNSET)

        port = d.pop("port", UNSET)

        ip = d.pop("ip", UNSET)

        disc_space_usage = d.pop("discSpaceUsage", UNSET)

        es_node_obj = cls(
            status=status,
            port=port,
            ip=ip,
            disc_space_usage=disc_space_usage,
        )

        es_node_obj.additional_properties = d
        return es_node_obj

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
