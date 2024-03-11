from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.map_to_index_value import MapToIndexValue


T = TypeVar("T", bound="MapToListOfMapToIndexValue")


@_attrs_define
class MapToListOfMapToIndexValue:
    """ """

    additional_properties: Dict[str, List["MapToIndexValue"]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for componentsschemas_list_of_map_to_index_value_item_data in prop:
                componentsschemas_list_of_map_to_index_value_item = (
                    componentsschemas_list_of_map_to_index_value_item_data.to_dict()
                )

                field_dict[prop_name].append(componentsschemas_list_of_map_to_index_value_item)

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_index_value import MapToIndexValue

        d = src_dict.copy()
        map_to_list_of_map_to_index_value = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemas_list_of_map_to_index_value_item_data in _additional_property:
                componentsschemas_list_of_map_to_index_value_item = MapToIndexValue.from_dict(
                    componentsschemas_list_of_map_to_index_value_item_data
                )

                additional_property.append(componentsschemas_list_of_map_to_index_value_item)

            additional_properties[prop_name] = additional_property

        map_to_list_of_map_to_index_value.additional_properties = additional_properties
        return map_to_list_of_map_to_index_value

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List["MapToIndexValue"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List["MapToIndexValue"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
