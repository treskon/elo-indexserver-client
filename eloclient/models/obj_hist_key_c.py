from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjHistKeyC")


@_attrs_define
class ObjHistKeyC:
    """<p>Bit constants for members of SordHistKey</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_key_data (Union[Unset, int]): DB column: okeydata
            ln_key_name (Union[Unset, int]): DB column: okeyname
            mb_key_name (Union[Unset, str]): DB column: okeyname
            ln_hist_guid (Union[Unset, int]): Column length: Serialisation version ID
                DB column: objhistguid
            mb_key_data_desc (Union[Unset, str]): Member bit: Internal helper column for memo text.
                DB column: objdesc
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_key_data (Union[Unset, str]): DB column: okeydata
            mb_key_no (Union[Unset, str]): DB column: okeyno
            mb_hist_guid (Union[Unset, str]): Member bit: Serialisation version ID
                DB column: objhistguid
            ln_key_data_desc (Union[Unset, int]): Column length: Internal helper column for memo text.
                DB column: objdesc
    """

    ln_key_data: Union[Unset, int] = UNSET
    ln_key_name: Union[Unset, int] = UNSET
    mb_key_name: Union[Unset, str] = UNSET
    ln_hist_guid: Union[Unset, int] = UNSET
    mb_key_data_desc: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_key_data: Union[Unset, str] = UNSET
    mb_key_no: Union[Unset, str] = UNSET
    mb_hist_guid: Union[Unset, str] = UNSET
    ln_key_data_desc: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_key_data = self.ln_key_data

        ln_key_name = self.ln_key_name

        mb_key_name = self.mb_key_name

        ln_hist_guid = self.ln_hist_guid

        mb_key_data_desc = self.mb_key_data_desc

        mb_all_members = self.mb_all_members

        mb_key_data = self.mb_key_data

        mb_key_no = self.mb_key_no

        mb_hist_guid = self.mb_hist_guid

        ln_key_data_desc = self.ln_key_data_desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_key_data is not UNSET:
            field_dict["lnKeyData"] = ln_key_data
        if ln_key_name is not UNSET:
            field_dict["lnKeyName"] = ln_key_name
        if mb_key_name is not UNSET:
            field_dict["mbKeyName"] = mb_key_name
        if ln_hist_guid is not UNSET:
            field_dict["lnHistGuid"] = ln_hist_guid
        if mb_key_data_desc is not UNSET:
            field_dict["mbKeyDataDesc"] = mb_key_data_desc
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_key_data is not UNSET:
            field_dict["mbKeyData"] = mb_key_data
        if mb_key_no is not UNSET:
            field_dict["mbKeyNo"] = mb_key_no
        if mb_hist_guid is not UNSET:
            field_dict["mbHistGuid"] = mb_hist_guid
        if ln_key_data_desc is not UNSET:
            field_dict["lnKeyDataDesc"] = ln_key_data_desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_key_data = d.pop("lnKeyData", UNSET)

        ln_key_name = d.pop("lnKeyName", UNSET)

        mb_key_name = d.pop("mbKeyName", UNSET)

        ln_hist_guid = d.pop("lnHistGuid", UNSET)

        mb_key_data_desc = d.pop("mbKeyDataDesc", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_key_data = d.pop("mbKeyData", UNSET)

        mb_key_no = d.pop("mbKeyNo", UNSET)

        mb_hist_guid = d.pop("mbHistGuid", UNSET)

        ln_key_data_desc = d.pop("lnKeyDataDesc", UNSET)

        obj_hist_key_c = cls(
            ln_key_data=ln_key_data,
            ln_key_name=ln_key_name,
            mb_key_name=mb_key_name,
            ln_hist_guid=ln_hist_guid,
            mb_key_data_desc=mb_key_data_desc,
            mb_all_members=mb_all_members,
            mb_key_data=mb_key_data,
            mb_key_no=mb_key_no,
            mb_hist_guid=mb_hist_guid,
            ln_key_data_desc=ln_key_data_desc,
        )

        obj_hist_key_c.additional_properties = d
        return obj_hist_key_c

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
