from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_type_e import FieldTypeE
    from ..models.query_filter import QueryFilter


T = TypeVar("T", bound="CompletionOptions")


@_attrs_define
class CompletionOptions:
    """Use this class if a completion should be retrieved by
    {@link de.elo.ix.client.IXServicePortIF#findCompletion(de.elo.ix.client.ClientInfo, de.elo.ix.client.FindInfo,
    int)}.<br>
     Deliver text to complete in {@link de.elo.ix.client.esearch.ESearchParams#query}.

        Attributes:
            completion_field (Union[Unset, QueryFilter]): <p>
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
            return_type (Union[Unset, FieldTypeE]): <p>
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

    completion_field: Union[Unset, "QueryFilter"] = UNSET
    return_type: Union[Unset, "FieldTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.completion_field, Unset):
            completion_field = self.completion_field.to_dict()

        return_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_type, Unset):
            return_type = self.return_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_field is not UNSET:
            field_dict["completionField"] = completion_field
        if return_type is not UNSET:
            field_dict["returnType"] = return_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_type_e import FieldTypeE
        from ..models.query_filter import QueryFilter

        d = src_dict.copy()
        _completion_field = d.pop("completionField", UNSET)
        completion_field: Union[Unset, QueryFilter]
        if isinstance(_completion_field, Unset):
            completion_field = UNSET
        else:
            completion_field = QueryFilter.from_dict(_completion_field)

        _return_type = d.pop("returnType", UNSET)
        return_type: Union[Unset, FieldTypeE]
        if isinstance(_return_type, Unset):
            return_type = UNSET
        else:
            return_type = FieldTypeE.from_dict(_return_type)

        completion_options = cls(
            completion_field=completion_field,
            return_type=return_type,
        )

        completion_options.additional_properties = d
        return completion_options

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
