from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.b_stream_reference import BStreamReference
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestRawStreamServiceUpload")


@_attrs_define
class BRequestRawStreamServiceUpload:
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
        params (Union[Unset, List[str]]):
        is_ (Union[Unset, BStreamReference]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    params: Union[Unset, List[str]] = UNSET
    is_: Union[Unset, "BStreamReference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params

        is_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_, Unset):
            is_ = self.is_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if params is not UNSET:
            field_dict["params"] = params
        if is_ is not UNSET:
            field_dict["is"] = is_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.b_stream_reference import BStreamReference
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        params = cast(List[str], d.pop("params", UNSET))

        _is_ = d.pop("is", UNSET)
        is_: Union[Unset, BStreamReference]
        if isinstance(_is_, Unset):
            is_ = UNSET
        else:
            is_ = BStreamReference.from_dict(_is_)

        b_request_raw_stream_service_upload = cls(
            ci=ci,
            params=params,
            is_=is_,
        )

        b_request_raw_stream_service_upload.additional_properties = d
        return b_request_raw_stream_service_upload

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
