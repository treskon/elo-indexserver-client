from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.subscription import Subscription
    from ..models.subscription_z import SubscriptionZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinSubscription")


@_attrs_define
class BRequestIXServicePortIFCheckinSubscription:
    """
    Attributes:
        subs (Union[Unset, Subscription]): This class describes a subscription. A user can subscribe for changes to an
            object.
            Currently,
             the only supported object type is a document feed. If the feed receives new comments,
             notification information is inserted into the database for the user. By calling
             FeedService.findFirstActions and setting FindActionsInfo.findNotifications=true, the user can
             search for her notifications.
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
        subs_z (Union[Unset, SubscriptionZ]):
    """

    subs: Union[Unset, "Subscription"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    subs_z: Union[Unset, "SubscriptionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subs, Unset):
            subs = self.subs.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        subs_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subs_z, Unset):
            subs_z = self.subs_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subs is not UNSET:
            field_dict["subs"] = subs
        if ci is not UNSET:
            field_dict["ci"] = ci
        if subs_z is not UNSET:
            field_dict["subsZ"] = subs_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.subscription import Subscription
        from ..models.subscription_z import SubscriptionZ

        d = src_dict.copy()
        _subs = d.pop("subs", UNSET)
        subs: Union[Unset, Subscription]
        if isinstance(_subs, Unset):
            subs = UNSET
        else:
            subs = Subscription.from_dict(_subs)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _subs_z = d.pop("subsZ", UNSET)
        subs_z: Union[Unset, SubscriptionZ]
        if isinstance(_subs_z, Unset):
            subs_z = UNSET
        else:
            subs_z = SubscriptionZ.from_dict(_subs_z)

        b_request_ix_service_port_if_checkin_subscription = cls(
            subs=subs,
            ci=ci,
            subs_z=subs_z,
        )

        b_request_ix_service_port_if_checkin_subscription.additional_properties = d
        return b_request_ix_service_port_if_checkin_subscription

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
