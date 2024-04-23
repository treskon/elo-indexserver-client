from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_type_e import FieldTypeE
    from ..models.filter_value import FilterValue
    from ..models.search_field_e import SearchFieldE


T = TypeVar("T", bound="QueryFilter")


@_attrs_define
class QueryFilter:
    """<p>
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
     <code>fieldType = SearchFieldC.INDEXFIELD; docMaskLine="NUMERICFIELD", FilterValue = new IntValue(200); fieldType =
    FieldTypeC.numeric;</code>
     </ul>
     </p>

        Attributes:
            search_field (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            index_field_key (Union[Unset, str]): Provide the name of the index field here.
                <br>
                 If searchField != SearchFieldC.INDEXFIELD, this value is ignored. If the associated docmask is
                 of type DocMaskC.DATA_ORGANISATION_OBJKEYS or DATA_ORGANISATION_TABLE the value of this field
                 should be the line key of the docMaskLine. If the associated docMask is of type
                 DocMaskC.DATA_ORGANISATION_ASPECT the value of this field should be the name of the aspectAssoc
                 followed by "¶" followed by the line key of the aspectLine, e.g. CUSTOMERADDRESS¶STREET.
            doc_mask_line (Union[Unset, str]): Provide the name of the index field here.
                <br>
                 If searchField != SearchFieldC.INDEXFIELD, this value is ignored.
            boost (Union[Unset, float]): Boost for calculated relevance.
                <br>
                 A field can be boosted and therefore has a higher influence on the calculated relevance.<br>
                 For more information, refere to <a href=
                 'https://www.elastic.co/guide/en/elasticsearch/guide/current/multi-query-strings.html#prioritising-
                clauses'>https://www.elastic.co/guide/en/elasticsearch/guide/current/multi-query-strings.html#prioritising-
                clauses</a>
            value (Union[Unset, FilterValue]): Deliver a value for QueryFilter.
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

    search_field: Union[Unset, "SearchFieldE"] = UNSET
    index_field_key: Union[Unset, str] = UNSET
    doc_mask_line: Union[Unset, str] = UNSET
    boost: Union[Unset, float] = UNSET
    value: Union[Unset, "FilterValue"] = UNSET
    field_type: Union[Unset, "FieldTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_field, Unset):
            search_field = self.search_field.to_dict()

        index_field_key = self.index_field_key

        doc_mask_line = self.doc_mask_line

        boost = self.boost

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_field is not UNSET:
            field_dict["searchField"] = search_field
        if index_field_key is not UNSET:
            field_dict["indexFieldKey"] = index_field_key
        if doc_mask_line is not UNSET:
            field_dict["docMaskLine"] = doc_mask_line
        if boost is not UNSET:
            field_dict["boost"] = boost
        if value is not UNSET:
            field_dict["value"] = value
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_type_e import FieldTypeE
        from ..models.filter_value import FilterValue
        from ..models.search_field_e import SearchFieldE

        d = src_dict.copy()
        _search_field = d.pop("searchField", UNSET)
        search_field: Union[Unset, SearchFieldE]
        if isinstance(_search_field, Unset):
            search_field = UNSET
        else:
            search_field = SearchFieldE.from_dict(_search_field)

        index_field_key = d.pop("indexFieldKey", UNSET)

        doc_mask_line = d.pop("docMaskLine", UNSET)

        boost = d.pop("boost", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, FilterValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = FilterValue.from_dict(_value)

        _field_type = d.pop("fieldType", UNSET)
        field_type: Union[Unset, FieldTypeE]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = FieldTypeE.from_dict(_field_type)

        query_filter = cls(
            search_field=search_field,
            index_field_key=index_field_key,
            doc_mask_line=doc_mask_line,
            boost=boost,
            value=value,
            field_type=field_type,
        )

        query_filter.additional_properties = d
        return query_filter

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
