from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteScriptResult")


@_attrs_define
class ExecuteScriptResult:
    """The function executeScript returns an object of this class to provide returned information or
    error information.

        Attributes:
            returned_string (Union[Unset, str]): Return value as string.
            error_message (Union[Unset, str]): Error message.
            error_column (Union[Unset, int]): Column where the error occured.
            error_line (Union[Unset, int]): Line where the error occured.
    """

    returned_string: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_column: Union[Unset, int] = UNSET
    error_line: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        returned_string = self.returned_string

        error_message = self.error_message

        error_column = self.error_column

        error_line = self.error_line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if returned_string is not UNSET:
            field_dict["returnedString"] = returned_string
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_column is not UNSET:
            field_dict["errorColumn"] = error_column
        if error_line is not UNSET:
            field_dict["errorLine"] = error_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        returned_string = d.pop("returnedString", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        error_column = d.pop("errorColumn", UNSET)

        error_line = d.pop("errorLine", UNSET)

        execute_script_result = cls(
            returned_string=returned_string,
            error_message=error_message,
            error_column=error_column,
            error_line=error_line,
        )

        execute_script_result.additional_properties = d
        return execute_script_result

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
