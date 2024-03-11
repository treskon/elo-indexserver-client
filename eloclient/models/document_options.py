from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.e_search_order_e import ESearchOrderE


T = TypeVar("T", bound="DocumentOptions")


@_attrs_define
class DocumentOptions:
    """Use this class to search for documents by
    {@link de.elo.ix.client.IXServicePortIF#findFirstSords(de.elo.ix.client.ClientInfo, de.elo.ix.client.FindInfo, int,
    de.elo.ix.client.SordZ)}
     and
     {@link de.elo.ix.client.IXServicePortIF#findNextSords(de.elo.ix.client.ClientInfo, String, int, int,
    de.elo.ix.client.SordZ)}.<br>
     Deliver query by {@link de.elo.ix.client.esearch.ESearchParams}.

        Attributes:
            sort (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
            highlighted_text (Union[Unset, bool]): Return highlighted result text for each sord.
                <br>
                 Highlighted text is retrieved from fulltext and surrounded by b-tags.<br>
                 Defaults to false.
            result_field (Union[Unset, bool]): Return fields in which search terms are found for each sord.
                <br>
                 Defaults to false.
            relevance (Union[Unset, bool]): Calculate relevance for each sord.
                <br>
                 Defaults to false.
            current_folder_id (Union[Unset, int]): Provide this ID to restrict search on current folder.
                <br>
    """

    sort: Union[Unset, "ESearchOrderE"] = UNSET
    highlighted_text: Union[Unset, bool] = UNSET
    result_field: Union[Unset, bool] = UNSET
    relevance: Union[Unset, bool] = UNSET
    current_folder_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sort: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        highlighted_text = self.highlighted_text
        result_field = self.result_field
        relevance = self.relevance
        current_folder_id = self.current_folder_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort is not UNSET:
            field_dict["sort"] = sort
        if highlighted_text is not UNSET:
            field_dict["highlightedText"] = highlighted_text
        if result_field is not UNSET:
            field_dict["resultField"] = result_field
        if relevance is not UNSET:
            field_dict["relevance"] = relevance
        if current_folder_id is not UNSET:
            field_dict["currentFolderId"] = current_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_search_order_e import ESearchOrderE

        d = src_dict.copy()
        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, ESearchOrderE]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = ESearchOrderE.from_dict(_sort)

        highlighted_text = d.pop("highlightedText", UNSET)

        result_field = d.pop("resultField", UNSET)

        relevance = d.pop("relevance", UNSET)

        current_folder_id = d.pop("currentFolderId", UNSET)

        document_options = cls(
            sort=sort,
            highlighted_text=highlighted_text,
            result_field=result_field,
            relevance=relevance,
            current_folder_id=current_folder_id,
        )

        document_options.additional_properties = d
        return document_options

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
