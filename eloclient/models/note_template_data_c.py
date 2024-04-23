from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteTemplateDataC")


@_attrs_define
class NoteTemplateDataC:
    """<p>Bit constants for members of NoteTemplate</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_opt_key (Union[Unset, str]): DB column: optkey
            ln_opt_key (Union[Unset, int]): DB column: optkey
            ln_opt_value (Union[Unset, int]): DB column: optvalue
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_opt_value (Union[Unset, str]): DB column: optvalue
            mb_user_id_int (Union[Unset, str]): DB column: userid
    """

    mb_opt_key: Union[Unset, str] = UNSET
    ln_opt_key: Union[Unset, int] = UNSET
    ln_opt_value: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_opt_value: Union[Unset, str] = UNSET
    mb_user_id_int: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_opt_key = self.mb_opt_key

        ln_opt_key = self.ln_opt_key

        ln_opt_value = self.ln_opt_value

        mb_all_members = self.mb_all_members

        mb_opt_value = self.mb_opt_value

        mb_user_id_int = self.mb_user_id_int

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_opt_key is not UNSET:
            field_dict["mbOptKey"] = mb_opt_key
        if ln_opt_key is not UNSET:
            field_dict["lnOptKey"] = ln_opt_key
        if ln_opt_value is not UNSET:
            field_dict["lnOptValue"] = ln_opt_value
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_opt_value is not UNSET:
            field_dict["mbOptValue"] = mb_opt_value
        if mb_user_id_int is not UNSET:
            field_dict["mbUserIdInt"] = mb_user_id_int

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_opt_key = d.pop("mbOptKey", UNSET)

        ln_opt_key = d.pop("lnOptKey", UNSET)

        ln_opt_value = d.pop("lnOptValue", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_opt_value = d.pop("mbOptValue", UNSET)

        mb_user_id_int = d.pop("mbUserIdInt", UNSET)

        note_template_data_c = cls(
            mb_opt_key=mb_opt_key,
            ln_opt_key=ln_opt_key,
            ln_opt_value=ln_opt_value,
            mb_all_members=mb_all_members,
            mb_opt_value=mb_opt_value,
            mb_user_id_int=mb_user_id_int,
        )

        note_template_data_c.additional_properties = d
        return note_template_data_c

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
