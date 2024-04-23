from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VtDocC")


@_attrs_define
class VtDocC:
    """<p>Bit constants for members of VtDoc</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_obj_id (Union[Unset, str]): DB column: objid
            mb_code (Union[Unset, str]): DB column: vtcode
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_doc_id (Union[Unset, str]): DB column: objdoc
    """

    mb_obj_id: Union[Unset, str] = UNSET
    mb_code: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_doc_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_obj_id = self.mb_obj_id

        mb_code = self.mb_code

        mb_all_members = self.mb_all_members

        mb_doc_id = self.mb_doc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_code is not UNSET:
            field_dict["mbCode"] = mb_code
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_doc_id is not UNSET:
            field_dict["mbDocId"] = mb_doc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_code = d.pop("mbCode", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_doc_id = d.pop("mbDocId", UNSET)

        vt_doc_c = cls(
            mb_obj_id=mb_obj_id,
            mb_code=mb_code,
            mb_all_members=mb_all_members,
            mb_doc_id=mb_doc_id,
        )

        vt_doc_c.additional_properties = d
        return vt_doc_c

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
