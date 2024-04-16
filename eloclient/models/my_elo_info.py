from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_notification_info import FindNotificationInfo
    from ..models.find_tasks_info import FindTasksInfo
    from ..models.find_workflow_info import FindWorkflowInfo


T = TypeVar("T", bound="MyELOInfo")


@_attrs_define
class MyELOInfo:
    """
    Attributes:
        date (Union[Unset, str]): Return Results only newer than the given date.
        notification_info (Union[Unset, FindNotificationInfo]): FindInfo for FindFirstNotifications.
        workflow_info (Union[Unset, FindWorkflowInfo]): This class contains the search criteria for selecting workflows.
            <p>
             Copyright: Copyright (c) 2008, 2010
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        max_ (Union[Unset, int]): Maximum number of Results that should be returned by this call.
        task_info (Union[Unset, FindTasksInfo]): This class contains the search criteria that are required for locating
            a task (reminders,
            workflow tasks or activity).
    """

    date: Union[Unset, str] = UNSET
    notification_info: Union[Unset, "FindNotificationInfo"] = UNSET
    workflow_info: Union[Unset, "FindWorkflowInfo"] = UNSET
    max_: Union[Unset, int] = UNSET
    task_info: Union[Unset, "FindTasksInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        notification_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notification_info, Unset):
            notification_info = self.notification_info.to_dict()

        workflow_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_info, Unset):
            workflow_info = self.workflow_info.to_dict()

        max_ = self.max_

        task_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.task_info, Unset):
            task_info = self.task_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if notification_info is not UNSET:
            field_dict["notificationInfo"] = notification_info
        if workflow_info is not UNSET:
            field_dict["workflowInfo"] = workflow_info
        if max_ is not UNSET:
            field_dict["max"] = max_
        if task_info is not UNSET:
            field_dict["taskInfo"] = task_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_notification_info import FindNotificationInfo
        from ..models.find_tasks_info import FindTasksInfo
        from ..models.find_workflow_info import FindWorkflowInfo

        d = src_dict.copy()
        date = d.pop("date", UNSET)

        _notification_info = d.pop("notificationInfo", UNSET)
        notification_info: Union[Unset, FindNotificationInfo]
        if isinstance(_notification_info, Unset):
            notification_info = UNSET
        else:
            notification_info = FindNotificationInfo.from_dict(_notification_info)

        _workflow_info = d.pop("workflowInfo", UNSET)
        workflow_info: Union[Unset, FindWorkflowInfo]
        if isinstance(_workflow_info, Unset):
            workflow_info = UNSET
        else:
            workflow_info = FindWorkflowInfo.from_dict(_workflow_info)

        max_ = d.pop("max", UNSET)

        _task_info = d.pop("taskInfo", UNSET)
        task_info: Union[Unset, FindTasksInfo]
        if isinstance(_task_info, Unset):
            task_info = UNSET
        else:
            task_info = FindTasksInfo.from_dict(_task_info)

        my_elo_info = cls(
            date=date,
            notification_info=notification_info,
            workflow_info=workflow_info,
            max_=max_,
            task_info=task_info,
        )

        my_elo_info.additional_properties = d
        return my_elo_info

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
