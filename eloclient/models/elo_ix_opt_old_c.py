from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloIxOptOldC")


@_attrs_define
class EloIxOptOldC:
    """<p>Bit constants for members of EloIxOpt_old</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_opt_val (Union[Unset, str]): DB column: optval
            mb_remark (Union[Unset, str]): DB column: remark
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_opt_val (Union[Unset, int]): DB column: optval
            ln_remark (Union[Unset, int]): DB column: remark
            mb_opt_no (Union[Unset, str]): DB column: optno
    """

    mb_opt_val: Union[Unset, str] = UNSET
    mb_remark: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_opt_val: Union[Unset, int] = UNSET
    ln_remark: Union[Unset, int] = UNSET
    mb_opt_no: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_opt_val = self.mb_opt_val

        mb_remark = self.mb_remark

        mb_all_members = self.mb_all_members

        ln_opt_val = self.ln_opt_val

        ln_remark = self.ln_remark

        mb_opt_no = self.mb_opt_no

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_opt_val is not UNSET:
            field_dict["mbOptVal"] = mb_opt_val
        if mb_remark is not UNSET:
            field_dict["mbRemark"] = mb_remark
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_opt_val is not UNSET:
            field_dict["lnOptVal"] = ln_opt_val
        if ln_remark is not UNSET:
            field_dict["lnRemark"] = ln_remark
        if mb_opt_no is not UNSET:
            field_dict["mbOptNo"] = mb_opt_no

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_opt_val = d.pop("mbOptVal", UNSET)

        mb_remark = d.pop("mbRemark", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_opt_val = d.pop("lnOptVal", UNSET)

        ln_remark = d.pop("lnRemark", UNSET)

        mb_opt_no = d.pop("mbOptNo", UNSET)

        elo_ix_opt_old_c = cls(
            mb_opt_val=mb_opt_val,
            mb_remark=mb_remark,
            mb_all_members=mb_all_members,
            ln_opt_val=ln_opt_val,
            ln_remark=ln_remark,
            mb_opt_no=mb_opt_no,
        )

        elo_ix_opt_old_c.additional_properties = d
        return elo_ix_opt_old_c

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
