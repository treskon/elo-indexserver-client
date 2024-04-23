from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupStatus")


@_attrs_define
class BackupStatus:
    """This class represents the status of the ELOdm backup task

    Attributes:
        seconds_until_next_check (Union[Unset, int]): waiting time in seconds until the next proccessing (when the
            backup profiles are traversed)
        is_running (Union[Unset, bool]): if the ELOdm backup task is running (the purge task can only run in combination
            with the backup
            task)
        number_of_docs_copied (Union[Unset, int]): number of copied documents since start of the backup task
        error_message (Union[Unset, str]): an error message, if an error occured, else an empty String
    """

    seconds_until_next_check: Union[Unset, int] = UNSET
    is_running: Union[Unset, bool] = UNSET
    number_of_docs_copied: Union[Unset, int] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seconds_until_next_check = self.seconds_until_next_check

        is_running = self.is_running

        number_of_docs_copied = self.number_of_docs_copied

        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seconds_until_next_check is not UNSET:
            field_dict["secondsUntilNextCheck"] = seconds_until_next_check
        if is_running is not UNSET:
            field_dict["isRunning"] = is_running
        if number_of_docs_copied is not UNSET:
            field_dict["numberOfDocsCopied"] = number_of_docs_copied
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seconds_until_next_check = d.pop("secondsUntilNextCheck", UNSET)

        is_running = d.pop("isRunning", UNSET)

        number_of_docs_copied = d.pop("numberOfDocsCopied", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        backup_status = cls(
            seconds_until_next_check=seconds_until_next_check,
            is_running=is_running,
            number_of_docs_copied=number_of_docs_copied,
            error_message=error_message,
        )

        backup_status.additional_properties = d
        return backup_status

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
