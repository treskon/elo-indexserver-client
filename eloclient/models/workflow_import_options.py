from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowImportOptions")


@_attrs_define
class WorkflowImportOptions:
    """Options for the workflow import.

    Attributes:
        replace_missing_user_by_user_id (Union[Unset, str]): If this variable is set, the missing user is replaced by
            this user.
            Otherwise the missing user
             will be created using a random password.
    """

    replace_missing_user_by_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        replace_missing_user_by_user_id = self.replace_missing_user_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replace_missing_user_by_user_id is not UNSET:
            field_dict["replaceMissingUserByUserId"] = replace_missing_user_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        replace_missing_user_by_user_id = d.pop("replaceMissingUserByUserId", UNSET)

        workflow_import_options = cls(
            replace_missing_user_by_user_id=replace_missing_user_by_user_id,
        )

        workflow_import_options.additional_properties = d
        return workflow_import_options

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
