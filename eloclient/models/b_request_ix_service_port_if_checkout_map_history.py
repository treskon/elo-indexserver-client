from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.map_hist_z import MapHistZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutMapHistory")


@_attrs_define
class BRequestIXServicePortIFCheckoutMapHistory:
    """
    Attributes:
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
        domain_name (Union[Unset, str]):
        map_id (Union[Unset, str]):
        members_z (Union[Unset, MapHistZ]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    domain_name: Union[Unset, str] = UNSET
    map_id: Union[Unset, str] = UNSET
    members_z: Union[Unset, "MapHistZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        domain_name = self.domain_name

        map_id = self.map_id

        members_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members_z, Unset):
            members_z = self.members_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if map_id is not UNSET:
            field_dict["mapId"] = map_id
        if members_z is not UNSET:
            field_dict["membersZ"] = members_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.map_hist_z import MapHistZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        domain_name = d.pop("domainName", UNSET)

        map_id = d.pop("mapId", UNSET)

        _members_z = d.pop("membersZ", UNSET)
        members_z: Union[Unset, MapHistZ]
        if isinstance(_members_z, Unset):
            members_z = UNSET
        else:
            members_z = MapHistZ.from_dict(_members_z)

        b_request_ix_service_port_if_checkout_map_history = cls(
            ci=ci,
            domain_name=domain_name,
            map_id=map_id,
            members_z=members_z,
        )

        b_request_ix_service_port_if_checkout_map_history.additional_properties = d
        return b_request_ix_service_port_if_checkout_map_history

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
