from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_integer import MapToInteger
    from ..models.map_to_string import MapToString


T = TypeVar("T", bound="CopyResult")


@_attrs_define
class CopyResult:
    """Results of a {@link ProcessCopyElements}-Operation.

    Attributes:
        map_guids_source_2_copy (Union[Unset, MapToString]):
        map_ids_source_2_copy (Union[Unset, MapToInteger]):
    """

    map_guids_source_2_copy: Union[Unset, "MapToString"] = UNSET
    map_ids_source_2_copy: Union[Unset, "MapToInteger"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        map_guids_source_2_copy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_guids_source_2_copy, Unset):
            map_guids_source_2_copy = self.map_guids_source_2_copy.to_dict()

        map_ids_source_2_copy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_ids_source_2_copy, Unset):
            map_ids_source_2_copy = self.map_ids_source_2_copy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_guids_source_2_copy is not UNSET:
            field_dict["mapGuidsSource2Copy"] = map_guids_source_2_copy
        if map_ids_source_2_copy is not UNSET:
            field_dict["mapIdsSource2Copy"] = map_ids_source_2_copy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_integer import MapToInteger
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        _map_guids_source_2_copy = d.pop("mapGuidsSource2Copy", UNSET)
        map_guids_source_2_copy: Union[Unset, MapToString]
        if isinstance(_map_guids_source_2_copy, Unset):
            map_guids_source_2_copy = UNSET
        else:
            map_guids_source_2_copy = MapToString.from_dict(_map_guids_source_2_copy)

        _map_ids_source_2_copy = d.pop("mapIdsSource2Copy", UNSET)
        map_ids_source_2_copy: Union[Unset, MapToInteger]
        if isinstance(_map_ids_source_2_copy, Unset):
            map_ids_source_2_copy = UNSET
        else:
            map_ids_source_2_copy = MapToInteger.from_dict(_map_ids_source_2_copy)

        copy_result = cls(
            map_guids_source_2_copy=map_guids_source_2_copy,
            map_ids_source_2_copy=map_ids_source_2_copy,
        )

        copy_result.additional_properties = d
        return copy_result

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
