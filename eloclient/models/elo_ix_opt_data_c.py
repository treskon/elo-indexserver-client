from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloIxOptDataC")


@_attrs_define
class EloIxOptDataC:
    """<p>Bit constants for members of EloIxOpt</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_ix_id (Union[Unset, int]): DB column: ixid
            ln_value (Union[Unset, int]): DB column: optval
            ln_name (Union[Unset, int]): DB column: optname
            mb_ix_id (Union[Unset, str]): DB column: ixid
            mb_value (Union[Unset, str]): DB column: optval
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_name (Union[Unset, str]): DB column: optname
    """

    ln_ix_id: Union[Unset, int] = UNSET
    ln_value: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_ix_id: Union[Unset, str] = UNSET
    mb_value: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_ix_id = self.ln_ix_id

        ln_value = self.ln_value

        ln_name = self.ln_name

        mb_ix_id = self.mb_ix_id

        mb_value = self.mb_value

        mb_all_members = self.mb_all_members

        mb_name = self.mb_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_ix_id is not UNSET:
            field_dict["lnIxId"] = ln_ix_id
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_ix_id is not UNSET:
            field_dict["mbIxId"] = mb_ix_id
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_ix_id = d.pop("lnIxId", UNSET)

        ln_value = d.pop("lnValue", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_ix_id = d.pop("mbIxId", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_name = d.pop("mbName", UNSET)

        elo_ix_opt_data_c = cls(
            ln_ix_id=ln_ix_id,
            ln_value=ln_value,
            ln_name=ln_name,
            mb_ix_id=mb_ix_id,
            mb_value=mb_value,
            mb_all_members=mb_all_members,
            mb_name=mb_name,
        )

        elo_ix_opt_data_c.additional_properties = d
        return elo_ix_opt_data_c

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
