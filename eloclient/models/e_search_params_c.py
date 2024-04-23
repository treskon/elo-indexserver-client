from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ESearchParamsC")


@_attrs_define
class ESearchParamsC:
    """<p>
    Constants for searchIn selector.
     </p>
     <p>
     Example for multiple selection to search in title and fulltext:<br>
     <code>searchIn = SearchObjectC.TITLE | SearchObjectC.FULLTEXT</code>
     </p>

        Attributes:
            fulltext (Union[Unset, str]): Search in FULLTEXT
            version (Union[Unset, str]): Search in latest VERSION
            title (Union[Unset, str]): Search in title
            index_fields (Union[Unset, str]): Search in INDEX_FIELDS
            extra_text (Union[Unset, str]): Search in EXTRA_TEXT
            feed (Union[Unset, str]): Search in FEED
    """

    fulltext: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    index_fields: Union[Unset, str] = UNSET
    extra_text: Union[Unset, str] = UNSET
    feed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulltext = self.fulltext

        version = self.version

        title = self.title

        index_fields = self.index_fields

        extra_text = self.extra_text

        feed = self.feed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulltext is not UNSET:
            field_dict["FULLTEXT"] = fulltext
        if version is not UNSET:
            field_dict["VERSION"] = version
        if title is not UNSET:
            field_dict["TITLE"] = title
        if index_fields is not UNSET:
            field_dict["INDEX_FIELDS"] = index_fields
        if extra_text is not UNSET:
            field_dict["EXTRA_TEXT"] = extra_text
        if feed is not UNSET:
            field_dict["FEED"] = feed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fulltext = d.pop("FULLTEXT", UNSET)

        version = d.pop("VERSION", UNSET)

        title = d.pop("TITLE", UNSET)

        index_fields = d.pop("INDEX_FIELDS", UNSET)

        extra_text = d.pop("EXTRA_TEXT", UNSET)

        feed = d.pop("FEED", UNSET)

        e_search_params_c = cls(
            fulltext=fulltext,
            version=version,
            title=title,
            index_fields=index_fields,
            extra_text=extra_text,
            feed=feed,
        )

        e_search_params_c.additional_properties = d
        return e_search_params_c

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
