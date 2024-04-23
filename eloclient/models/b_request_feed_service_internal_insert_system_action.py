from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestFeedServiceInternalInsertSystemAction")


@_attrs_define
class BRequestFeedServiceInternalInsertSystemAction:
    """
    Attributes:
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
        action (Union[Unset, Action]): This class describes an entry in a document feed.
            There are three kinds of entries/actions in
             general. First, an action can be a comment added manually by a user. Second, scripts or programs
             can insert actions e.g. to notify about a particular state. Third, actions are generated by the
             system e.g. when a new document version is created. In order to add an action to a feed, call
             {@link FeedService#checkinAction(de.elo.ix.client.ClientInfo, Action, ActionZ)}. User comments
             can have a parent action to support a two level hierarchy of entries.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    action: Union[Unset, "Action"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action import Action
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _action = d.pop("action", UNSET)
        action: Union[Unset, Action]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = Action.from_dict(_action)

        b_request_feed_service_internal_insert_system_action = cls(
            ci=ci,
            action=action,
        )

        b_request_feed_service_internal_insert_system_action.additional_properties = d
        return b_request_feed_service_internal_insert_system_action

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
