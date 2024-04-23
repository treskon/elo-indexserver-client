from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.ocr_info import OcrInfo


T = TypeVar("T", bound="BRequestIXServicePortIFProcessOcr")


@_attrs_define
class BRequestIXServicePortIFProcessOcr:
    """
    Attributes:
        ocr_info (Union[Unset, OcrInfo]): This class defines the properties of an OCR request.
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

    ocr_info: Union[Unset, "OcrInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ocr_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ocr_info, Unset):
            ocr_info = self.ocr_info.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocr_info is not UNSET:
            field_dict["ocrInfo"] = ocr_info
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.ocr_info import OcrInfo

        d = src_dict.copy()
        _ocr_info = d.pop("ocrInfo", UNSET)
        ocr_info: Union[Unset, OcrInfo]
        if isinstance(_ocr_info, Unset):
            ocr_info = UNSET
        else:
            ocr_info = OcrInfo.from_dict(_ocr_info)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_process_ocr = cls(
            ocr_info=ocr_info,
            ci=ci,
        )

        b_request_ix_service_port_if_process_ocr.additional_properties = d
        return b_request_ix_service_port_if_process_ocr

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
