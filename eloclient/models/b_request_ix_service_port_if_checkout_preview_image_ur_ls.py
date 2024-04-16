from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.preview_image_info import PreviewImageInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutPreviewImageURLs")


@_attrs_define
class BRequestIXServicePortIFCheckoutPreviewImageURLs:
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
        preview_image_info (Union[Unset, PreviewImageInfo]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    preview_image_info: Union[Unset, "PreviewImageInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        preview_image_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview_image_info, Unset):
            preview_image_info = self.preview_image_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if preview_image_info is not UNSET:
            field_dict["previewImageInfo"] = preview_image_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.preview_image_info import PreviewImageInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _preview_image_info = d.pop("previewImageInfo", UNSET)
        preview_image_info: Union[Unset, PreviewImageInfo]
        if isinstance(_preview_image_info, Unset):
            preview_image_info = UNSET
        else:
            preview_image_info = PreviewImageInfo.from_dict(_preview_image_info)

        b_request_ix_service_port_if_checkout_preview_image_ur_ls = cls(
            ci=ci,
            preview_image_info=preview_image_info,
        )

        b_request_ix_service_port_if_checkout_preview_image_ur_ls.additional_properties = d
        return b_request_ix_service_port_if_checkout_preview_image_ur_ls

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
