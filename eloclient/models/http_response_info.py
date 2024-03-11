from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpResponseInfo")


@_attrs_define
class HttpResponseInfo:
    """This class contains information for the HttpServletResponse object to be sent by the Indexserver servlet.

    Attributes:
        content_type (Union[Unset, str]): Content type header. HttpServletResponse.
            setContentType()
        response_string (Union[Unset, str]): Response text. Written to HttpServletResponse.
            getOutputStream()
    """

    content_type: Union[Unset, str] = UNSET
    response_string: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type = self.content_type
        response_string = self.response_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if response_string is not UNSET:
            field_dict["responseString"] = response_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = d.pop("contentType", UNSET)

        response_string = d.pop("responseString", UNSET)

        http_response_info = cls(
            content_type=content_type,
            response_string=response_string,
        )

        http_response_info.additional_properties = d
        return http_response_info

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
