from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_users_z import CheckinUsersZ


T = TypeVar("T", bound="CheckinUsersC")


@_attrs_define
class CheckinUsersC:
    """<p>
    Constants for the function <code>checkinUsers</code>.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation:
     </p>

        Attributes:
            bset_nothing (Union[Unset, str]): Checkin no user. Makes sense if you only want to unlock user data.
            bset_write (Union[Unset, str]): Write without password. Create new user if user ID &lt; 0.
            bset_password (Union[Unset, str]): Updates a users password.
            bset_new_user (Union[Unset, str]): Insert a new user with the supplied user ID.
            nothing (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            password (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            new_user (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            write (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            write_password (Union[Unset, CheckinUsersZ]): This class encapsulates the constants of CheckinUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    bset_nothing: Union[Unset, str] = UNSET
    bset_write: Union[Unset, str] = UNSET
    bset_password: Union[Unset, str] = UNSET
    bset_new_user: Union[Unset, str] = UNSET
    nothing: Union[Unset, "CheckinUsersZ"] = UNSET
    password: Union[Unset, "CheckinUsersZ"] = UNSET
    new_user: Union[Unset, "CheckinUsersZ"] = UNSET
    write: Union[Unset, "CheckinUsersZ"] = UNSET
    write_password: Union[Unset, "CheckinUsersZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_nothing = self.bset_nothing
        bset_write = self.bset_write
        bset_password = self.bset_password
        bset_new_user = self.bset_new_user
        nothing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nothing, Unset):
            nothing = self.nothing.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        new_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_user, Unset):
            new_user = self.new_user.to_dict()

        write: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.write, Unset):
            write = self.write.to_dict()

        write_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.write_password, Unset):
            write_password = self.write_password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_nothing is not UNSET:
            field_dict["bsetNOTHING"] = bset_nothing
        if bset_write is not UNSET:
            field_dict["bsetWRITE"] = bset_write
        if bset_password is not UNSET:
            field_dict["bsetPASSWORD"] = bset_password
        if bset_new_user is not UNSET:
            field_dict["bsetNEW_USER"] = bset_new_user
        if nothing is not UNSET:
            field_dict["NOTHING"] = nothing
        if password is not UNSET:
            field_dict["PASSWORD"] = password
        if new_user is not UNSET:
            field_dict["NEW_USER"] = new_user
        if write is not UNSET:
            field_dict["WRITE"] = write
        if write_password is not UNSET:
            field_dict["WRITE_PASSWORD"] = write_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_users_z import CheckinUsersZ

        d = src_dict.copy()
        bset_nothing = d.pop("bsetNOTHING", UNSET)

        bset_write = d.pop("bsetWRITE", UNSET)

        bset_password = d.pop("bsetPASSWORD", UNSET)

        bset_new_user = d.pop("bsetNEW_USER", UNSET)

        _nothing = d.pop("NOTHING", UNSET)
        nothing: Union[Unset, CheckinUsersZ]
        if isinstance(_nothing, Unset):
            nothing = UNSET
        else:
            nothing = CheckinUsersZ.from_dict(_nothing)

        _password = d.pop("PASSWORD", UNSET)
        password: Union[Unset, CheckinUsersZ]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = CheckinUsersZ.from_dict(_password)

        _new_user = d.pop("NEW_USER", UNSET)
        new_user: Union[Unset, CheckinUsersZ]
        if isinstance(_new_user, Unset):
            new_user = UNSET
        else:
            new_user = CheckinUsersZ.from_dict(_new_user)

        _write = d.pop("WRITE", UNSET)
        write: Union[Unset, CheckinUsersZ]
        if isinstance(_write, Unset):
            write = UNSET
        else:
            write = CheckinUsersZ.from_dict(_write)

        _write_password = d.pop("WRITE_PASSWORD", UNSET)
        write_password: Union[Unset, CheckinUsersZ]
        if isinstance(_write_password, Unset):
            write_password = UNSET
        else:
            write_password = CheckinUsersZ.from_dict(_write_password)

        checkin_users_c = cls(
            bset_nothing=bset_nothing,
            bset_write=bset_write,
            bset_password=bset_password,
            bset_new_user=bset_new_user,
            nothing=nothing,
            password=password,
            new_user=new_user,
            write=write,
            write_password=write_password,
        )

        checkin_users_c.additional_properties = d
        return checkin_users_c

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
