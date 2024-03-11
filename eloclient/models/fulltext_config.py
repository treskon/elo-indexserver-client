from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_indexer_config import SearchIndexerConfig


T = TypeVar("T", bound="FulltextConfig")


@_attrs_define
class FulltextConfig:
    """This class provides information about the configuration of the fulltext database.

    Attributes:
        source (Union[Unset, int]): One of the FulltextConfigC.SOURCE_* constants.
        flags (Union[Unset, int]): A combination of FulltextConfigC.FLAG_* constants.
        knowlege_map_url (Union[Unset, str]): URL of the Knowlege Map service. Only valid for iSearch.
        indexer_config (Union[Unset, SearchIndexerConfig]):
    """

    source: Union[Unset, int] = UNSET
    flags: Union[Unset, int] = UNSET
    knowlege_map_url: Union[Unset, str] = UNSET
    indexer_config: Union[Unset, "SearchIndexerConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        flags = self.flags
        knowlege_map_url = self.knowlege_map_url
        indexer_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indexer_config, Unset):
            indexer_config = self.indexer_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if flags is not UNSET:
            field_dict["flags"] = flags
        if knowlege_map_url is not UNSET:
            field_dict["knowlegeMapUrl"] = knowlege_map_url
        if indexer_config is not UNSET:
            field_dict["indexerConfig"] = indexer_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_indexer_config import SearchIndexerConfig

        d = src_dict.copy()
        source = d.pop("source", UNSET)

        flags = d.pop("flags", UNSET)

        knowlege_map_url = d.pop("knowlegeMapUrl", UNSET)

        _indexer_config = d.pop("indexerConfig", UNSET)
        indexer_config: Union[Unset, SearchIndexerConfig]
        if isinstance(_indexer_config, Unset):
            indexer_config = UNSET
        else:
            indexer_config = SearchIndexerConfig.from_dict(_indexer_config)

        fulltext_config = cls(
            source=source,
            flags=flags,
            knowlege_map_url=knowlege_map_url,
            indexer_config=indexer_config,
        )

        fulltext_config.additional_properties = d
        return fulltext_config

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
