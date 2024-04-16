from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloIxOpt")


@_attrs_define
class EloIxOpt:
    """Internal class.

    Attributes:
        name (Union[Unset, str]): DB column: optname
        ix_id (Union[Unset, str]): DB column: ixid
        value (Union[Unset, str]): DB column: optval
    """

    name: Union[Unset, str] = UNSET
    ix_id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        ix_id = self.ix_id

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ix_id is not UNSET:
            field_dict["ixId"] = ix_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        ix_id = d.pop("ixId", UNSET)

        value = d.pop("value", UNSET)

        elo_ix_opt = cls(
            name=name,
            ix_id=ix_id,
            value=value,
        )

        elo_ix_opt.additional_properties = d
        return elo_ix_opt

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
