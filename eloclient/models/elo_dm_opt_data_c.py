from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloDmOptDataC")


@_attrs_define
class EloDmOptDataC:
    """<p>
    Bit constants for members of EloDmOpt
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: optno
            mb_value (Union[Unset, str]): DB column: optval
            ln_value (Union[Unset, int]): DB column: optval
            mb_remark (Union[Unset, str]): DB column: remark
            ln_remark (Union[Unset, int]): DB column: remark
            mb_instance_name (Union[Unset, str]): Member bit: DB column: instance DB column: instancename
            ln_instance_name (Union[Unset, int]): Column length: DB column: instance DB column: instancename
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_id: Union[Unset, str] = UNSET
    mb_value: Union[Unset, str] = UNSET
    ln_value: Union[Unset, int] = UNSET
    mb_remark: Union[Unset, str] = UNSET
    ln_remark: Union[Unset, int] = UNSET
    mb_instance_name: Union[Unset, str] = UNSET
    ln_instance_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id
        mb_value = self.mb_value
        ln_value = self.ln_value
        mb_remark = self.mb_remark
        ln_remark = self.ln_remark
        mb_instance_name = self.mb_instance_name
        ln_instance_name = self.ln_instance_name
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if mb_remark is not UNSET:
            field_dict["mbRemark"] = mb_remark
        if ln_remark is not UNSET:
            field_dict["lnRemark"] = ln_remark
        if mb_instance_name is not UNSET:
            field_dict["mbInstanceName"] = mb_instance_name
        if ln_instance_name is not UNSET:
            field_dict["lnInstanceName"] = ln_instance_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        ln_value = d.pop("lnValue", UNSET)

        mb_remark = d.pop("mbRemark", UNSET)

        ln_remark = d.pop("lnRemark", UNSET)

        mb_instance_name = d.pop("mbInstanceName", UNSET)

        ln_instance_name = d.pop("lnInstanceName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        elo_dm_opt_data_c = cls(
            mb_id=mb_id,
            mb_value=mb_value,
            ln_value=ln_value,
            mb_remark=mb_remark,
            ln_remark=ln_remark,
            mb_instance_name=mb_instance_name,
            ln_instance_name=ln_instance_name,
            mb_all_members=mb_all_members,
        )

        elo_dm_opt_data_c.additional_properties = d
        return elo_dm_opt_data_c

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
