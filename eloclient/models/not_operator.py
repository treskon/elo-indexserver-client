from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_filter import QueryFilter


T = TypeVar("T", bound="NotOperator")


@_attrs_define
class NotOperator:
    """This operator contains a single QueryObject which is excluded from the search.
    This means, a
     document is returned if the QueryObject is not present in the document.

        Attributes:
            query_filter (Union[Unset, QueryFilter]): <p>
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
    """

    query_filter: Union[Unset, "QueryFilter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_filter, Unset):
            query_filter = self.query_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_filter is not UNSET:
            field_dict["queryFilter"] = query_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_filter import QueryFilter

        d = src_dict.copy()
        _query_filter = d.pop("queryFilter", UNSET)
        query_filter: Union[Unset, QueryFilter]
        if isinstance(_query_filter, Unset):
            query_filter = UNSET
        else:
            query_filter = QueryFilter.from_dict(_query_filter)

        not_operator = cls(
            query_filter=query_filter,
        )

        not_operator.additional_properties = d
        return not_operator

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
