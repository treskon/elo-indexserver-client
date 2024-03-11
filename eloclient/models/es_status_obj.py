from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString


T = TypeVar("T", bound="ESStatusObj")


@_attrs_define
class ESStatusObj:
    """Calling checkoutEsStatus returns this object to inform about the current status of connection to Elasticsearch and
    running processes.

        Attributes:
            es_connection (Union[Unset, bool]): Is this IX connected to the Elasticsearch server.
            running_updaters (Union[Unset, MapToString]):
            running_reindexers (Union[Unset, MapToString]):
            last_exception_updater (Union[Unset, str]): Last exception of updater of this IX
            last_exception_reindexer (Union[Unset, str]): Last exception of reindexer of this IX
    """

    es_connection: Union[Unset, bool] = UNSET
    running_updaters: Union[Unset, "MapToString"] = UNSET
    running_reindexers: Union[Unset, "MapToString"] = UNSET
    last_exception_updater: Union[Unset, str] = UNSET
    last_exception_reindexer: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        es_connection = self.es_connection
        running_updaters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.running_updaters, Unset):
            running_updaters = self.running_updaters.to_dict()

        running_reindexers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.running_reindexers, Unset):
            running_reindexers = self.running_reindexers.to_dict()

        last_exception_updater = self.last_exception_updater
        last_exception_reindexer = self.last_exception_reindexer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if es_connection is not UNSET:
            field_dict["esConnection"] = es_connection
        if running_updaters is not UNSET:
            field_dict["runningUpdaters"] = running_updaters
        if running_reindexers is not UNSET:
            field_dict["runningReindexers"] = running_reindexers
        if last_exception_updater is not UNSET:
            field_dict["lastExceptionUpdater"] = last_exception_updater
        if last_exception_reindexer is not UNSET:
            field_dict["lastExceptionReindexer"] = last_exception_reindexer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        es_connection = d.pop("esConnection", UNSET)

        _running_updaters = d.pop("runningUpdaters", UNSET)
        running_updaters: Union[Unset, MapToString]
        if isinstance(_running_updaters, Unset):
            running_updaters = UNSET
        else:
            running_updaters = MapToString.from_dict(_running_updaters)

        _running_reindexers = d.pop("runningReindexers", UNSET)
        running_reindexers: Union[Unset, MapToString]
        if isinstance(_running_reindexers, Unset):
            running_reindexers = UNSET
        else:
            running_reindexers = MapToString.from_dict(_running_reindexers)

        last_exception_updater = d.pop("lastExceptionUpdater", UNSET)

        last_exception_reindexer = d.pop("lastExceptionReindexer", UNSET)

        es_status_obj = cls(
            es_connection=es_connection,
            running_updaters=running_updaters,
            running_reindexers=running_reindexers,
            last_exception_updater=last_exception_updater,
            last_exception_reindexer=last_exception_reindexer,
        )

        es_status_obj.additional_properties = d
        return es_status_obj

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
