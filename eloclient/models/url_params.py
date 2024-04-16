from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlParams")


@_attrs_define
class UrlParams:
    """This class describes additional params for an upload or download URL.

    Attributes:
        offset (Union[Unset, str]): Download bytes beginning from this offset.
        length (Union[Unset, str]): Download only length bytes from the resource. Set this value to 0, if all bytes
            should be read.
        highlight_terms (Union[Unset, str]): Highlight this terms. This value is only valid for fulltext URLs.
            Many terms have to be
             separated by space character. Each term is enclosed in the HTML tags &lt;b&gt; term &lt;/b&gt;
    """

    offset: Union[Unset, str] = UNSET
    length: Union[Unset, str] = UNSET
    highlight_terms: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offset = self.offset

        length = self.length

        highlight_terms = self.highlight_terms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if length is not UNSET:
            field_dict["length"] = length
        if highlight_terms is not UNSET:
            field_dict["highlightTerms"] = highlight_terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        offset = d.pop("offset", UNSET)

        length = d.pop("length", UNSET)

        highlight_terms = d.pop("highlightTerms", UNSET)

        url_params = cls(
            offset=offset,
            length=length,
            highlight_terms=highlight_terms,
        )

        url_params.additional_properties = d
        return url_params

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
