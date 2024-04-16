from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_record import ConfigRecord


T = TypeVar("T", bound="ConfigBatchData")


@_attrs_define
class ConfigBatchData:
    """Collects configuration data to be inserted, updated, or deleted.

    Attributes:
        deletes (Union[Unset, List[str]]):
        updates (Union[Unset, List['ConfigRecord']]):
        inserts (Union[Unset, List['ConfigRecord']]):
    """

    deletes: Union[Unset, List[str]] = UNSET
    updates: Union[Unset, List["ConfigRecord"]] = UNSET
    inserts: Union[Unset, List["ConfigRecord"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deletes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        updates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for componentsschemas_list_of_config_record_item_data in self.updates:
                componentsschemas_list_of_config_record_item = (
                    componentsschemas_list_of_config_record_item_data.to_dict()
                )
                updates.append(componentsschemas_list_of_config_record_item)

        inserts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inserts, Unset):
            inserts = []
            for componentsschemas_list_of_config_record_item_data in self.inserts:
                componentsschemas_list_of_config_record_item = (
                    componentsschemas_list_of_config_record_item_data.to_dict()
                )
                inserts.append(componentsschemas_list_of_config_record_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deletes is not UNSET:
            field_dict["deletes"] = deletes
        if updates is not UNSET:
            field_dict["updates"] = updates
        if inserts is not UNSET:
            field_dict["inserts"] = inserts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_record import ConfigRecord

        d = src_dict.copy()
        deletes = cast(List[str], d.pop("deletes", UNSET))

        updates = []
        _updates = d.pop("updates", UNSET)
        for componentsschemas_list_of_config_record_item_data in _updates or []:
            componentsschemas_list_of_config_record_item = ConfigRecord.from_dict(
                componentsschemas_list_of_config_record_item_data
            )

            updates.append(componentsschemas_list_of_config_record_item)

        inserts = []
        _inserts = d.pop("inserts", UNSET)
        for componentsschemas_list_of_config_record_item_data in _inserts or []:
            componentsschemas_list_of_config_record_item = ConfigRecord.from_dict(
                componentsschemas_list_of_config_record_item_data
            )

            inserts.append(componentsschemas_list_of_config_record_item)

        config_batch_data = cls(
            deletes=deletes,
            updates=updates,
            inserts=inserts,
        )

        config_batch_data.additional_properties = d
        return config_batch_data

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
