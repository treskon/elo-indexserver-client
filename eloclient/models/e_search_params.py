from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_operator import QueryOperator


T = TypeVar("T", bound="ESearchParams")


@_attrs_define
class ESearchParams:
    """Parameters for iSearch.

    Attributes:
        query (Union[Unset, str]): <p>
            QueryString
             </p>
             <p>
             Note: Do not escaped any characters, this is done by IX.
             <p>
             <p>
             A PowerSearch is enabled if query starts with <i>=</i>. In this case, nothing is escaped by IX.
        search_in (Union[Unset, str]): <p>
            Select which Information should be searched.
             <p>

             <p>
             Example for multiple selection to search in title and fulltext:<br>
             <code>searchIn = SearchObjectC.TITLE | SearchObjectC.FULLTEXT</code>
             <p>
        query_operator (Union[Unset, QueryOperator]): A QueryOperator is used to include or exclude QueryObjects from a
            search and to concatenate
            QueryObjects.<br>
             Like this, complex queries can be build.
        incl_deleted (Union[Unset, int]): Define if deleted sords should be included:
            <ul>
             <li>0: exclude deleted sords (default).
             <li>1: include deleted sords.
             <li>2: only deleted sords.
             </ul>
    """

    query: Union[Unset, str] = UNSET
    search_in: Union[Unset, str] = UNSET
    query_operator: Union[Unset, "QueryOperator"] = UNSET
    incl_deleted: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        search_in = self.search_in

        query_operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_operator, Unset):
            query_operator = self.query_operator.to_dict()

        incl_deleted = self.incl_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if search_in is not UNSET:
            field_dict["searchIn"] = search_in
        if query_operator is not UNSET:
            field_dict["queryOperator"] = query_operator
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_operator import QueryOperator

        d = src_dict.copy()
        query = d.pop("query", UNSET)

        search_in = d.pop("searchIn", UNSET)

        _query_operator = d.pop("queryOperator", UNSET)
        query_operator: Union[Unset, QueryOperator]
        if isinstance(_query_operator, Unset):
            query_operator = UNSET
        else:
            query_operator = QueryOperator.from_dict(_query_operator)

        incl_deleted = d.pop("inclDeleted", UNSET)

        e_search_params = cls(
            query=query,
            search_in=search_in,
            query_operator=query_operator,
            incl_deleted=incl_deleted,
        )

        e_search_params.additional_properties = d
        return e_search_params

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
