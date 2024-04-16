from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloFtOpt")


@_attrs_define
class EloFtOpt:
    """Internal class.

    Attributes:
        remark (Union[Unset, str]): DB column: remark
        id (Union[Unset, int]): DB column: optid
        value (Union[Unset, str]): DB column: optval
    """

    remark: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remark = self.remark

        id = self.id

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remark is not UNSET:
            field_dict["remark"] = remark
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        remark = d.pop("remark", UNSET)

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        elo_ft_opt = cls(
            remark=remark,
            id=id,
            value=value,
        )

        elo_ft_opt.additional_properties = d
        return elo_ft_opt

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
