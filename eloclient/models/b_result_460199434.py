from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity import Activity


T = TypeVar("T", bound="BResult460199434")


@_attrs_define
class BResult460199434:
    """
    Attributes:
        result (Union[Unset, Activity]): This class represents an activity.
            <p>
             An activity is a task delegated to an instance outside the ELO system. It is created when the
             task is sent to the instance and deleted, if it is received back. An activity defines a date for
             expecting the response, <code>dueDateIso</code>. At this date, the activity appears in the task
             list of the initiator. If the task is finished, the initiator sets the <code>backAt</code> member
             and the activity is closed.
             </p>
             <p>
             Activities can be used to observe a document or a folder. For each modification, a ELO_NOTIFY
             activity is created and displayed in the task list of the user that wants to observe the object.
             </p>
             <p>
             An activity object is an instance on an activity project. The project defines the properties the
             user can edit or select to provide more information to the task.
             </p>
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, "Activity"] = UNSET
    exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        exception = self.exception

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity import Activity

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, Activity]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Activity.from_dict(_result)

        exception = d.pop("exception", UNSET)

        b_result_460199434 = cls(
            result=result,
            exception=exception,
        )

        b_result_460199434.additional_properties = d
        return b_result_460199434

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
