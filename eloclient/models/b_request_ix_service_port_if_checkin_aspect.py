from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect import Aspect
    from ..models.aspect_z import AspectZ
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinAspect")


@_attrs_define
class BRequestIXServicePortIFCheckinAspect:
    """
    Attributes:
        aspect_z (Union[Unset, AspectZ]): This class encapsulates the constants of the AspectC class.
            <p>
             Copyright: Copyright (c) 2019
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
        aspect (Union[Unset, Aspect]): This class defines a keywording aspect.
    """

    aspect_z: Union[Unset, "AspectZ"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    aspect: Union[Unset, "Aspect"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aspect_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_z, Unset):
            aspect_z = self.aspect_z.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        aspect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect, Unset):
            aspect = self.aspect.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_z is not UNSET:
            field_dict["aspectZ"] = aspect_z
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if aspect is not UNSET:
            field_dict["aspect"] = aspect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect import Aspect
        from ..models.aspect_z import AspectZ
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _aspect_z = d.pop("aspectZ", UNSET)
        aspect_z: Union[Unset, AspectZ]
        if isinstance(_aspect_z, Unset):
            aspect_z = UNSET
        else:
            aspect_z = AspectZ.from_dict(_aspect_z)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _aspect = d.pop("aspect", UNSET)
        aspect: Union[Unset, Aspect]
        if isinstance(_aspect, Unset):
            aspect = UNSET
        else:
            aspect = Aspect.from_dict(_aspect)

        b_request_ix_service_port_if_checkin_aspect = cls(
            aspect_z=aspect_z,
            unlock_z=unlock_z,
            ci=ci,
            aspect=aspect,
        )

        b_request_ix_service_port_if_checkin_aspect.additional_properties = d
        return b_request_ix_service_port_if_checkin_aspect

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
