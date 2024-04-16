from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.hash_tag_relation import HashTagRelation
    from ..models.map_to_feed import MapToFeed
    from ..models.map_to_hash_tag import MapToHashTag
    from ..models.map_to_notification import MapToNotification
    from ..models.map_to_subscription import MapToSubscription
    from ..models.sord import Sord
    from ..models.user_task import UserTask
    from ..models.wf_diagram import WFDiagram


T = TypeVar("T", bound="MyELOContent")


@_attrs_define
class MyELOContent:
    """
    Attributes:
        subscriptions (Union[Unset, MapToSubscription]):
        hash_tags (Union[Unset, MapToHashTag]):
        hash_tag_relations (Union[Unset, List['HashTagRelation']]):
        feeds (Union[Unset, MapToFeed]):
        workflows (Union[Unset, List['WFDiagram']]):
        sords (Union[Unset, List['Sord']]):
        actions (Union[Unset, List['Action']]):
        tasks (Union[Unset, List['UserTask']]):
        notifications (Union[Unset, MapToNotification]):
    """

    subscriptions: Union[Unset, "MapToSubscription"] = UNSET
    hash_tags: Union[Unset, "MapToHashTag"] = UNSET
    hash_tag_relations: Union[Unset, List["HashTagRelation"]] = UNSET
    feeds: Union[Unset, "MapToFeed"] = UNSET
    workflows: Union[Unset, List["WFDiagram"]] = UNSET
    sords: Union[Unset, List["Sord"]] = UNSET
    actions: Union[Unset, List["Action"]] = UNSET
    tasks: Union[Unset, List["UserTask"]] = UNSET
    notifications: Union[Unset, "MapToNotification"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        hash_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hash_tags, Unset):
            hash_tags = self.hash_tags.to_dict()

        hash_tag_relations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hash_tag_relations, Unset):
            hash_tag_relations = []
            for componentsschemas_list_of_hash_tag_relation_item_data in self.hash_tag_relations:
                componentsschemas_list_of_hash_tag_relation_item = (
                    componentsschemas_list_of_hash_tag_relation_item_data.to_dict()
                )
                hash_tag_relations.append(componentsschemas_list_of_hash_tag_relation_item)

        feeds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feeds, Unset):
            feeds = self.feeds.to_dict()

        workflows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        sords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sords, Unset):
            sords = []
            for sords_item_data in self.sords:
                sords_item = sords_item_data.to_dict()
                sords.append(sords_item)

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if hash_tags is not UNSET:
            field_dict["hashTags"] = hash_tags
        if hash_tag_relations is not UNSET:
            field_dict["hashTagRelations"] = hash_tag_relations
        if feeds is not UNSET:
            field_dict["feeds"] = feeds
        if workflows is not UNSET:
            field_dict["workflows"] = workflows
        if sords is not UNSET:
            field_dict["sords"] = sords
        if actions is not UNSET:
            field_dict["actions"] = actions
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action import Action
        from ..models.hash_tag_relation import HashTagRelation
        from ..models.map_to_feed import MapToFeed
        from ..models.map_to_hash_tag import MapToHashTag
        from ..models.map_to_notification import MapToNotification
        from ..models.map_to_subscription import MapToSubscription
        from ..models.sord import Sord
        from ..models.user_task import UserTask
        from ..models.wf_diagram import WFDiagram

        d = src_dict.copy()
        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: Union[Unset, MapToSubscription]
        if isinstance(_subscriptions, Unset):
            subscriptions = UNSET
        else:
            subscriptions = MapToSubscription.from_dict(_subscriptions)

        _hash_tags = d.pop("hashTags", UNSET)
        hash_tags: Union[Unset, MapToHashTag]
        if isinstance(_hash_tags, Unset):
            hash_tags = UNSET
        else:
            hash_tags = MapToHashTag.from_dict(_hash_tags)

        hash_tag_relations = []
        _hash_tag_relations = d.pop("hashTagRelations", UNSET)
        for componentsschemas_list_of_hash_tag_relation_item_data in _hash_tag_relations or []:
            componentsschemas_list_of_hash_tag_relation_item = HashTagRelation.from_dict(
                componentsschemas_list_of_hash_tag_relation_item_data
            )

            hash_tag_relations.append(componentsschemas_list_of_hash_tag_relation_item)

        _feeds = d.pop("feeds", UNSET)
        feeds: Union[Unset, MapToFeed]
        if isinstance(_feeds, Unset):
            feeds = UNSET
        else:
            feeds = MapToFeed.from_dict(_feeds)

        workflows = []
        _workflows = d.pop("workflows", UNSET)
        for workflows_item_data in _workflows or []:
            workflows_item = WFDiagram.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        sords = []
        _sords = d.pop("sords", UNSET)
        for sords_item_data in _sords or []:
            sords_item = Sord.from_dict(sords_item_data)

            sords.append(sords_item)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = Action.from_dict(actions_item_data)

            actions.append(actions_item)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = UserTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        _notifications = d.pop("notifications", UNSET)
        notifications: Union[Unset, MapToNotification]
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = MapToNotification.from_dict(_notifications)

        my_elo_content = cls(
            subscriptions=subscriptions,
            hash_tags=hash_tags,
            hash_tag_relations=hash_tag_relations,
            feeds=feeds,
            workflows=workflows,
            sords=sords,
            actions=actions,
            tasks=tasks,
            notifications=notifications,
        )

        my_elo_content.additional_properties = d
        return my_elo_content

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
