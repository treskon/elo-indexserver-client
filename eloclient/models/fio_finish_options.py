from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_state import JobState


T = TypeVar("T", bound="FioFinishOptions")


@_attrs_define
class FioFinishOptions:
    """
    Attributes:
        job_state (Union[Unset, JobState]): Objects of this class provide information on the state of any background
            processes.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    job_state: Union[Unset, "JobState"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_state, Unset):
            job_state = self.job_state.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_state is not UNSET:
            field_dict["jobState"] = job_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_state import JobState

        d = src_dict.copy()
        _job_state = d.pop("jobState", UNSET)
        job_state: Union[Unset, JobState]
        if isinstance(_job_state, Unset):
            job_state = UNSET
        else:
            job_state = JobState.from_dict(_job_state)

        fio_finish_options = cls(
            job_state=job_state,
        )

        fio_finish_options.additional_properties = d
        return fio_finish_options

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
