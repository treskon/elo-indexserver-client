from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplSetCombinationC")


@_attrs_define
class ReplSetCombinationC:
    """<p>Bit constants for members of ReplSetCombination</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_combi (Union[Unset, str]): DB column: dw
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_combi_guid (Union[Unset, str]): DB column: combiid
            ln_combi (Union[Unset, int]): DB column: dw
            ln_combi_guid (Union[Unset, int]): DB column: combiid
    """

    mb_combi: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_combi_guid: Union[Unset, str] = UNSET
    ln_combi: Union[Unset, int] = UNSET
    ln_combi_guid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_combi = self.mb_combi

        mb_all_members = self.mb_all_members

        mb_combi_guid = self.mb_combi_guid

        ln_combi = self.ln_combi

        ln_combi_guid = self.ln_combi_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_combi is not UNSET:
            field_dict["mbCombi"] = mb_combi
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_combi_guid is not UNSET:
            field_dict["mbCombiGuid"] = mb_combi_guid
        if ln_combi is not UNSET:
            field_dict["lnCombi"] = ln_combi
        if ln_combi_guid is not UNSET:
            field_dict["lnCombiGuid"] = ln_combi_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_combi = d.pop("mbCombi", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_combi_guid = d.pop("mbCombiGuid", UNSET)

        ln_combi = d.pop("lnCombi", UNSET)

        ln_combi_guid = d.pop("lnCombiGuid", UNSET)

        repl_set_combination_c = cls(
            mb_combi=mb_combi,
            mb_all_members=mb_all_members,
            mb_combi_guid=mb_combi_guid,
            ln_combi=ln_combi,
            ln_combi_guid=ln_combi_guid,
        )

        repl_set_combination_c.additional_properties = d
        return repl_set_combination_c

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
