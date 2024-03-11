from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask_z import DocMaskZ
    from ..models.find_result_access_mode import FindResultAccessMode
    from ..models.lock_z import LockZ
    from ..models.repl_set import ReplSet
    from ..models.search_mode_z import SearchModeZ


T = TypeVar("T", bound="FindOptions")


@_attrs_define
class FindOptions:
    """This class contains several options to control the search process of findFirstSords.

    Attributes:
        escape_char (Union[Unset, str]): SQL escape character. Overwrites the character that can be specified by
            setSessionOptions.
        incl_deleted (Union[Unset, bool]): Include logically deleted objects.
        obj_ids (Union[Unset, List[str]]):
        order_by (Union[Unset, str]): An SQL ORDER BY clause can be provided here, if required.
        range_delimiter (Union[Unset, str]): Range values can be used to search many index and date attribute values.
            The delimiter between the lower limit and
             upper limit value is defined by rangeDelimiter. The default rangeDelimiter is "...".
        repl_set (Union[Unset, ReplSet]): <p>
            Objects of this class store the replication information of archive entries.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        reserved (Union[Unset, str]): This value is reserved for internal testing purposes and must be set to 0 in all
            cases.
        search_id (Union[Unset, str]): Restricts the results to objects returned by a previous search.
        search_mode (Union[Unset, SearchModeZ]): <p>
            This class encapsulates the constants of <code>SearchModeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        sort_order (Union[Unset, int]): Defines the sort order of the results.
            If sortOrder is 0 and the search process searches for child objects
             (FindInfo.findChildren!=null), the objects are sorted by the sort flags of the parent. If sortOrder is 0 and
            the
             search uses FindInfo.findByIndex, the objects are sorted alphabetically.
        timeout_seconds (Union[Unset, int]): Specifies the time limit for the search. If the limit is exceeded, the
            search is interruped.
            If the search is not
             to have a time limit timeoutSeconds=0 must be used.
        total_count (Union[Unset, int]): The search is terminated if this number of objects are found.
            If the number of results should not be constrained,
             set this value to 2^32-1 = 2147483647 (maximum value of a positive 32bit integer minus 1). If totalCount is not
             set, the Indexserver option totalCount is used, which is 10000 by default. If this value is set to 1,
             findFirstSords will not generate a report entry {@link ReportInfoC#ACT_CLIENT_SEARCH}.
        eval_count (Union[Unset, bool]): Compute the number of results. The number of results are returned in
            FindResult.count.
            Be aware of the fact that
             this option needs to read all database result rows and check user access before findFirstSords returns.
        only_deleted (Union[Unset, bool]): Only logically deleted objects. If this member is true, inclDeleted is
            ignored.
        t_stamp (Union[Unset, str]): Return objects that were last modified at this time or in this time range.
            The time stamp is an ISO formatted value
             in the UTC timezone. It might include dots to separate the date and time elements. A time range is separated by
            the
             <code>rangeDelimiter</code>. The selection includes the range limits. Because the FindOptions cannot be the
            only
             criteria in FindInfo, use FindByIndex.name="*" to select over the entire archive.
        wildcards (Union[Unset, str]): This characters are used as wildcards in search terms. The first wildcard is used
            for zero or more characters.
            The
             second wildcard is used for exactly one character. By default (if this member is null or empty), only the first
             wildcard is defined: *.
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        search_lifetime_seconds (Union[Unset, int]): Lifetime of cached search results. This value overrides the ELOix
            configuration option searchLifetimeSeconds.
            The
             value determines the time in seconds, how long the search results are cached. As long the results are valid,
            they
             can be read by findNext-functions of the API.
        exclude_summary (Union[Unset, bool]): Do not generate summary information. Retrieving summaries is very
            expensive for the iSearch module.
        find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
            find results.
        doc_mask_z (Union[Unset, DocMaskZ]): This class encapsulates the constants of the DocMaskC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    escape_char: Union[Unset, str] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    obj_ids: Union[Unset, List[str]] = UNSET
    order_by: Union[Unset, str] = UNSET
    range_delimiter: Union[Unset, str] = UNSET
    repl_set: Union[Unset, "ReplSet"] = UNSET
    reserved: Union[Unset, str] = UNSET
    search_id: Union[Unset, str] = UNSET
    search_mode: Union[Unset, "SearchModeZ"] = UNSET
    sort_order: Union[Unset, int] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    total_count: Union[Unset, int] = UNSET
    eval_count: Union[Unset, bool] = UNSET
    only_deleted: Union[Unset, bool] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    wildcards: Union[Unset, str] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    search_lifetime_seconds: Union[Unset, int] = UNSET
    exclude_summary: Union[Unset, bool] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    doc_mask_z: Union[Unset, "DocMaskZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        escape_char = self.escape_char
        incl_deleted = self.incl_deleted
        obj_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.obj_ids, Unset):
            obj_ids = self.obj_ids

        order_by = self.order_by
        range_delimiter = self.range_delimiter
        repl_set: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repl_set, Unset):
            repl_set = self.repl_set.to_dict()

        reserved = self.reserved
        search_id = self.search_id
        search_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_mode, Unset):
            search_mode = self.search_mode.to_dict()

        sort_order = self.sort_order
        timeout_seconds = self.timeout_seconds
        total_count = self.total_count
        eval_count = self.eval_count
        only_deleted = self.only_deleted
        t_stamp = self.t_stamp
        wildcards = self.wildcards
        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        search_lifetime_seconds = self.search_lifetime_seconds
        exclude_summary = self.exclude_summary
        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        doc_mask_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask_z, Unset):
            doc_mask_z = self.doc_mask_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if escape_char is not UNSET:
            field_dict["escapeChar"] = escape_char
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted
        if obj_ids is not UNSET:
            field_dict["objIds"] = obj_ids
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if range_delimiter is not UNSET:
            field_dict["rangeDelimiter"] = range_delimiter
        if repl_set is not UNSET:
            field_dict["replSet"] = repl_set
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if search_mode is not UNSET:
            field_dict["searchMode"] = search_mode
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if eval_count is not UNSET:
            field_dict["evalCount"] = eval_count
        if only_deleted is not UNSET:
            field_dict["onlyDeleted"] = only_deleted
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if wildcards is not UNSET:
            field_dict["wildcards"] = wildcards
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if search_lifetime_seconds is not UNSET:
            field_dict["searchLifetimeSeconds"] = search_lifetime_seconds
        if exclude_summary is not UNSET:
            field_dict["excludeSummary"] = exclude_summary
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode
        if doc_mask_z is not UNSET:
            field_dict["docMaskZ"] = doc_mask_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask_z import DocMaskZ
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.lock_z import LockZ
        from ..models.repl_set import ReplSet
        from ..models.search_mode_z import SearchModeZ

        d = src_dict.copy()
        escape_char = d.pop("escapeChar", UNSET)

        incl_deleted = d.pop("inclDeleted", UNSET)

        obj_ids = cast(List[str], d.pop("objIds", UNSET))

        order_by = d.pop("orderBy", UNSET)

        range_delimiter = d.pop("rangeDelimiter", UNSET)

        _repl_set = d.pop("replSet", UNSET)
        repl_set: Union[Unset, ReplSet]
        if isinstance(_repl_set, Unset):
            repl_set = UNSET
        else:
            repl_set = ReplSet.from_dict(_repl_set)

        reserved = d.pop("reserved", UNSET)

        search_id = d.pop("searchId", UNSET)

        _search_mode = d.pop("searchMode", UNSET)
        search_mode: Union[Unset, SearchModeZ]
        if isinstance(_search_mode, Unset):
            search_mode = UNSET
        else:
            search_mode = SearchModeZ.from_dict(_search_mode)

        sort_order = d.pop("sortOrder", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        total_count = d.pop("totalCount", UNSET)

        eval_count = d.pop("evalCount", UNSET)

        only_deleted = d.pop("onlyDeleted", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        wildcards = d.pop("wildcards", UNSET)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        search_lifetime_seconds = d.pop("searchLifetimeSeconds", UNSET)

        exclude_summary = d.pop("excludeSummary", UNSET)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        _doc_mask_z = d.pop("docMaskZ", UNSET)
        doc_mask_z: Union[Unset, DocMaskZ]
        if isinstance(_doc_mask_z, Unset):
            doc_mask_z = UNSET
        else:
            doc_mask_z = DocMaskZ.from_dict(_doc_mask_z)

        find_options = cls(
            escape_char=escape_char,
            incl_deleted=incl_deleted,
            obj_ids=obj_ids,
            order_by=order_by,
            range_delimiter=range_delimiter,
            repl_set=repl_set,
            reserved=reserved,
            search_id=search_id,
            search_mode=search_mode,
            sort_order=sort_order,
            timeout_seconds=timeout_seconds,
            total_count=total_count,
            eval_count=eval_count,
            only_deleted=only_deleted,
            t_stamp=t_stamp,
            wildcards=wildcards,
            lock_z=lock_z,
            search_lifetime_seconds=search_lifetime_seconds,
            exclude_summary=exclude_summary,
            find_result_access_mode=find_result_access_mode,
            doc_mask_z=doc_mask_z,
        )

        find_options.additional_properties = d
        return find_options

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
