from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_status import BackupStatus
    from ..models.purge_status import PurgeStatus


T = TypeVar("T", bound="BackupPurgeStatus")


@_attrs_define
class BackupPurgeStatus:
    """This class represents the status of the ELOdm backup and purge tasks

    Attributes:
        backup_status (Union[Unset, BackupStatus]): This class represents the status of the ELOdm backup task
        purge_status (Union[Unset, PurgeStatus]): This class represents the status of the ELOdm purge task
    """

    backup_status: Union[Unset, "BackupStatus"] = UNSET
    purge_status: Union[Unset, "PurgeStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.to_dict()

        purge_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.purge_status, Unset):
            purge_status = self.purge_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if purge_status is not UNSET:
            field_dict["purgeStatus"] = purge_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.backup_status import BackupStatus
        from ..models.purge_status import PurgeStatus

        d = src_dict.copy()
        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: Union[Unset, BackupStatus]
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupStatus.from_dict(_backup_status)

        _purge_status = d.pop("purgeStatus", UNSET)
        purge_status: Union[Unset, PurgeStatus]
        if isinstance(_purge_status, Unset):
            purge_status = UNSET
        else:
            purge_status = PurgeStatus.from_dict(_purge_status)

        backup_purge_status = cls(
            backup_status=backup_status,
            purge_status=purge_status,
        )

        backup_purge_status.additional_properties = d
        return backup_purge_status

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
