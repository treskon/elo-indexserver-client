import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_indexer_status import SearchIndexerStatus


T = TypeVar("T", bound="UpdaterConfig")


@_attrs_define
class UpdaterConfig:
    """Configuration and status of updater process.

    Attributes:
        status (Union[Unset, SearchIndexerStatus]):
        next_run_at (Union[Unset, datetime.datetime]):
        interval_minutes (Union[Unset, int]):
        update_newer_than (Union[Unset, datetime.datetime]):
        progress_in_percent (Union[Unset, int]):
        ixid (Union[Unset, str]): This Indexserver instance is processing the update.
        last_exception (Union[Unset, str]): Last exception occured during processing.
        lock_name (Union[Unset, str]): Process runs under this user account.
    """

    status: Union[Unset, "SearchIndexerStatus"] = UNSET
    next_run_at: Union[Unset, datetime.datetime] = UNSET
    interval_minutes: Union[Unset, int] = UNSET
    update_newer_than: Union[Unset, datetime.datetime] = UNSET
    progress_in_percent: Union[Unset, int] = UNSET
    ixid: Union[Unset, str] = UNSET
    last_exception: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        next_run_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_run_at, Unset):
            next_run_at = self.next_run_at.isoformat()

        interval_minutes = self.interval_minutes
        update_newer_than: Union[Unset, str] = UNSET
        if not isinstance(self.update_newer_than, Unset):
            update_newer_than = self.update_newer_than.isoformat()

        progress_in_percent = self.progress_in_percent
        ixid = self.ixid
        last_exception = self.last_exception
        lock_name = self.lock_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if next_run_at is not UNSET:
            field_dict["nextRunAt"] = next_run_at
        if interval_minutes is not UNSET:
            field_dict["intervalMinutes"] = interval_minutes
        if update_newer_than is not UNSET:
            field_dict["updateNewerThan"] = update_newer_than
        if progress_in_percent is not UNSET:
            field_dict["progressInPercent"] = progress_in_percent
        if ixid is not UNSET:
            field_dict["ixid"] = ixid
        if last_exception is not UNSET:
            field_dict["lastException"] = last_exception
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_indexer_status import SearchIndexerStatus

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SearchIndexerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchIndexerStatus.from_dict(_status)

        _next_run_at = d.pop("nextRunAt", UNSET)
        next_run_at: Union[Unset, datetime.datetime]
        if isinstance(_next_run_at, Unset):
            next_run_at = UNSET
        else:
            next_run_at = isoparse(_next_run_at)

        interval_minutes = d.pop("intervalMinutes", UNSET)

        _update_newer_than = d.pop("updateNewerThan", UNSET)
        update_newer_than: Union[Unset, datetime.datetime]
        if isinstance(_update_newer_than, Unset):
            update_newer_than = UNSET
        else:
            update_newer_than = isoparse(_update_newer_than)

        progress_in_percent = d.pop("progressInPercent", UNSET)

        ixid = d.pop("ixid", UNSET)

        last_exception = d.pop("lastException", UNSET)

        lock_name = d.pop("lockName", UNSET)

        updater_config = cls(
            status=status,
            next_run_at=next_run_at,
            interval_minutes=interval_minutes,
            update_newer_than=update_newer_than,
            progress_in_percent=progress_in_percent,
            ixid=ixid,
            last_exception=last_exception,
            lock_name=lock_name,
        )

        updater_config.additional_properties = d
        return updater_config

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
