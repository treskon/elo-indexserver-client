from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationDataC")


@_attrs_define
class NotificationDataC:
    """<p>Bit constants for members of Notification</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_user_guid (Union[Unset, str]): Member bit: GUID of user who should receive this notification.
                DB column: userguid
            ln_user_guid (Union[Unset, int]): Column length: GUID of user who should receive this notification.
                DB column: userguid
            ln_create_date_iso (Union[Unset, int]): Column length: Create date of the notification.
                DB column: createdateiso
            mb_create_date_iso (Union[Unset, str]): Member bit: Create date of the notification.
                DB column: createdateiso
            mb_prio (Union[Unset, str]): Member bit: Indicates if the Notification is marked as important
                DB column: prio
            mb_what (Union[Unset, str]): Member bit: Indicates the type of the watched Element. 0 - Action. 1 - HashTag.
                DB column: what
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_watch_guid (Union[Unset, str]): Member bit: GUID of changed Object.
                DB column: watchguid
            ln_watch_guid (Union[Unset, int]): Column length: GUID of changed Object.
                DB column: watchguid
    """

    mb_user_guid: Union[Unset, str] = UNSET
    ln_user_guid: Union[Unset, int] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_what: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_watch_guid: Union[Unset, str] = UNSET
    ln_watch_guid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_user_guid = self.mb_user_guid

        ln_user_guid = self.ln_user_guid

        ln_create_date_iso = self.ln_create_date_iso

        mb_create_date_iso = self.mb_create_date_iso

        mb_prio = self.mb_prio

        mb_what = self.mb_what

        mb_all_members = self.mb_all_members

        mb_watch_guid = self.mb_watch_guid

        ln_watch_guid = self.ln_watch_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_user_guid is not UNSET:
            field_dict["mbUserGuid"] = mb_user_guid
        if ln_user_guid is not UNSET:
            field_dict["lnUserGuid"] = ln_user_guid
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_what is not UNSET:
            field_dict["mbWhat"] = mb_what
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_watch_guid is not UNSET:
            field_dict["mbWatchGuid"] = mb_watch_guid
        if ln_watch_guid is not UNSET:
            field_dict["lnWatchGuid"] = ln_watch_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_user_guid = d.pop("mbUserGuid", UNSET)

        ln_user_guid = d.pop("lnUserGuid", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_what = d.pop("mbWhat", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_watch_guid = d.pop("mbWatchGuid", UNSET)

        ln_watch_guid = d.pop("lnWatchGuid", UNSET)

        notification_data_c = cls(
            mb_user_guid=mb_user_guid,
            ln_user_guid=ln_user_guid,
            ln_create_date_iso=ln_create_date_iso,
            mb_create_date_iso=mb_create_date_iso,
            mb_prio=mb_prio,
            mb_what=mb_what,
            mb_all_members=mb_all_members,
            mb_watch_guid=mb_watch_guid,
            ln_watch_guid=ln_watch_guid,
        )

        notification_data_c.additional_properties = d
        return notification_data_c

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
