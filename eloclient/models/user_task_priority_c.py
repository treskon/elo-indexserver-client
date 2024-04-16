from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTaskPriorityC")


@_attrs_define
class UserTaskPriorityC:
    """
    Attributes:
        lowest (Union[Unset, int]): Lowest priority.
        min_ (Union[Unset, int]): Minimum value = highest priority of reminder and activity
        max_ (Union[Unset, int]): Maximum value = lowest priority of reminder and activity
        highest (Union[Unset, int]): Highest priority.
    """

    lowest: Union[Unset, int] = UNSET
    min_: Union[Unset, int] = UNSET
    max_: Union[Unset, int] = UNSET
    highest: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lowest = self.lowest

        min_ = self.min_

        max_ = self.max_

        highest = self.highest

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lowest is not UNSET:
            field_dict["LOWEST"] = lowest
        if min_ is not UNSET:
            field_dict["MIN"] = min_
        if max_ is not UNSET:
            field_dict["MAX"] = max_
        if highest is not UNSET:
            field_dict["HIGHEST"] = highest

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lowest = d.pop("LOWEST", UNSET)

        min_ = d.pop("MIN", UNSET)

        max_ = d.pop("MAX", UNSET)

        highest = d.pop("HIGHEST", UNSET)

        user_task_priority_c = cls(
            lowest=lowest,
            min_=min_,
            max_=max_,
            highest=highest,
        )

        user_task_priority_c.additional_properties = d
        return user_task_priority_c

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
