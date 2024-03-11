from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """Objects of this class represent a change notification. This class is used internally.

    Attributes:
        user_guid (Union[Unset, str]): GUID of user who should receive this notification.
        watch_guid (Union[Unset, str]): GUID of changed Object.
        create_date_iso (Union[Unset, str]): Create date of the notification.
        prio (Union[Unset, int]): Indicates if the Notification is marked as important
        what (Union[Unset, int]): Indicates the type of the watched Element. 0 - Action. 1 - HashTag.
    """

    user_guid: Union[Unset, str] = UNSET
    watch_guid: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    what: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_guid = self.user_guid
        watch_guid = self.watch_guid
        create_date_iso = self.create_date_iso
        prio = self.prio
        what = self.what

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_guid is not UNSET:
            field_dict["userGuid"] = user_guid
        if watch_guid is not UNSET:
            field_dict["watchGuid"] = watch_guid
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if prio is not UNSET:
            field_dict["prio"] = prio
        if what is not UNSET:
            field_dict["what"] = what

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_guid = d.pop("userGuid", UNSET)

        watch_guid = d.pop("watchGuid", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        prio = d.pop("prio", UNSET)

        what = d.pop("what", UNSET)

        notification = cls(
            user_guid=user_guid,
            watch_guid=watch_guid,
            create_date_iso=create_date_iso,
            prio=prio,
            what=what,
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
