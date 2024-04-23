from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_term_return_type_e import ContextTermReturnTypeE
    from ..models.query_filter import QueryFilter


T = TypeVar("T", bound="ContextTermQuery")


@_attrs_define
class ContextTermQuery:
    """<p>
    Submit a ContextTermQuery for each ContextTerm to be retrieved.
     </p>
     <p>
     Describe the contextTerm in with filter. If a value is committed, this value is used to calculate
     every other ContextTerm in ContextTermOptions.contextTermQueries
     <p>
     <p>
     Specify a return type for each contextTerm: {@link ContextTermReturnTypeE}
     </p>
     <p>
     To exclude a value from contextTerms, use set isNegated=true. Defaults to false.
     </p>

        Attributes:
            filter_ (Union[Unset, QueryFilter]): <p>
                A QueryFilter is used to describe a value to search for in a document.
                 </p>
                 <p>
                 It references a field in which should be searched and its value.
                 </p>
                 <p>
                 There are other usecases, in which a QueryFilter is used to describe a certain field and its
                 value is not needed and therefore ignored: To retrieve context terms and completions.
                 </p>
                 <p>
                 <b>Usage:</b> Define where to search for the value by the parameters searchField and
                 indexFieldKey. If the field you want to search in is defined in SearchFieldC, use one of the
                 constants. In this case, the value of indexFieldKey is ignored.<br>
                 If you want to search in an index field, set searchField = SearchFieldC.INDEXFIELD and provide
                 its name in indexFieldKey. For a DocMask with data organization "Aspect" the indexFieldKey must
                 contain the name of the aspectAssoc and the lineKey of the aspectLine separated by "¶". For a
                 DocMask with data organization "ObjKey" or "Table" the indexFieldKey must contain the lineKey of
                 the docMaskLine.
                 <p>
                 <b>Examples:</b>
                 <ul>
                 <li>Search for "Hello World" in the title:<br>
                 <code>fieldType = SearchFieldC.TITLE; FilterValue = new StringValue("Hello World"); fieldType =
                FieldTypeC.tokenized;</code>
                 <li>Search for "200" in a numeric index line called NUMERICFIELD:<br>
                 <code>fieldType = SearchFieldC.INDEXFIELD; docMaskLine="NUMERICFIELD", FilterValue = new IntValue(200);
                fieldType = FieldTypeC.numeric;</code>
                 </ul>
                 </p>
            is_negated (Union[Unset, bool]): To exclude a value from contextTerms, use set isNegated=true. Defaults to
                false.
            return_type (Union[Unset, ContextTermReturnTypeE]): Specifies the return type for context terms.
    """

    filter_: Union[Unset, "QueryFilter"] = UNSET
    is_negated: Union[Unset, bool] = UNSET
    return_type: Union[Unset, "ContextTermReturnTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        is_negated = self.is_negated

        return_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_type, Unset):
            return_type = self.return_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if is_negated is not UNSET:
            field_dict["isNegated"] = is_negated
        if return_type is not UNSET:
            field_dict["returnType"] = return_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.context_term_return_type_e import ContextTermReturnTypeE
        from ..models.query_filter import QueryFilter

        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, QueryFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = QueryFilter.from_dict(_filter_)

        is_negated = d.pop("isNegated", UNSET)

        _return_type = d.pop("returnType", UNSET)
        return_type: Union[Unset, ContextTermReturnTypeE]
        if isinstance(_return_type, Unset):
            return_type = UNSET
        else:
            return_type = ContextTermReturnTypeE.from_dict(_return_type)

        context_term_query = cls(
            filter_=filter_,
            is_negated=is_negated,
            return_type=return_type,
        )

        context_term_query.additional_properties = d
        return context_term_query

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
