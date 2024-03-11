from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_z import ActionZ
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestFeedServiceFindNextActions")


@_attrs_define
class BRequestFeedServiceFindNextActions:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        search_id (Union[Unset, str]):
        idx (Union[Unset, int]):
        max_ (Union[Unset, int]):
        action_z (Union[Unset, ActionZ]): Type safe element selector for class Action.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    search_id: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    max_: Union[Unset, int] = UNSET
    action_z: Union[Unset, "ActionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        search_id = self.search_id
        idx = self.idx
        max_ = self.max_
        action_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action_z, Unset):
            action_z = self.action_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if max_ is not UNSET:
            field_dict["max"] = max_
        if action_z is not UNSET:
            field_dict["actionZ"] = action_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_z import ActionZ
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        search_id = d.pop("searchId", UNSET)

        idx = d.pop("idx", UNSET)

        max_ = d.pop("max", UNSET)

        _action_z = d.pop("actionZ", UNSET)
        action_z: Union[Unset, ActionZ]
        if isinstance(_action_z, Unset):
            action_z = UNSET
        else:
            action_z = ActionZ.from_dict(_action_z)

        b_request_feed_service_find_next_actions = cls(
            ci=ci,
            search_id=search_id,
            idx=idx,
            max_=max_,
            action_z=action_z,
        )

        b_request_feed_service_find_next_actions.additional_properties = d
        return b_request_feed_service_find_next_actions

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
