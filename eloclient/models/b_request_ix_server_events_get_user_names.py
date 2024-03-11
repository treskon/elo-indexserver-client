from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_users_z import CheckoutUsersZ
    from ..models.ix_server_events_context import IXServerEventsContext


T = TypeVar("T", bound="BRequestIXServerEventsGetUserNames")


@_attrs_define
class BRequestIXServerEventsGetUserNames:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        ids (Union[Unset, List[str]]):
        checkout_users_z (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    checkout_users_z: Union[Unset, "CheckoutUsersZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        checkout_users_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_users_z, Unset):
            checkout_users_z = self.checkout_users_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if ids is not UNSET:
            field_dict["ids"] = ids
        if checkout_users_z is not UNSET:
            field_dict["checkoutUsersZ"] = checkout_users_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_users_z import CheckoutUsersZ
        from ..models.ix_server_events_context import IXServerEventsContext

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        ids = cast(List[str], d.pop("ids", UNSET))

        _checkout_users_z = d.pop("checkoutUsersZ", UNSET)
        checkout_users_z: Union[Unset, CheckoutUsersZ]
        if isinstance(_checkout_users_z, Unset):
            checkout_users_z = UNSET
        else:
            checkout_users_z = CheckoutUsersZ.from_dict(_checkout_users_z)

        b_request_ix_server_events_get_user_names = cls(
            ec=ec,
            ids=ids,
            checkout_users_z=checkout_users_z,
        )

        b_request_ix_server_events_get_user_names.additional_properties = d
        return b_request_ix_server_events_get_user_names

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
