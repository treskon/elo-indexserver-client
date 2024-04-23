from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByFulltext")


@_attrs_define
class FindByFulltext:
    """<p>
    Performs a fulltext search.
     </p>

     <p>
     The fulltext search is performed via iSearch. Therefore, use
     {@link de.elo.ix.client.esearch.FindByESearch} instead. The {@link #term} should be replaces by
     the actual query term and additional filters (e.g. DocMask) should be submitted by
     {@link de.elo.ix.client.esearch.ESearchParams#queryOperator}. The areas in which should be search
     should be set in {@link de.elo.ix.client.esearch.ESearchParams#searchIn}.<br>
     Searches using this class are still executed but internally mapped to
     {@link de.elo.ix.client.esearch.FindByESearch} objects and some values might be ignored.
     </p>

        Attributes:
            term (Union[Unset, str]): Search term to be located in the fulltext database. Can be a single word or a number
                of words.
                Wildcard * is allowed, it matches any number of characters. Term is interpreted based on the
                 options given by FindOptions in FindInfo. Exception: FindOptionsC.ONE_TERM is not supported.
    """

    term: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        term = d.pop("term", UNSET)

        find_by_fulltext = cls(
            term=term,
        )

        find_by_fulltext.additional_properties = d
        return find_by_fulltext

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
