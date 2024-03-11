from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.map_domain import MapDomain


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinMapDomain")


@_attrs_define
class BRequestIXServicePortIFCheckinMapDomain:
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
        map_domain (Union[Unset, MapDomain]): This class contains the information of a map domain.
            A map is a set of key value pairs and can be addressed by a map
             domain name and a map ID. All maps with the same domain name are stored in the same database tables. These maps
            are
             distinguished by their ID, which can be an arbitary string. A map can be attached to a Sord object by setting
            the map
             ID to the Sord ID. Attached maps are deleted, when the Sord object is finally deleted. Furthermore they can be
            copied
             with the Sord object.
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    map_domain: Union[Unset, "MapDomain"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        map_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_domain, Unset):
            map_domain = self.map_domain.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if map_domain is not UNSET:
            field_dict["mapDomain"] = map_domain
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.map_domain import MapDomain

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _map_domain = d.pop("mapDomain", UNSET)
        map_domain: Union[Unset, MapDomain]
        if isinstance(_map_domain, Unset):
            map_domain = UNSET
        else:
            map_domain = MapDomain.from_dict(_map_domain)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_service_port_if_checkin_map_domain = cls(
            ci=ci,
            map_domain=map_domain,
            unlock_z=unlock_z,
        )

        b_request_ix_service_port_if_checkin_map_domain.additional_properties = d
        return b_request_ix_service_port_if_checkin_map_domain

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
