from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjChangeC")


@_attrs_define
class ObjChangeC:
    """<p>Bit constants for members of ObjChange</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_obj_id (Union[Unset, str]): DB column: chgobjid
            mb_t_stamp (Union[Unset, str]): DB column: chgtstamp
            mb_code (Union[Unset, str]): DB column: chgcode
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_param_2 (Union[Unset, str]): DB column: chgparam2
            ln_t_stamp (Union[Unset, int]): DB column: chgtstamp
            ln_param_2 (Union[Unset, int]): DB column: chgparam2
            ln_obj_id (Union[Unset, int]): DB column: chgobjid
            mb_user (Union[Unset, str]): DB column: chguser
            mb_param (Union[Unset, str]): DB column: chgparam
    """

    mb_obj_id: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_code: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_param_2: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_param_2: Union[Unset, int] = UNSET
    ln_obj_id: Union[Unset, int] = UNSET
    mb_user: Union[Unset, str] = UNSET
    mb_param: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_obj_id = self.mb_obj_id

        mb_t_stamp = self.mb_t_stamp

        mb_code = self.mb_code

        mb_all_members = self.mb_all_members

        mb_param_2 = self.mb_param_2

        ln_t_stamp = self.ln_t_stamp

        ln_param_2 = self.ln_param_2

        ln_obj_id = self.ln_obj_id

        mb_user = self.mb_user

        mb_param = self.mb_param

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_code is not UNSET:
            field_dict["mbCode"] = mb_code
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_param_2 is not UNSET:
            field_dict["mbParam2"] = mb_param_2
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_param_2 is not UNSET:
            field_dict["lnParam2"] = ln_param_2
        if ln_obj_id is not UNSET:
            field_dict["lnObjId"] = ln_obj_id
        if mb_user is not UNSET:
            field_dict["mbUser"] = mb_user
        if mb_param is not UNSET:
            field_dict["mbParam"] = mb_param

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_code = d.pop("mbCode", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_param_2 = d.pop("mbParam2", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_param_2 = d.pop("lnParam2", UNSET)

        ln_obj_id = d.pop("lnObjId", UNSET)

        mb_user = d.pop("mbUser", UNSET)

        mb_param = d.pop("mbParam", UNSET)

        obj_change_c = cls(
            mb_obj_id=mb_obj_id,
            mb_t_stamp=mb_t_stamp,
            mb_code=mb_code,
            mb_all_members=mb_all_members,
            mb_param_2=mb_param_2,
            ln_t_stamp=ln_t_stamp,
            ln_param_2=ln_param_2,
            ln_obj_id=ln_obj_id,
            mb_user=mb_user,
            mb_param=mb_param,
        )

        obj_change_c.additional_properties = d
        return obj_change_c

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
