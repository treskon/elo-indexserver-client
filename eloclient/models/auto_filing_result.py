from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoFilingResult")


@_attrs_define
class AutoFilingResult:
    """Contains the archive destination returned by a call to
    {@link IXServicePortIF#evalAutoFiling(ClientInfo, String, Sord, AutoFilingOptions)}.

        Attributes:
            parent_ids (Union[Unset, List[int]]):
            paths_as_string (Union[Unset, List[str]]):
    """

    parent_ids: Union[Unset, List[int]] = UNSET
    paths_as_string: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.parent_ids, Unset):
            parent_ids = self.parent_ids

        paths_as_string: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paths_as_string, Unset):
            paths_as_string = self.paths_as_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_ids is not UNSET:
            field_dict["parentIds"] = parent_ids
        if paths_as_string is not UNSET:
            field_dict["pathsAsString"] = paths_as_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parent_ids = cast(List[int], d.pop("parentIds", UNSET))

        paths_as_string = cast(List[str], d.pop("pathsAsString", UNSET))

        auto_filing_result = cls(
            parent_ids=parent_ids,
            paths_as_string=paths_as_string,
        )

        auto_filing_result.additional_properties = d
        return auto_filing_result

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
