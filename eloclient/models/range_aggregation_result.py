from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket import Bucket


T = TypeVar("T", bound="RangeAggregationResult")


@_attrs_define
class RangeAggregationResult:
    """The result object of a range aggregation.
    <br>
     It consists mainly of buckets and within its inner aggregations results (sub-aggregations).

        Attributes:
            buckets (Union[Unset, List['Bucket']]):
    """

    buckets: Union[Unset, List["Bucket"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buckets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for componentsschemas_list_of_bucket_item_data in self.buckets:
                componentsschemas_list_of_bucket_item = componentsschemas_list_of_bucket_item_data.to_dict()
                buckets.append(componentsschemas_list_of_bucket_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bucket import Bucket

        d = src_dict.copy()
        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for componentsschemas_list_of_bucket_item_data in _buckets or []:
            componentsschemas_list_of_bucket_item = Bucket.from_dict(componentsschemas_list_of_bucket_item_data)

            buckets.append(componentsschemas_list_of_bucket_item)

        range_aggregation_result = cls(
            buckets=buckets,
        )

        range_aggregation_result.additional_properties = d
        return range_aggregation_result

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
