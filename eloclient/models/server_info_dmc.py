from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerInfoDMC")


@_attrs_define
class ServerInfoDMC:
    """Constants used by the members of the class ServerInfoDM.

    Attributes:
        storemode_basepath_fill_up (Union[Unset, int]): Fill up base paths subsequently.
        storemode_basepath_mask (Union[Unset, int]): This bitmask selects the lower two bits of the
            ServerInfoDM.storeMode.
            This bits are equal to
             one of the STOREMODE_BASEPATH_* constants.
        storemode_basepath_roundrobin (Union[Unset, int]): Fill base paths by round robin algorithm.
    """

    storemode_basepath_fill_up: Union[Unset, int] = UNSET
    storemode_basepath_mask: Union[Unset, int] = UNSET
    storemode_basepath_roundrobin: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storemode_basepath_fill_up = self.storemode_basepath_fill_up

        storemode_basepath_mask = self.storemode_basepath_mask

        storemode_basepath_roundrobin = self.storemode_basepath_roundrobin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storemode_basepath_fill_up is not UNSET:
            field_dict["STOREMODE_BASEPATH_FILL_UP"] = storemode_basepath_fill_up
        if storemode_basepath_mask is not UNSET:
            field_dict["STOREMODE_BASEPATH_MASK"] = storemode_basepath_mask
        if storemode_basepath_roundrobin is not UNSET:
            field_dict["STOREMODE_BASEPATH_ROUNDROBIN"] = storemode_basepath_roundrobin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        storemode_basepath_fill_up = d.pop("STOREMODE_BASEPATH_FILL_UP", UNSET)

        storemode_basepath_mask = d.pop("STOREMODE_BASEPATH_MASK", UNSET)

        storemode_basepath_roundrobin = d.pop("STOREMODE_BASEPATH_ROUNDROBIN", UNSET)

        server_info_dmc = cls(
            storemode_basepath_fill_up=storemode_basepath_fill_up,
            storemode_basepath_mask=storemode_basepath_mask,
            storemode_basepath_roundrobin=storemode_basepath_roundrobin,
        )

        server_info_dmc.additional_properties = d
        return server_info_dmc

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
