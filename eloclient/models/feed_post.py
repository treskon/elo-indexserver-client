from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action


T = TypeVar("T", bound="FeedPost")


@_attrs_define
class FeedPost:
    """A FeedPost contains a parent action (an action where action.
    parentGuid is empty) and all subactions (actions where
     action.parentGuid = parent action's guid).

     From all actions their information (e.g. hashtags, mentions) are accumulated into lists.

        Attributes:
            parent_action (Union[Unset, Action]): This class describes an entry in a document feed. There are three kinds of
                entries/actions in general.
                First, an
                 action can be a comment added manually by a user. Second, scripts or programs can insert actions e.g. to notify
                about
                 a particular state. Third, actions are generated by the system e.g. when a new document version is created. In
                order
                 to add an action to a feed, call {@link FeedService#checkinAction(de.elo.ix.client.ClientInfo, Action,
                ActionZ)}.
                 User comments can have a parent action to support a two level hierarchy of entries.
            sord_guid (Union[Unset, str]): GUID of corresponsing Sord
            feed_guid (Union[Unset, str]): GUID of corresponding feed (read from parentAction.
                feedGuid)
            sub_actions (Union[Unset, List['Action']]):
            hash_tags (Union[Unset, List[str]]):
            mentions (Union[Unset, List[str]]):
            linked_guids (Union[Unset, List[str]]):
            creator_ids (Union[Unset, List[int]]):
            text (Union[Unset, str]): Text of all actions, separated by a whitespace
            text_list (Union[Unset, List[str]]):
            last_changed (Union[Unset, str]): Date of last change of any action
            version_name (Union[Unset, str]): Name of corresponding DocVersion if parentAction.getDocVersionGuid() is set.
            version_comment (Union[Unset, str]): Version comment of corresponding DocVersion if
                parentAction.getDocVersionGuid() is set.
    """

    parent_action: Union[Unset, "Action"] = UNSET
    sord_guid: Union[Unset, str] = UNSET
    feed_guid: Union[Unset, str] = UNSET
    sub_actions: Union[Unset, List["Action"]] = UNSET
    hash_tags: Union[Unset, List[str]] = UNSET
    mentions: Union[Unset, List[str]] = UNSET
    linked_guids: Union[Unset, List[str]] = UNSET
    creator_ids: Union[Unset, List[int]] = UNSET
    text: Union[Unset, str] = UNSET
    text_list: Union[Unset, List[str]] = UNSET
    last_changed: Union[Unset, str] = UNSET
    version_name: Union[Unset, str] = UNSET
    version_comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_action, Unset):
            parent_action = self.parent_action.to_dict()

        sord_guid = self.sord_guid
        feed_guid = self.feed_guid
        sub_actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_actions, Unset):
            sub_actions = []
            for componentsschemas_list_of_action_item_data in self.sub_actions:
                componentsschemas_list_of_action_item = componentsschemas_list_of_action_item_data.to_dict()

                sub_actions.append(componentsschemas_list_of_action_item)

        hash_tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hash_tags, Unset):
            hash_tags = self.hash_tags

        mentions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = self.mentions

        linked_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.linked_guids, Unset):
            linked_guids = self.linked_guids

        creator_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.creator_ids, Unset):
            creator_ids = self.creator_ids

        text = self.text
        text_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.text_list, Unset):
            text_list = self.text_list

        last_changed = self.last_changed
        version_name = self.version_name
        version_comment = self.version_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_action is not UNSET:
            field_dict["parentAction"] = parent_action
        if sord_guid is not UNSET:
            field_dict["sordGuid"] = sord_guid
        if feed_guid is not UNSET:
            field_dict["feedGuid"] = feed_guid
        if sub_actions is not UNSET:
            field_dict["subActions"] = sub_actions
        if hash_tags is not UNSET:
            field_dict["hashTags"] = hash_tags
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if linked_guids is not UNSET:
            field_dict["linkedGuids"] = linked_guids
        if creator_ids is not UNSET:
            field_dict["creatorIds"] = creator_ids
        if text is not UNSET:
            field_dict["text"] = text
        if text_list is not UNSET:
            field_dict["textList"] = text_list
        if last_changed is not UNSET:
            field_dict["lastChanged"] = last_changed
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if version_comment is not UNSET:
            field_dict["versionComment"] = version_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action import Action

        d = src_dict.copy()
        _parent_action = d.pop("parentAction", UNSET)
        parent_action: Union[Unset, Action]
        if isinstance(_parent_action, Unset):
            parent_action = UNSET
        else:
            parent_action = Action.from_dict(_parent_action)

        sord_guid = d.pop("sordGuid", UNSET)

        feed_guid = d.pop("feedGuid", UNSET)

        sub_actions = []
        _sub_actions = d.pop("subActions", UNSET)
        for componentsschemas_list_of_action_item_data in _sub_actions or []:
            componentsschemas_list_of_action_item = Action.from_dict(componentsschemas_list_of_action_item_data)

            sub_actions.append(componentsschemas_list_of_action_item)

        hash_tags = cast(List[str], d.pop("hashTags", UNSET))

        mentions = cast(List[str], d.pop("mentions", UNSET))

        linked_guids = cast(List[str], d.pop("linkedGuids", UNSET))

        creator_ids = cast(List[int], d.pop("creatorIds", UNSET))

        text = d.pop("text", UNSET)

        text_list = cast(List[str], d.pop("textList", UNSET))

        last_changed = d.pop("lastChanged", UNSET)

        version_name = d.pop("versionName", UNSET)

        version_comment = d.pop("versionComment", UNSET)

        feed_post = cls(
            parent_action=parent_action,
            sord_guid=sord_guid,
            feed_guid=feed_guid,
            sub_actions=sub_actions,
            hash_tags=hash_tags,
            mentions=mentions,
            linked_guids=linked_guids,
            creator_ids=creator_ids,
            text=text,
            text_list=text_list,
            last_changed=last_changed,
            version_name=version_name,
            version_comment=version_comment,
        )

        feed_post.additional_properties = d
        return feed_post

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