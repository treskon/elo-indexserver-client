from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.notification import Notification
    from ..models.notification_z import NotificationZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinNotification")


@_attrs_define
class BRequestIXServicePortIFCheckinNotification:
    """
    Attributes:
        notif (Union[Unset, Notification]): Objects of this class represent a change notification. This class is used
            internally.
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
        noti_z (Union[Unset, NotificationZ]): <p>
            This class encapsulates the constants of <code>NotificationC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2015
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    notif: Union[Unset, "Notification"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    noti_z: Union[Unset, "NotificationZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notif: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notif, Unset):
            notif = self.notif.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        noti_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.noti_z, Unset):
            noti_z = self.noti_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notif is not UNSET:
            field_dict["notif"] = notif
        if ci is not UNSET:
            field_dict["ci"] = ci
        if noti_z is not UNSET:
            field_dict["notiZ"] = noti_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.notification import Notification
        from ..models.notification_z import NotificationZ

        d = src_dict.copy()
        _notif = d.pop("notif", UNSET)
        notif: Union[Unset, Notification]
        if isinstance(_notif, Unset):
            notif = UNSET
        else:
            notif = Notification.from_dict(_notif)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _noti_z = d.pop("notiZ", UNSET)
        noti_z: Union[Unset, NotificationZ]
        if isinstance(_noti_z, Unset):
            noti_z = UNSET
        else:
            noti_z = NotificationZ.from_dict(_noti_z)

        b_request_ix_service_port_if_checkin_notification = cls(
            notif=notif,
            ci=ci,
            noti_z=noti_z,
        )

        b_request_ix_service_port_if_checkin_notification.additional_properties = d
        return b_request_ix_service_port_if_checkin_notification

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
