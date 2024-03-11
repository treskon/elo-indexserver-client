from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IXExceptionData")


@_attrs_define
class IXExceptionData:
    """This class describes an exception that can occur during the execution of an Index server function.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            call_id (Union[Unset, str]): String containing the ClientInfo.callId for the ClientInfo object.
                This is given to the function which
                 triggered/caused the error.
            details (Union[Unset, str]): Detail text for the exception.
            exception_type (Union[Unset, int]): This is the type of exception. This is one of the constants from
                IXExceptionC.
            message (Union[Unset, str]): The error message text for the exception.
            ticket (Union[Unset, str]): Ticket given to the function.
    """

    call_id: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    exception_type: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    ticket: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_id = self.call_id
        details = self.details
        exception_type = self.exception_type
        message = self.message
        ticket = self.ticket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_id is not UNSET:
            field_dict["callId"] = call_id
        if details is not UNSET:
            field_dict["details"] = details
        if exception_type is not UNSET:
            field_dict["exceptionType"] = exception_type
        if message is not UNSET:
            field_dict["message"] = message
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        call_id = d.pop("callId", UNSET)

        details = d.pop("details", UNSET)

        exception_type = d.pop("exceptionType", UNSET)

        message = d.pop("message", UNSET)

        ticket = d.pop("ticket", UNSET)

        ix_exception_data = cls(
            call_id=call_id,
            details=details,
            exception_type=exception_type,
            message=message,
            ticket=ticket,
        )

        ix_exception_data.additional_properties = d
        return ix_exception_data

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
