from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language_config import LanguageConfig
    from ..models.optimizer_config import OptimizerConfig
    from ..models.reindexer_config import ReindexerConfig
    from ..models.updater_config import UpdaterConfig


T = TypeVar("T", bound="SearchIndexerConfig")


@_attrs_define
class SearchIndexerConfig:
    """
    Attributes:
        optimizer_config (Union[Unset, OptimizerConfig]): Configuration and status of optimizer process.
        reindexer_config (Union[Unset, ReindexerConfig]): Configuration and status of Re-indexer process.
        language_config (Union[Unset, LanguageConfig]):
        updater_config (Union[Unset, UpdaterConfig]): Configuration and status of updater process.
    """

    optimizer_config: Union[Unset, "OptimizerConfig"] = UNSET
    reindexer_config: Union[Unset, "ReindexerConfig"] = UNSET
    language_config: Union[Unset, "LanguageConfig"] = UNSET
    updater_config: Union[Unset, "UpdaterConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        optimizer_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.optimizer_config, Unset):
            optimizer_config = self.optimizer_config.to_dict()

        reindexer_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reindexer_config, Unset):
            reindexer_config = self.reindexer_config.to_dict()

        language_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.language_config, Unset):
            language_config = self.language_config.to_dict()

        updater_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updater_config, Unset):
            updater_config = self.updater_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if optimizer_config is not UNSET:
            field_dict["optimizerConfig"] = optimizer_config
        if reindexer_config is not UNSET:
            field_dict["reindexerConfig"] = reindexer_config
        if language_config is not UNSET:
            field_dict["languageConfig"] = language_config
        if updater_config is not UNSET:
            field_dict["updaterConfig"] = updater_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_config import LanguageConfig
        from ..models.optimizer_config import OptimizerConfig
        from ..models.reindexer_config import ReindexerConfig
        from ..models.updater_config import UpdaterConfig

        d = src_dict.copy()
        _optimizer_config = d.pop("optimizerConfig", UNSET)
        optimizer_config: Union[Unset, OptimizerConfig]
        if isinstance(_optimizer_config, Unset):
            optimizer_config = UNSET
        else:
            optimizer_config = OptimizerConfig.from_dict(_optimizer_config)

        _reindexer_config = d.pop("reindexerConfig", UNSET)
        reindexer_config: Union[Unset, ReindexerConfig]
        if isinstance(_reindexer_config, Unset):
            reindexer_config = UNSET
        else:
            reindexer_config = ReindexerConfig.from_dict(_reindexer_config)

        _language_config = d.pop("languageConfig", UNSET)
        language_config: Union[Unset, LanguageConfig]
        if isinstance(_language_config, Unset):
            language_config = UNSET
        else:
            language_config = LanguageConfig.from_dict(_language_config)

        _updater_config = d.pop("updaterConfig", UNSET)
        updater_config: Union[Unset, UpdaterConfig]
        if isinstance(_updater_config, Unset):
            updater_config = UNSET
        else:
            updater_config = UpdaterConfig.from_dict(_updater_config)

        search_indexer_config = cls(
            optimizer_config=optimizer_config,
            reindexer_config=reindexer_config,
            language_config=language_config,
            updater_config=updater_config,
        )

        search_indexer_config.additional_properties = d
        return search_indexer_config

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
