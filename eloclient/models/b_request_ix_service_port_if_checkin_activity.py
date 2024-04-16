from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity import Activity
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinActivity")


@_attrs_define
class BRequestIXServicePortIFCheckinActivity:
    """
    Attributes:
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        act (Union[Unset, Activity]): This class represents an activity.
            <p>
             An activity is a task delegated to an instance outside the ELO system. It is created when the
             task is sent to the instance and deleted, if it is received back. An activity defines a date for
             expecting the response, <code>dueDateIso</code>. At this date, the activity appears in the task
             list of the initiator. If the task is finished, the initiator sets the <code>backAt</code> member
             and the activity is closed.
             </p>
             <p>
             Activities can be used to observe a document or a folder. For each modification, a ELO_NOTIFY
             activity is created and displayed in the task list of the user that wants to observe the object.
             </p>
             <p>
             An activity object is an instance on an activity project. The project defines the properties the
             user can edit or select to provide more information to the task.
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

    unlock_z: Union[Unset, "LockZ"] = UNSET
    act: Union[Unset, "Activity"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        act: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.act, Unset):
            act = self.act.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if act is not UNSET:
            field_dict["act"] = act
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity import Activity
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _act = d.pop("act", UNSET)
        act: Union[Unset, Activity]
        if isinstance(_act, Unset):
            act = UNSET
        else:
            act = Activity.from_dict(_act)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_checkin_activity = cls(
            unlock_z=unlock_z,
            act=act,
            ci=ci,
        )

        b_request_ix_service_port_if_checkin_activity.additional_properties = d
        return b_request_ix_service_port_if_checkin_activity

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
