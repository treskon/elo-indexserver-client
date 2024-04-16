from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NavigationInfoC")


@_attrs_define
class NavigationInfoC:
    """Constants class for the NavigationInfo class.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            min_nav_depth (Union[Unset, int]): The minimum depth for tree walks.
            min_nav_max_count (Union[Unset, int]): The overall limit for any visited element.
            skip_nav_limit (Union[Unset, int]): This constant is used to override the navigation limit.
            min_nav_siblings (Union[Unset, int]): The minimum amount of collected siblings.
    """

    min_nav_depth: Union[Unset, int] = UNSET
    min_nav_max_count: Union[Unset, int] = UNSET
    skip_nav_limit: Union[Unset, int] = UNSET
    min_nav_siblings: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_nav_depth = self.min_nav_depth

        min_nav_max_count = self.min_nav_max_count

        skip_nav_limit = self.skip_nav_limit

        min_nav_siblings = self.min_nav_siblings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_nav_depth is not UNSET:
            field_dict["MIN_NAV_DEPTH"] = min_nav_depth
        if min_nav_max_count is not UNSET:
            field_dict["MIN_NAV_MAX_COUNT"] = min_nav_max_count
        if skip_nav_limit is not UNSET:
            field_dict["SKIP_NAV_LIMIT"] = skip_nav_limit
        if min_nav_siblings is not UNSET:
            field_dict["MIN_NAV_SIBLINGS"] = min_nav_siblings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_nav_depth = d.pop("MIN_NAV_DEPTH", UNSET)

        min_nav_max_count = d.pop("MIN_NAV_MAX_COUNT", UNSET)

        skip_nav_limit = d.pop("SKIP_NAV_LIMIT", UNSET)

        min_nav_siblings = d.pop("MIN_NAV_SIBLINGS", UNSET)

        navigation_info_c = cls(
            min_nav_depth=min_nav_depth,
            min_nav_max_count=min_nav_max_count,
            skip_nav_limit=skip_nav_limit,
            min_nav_siblings=min_nav_siblings,
        )

        navigation_info_c.additional_properties = d
        return navigation_info_c

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
