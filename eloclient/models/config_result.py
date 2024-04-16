from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_record import ConfigRecord
    from ..models.map_to_list_of_config_record import MapToListOfConfigRecord


T = TypeVar("T", bound="ConfigResult")


@_attrs_define
class ConfigResult:
    """Return value for {@link ConfigService} functions.

    Attributes:
        config_records (Union[Unset, MapToListOfConfigRecord]):
        written_records (Union[Unset, List['ConfigRecord']]):
    """

    config_records: Union[Unset, "MapToListOfConfigRecord"] = UNSET
    written_records: Union[Unset, List["ConfigRecord"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_records: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_records, Unset):
            config_records = self.config_records.to_dict()

        written_records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.written_records, Unset):
            written_records = []
            for componentsschemas_list_of_config_record_item_data in self.written_records:
                componentsschemas_list_of_config_record_item = (
                    componentsschemas_list_of_config_record_item_data.to_dict()
                )
                written_records.append(componentsschemas_list_of_config_record_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_records is not UNSET:
            field_dict["configRecords"] = config_records
        if written_records is not UNSET:
            field_dict["writtenRecords"] = written_records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_record import ConfigRecord
        from ..models.map_to_list_of_config_record import MapToListOfConfigRecord

        d = src_dict.copy()
        _config_records = d.pop("configRecords", UNSET)
        config_records: Union[Unset, MapToListOfConfigRecord]
        if isinstance(_config_records, Unset):
            config_records = UNSET
        else:
            config_records = MapToListOfConfigRecord.from_dict(_config_records)

        written_records = []
        _written_records = d.pop("writtenRecords", UNSET)
        for componentsschemas_list_of_config_record_item_data in _written_records or []:
            componentsschemas_list_of_config_record_item = ConfigRecord.from_dict(
                componentsschemas_list_of_config_record_item_data
            )

            written_records.append(componentsschemas_list_of_config_record_item)

        config_result = cls(
            config_records=config_records,
            written_records=written_records,
        )

        config_result.additional_properties = d
        return config_result

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
