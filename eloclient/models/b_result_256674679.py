from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reminder import Reminder


T = TypeVar("T", bound="BResult256674679")


@_attrs_define
class BResult256674679:
    """
    Attributes:
        result (Union[Unset, Reminder]):
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, "Reminder"] = UNSET
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
        from ..models.reminder import Reminder

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, Reminder]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Reminder.from_dict(_result)

        exception = d.pop("exception", UNSET)

        b_result_256674679 = cls(
            result=result,
            exception=exception,
        )

        b_result_256674679.additional_properties = d
        return b_result_256674679

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
