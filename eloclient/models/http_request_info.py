from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="HttpRequestInfo")


@_attrs_define
class HttpRequestInfo:
    """This class contains information from the HttpServletRequest received by the Indexserver servlet

    Attributes:
        headers (Union[Unset, List['KeyValue']]):
        request_url (Union[Unset, str]): Value of the request URL. HttpServletRequest.
            getRequestURL()
        request_params (Union[Unset, List['KeyValue']]):
        request_uri (Union[Unset, str]): Value of the request URI. HttpServletRequest.
            getRequestURI()
        cookies (Union[Unset, List['KeyValue']]):
    """

    headers: Union[Unset, List["KeyValue"]] = UNSET
    request_url: Union[Unset, str] = UNSET
    request_params: Union[Unset, List["KeyValue"]] = UNSET
    request_uri: Union[Unset, str] = UNSET
    cookies: Union[Unset, List["KeyValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        request_url = self.request_url

        request_params: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.request_params, Unset):
            request_params = []
            for request_params_item_data in self.request_params:
                request_params_item = request_params_item_data.to_dict()
                request_params.append(request_params_item)

        request_uri = self.request_uri

        cookies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cookies, Unset):
            cookies = []
            for cookies_item_data in self.cookies:
                cookies_item = cookies_item_data.to_dict()
                cookies.append(cookies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if request_url is not UNSET:
            field_dict["requestURL"] = request_url
        if request_params is not UNSET:
            field_dict["requestParams"] = request_params
        if request_uri is not UNSET:
            field_dict["requestURI"] = request_uri
        if cookies is not UNSET:
            field_dict["cookies"] = cookies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        headers = []
        _headers = d.pop("headers", UNSET)
        for headers_item_data in _headers or []:
            headers_item = KeyValue.from_dict(headers_item_data)

            headers.append(headers_item)

        request_url = d.pop("requestURL", UNSET)

        request_params = []
        _request_params = d.pop("requestParams", UNSET)
        for request_params_item_data in _request_params or []:
            request_params_item = KeyValue.from_dict(request_params_item_data)

            request_params.append(request_params_item)

        request_uri = d.pop("requestURI", UNSET)

        cookies = []
        _cookies = d.pop("cookies", UNSET)
        for cookies_item_data in _cookies or []:
            cookies_item = KeyValue.from_dict(cookies_item_data)

            cookies.append(cookies_item)

        http_request_info = cls(
            headers=headers,
            request_url=request_url,
            request_params=request_params,
            request_uri=request_uri,
            cookies=cookies,
        )

        http_request_info.additional_properties = d
        return http_request_info

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
