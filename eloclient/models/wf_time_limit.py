from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFTimeLimit")


@_attrs_define
class WFTimeLimit:
    """This class describes a time limit for a workflow or for a person node of a workflow.

    Attributes:
        time_limit (Union[Unset, int]): Time-limit in minutes.
        time_limit_iso (Union[Unset, str]): After this date the node exceeds the time-limit for processing. Read-only.
        over_time_limit (Union[Unset, bool]): True, if the workflow exceeds the time limit. Read-only.
        user_name (Union[Unset, str]): User name for timeLimitUserId; When writing a workflow with checkinWorkFlow, this
            value has
            preceedence before timeLimitUserId. Set timeLimitUserName to an empty string, if
             timeLimitUserId should be used.
        user_id (Union[Unset, int]): The ID of the user that should be informed, if the time-limit is exceeded.
            The Indexserver does
             not send any notification to the user. The client application is responsible for doing this.
    """

    time_limit: Union[Unset, int] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_limit = self.time_limit

        time_limit_iso = self.time_limit_iso

        over_time_limit = self.over_time_limit

        user_name = self.user_name

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_limit = d.pop("timeLimit", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        wf_time_limit = cls(
            time_limit=time_limit,
            time_limit_iso=time_limit_iso,
            over_time_limit=over_time_limit,
            user_name=user_name,
            user_id=user_id,
        )

        wf_time_limit.additional_properties = d
        return wf_time_limit

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
