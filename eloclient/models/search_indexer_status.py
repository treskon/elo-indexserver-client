from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchIndexerStatus")


@_attrs_define
class SearchIndexerStatus:
    """
    Attributes:
        sleeping (Union[Unset, SearchIndexerStatus]):
        running (Union[Unset, SearchIndexerStatus]):
        inactive (Union[Unset, SearchIndexerStatus]):
    """

    sleeping: Union[Unset, "SearchIndexerStatus"] = UNSET
    running: Union[Unset, "SearchIndexerStatus"] = UNSET
    inactive: Union[Unset, "SearchIndexerStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sleeping: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sleeping, Unset):
            sleeping = self.sleeping.to_dict()

        running: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.running, Unset):
            running = self.running.to_dict()

        inactive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inactive, Unset):
            inactive = self.inactive.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sleeping is not UNSET:
            field_dict["Sleeping"] = sleeping
        if running is not UNSET:
            field_dict["Running"] = running
        if inactive is not UNSET:
            field_dict["Inactive"] = inactive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sleeping = d.pop("Sleeping", UNSET)
        sleeping: Union[Unset, SearchIndexerStatus]
        if isinstance(_sleeping, Unset):
            sleeping = UNSET
        else:
            sleeping = SearchIndexerStatus.from_dict(_sleeping)

        _running = d.pop("Running", UNSET)
        running: Union[Unset, SearchIndexerStatus]
        if isinstance(_running, Unset):
            running = UNSET
        else:
            running = SearchIndexerStatus.from_dict(_running)

        _inactive = d.pop("Inactive", UNSET)
        inactive: Union[Unset, SearchIndexerStatus]
        if isinstance(_inactive, Unset):
            inactive = UNSET
        else:
            inactive = SearchIndexerStatus.from_dict(_inactive)

        search_indexer_status = cls(
            sleeping=sleeping,
            running=running,
            inactive=inactive,
        )

        search_indexer_status.additional_properties = d
        return search_indexer_status

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
