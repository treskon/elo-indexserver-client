from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_users_z import CheckinUsersZ
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinUser")


@_attrs_define
class BRequestIXServicePortIFCheckinUser:
    """
    Attributes:
        user_info (Union[Unset, UserInfo]): <p>
            Data class containing the user information data for the user logged in to the Index server. User
             information includes ID, name, rights, parent, etc.
             </p>
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
        checkin_users_z (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
    """

    user_info: Union[Unset, "UserInfo"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    checkin_users_z: Union[Unset, "CheckinUsersZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        checkin_users_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkin_users_z, Unset):
            checkin_users_z = self.checkin_users_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if checkin_users_z is not UNSET:
            field_dict["checkinUsersZ"] = checkin_users_z
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_users_z import CheckinUsersZ
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _user_info = d.pop("userInfo", UNSET)
        user_info: Union[Unset, UserInfo]
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = UserInfo.from_dict(_user_info)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _checkin_users_z = d.pop("checkinUsersZ", UNSET)
        checkin_users_z: Union[Unset, CheckinUsersZ]
        if isinstance(_checkin_users_z, Unset):
            checkin_users_z = UNSET
        else:
            checkin_users_z = CheckinUsersZ.from_dict(_checkin_users_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_checkin_user = cls(
            user_info=user_info,
            unlock_z=unlock_z,
            checkin_users_z=checkin_users_z,
            ci=ci,
        )

        b_request_ix_service_port_if_checkin_user.additional_properties = d
        return b_request_ix_service_port_if_checkin_user

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
