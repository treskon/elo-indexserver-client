from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.aggregation_result import AggregationResult


T = TypeVar("T", bound="MapToAggregationResult")


@_attrs_define
class MapToAggregationResult:
    """ """

    additional_properties: Dict[str, "AggregationResult"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_result import AggregationResult

        d = src_dict.copy()
        map_to_aggregation_result = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AggregationResult.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        map_to_aggregation_result.additional_properties = additional_properties
        return map_to_aggregation_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AggregationResult":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AggregationResult") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties