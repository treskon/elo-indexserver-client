from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """Objects of this class represent a change notification. This class is used internally.

    Attributes:
        what (Union[Unset, int]): Indicates the type of the watched Element. 0 - Action. 1 - HashTag.
        create_date_iso (Union[Unset, str]): Create date of the notification.
        watch_guid (Union[Unset, str]): GUID of changed Object.
        user_guid (Union[Unset, str]): GUID of user who should receive this notification.
        prio (Union[Unset, int]): Indicates if the Notification is marked as important
    """

    what: Union[Unset, int] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    watch_guid: Union[Unset, str] = UNSET
    user_guid: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        what = self.what

        create_date_iso = self.create_date_iso

        watch_guid = self.watch_guid

        user_guid = self.user_guid

        prio = self.prio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if what is not UNSET:
            field_dict["what"] = what
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if watch_guid is not UNSET:
            field_dict["watchGuid"] = watch_guid
        if user_guid is not UNSET:
            field_dict["userGuid"] = user_guid
        if prio is not UNSET:
            field_dict["prio"] = prio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        what = d.pop("what", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        watch_guid = d.pop("watchGuid", UNSET)

        user_guid = d.pop("userGuid", UNSET)

        prio = d.pop("prio", UNSET)

        notification = cls(
            what=what,
            create_date_iso=create_date_iso,
            watch_guid=watch_guid,
            user_guid=user_guid,
            prio=prio,
        )

        notification.additional_properties = d
        return notification

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
