from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloDmOpt")


@_attrs_define
class EloDmOpt:
    """Internal class.

    Attributes:
        instance_name (Union[Unset, str]): DB column: instance
        remark (Union[Unset, str]): DB column: remark
        id (Union[Unset, int]): DB column: optno
        value (Union[Unset, str]): DB column: optval
    """

    instance_name: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instance_name = self.instance_name

        remark = self.remark

        id = self.id

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
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
        instance_name = d.pop("instanceName", UNSET)

        remark = d.pop("remark", UNSET)

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        elo_dm_opt = cls(
            instance_name=instance_name,
            remark=remark,
            id=id,
            value=value,
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
