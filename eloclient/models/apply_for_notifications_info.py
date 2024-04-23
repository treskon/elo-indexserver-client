from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplyForNotificationsInfo")


@_attrs_define
class ApplyForNotificationsInfo:
    """This class defines which notification messages the server has to send.

    Attributes:
        admin_mode (Union[Unset, bool]): Receive {@link de.elo.ix.client.notify.
            ClientNotification#adminMode(ClientInfo, int)}
        user_task (Union[Unset, bool]): Reserved
    """

    admin_mode: Union[Unset, bool] = UNSET
    user_task: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin_mode = self.admin_mode

        user_task = self.user_task

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_mode is not UNSET:
            field_dict["adminMode"] = admin_mode
        if user_task is not UNSET:
            field_dict["userTask"] = user_task

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_mode = d.pop("adminMode", UNSET)

        user_task = d.pop("userTask", UNSET)

        apply_for_notifications_info = cls(
            admin_mode=admin_mode,
            user_task=user_task,
        )

        apply_for_notifications_info.additional_properties = d
        return apply_for_notifications_info

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
