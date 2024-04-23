from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindDirect")


@_attrs_define
class FindDirect:
    """<p>
    Search query for locating text in the archive.
     </p>

     <p>
     The fulltext search is performed via iSearch. Therefore, use
     {@link de.elo.ix.client.esearch.FindByESearch} instead. The {@link #query} should be replaces by
     the actual query term and additional filters (e.g. DocMask) should be submitted by
     {@link de.elo.ix.client.esearch.ESearchParams#queryOperator}. The areas in which should be search
     should be set in {@link de.elo.ix.client.esearch.ESearchParams#searchIn}.<br>
     Searches using this class are still executed but internally mapped to
     {@link de.elo.ix.client.esearch.FindByESearch} objects and some values might be ignored.
     </p>

        Attributes:
            search_in_memo (Union[Unset, bool]): <i>Is ignored, reserved for future use</i>
            search_in_sord_name (Union[Unset, bool]):
            search_in_fulltext (Union[Unset, bool]):
            search_in_index (Union[Unset, bool]):
            query (Union[Unset, str]): Search query.
            search_in_notes (Union[Unset, bool]): <i>Is ignored, reserved for future use</i>
            search_in_versions (Union[Unset, bool]):
    """

    search_in_memo: Union[Unset, bool] = UNSET
    search_in_sord_name: Union[Unset, bool] = UNSET
    search_in_fulltext: Union[Unset, bool] = UNSET
    search_in_index: Union[Unset, bool] = UNSET
    query: Union[Unset, str] = UNSET
    search_in_notes: Union[Unset, bool] = UNSET
    search_in_versions: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_in_memo = self.search_in_memo

        search_in_sord_name = self.search_in_sord_name

        search_in_fulltext = self.search_in_fulltext

        search_in_index = self.search_in_index

        query = self.query

        search_in_notes = self.search_in_notes

        search_in_versions = self.search_in_versions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_in_memo is not UNSET:
            field_dict["searchInMemo"] = search_in_memo
        if search_in_sord_name is not UNSET:
            field_dict["searchInSordName"] = search_in_sord_name
        if search_in_fulltext is not UNSET:
            field_dict["searchInFulltext"] = search_in_fulltext
        if search_in_index is not UNSET:
            field_dict["searchInIndex"] = search_in_index
        if query is not UNSET:
            field_dict["query"] = query
        if search_in_notes is not UNSET:
            field_dict["searchInNotes"] = search_in_notes
        if search_in_versions is not UNSET:
            field_dict["searchInVersions"] = search_in_versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_in_memo = d.pop("searchInMemo", UNSET)

        search_in_sord_name = d.pop("searchInSordName", UNSET)

        search_in_fulltext = d.pop("searchInFulltext", UNSET)

        search_in_index = d.pop("searchInIndex", UNSET)

        query = d.pop("query", UNSET)

        search_in_notes = d.pop("searchInNotes", UNSET)

        search_in_versions = d.pop("searchInVersions", UNSET)

        find_direct = cls(
            search_in_memo=search_in_memo,
            search_in_sord_name=search_in_sord_name,
            search_in_fulltext=search_in_fulltext,
            search_in_index=search_in_index,
            query=query,
            search_in_notes=search_in_notes,
            search_in_versions=search_in_versions,
        )

        find_direct.additional_properties = d
        return find_direct

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
