from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjChange")


@_attrs_define
class ObjChange:
    """Internal class.

    Attributes:
        obj_id (Union[Unset, str]): DB column: chgobjid
        t_stamp (Union[Unset, str]): DB column: chgtstamp
        code (Union[Unset, int]): DB column: chgcode
        param (Union[Unset, int]): DB column: chgparam
        param2 (Union[Unset, str]): DB column: chgparam2
        user (Union[Unset, int]): DB column: chguser
    """

    obj_id: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    code: Union[Unset, int] = UNSET
    param: Union[Unset, int] = UNSET
    param2: Union[Unset, str] = UNSET
    user: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        obj_id = self.obj_id
        t_stamp = self.t_stamp
        code = self.code
        param = self.param
        param2 = self.param2
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if code is not UNSET:
            field_dict["code"] = code
        if param is not UNSET:
            field_dict["param"] = param
        if param2 is not UNSET:
            field_dict["param2"] = param2
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        obj_id = d.pop("objId", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        code = d.pop("code", UNSET)

        param = d.pop("param", UNSET)

        param2 = d.pop("param2", UNSET)

        user = d.pop("user", UNSET)

        obj_change = cls(
            obj_id=obj_id,
            t_stamp=t_stamp,
            code=code,
            param=param,
            param2=param2,
            user=user,
        )

        obj_change.additional_properties = d
        return obj_change

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
