from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.find_background_thread_options import FindBackgroundThreadOptions


T = TypeVar("T", bound="BRequestIXServicePortIFFindBackgroundThreads")


@_attrs_define
class BRequestIXServicePortIFFindBackgroundThreads:
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
        find_background_thread_options (Union[Unset, FindBackgroundThreadOptions]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    find_background_thread_options: Union[Unset, "FindBackgroundThreadOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        find_background_thread_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_background_thread_options, Unset):
            find_background_thread_options = self.find_background_thread_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if find_background_thread_options is not UNSET:
            field_dict["findBackgroundThreadOptions"] = find_background_thread_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.find_background_thread_options import FindBackgroundThreadOptions

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _find_background_thread_options = d.pop("findBackgroundThreadOptions", UNSET)
        find_background_thread_options: Union[Unset, FindBackgroundThreadOptions]
        if isinstance(_find_background_thread_options, Unset):
            find_background_thread_options = UNSET
        else:
            find_background_thread_options = FindBackgroundThreadOptions.from_dict(_find_background_thread_options)

        b_request_ix_service_port_if_find_background_threads = cls(
            ci=ci,
            find_background_thread_options=find_background_thread_options,
        )

        b_request_ix_service_port_if_find_background_threads.additional_properties = d
        return b_request_ix_service_port_if_find_background_threads

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
