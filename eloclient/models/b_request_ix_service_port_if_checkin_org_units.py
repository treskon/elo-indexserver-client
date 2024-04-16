from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_org_unit_info import CheckinOrgUnitInfo
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.org_unit_info import OrgUnitInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinOrgUnits")


@_attrs_define
class BRequestIXServicePortIFCheckinOrgUnits:
    """
    Attributes:
        org_unit_infos (Union[Unset, List['OrgUnitInfo']]):
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        reserved (Union[Unset, CheckinOrgUnitInfo]): Objects of this class specify the selection criteria for
            <code>checkinOrgUnits</code>.
            <p>
             Copyright: Copyright (c) 2013
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

    org_unit_infos: Union[Unset, List["OrgUnitInfo"]] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    reserved: Union[Unset, "CheckinOrgUnitInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        org_unit_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.org_unit_infos, Unset):
            org_unit_infos = []
            for org_unit_infos_item_data in self.org_unit_infos:
                org_unit_infos_item = org_unit_infos_item_data.to_dict()
                org_unit_infos.append(org_unit_infos_item)

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        reserved: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reserved, Unset):
            reserved = self.reserved.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_unit_infos is not UNSET:
            field_dict["orgUnitInfos"] = org_unit_infos
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_org_unit_info import CheckinOrgUnitInfo
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.org_unit_info import OrgUnitInfo

        d = src_dict.copy()
        org_unit_infos = []
        _org_unit_infos = d.pop("orgUnitInfos", UNSET)
        for org_unit_infos_item_data in _org_unit_infos or []:
            org_unit_infos_item = OrgUnitInfo.from_dict(org_unit_infos_item_data)

            org_unit_infos.append(org_unit_infos_item)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _reserved = d.pop("reserved", UNSET)
        reserved: Union[Unset, CheckinOrgUnitInfo]
        if isinstance(_reserved, Unset):
            reserved = UNSET
        else:
            reserved = CheckinOrgUnitInfo.from_dict(_reserved)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_checkin_org_units = cls(
            org_unit_infos=org_unit_infos,
            unlock_z=unlock_z,
            reserved=reserved,
            ci=ci,
        )

        b_request_ix_service_port_if_checkin_org_units.additional_properties = d
        return b_request_ix_service_port_if_checkin_org_units

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
