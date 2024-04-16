from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFInternalReceiveEvents")


@_attrs_define
class BRequestIXServicePortIFInternalReceiveEvents:
    """
    Attributes:
        subs_id (Union[Unset, str]):
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
        timeout_millis (Union[Unset, str]):
    """

    subs_id: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    timeout_millis: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subs_id = self.subs_id

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        timeout_millis = self.timeout_millis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subs_id is not UNSET:
            field_dict["subsId"] = subs_id
        if ci is not UNSET:
            field_dict["ci"] = ci
        if timeout_millis is not UNSET:
            field_dict["timeoutMillis"] = timeout_millis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        subs_id = d.pop("subsId", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        timeout_millis = d.pop("timeoutMillis", UNSET)

        b_request_ix_service_port_if_internal_receive_events = cls(
            subs_id=subs_id,
            ci=ci,
            timeout_millis=timeout_millis,
        )

        b_request_ix_service_port_if_internal_receive_events.additional_properties = d
        return b_request_ix_service_port_if_internal_receive_events

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
