from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.invalidate_cache_info import InvalidateCacheInfo


T = TypeVar("T", bound="BRequestIXServicePortIFInvalidateCache2")


@_attrs_define
class BRequestIXServicePortIFInvalidateCache2:
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
        info (Union[Unset, InvalidateCacheInfo]): This class contains the parameters for the API function
            invalidateCache2
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    info: Union[Unset, "InvalidateCacheInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.invalidate_cache_info import InvalidateCacheInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _info = d.pop("info", UNSET)
        info: Union[Unset, InvalidateCacheInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = InvalidateCacheInfo.from_dict(_info)

        b_request_ix_service_port_if_invalidate_cache_2 = cls(
            ci=ci,
            info=info,
        )

        b_request_ix_service_port_if_invalidate_cache_2.additional_properties = d
        return b_request_ix_service_port_if_invalidate_cache_2

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
