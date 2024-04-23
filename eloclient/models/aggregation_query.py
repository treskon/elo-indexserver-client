from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_query_params import AggregationQueryParams
    from ..models.aggregation_type_e import AggregationTypeE
    from ..models.field_type_e import FieldTypeE
    from ..models.search_field_e import SearchFieldE


T = TypeVar("T", bound="AggregationQuery")


@_attrs_define
class AggregationQuery:
    """
    Attributes:
        aggregation_query_params (Union[Unset, AggregationQueryParams]): Base class for aggregation type specific
            parameters given in an AggregationQuery.
        search_field (Union[Unset, SearchFieldE]): <p>
            Use this class of constants to define in which field should be searched or aggregated.
             </p>
             <p>
             For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
             type is incorrect.
             </p>
        index_field_key (Union[Unset, str]): If searchfield equals to SearchFieldE.INDEXFIELD, provide the name of the
            index field here.
            <br>
             If searchField != SearchFieldE.INDEXFIELD, this value is ignored. If the associated docmask is
             of type DocMaskC.DATA_ORGANISATION_OBJKEYS or DATA_ORGANISATION_TABLE the value of this field
             should be the line key of the docMaskLine. If the associated docMask is of type
             DocMaskC.DATA_ORGANISATION_ASPECT the value of this field should be the name of the aspectAssoc
             followed by "¶" followed by the line key of the aspectLine, e.g. CUSTOMERADDRESS¶STREET.
        name (Union[Unset, str]):
        type (Union[Unset, AggregationTypeE]): Types of Aggregations for ESearch AggregationQuery.
        field_type (Union[Unset, FieldTypeE]): <p>
            This enum defines how should be searched for query terms.
             </p>

             <p>
             It can, for example, be used with {@link QueryFilter#fieldType}
             </p>
             <p>
             For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
             therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
             </p>
    """

    aggregation_query_params: Union[Unset, "AggregationQueryParams"] = UNSET
    search_field: Union[Unset, "SearchFieldE"] = UNSET
    index_field_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, "AggregationTypeE"] = UNSET
    field_type: Union[Unset, "FieldTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregation_query_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregation_query_params, Unset):
            aggregation_query_params = self.aggregation_query_params.to_dict()

        search_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_field, Unset):
            search_field = self.search_field.to_dict()

        index_field_key = self.index_field_key

        name = self.name

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_query_params is not UNSET:
            field_dict["aggregationQueryParams"] = aggregation_query_params
        if search_field is not UNSET:
            field_dict["searchField"] = search_field
        if index_field_key is not UNSET:
            field_dict["indexFieldKey"] = index_field_key
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_query_params import AggregationQueryParams
        from ..models.aggregation_type_e import AggregationTypeE
        from ..models.field_type_e import FieldTypeE
        from ..models.search_field_e import SearchFieldE

        d = src_dict.copy()
        _aggregation_query_params = d.pop("aggregationQueryParams", UNSET)
        aggregation_query_params: Union[Unset, AggregationQueryParams]
        if isinstance(_aggregation_query_params, Unset):
            aggregation_query_params = UNSET
        else:
            aggregation_query_params = AggregationQueryParams.from_dict(_aggregation_query_params)

        _search_field = d.pop("searchField", UNSET)
        search_field: Union[Unset, SearchFieldE]
        if isinstance(_search_field, Unset):
            search_field = UNSET
        else:
            search_field = SearchFieldE.from_dict(_search_field)

        index_field_key = d.pop("indexFieldKey", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AggregationTypeE]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AggregationTypeE.from_dict(_type)

        _field_type = d.pop("fieldType", UNSET)
        field_type: Union[Unset, FieldTypeE]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = FieldTypeE.from_dict(_field_type)

        aggregation_query = cls(
            aggregation_query_params=aggregation_query_params,
            search_field=search_field,
            index_field_key=index_field_key,
            name=name,
            type=type,
            field_type=field_type,
        )

        aggregation_query.additional_properties = d
        return aggregation_query

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
