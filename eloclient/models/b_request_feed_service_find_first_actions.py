from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_z import ActionZ
    from ..models.client_info import ClientInfo
    from ..models.find_actions_info import FindActionsInfo


T = TypeVar("T", bound="BRequestFeedServiceFindFirstActions")


@_attrs_define
class BRequestFeedServiceFindFirstActions:
    """
    Attributes:
        action_z (Union[Unset, ActionZ]): Type safe element selector for class Action.
        max_ (Union[Unset, int]):
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        find_info (Union[Unset, FindActionsInfo]): Describes search criteria for
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
    """

    action_z: Union[Unset, "ActionZ"] = UNSET
    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    find_info: Union[Unset, "FindActionsInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action_z, Unset):
            action_z = self.action_z.to_dict()

        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_z is not UNSET:
            field_dict["actionZ"] = action_z
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_z import ActionZ
        from ..models.client_info import ClientInfo
        from ..models.find_actions_info import FindActionsInfo

        d = src_dict.copy()
        _action_z = d.pop("actionZ", UNSET)
        action_z: Union[Unset, ActionZ]
        if isinstance(_action_z, Unset):
            action_z = UNSET
        else:
            action_z = ActionZ.from_dict(_action_z)

        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindActionsInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindActionsInfo.from_dict(_find_info)

        b_request_feed_service_find_first_actions = cls(
            action_z=action_z,
            max_=max_,
            ci=ci,
            find_info=find_info,
        )

        b_request_feed_service_find_first_actions.additional_properties = d
        return b_request_feed_service_find_first_actions

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
