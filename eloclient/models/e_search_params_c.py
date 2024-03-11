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
            title (Union[Unset, str]): Search in title
            fulltext (Union[Unset, str]): Search in FULLTEXT
            index_fields (Union[Unset, str]): Search in INDEX_FIELDS
            extra_text (Union[Unset, str]): Search in EXTRA_TEXT
            version (Union[Unset, str]): Search in latest VERSION
            feed (Union[Unset, str]): Search in FEED
    """

    title: Union[Unset, str] = UNSET
    fulltext: Union[Unset, str] = UNSET
    index_fields: Union[Unset, str] = UNSET
    extra_text: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    feed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        fulltext = self.fulltext
        index_fields = self.index_fields
        extra_text = self.extra_text
        version = self.version
        feed = self.feed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["TITLE"] = title
        if fulltext is not UNSET:
            field_dict["FULLTEXT"] = fulltext
        if index_fields is not UNSET:
            field_dict["INDEX_FIELDS"] = index_fields
        if extra_text is not UNSET:
            field_dict["EXTRA_TEXT"] = extra_text
        if version is not UNSET:
            field_dict["VERSION"] = version
        if feed is not UNSET:
            field_dict["FEED"] = feed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("TITLE", UNSET)

        fulltext = d.pop("FULLTEXT", UNSET)

        index_fields = d.pop("INDEX_FIELDS", UNSET)

        extra_text = d.pop("EXTRA_TEXT", UNSET)

        version = d.pop("VERSION", UNSET)

        feed = d.pop("FEED", UNSET)

        e_search_params_c = cls(
            title=title,
            fulltext=fulltext,
            index_fields=index_fields,
            extra_text=extra_text,
            version=version,
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
