from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.reminder import Reminder


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinReminder")


@_attrs_define
class BRequestIXServicePortIFCheckinReminder:
    """
    Attributes:
        expand_groups (Union[Unset, bool]):
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        receiver_ids (Union[Unset, List[str]]):
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
        remi (Union[Unset, Reminder]):
    """

    expand_groups: Union[Unset, bool] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    receiver_ids: Union[Unset, List[str]] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    remi: Union[Unset, "Reminder"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expand_groups = self.expand_groups

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        receiver_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.receiver_ids, Unset):
            receiver_ids = self.receiver_ids

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        remi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remi, Unset):
            remi = self.remi.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expand_groups is not UNSET:
            field_dict["expandGroups"] = expand_groups
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if receiver_ids is not UNSET:
            field_dict["receiverIds"] = receiver_ids
        if ci is not UNSET:
            field_dict["ci"] = ci
        if remi is not UNSET:
            field_dict["remi"] = remi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.reminder import Reminder

        d = src_dict.copy()
        expand_groups = d.pop("expandGroups", UNSET)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        receiver_ids = cast(List[str], d.pop("receiverIds", UNSET))

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _remi = d.pop("remi", UNSET)
        remi: Union[Unset, Reminder]
        if isinstance(_remi, Unset):
            remi = UNSET
        else:
            remi = Reminder.from_dict(_remi)

        b_request_ix_service_port_if_checkin_reminder = cls(
            expand_groups=expand_groups,
            unlock_z=unlock_z,
            receiver_ids=receiver_ids,
            ci=ci,
            remi=remi,
        )

        b_request_ix_service_port_if_checkin_reminder.additional_properties = d
        return b_request_ix_service_port_if_checkin_reminder

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
