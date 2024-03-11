from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.es_settings_property import EsSettingsProperty


T = TypeVar("T", bound="ESInstanceSettings")


@_attrs_define
class ESInstanceSettings:
    """<p>
    Class to read and write settings of Elasticsearch.
     </p>

        Attributes:
            instance_name (Union[Unset, str]):
            indexing_disabled (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            updater_next_start (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            updater_from_ts (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            updater_interval (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            reindex_started (Union[Unset, str]): Reindex started at this time. Format: yyyyMMddHHmmss Timezone: JVM default.
            reindex_from_obj_id (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            reindex_to_obj_id (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            additional_index (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            nb_of_allowed_langs (Union[Unset, int]): Number of allowed languages.
                <p>
                 <i>Immutable.</i>
                 </p>
            configured_langs (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            archive_lang (Union[Unset, str]): Archive language.
                <p>
                 <i>Immutable.</i>
                 </p>
            max_objs_per_reindex_interval (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            max_objs_per_update_interval (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            continue_reindex_on_failure (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            correction (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            completion (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            synonyms (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            max_amount_of_references_in_error_folder (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            max_token_length (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            german_analyzer (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            search_analyzer (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            feed_analyzer (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            max_fulltext_length (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            number_of_shards (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            number_of_shards_by_mask_id (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            use_ssl (Union[Unset, bool]): Use SSL encryption.
            cluster_name (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            node_name (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            index_name (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            hosts (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            allow_leading_wildcards (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            max_search_results (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
            skip_non_ascii_steps_on_fallback (Union[Unset, EsSettingsProperty]): Properties of ESInstanceSettings
    """

    instance_name: Union[Unset, str] = UNSET
    indexing_disabled: Union[Unset, "EsSettingsProperty"] = UNSET
    updater_next_start: Union[Unset, "EsSettingsProperty"] = UNSET
    updater_from_ts: Union[Unset, "EsSettingsProperty"] = UNSET
    updater_interval: Union[Unset, "EsSettingsProperty"] = UNSET
    reindex_started: Union[Unset, str] = UNSET
    reindex_from_obj_id: Union[Unset, "EsSettingsProperty"] = UNSET
    reindex_to_obj_id: Union[Unset, "EsSettingsProperty"] = UNSET
    additional_index: Union[Unset, "EsSettingsProperty"] = UNSET
    nb_of_allowed_langs: Union[Unset, int] = UNSET
    configured_langs: Union[Unset, "EsSettingsProperty"] = UNSET
    archive_lang: Union[Unset, str] = UNSET
    max_objs_per_reindex_interval: Union[Unset, "EsSettingsProperty"] = UNSET
    max_objs_per_update_interval: Union[Unset, "EsSettingsProperty"] = UNSET
    continue_reindex_on_failure: Union[Unset, "EsSettingsProperty"] = UNSET
    correction: Union[Unset, "EsSettingsProperty"] = UNSET
    completion: Union[Unset, "EsSettingsProperty"] = UNSET
    synonyms: Union[Unset, "EsSettingsProperty"] = UNSET
    max_amount_of_references_in_error_folder: Union[Unset, "EsSettingsProperty"] = UNSET
    max_token_length: Union[Unset, "EsSettingsProperty"] = UNSET
    german_analyzer: Union[Unset, "EsSettingsProperty"] = UNSET
    search_analyzer: Union[Unset, "EsSettingsProperty"] = UNSET
    feed_analyzer: Union[Unset, "EsSettingsProperty"] = UNSET
    max_fulltext_length: Union[Unset, "EsSettingsProperty"] = UNSET
    number_of_shards: Union[Unset, "EsSettingsProperty"] = UNSET
    number_of_shards_by_mask_id: Union[Unset, "EsSettingsProperty"] = UNSET
    use_ssl: Union[Unset, bool] = UNSET
    cluster_name: Union[Unset, "EsSettingsProperty"] = UNSET
    node_name: Union[Unset, "EsSettingsProperty"] = UNSET
    index_name: Union[Unset, "EsSettingsProperty"] = UNSET
    hosts: Union[Unset, "EsSettingsProperty"] = UNSET
    allow_leading_wildcards: Union[Unset, "EsSettingsProperty"] = UNSET
    max_search_results: Union[Unset, "EsSettingsProperty"] = UNSET
    skip_non_ascii_steps_on_fallback: Union[Unset, "EsSettingsProperty"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instance_name = self.instance_name
        indexing_disabled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indexing_disabled, Unset):
            indexing_disabled = self.indexing_disabled.to_dict()

        updater_next_start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updater_next_start, Unset):
            updater_next_start = self.updater_next_start.to_dict()

        updater_from_ts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updater_from_ts, Unset):
            updater_from_ts = self.updater_from_ts.to_dict()

        updater_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updater_interval, Unset):
            updater_interval = self.updater_interval.to_dict()

        reindex_started = self.reindex_started
        reindex_from_obj_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reindex_from_obj_id, Unset):
            reindex_from_obj_id = self.reindex_from_obj_id.to_dict()

        reindex_to_obj_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reindex_to_obj_id, Unset):
            reindex_to_obj_id = self.reindex_to_obj_id.to_dict()

        additional_index: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_index, Unset):
            additional_index = self.additional_index.to_dict()

        nb_of_allowed_langs = self.nb_of_allowed_langs
        configured_langs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configured_langs, Unset):
            configured_langs = self.configured_langs.to_dict()

        archive_lang = self.archive_lang
        max_objs_per_reindex_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_objs_per_reindex_interval, Unset):
            max_objs_per_reindex_interval = self.max_objs_per_reindex_interval.to_dict()

        max_objs_per_update_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_objs_per_update_interval, Unset):
            max_objs_per_update_interval = self.max_objs_per_update_interval.to_dict()

        continue_reindex_on_failure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.continue_reindex_on_failure, Unset):
            continue_reindex_on_failure = self.continue_reindex_on_failure.to_dict()

        correction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.correction, Unset):
            correction = self.correction.to_dict()

        completion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.completion, Unset):
            completion = self.completion.to_dict()

        synonyms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms.to_dict()

        max_amount_of_references_in_error_folder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_amount_of_references_in_error_folder, Unset):
            max_amount_of_references_in_error_folder = self.max_amount_of_references_in_error_folder.to_dict()

        max_token_length: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_token_length, Unset):
            max_token_length = self.max_token_length.to_dict()

        german_analyzer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.german_analyzer, Unset):
            german_analyzer = self.german_analyzer.to_dict()

        search_analyzer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_analyzer, Unset):
            search_analyzer = self.search_analyzer.to_dict()

        feed_analyzer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_analyzer, Unset):
            feed_analyzer = self.feed_analyzer.to_dict()

        max_fulltext_length: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_fulltext_length, Unset):
            max_fulltext_length = self.max_fulltext_length.to_dict()

        number_of_shards: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.number_of_shards, Unset):
            number_of_shards = self.number_of_shards.to_dict()

        number_of_shards_by_mask_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.number_of_shards_by_mask_id, Unset):
            number_of_shards_by_mask_id = self.number_of_shards_by_mask_id.to_dict()

        use_ssl = self.use_ssl
        cluster_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_name, Unset):
            cluster_name = self.cluster_name.to_dict()

        node_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node_name, Unset):
            node_name = self.node_name.to_dict()

        index_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.index_name, Unset):
            index_name = self.index_name.to_dict()

        hosts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts.to_dict()

        allow_leading_wildcards: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allow_leading_wildcards, Unset):
            allow_leading_wildcards = self.allow_leading_wildcards.to_dict()

        max_search_results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_search_results, Unset):
            max_search_results = self.max_search_results.to_dict()

        skip_non_ascii_steps_on_fallback: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skip_non_ascii_steps_on_fallback, Unset):
            skip_non_ascii_steps_on_fallback = self.skip_non_ascii_steps_on_fallback.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if indexing_disabled is not UNSET:
            field_dict["indexingDisabled"] = indexing_disabled
        if updater_next_start is not UNSET:
            field_dict["updaterNextStart"] = updater_next_start
        if updater_from_ts is not UNSET:
            field_dict["updaterFromTs"] = updater_from_ts
        if updater_interval is not UNSET:
            field_dict["updaterInterval"] = updater_interval
        if reindex_started is not UNSET:
            field_dict["reindexStarted"] = reindex_started
        if reindex_from_obj_id is not UNSET:
            field_dict["reindexFromObjId"] = reindex_from_obj_id
        if reindex_to_obj_id is not UNSET:
            field_dict["reindexToObjId"] = reindex_to_obj_id
        if additional_index is not UNSET:
            field_dict["additionalIndex"] = additional_index
        if nb_of_allowed_langs is not UNSET:
            field_dict["nbOfAllowedLangs"] = nb_of_allowed_langs
        if configured_langs is not UNSET:
            field_dict["configuredLangs"] = configured_langs
        if archive_lang is not UNSET:
            field_dict["archiveLang"] = archive_lang
        if max_objs_per_reindex_interval is not UNSET:
            field_dict["maxObjsPerReindexInterval"] = max_objs_per_reindex_interval
        if max_objs_per_update_interval is not UNSET:
            field_dict["maxObjsPerUpdateInterval"] = max_objs_per_update_interval
        if continue_reindex_on_failure is not UNSET:
            field_dict["continueReindexOnFailure"] = continue_reindex_on_failure
        if correction is not UNSET:
            field_dict["correction"] = correction
        if completion is not UNSET:
            field_dict["completion"] = completion
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if max_amount_of_references_in_error_folder is not UNSET:
            field_dict["maxAmountOfReferencesInErrorFolder"] = max_amount_of_references_in_error_folder
        if max_token_length is not UNSET:
            field_dict["maxTokenLength"] = max_token_length
        if german_analyzer is not UNSET:
            field_dict["germanAnalyzer"] = german_analyzer
        if search_analyzer is not UNSET:
            field_dict["searchAnalyzer"] = search_analyzer
        if feed_analyzer is not UNSET:
            field_dict["feedAnalyzer"] = feed_analyzer
        if max_fulltext_length is not UNSET:
            field_dict["maxFulltextLength"] = max_fulltext_length
        if number_of_shards is not UNSET:
            field_dict["numberOfShards"] = number_of_shards
        if number_of_shards_by_mask_id is not UNSET:
            field_dict["numberOfShardsByMaskId"] = number_of_shards_by_mask_id
        if use_ssl is not UNSET:
            field_dict["useSsl"] = use_ssl
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if index_name is not UNSET:
            field_dict["indexName"] = index_name
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if allow_leading_wildcards is not UNSET:
            field_dict["allowLeadingWildcards"] = allow_leading_wildcards
        if max_search_results is not UNSET:
            field_dict["maxSearchResults"] = max_search_results
        if skip_non_ascii_steps_on_fallback is not UNSET:
            field_dict["skipNonAsciiStepsOnFallback"] = skip_non_ascii_steps_on_fallback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.es_settings_property import EsSettingsProperty

        d = src_dict.copy()
        instance_name = d.pop("instanceName", UNSET)

        _indexing_disabled = d.pop("indexingDisabled", UNSET)
        indexing_disabled: Union[Unset, EsSettingsProperty]
        if isinstance(_indexing_disabled, Unset):
            indexing_disabled = UNSET
        else:
            indexing_disabled = EsSettingsProperty.from_dict(_indexing_disabled)

        _updater_next_start = d.pop("updaterNextStart", UNSET)
        updater_next_start: Union[Unset, EsSettingsProperty]
        if isinstance(_updater_next_start, Unset):
            updater_next_start = UNSET
        else:
            updater_next_start = EsSettingsProperty.from_dict(_updater_next_start)

        _updater_from_ts = d.pop("updaterFromTs", UNSET)
        updater_from_ts: Union[Unset, EsSettingsProperty]
        if isinstance(_updater_from_ts, Unset):
            updater_from_ts = UNSET
        else:
            updater_from_ts = EsSettingsProperty.from_dict(_updater_from_ts)

        _updater_interval = d.pop("updaterInterval", UNSET)
        updater_interval: Union[Unset, EsSettingsProperty]
        if isinstance(_updater_interval, Unset):
            updater_interval = UNSET
        else:
            updater_interval = EsSettingsProperty.from_dict(_updater_interval)

        reindex_started = d.pop("reindexStarted", UNSET)

        _reindex_from_obj_id = d.pop("reindexFromObjId", UNSET)
        reindex_from_obj_id: Union[Unset, EsSettingsProperty]
        if isinstance(_reindex_from_obj_id, Unset):
            reindex_from_obj_id = UNSET
        else:
            reindex_from_obj_id = EsSettingsProperty.from_dict(_reindex_from_obj_id)

        _reindex_to_obj_id = d.pop("reindexToObjId", UNSET)
        reindex_to_obj_id: Union[Unset, EsSettingsProperty]
        if isinstance(_reindex_to_obj_id, Unset):
            reindex_to_obj_id = UNSET
        else:
            reindex_to_obj_id = EsSettingsProperty.from_dict(_reindex_to_obj_id)

        _additional_index = d.pop("additionalIndex", UNSET)
        additional_index: Union[Unset, EsSettingsProperty]
        if isinstance(_additional_index, Unset):
            additional_index = UNSET
        else:
            additional_index = EsSettingsProperty.from_dict(_additional_index)

        nb_of_allowed_langs = d.pop("nbOfAllowedLangs", UNSET)

        _configured_langs = d.pop("configuredLangs", UNSET)
        configured_langs: Union[Unset, EsSettingsProperty]
        if isinstance(_configured_langs, Unset):
            configured_langs = UNSET
        else:
            configured_langs = EsSettingsProperty.from_dict(_configured_langs)

        archive_lang = d.pop("archiveLang", UNSET)

        _max_objs_per_reindex_interval = d.pop("maxObjsPerReindexInterval", UNSET)
        max_objs_per_reindex_interval: Union[Unset, EsSettingsProperty]
        if isinstance(_max_objs_per_reindex_interval, Unset):
            max_objs_per_reindex_interval = UNSET
        else:
            max_objs_per_reindex_interval = EsSettingsProperty.from_dict(_max_objs_per_reindex_interval)

        _max_objs_per_update_interval = d.pop("maxObjsPerUpdateInterval", UNSET)
        max_objs_per_update_interval: Union[Unset, EsSettingsProperty]
        if isinstance(_max_objs_per_update_interval, Unset):
            max_objs_per_update_interval = UNSET
        else:
            max_objs_per_update_interval = EsSettingsProperty.from_dict(_max_objs_per_update_interval)

        _continue_reindex_on_failure = d.pop("continueReindexOnFailure", UNSET)
        continue_reindex_on_failure: Union[Unset, EsSettingsProperty]
        if isinstance(_continue_reindex_on_failure, Unset):
            continue_reindex_on_failure = UNSET
        else:
            continue_reindex_on_failure = EsSettingsProperty.from_dict(_continue_reindex_on_failure)

        _correction = d.pop("correction", UNSET)
        correction: Union[Unset, EsSettingsProperty]
        if isinstance(_correction, Unset):
            correction = UNSET
        else:
            correction = EsSettingsProperty.from_dict(_correction)

        _completion = d.pop("completion", UNSET)
        completion: Union[Unset, EsSettingsProperty]
        if isinstance(_completion, Unset):
            completion = UNSET
        else:
            completion = EsSettingsProperty.from_dict(_completion)

        _synonyms = d.pop("synonyms", UNSET)
        synonyms: Union[Unset, EsSettingsProperty]
        if isinstance(_synonyms, Unset):
            synonyms = UNSET
        else:
            synonyms = EsSettingsProperty.from_dict(_synonyms)

        _max_amount_of_references_in_error_folder = d.pop("maxAmountOfReferencesInErrorFolder", UNSET)
        max_amount_of_references_in_error_folder: Union[Unset, EsSettingsProperty]
        if isinstance(_max_amount_of_references_in_error_folder, Unset):
            max_amount_of_references_in_error_folder = UNSET
        else:
            max_amount_of_references_in_error_folder = EsSettingsProperty.from_dict(
                _max_amount_of_references_in_error_folder
            )

        _max_token_length = d.pop("maxTokenLength", UNSET)
        max_token_length: Union[Unset, EsSettingsProperty]
        if isinstance(_max_token_length, Unset):
            max_token_length = UNSET
        else:
            max_token_length = EsSettingsProperty.from_dict(_max_token_length)

        _german_analyzer = d.pop("germanAnalyzer", UNSET)
        german_analyzer: Union[Unset, EsSettingsProperty]
        if isinstance(_german_analyzer, Unset):
            german_analyzer = UNSET
        else:
            german_analyzer = EsSettingsProperty.from_dict(_german_analyzer)

        _search_analyzer = d.pop("searchAnalyzer", UNSET)
        search_analyzer: Union[Unset, EsSettingsProperty]
        if isinstance(_search_analyzer, Unset):
            search_analyzer = UNSET
        else:
            search_analyzer = EsSettingsProperty.from_dict(_search_analyzer)

        _feed_analyzer = d.pop("feedAnalyzer", UNSET)
        feed_analyzer: Union[Unset, EsSettingsProperty]
        if isinstance(_feed_analyzer, Unset):
            feed_analyzer = UNSET
        else:
            feed_analyzer = EsSettingsProperty.from_dict(_feed_analyzer)

        _max_fulltext_length = d.pop("maxFulltextLength", UNSET)
        max_fulltext_length: Union[Unset, EsSettingsProperty]
        if isinstance(_max_fulltext_length, Unset):
            max_fulltext_length = UNSET
        else:
            max_fulltext_length = EsSettingsProperty.from_dict(_max_fulltext_length)

        _number_of_shards = d.pop("numberOfShards", UNSET)
        number_of_shards: Union[Unset, EsSettingsProperty]
        if isinstance(_number_of_shards, Unset):
            number_of_shards = UNSET
        else:
            number_of_shards = EsSettingsProperty.from_dict(_number_of_shards)

        _number_of_shards_by_mask_id = d.pop("numberOfShardsByMaskId", UNSET)
        number_of_shards_by_mask_id: Union[Unset, EsSettingsProperty]
        if isinstance(_number_of_shards_by_mask_id, Unset):
            number_of_shards_by_mask_id = UNSET
        else:
            number_of_shards_by_mask_id = EsSettingsProperty.from_dict(_number_of_shards_by_mask_id)

        use_ssl = d.pop("useSsl", UNSET)

        _cluster_name = d.pop("clusterName", UNSET)
        cluster_name: Union[Unset, EsSettingsProperty]
        if isinstance(_cluster_name, Unset):
            cluster_name = UNSET
        else:
            cluster_name = EsSettingsProperty.from_dict(_cluster_name)

        _node_name = d.pop("nodeName", UNSET)
        node_name: Union[Unset, EsSettingsProperty]
        if isinstance(_node_name, Unset):
            node_name = UNSET
        else:
            node_name = EsSettingsProperty.from_dict(_node_name)

        _index_name = d.pop("indexName", UNSET)
        index_name: Union[Unset, EsSettingsProperty]
        if isinstance(_index_name, Unset):
            index_name = UNSET
        else:
            index_name = EsSettingsProperty.from_dict(_index_name)

        _hosts = d.pop("hosts", UNSET)
        hosts: Union[Unset, EsSettingsProperty]
        if isinstance(_hosts, Unset):
            hosts = UNSET
        else:
            hosts = EsSettingsProperty.from_dict(_hosts)

        _allow_leading_wildcards = d.pop("allowLeadingWildcards", UNSET)
        allow_leading_wildcards: Union[Unset, EsSettingsProperty]
        if isinstance(_allow_leading_wildcards, Unset):
            allow_leading_wildcards = UNSET
        else:
            allow_leading_wildcards = EsSettingsProperty.from_dict(_allow_leading_wildcards)

        _max_search_results = d.pop("maxSearchResults", UNSET)
        max_search_results: Union[Unset, EsSettingsProperty]
        if isinstance(_max_search_results, Unset):
            max_search_results = UNSET
        else:
            max_search_results = EsSettingsProperty.from_dict(_max_search_results)

        _skip_non_ascii_steps_on_fallback = d.pop("skipNonAsciiStepsOnFallback", UNSET)
        skip_non_ascii_steps_on_fallback: Union[Unset, EsSettingsProperty]
        if isinstance(_skip_non_ascii_steps_on_fallback, Unset):
            skip_non_ascii_steps_on_fallback = UNSET
        else:
            skip_non_ascii_steps_on_fallback = EsSettingsProperty.from_dict(_skip_non_ascii_steps_on_fallback)

        es_instance_settings = cls(
            instance_name=instance_name,
            indexing_disabled=indexing_disabled,
            updater_next_start=updater_next_start,
            updater_from_ts=updater_from_ts,
            updater_interval=updater_interval,
            reindex_started=reindex_started,
            reindex_from_obj_id=reindex_from_obj_id,
            reindex_to_obj_id=reindex_to_obj_id,
            additional_index=additional_index,
            nb_of_allowed_langs=nb_of_allowed_langs,
            configured_langs=configured_langs,
            archive_lang=archive_lang,
            max_objs_per_reindex_interval=max_objs_per_reindex_interval,
            max_objs_per_update_interval=max_objs_per_update_interval,
            continue_reindex_on_failure=continue_reindex_on_failure,
            correction=correction,
            completion=completion,
            synonyms=synonyms,
            max_amount_of_references_in_error_folder=max_amount_of_references_in_error_folder,
            max_token_length=max_token_length,
            german_analyzer=german_analyzer,
            search_analyzer=search_analyzer,
            feed_analyzer=feed_analyzer,
            max_fulltext_length=max_fulltext_length,
            number_of_shards=number_of_shards,
            number_of_shards_by_mask_id=number_of_shards_by_mask_id,
            use_ssl=use_ssl,
            cluster_name=cluster_name,
            node_name=node_name,
            index_name=index_name,
            hosts=hosts,
            allow_leading_wildcards=allow_leading_wildcards,
            max_search_results=max_search_results,
            skip_non_ascii_steps_on_fallback=skip_non_ascii_steps_on_fallback,
        )

        es_instance_settings.additional_properties = d
        return es_instance_settings

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
