from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskInheritC")


@_attrs_define
class DocMaskInheritC:
    """<p>Bit constants for members of DocMaskInherit</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_child_mask_id (Union[Unset, str]): DB column: childmaskid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_parent_mask_id (Union[Unset, str]): DB column: parentmaskid
    """

    mb_child_mask_id: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_parent_mask_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_child_mask_id = self.mb_child_mask_id

        mb_all_members = self.mb_all_members

        mb_parent_mask_id = self.mb_parent_mask_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_child_mask_id is not UNSET:
            field_dict["mbChildMaskId"] = mb_child_mask_id
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_parent_mask_id is not UNSET:
            field_dict["mbParentMaskId"] = mb_parent_mask_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_child_mask_id = d.pop("mbChildMaskId", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_parent_mask_id = d.pop("mbParentMaskId", UNSET)

        doc_mask_inherit_c = cls(
            mb_child_mask_id=mb_child_mask_id,
            mb_all_members=mb_all_members,
            mb_parent_mask_id=mb_parent_mask_id,
        )

        doc_mask_inherit_c.additional_properties = d
        return doc_mask_inherit_c

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
