from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloFtOptDataC")


@_attrs_define
class EloFtOptDataC:
    """<p>Bit constants for members of EloFtOpt</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_value (Union[Unset, int]): DB column: optval
            mb_id (Union[Unset, str]): DB column: optid
            mb_value (Union[Unset, str]): DB column: optval
            mb_remark (Union[Unset, str]): DB column: remark
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_remark (Union[Unset, int]): DB column: remark
    """

    ln_value: Union[Unset, int] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_value: Union[Unset, str] = UNSET
    mb_remark: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_remark: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_value = self.ln_value

        mb_id = self.mb_id

        mb_value = self.mb_value

        mb_remark = self.mb_remark

        mb_all_members = self.mb_all_members

        ln_remark = self.ln_remark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if mb_remark is not UNSET:
            field_dict["mbRemark"] = mb_remark
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_remark is not UNSET:
            field_dict["lnRemark"] = ln_remark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_value = d.pop("lnValue", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        mb_remark = d.pop("mbRemark", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_remark = d.pop("lnRemark", UNSET)

        elo_ft_opt_data_c = cls(
            ln_value=ln_value,
            mb_id=mb_id,
            mb_value=mb_value,
            mb_remark=mb_remark,
            mb_all_members=mb_all_members,
            ln_remark=ln_remark,
        )

        elo_ft_opt_data_c.additional_properties = d
        return elo_ft_opt_data_c

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
