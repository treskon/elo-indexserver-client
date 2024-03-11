from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestFeedServiceCreateHashTagSubscription")


@_attrs_define
class BRequestFeedServiceCreateHashTagSubscription:
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
        hashtag_guid_or_name (Union[Unset, str]):
        user_guid_or_id (Union[Unset, str]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    hashtag_guid_or_name: Union[Unset, str] = UNSET
    user_guid_or_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        hashtag_guid_or_name = self.hashtag_guid_or_name
        user_guid_or_id = self.user_guid_or_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if hashtag_guid_or_name is not UNSET:
            field_dict["hashtagGuidOrName"] = hashtag_guid_or_name
        if user_guid_or_id is not UNSET:
            field_dict["userGuidOrId"] = user_guid_or_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        hashtag_guid_or_name = d.pop("hashtagGuidOrName", UNSET)

        user_guid_or_id = d.pop("userGuidOrId", UNSET)

        b_request_feed_service_create_hash_tag_subscription = cls(
            ci=ci,
            hashtag_guid_or_name=hashtag_guid_or_name,
            user_guid_or_id=user_guid_or_id,
        )

        b_request_feed_service_create_hash_tag_subscription.additional_properties = d
        return b_request_feed_service_create_hash_tag_subscription

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
