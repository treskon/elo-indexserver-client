from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationOrderE")


@_attrs_define
class AggregationOrderE:
    """Sort options for ElasticSearch.
    <br>
     <br>
     By default, the terms aggregation orders terms by descending document _count. The date_histogram
     aggregation, however, sorts buckets by default by their key ascending.<br>
     Use the order parameter to specify a different sort order.<br>
     <br>
     We do not offer some sort order types if it is not guaranteed to produce reasonable results. E.g.
     Due to the way the terms aggregation gets terms from shards, sorting by ascending doc count often
     produces inaccurate results.<br>

        Attributes:
            key_desc (Union[Unset, AggregationOrderE]): Sort options for ElasticSearch.
                <br>
                 <br>
                 By default, the terms aggregation orders terms by descending document _count. The date_histogram
                 aggregation, however, sorts buckets by default by their key ascending.<br>
                 Use the order parameter to specify a different sort order.<br>
                 <br>
                 We do not offer some sort order types if it is not guaranteed to produce reasonable results. E.g.
                 Due to the way the terms aggregation gets terms from shards, sorting by ascending doc count often
                 produces inaccurate results.<br>
            count_desc (Union[Unset, AggregationOrderE]): Sort options for ElasticSearch.
                <br>
                 <br>
                 By default, the terms aggregation orders terms by descending document _count. The date_histogram
                 aggregation, however, sorts buckets by default by their key ascending.<br>
                 Use the order parameter to specify a different sort order.<br>
                 <br>
                 We do not offer some sort order types if it is not guaranteed to produce reasonable results. E.g.
                 Due to the way the terms aggregation gets terms from shards, sorting by ascending doc count often
                 produces inaccurate results.<br>
            key_asc (Union[Unset, AggregationOrderE]): Sort options for ElasticSearch.
                <br>
                 <br>
                 By default, the terms aggregation orders terms by descending document _count. The date_histogram
                 aggregation, however, sorts buckets by default by their key ascending.<br>
                 Use the order parameter to specify a different sort order.<br>
                 <br>
                 We do not offer some sort order types if it is not guaranteed to produce reasonable results. E.g.
                 Due to the way the terms aggregation gets terms from shards, sorting by ascending doc count often
                 produces inaccurate results.<br>
            default (Union[Unset, AggregationOrderE]): Sort options for ElasticSearch.
                <br>
                 <br>
                 By default, the terms aggregation orders terms by descending document _count. The date_histogram
                 aggregation, however, sorts buckets by default by their key ascending.<br>
                 Use the order parameter to specify a different sort order.<br>
                 <br>
                 We do not offer some sort order types if it is not guaranteed to produce reasonable results. E.g.
                 Due to the way the terms aggregation gets terms from shards, sorting by ascending doc count often
                 produces inaccurate results.<br>
    """

    key_desc: Union[Unset, "AggregationOrderE"] = UNSET
    count_desc: Union[Unset, "AggregationOrderE"] = UNSET
    key_asc: Union[Unset, "AggregationOrderE"] = UNSET
    default: Union[Unset, "AggregationOrderE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_desc, Unset):
            key_desc = self.key_desc.to_dict()

        count_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.count_desc, Unset):
            count_desc = self.count_desc.to_dict()

        key_asc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_asc, Unset):
            key_asc = self.key_asc.to_dict()

        default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_desc is not UNSET:
            field_dict["KEY_DESC"] = key_desc
        if count_desc is not UNSET:
            field_dict["COUNT_DESC"] = count_desc
        if key_asc is not UNSET:
            field_dict["KEY_ASC"] = key_asc
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _key_desc = d.pop("KEY_DESC", UNSET)
        key_desc: Union[Unset, AggregationOrderE]
        if isinstance(_key_desc, Unset):
            key_desc = UNSET
        else:
            key_desc = AggregationOrderE.from_dict(_key_desc)

        _count_desc = d.pop("COUNT_DESC", UNSET)
        count_desc: Union[Unset, AggregationOrderE]
        if isinstance(_count_desc, Unset):
            count_desc = UNSET
        else:
            count_desc = AggregationOrderE.from_dict(_count_desc)

        _key_asc = d.pop("KEY_ASC", UNSET)
        key_asc: Union[Unset, AggregationOrderE]
        if isinstance(_key_asc, Unset):
            key_asc = UNSET
        else:
            key_asc = AggregationOrderE.from_dict(_key_asc)

        _default = d.pop("DEFAULT", UNSET)
        default: Union[Unset, AggregationOrderE]
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = AggregationOrderE.from_dict(_default)

        aggregation_order_e = cls(
            key_desc=key_desc,
            count_desc=count_desc,
            key_asc=key_asc,
            default=default,
        )

        aggregation_order_e.additional_properties = d
        return aggregation_order_e

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
