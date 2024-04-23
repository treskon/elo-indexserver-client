from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.e_search_options import ESearchOptions
    from ..models.e_search_params import ESearchParams


T = TypeVar("T", bound="FindByESearch")


@_attrs_define
class FindByESearch:
    """Use this class to search by iSearch with API functionality starting with ELO 11.

    Attributes:
        search_options (Union[Unset, ESearchOptions]): Class for various iSearch options.
        search_params (Union[Unset, ESearchParams]): Parameters for iSearch.
    """

    search_options: Union[Unset, "ESearchOptions"] = UNSET
    search_params: Union[Unset, "ESearchParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_options, Unset):
            search_options = self.search_options.to_dict()

        search_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_params, Unset):
            search_params = self.search_params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_options is not UNSET:
            field_dict["searchOptions"] = search_options
        if search_params is not UNSET:
            field_dict["searchParams"] = search_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_search_options import ESearchOptions
        from ..models.e_search_params import ESearchParams

        d = src_dict.copy()
        _search_options = d.pop("searchOptions", UNSET)
        search_options: Union[Unset, ESearchOptions]
        if isinstance(_search_options, Unset):
            search_options = UNSET
        else:
            search_options = ESearchOptions.from_dict(_search_options)

        _search_params = d.pop("searchParams", UNSET)
        search_params: Union[Unset, ESearchParams]
        if isinstance(_search_params, Unset):
            search_params = UNSET
        else:
            search_params = ESearchParams.from_dict(_search_params)

        find_by_e_search = cls(
            search_options=search_options,
            search_params=search_params,
        )

        find_by_e_search.additional_properties = d
        return find_by_e_search

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
