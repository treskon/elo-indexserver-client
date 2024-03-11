from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count_result import CountResult
    from ..models.process_info import ProcessInfo


T = TypeVar("T", bound="JobState")


@_attrs_define
class JobState:
    """Objects of this class provide information on the state of any background processes.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            count_errors (Union[Unset, str]): Error status information.
            count_estimated_max (Union[Unset, str]): Estimated maximum amount.
            count_processed (Union[Unset, str]): Progress status information.
            expires (Union[Unset, str]): When the information expires (milliseconds): (jobEnd + expires &lt; current-date).
            job_end (Union[Unset, str]): End or termination of the job.
            job_guid (Union[Unset, str]): Job identifier.
            job_name (Union[Unset, str]): Thread name.
            job_running (Union[Unset, bool]): Set to true while the job is being executed.
            job_start (Union[Unset, str]): Start of job.
            last_guid (Union[Unset, str]): Status information for GUIDs.
            last_id (Union[Unset, int]): Status information for integer IDs.
            proc_info (Union[Unset, ProcessInfo]): Specific processing information for each node of processTrees(...) or
                processFindResults(...).
                The operations will be
                 for existence (not null) in order of their appearance in ProcessInfo. Some of the underlying structures may
                allow
                 toggling between prefix and postfix processing when used with processTrees.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            count_result (Union[Unset, CountResult]): Class for the results of one count process.
            str_msg (Union[Unset, str]): Job-defined message string.
            do_cancel_job (Union[Unset, bool]): Tell the Indexserver to cancel the job.
    """

    count_errors: Union[Unset, str] = UNSET
    count_estimated_max: Union[Unset, str] = UNSET
    count_processed: Union[Unset, str] = UNSET
    expires: Union[Unset, str] = UNSET
    job_end: Union[Unset, str] = UNSET
    job_guid: Union[Unset, str] = UNSET
    job_name: Union[Unset, str] = UNSET
    job_running: Union[Unset, bool] = UNSET
    job_start: Union[Unset, str] = UNSET
    last_guid: Union[Unset, str] = UNSET
    last_id: Union[Unset, int] = UNSET
    proc_info: Union[Unset, "ProcessInfo"] = UNSET
    count_result: Union[Unset, "CountResult"] = UNSET
    str_msg: Union[Unset, str] = UNSET
    do_cancel_job: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count_errors = self.count_errors
        count_estimated_max = self.count_estimated_max
        count_processed = self.count_processed
        expires = self.expires
        job_end = self.job_end
        job_guid = self.job_guid
        job_name = self.job_name
        job_running = self.job_running
        job_start = self.job_start
        last_guid = self.last_guid
        last_id = self.last_id
        proc_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_info, Unset):
            proc_info = self.proc_info.to_dict()

        count_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.count_result, Unset):
            count_result = self.count_result.to_dict()

        str_msg = self.str_msg
        do_cancel_job = self.do_cancel_job

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_errors is not UNSET:
            field_dict["countErrors"] = count_errors
        if count_estimated_max is not UNSET:
            field_dict["countEstimatedMax"] = count_estimated_max
        if count_processed is not UNSET:
            field_dict["countProcessed"] = count_processed
        if expires is not UNSET:
            field_dict["expires"] = expires
        if job_end is not UNSET:
            field_dict["jobEnd"] = job_end
        if job_guid is not UNSET:
            field_dict["jobGuid"] = job_guid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_running is not UNSET:
            field_dict["jobRunning"] = job_running
        if job_start is not UNSET:
            field_dict["jobStart"] = job_start
        if last_guid is not UNSET:
            field_dict["lastGuid"] = last_guid
        if last_id is not UNSET:
            field_dict["lastID"] = last_id
        if proc_info is not UNSET:
            field_dict["procInfo"] = proc_info
        if count_result is not UNSET:
            field_dict["countResult"] = count_result
        if str_msg is not UNSET:
            field_dict["strMsg"] = str_msg
        if do_cancel_job is not UNSET:
            field_dict["doCancelJob"] = do_cancel_job

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.count_result import CountResult
        from ..models.process_info import ProcessInfo

        d = src_dict.copy()
        count_errors = d.pop("countErrors", UNSET)

        count_estimated_max = d.pop("countEstimatedMax", UNSET)

        count_processed = d.pop("countProcessed", UNSET)

        expires = d.pop("expires", UNSET)

        job_end = d.pop("jobEnd", UNSET)

        job_guid = d.pop("jobGuid", UNSET)

        job_name = d.pop("jobName", UNSET)

        job_running = d.pop("jobRunning", UNSET)

        job_start = d.pop("jobStart", UNSET)

        last_guid = d.pop("lastGuid", UNSET)

        last_id = d.pop("lastID", UNSET)

        _proc_info = d.pop("procInfo", UNSET)
        proc_info: Union[Unset, ProcessInfo]
        if isinstance(_proc_info, Unset):
            proc_info = UNSET
        else:
            proc_info = ProcessInfo.from_dict(_proc_info)

        _count_result = d.pop("countResult", UNSET)
        count_result: Union[Unset, CountResult]
        if isinstance(_count_result, Unset):
            count_result = UNSET
        else:
            count_result = CountResult.from_dict(_count_result)

        str_msg = d.pop("strMsg", UNSET)

        do_cancel_job = d.pop("doCancelJob", UNSET)

        job_state = cls(
            count_errors=count_errors,
            count_estimated_max=count_estimated_max,
            count_processed=count_processed,
            expires=expires,
            job_end=job_end,
            job_guid=job_guid,
            job_name=job_name,
            job_running=job_running,
            job_start=job_start,
            last_guid=last_guid,
            last_id=last_id,
            proc_info=proc_info,
            count_result=count_result,
            str_msg=str_msg,
            do_cancel_job=do_cancel_job,
        )

        job_state.additional_properties = d
        return job_state

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
