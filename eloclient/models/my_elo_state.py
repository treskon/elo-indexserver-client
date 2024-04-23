from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyELOState")


@_attrs_define
class MyELOState:
    """
    Attributes:
        new_feed (Union[Unset, bool]):
        new_workflow (Union[Unset, bool]):
        user_guid (Union[Unset, str]):
        new_task (Union[Unset, bool]):
    """

    new_feed: Union[Unset, bool] = UNSET
    new_workflow: Union[Unset, bool] = UNSET
    user_guid: Union[Unset, str] = UNSET
    new_task: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_feed = self.new_feed

        new_workflow = self.new_workflow

        user_guid = self.user_guid

        new_task = self.new_task

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_feed is not UNSET:
            field_dict["newFeed"] = new_feed
        if new_workflow is not UNSET:
            field_dict["newWorkflow"] = new_workflow
        if user_guid is not UNSET:
            field_dict["userGuid"] = user_guid
        if new_task is not UNSET:
            field_dict["newTask"] = new_task

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_feed = d.pop("newFeed", UNSET)

        new_workflow = d.pop("newWorkflow", UNSET)

        user_guid = d.pop("userGuid", UNSET)

        new_task = d.pop("newTask", UNSET)

        my_elo_state = cls(
            new_feed=new_feed,
            new_workflow=new_workflow,
            user_guid=user_guid,
            new_task=new_task,
        )

        my_elo_state.additional_properties = d
        return my_elo_state

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
