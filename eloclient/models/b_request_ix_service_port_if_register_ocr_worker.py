from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.ocr_worker import OcrWorker


T = TypeVar("T", bound="BRequestIXServicePortIFRegisterOcrWorker")


@_attrs_define
class BRequestIXServicePortIFRegisterOcrWorker:
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
        ocr_worker (Union[Unset, OcrWorker]): This class is used to describe an OCR worker process.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    ocr_worker: Union[Unset, "OcrWorker"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        ocr_worker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ocr_worker, Unset):
            ocr_worker = self.ocr_worker.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if ocr_worker is not UNSET:
            field_dict["ocrWorker"] = ocr_worker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.ocr_worker import OcrWorker

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _ocr_worker = d.pop("ocrWorker", UNSET)
        ocr_worker: Union[Unset, OcrWorker]
        if isinstance(_ocr_worker, Unset):
            ocr_worker = UNSET
        else:
            ocr_worker = OcrWorker.from_dict(_ocr_worker)

        b_request_ix_service_port_if_register_ocr_worker = cls(
            ci=ci,
            ocr_worker=ocr_worker,
        )

        b_request_ix_service_port_if_register_ocr_worker.additional_properties = d
        return b_request_ix_service_port_if_register_ocr_worker

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
