from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloDmOpt")


@_attrs_define
class EloDmOpt:
    """Internal class.

    Attributes:
        id (Union[Unset, int]): DB column: optno
        value (Union[Unset, str]): DB column: optval
        remark (Union[Unset, str]): DB column: remark
        instance_name (Union[Unset, str]): DB column: instance
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    instance_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        remark = self.remark
        instance_name = self.instance_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if remark is not UNSET:
            field_dict["remark"] = remark
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        remark = d.pop("remark", UNSET)

        instance_name = d.pop("instanceName", UNSET)

        elo_dm_opt = cls(
            id=id,
            value=value,
            remark=remark,
            instance_name=instance_name,
        )

        elo_dm_opt.additional_properties = d
        return elo_dm_opt

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
