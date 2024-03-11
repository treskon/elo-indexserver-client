from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.task_notify_type import TaskNotifyType
    from ..models.user_task import UserTask


T = TypeVar("T", bound="BRequestClientNotificationUpdateTask")


@_attrs_define
class BRequestClientNotificationUpdateTask:
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
        user_task (Union[Unset, UserTask]): Describes the tasks assigned to a user. ix.
            findFirstTasks returns the tasks for a user in the form of UserTask
             objects. Either activity, reminder or workflow is set depending upon whether the task is an activity, reminder
            or
             workflow task.

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        notify_type (Union[Unset, TaskNotifyType]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    user_task: Union[Unset, "UserTask"] = UNSET
    notify_type: Union[Unset, "TaskNotifyType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        user_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_task, Unset):
            user_task = self.user_task.to_dict()

        notify_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notify_type, Unset):
            notify_type = self.notify_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if user_task is not UNSET:
            field_dict["userTask"] = user_task
        if notify_type is not UNSET:
            field_dict["notifyType"] = notify_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.task_notify_type import TaskNotifyType
        from ..models.user_task import UserTask

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _user_task = d.pop("userTask", UNSET)
        user_task: Union[Unset, UserTask]
        if isinstance(_user_task, Unset):
            user_task = UNSET
        else:
            user_task = UserTask.from_dict(_user_task)

        _notify_type = d.pop("notifyType", UNSET)
        notify_type: Union[Unset, TaskNotifyType]
        if isinstance(_notify_type, Unset):
            notify_type = UNSET
        else:
            notify_type = TaskNotifyType.from_dict(_notify_type)

        b_request_client_notification_update_task = cls(
            ci=ci,
            user_task=user_task,
            notify_type=notify_type,
        )

        b_request_client_notification_update_task.additional_properties = d
        return b_request_client_notification_update_task

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
