from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.feed_notification import FeedNotification


T = TypeVar("T", bound="BRequestFeedServiceRegisterNotify")


@_attrs_define
class BRequestFeedServiceRegisterNotify:
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
        feed_guid (Union[Unset, str]):
        notify (Union[Unset, FeedNotification]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    feed_guid: Union[Unset, str] = UNSET
    notify: Union[Unset, "FeedNotification"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        feed_guid = self.feed_guid
        notify: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notify, Unset):
            notify = self.notify.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if feed_guid is not UNSET:
            field_dict["feedGuid"] = feed_guid
        if notify is not UNSET:
            field_dict["notify"] = notify

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.feed_notification import FeedNotification

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        feed_guid = d.pop("feedGuid", UNSET)

        _notify = d.pop("notify", UNSET)
        notify: Union[Unset, FeedNotification]
        if isinstance(_notify, Unset):
            notify = UNSET
        else:
            notify = FeedNotification.from_dict(_notify)

        b_request_feed_service_register_notify = cls(
            ci=ci,
            feed_guid=feed_guid,
            notify=notify,
        )

        b_request_feed_service_register_notify.additional_properties = d
        return b_request_feed_service_register_notify

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
