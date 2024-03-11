from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CleanUpInfo")


@_attrs_define
class CleanUpInfo:
    """Settings Object for MyELOService.
    cleanUpNotifications()

        Attributes:
            lifetime_days (Union[Unset, int]): Lifetime of notifications in days.
            delete_important (Union[Unset, bool]): Include Notifications marked as important.
            user_guid_or_id (Union[Unset, str]): GUID or ID or Name of the User. If null, current user will be set.
                If GUID/ID is not the current user, admin rights
                 are required to perform the cleanup
    """

    lifetime_days: Union[Unset, int] = UNSET
    delete_important: Union[Unset, bool] = UNSET
    user_guid_or_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lifetime_days = self.lifetime_days
        delete_important = self.delete_important
        user_guid_or_id = self.user_guid_or_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lifetime_days is not UNSET:
            field_dict["lifetimeDays"] = lifetime_days
        if delete_important is not UNSET:
            field_dict["deleteImportant"] = delete_important
        if user_guid_or_id is not UNSET:
            field_dict["userGuidOrID"] = user_guid_or_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lifetime_days = d.pop("lifetimeDays", UNSET)

        delete_important = d.pop("deleteImportant", UNSET)

        user_guid_or_id = d.pop("userGuidOrID", UNSET)

        clean_up_info = cls(
            lifetime_days=lifetime_days,
            delete_important=delete_important,
            user_guid_or_id=user_guid_or_id,
        )

        clean_up_info.additional_properties = d
        return clean_up_info

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
