from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_z import ActionZ
    from ..models.find_result_access_mode import FindResultAccessMode
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="FindHashTagInfo")


@_attrs_define
class FindHashTagInfo:
    """
    Attributes:
        hashtag_guid_or_name (Union[Unset, str]): HashTag Guid or Name
        create_date_iso (Union[Unset, str]): Search by create date. A date range can be specified by using the default
            range delimiter "...
            " or the one defined
             in {@link de.elo.ix.client.FindOptions#getRangeDelimiter()}.
        last_used_iso (Union[Unset, str]): Search by last used. A date range can be specified by using the default range
            delimiter "...
            " or the one defined in
             {@link de.elo.ix.client.FindOptions#getRangeDelimiter()}.
        min_count (Union[Unset, int]): Filter the result by number of use.
            Only HashTags with >= minCount will be returned
        action_z (Union[Unset, ActionZ]): Type safe element selector for class Action.
        sord_z (Union[Unset, SordZ]): <p>
            This class encapsulates the constants of <code>SordC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        find_feeds (Union[Unset, bool]): If true a Map&lt;String, Feed&gt; will be set in the FindResult.
            by default true
        find_hash_tags (Union[Unset, bool]):
        find_subscriptions (Union[Unset, bool]): If true a Map&lt;String, Subscription&gt; will be set in the FindResult
        find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
            find results.
    """

    hashtag_guid_or_name: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    last_used_iso: Union[Unset, str] = UNSET
    min_count: Union[Unset, int] = UNSET
    action_z: Union[Unset, "ActionZ"] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    find_feeds: Union[Unset, bool] = UNSET
    find_hash_tags: Union[Unset, bool] = UNSET
    find_subscriptions: Union[Unset, bool] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hashtag_guid_or_name = self.hashtag_guid_or_name
        create_date_iso = self.create_date_iso
        last_used_iso = self.last_used_iso
        min_count = self.min_count
        action_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action_z, Unset):
            action_z = self.action_z.to_dict()

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        find_feeds = self.find_feeds
        find_hash_tags = self.find_hash_tags
        find_subscriptions = self.find_subscriptions
        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hashtag_guid_or_name is not UNSET:
            field_dict["hashtagGuidOrName"] = hashtag_guid_or_name
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if last_used_iso is not UNSET:
            field_dict["lastUsedIso"] = last_used_iso
        if min_count is not UNSET:
            field_dict["minCount"] = min_count
        if action_z is not UNSET:
            field_dict["actionZ"] = action_z
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if find_feeds is not UNSET:
            field_dict["findFeeds"] = find_feeds
        if find_hash_tags is not UNSET:
            field_dict["findHashTags"] = find_hash_tags
        if find_subscriptions is not UNSET:
            field_dict["findSubscriptions"] = find_subscriptions
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_z import ActionZ
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        hashtag_guid_or_name = d.pop("hashtagGuidOrName", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        last_used_iso = d.pop("lastUsedIso", UNSET)

        min_count = d.pop("minCount", UNSET)

        _action_z = d.pop("actionZ", UNSET)
        action_z: Union[Unset, ActionZ]
        if isinstance(_action_z, Unset):
            action_z = UNSET
        else:
            action_z = ActionZ.from_dict(_action_z)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        find_feeds = d.pop("findFeeds", UNSET)

        find_hash_tags = d.pop("findHashTags", UNSET)

        find_subscriptions = d.pop("findSubscriptions", UNSET)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        find_hash_tag_info = cls(
            hashtag_guid_or_name=hashtag_guid_or_name,
            create_date_iso=create_date_iso,
            last_used_iso=last_used_iso,
            min_count=min_count,
            action_z=action_z,
            sord_z=sord_z,
            find_feeds=find_feeds,
            find_hash_tags=find_hash_tags,
            find_subscriptions=find_subscriptions,
            find_result_access_mode=find_result_access_mode,
        )

        find_hash_tag_info.additional_properties = d
        return find_hash_tag_info

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
