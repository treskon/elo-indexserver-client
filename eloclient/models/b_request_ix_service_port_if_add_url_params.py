from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.url_params import UrlParams


T = TypeVar("T", bound="BRequestIXServicePortIFAddUrlParams")


@_attrs_define
class BRequestIXServicePortIFAddUrlParams:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        url (Union[Unset, str]):
        params (Union[Unset, UrlParams]): This class describes additional params for an upload or download URL.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    url: Union[Unset, str] = UNSET
    params: Union[Unset, "UrlParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        url = self.url
        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if url is not UNSET:
            field_dict["url"] = url
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.url_params import UrlParams

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        url = d.pop("url", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, UrlParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = UrlParams.from_dict(_params)

        b_request_ix_service_port_if_add_url_params = cls(
            ci=ci,
            url=url,
            params=params,
        )

        b_request_ix_service_port_if_add_url_params.additional_properties = d
        return b_request_ix_service_port_if_add_url_params

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
