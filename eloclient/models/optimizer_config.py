import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_indexer_status import SearchIndexerStatus


T = TypeVar("T", bound="OptimizerConfig")


@_attrs_define
class OptimizerConfig:
    """Configuration and status of optimizer process.

    Attributes:
        last_exception (Union[Unset, str]): Last exception occured during processing.
        ixid (Union[Unset, str]): This Indexserver instance is processing the optimization.
        next_run_at (Union[Unset, datetime.datetime]):
        lock_name (Union[Unset, str]): Process runs under this user account.
        interval_hours (Union[Unset, int]):
        status (Union[Unset, SearchIndexerStatus]):
    """

    last_exception: Union[Unset, str] = UNSET
    ixid: Union[Unset, str] = UNSET
    next_run_at: Union[Unset, datetime.datetime] = UNSET
    lock_name: Union[Unset, str] = UNSET
    interval_hours: Union[Unset, int] = UNSET
    status: Union[Unset, "SearchIndexerStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_exception = self.last_exception

        ixid = self.ixid

        next_run_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_run_at, Unset):
            next_run_at = self.next_run_at.isoformat()

        lock_name = self.lock_name

        interval_hours = self.interval_hours

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_exception is not UNSET:
            field_dict["lastException"] = last_exception
        if ixid is not UNSET:
            field_dict["ixid"] = ixid
        if next_run_at is not UNSET:
            field_dict["nextRunAt"] = next_run_at
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if interval_hours is not UNSET:
            field_dict["intervalHours"] = interval_hours
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_indexer_status import SearchIndexerStatus

        d = src_dict.copy()
        last_exception = d.pop("lastException", UNSET)

        ixid = d.pop("ixid", UNSET)

        _next_run_at = d.pop("nextRunAt", UNSET)
        next_run_at: Union[Unset, datetime.datetime]
        if isinstance(_next_run_at, Unset):
            next_run_at = UNSET
        else:
            next_run_at = isoparse(_next_run_at)

        lock_name = d.pop("lockName", UNSET)

        interval_hours = d.pop("intervalHours", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SearchIndexerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchIndexerStatus.from_dict(_status)

        optimizer_config = cls(
            last_exception=last_exception,
            ixid=ixid,
            next_run_at=next_run_at,
            lock_name=lock_name,
            interval_hours=interval_hours,
            status=status,
        )

        optimizer_config.additional_properties = d
        return optimizer_config

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
