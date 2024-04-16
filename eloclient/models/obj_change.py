from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjChange")


@_attrs_define
class ObjChange:
    """Internal class.

    Attributes:
        code (Union[Unset, int]): DB column: chgcode
        param (Union[Unset, int]): DB column: chgparam
        t_stamp (Union[Unset, str]): DB column: chgtstamp
        obj_id (Union[Unset, str]): DB column: chgobjid
        user (Union[Unset, int]): DB column: chguser
        param2 (Union[Unset, str]): DB column: chgparam2
    """

    code: Union[Unset, int] = UNSET
    param: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    user: Union[Unset, int] = UNSET
    param2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        param = self.param

        t_stamp = self.t_stamp

        obj_id = self.obj_id

        user = self.user

        param2 = self.param2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if param is not UNSET:
            field_dict["param"] = param
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if user is not UNSET:
            field_dict["user"] = user
        if param2 is not UNSET:
            field_dict["param2"] = param2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        param = d.pop("param", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        obj_id = d.pop("objId", UNSET)

        user = d.pop("user", UNSET)

        param2 = d.pop("param2", UNSET)

        obj_change = cls(
            code=code,
            param=param,
            t_stamp=t_stamp,
            obj_id=obj_id,
            user=user,
            param2=param2,
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
