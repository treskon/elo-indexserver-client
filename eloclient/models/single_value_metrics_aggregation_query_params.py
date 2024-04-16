from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleValueMetricsAggregationQueryParams")


@_attrs_define
class SingleValueMetricsAggregationQueryParams:
    """Defines parameters to run an aggregation of one of the types Min, Max, Sum, Avg
    (single-value-metrics-aggregations).<br>
     This aggregation query doesn't allow sub-aggregations.<br>
     <br>
     Note: The value_count aggregation gets an an own query params class although it is a
     single-value-metrics-aggregation, because it has a different return value type (long).

        Attributes:
            missing_value (Union[Unset, str]): The missing parameter defines how documents that are missing a value should
                be treated.
                By
                 default they will be ignored but it is also possible to treat them as if they had a value.<br>
                 Note: At ELO this is currently only supported for string-based values.<br>
                 Note: This field will be ignored if type is VALUE_COUNT.
    """

    missing_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        missing_value = self.missing_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if missing_value is not UNSET:
            field_dict["missingValue"] = missing_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        missing_value = d.pop("missingValue", UNSET)

        single_value_metrics_aggregation_query_params = cls(
            missing_value=missing_value,
        )

        single_value_metrics_aggregation_query_params.additional_properties = d
        return single_value_metrics_aggregation_query_params

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
