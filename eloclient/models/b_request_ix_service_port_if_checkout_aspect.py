from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect_z import AspectZ
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutAspect")


@_attrs_define
class BRequestIXServicePortIFCheckoutAspect:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        aspect_id (Union[Unset, str]):
        aspect_z (Union[Unset, AspectZ]): This class encapsulates the constants of the AspectC class.
            <p>
             Copyright: Copyright (c) 2019
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    aspect_id: Union[Unset, str] = UNSET
    aspect_z: Union[Unset, "AspectZ"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        aspect_id = self.aspect_id
        aspect_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_z, Unset):
            aspect_z = self.aspect_z.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if aspect_id is not UNSET:
            field_dict["aspectId"] = aspect_id
        if aspect_z is not UNSET:
            field_dict["aspectZ"] = aspect_z
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect_z import AspectZ
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        aspect_id = d.pop("aspectId", UNSET)

        _aspect_z = d.pop("aspectZ", UNSET)
        aspect_z: Union[Unset, AspectZ]
        if isinstance(_aspect_z, Unset):
            aspect_z = UNSET
        else:
            aspect_z = AspectZ.from_dict(_aspect_z)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        b_request_ix_service_port_if_checkout_aspect = cls(
            ci=ci,
            aspect_id=aspect_id,
            aspect_z=aspect_z,
            lock_z=lock_z,
        )

        b_request_ix_service_port_if_checkout_aspect.additional_properties = d
        return b_request_ix_service_port_if_checkout_aspect

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
