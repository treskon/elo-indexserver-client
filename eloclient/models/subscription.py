from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """This class describes a subscription. A user can subscribe for changes to an object.
    Currently,
     the only supported object type is a document feed. If the feed receives new comments,
     notification information is inserted into the database for the user. By calling
     FeedService.findFirstActions and setting FindActionsInfo.findNotifications=true, the user can
     search for her notifications.

        Attributes:
            create_date_iso (Union[Unset, str]): Create date of the subscription.
            watch_guid (Union[Unset, str]): GUID of Object to be watched.
                This is either a {@link de.elo.ix.client.feed.Feed#getGuid()},
                 {@link de.elo.ix.client.feed.Action#getGuid()} or
                 {@link de.elo.ix.client.feed.HashTag#getHstgGuid()}.
            user_guid (Union[Unset, str]): GUID of user who registered the subscription.
    """

    create_date_iso: Union[Unset, str] = UNSET
    watch_guid: Union[Unset, str] = UNSET
    user_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_date_iso = self.create_date_iso

        watch_guid = self.watch_guid

        user_guid = self.user_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if watch_guid is not UNSET:
            field_dict["watchGuid"] = watch_guid
        if user_guid is not UNSET:
            field_dict["userGuid"] = user_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_date_iso = d.pop("createDateIso", UNSET)

        watch_guid = d.pop("watchGuid", UNSET)

        user_guid = d.pop("userGuid", UNSET)

        subscription = cls(
            create_date_iso=create_date_iso,
            watch_guid=watch_guid,
            user_guid=user_guid,
        )

        subscription.additional_properties = d
        return subscription

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
