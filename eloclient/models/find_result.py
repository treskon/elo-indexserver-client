from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.config_file import ConfigFile
    from ..models.context_term_results import ContextTermResults
    from ..models.find_by_fulltext_ctrl_result_item import FindByFulltextCtrlResultItem
    from ..models.find_by_fulltext_result_item import FindByFulltextResultItem
    from ..models.hash_tag_relation import HashTagRelation
    from ..models.job_state import JobState
    from ..models.map_to_aggregation_result import MapToAggregationResult
    from ..models.map_to_doc_mask import MapToDocMask
    from ..models.map_to_feed import MapToFeed
    from ..models.map_to_hash_tag import MapToHashTag
    from ..models.map_to_notification import MapToNotification
    from ..models.map_to_subscription import MapToSubscription
    from ..models.map_to_user_info import MapToUserInfo
    from ..models.map_to_user_name import MapToUserName
    from ..models.note import Note
    from ..models.report_info import ReportInfo
    from ..models.sord import Sord
    from ..models.translate_term import TranslateTerm
    from ..models.user_task import UserTask
    from ..models.value_class import ValueClass
    from ..models.wf_diagram import WFDiagram


T = TypeVar("T", bound="FindResult")


@_attrs_define
class FindResult:
    """<p>
    This class contains the search results of a call to <code>IXServicePortIF.findFirstSords</code>
     </p>
     or <code>IXServicePortIF.findNextSords</code>.
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            subscriptions (Union[Unset, MapToSubscription]):
            notes (Union[Unset, List['Note']]):
            dynamic_folder (Union[Unset, str]): String representation of FindInfo used to define a dynamic register.
                Function
                 {@link IXServicePortIF#findFirstSords(ClientInfo, FindInfo, int, SordZ)} returns a serialized
                 FindInfo in this member. It can be used to define a dynamic register by setting
                 <code>Sord.desc=FindResult.dynamicFolder</code>.
            workflows (Union[Unset, List['WFDiagram']]):
            more_results (Union[Unset, bool]): Is true if there are more results.
            fulltext_ctrl_result_items (Union[Unset, List['FindByFulltextCtrlResultItem']]):
            translate_terms (Union[Unset, List['TranslateTerm']]):
            fulltext_result_items (Union[Unset, List['FindByFulltextResultItem']]):
            job_states (Union[Unset, List['JobState']]):
            hash_tags (Union[Unset, MapToHashTag]):
            search_id (Union[Unset, str]): Identifier to get more results.
            hash_tag_relations (Union[Unset, List['HashTagRelation']]):
            feeds (Union[Unset, MapToFeed]):
            sorted_result (Union[Unset, List['ValueClass']]):
            break_total_count (Union[Unset, bool]): The search is breaked because the total number of results are reached.
            tasks (Union[Unset, List['UserTask']]):
            break_timeout (Union[Unset, bool]): The time limit for the search is exceeded.
            report_infos (Union[Unset, List['ReportInfo']]):
            synonyms (Union[Unset, List[str]]):
            count (Union[Unset, int]): Number of results. This member is only valid, if FindInfo.findOptions.evalCount is
                true.
            context_terms (Union[Unset, List['ContextTermResults']]):
            completions (Union[Unset, List[str]]):
            masks (Union[Unset, MapToDocMask]):
            sords (Union[Unset, List['Sord']]):
            estimated_count (Union[Unset, int]): Estimated number of hits that can be found by the query.
                This number cannot be computed for any
                 search and is usually -1. Only if the search engine supplies an estimated count, it is &gt;= 0.
            config_files (Union[Unset, List['ConfigFile']]):
            corrections (Union[Unset, List[str]]):
            ids (Union[Unset, List[str]]):
            user_infos (Union[Unset, MapToUserInfo]):
            user_names (Union[Unset, MapToUserName]):
            actions (Union[Unset, List['Action']]):
            aggregations (Union[Unset, MapToAggregationResult]):
            notifications (Union[Unset, MapToNotification]):
    """

    subscriptions: Union[Unset, "MapToSubscription"] = UNSET
    notes: Union[Unset, List["Note"]] = UNSET
    dynamic_folder: Union[Unset, str] = UNSET
    workflows: Union[Unset, List["WFDiagram"]] = UNSET
    more_results: Union[Unset, bool] = UNSET
    fulltext_ctrl_result_items: Union[Unset, List["FindByFulltextCtrlResultItem"]] = UNSET
    translate_terms: Union[Unset, List["TranslateTerm"]] = UNSET
    fulltext_result_items: Union[Unset, List["FindByFulltextResultItem"]] = UNSET
    job_states: Union[Unset, List["JobState"]] = UNSET
    hash_tags: Union[Unset, "MapToHashTag"] = UNSET
    search_id: Union[Unset, str] = UNSET
    hash_tag_relations: Union[Unset, List["HashTagRelation"]] = UNSET
    feeds: Union[Unset, "MapToFeed"] = UNSET
    sorted_result: Union[Unset, List["ValueClass"]] = UNSET
    break_total_count: Union[Unset, bool] = UNSET
    tasks: Union[Unset, List["UserTask"]] = UNSET
    break_timeout: Union[Unset, bool] = UNSET
    report_infos: Union[Unset, List["ReportInfo"]] = UNSET
    synonyms: Union[Unset, List[str]] = UNSET
    count: Union[Unset, int] = UNSET
    context_terms: Union[Unset, List["ContextTermResults"]] = UNSET
    completions: Union[Unset, List[str]] = UNSET
    masks: Union[Unset, "MapToDocMask"] = UNSET
    sords: Union[Unset, List["Sord"]] = UNSET
    estimated_count: Union[Unset, int] = UNSET
    config_files: Union[Unset, List["ConfigFile"]] = UNSET
    corrections: Union[Unset, List[str]] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    user_infos: Union[Unset, "MapToUserInfo"] = UNSET
    user_names: Union[Unset, "MapToUserName"] = UNSET
    actions: Union[Unset, List["Action"]] = UNSET
    aggregations: Union[Unset, "MapToAggregationResult"] = UNSET
    notifications: Union[Unset, "MapToNotification"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for componentsschemas_list_of_note_item_data in self.notes:
                componentsschemas_list_of_note_item = componentsschemas_list_of_note_item_data.to_dict()
                notes.append(componentsschemas_list_of_note_item)

        dynamic_folder = self.dynamic_folder

        workflows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        more_results = self.more_results

        fulltext_ctrl_result_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulltext_ctrl_result_items, Unset):
            fulltext_ctrl_result_items = []
            for fulltext_ctrl_result_items_item_data in self.fulltext_ctrl_result_items:
                fulltext_ctrl_result_items_item = fulltext_ctrl_result_items_item_data.to_dict()
                fulltext_ctrl_result_items.append(fulltext_ctrl_result_items_item)

        translate_terms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translate_terms, Unset):
            translate_terms = []
            for translate_terms_item_data in self.translate_terms:
                translate_terms_item = translate_terms_item_data.to_dict()
                translate_terms.append(translate_terms_item)

        fulltext_result_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulltext_result_items, Unset):
            fulltext_result_items = []
            for fulltext_result_items_item_data in self.fulltext_result_items:
                fulltext_result_items_item = fulltext_result_items_item_data.to_dict()
                fulltext_result_items.append(fulltext_result_items_item)

        job_states: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_states, Unset):
            job_states = []
            for job_states_item_data in self.job_states:
                job_states_item = job_states_item_data.to_dict()
                job_states.append(job_states_item)

        hash_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hash_tags, Unset):
            hash_tags = self.hash_tags.to_dict()

        search_id = self.search_id

        hash_tag_relations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hash_tag_relations, Unset):
            hash_tag_relations = []
            for componentsschemas_list_of_hash_tag_relation_item_data in self.hash_tag_relations:
                componentsschemas_list_of_hash_tag_relation_item = (
                    componentsschemas_list_of_hash_tag_relation_item_data.to_dict()
                )
                hash_tag_relations.append(componentsschemas_list_of_hash_tag_relation_item)

        feeds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feeds, Unset):
            feeds = self.feeds.to_dict()

        sorted_result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorted_result, Unset):
            sorted_result = []
            for componentsschemas_list_of_value_class_item_data in self.sorted_result:
                componentsschemas_list_of_value_class_item = componentsschemas_list_of_value_class_item_data.to_dict()
                sorted_result.append(componentsschemas_list_of_value_class_item)

        break_total_count = self.break_total_count

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        break_timeout = self.break_timeout

        report_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_infos, Unset):
            report_infos = []
            for report_infos_item_data in self.report_infos:
                report_infos_item = report_infos_item_data.to_dict()
                report_infos.append(report_infos_item)

        synonyms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        count = self.count

        context_terms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.context_terms, Unset):
            context_terms = []
            for componentsschemas_list_of_context_term_results_item_data in self.context_terms:
                componentsschemas_list_of_context_term_results_item = (
                    componentsschemas_list_of_context_term_results_item_data.to_dict()
                )
                context_terms.append(componentsschemas_list_of_context_term_results_item)

        completions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.completions, Unset):
            completions = self.completions

        masks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.masks, Unset):
            masks = self.masks.to_dict()

        sords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sords, Unset):
            sords = []
            for sords_item_data in self.sords:
                sords_item = sords_item_data.to_dict()
                sords.append(sords_item)

        estimated_count = self.estimated_count

        config_files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.config_files, Unset):
            config_files = []
            for config_files_item_data in self.config_files:
                config_files_item = config_files_item_data.to_dict()
                config_files.append(config_files_item)

        corrections: Union[Unset, List[str]] = UNSET
        if not isinstance(self.corrections, Unset):
            corrections = self.corrections

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        user_infos: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_infos, Unset):
            user_infos = self.user_infos.to_dict()

        user_names: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_names, Unset):
            user_names = self.user_names.to_dict()

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        aggregations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregations, Unset):
            aggregations = self.aggregations.to_dict()

        notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if notes is not UNSET:
            field_dict["notes"] = notes
        if dynamic_folder is not UNSET:
            field_dict["dynamicFolder"] = dynamic_folder
        if workflows is not UNSET:
            field_dict["workflows"] = workflows
        if more_results is not UNSET:
            field_dict["moreResults"] = more_results
        if fulltext_ctrl_result_items is not UNSET:
            field_dict["fulltextCtrlResultItems"] = fulltext_ctrl_result_items
        if translate_terms is not UNSET:
            field_dict["translateTerms"] = translate_terms
        if fulltext_result_items is not UNSET:
            field_dict["fulltextResultItems"] = fulltext_result_items
        if job_states is not UNSET:
            field_dict["jobStates"] = job_states
        if hash_tags is not UNSET:
            field_dict["hashTags"] = hash_tags
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if hash_tag_relations is not UNSET:
            field_dict["hashTagRelations"] = hash_tag_relations
        if feeds is not UNSET:
            field_dict["feeds"] = feeds
        if sorted_result is not UNSET:
            field_dict["sortedResult"] = sorted_result
        if break_total_count is not UNSET:
            field_dict["breakTotalCount"] = break_total_count
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if break_timeout is not UNSET:
            field_dict["breakTimeout"] = break_timeout
        if report_infos is not UNSET:
            field_dict["reportInfos"] = report_infos
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if count is not UNSET:
            field_dict["count"] = count
        if context_terms is not UNSET:
            field_dict["contextTerms"] = context_terms
        if completions is not UNSET:
            field_dict["completions"] = completions
        if masks is not UNSET:
            field_dict["masks"] = masks
        if sords is not UNSET:
            field_dict["sords"] = sords
        if estimated_count is not UNSET:
            field_dict["estimatedCount"] = estimated_count
        if config_files is not UNSET:
            field_dict["configFiles"] = config_files
        if corrections is not UNSET:
            field_dict["corrections"] = corrections
        if ids is not UNSET:
            field_dict["ids"] = ids
        if user_infos is not UNSET:
            field_dict["userInfos"] = user_infos
        if user_names is not UNSET:
            field_dict["userNames"] = user_names
        if actions is not UNSET:
            field_dict["actions"] = actions
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action import Action
        from ..models.config_file import ConfigFile
        from ..models.context_term_results import ContextTermResults
        from ..models.find_by_fulltext_ctrl_result_item import FindByFulltextCtrlResultItem
        from ..models.find_by_fulltext_result_item import FindByFulltextResultItem
        from ..models.hash_tag_relation import HashTagRelation
        from ..models.job_state import JobState
        from ..models.map_to_aggregation_result import MapToAggregationResult
        from ..models.map_to_doc_mask import MapToDocMask
        from ..models.map_to_feed import MapToFeed
        from ..models.map_to_hash_tag import MapToHashTag
        from ..models.map_to_notification import MapToNotification
        from ..models.map_to_subscription import MapToSubscription
        from ..models.map_to_user_info import MapToUserInfo
        from ..models.map_to_user_name import MapToUserName
        from ..models.note import Note
        from ..models.report_info import ReportInfo
        from ..models.sord import Sord
        from ..models.translate_term import TranslateTerm
        from ..models.user_task import UserTask
        from ..models.value_class import ValueClass
        from ..models.wf_diagram import WFDiagram

        d = src_dict.copy()
        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: Union[Unset, MapToSubscription]
        if isinstance(_subscriptions, Unset):
            subscriptions = UNSET
        else:
            subscriptions = MapToSubscription.from_dict(_subscriptions)

        notes = []
        _notes = d.pop("notes", UNSET)
        for componentsschemas_list_of_note_item_data in _notes or []:
            componentsschemas_list_of_note_item = Note.from_dict(componentsschemas_list_of_note_item_data)

            notes.append(componentsschemas_list_of_note_item)

        dynamic_folder = d.pop("dynamicFolder", UNSET)

        workflows = []
        _workflows = d.pop("workflows", UNSET)
        for workflows_item_data in _workflows or []:
            workflows_item = WFDiagram.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        more_results = d.pop("moreResults", UNSET)

        fulltext_ctrl_result_items = []
        _fulltext_ctrl_result_items = d.pop("fulltextCtrlResultItems", UNSET)
        for fulltext_ctrl_result_items_item_data in _fulltext_ctrl_result_items or []:
            fulltext_ctrl_result_items_item = FindByFulltextCtrlResultItem.from_dict(
                fulltext_ctrl_result_items_item_data
            )

            fulltext_ctrl_result_items.append(fulltext_ctrl_result_items_item)

        translate_terms = []
        _translate_terms = d.pop("translateTerms", UNSET)
        for translate_terms_item_data in _translate_terms or []:
            translate_terms_item = TranslateTerm.from_dict(translate_terms_item_data)

            translate_terms.append(translate_terms_item)

        fulltext_result_items = []
        _fulltext_result_items = d.pop("fulltextResultItems", UNSET)
        for fulltext_result_items_item_data in _fulltext_result_items or []:
            fulltext_result_items_item = FindByFulltextResultItem.from_dict(fulltext_result_items_item_data)

            fulltext_result_items.append(fulltext_result_items_item)

        job_states = []
        _job_states = d.pop("jobStates", UNSET)
        for job_states_item_data in _job_states or []:
            job_states_item = JobState.from_dict(job_states_item_data)

            job_states.append(job_states_item)

        _hash_tags = d.pop("hashTags", UNSET)
        hash_tags: Union[Unset, MapToHashTag]
        if isinstance(_hash_tags, Unset):
            hash_tags = UNSET
        else:
            hash_tags = MapToHashTag.from_dict(_hash_tags)

        search_id = d.pop("searchId", UNSET)

        hash_tag_relations = []
        _hash_tag_relations = d.pop("hashTagRelations", UNSET)
        for componentsschemas_list_of_hash_tag_relation_item_data in _hash_tag_relations or []:
            componentsschemas_list_of_hash_tag_relation_item = HashTagRelation.from_dict(
                componentsschemas_list_of_hash_tag_relation_item_data
            )

            hash_tag_relations.append(componentsschemas_list_of_hash_tag_relation_item)

        _feeds = d.pop("feeds", UNSET)
        feeds: Union[Unset, MapToFeed]
        if isinstance(_feeds, Unset):
            feeds = UNSET
        else:
            feeds = MapToFeed.from_dict(_feeds)

        sorted_result = []
        _sorted_result = d.pop("sortedResult", UNSET)
        for componentsschemas_list_of_value_class_item_data in _sorted_result or []:
            componentsschemas_list_of_value_class_item = ValueClass.from_dict(
                componentsschemas_list_of_value_class_item_data
            )

            sorted_result.append(componentsschemas_list_of_value_class_item)

        break_total_count = d.pop("breakTotalCount", UNSET)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = UserTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        break_timeout = d.pop("breakTimeout", UNSET)

        report_infos = []
        _report_infos = d.pop("reportInfos", UNSET)
        for report_infos_item_data in _report_infos or []:
            report_infos_item = ReportInfo.from_dict(report_infos_item_data)

            report_infos.append(report_infos_item)

        synonyms = cast(List[str], d.pop("synonyms", UNSET))

        count = d.pop("count", UNSET)

        context_terms = []
        _context_terms = d.pop("contextTerms", UNSET)
        for componentsschemas_list_of_context_term_results_item_data in _context_terms or []:
            componentsschemas_list_of_context_term_results_item = ContextTermResults.from_dict(
                componentsschemas_list_of_context_term_results_item_data
            )

            context_terms.append(componentsschemas_list_of_context_term_results_item)

        completions = cast(List[str], d.pop("completions", UNSET))

        _masks = d.pop("masks", UNSET)
        masks: Union[Unset, MapToDocMask]
        if isinstance(_masks, Unset):
            masks = UNSET
        else:
            masks = MapToDocMask.from_dict(_masks)

        sords = []
        _sords = d.pop("sords", UNSET)
        for sords_item_data in _sords or []:
            sords_item = Sord.from_dict(sords_item_data)

            sords.append(sords_item)

        estimated_count = d.pop("estimatedCount", UNSET)

        config_files = []
        _config_files = d.pop("configFiles", UNSET)
        for config_files_item_data in _config_files or []:
            config_files_item = ConfigFile.from_dict(config_files_item_data)

            config_files.append(config_files_item)

        corrections = cast(List[str], d.pop("corrections", UNSET))

        ids = cast(List[str], d.pop("ids", UNSET))

        _user_infos = d.pop("userInfos", UNSET)
        user_infos: Union[Unset, MapToUserInfo]
        if isinstance(_user_infos, Unset):
            user_infos = UNSET
        else:
            user_infos = MapToUserInfo.from_dict(_user_infos)

        _user_names = d.pop("userNames", UNSET)
        user_names: Union[Unset, MapToUserName]
        if isinstance(_user_names, Unset):
            user_names = UNSET
        else:
            user_names = MapToUserName.from_dict(_user_names)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = Action.from_dict(actions_item_data)

            actions.append(actions_item)

        _aggregations = d.pop("aggregations", UNSET)
        aggregations: Union[Unset, MapToAggregationResult]
        if isinstance(_aggregations, Unset):
            aggregations = UNSET
        else:
            aggregations = MapToAggregationResult.from_dict(_aggregations)

        _notifications = d.pop("notifications", UNSET)
        notifications: Union[Unset, MapToNotification]
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = MapToNotification.from_dict(_notifications)

        find_result = cls(
            subscriptions=subscriptions,
            notes=notes,
            dynamic_folder=dynamic_folder,
            workflows=workflows,
            more_results=more_results,
            fulltext_ctrl_result_items=fulltext_ctrl_result_items,
            translate_terms=translate_terms,
            fulltext_result_items=fulltext_result_items,
            job_states=job_states,
            hash_tags=hash_tags,
            search_id=search_id,
            hash_tag_relations=hash_tag_relations,
            feeds=feeds,
            sorted_result=sorted_result,
            break_total_count=break_total_count,
            tasks=tasks,
            break_timeout=break_timeout,
            report_infos=report_infos,
            synonyms=synonyms,
            count=count,
            context_terms=context_terms,
            completions=completions,
            masks=masks,
            sords=sords,
            estimated_count=estimated_count,
            config_files=config_files,
            corrections=corrections,
            ids=ids,
            user_infos=user_infos,
            user_names=user_names,
            actions=actions,
            aggregations=aggregations,
            notifications=notifications,
        )

        find_result.additional_properties = d
        return find_result

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
