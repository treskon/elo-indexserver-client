from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_document_hash_result import ComputeDocumentHashResult


T = TypeVar("T", bound="BResult847213937")


@_attrs_define
class BResult847213937:
    """
    Attributes:
        result (Union[Unset, ComputeDocumentHashResult]): This class provides the result data computed by
            {@link IXServicePortIF#computeDocumentHash(ClientInfo, ComputeDocumentHashInfo)}.
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, "ComputeDocumentHashResult"] = UNSET
    exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        exception = self.exception

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_document_hash_result import ComputeDocumentHashResult

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, ComputeDocumentHashResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ComputeDocumentHashResult.from_dict(_result)

        exception = d.pop("exception", UNSET)

        b_result_847213937 = cls(
            result=result,
            exception=exception,
        )

        b_result_847213937.additional_properties = d
        return b_result_847213937

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
