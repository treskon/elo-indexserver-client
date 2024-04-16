from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.find_subscription_info import FindSubscriptionInfo
    from ..models.subscription_z import SubscriptionZ


T = TypeVar("T", bound="BRequestIXServicePortIFFindFirstSubscriptions")


@_attrs_define
class BRequestIXServicePortIFFindFirstSubscriptions:
    """
    Attributes:
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
        find_info (Union[Unset, FindSubscriptionInfo]): Find criteria for function findFirstSubscriptions.
        subs_z (Union[Unset, SubscriptionZ]):
    """

    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    find_info: Union[Unset, "FindSubscriptionInfo"] = UNSET
    subs_z: Union[Unset, "SubscriptionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        subs_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subs_z, Unset):
            subs_z = self.subs_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info
        if subs_z is not UNSET:
            field_dict["subsZ"] = subs_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.find_subscription_info import FindSubscriptionInfo
        from ..models.subscription_z import SubscriptionZ

        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindSubscriptionInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindSubscriptionInfo.from_dict(_find_info)

        _subs_z = d.pop("subsZ", UNSET)
        subs_z: Union[Unset, SubscriptionZ]
        if isinstance(_subs_z, Unset):
            subs_z = UNSET
        else:
            subs_z = SubscriptionZ.from_dict(_subs_z)

        b_request_ix_service_port_if_find_first_subscriptions = cls(
            max_=max_,
            ci=ci,
            find_info=find_info,
            subs_z=subs_z,
        )

        b_request_ix_service_port_if_find_first_subscriptions.additional_properties = d
        return b_request_ix_service_port_if_find_first_subscriptions

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
