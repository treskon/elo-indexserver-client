from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_order_sequence_e import SortOrderSequenceE


T = TypeVar("T", bound="FindResultSortSpecification")


@_attrs_define
class FindResultSortSpecification:
    """This class specifies the sorting criteria of a search for aspect data.

    Attributes:
        sort_order_sequence (Union[Unset, SortOrderSequenceE]): Possible sorting sequences of database searches for
            aspect data.
        key (Union[Unset, str]): This key specifies the {@link AspectLine} as sorting criteria.
            The string must be in the same
             syntax as the key in {@link FindByIndex#aspects}:

             <pre>
             {@code AspectAssoc¶Aspect¶AspectLine}
             </pre>

             The server expects their corresponding technical identifiers - meaning
             {@link AspectAssoc#name}, {@link Aspect#name}, and {@link AspectLine#key} respectively. Similar
             to the key in {@link FindByIndex#aspects} you may leave the name of the {@link Aspect} and
             {@link AspectAssoc} empty, but not the key of the {@link AspectLine}.
    """

    sort_order_sequence: Union[Unset, "SortOrderSequenceE"] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sort_order_sequence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort_order_sequence, Unset):
            sort_order_sequence = self.sort_order_sequence.to_dict()

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_order_sequence is not UNSET:
            field_dict["sortOrderSequence"] = sort_order_sequence
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sort_order_sequence_e import SortOrderSequenceE

        d = src_dict.copy()
        _sort_order_sequence = d.pop("sortOrderSequence", UNSET)
        sort_order_sequence: Union[Unset, SortOrderSequenceE]
        if isinstance(_sort_order_sequence, Unset):
            sort_order_sequence = UNSET
        else:
            sort_order_sequence = SortOrderSequenceE.from_dict(_sort_order_sequence)

        key = d.pop("key", UNSET)

        find_result_sort_specification = cls(
            sort_order_sequence=sort_order_sequence,
            key=key,
        )

        find_result_sort_specification.additional_properties = d
        return find_result_sort_specification

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
