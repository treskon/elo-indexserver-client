import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_indexer_status import SearchIndexerStatus


T = TypeVar("T", bound="ReindexerConfig")


@_attrs_define
class ReindexerConfig:
    """Configuration and status of Re-indexer process.

    Attributes:
        status (Union[Unset, SearchIndexerStatus]):
        started_at (Union[Unset, datetime.datetime]):
        progress_in_percent (Union[Unset, int]):
        ixid (Union[Unset, str]): This Indexserver instance is processing the update.
        last_exception (Union[Unset, str]): Last exception occured during processing.
        obj_id_range (Union[Unset, str]): Lower and upper limit of object IDs processed by re-indexing process.
        lock_name (Union[Unset, str]): Process runs under this user account.
    """

    status: Union[Unset, "SearchIndexerStatus"] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    progress_in_percent: Union[Unset, int] = UNSET
    ixid: Union[Unset, str] = UNSET
    last_exception: Union[Unset, str] = UNSET
    obj_id_range: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        progress_in_percent = self.progress_in_percent
        ixid = self.ixid
        last_exception = self.last_exception
        obj_id_range = self.obj_id_range
        lock_name = self.lock_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if progress_in_percent is not UNSET:
            field_dict["progressInPercent"] = progress_in_percent
        if ixid is not UNSET:
            field_dict["ixid"] = ixid
        if last_exception is not UNSET:
            field_dict["lastException"] = last_exception
        if obj_id_range is not UNSET:
            field_dict["objIdRange"] = obj_id_range
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

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        progress_in_percent = d.pop("progressInPercent", UNSET)

        ixid = d.pop("ixid", UNSET)

        last_exception = d.pop("lastException", UNSET)

        obj_id_range = d.pop("objIdRange", UNSET)

        lock_name = d.pop("lockName", UNSET)

        reindexer_config = cls(
            status=status,
            started_at=started_at,
            progress_in_percent=progress_in_percent,
            ixid=ixid,
            last_exception=last_exception,
            obj_id_range=obj_id_range,
            lock_name=lock_name,
        )

        reindexer_config.additional_properties = d
        return reindexer_config

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
