from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_field_e import SearchFieldE
    from ..models.sord import Sord


T = TypeVar("T", bound="FindByFulltextResultItem")


@_attrs_define
class FindByFulltextResultItem:
    """Additional information for an item found by fulltext search.

    Attributes:
        relevance (Union[Unset, int]): Relevance in per mill.
        summary_fulltext (Union[Unset, str]): Textpart from document.
        summary_desc (Union[Unset, str]): Textpart from memo text.
        field_names (Union[Unset, List[str]]):
        result_fields (Union[Unset, List['SearchFieldE']]):
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    relevance: Union[Unset, int] = UNSET
    summary_fulltext: Union[Unset, str] = UNSET
    summary_desc: Union[Unset, str] = UNSET
    field_names: Union[Unset, List[str]] = UNSET
    result_fields: Union[Unset, List["SearchFieldE"]] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relevance = self.relevance
        summary_fulltext = self.summary_fulltext
        summary_desc = self.summary_desc
        field_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_names, Unset):
            field_names = self.field_names

        result_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result_fields, Unset):
            result_fields = []
            for componentsschemas_array_list_of_search_field_e_item_data in self.result_fields:
                componentsschemas_array_list_of_search_field_e_item = (
                    componentsschemas_array_list_of_search_field_e_item_data.to_dict()
                )

                result_fields.append(componentsschemas_array_list_of_search_field_e_item)

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relevance is not UNSET:
            field_dict["relevance"] = relevance
        if summary_fulltext is not UNSET:
            field_dict["summaryFulltext"] = summary_fulltext
        if summary_desc is not UNSET:
            field_dict["summaryDesc"] = summary_desc
        if field_names is not UNSET:
            field_dict["fieldNames"] = field_names
        if result_fields is not UNSET:
            field_dict["resultFields"] = result_fields
        if sord is not UNSET:
            field_dict["sord"] = sord

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_field_e import SearchFieldE
        from ..models.sord import Sord

        d = src_dict.copy()
        relevance = d.pop("relevance", UNSET)

        summary_fulltext = d.pop("summaryFulltext", UNSET)

        summary_desc = d.pop("summaryDesc", UNSET)

        field_names = cast(List[str], d.pop("fieldNames", UNSET))

        result_fields = []
        _result_fields = d.pop("resultFields", UNSET)
        for componentsschemas_array_list_of_search_field_e_item_data in _result_fields or []:
            componentsschemas_array_list_of_search_field_e_item = SearchFieldE.from_dict(
                componentsschemas_array_list_of_search_field_e_item_data
            )

            result_fields.append(componentsschemas_array_list_of_search_field_e_item)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        find_by_fulltext_result_item = cls(
            relevance=relevance,
            summary_fulltext=summary_fulltext,
            summary_desc=summary_desc,
            field_names=field_names,
            result_fields=result_fields,
            sord=sord,
        )

        find_by_fulltext_result_item.additional_properties = d
        return find_by_fulltext_result_item

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
