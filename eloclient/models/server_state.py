from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerState")


@_attrs_define
class ServerState:
    """Internal class.

    Attributes:
        action_id (Union[Unset, int]): DB column: actionid
        sub_key (Union[Unset, int]): DB column: subkey
        action (Union[Unset, str]): DB column: action
    """

    action_id: Union[Unset, int] = UNSET
    sub_key: Union[Unset, int] = UNSET
    action: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_id = self.action_id
        sub_key = self.sub_key
        action = self.action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_id is not UNSET:
            field_dict["actionId"] = action_id
        if sub_key is not UNSET:
            field_dict["subKey"] = sub_key
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action_id = d.pop("actionId", UNSET)

        sub_key = d.pop("subKey", UNSET)

        action = d.pop("action", UNSET)

        server_state = cls(
            action_id=action_id,
            sub_key=sub_key,
            action=action,
        )

        server_state.additional_properties = d
        return server_state

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
