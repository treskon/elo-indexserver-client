from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotifyServerInfo")


@_attrs_define
class NotifyServerInfo:
    """This class is used in IXServicePortIF.
    notifyServer to describe which operation(s) has (have) been processed by the
     client application.

        Attributes:
            scan_count (Union[Unset, int]): The number of scanned documents.
            ocr_count (Union[Unset, int]): The number of documents for which OCR was processed.
    """

    scan_count: Union[Unset, int] = UNSET
    ocr_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_count = self.scan_count
        ocr_count = self.ocr_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_count is not UNSET:
            field_dict["scanCount"] = scan_count
        if ocr_count is not UNSET:
            field_dict["ocrCount"] = ocr_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scan_count = d.pop("scanCount", UNSET)

        ocr_count = d.pop("ocrCount", UNSET)

        notify_server_info = cls(
            scan_count=scan_count,
            ocr_count=ocr_count,
        )

        notify_server_info.additional_properties = d
        return notify_server_info

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
