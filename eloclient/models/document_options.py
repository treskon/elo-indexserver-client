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
            highlighted_text (Union[Unset, bool]): Return highlighted result text for each sord.
                <br>
                 Highlighted text is retrieved from fulltext and surrounded by b-tags.<br>
                 Defaults to false.
            result_field (Union[Unset, bool]): Return fields in which search terms are found for each sord.
                <br>
                 Defaults to false.
            sort (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
            current_folder_id (Union[Unset, int]): Provide this ID to restrict search on current folder.
                <br>
            relevance (Union[Unset, bool]): Calculate relevance for each sord.
                <br>
                 Defaults to false.
    """

    highlighted_text: Union[Unset, bool] = UNSET
    result_field: Union[Unset, bool] = UNSET
    sort: Union[Unset, "ESearchOrderE"] = UNSET
    current_folder_id: Union[Unset, int] = UNSET
    relevance: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        highlighted_text = self.highlighted_text

        result_field = self.result_field

        sort: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        current_folder_id = self.current_folder_id

        relevance = self.relevance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if highlighted_text is not UNSET:
            field_dict["highlightedText"] = highlighted_text
        if result_field is not UNSET:
            field_dict["resultField"] = result_field
        if sort is not UNSET:
            field_dict["sort"] = sort
        if current_folder_id is not UNSET:
            field_dict["currentFolderId"] = current_folder_id
        if relevance is not UNSET:
            field_dict["relevance"] = relevance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_search_order_e import ESearchOrderE

        d = src_dict.copy()
        highlighted_text = d.pop("highlightedText", UNSET)

        result_field = d.pop("resultField", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, ESearchOrderE]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = ESearchOrderE.from_dict(_sort)

        current_folder_id = d.pop("currentFolderId", UNSET)

        relevance = d.pop("relevance", UNSET)

        document_options = cls(
            highlighted_text=highlighted_text,
            result_field=result_field,
            sort=sort,
            current_folder_id=current_folder_id,
            relevance=relevance,
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
