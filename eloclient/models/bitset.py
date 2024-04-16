from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Bitset")


@_attrs_define
class Bitset:
    """This class is used in the scripting API of Indexserver and provides bit operations on 64 bit
    integers. JavaScript does not support bit operations for 64 bit integers. The global context of
     the JavaScripts executed by Indexserver contain an object named Bitset which is an instance of
     this class.

        Attributes:
            v (Union[Unset, str]): Internal 64 bit integer value
    """

    v: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        v = self.v

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v is not UNSET:
            field_dict["v"] = v

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        v = d.pop("v", UNSET)

        bitset = cls(
            v=v,
        )

        bitset.additional_properties = d
        return bitset

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
