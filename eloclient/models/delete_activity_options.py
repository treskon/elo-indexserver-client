from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteActivityOptions")


@_attrs_define
class DeleteActivityOptions:
    """This class defines options for the API function deleteActivity.

    Attributes:
        delete_finally (Union[Unset, bool]): Delete activity finally.
            The database information for the activity is deleted, if this member
             is true. Otherwise the Activity.backAt is set to the current date.
    """

    delete_finally: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delete_finally = self.delete_finally

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_finally is not UNSET:
            field_dict["deleteFinally"] = delete_finally

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delete_finally = d.pop("deleteFinally", UNSET)

        delete_activity_options = cls(
            delete_finally=delete_finally,
        )

        delete_activity_options.additional_properties = d
        return delete_activity_options

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
