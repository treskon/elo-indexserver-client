from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.public_download_options import PublicDownloadOptions


T = TypeVar("T", bound="BRequestIXServicePortIFEditPublicDownloadUrls")


@_attrs_define
class BRequestIXServicePortIFEditPublicDownloadUrls:
    """
    Attributes:
        opts (Union[Unset, PublicDownloadOptions]): This class contains several options that are used to get the public
            downloads.
            <p>
             Copyright: Copyright (c) 2014
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
    """

    opts: Union[Unset, "PublicDownloadOptions"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opts, Unset):
            opts = self.opts.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opts is not UNSET:
            field_dict["opts"] = opts
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.public_download_options import PublicDownloadOptions

        d = src_dict.copy()
        _opts = d.pop("opts", UNSET)
        opts: Union[Unset, PublicDownloadOptions]
        if isinstance(_opts, Unset):
            opts = UNSET
        else:
            opts = PublicDownloadOptions.from_dict(_opts)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_edit_public_download_urls = cls(
            opts=opts,
            ci=ci,
        )

        b_request_ix_service_port_if_edit_public_download_urls.additional_properties = d
        return b_request_ix_service_port_if_edit_public_download_urls

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
