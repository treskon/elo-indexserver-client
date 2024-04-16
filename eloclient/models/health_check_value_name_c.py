from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheckValueNameC")


@_attrs_define
class HealthCheckValueNameC:
    """Predefined value names for HealthCheckInfo objects.

    Attributes:
        nb_of_failed_logins (Union[Unset, str]): Number of failed logins. Due to wrong name or password.
        nb_of_sessions (Union[Unset, str]): Number of current sessions.
        nb_of_documents (Union[Unset, str]): Number of logically documents.
        nb_of_successful_logins (Union[Unset, str]): Number of successful logins.
            the full number of attempted logins, whether successful or not is
             the sum of successful and failed logins.
        nb_of_checkoutsord (Union[Unset, str]): Number of checkoutSord calls.
        status_of_versions (Union[Unset, str]): Version status.
        nb_of_garbage_collections (Union[Unset, str]): Number of Garbage Collections.
        duration_of_workflow_forwarding (Union[Unset, str]): Duration of Workflow forwarding.
        nb_of_checkinsord (Union[Unset, str]): Number of checkinSord calls.
        size_of_used_java_heap (Union[Unset, str]): Java Heap Size.
        duration_of_sql_query (Union[Unset, str]): Duration of SQL queries.
        duration_of_checkoutsord (Union[Unset, str]): Duration of checkoutSord calls.
        dynamic (Union[Unset, str]): Name of dynamically evaluated values starts with this prefix.
        nb_of_document_files_without_backup (Union[Unset, str]): Number of logically documents without backup.
        nb_of_document_files (Union[Unset, str]): Number of document files (resp. number of document versions).
        duration_of_search_query (Union[Unset, str]): Search Task duration.
        nb_of_ix_method_calls (Union[Unset, str]): Number of IX-method calls.
        total_size_of_document_files (Union[Unset, str]): Total size of document files (resp. document versions).
        duration_of_ix_method_calls (Union[Unset, str]): Duration of IX-method calls.
        free_space_of_sql_server (Union[Unset, str]): Freier Speicher SQL Server.
        duration_of_checkinsord (Union[Unset, str]): Duration of checkinSord calls.
        nb_of_document_files_with_backup (Union[Unset, str]): Number of document files with backup.
    """

    nb_of_failed_logins: Union[Unset, str] = UNSET
    nb_of_sessions: Union[Unset, str] = UNSET
    nb_of_documents: Union[Unset, str] = UNSET
    nb_of_successful_logins: Union[Unset, str] = UNSET
    nb_of_checkoutsord: Union[Unset, str] = UNSET
    status_of_versions: Union[Unset, str] = UNSET
    nb_of_garbage_collections: Union[Unset, str] = UNSET
    duration_of_workflow_forwarding: Union[Unset, str] = UNSET
    nb_of_checkinsord: Union[Unset, str] = UNSET
    size_of_used_java_heap: Union[Unset, str] = UNSET
    duration_of_sql_query: Union[Unset, str] = UNSET
    duration_of_checkoutsord: Union[Unset, str] = UNSET
    dynamic: Union[Unset, str] = UNSET
    nb_of_document_files_without_backup: Union[Unset, str] = UNSET
    nb_of_document_files: Union[Unset, str] = UNSET
    duration_of_search_query: Union[Unset, str] = UNSET
    nb_of_ix_method_calls: Union[Unset, str] = UNSET
    total_size_of_document_files: Union[Unset, str] = UNSET
    duration_of_ix_method_calls: Union[Unset, str] = UNSET
    free_space_of_sql_server: Union[Unset, str] = UNSET
    duration_of_checkinsord: Union[Unset, str] = UNSET
    nb_of_document_files_with_backup: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nb_of_failed_logins = self.nb_of_failed_logins

        nb_of_sessions = self.nb_of_sessions

        nb_of_documents = self.nb_of_documents

        nb_of_successful_logins = self.nb_of_successful_logins

        nb_of_checkoutsord = self.nb_of_checkoutsord

        status_of_versions = self.status_of_versions

        nb_of_garbage_collections = self.nb_of_garbage_collections

        duration_of_workflow_forwarding = self.duration_of_workflow_forwarding

        nb_of_checkinsord = self.nb_of_checkinsord

        size_of_used_java_heap = self.size_of_used_java_heap

        duration_of_sql_query = self.duration_of_sql_query

        duration_of_checkoutsord = self.duration_of_checkoutsord

        dynamic = self.dynamic

        nb_of_document_files_without_backup = self.nb_of_document_files_without_backup

        nb_of_document_files = self.nb_of_document_files

        duration_of_search_query = self.duration_of_search_query

        nb_of_ix_method_calls = self.nb_of_ix_method_calls

        total_size_of_document_files = self.total_size_of_document_files

        duration_of_ix_method_calls = self.duration_of_ix_method_calls

        free_space_of_sql_server = self.free_space_of_sql_server

        duration_of_checkinsord = self.duration_of_checkinsord

        nb_of_document_files_with_backup = self.nb_of_document_files_with_backup

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nb_of_failed_logins is not UNSET:
            field_dict["NB_OF_FAILED_LOGINS"] = nb_of_failed_logins
        if nb_of_sessions is not UNSET:
            field_dict["NB_OF_SESSIONS"] = nb_of_sessions
        if nb_of_documents is not UNSET:
            field_dict["NB_OF_DOCUMENTS"] = nb_of_documents
        if nb_of_successful_logins is not UNSET:
            field_dict["NB_OF_SUCCESSFUL_LOGINS"] = nb_of_successful_logins
        if nb_of_checkoutsord is not UNSET:
            field_dict["NB_OF_CHECKOUTSORD"] = nb_of_checkoutsord
        if status_of_versions is not UNSET:
            field_dict["STATUS_OF_VERSIONS"] = status_of_versions
        if nb_of_garbage_collections is not UNSET:
            field_dict["NB_OF_GARBAGE_COLLECTIONS"] = nb_of_garbage_collections
        if duration_of_workflow_forwarding is not UNSET:
            field_dict["DURATION_OF_WORKFLOW_FORWARDING"] = duration_of_workflow_forwarding
        if nb_of_checkinsord is not UNSET:
            field_dict["NB_OF_CHECKINSORD"] = nb_of_checkinsord
        if size_of_used_java_heap is not UNSET:
            field_dict["SIZE_OF_USED_JAVA_HEAP"] = size_of_used_java_heap
        if duration_of_sql_query is not UNSET:
            field_dict["DURATION_OF_SQL_QUERY"] = duration_of_sql_query
        if duration_of_checkoutsord is not UNSET:
            field_dict["DURATION_OF_CHECKOUTSORD"] = duration_of_checkoutsord
        if dynamic is not UNSET:
            field_dict["DYNAMIC"] = dynamic
        if nb_of_document_files_without_backup is not UNSET:
            field_dict["NB_OF_DOCUMENT_FILES_WITHOUT_BACKUP"] = nb_of_document_files_without_backup
        if nb_of_document_files is not UNSET:
            field_dict["NB_OF_DOCUMENT_FILES"] = nb_of_document_files
        if duration_of_search_query is not UNSET:
            field_dict["DURATION_OF_SEARCH_QUERY"] = duration_of_search_query
        if nb_of_ix_method_calls is not UNSET:
            field_dict["NB_OF_IX_METHOD_CALLS"] = nb_of_ix_method_calls
        if total_size_of_document_files is not UNSET:
            field_dict["TOTAL_SIZE_OF_DOCUMENT_FILES"] = total_size_of_document_files
        if duration_of_ix_method_calls is not UNSET:
            field_dict["DURATION_OF_IX_METHOD_CALLS"] = duration_of_ix_method_calls
        if free_space_of_sql_server is not UNSET:
            field_dict["FREE_SPACE_OF_SQL_SERVER"] = free_space_of_sql_server
        if duration_of_checkinsord is not UNSET:
            field_dict["DURATION_OF_CHECKINSORD"] = duration_of_checkinsord
        if nb_of_document_files_with_backup is not UNSET:
            field_dict["NB_OF_DOCUMENT_FILES_WITH_BACKUP"] = nb_of_document_files_with_backup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nb_of_failed_logins = d.pop("NB_OF_FAILED_LOGINS", UNSET)

        nb_of_sessions = d.pop("NB_OF_SESSIONS", UNSET)

        nb_of_documents = d.pop("NB_OF_DOCUMENTS", UNSET)

        nb_of_successful_logins = d.pop("NB_OF_SUCCESSFUL_LOGINS", UNSET)

        nb_of_checkoutsord = d.pop("NB_OF_CHECKOUTSORD", UNSET)

        status_of_versions = d.pop("STATUS_OF_VERSIONS", UNSET)

        nb_of_garbage_collections = d.pop("NB_OF_GARBAGE_COLLECTIONS", UNSET)

        duration_of_workflow_forwarding = d.pop("DURATION_OF_WORKFLOW_FORWARDING", UNSET)

        nb_of_checkinsord = d.pop("NB_OF_CHECKINSORD", UNSET)

        size_of_used_java_heap = d.pop("SIZE_OF_USED_JAVA_HEAP", UNSET)

        duration_of_sql_query = d.pop("DURATION_OF_SQL_QUERY", UNSET)

        duration_of_checkoutsord = d.pop("DURATION_OF_CHECKOUTSORD", UNSET)

        dynamic = d.pop("DYNAMIC", UNSET)

        nb_of_document_files_without_backup = d.pop("NB_OF_DOCUMENT_FILES_WITHOUT_BACKUP", UNSET)

        nb_of_document_files = d.pop("NB_OF_DOCUMENT_FILES", UNSET)

        duration_of_search_query = d.pop("DURATION_OF_SEARCH_QUERY", UNSET)

        nb_of_ix_method_calls = d.pop("NB_OF_IX_METHOD_CALLS", UNSET)

        total_size_of_document_files = d.pop("TOTAL_SIZE_OF_DOCUMENT_FILES", UNSET)

        duration_of_ix_method_calls = d.pop("DURATION_OF_IX_METHOD_CALLS", UNSET)

        free_space_of_sql_server = d.pop("FREE_SPACE_OF_SQL_SERVER", UNSET)

        duration_of_checkinsord = d.pop("DURATION_OF_CHECKINSORD", UNSET)

        nb_of_document_files_with_backup = d.pop("NB_OF_DOCUMENT_FILES_WITH_BACKUP", UNSET)

        health_check_value_name_c = cls(
            nb_of_failed_logins=nb_of_failed_logins,
            nb_of_sessions=nb_of_sessions,
            nb_of_documents=nb_of_documents,
            nb_of_successful_logins=nb_of_successful_logins,
            nb_of_checkoutsord=nb_of_checkoutsord,
            status_of_versions=status_of_versions,
            nb_of_garbage_collections=nb_of_garbage_collections,
            duration_of_workflow_forwarding=duration_of_workflow_forwarding,
            nb_of_checkinsord=nb_of_checkinsord,
            size_of_used_java_heap=size_of_used_java_heap,
            duration_of_sql_query=duration_of_sql_query,
            duration_of_checkoutsord=duration_of_checkoutsord,
            dynamic=dynamic,
            nb_of_document_files_without_backup=nb_of_document_files_without_backup,
            nb_of_document_files=nb_of_document_files,
            duration_of_search_query=duration_of_search_query,
            nb_of_ix_method_calls=nb_of_ix_method_calls,
            total_size_of_document_files=total_size_of_document_files,
            duration_of_ix_method_calls=duration_of_ix_method_calls,
            free_space_of_sql_server=free_space_of_sql_server,
            duration_of_checkinsord=duration_of_checkinsord,
            nb_of_document_files_with_backup=nb_of_document_files_with_backup,
        )

        health_check_value_name_c.additional_properties = d
        return health_check_value_name_c

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
