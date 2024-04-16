from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.query_job_protocol_info import QueryJobProtocolInfo


T = TypeVar("T", bound="BRequestIXServicePortIFQueryJobProtocol")


@_attrs_define
class BRequestIXServicePortIFQueryJobProtocol:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        query_job_protocol_info (Union[Unset, QueryJobProtocolInfo]): This class contains the parameters for the
            interface function
            {@link IXServicePortIF#queryJobProtocol(ClientInfo, QueryJobProtocolInfo)}.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    query_job_protocol_info: Union[Unset, "QueryJobProtocolInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        query_job_protocol_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_job_protocol_info, Unset):
            query_job_protocol_info = self.query_job_protocol_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if query_job_protocol_info is not UNSET:
            field_dict["queryJobProtocolInfo"] = query_job_protocol_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.query_job_protocol_info import QueryJobProtocolInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _query_job_protocol_info = d.pop("queryJobProtocolInfo", UNSET)
        query_job_protocol_info: Union[Unset, QueryJobProtocolInfo]
        if isinstance(_query_job_protocol_info, Unset):
            query_job_protocol_info = UNSET
        else:
            query_job_protocol_info = QueryJobProtocolInfo.from_dict(_query_job_protocol_info)

        b_request_ix_service_port_if_query_job_protocol = cls(
            ci=ci,
            query_job_protocol_info=query_job_protocol_info,
        )

        b_request_ix_service_port_if_query_job_protocol.additional_properties = d
        return b_request_ix_service_port_if_query_job_protocol

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
