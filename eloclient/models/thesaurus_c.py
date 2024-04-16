from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThesaurusC")


@_attrs_define
class ThesaurusC:
    """<p>Bit constants for members of Thesaurus</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_data (Union[Unset, int]): DB column: data
            mb_prio (Union[Unset, str]): DB column: prio
            mb_compare (Union[Unset, str]): DB column: compare
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_group_id (Union[Unset, str]): DB column: groupid
            mb_data (Union[Unset, str]): DB column: data
            ln_compare (Union[Unset, int]): DB column: compare
            mb_list_id (Union[Unset, str]): DB column: listid
    """

    ln_data: Union[Unset, int] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_compare: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_group_id: Union[Unset, str] = UNSET
    mb_data: Union[Unset, str] = UNSET
    ln_compare: Union[Unset, int] = UNSET
    mb_list_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_data = self.ln_data

        mb_prio = self.mb_prio

        mb_compare = self.mb_compare

        mb_all_members = self.mb_all_members

        mb_group_id = self.mb_group_id

        mb_data = self.mb_data

        ln_compare = self.ln_compare

        mb_list_id = self.mb_list_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_data is not UNSET:
            field_dict["lnData"] = ln_data
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_compare is not UNSET:
            field_dict["mbCompare"] = mb_compare
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_group_id is not UNSET:
            field_dict["mbGroupId"] = mb_group_id
        if mb_data is not UNSET:
            field_dict["mbData"] = mb_data
        if ln_compare is not UNSET:
            field_dict["lnCompare"] = ln_compare
        if mb_list_id is not UNSET:
            field_dict["mbListId"] = mb_list_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_data = d.pop("lnData", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_compare = d.pop("mbCompare", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_group_id = d.pop("mbGroupId", UNSET)

        mb_data = d.pop("mbData", UNSET)

        ln_compare = d.pop("lnCompare", UNSET)

        mb_list_id = d.pop("mbListId", UNSET)

        thesaurus_c = cls(
            ln_data=ln_data,
            mb_prio=mb_prio,
            mb_compare=mb_compare,
            mb_all_members=mb_all_members,
            mb_group_id=mb_group_id,
            mb_data=mb_data,
            ln_compare=ln_compare,
            mb_list_id=mb_list_id,
        )

        thesaurus_c.additional_properties = d
        return thesaurus_c

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
