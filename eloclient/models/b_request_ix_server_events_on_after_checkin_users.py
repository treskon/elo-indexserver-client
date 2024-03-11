from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_users_z import CheckinUsersZ
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.lock_z import LockZ
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="BRequestIXServerEventsOnAfterCheckinUsers")


@_attrs_define
class BRequestIXServerEventsOnAfterCheckinUsers:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        user_infos (Union[Unset, List['UserInfo']]):
        checkin_users_z (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    user_infos: Union[Unset, List["UserInfo"]] = UNSET
    checkin_users_z: Union[Unset, "CheckinUsersZ"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        user_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_infos, Unset):
            user_infos = []
            for user_infos_item_data in self.user_infos:
                user_infos_item = user_infos_item_data.to_dict()

                user_infos.append(user_infos_item)

        checkin_users_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkin_users_z, Unset):
            checkin_users_z = self.checkin_users_z.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if user_infos is not UNSET:
            field_dict["userInfos"] = user_infos
        if checkin_users_z is not UNSET:
            field_dict["checkinUsersZ"] = checkin_users_z
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_users_z import CheckinUsersZ
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.lock_z import LockZ
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        user_infos = []
        _user_infos = d.pop("userInfos", UNSET)
        for user_infos_item_data in _user_infos or []:
            user_infos_item = UserInfo.from_dict(user_infos_item_data)

            user_infos.append(user_infos_item)

        _checkin_users_z = d.pop("checkinUsersZ", UNSET)
        checkin_users_z: Union[Unset, CheckinUsersZ]
        if isinstance(_checkin_users_z, Unset):
            checkin_users_z = UNSET
        else:
            checkin_users_z = CheckinUsersZ.from_dict(_checkin_users_z)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_server_events_on_after_checkin_users = cls(
            ec=ec,
            user_infos=user_infos,
            checkin_users_z=checkin_users_z,
            unlock_z=unlock_z,
        )

        b_request_ix_server_events_on_after_checkin_users.additional_properties = d
        return b_request_ix_server_events_on_after_checkin_users

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
