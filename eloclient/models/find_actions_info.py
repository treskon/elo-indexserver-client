from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.e_action_type import EActionType
    from ..models.find_result_access_mode import FindResultAccessMode
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="FindActionsInfo")


@_attrs_define
class FindActionsInfo:
    """Describes search criteria for
    {@link FeedService#findFirstActions(de.elo.ix.client.ClientInfo, FindActionsInfo, int, ActionZ)}.
     <p>
     If only objId is set, userId and createDateIso is empty, the entire document feed of the given
     object is returned. The (main) actions are sorted descending by create date. The answers (child
     actions) follow immediately their associated main action. Answers are sorted ascending by create
     date.
     </p>
     <p>
     If any other member is also set, or if objId is combined with another member, the search combines
     the elements by logical AND. The result list contains all actions sorted descending by create
     date. The ordering does not distinguish between main actions and child actions.
     </p>

        Attributes:
            space_guid (Union[Unset, str]): Collect feed actions of all items in a teamspace or workspace.
                This option contains the
                 {@link Sord#getGuid()} of a teamspace or workspace and can only be combinded with
                 {@link #createDateIso}, {@link #actionTypes}, {@link #userId}, and {@link #sordZ}.
            sord_z (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            create_date_iso (Union[Unset, str]): Search by create date. A date range can be specified by using the default
                range delimiter "...
                "
                 or the one defined in {@link de.elo.ix.client.FindOptions#getRangeDelimiter()}. The time part
                 is assumed to be in the timezone defined by {@link ClientInfo#getTimeZone()}.
            obj_id (Union[Unset, str]): Search by Sord ID, GUID, etc.
                This value can be an ID, a GUID or an expression as defined in
                 {@link de.elo.ix.client.IXServicePortIF#checkoutSord(de.elo.ix.client.ClientInfo, String,
                de.elo.ix.client.EditInfoZ, de.elo.ix.client.LockZ)}.
            find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
                find results.
            user_id (Union[Unset, str]): Search by user ID, GUID, name.
            find_notifications (Union[Unset, bool]): Search for notifications.
                If this member is true, only those actions are found for which the
                 user was notified.
            find_subscriptions (Union[Unset, bool]): If true a Map&lt;String, Subscription&gt; will be set in the FindResult
            action_types (Union[Unset, List['EActionType']]):
            find_hash_tags (Union[Unset, bool]): Search for HashTags If this member is true, all HashTags within the action
                will be returned
    """

    space_guid: Union[Unset, str] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    user_id: Union[Unset, str] = UNSET
    find_notifications: Union[Unset, bool] = UNSET
    find_subscriptions: Union[Unset, bool] = UNSET
    action_types: Union[Unset, List["EActionType"]] = UNSET
    find_hash_tags: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        space_guid = self.space_guid

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        create_date_iso = self.create_date_iso

        obj_id = self.obj_id

        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        user_id = self.user_id

        find_notifications = self.find_notifications

        find_subscriptions = self.find_subscriptions

        action_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.action_types, Unset):
            action_types = []
            for componentsschemas_list_of_e_action_type_item_data in self.action_types:
                componentsschemas_list_of_e_action_type_item = (
                    componentsschemas_list_of_e_action_type_item_data.to_dict()
                )
                action_types.append(componentsschemas_list_of_e_action_type_item)

        find_hash_tags = self.find_hash_tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if space_guid is not UNSET:
            field_dict["spaceGuid"] = space_guid
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if find_notifications is not UNSET:
            field_dict["findNotifications"] = find_notifications
        if find_subscriptions is not UNSET:
            field_dict["findSubscriptions"] = find_subscriptions
        if action_types is not UNSET:
            field_dict["actionTypes"] = action_types
        if find_hash_tags is not UNSET:
            field_dict["findHashTags"] = find_hash_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_action_type import EActionType
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        space_guid = d.pop("spaceGuid", UNSET)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        create_date_iso = d.pop("createDateIso", UNSET)

        obj_id = d.pop("objId", UNSET)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        user_id = d.pop("userId", UNSET)

        find_notifications = d.pop("findNotifications", UNSET)

        find_subscriptions = d.pop("findSubscriptions", UNSET)

        action_types = []
        _action_types = d.pop("actionTypes", UNSET)
        for componentsschemas_list_of_e_action_type_item_data in _action_types or []:
            componentsschemas_list_of_e_action_type_item = EActionType.from_dict(
                componentsschemas_list_of_e_action_type_item_data
            )

            action_types.append(componentsschemas_list_of_e_action_type_item)

        find_hash_tags = d.pop("findHashTags", UNSET)

        find_actions_info = cls(
            space_guid=space_guid,
            sord_z=sord_z,
            create_date_iso=create_date_iso,
            obj_id=obj_id,
            find_result_access_mode=find_result_access_mode,
            user_id=user_id,
            find_notifications=find_notifications,
            find_subscriptions=find_subscriptions,
            action_types=action_types,
            find_hash_tags=find_hash_tags,
        )

        find_actions_info.additional_properties = d
        return find_actions_info

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
