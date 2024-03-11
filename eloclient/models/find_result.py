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
            break_timeout (Union[Unset, bool]): The time limit for the search is exceeded.
            break_total_count (Union[Unset, bool]): The search is breaked because the total number of results are reached.
            config_files (Union[Unset, List['ConfigFile']]):
            ids (Union[Unset, List[str]]):
            more_results (Union[Unset, bool]): Is true if there are more results.
            report_infos (Union[Unset, List['ReportInfo']]):
            count (Union[Unset, int]): Number of results. This member is only valid, if FindInfo.findOptions.evalCount is
                true.
            estimated_count (Union[Unset, int]): Estimated number of hits that can be found by the query.
                This number cannot be computed for any search and is
                 usually -1. Only if the search engine supplies an estimated count, it is &gt;= 0.
            search_id (Union[Unset, str]): Identifier to get more results.
            sords (Union[Unset, List['Sord']]):
            tasks (Union[Unset, List['UserTask']]):
            workflows (Union[Unset, List['WFDiagram']]):
            translate_terms (Union[Unset, List['TranslateTerm']]):
            fulltext_result_items (Union[Unset, List['FindByFulltextResultItem']]):
            fulltext_ctrl_result_items (Union[Unset, List['FindByFulltextCtrlResultItem']]):
            dynamic_folder (Union[Unset, str]): String representation of FindInfo used to define a dynamic register.
                Function
                 {@link IXServicePortIF#findFirstSords(ClientInfo, FindInfo, int, SordZ)} returns a serialized FindInfo in this
                 member. It can be used to define a dynamic register by setting <code>Sord.desc=FindResult.dynamicFolder</code>.
            job_states (Union[Unset, List['JobState']]):
            actions (Union[Unset, List['Action']]):
            feeds (Union[Unset, MapToFeed]):
            subscriptions (Union[Unset, MapToSubscription]):
            notifications (Union[Unset, MapToNotification]):
            hash_tag_relations (Union[Unset, List['HashTagRelation']]):
            hash_tags (Union[Unset, MapToHashTag]):
            notes (Union[Unset, List['Note']]):
            user_infos (Union[Unset, MapToUserInfo]):
            user_names (Union[Unset, MapToUserName]):
            context_terms (Union[Unset, List['ContextTermResults']]):
            completions (Union[Unset, List[str]]):
            corrections (Union[Unset, List[str]]):
            synonyms (Union[Unset, List[str]]):
            sorted_result (Union[Unset, List['ValueClass']]):
            masks (Union[Unset, MapToDocMask]):
    """

    break_timeout: Union[Unset, bool] = UNSET
    break_total_count: Union[Unset, bool] = UNSET
    config_files: Union[Unset, List["ConfigFile"]] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    more_results: Union[Unset, bool] = UNSET
    report_infos: Union[Unset, List["ReportInfo"]] = UNSET
    count: Union[Unset, int] = UNSET
    estimated_count: Union[Unset, int] = UNSET
    search_id: Union[Unset, str] = UNSET
    sords: Union[Unset, List["Sord"]] = UNSET
    tasks: Union[Unset, List["UserTask"]] = UNSET
    workflows: Union[Unset, List["WFDiagram"]] = UNSET
    translate_terms: Union[Unset, List["TranslateTerm"]] = UNSET
    fulltext_result_items: Union[Unset, List["FindByFulltextResultItem"]] = UNSET
    fulltext_ctrl_result_items: Union[Unset, List["FindByFulltextCtrlResultItem"]] = UNSET
    dynamic_folder: Union[Unset, str] = UNSET
    job_states: Union[Unset, List["JobState"]] = UNSET
    actions: Union[Unset, List["Action"]] = UNSET
    feeds: Union[Unset, "MapToFeed"] = UNSET
    subscriptions: Union[Unset, "MapToSubscription"] = UNSET
    notifications: Union[Unset, "MapToNotification"] = UNSET
    hash_tag_relations: Union[Unset, List["HashTagRelation"]] = UNSET
    hash_tags: Union[Unset, "MapToHashTag"] = UNSET
    notes: Union[Unset, List["Note"]] = UNSET
    user_infos: Union[Unset, "MapToUserInfo"] = UNSET
    user_names: Union[Unset, "MapToUserName"] = UNSET
    context_terms: Union[Unset, List["ContextTermResults"]] = UNSET
    completions: Union[Unset, List[str]] = UNSET
    corrections: Union[Unset, List[str]] = UNSET
    synonyms: Union[Unset, List[str]] = UNSET
    sorted_result: Union[Unset, List["ValueClass"]] = UNSET
    masks: Union[Unset, "MapToDocMask"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        break_timeout = self.break_timeout
        break_total_count = self.break_total_count
        config_files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.config_files, Unset):
            config_files = []
            for config_files_item_data in self.config_files:
                config_files_item = config_files_item_data.to_dict()

                config_files.append(config_files_item)

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        more_results = self.more_results
        report_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_infos, Unset):
            report_infos = []
            for report_infos_item_data in self.report_infos:
                report_infos_item = report_infos_item_data.to_dict()

                report_infos.append(report_infos_item)

        count = self.count
        estimated_count = self.estimated_count
        search_id = self.search_id
        sords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sords, Unset):
            sords = []
            for sords_item_data in self.sords:
                sords_item = sords_item_data.to_dict()

                sords.append(sords_item)

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        workflows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()

                workflows.append(workflows_item)

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

        fulltext_ctrl_result_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulltext_ctrl_result_items, Unset):
            fulltext_ctrl_result_items = []
            for fulltext_ctrl_result_items_item_data in self.fulltext_ctrl_result_items:
                fulltext_ctrl_result_items_item = fulltext_ctrl_result_items_item_data.to_dict()

                fulltext_ctrl_result_items.append(fulltext_ctrl_result_items_item)

        dynamic_folder = self.dynamic_folder
        job_states: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_states, Unset):
            job_states = []
            for job_states_item_data in self.job_states:
                job_states_item = job_states_item_data.to_dict()

                job_states.append(job_states_item)

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        feeds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feeds, Unset):
            feeds = self.feeds.to_dict()

        subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        hash_tag_relations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hash_tag_relations, Unset):
            hash_tag_relations = []
            for componentsschemas_list_of_hash_tag_relation_item_data in self.hash_tag_relations:
                componentsschemas_list_of_hash_tag_relation_item = (
                    componentsschemas_list_of_hash_tag_relation_item_data.to_dict()
                )

                hash_tag_relations.append(componentsschemas_list_of_hash_tag_relation_item)

        hash_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hash_tags, Unset):
            hash_tags = self.hash_tags.to_dict()

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for componentsschemas_list_of_note_item_data in self.notes:
                componentsschemas_list_of_note_item = componentsschemas_list_of_note_item_data.to_dict()

                notes.append(componentsschemas_list_of_note_item)

        user_infos: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_infos, Unset):
            user_infos = self.user_infos.to_dict()

        user_names: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_names, Unset):
            user_names = self.user_names.to_dict()

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

        corrections: Union[Unset, List[str]] = UNSET
        if not isinstance(self.corrections, Unset):
            corrections = self.corrections

        synonyms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        sorted_result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorted_result, Unset):
            sorted_result = []
            for componentsschemas_list_of_value_class_item_data in self.sorted_result:
                componentsschemas_list_of_value_class_item = componentsschemas_list_of_value_class_item_data.to_dict()

                sorted_result.append(componentsschemas_list_of_value_class_item)

        masks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.masks, Unset):
            masks = self.masks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if break_timeout is not UNSET:
            field_dict["breakTimeout"] = break_timeout
        if break_total_count is not UNSET:
            field_dict["breakTotalCount"] = break_total_count
        if config_files is not UNSET:
            field_dict["configFiles"] = config_files
        if ids is not UNSET:
            field_dict["ids"] = ids
        if more_results is not UNSET:
            field_dict["moreResults"] = more_results
        if report_infos is not UNSET:
            field_dict["reportInfos"] = report_infos
        if count is not UNSET:
            field_dict["count"] = count
        if estimated_count is not UNSET:
            field_dict["estimatedCount"] = estimated_count
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if sords is not UNSET:
            field_dict["sords"] = sords
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if workflows is not UNSET:
            field_dict["workflows"] = workflows
        if translate_terms is not UNSET:
            field_dict["translateTerms"] = translate_terms
        if fulltext_result_items is not UNSET:
            field_dict["fulltextResultItems"] = fulltext_result_items
        if fulltext_ctrl_result_items is not UNSET:
            field_dict["fulltextCtrlResultItems"] = fulltext_ctrl_result_items
        if dynamic_folder is not UNSET:
            field_dict["dynamicFolder"] = dynamic_folder
        if job_states is not UNSET:
            field_dict["jobStates"] = job_states
        if actions is not UNSET:
            field_dict["actions"] = actions
        if feeds is not UNSET:
            field_dict["feeds"] = feeds
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if hash_tag_relations is not UNSET:
            field_dict["hashTagRelations"] = hash_tag_relations
        if hash_tags is not UNSET:
            field_dict["hashTags"] = hash_tags
        if notes is not UNSET:
            field_dict["notes"] = notes
        if user_infos is not UNSET:
            field_dict["userInfos"] = user_infos
        if user_names is not UNSET:
            field_dict["userNames"] = user_names
        if context_terms is not UNSET:
            field_dict["contextTerms"] = context_terms
        if completions is not UNSET:
            field_dict["completions"] = completions
        if corrections is not UNSET:
            field_dict["corrections"] = corrections
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if sorted_result is not UNSET:
            field_dict["sortedResult"] = sorted_result
        if masks is not UNSET:
            field_dict["masks"] = masks

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
        break_timeout = d.pop("breakTimeout", UNSET)

        break_total_count = d.pop("breakTotalCount", UNSET)

        config_files = []
        _config_files = d.pop("configFiles", UNSET)
        for config_files_item_data in _config_files or []:
            config_files_item = ConfigFile.from_dict(config_files_item_data)

            config_files.append(config_files_item)

        ids = cast(List[str], d.pop("ids", UNSET))

        more_results = d.pop("moreResults", UNSET)

        report_infos = []
        _report_infos = d.pop("reportInfos", UNSET)
        for report_infos_item_data in _report_infos or []:
            report_infos_item = ReportInfo.from_dict(report_infos_item_data)

            report_infos.append(report_infos_item)

        count = d.pop("count", UNSET)

        estimated_count = d.pop("estimatedCount", UNSET)

        search_id = d.pop("searchId", UNSET)

        sords = []
        _sords = d.pop("sords", UNSET)
        for sords_item_data in _sords or []:
            sords_item = Sord.from_dict(sords_item_data)

            sords.append(sords_item)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = UserTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        workflows = []
        _workflows = d.pop("workflows", UNSET)
        for workflows_item_data in _workflows or []:
            workflows_item = WFDiagram.from_dict(workflows_item_data)

            workflows.append(workflows_item)

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

        fulltext_ctrl_result_items = []
        _fulltext_ctrl_result_items = d.pop("fulltextCtrlResultItems", UNSET)
        for fulltext_ctrl_result_items_item_data in _fulltext_ctrl_result_items or []:
            fulltext_ctrl_result_items_item = FindByFulltextCtrlResultItem.from_dict(
                fulltext_ctrl_result_items_item_data
            )

            fulltext_ctrl_result_items.append(fulltext_ctrl_result_items_item)

        dynamic_folder = d.pop("dynamicFolder", UNSET)

        job_states = []
        _job_states = d.pop("jobStates", UNSET)
        for job_states_item_data in _job_states or []:
            job_states_item = JobState.from_dict(job_states_item_data)

            job_states.append(job_states_item)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = Action.from_dict(actions_item_data)

            actions.append(actions_item)

        _feeds = d.pop("feeds", UNSET)
        feeds: Union[Unset, MapToFeed]
        if isinstance(_feeds, Unset):
            feeds = UNSET
        else:
            feeds = MapToFeed.from_dict(_feeds)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: Union[Unset, MapToSubscription]
        if isinstance(_subscriptions, Unset):
            subscriptions = UNSET
        else:
            subscriptions = MapToSubscription.from_dict(_subscriptions)

        _notifications = d.pop("notifications", UNSET)
        notifications: Union[Unset, MapToNotification]
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = MapToNotification.from_dict(_notifications)

        hash_tag_relations = []
        _hash_tag_relations = d.pop("hashTagRelations", UNSET)
        for componentsschemas_list_of_hash_tag_relation_item_data in _hash_tag_relations or []:
            componentsschemas_list_of_hash_tag_relation_item = HashTagRelation.from_dict(
                componentsschemas_list_of_hash_tag_relation_item_data
            )

            hash_tag_relations.append(componentsschemas_list_of_hash_tag_relation_item)

        _hash_tags = d.pop("hashTags", UNSET)
        hash_tags: Union[Unset, MapToHashTag]
        if isinstance(_hash_tags, Unset):
            hash_tags = UNSET
        else:
            hash_tags = MapToHashTag.from_dict(_hash_tags)

        notes = []
        _notes = d.pop("notes", UNSET)
        for componentsschemas_list_of_note_item_data in _notes or []:
            componentsschemas_list_of_note_item = Note.from_dict(componentsschemas_list_of_note_item_data)

            notes.append(componentsschemas_list_of_note_item)

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

        context_terms = []
        _context_terms = d.pop("contextTerms", UNSET)
        for componentsschemas_list_of_context_term_results_item_data in _context_terms or []:
            componentsschemas_list_of_context_term_results_item = ContextTermResults.from_dict(
                componentsschemas_list_of_context_term_results_item_data
            )

            context_terms.append(componentsschemas_list_of_context_term_results_item)

        completions = cast(List[str], d.pop("completions", UNSET))

        corrections = cast(List[str], d.pop("corrections", UNSET))

        synonyms = cast(List[str], d.pop("synonyms", UNSET))

        sorted_result = []
        _sorted_result = d.pop("sortedResult", UNSET)
        for componentsschemas_list_of_value_class_item_data in _sorted_result or []:
            componentsschemas_list_of_value_class_item = ValueClass.from_dict(
                componentsschemas_list_of_value_class_item_data
            )

            sorted_result.append(componentsschemas_list_of_value_class_item)

        _masks = d.pop("masks", UNSET)
        masks: Union[Unset, MapToDocMask]
        if isinstance(_masks, Unset):
            masks = UNSET
        else:
            masks = MapToDocMask.from_dict(_masks)

        find_result = cls(
            break_timeout=break_timeout,
            break_total_count=break_total_count,
            config_files=config_files,
            ids=ids,
            more_results=more_results,
            report_infos=report_infos,
            count=count,
            estimated_count=estimated_count,
            search_id=search_id,
            sords=sords,
            tasks=tasks,
            workflows=workflows,
            translate_terms=translate_terms,
            fulltext_result_items=fulltext_result_items,
            fulltext_ctrl_result_items=fulltext_ctrl_result_items,
            dynamic_folder=dynamic_folder,
            job_states=job_states,
            actions=actions,
            feeds=feeds,
            subscriptions=subscriptions,
            notifications=notifications,
            hash_tag_relations=hash_tag_relations,
            hash_tags=hash_tags,
            notes=notes,
            user_infos=user_infos,
            user_names=user_names,
            context_terms=context_terms,
            completions=completions,
            corrections=corrections,
            synonyms=synonyms,
            sorted_result=sorted_result,
            masks=masks,
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
