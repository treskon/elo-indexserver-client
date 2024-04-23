from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_profile import BackupProfile
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFConfigureBackup")


@_attrs_define
class BRequestIXServicePortIFConfigureBackup:
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
        backup_profiles (Union[Unset, List['BackupProfile']]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    backup_profiles: Union[Unset, List["BackupProfile"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        backup_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.backup_profiles, Unset):
            backup_profiles = []
            for backup_profiles_item_data in self.backup_profiles:
                backup_profiles_item = backup_profiles_item_data.to_dict()
                backup_profiles.append(backup_profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if backup_profiles is not UNSET:
            field_dict["backupProfiles"] = backup_profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.backup_profile import BackupProfile
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        backup_profiles = []
        _backup_profiles = d.pop("backupProfiles", UNSET)
        for backup_profiles_item_data in _backup_profiles or []:
            backup_profiles_item = BackupProfile.from_dict(backup_profiles_item_data)

            backup_profiles.append(backup_profiles_item)

        b_request_ix_service_port_if_configure_backup = cls(
            ci=ci,
            backup_profiles=backup_profiles,
        )

        b_request_ix_service_port_if_configure_backup.additional_properties = d
        return b_request_ix_service_port_if_configure_backup

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
