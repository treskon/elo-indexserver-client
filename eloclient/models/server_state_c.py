from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStateC")


@_attrs_define
class ServerStateC:
    """<p>Bit constants for members of ServerState</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_sub_key (Union[Unset, str]): DB column: subkey
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_action (Union[Unset, int]): DB column: action
            mb_action_id (Union[Unset, str]): DB column: actionid
            mb_action (Union[Unset, str]): DB column: action
    """

    mb_sub_key: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_action: Union[Unset, int] = UNSET
    mb_action_id: Union[Unset, str] = UNSET
    mb_action: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_sub_key = self.mb_sub_key

        mb_all_members = self.mb_all_members

        ln_action = self.ln_action

        mb_action_id = self.mb_action_id

        mb_action = self.mb_action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_sub_key is not UNSET:
            field_dict["mbSubKey"] = mb_sub_key
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_action is not UNSET:
            field_dict["lnAction"] = ln_action
        if mb_action_id is not UNSET:
            field_dict["mbActionId"] = mb_action_id
        if mb_action is not UNSET:
            field_dict["mbAction"] = mb_action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_sub_key = d.pop("mbSubKey", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_action = d.pop("lnAction", UNSET)

        mb_action_id = d.pop("mbActionId", UNSET)

        mb_action = d.pop("mbAction", UNSET)

        server_state_c = cls(
            mb_sub_key=mb_sub_key,
            mb_all_members=mb_all_members,
            ln_action=ln_action,
            mb_action_id=mb_action_id,
            mb_action=mb_action,
        )

        server_state_c.additional_properties = d
        return server_state_c

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
