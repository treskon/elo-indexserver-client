from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskNotifyType")


@_attrs_define
class TaskNotifyType:
    """
    Attributes:
        update_task (Union[Unset, TaskNotifyType]):
        remove_task (Union[Unset, TaskNotifyType]):
        insert_task (Union[Unset, TaskNotifyType]):
    """

    update_task: Union[Unset, "TaskNotifyType"] = UNSET
    remove_task: Union[Unset, "TaskNotifyType"] = UNSET
    insert_task: Union[Unset, "TaskNotifyType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_task, Unset):
            update_task = self.update_task.to_dict()

        remove_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remove_task, Unset):
            remove_task = self.remove_task.to_dict()

        insert_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.insert_task, Unset):
            insert_task = self.insert_task.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_task is not UNSET:
            field_dict["UpdateTask"] = update_task
        if remove_task is not UNSET:
            field_dict["RemoveTask"] = remove_task
        if insert_task is not UNSET:
            field_dict["InsertTask"] = insert_task

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _update_task = d.pop("UpdateTask", UNSET)
        update_task: Union[Unset, TaskNotifyType]
        if isinstance(_update_task, Unset):
            update_task = UNSET
        else:
            update_task = TaskNotifyType.from_dict(_update_task)

        _remove_task = d.pop("RemoveTask", UNSET)
        remove_task: Union[Unset, TaskNotifyType]
        if isinstance(_remove_task, Unset):
            remove_task = UNSET
        else:
            remove_task = TaskNotifyType.from_dict(_remove_task)

        _insert_task = d.pop("InsertTask", UNSET)
        insert_task: Union[Unset, TaskNotifyType]
        if isinstance(_insert_task, Unset):
            insert_task = UNSET
        else:
            insert_task = TaskNotifyType.from_dict(_insert_task)

        task_notify_type = cls(
            update_task=update_task,
            remove_task=remove_task,
            insert_task=insert_task,
        )

        task_notify_type.additional_properties = d
        return task_notify_type

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
