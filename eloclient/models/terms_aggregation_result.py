from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket import Bucket


T = TypeVar("T", bound="TermsAggregationResult")


@_attrs_define
class TermsAggregationResult:
    """The result object of a terms aggregation.
    <br>
     It consists mainly of buckets and within its inner aggregations results (sub-aggregations).

        Attributes:
            sum_other_doc_count (Union[Unset, str]): Number of documents that didn’t make it into the the top size terms.
                <br>
                 If this is greater than 0, you can be sure that the terms agg had to throw away some buckets,
                 either because they didn’t fit into size on the coordinating node or they didn’t fit into
                 shard_size on the data node.
            doc_count_error_upper_bound (Union[Unset, str]): If you set the show_term_doc_count_error parameter to true, the
                terms aggregation will include
                doc_count_error_upper_bound, which is an upper bound to the error on the doc_count returned by
                 each shard. It’s the sum of the size of the largest bucket on each shard that didn’t fit into
                 shard_size.
            buckets (Union[Unset, List['Bucket']]):
    """

    sum_other_doc_count: Union[Unset, str] = UNSET
    doc_count_error_upper_bound: Union[Unset, str] = UNSET
    buckets: Union[Unset, List["Bucket"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sum_other_doc_count = self.sum_other_doc_count

        doc_count_error_upper_bound = self.doc_count_error_upper_bound

        buckets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for componentsschemas_list_of_bucket_item_data in self.buckets:
                componentsschemas_list_of_bucket_item = componentsschemas_list_of_bucket_item_data.to_dict()
                buckets.append(componentsschemas_list_of_bucket_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sum_other_doc_count is not UNSET:
            field_dict["sumOtherDocCount"] = sum_other_doc_count
        if doc_count_error_upper_bound is not UNSET:
            field_dict["docCountErrorUpperBound"] = doc_count_error_upper_bound
        if buckets is not UNSET:
            field_dict["buckets"] = buckets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bucket import Bucket

        d = src_dict.copy()
        sum_other_doc_count = d.pop("sumOtherDocCount", UNSET)

        doc_count_error_upper_bound = d.pop("docCountErrorUpperBound", UNSET)

        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for componentsschemas_list_of_bucket_item_data in _buckets or []:
            componentsschemas_list_of_bucket_item = Bucket.from_dict(componentsschemas_list_of_bucket_item_data)

            buckets.append(componentsschemas_list_of_bucket_item)

        terms_aggregation_result = cls(
            sum_other_doc_count=sum_other_doc_count,
            doc_count_error_upper_bound=doc_count_error_upper_bound,
            buckets=buckets,
        )

        terms_aggregation_result.additional_properties = d
        return terms_aggregation_result

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
