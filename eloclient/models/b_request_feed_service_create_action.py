from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.e_action_type import EActionType


T = TypeVar("T", bound="BRequestFeedServiceCreateAction")


@_attrs_define
class BRequestFeedServiceCreateAction:
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
        type (Union[Unset, EActionType]): Types of document feed entries.
        parent_guid (Union[Unset, str]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    type: Union[Unset, "EActionType"] = UNSET
    parent_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        parent_guid = self.parent_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if type is not UNSET:
            field_dict["type"] = type
        if parent_guid is not UNSET:
            field_dict["parentGuid"] = parent_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.e_action_type import EActionType

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EActionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EActionType.from_dict(_type)

        parent_guid = d.pop("parentGuid", UNSET)

        b_request_feed_service_create_action = cls(
            ci=ci,
            type=type,
            parent_guid=parent_guid,
        )

        b_request_feed_service_create_action.additional_properties = d
        return b_request_feed_service_create_action

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
