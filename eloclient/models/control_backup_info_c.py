from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlBackupInfoC")


@_attrs_define
class ControlBackupInfoC:
    """Constants for class ControlBackupInfo (mode for the ELOdm backup and purge tasks)

    Attributes:
        mode_stop (Union[Unset, int]): Stop the backup and purge tasks
        mode_start_backup_purge (Union[Unset, int]): Start the backup and the purge task.
            If the backup task is already running, only the purge task
             is started.
        mode_status (Union[Unset, int]): Query the status of the backup and purge tasks
        mode_start_backup (Union[Unset, int]): Start the backup task (if it is already running, nothing happens).
            If the purge task is already
             running, it is stopped.
    """

    mode_stop: Union[Unset, int] = UNSET
    mode_start_backup_purge: Union[Unset, int] = UNSET
    mode_status: Union[Unset, int] = UNSET
    mode_start_backup: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode_stop = self.mode_stop

        mode_start_backup_purge = self.mode_start_backup_purge

        mode_status = self.mode_status

        mode_start_backup = self.mode_start_backup

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode_stop is not UNSET:
            field_dict["MODE_STOP"] = mode_stop
        if mode_start_backup_purge is not UNSET:
            field_dict["MODE_START_BACKUP_PURGE"] = mode_start_backup_purge
        if mode_status is not UNSET:
            field_dict["MODE_STATUS"] = mode_status
        if mode_start_backup is not UNSET:
            field_dict["MODE_START_BACKUP"] = mode_start_backup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode_stop = d.pop("MODE_STOP", UNSET)

        mode_start_backup_purge = d.pop("MODE_START_BACKUP_PURGE", UNSET)

        mode_status = d.pop("MODE_STATUS", UNSET)

        mode_start_backup = d.pop("MODE_START_BACKUP", UNSET)

        control_backup_info_c = cls(
            mode_stop=mode_stop,
            mode_start_backup_purge=mode_start_backup_purge,
            mode_status=mode_status,
            mode_start_backup=mode_start_backup,
        )

        control_backup_info_c.additional_properties = d
        return control_backup_info_c

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
