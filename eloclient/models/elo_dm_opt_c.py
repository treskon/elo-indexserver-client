from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloDmOptC")


@_attrs_define
class EloDmOptC:
    """Internal class

    Attributes:
        instance_all (Union[Unset, str]): Instance name for options related to all ELOdm instances.
    """

    instance_all: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instance_all = self.instance_all

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_all is not UNSET:
            field_dict["INSTANCE_ALL"] = instance_all

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instance_all = d.pop("INSTANCE_ALL", UNSET)

        elo_dm_opt_c = cls(
            instance_all=instance_all,
        )

        elo_dm_opt_c.additional_properties = d
        return elo_dm_opt_c

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
