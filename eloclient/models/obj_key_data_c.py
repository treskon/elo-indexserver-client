from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjKeyDataC")


@_attrs_define
class ObjKeyDataC:
    """<p>Bit constants for members of ObjKeyData</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: okeyno
            mb_name (Union[Unset, str]): DB column: okeyname
            mb_sdata (Union[Unset, str]): DB column: okeysdata_off
            ln_sdata (Union[Unset, int]): DB column: okeysdata_off
            ln_udata (Union[Unset, int]): DB column: okeyudata
            mb_odouble (Union[Unset, str]): Member bit: DB column: odouble
                DB column: okeydouble
            ln_name (Union[Unset, int]): DB column: okeyname
            mb_obj_id (Union[Unset, str]): DB column: parentid
            mb_udata (Union[Unset, str]): DB column: okeyudata
            ln_data (Union[Unset, int]): DB column: okeydata
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_data (Union[Unset, str]): DB column: okeydata
            ln_odouble (Union[Unset, int]): Column length: DB column: odouble
                DB column: okeydouble
    """

    mb_id: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_sdata: Union[Unset, str] = UNSET
    ln_sdata: Union[Unset, int] = UNSET
    ln_udata: Union[Unset, int] = UNSET
    mb_odouble: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_udata: Union[Unset, str] = UNSET
    ln_data: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_data: Union[Unset, str] = UNSET
    ln_odouble: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id

        mb_name = self.mb_name

        mb_sdata = self.mb_sdata

        ln_sdata = self.ln_sdata

        ln_udata = self.ln_udata

        mb_odouble = self.mb_odouble

        ln_name = self.ln_name

        mb_obj_id = self.mb_obj_id

        mb_udata = self.mb_udata

        ln_data = self.ln_data

        mb_all_members = self.mb_all_members

        mb_data = self.mb_data

        ln_odouble = self.ln_odouble

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_sdata is not UNSET:
            field_dict["mbSdata"] = mb_sdata
        if ln_sdata is not UNSET:
            field_dict["lnSdata"] = ln_sdata
        if ln_udata is not UNSET:
            field_dict["lnUdata"] = ln_udata
        if mb_odouble is not UNSET:
            field_dict["mbOdouble"] = mb_odouble
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_udata is not UNSET:
            field_dict["mbUdata"] = mb_udata
        if ln_data is not UNSET:
            field_dict["lnData"] = ln_data
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_data is not UNSET:
            field_dict["mbData"] = mb_data
        if ln_odouble is not UNSET:
            field_dict["lnOdouble"] = ln_odouble

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_sdata = d.pop("mbSdata", UNSET)

        ln_sdata = d.pop("lnSdata", UNSET)

        ln_udata = d.pop("lnUdata", UNSET)

        mb_odouble = d.pop("mbOdouble", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_udata = d.pop("mbUdata", UNSET)

        ln_data = d.pop("lnData", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_data = d.pop("mbData", UNSET)

        ln_odouble = d.pop("lnOdouble", UNSET)

        obj_key_data_c = cls(
            mb_id=mb_id,
            mb_name=mb_name,
            mb_sdata=mb_sdata,
            ln_sdata=ln_sdata,
            ln_udata=ln_udata,
            mb_odouble=mb_odouble,
            ln_name=ln_name,
            mb_obj_id=mb_obj_id,
            mb_udata=mb_udata,
            ln_data=ln_data,
            mb_all_members=mb_all_members,
            mb_data=mb_data,
            ln_odouble=ln_odouble,
        )

        obj_key_data_c.additional_properties = d
        return obj_key_data_c

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
