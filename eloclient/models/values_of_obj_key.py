from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValuesOfObjKey")


@_attrs_define
class ValuesOfObjKey:
    """Objects of this class contain the returned data from IXServicePortIF.getDistinctValuesOfObjKey.

    Attributes:
        usage_counts (Union[Unset, List[int]]):
        values (Union[Unset, List[str]]):
        total_count (Union[Unset, int]): The sum of all usageCounts.
    """

    usage_counts: Union[Unset, List[int]] = UNSET
    values: Union[Unset, List[str]] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        usage_counts: Union[Unset, List[int]] = UNSET
        if not isinstance(self.usage_counts, Unset):
            usage_counts = self.usage_counts

        values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usage_counts is not UNSET:
            field_dict["usageCounts"] = usage_counts
        if values is not UNSET:
            field_dict["values"] = values
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        usage_counts = cast(List[int], d.pop("usageCounts", UNSET))

        values = cast(List[str], d.pop("values", UNSET))

        total_count = d.pop("totalCount", UNSET)

        values_of_obj_key = cls(
            usage_counts=usage_counts,
            values=values,
            total_count=total_count,
        )

        values_of_obj_key.additional_properties = d
        return values_of_obj_key

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
