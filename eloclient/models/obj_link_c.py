from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjLinkC")


@_attrs_define
class ObjLinkC:
    """<p>
    Bit constants for members of SordLink
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_parent_id (Union[Unset, str]): DB column: objguidparent
            ln_parent_id (Union[Unset, int]): DB column: objguidparent
            mb_id (Union[Unset, str]): DB column: objguidtarget
            ln_id (Union[Unset, int]): DB column: objguidtarget
            mb_link_id (Union[Unset, str]): DB column: linkguid
            ln_link_id (Union[Unset, int]): DB column: linkguid
            mb_t_stamp (Union[Unset, str]): DB column: linktstamp
            ln_t_stamp (Union[Unset, int]): DB column: linktstamp
            mb_flags (Union[Unset, str]): DB column: linkflags
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_parent_id: Union[Unset, str] = UNSET
    ln_parent_id: Union[Unset, int] = UNSET
    mb_id: Union[Unset, str] = UNSET
    ln_id: Union[Unset, int] = UNSET
    mb_link_id: Union[Unset, str] = UNSET
    ln_link_id: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_parent_id = self.mb_parent_id
        ln_parent_id = self.ln_parent_id
        mb_id = self.mb_id
        ln_id = self.ln_id
        mb_link_id = self.mb_link_id
        ln_link_id = self.ln_link_id
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_flags = self.mb_flags
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_parent_id is not UNSET:
            field_dict["mbParentId"] = mb_parent_id
        if ln_parent_id is not UNSET:
            field_dict["lnParentId"] = ln_parent_id
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if mb_link_id is not UNSET:
            field_dict["mbLinkId"] = mb_link_id
        if ln_link_id is not UNSET:
            field_dict["lnLinkId"] = ln_link_id
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_parent_id = d.pop("mbParentId", UNSET)

        ln_parent_id = d.pop("lnParentId", UNSET)

        mb_id = d.pop("mbId", UNSET)

        ln_id = d.pop("lnId", UNSET)

        mb_link_id = d.pop("mbLinkId", UNSET)

        ln_link_id = d.pop("lnLinkId", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        obj_link_c = cls(
            mb_parent_id=mb_parent_id,
            ln_parent_id=ln_parent_id,
            mb_id=mb_id,
            ln_id=ln_id,
            mb_link_id=mb_link_id,
            ln_link_id=ln_link_id,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_flags=mb_flags,
            mb_all_members=mb_all_members,
        )

        obj_link_c.additional_properties = d
        return obj_link_c

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
