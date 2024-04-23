from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_term_query import ContextTermQuery


T = TypeVar("T", bound="ContextTermOptions")


@_attrs_define
class ContextTermOptions:
    """<p>
    Use this class if context terms should be retrieved by
     {@link de.elo.ix.client.IXServicePortIF#findContextTerms(de.elo.ix.client.ClientInfo, de.elo.ix.client.FindInfo,
    int)}.<br>
     Query is submitted by {@link de.elo.ix.client.esearch.ESearchParams}.
     </p>
     <p>
     Submit a list of ContextTermQuerys to retrieve context terms for each of them.<br>
     For every ContextTermQuerys, context terms are returned by adding all other ContextTermQuerys to
     the query but itself.<br>
     This means, if you want have various values for one index field, use one ContextTermQuery with a
     ValueList to submit the values instead of one ContextTermQuery for each value.<br>
     If a QueryFilter.value == null, it is not used to restrict the query. Context terms for this
     ContextTermQuery are returned.<br>
     </p>
     <p>
     The resulting list {@link ContextTermResults#contextTerms} is provided in the same order as the
     submitted list contextTermQueries
     </p>
     </p>

        Attributes:
            context_term_queries (Union[Unset, List['ContextTermQuery']]):
    """

    context_term_queries: Union[Unset, List["ContextTermQuery"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context_term_queries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.context_term_queries, Unset):
            context_term_queries = []
            for componentsschemas_list_of_context_term_query_item_data in self.context_term_queries:
                componentsschemas_list_of_context_term_query_item = (
                    componentsschemas_list_of_context_term_query_item_data.to_dict()
                )
                context_term_queries.append(componentsschemas_list_of_context_term_query_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_term_queries is not UNSET:
            field_dict["contextTermQueries"] = context_term_queries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.context_term_query import ContextTermQuery

        d = src_dict.copy()
        context_term_queries = []
        _context_term_queries = d.pop("contextTermQueries", UNSET)
        for componentsschemas_list_of_context_term_query_item_data in _context_term_queries or []:
            componentsschemas_list_of_context_term_query_item = ContextTermQuery.from_dict(
                componentsschemas_list_of_context_term_query_item_data
            )

            context_term_queries.append(componentsschemas_list_of_context_term_query_item)

        context_term_options = cls(
            context_term_queries=context_term_queries,
        )

        context_term_options.additional_properties = d
        return context_term_options

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
