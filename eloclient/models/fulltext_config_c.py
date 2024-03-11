from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulltextConfigC")


@_attrs_define
class FulltextConfigC:
    """Constants for class FulltextConfig.

    Attributes:
        source_classic (Union[Unset, int]): Use fulltext information from inverse index stored in the archive database.
        source_ftcat (Union[Unset, int]): Use fulltext information from Microsoft SQL-Server fulltext catalog.
        source_isearch (Union[Unset, int]): Use fulltext information from iSearch.
        source_elasticsearch (Union[Unset, int]): Use fulltext information from Elasticsearch.
        flag_isearch_did_you_mean (Union[Unset, int]): Evaluate suggestions for similar terms (= corrections)
        flag_isearch_search_as_you_type (Union[Unset, int]): Perform a search for each pressed key (= completion)
        flag_isearch_summary (Union[Unset, int]): Retrieve a summary text for each word.
        flag_isearch_company_thesaurus (Union[Unset, int]): Use the thesaurus of the company.
        flag_isearch_knowlege_map (Union[Unset, int]): Use the extension "Knowlege Map".
        flag_isearch_ontology_net (Union[Unset, int]): Use the extension "Ontology Net".
        flag_isearch_elo_thesaurus (Union[Unset, int]): Use thesaurus provided by ELO (= synonyms)
        flag_isearch_optionsoff (Union[Unset, int]): Turn off all search options (if 0 or not in db, a default set of
            search options (correction, synonyms, search
            terms) is turned on). If combined with other flags, the other options are turned on.
        flag_isearch_feed (Union[Unset, int]):
    """

    source_classic: Union[Unset, int] = UNSET
    source_ftcat: Union[Unset, int] = UNSET
    source_isearch: Union[Unset, int] = UNSET
    source_elasticsearch: Union[Unset, int] = UNSET
    flag_isearch_did_you_mean: Union[Unset, int] = UNSET
    flag_isearch_search_as_you_type: Union[Unset, int] = UNSET
    flag_isearch_summary: Union[Unset, int] = UNSET
    flag_isearch_company_thesaurus: Union[Unset, int] = UNSET
    flag_isearch_knowlege_map: Union[Unset, int] = UNSET
    flag_isearch_ontology_net: Union[Unset, int] = UNSET
    flag_isearch_elo_thesaurus: Union[Unset, int] = UNSET
    flag_isearch_optionsoff: Union[Unset, int] = UNSET
    flag_isearch_feed: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_classic = self.source_classic
        source_ftcat = self.source_ftcat
        source_isearch = self.source_isearch
        source_elasticsearch = self.source_elasticsearch
        flag_isearch_did_you_mean = self.flag_isearch_did_you_mean
        flag_isearch_search_as_you_type = self.flag_isearch_search_as_you_type
        flag_isearch_summary = self.flag_isearch_summary
        flag_isearch_company_thesaurus = self.flag_isearch_company_thesaurus
        flag_isearch_knowlege_map = self.flag_isearch_knowlege_map
        flag_isearch_ontology_net = self.flag_isearch_ontology_net
        flag_isearch_elo_thesaurus = self.flag_isearch_elo_thesaurus
        flag_isearch_optionsoff = self.flag_isearch_optionsoff
        flag_isearch_feed = self.flag_isearch_feed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_classic is not UNSET:
            field_dict["SOURCE_CLASSIC"] = source_classic
        if source_ftcat is not UNSET:
            field_dict["SOURCE_FTCAT"] = source_ftcat
        if source_isearch is not UNSET:
            field_dict["SOURCE_ISEARCH"] = source_isearch
        if source_elasticsearch is not UNSET:
            field_dict["SOURCE_ELASTICSEARCH"] = source_elasticsearch
        if flag_isearch_did_you_mean is not UNSET:
            field_dict["FLAG_ISEARCH_DID_YOU_MEAN"] = flag_isearch_did_you_mean
        if flag_isearch_search_as_you_type is not UNSET:
            field_dict["FLAG_ISEARCH_SEARCH_AS_YOU_TYPE"] = flag_isearch_search_as_you_type
        if flag_isearch_summary is not UNSET:
            field_dict["FLAG_ISEARCH_SUMMARY"] = flag_isearch_summary
        if flag_isearch_company_thesaurus is not UNSET:
            field_dict["FLAG_ISEARCH_COMPANY_THESAURUS"] = flag_isearch_company_thesaurus
        if flag_isearch_knowlege_map is not UNSET:
            field_dict["FLAG_ISEARCH_KNOWLEGE_MAP"] = flag_isearch_knowlege_map
        if flag_isearch_ontology_net is not UNSET:
            field_dict["FLAG_ISEARCH_ONTOLOGY_NET"] = flag_isearch_ontology_net
        if flag_isearch_elo_thesaurus is not UNSET:
            field_dict["FLAG_ISEARCH_ELO_THESAURUS"] = flag_isearch_elo_thesaurus
        if flag_isearch_optionsoff is not UNSET:
            field_dict["FLAG_ISEARCH_OPTIONSOFF"] = flag_isearch_optionsoff
        if flag_isearch_feed is not UNSET:
            field_dict["FLAG_ISEARCH_FEED"] = flag_isearch_feed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_classic = d.pop("SOURCE_CLASSIC", UNSET)

        source_ftcat = d.pop("SOURCE_FTCAT", UNSET)

        source_isearch = d.pop("SOURCE_ISEARCH", UNSET)

        source_elasticsearch = d.pop("SOURCE_ELASTICSEARCH", UNSET)

        flag_isearch_did_you_mean = d.pop("FLAG_ISEARCH_DID_YOU_MEAN", UNSET)

        flag_isearch_search_as_you_type = d.pop("FLAG_ISEARCH_SEARCH_AS_YOU_TYPE", UNSET)

        flag_isearch_summary = d.pop("FLAG_ISEARCH_SUMMARY", UNSET)

        flag_isearch_company_thesaurus = d.pop("FLAG_ISEARCH_COMPANY_THESAURUS", UNSET)

        flag_isearch_knowlege_map = d.pop("FLAG_ISEARCH_KNOWLEGE_MAP", UNSET)

        flag_isearch_ontology_net = d.pop("FLAG_ISEARCH_ONTOLOGY_NET", UNSET)

        flag_isearch_elo_thesaurus = d.pop("FLAG_ISEARCH_ELO_THESAURUS", UNSET)

        flag_isearch_optionsoff = d.pop("FLAG_ISEARCH_OPTIONSOFF", UNSET)

        flag_isearch_feed = d.pop("FLAG_ISEARCH_FEED", UNSET)

        fulltext_config_c = cls(
            source_classic=source_classic,
            source_ftcat=source_ftcat,
            source_isearch=source_isearch,
            source_elasticsearch=source_elasticsearch,
            flag_isearch_did_you_mean=flag_isearch_did_you_mean,
            flag_isearch_search_as_you_type=flag_isearch_search_as_you_type,
            flag_isearch_summary=flag_isearch_summary,
            flag_isearch_company_thesaurus=flag_isearch_company_thesaurus,
            flag_isearch_knowlege_map=flag_isearch_knowlege_map,
            flag_isearch_ontology_net=flag_isearch_ontology_net,
            flag_isearch_elo_thesaurus=flag_isearch_elo_thesaurus,
            flag_isearch_optionsoff=flag_isearch_optionsoff,
            flag_isearch_feed=flag_isearch_feed,
        )

        fulltext_config_c.additional_properties = d
        return fulltext_config_c

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
