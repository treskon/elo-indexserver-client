from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchTermOptions")


@_attrs_define
class SearchTermOptions:
    """Use this class if alternative search terms should be retrieved by
    {@link de.elo.ix.client.IXServicePortIF#findSearchTerms(de.elo.ix.client.ClientInfo, de.elo.ix.client.FindInfo,
    int)}.<br>
     Deliver query by {@link de.elo.ix.client.esearch.ESearchParams}.

        Attributes:
            synonyms (Union[Unset, bool]): Return synonyms for search query.
            correction (Union[Unset, bool]): Return correction suggestion for search query.
                <br>
                 Example for a correction: tets -> test
    """

    synonyms: Union[Unset, bool] = UNSET
    correction: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        synonyms = self.synonyms

        correction = self.correction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if correction is not UNSET:
            field_dict["correction"] = correction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        synonyms = d.pop("synonyms", UNSET)

        correction = d.pop("correction", UNSET)

        search_term_options = cls(
            synonyms=synonyms,
            correction=correction,
        )

        search_term_options.additional_properties = d
        return search_term_options

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
