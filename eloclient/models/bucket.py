from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_type_e import AggregationTypeE
    from ..models.map_to_aggregation_result import MapToAggregationResult


T = TypeVar("T", bound="Bucket")


@_attrs_define
class Bucket:
    """Represents a bucket within an AggregationResult for a bucket aggregation.

    Attributes:
        doc_count (Union[Unset, str]): Number of documents belonging to the bucket's criteria.
        from_ (Union[Unset, str]): For aggregations of type RANGE and DATE_RANGE, this value is a string representation
            of the
            lower bound of this bucket.
        to (Union[Unset, str]): For aggregations of type RANGE and DATE_RANGE, this value is a string representation of
            the
            upper bound of this bucket.
        type (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        aggregations (Union[Unset, MapToAggregationResult]):
        key (Union[Unset, str]): The bucket key identifying the bucket.
    """

    doc_count: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    type: Union[Unset, "AggregationTypeE"] = UNSET
    aggregations: Union[Unset, "MapToAggregationResult"] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_count = self.doc_count

        from_ = self.from_

        to = self.to

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregations, Unset):
            aggregations = self.aggregations.to_dict()

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_count is not UNSET:
            field_dict["docCount"] = doc_count
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if type is not UNSET:
            field_dict["type"] = type
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_type_e import AggregationTypeE
        from ..models.map_to_aggregation_result import MapToAggregationResult

        d = src_dict.copy()
        doc_count = d.pop("docCount", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AggregationTypeE]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AggregationTypeE.from_dict(_type)

        _aggregations = d.pop("aggregations", UNSET)
        aggregations: Union[Unset, MapToAggregationResult]
        if isinstance(_aggregations, Unset):
            aggregations = UNSET
        else:
            aggregations = MapToAggregationResult.from_dict(_aggregations)

        key = d.pop("key", UNSET)

        bucket = cls(
            doc_count=doc_count,
            from_=from_,
            to=to,
            type=type,
            aggregations=aggregations,
            key=key,
        )

        bucket.additional_properties = d
        return bucket

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
