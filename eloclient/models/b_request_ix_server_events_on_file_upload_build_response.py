from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_version import DocVersion
    from ..models.http_request_info import HttpRequestInfo
    from ..models.http_response_info import HttpResponseInfo
    from ..models.ix_server_events_context import IXServerEventsContext


T = TypeVar("T", bound="BRequestIXServerEventsOnFileUploadBuildResponse")


@_attrs_define
class BRequestIXServerEventsOnFileUploadBuildResponse:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        dv (Union[Unset, DocVersion]): <p>
            Description: This class describes a document version, a document preview or a signature.
             </p>
             <p>
             Copyright: Copyright (c) 2002
             </p>
             <p>
             Organisation: ELO DIgital Office GmbH
             </p>
        file_name (Union[Unset, str]):
        request_info (Union[Unset, HttpRequestInfo]): This class contains information from the HttpServletRequest
            received by the Indexserver servlet
        response_info (Union[Unset, HttpResponseInfo]): This class contains information for the HttpServletResponse
            object to be sent by the Indexserver servlet.
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    dv: Union[Unset, "DocVersion"] = UNSET
    file_name: Union[Unset, str] = UNSET
    request_info: Union[Unset, "HttpRequestInfo"] = UNSET
    response_info: Union[Unset, "HttpResponseInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        dv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dv, Unset):
            dv = self.dv.to_dict()

        file_name = self.file_name
        request_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.request_info, Unset):
            request_info = self.request_info.to_dict()

        response_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response_info, Unset):
            response_info = self.response_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if dv is not UNSET:
            field_dict["dv"] = dv
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if request_info is not UNSET:
            field_dict["requestInfo"] = request_info
        if response_info is not UNSET:
            field_dict["responseInfo"] = response_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_version import DocVersion
        from ..models.http_request_info import HttpRequestInfo
        from ..models.http_response_info import HttpResponseInfo
        from ..models.ix_server_events_context import IXServerEventsContext

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _dv = d.pop("dv", UNSET)
        dv: Union[Unset, DocVersion]
        if isinstance(_dv, Unset):
            dv = UNSET
        else:
            dv = DocVersion.from_dict(_dv)

        file_name = d.pop("fileName", UNSET)

        _request_info = d.pop("requestInfo", UNSET)
        request_info: Union[Unset, HttpRequestInfo]
        if isinstance(_request_info, Unset):
            request_info = UNSET
        else:
            request_info = HttpRequestInfo.from_dict(_request_info)

        _response_info = d.pop("responseInfo", UNSET)
        response_info: Union[Unset, HttpResponseInfo]
        if isinstance(_response_info, Unset):
            response_info = UNSET
        else:
            response_info = HttpResponseInfo.from_dict(_response_info)

        b_request_ix_server_events_on_file_upload_build_response = cls(
            ec=ec,
            dv=dv,
            file_name=file_name,
            request_info=request_info,
            response_info=response_info,
        )

        b_request_ix_server_events_on_file_upload_build_response.additional_properties = d
        return b_request_ix_server_events_on_file_upload_build_response

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
