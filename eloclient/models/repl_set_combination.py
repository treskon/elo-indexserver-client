from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplSetCombination")


@_attrs_define
class ReplSetCombination:
    """Internal class.

    Attributes:
        guid (Union[Unset, str]):
        combi (Union[Unset, str]):
    """

    guid: Union[Unset, str] = UNSET
    combi: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid

        combi = self.combi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid
        if combi is not UNSET:
            field_dict["combi"] = combi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid = d.pop("guid", UNSET)

        combi = d.pop("combi", UNSET)

        repl_set_combination = cls(
            guid=guid,
            combi=combi,
        )

        repl_set_combination.additional_properties = d
        return repl_set_combination

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
