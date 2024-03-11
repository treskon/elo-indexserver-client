from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionHistDataC")


@_attrs_define
class ActionHistDataC:
    """<p>
    Bit constants for members of ActionHistory
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_action_guid (Union[Unset, str]): Member bit: Action GUID.
                DB column: actionguid
            ln_action_guid (Union[Unset, int]): Column length: Action GUID.
                DB column: actionguid
            mb_create_date_iso (Union[Unset, str]): Member bit: Create date.
                DB column: createdateiso
            ln_create_date_iso (Union[Unset, int]): Column length: Create date.
                DB column: createdateiso
            mb_text (Union[Unset, str]): Member bit: Comment text.
                DB column: actiontext
            ln_text (Union[Unset, int]): Column length: Comment text.
                DB column: actiontext
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_action_guid: Union[Unset, str] = UNSET
    ln_action_guid: Union[Unset, int] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_text: Union[Unset, str] = UNSET
    ln_text: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_action_guid = self.mb_action_guid
        ln_action_guid = self.ln_action_guid
        mb_create_date_iso = self.mb_create_date_iso
        ln_create_date_iso = self.ln_create_date_iso
        mb_text = self.mb_text
        ln_text = self.ln_text
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_action_guid is not UNSET:
            field_dict["mbActionGuid"] = mb_action_guid
        if ln_action_guid is not UNSET:
            field_dict["lnActionGuid"] = ln_action_guid
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_text is not UNSET:
            field_dict["mbText"] = mb_text
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_action_guid = d.pop("mbActionGuid", UNSET)

        ln_action_guid = d.pop("lnActionGuid", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_text = d.pop("mbText", UNSET)

        ln_text = d.pop("lnText", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        action_hist_data_c = cls(
            mb_action_guid=mb_action_guid,
            ln_action_guid=ln_action_guid,
            mb_create_date_iso=mb_create_date_iso,
            ln_create_date_iso=ln_create_date_iso,
            mb_text=mb_text,
            ln_text=ln_text,
            mb_all_members=mb_all_members,
        )

        action_hist_data_c.additional_properties = d
        return action_hist_data_c

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
