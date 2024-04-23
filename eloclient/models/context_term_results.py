from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_term import ContextTerm


T = TypeVar("T", bound="ContextTermResults")


@_attrs_define
class ContextTermResults:
    """
    Attributes:
        context_terms (Union[Unset, List['ContextTerm']]):
    """

    context_terms: Union[Unset, List["ContextTerm"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context_terms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.context_terms, Unset):
            context_terms = []
            for componentsschemas_list_of_context_term_item_data in self.context_terms:
                componentsschemas_list_of_context_term_item = componentsschemas_list_of_context_term_item_data.to_dict()
                context_terms.append(componentsschemas_list_of_context_term_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_terms is not UNSET:
            field_dict["contextTerms"] = context_terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.context_term import ContextTerm

        d = src_dict.copy()
        context_terms = []
        _context_terms = d.pop("contextTerms", UNSET)
        for componentsschemas_list_of_context_term_item_data in _context_terms or []:
            componentsschemas_list_of_context_term_item = ContextTerm.from_dict(
                componentsschemas_list_of_context_term_item_data
            )

            context_terms.append(componentsschemas_list_of_context_term_item)

        context_term_results = cls(
            context_terms=context_terms,
        )

        context_term_results.additional_properties = d
        return context_term_results

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
