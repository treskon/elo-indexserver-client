from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_z import ActionZ
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="FindNotificationInfo")


@_attrs_define
class FindNotificationInfo:
    """FindInfo for FindFirstNotifications.

    Attributes:
        user_guid_or_id (Union[Unset, str]): GUID or ID or Name of the User. If null, current user will be set.
            If GUID/ID is not the
             current user, admin rights are needed to preform the search
        what (Union[Unset, int]): Reserved.
        sord_z (Union[Unset, SordZ]): <p>
            This class encapsulates the constants of <code>SordC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        action_z (Union[Unset, ActionZ]): Type safe element selector for class Action.
        create_date_iso (Union[Unset, str]): Search by create date. A date range can be specified by using the default
            range delimiter "...
            "
             or the one defined in {@link de.elo.ix.client.FindOptions#getRangeDelimiter()}.
        incl_important (Union[Unset, bool]): If true and createDateIso is set, it will also return all Notifications
            marked as Important
            even if they are not in the specified createDate range. If true and createDateIso is not set,
             it will return only Notifications marked as Important
        find_feeds (Union[Unset, bool]): If true a Map&lt;String, Feed&gt; will be set in the FindResult.
            by default true
        find_subscriptions (Union[Unset, bool]): If true a Map&lt;String, Subscription&gt; will be set in the FindResult
        find_hash_tags (Union[Unset, bool]): If true a List&lt;HashTagRelation&gt; and a Map&lt;String, HashTag&gt; will
            be set in the
            FindResult
    """

    user_guid_or_id: Union[Unset, str] = UNSET
    what: Union[Unset, int] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    action_z: Union[Unset, "ActionZ"] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    incl_important: Union[Unset, bool] = UNSET
    find_feeds: Union[Unset, bool] = UNSET
    find_subscriptions: Union[Unset, bool] = UNSET
    find_hash_tags: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_guid_or_id = self.user_guid_or_id

        what = self.what

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        action_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action_z, Unset):
            action_z = self.action_z.to_dict()

        create_date_iso = self.create_date_iso

        incl_important = self.incl_important

        find_feeds = self.find_feeds

        find_subscriptions = self.find_subscriptions

        find_hash_tags = self.find_hash_tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_guid_or_id is not UNSET:
            field_dict["userGuidOrID"] = user_guid_or_id
        if what is not UNSET:
            field_dict["what"] = what
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if action_z is not UNSET:
            field_dict["actionZ"] = action_z
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if incl_important is not UNSET:
            field_dict["inclImportant"] = incl_important
        if find_feeds is not UNSET:
            field_dict["findFeeds"] = find_feeds
        if find_subscriptions is not UNSET:
            field_dict["findSubscriptions"] = find_subscriptions
        if find_hash_tags is not UNSET:
            field_dict["findHashTags"] = find_hash_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_z import ActionZ
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        user_guid_or_id = d.pop("userGuidOrID", UNSET)

        what = d.pop("what", UNSET)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        _action_z = d.pop("actionZ", UNSET)
        action_z: Union[Unset, ActionZ]
        if isinstance(_action_z, Unset):
            action_z = UNSET
        else:
            action_z = ActionZ.from_dict(_action_z)

        create_date_iso = d.pop("createDateIso", UNSET)

        incl_important = d.pop("inclImportant", UNSET)

        find_feeds = d.pop("findFeeds", UNSET)

        find_subscriptions = d.pop("findSubscriptions", UNSET)

        find_hash_tags = d.pop("findHashTags", UNSET)

        find_notification_info = cls(
            user_guid_or_id=user_guid_or_id,
            what=what,
            sord_z=sord_z,
            action_z=action_z,
            create_date_iso=create_date_iso,
            incl_important=incl_important,
            find_feeds=find_feeds,
            find_subscriptions=find_subscriptions,
            find_hash_tags=find_hash_tags,
        )

        find_notification_info.additional_properties = d
        return find_notification_info

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
