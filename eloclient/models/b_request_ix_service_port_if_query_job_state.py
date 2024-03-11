from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFQueryJobState")


@_attrs_define
class BRequestIXServicePortIFQueryJobState:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        job_guid (Union[Unset, str]):
        active_jobs (Union[Unset, bool]):
        finished_jobs (Union[Unset, bool]):
        full_info (Union[Unset, bool]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    job_guid: Union[Unset, str] = UNSET
    active_jobs: Union[Unset, bool] = UNSET
    finished_jobs: Union[Unset, bool] = UNSET
    full_info: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        job_guid = self.job_guid
        active_jobs = self.active_jobs
        finished_jobs = self.finished_jobs
        full_info = self.full_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if job_guid is not UNSET:
            field_dict["jobGuid"] = job_guid
        if active_jobs is not UNSET:
            field_dict["activeJobs"] = active_jobs
        if finished_jobs is not UNSET:
            field_dict["finishedJobs"] = finished_jobs
        if full_info is not UNSET:
            field_dict["fullInfo"] = full_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        job_guid = d.pop("jobGuid", UNSET)

        active_jobs = d.pop("activeJobs", UNSET)

        finished_jobs = d.pop("finishedJobs", UNSET)

        full_info = d.pop("fullInfo", UNSET)

        b_request_ix_service_port_if_query_job_state = cls(
            ci=ci,
            job_guid=job_guid,
            active_jobs=active_jobs,
            finished_jobs=finished_jobs,
            full_info=full_info,
        )

        b_request_ix_service_port_if_query_job_state.additional_properties = d
        return b_request_ix_service_port_if_query_job_state

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
