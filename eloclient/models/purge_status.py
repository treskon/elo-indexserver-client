from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurgeStatus")


@_attrs_define
class PurgeStatus:
    """This class represents the status of the ELOdm purge task

    Attributes:
        last_purge_time (Union[Unset, str]): last purge work time (ISO UTC date and time without dots) If no purge has
            been done yet, the
            variable is empty.
        is_running (Union[Unset, bool]): if the ELOdm purge task is running (it can only run in combination with the
            backup task)
        error_message (Union[Unset, str]): an error message, if an error occured, else an empty String
        number_of_docs_purged (Union[Unset, int]): number of purged documents
    """

    last_purge_time: Union[Unset, str] = UNSET
    is_running: Union[Unset, bool] = UNSET
    error_message: Union[Unset, str] = UNSET
    number_of_docs_purged: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_purge_time = self.last_purge_time

        is_running = self.is_running

        error_message = self.error_message

        number_of_docs_purged = self.number_of_docs_purged

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_purge_time is not UNSET:
            field_dict["lastPurgeTime"] = last_purge_time
        if is_running is not UNSET:
            field_dict["isRunning"] = is_running
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if number_of_docs_purged is not UNSET:
            field_dict["numberOfDocsPurged"] = number_of_docs_purged

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_purge_time = d.pop("lastPurgeTime", UNSET)

        is_running = d.pop("isRunning", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        number_of_docs_purged = d.pop("numberOfDocsPurged", UNSET)

        purge_status = cls(
            last_purge_time=last_purge_time,
            is_running=is_running,
            error_message=error_message,
            number_of_docs_purged=number_of_docs_purged,
        )

        purge_status.additional_properties = d
        return purge_status

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
