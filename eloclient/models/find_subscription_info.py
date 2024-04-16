from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_z import FeedZ
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="FindSubscriptionInfo")


@_attrs_define
class FindSubscriptionInfo:
    """Find criteria for function findFirstSubscriptions.

    Attributes:
        feed_z (Union[Unset, FeedZ]): Type safe element selector for class Feed.
        sord_z (Union[Unset, SordZ]): <p>
            This class encapsulates the constants of <code>SordC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        user_id (Union[Unset, str]): Find subscriptions of this user.
            If this member is empty, the current users subscriptions are
             returned. This member is ignored for non-administrators. User ID, GUID or Name is accepted.
    """

    feed_z: Union[Unset, "FeedZ"] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_z, Unset):
            feed_z = self.feed_z.to_dict()

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feed_z is not UNSET:
            field_dict["feedZ"] = feed_z
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_z import FeedZ
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        _feed_z = d.pop("feedZ", UNSET)
        feed_z: Union[Unset, FeedZ]
        if isinstance(_feed_z, Unset):
            feed_z = UNSET
        else:
            feed_z = FeedZ.from_dict(_feed_z)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        user_id = d.pop("userId", UNSET)

        find_subscription_info = cls(
            feed_z=feed_z,
            sord_z=sord_z,
            user_id=user_id,
        )

        find_subscription_info.additional_properties = d
        return find_subscription_info

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
