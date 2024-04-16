from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_z import ActionZ


T = TypeVar("T", bound="ActionC")


@_attrs_define
class ActionC:
    """Constants for class Action.

    Attributes:
        mb_min (Union[Unset, ActionZ]): Type safe element selector for class Action.
        mb_history (Union[Unset, str]):
        mb_all (Union[Unset, ActionZ]): Type safe element selector for class Action.
        mb_doc_version (Union[Unset, str]):
        mb_all_members (Union[Unset, str]):
        mb_workflow (Union[Unset, str]):
    """

    mb_min: Union[Unset, "ActionZ"] = UNSET
    mb_history: Union[Unset, str] = UNSET
    mb_all: Union[Unset, "ActionZ"] = UNSET
    mb_doc_version: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_workflow: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_min: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_min, Unset):
            mb_min = self.mb_min.to_dict()

        mb_history = self.mb_history

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_doc_version = self.mb_doc_version

        mb_all_members = self.mb_all_members

        mb_workflow = self.mb_workflow

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_min is not UNSET:
            field_dict["mbMin"] = mb_min
        if mb_history is not UNSET:
            field_dict["mbHistory"] = mb_history
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_doc_version is not UNSET:
            field_dict["mbDocVersion"] = mb_doc_version
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_workflow is not UNSET:
            field_dict["mbWorkflow"] = mb_workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_z import ActionZ

        d = src_dict.copy()
        _mb_min = d.pop("mbMin", UNSET)
        mb_min: Union[Unset, ActionZ]
        if isinstance(_mb_min, Unset):
            mb_min = UNSET
        else:
            mb_min = ActionZ.from_dict(_mb_min)

        mb_history = d.pop("mbHistory", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, ActionZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = ActionZ.from_dict(_mb_all)

        mb_doc_version = d.pop("mbDocVersion", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_workflow = d.pop("mbWorkflow", UNSET)

        action_c = cls(
            mb_min=mb_min,
            mb_history=mb_history,
            mb_all=mb_all,
            mb_doc_version=mb_doc_version,
            mb_all_members=mb_all_members,
            mb_workflow=mb_workflow,
        )

        action_c.additional_properties = d
        return action_c

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
