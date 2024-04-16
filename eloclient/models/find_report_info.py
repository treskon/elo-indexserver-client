from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindReportInfo")


@_attrs_define
class FindReportInfo:
    """Objects of this class specify the selection criteria for report entries in
    <code>findReport</code>.
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            search_id (Union[Unset, str]): reserved.
            start_date_iso (Union[Unset, str]): Start date (UTC)
            obj_id (Union[Unset, str]): Object ID or GUID
            order_by (Union[Unset, str]): Can contain an SQL ORDER BY clause.
            timeout_seconds (Union[Unset, int]): Specifies the time limit for the search. If the limit is exceeded, the
                search is interruped.
                <code>timeoutSeconds=0</code> means that the search has no time limit.
            end_date_iso (Union[Unset, str]): End date (UTC)
            find_last_entry_before_end_date (Union[Unset, bool]): Find the last entry before the given {@link #endDateIso}.
                This option e.g.
                allows to find the
                 user permissions at the given {@link #endDateIso}. Therefore, set
                 <code>erpCodes = new int[] { ReportOptionsC.ERP_LOGOPENARC, ReportOptionsC.ERP_LOGUSERDATA };</code>.
            extra1 (Union[Unset, str]): Specifies the extra1 value. Only Integer values are allowed for this element.
            erp_codes (Union[Unset, List[int]]):
            total_count (Union[Unset, int]): The search is ended once this number of objects have been found.
                A value of <code>0</code> sets
                 no constraint to the number of objects.
            user_id (Union[Unset, str]): User ID or name.
    """

    search_id: Union[Unset, str] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    order_by: Union[Unset, str] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    end_date_iso: Union[Unset, str] = UNSET
    find_last_entry_before_end_date: Union[Unset, bool] = UNSET
    extra1: Union[Unset, str] = UNSET
    erp_codes: Union[Unset, List[int]] = UNSET
    total_count: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_id = self.search_id

        start_date_iso = self.start_date_iso

        obj_id = self.obj_id

        order_by = self.order_by

        timeout_seconds = self.timeout_seconds

        end_date_iso = self.end_date_iso

        find_last_entry_before_end_date = self.find_last_entry_before_end_date

        extra1 = self.extra1

        erp_codes: Union[Unset, List[int]] = UNSET
        if not isinstance(self.erp_codes, Unset):
            erp_codes = self.erp_codes

        total_count = self.total_count

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if start_date_iso is not UNSET:
            field_dict["startDateIso"] = start_date_iso
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if end_date_iso is not UNSET:
            field_dict["endDateIso"] = end_date_iso
        if find_last_entry_before_end_date is not UNSET:
            field_dict["findLastEntryBeforeEndDate"] = find_last_entry_before_end_date
        if extra1 is not UNSET:
            field_dict["extra1"] = extra1
        if erp_codes is not UNSET:
            field_dict["erpCodes"] = erp_codes
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_id = d.pop("searchId", UNSET)

        start_date_iso = d.pop("startDateIso", UNSET)

        obj_id = d.pop("objId", UNSET)

        order_by = d.pop("orderBy", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        end_date_iso = d.pop("endDateIso", UNSET)

        find_last_entry_before_end_date = d.pop("findLastEntryBeforeEndDate", UNSET)

        extra1 = d.pop("extra1", UNSET)

        erp_codes = cast(List[int], d.pop("erpCodes", UNSET))

        total_count = d.pop("totalCount", UNSET)

        user_id = d.pop("userId", UNSET)

        find_report_info = cls(
            search_id=search_id,
            start_date_iso=start_date_iso,
            obj_id=obj_id,
            order_by=order_by,
            timeout_seconds=timeout_seconds,
            end_date_iso=end_date_iso,
            find_last_entry_before_end_date=find_last_entry_before_end_date,
            extra1=extra1,
            erp_codes=erp_codes,
            total_count=total_count,
            user_id=user_id,
        )

        find_report_info.additional_properties = d
        return find_report_info

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
