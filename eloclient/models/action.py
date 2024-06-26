from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.action_history import ActionHistory
    from ..models.doc_version import DocVersion
    from ..models.e_action_type import EActionType
    from ..models.wf_diagram import WFDiagram


T = TypeVar("T", bound="Action")


@_attrs_define
class Action:
    """This class describes an entry in a document feed.
    There are three kinds of entries/actions in
     general. First, an action can be a comment added manually by a user. Second, scripts or programs
     can insert actions e.g. to notify about a particular state. Third, actions are generated by the
     system e.g. when a new document version is created. In order to add an action to a feed, call
     {@link FeedService#checkinAction(de.elo.ix.client.ClientInfo, Action, ActionZ)}. User comments
     can have a parent action to support a two level hierarchy of entries.

        Attributes:
            workflow (Union[Unset, WFDiagram]): This class represents an active or finished workflow or a workflow template
            history (Union[Unset, List['ActionHistory']]):
            acl (Union[Unset, str]): Raw ACL representation.
                Only valid for Actions of type {@link EActionType#UserComment} or
                 {@link EActionType#AutoComment}. This member is ignored if {@link Action#aclItems} is not null.
            type (Union[Unset, EActionType]): Types of document feed entries.
            user_guid (Union[Unset, str]): User GUID. The GUID of the user who has created this action.
                For actions of type
                 {@link EActionType#SordCreated}, this member holds the GUID of Sord.ownerId. For actions of
                 type {@link EActionType#VersionCreated}, this member holds the GUID of DocVersion.ownerId.
            user_name (Union[Unset, str]): User name. It is set to the name of the user given by {@link #userGuid}.
                This element is
                 read-only.
            user_id (Union[Unset, int]): User ID. It is set to the numerical ID of the user given by {@link #userGuid}.
                This element is
                 read-only.
            feed_guid (Union[Unset, str]): Feed GUID. This action belongs to the feed identified by this GUID.
            change_counter (Union[Unset, int]): Counts the number of updates. This element is only valid for {@link
                EActionType#UserComment}.
                It counts the number of updates made to the comment.
            t_stamp (Union[Unset, str]): Time stamp. Time stamp of creation or modification.
            update_date_iso (Union[Unset, str]): Update date. This element is only valid for {@link
                EActionType#UserComment}.
                It holds the ISO
                 formatted update date. When this object is received from
                 {@link FeedService#checkoutAction(de.elo.ix.client.ClientInfo, String, ActionZ)} or
                 {@link FeedService#findFirstActions(de.elo.ix.client.ClientInfo, FindActionsInfo, int, ActionZ)}
                 the value is supplied in the time zone of the client application - which is UTC by default. In
                 case of the object is received by a notify message in
                 {@link FeedNotification#updateAction(Action)} the value is relative to the UTC timezone. In
                 order to convert this value into a date object, invoke function
                 {@link de.elo.ix.client.IXConnection#isoToDate}.
            create_date_iso (Union[Unset, str]): Create date. This element is the ISO formatted create date of the action.
                When this object is
                 received from {@link FeedService#checkoutAction(de.elo.ix.client.ClientInfo, String, ActionZ)}
                 or
                 {@link FeedService#findFirstActions(de.elo.ix.client.ClientInfo, FindActionsInfo, int, ActionZ)}
                 the value is supplied in the time zone of the client application - which is UTC by default. In
                 case of the object is received by a notify message in
                 {@link FeedNotification#updateAction(Action)} the value is relative to the UTC timezone. In
                 order to convert this value into a date object, invoke function
                 {@link de.elo.ix.client.IXConnection#isoToDate}.
            doc_version_guid (Union[Unset, str]): GUID of the associated document version.
                This element is only valid for generated actions that
                 belong to a document version, e.g. {@link EActionType#VersionCreated}. Read-only.
            workflow_guid (Union[Unset, str]): GUID of the associated workflow.
                This element is valid for action types that belong to a
                 workflow.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            parent_guid (Union[Unset, str]): Parent action GUID.
                This element is only valid for user comments,
                 {@link EActionType#UserComment}. If not empty, this action is subordinated under the action
                 given by this GUID.
            acl_items (Union[Unset, List['AclItem']]):
            guid (Union[Unset, str]): Action GUID. Unique identifier.
            text (Union[Unset, str]): Comment text.
                This element is only valid for {@link EActionType#UserComment}, and
                 {@link EActionType#AutoComment}.
            doc_version (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
    """

    workflow: Union[Unset, "WFDiagram"] = UNSET
    history: Union[Unset, List["ActionHistory"]] = UNSET
    acl: Union[Unset, str] = UNSET
    type: Union[Unset, "EActionType"] = UNSET
    user_guid: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    feed_guid: Union[Unset, str] = UNSET
    change_counter: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    update_date_iso: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    doc_version_guid: Union[Unset, str] = UNSET
    workflow_guid: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    parent_guid: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    guid: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    doc_version: Union[Unset, "DocVersion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for componentsschemas_list_of_action_history_item_data in self.history:
                componentsschemas_list_of_action_history_item = (
                    componentsschemas_list_of_action_history_item_data.to_dict()
                )
                history.append(componentsschemas_list_of_action_history_item)

        acl = self.acl

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        user_guid = self.user_guid

        user_name = self.user_name

        user_id = self.user_id

        feed_guid = self.feed_guid

        change_counter = self.change_counter

        t_stamp = self.t_stamp

        update_date_iso = self.update_date_iso

        create_date_iso = self.create_date_iso

        doc_version_guid = self.doc_version_guid

        workflow_guid = self.workflow_guid

        t_stamp_sync = self.t_stamp_sync

        parent_guid = self.parent_guid

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        guid = self.guid

        text = self.text

        doc_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_version, Unset):
            doc_version = self.doc_version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if history is not UNSET:
            field_dict["history"] = history
        if acl is not UNSET:
            field_dict["acl"] = acl
        if type is not UNSET:
            field_dict["type"] = type
        if user_guid is not UNSET:
            field_dict["userGuid"] = user_guid
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if feed_guid is not UNSET:
            field_dict["feedGuid"] = feed_guid
        if change_counter is not UNSET:
            field_dict["changeCounter"] = change_counter
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if update_date_iso is not UNSET:
            field_dict["updateDateIso"] = update_date_iso
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if doc_version_guid is not UNSET:
            field_dict["docVersionGuid"] = doc_version_guid
        if workflow_guid is not UNSET:
            field_dict["workflowGuid"] = workflow_guid
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if parent_guid is not UNSET:
            field_dict["parentGuid"] = parent_guid
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if guid is not UNSET:
            field_dict["guid"] = guid
        if text is not UNSET:
            field_dict["text"] = text
        if doc_version is not UNSET:
            field_dict["docVersion"] = doc_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.action_history import ActionHistory
        from ..models.doc_version import DocVersion
        from ..models.e_action_type import EActionType
        from ..models.wf_diagram import WFDiagram

        d = src_dict.copy()
        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WFDiagram]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WFDiagram.from_dict(_workflow)

        history = []
        _history = d.pop("history", UNSET)
        for componentsschemas_list_of_action_history_item_data in _history or []:
            componentsschemas_list_of_action_history_item = ActionHistory.from_dict(
                componentsschemas_list_of_action_history_item_data
            )

            history.append(componentsschemas_list_of_action_history_item)

        acl = d.pop("acl", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EActionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EActionType.from_dict(_type)

        user_guid = d.pop("userGuid", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        feed_guid = d.pop("feedGuid", UNSET)

        change_counter = d.pop("changeCounter", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        update_date_iso = d.pop("updateDateIso", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        doc_version_guid = d.pop("docVersionGuid", UNSET)

        workflow_guid = d.pop("workflowGuid", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        parent_guid = d.pop("parentGuid", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        guid = d.pop("guid", UNSET)

        text = d.pop("text", UNSET)

        _doc_version = d.pop("docVersion", UNSET)
        doc_version: Union[Unset, DocVersion]
        if isinstance(_doc_version, Unset):
            doc_version = UNSET
        else:
            doc_version = DocVersion.from_dict(_doc_version)

        action = cls(
            workflow=workflow,
            history=history,
            acl=acl,
            type=type,
            user_guid=user_guid,
            user_name=user_name,
            user_id=user_id,
            feed_guid=feed_guid,
            change_counter=change_counter,
            t_stamp=t_stamp,
            update_date_iso=update_date_iso,
            create_date_iso=create_date_iso,
            doc_version_guid=doc_version_guid,
            workflow_guid=workflow_guid,
            t_stamp_sync=t_stamp_sync,
            parent_guid=parent_guid,
            acl_items=acl_items,
            guid=guid,
            text=text,
            doc_version=doc_version,
        )

        action.additional_properties = d
        return action

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
