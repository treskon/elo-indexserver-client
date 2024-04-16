from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcrResultQueryLanguages")


@_attrs_define
class OcrResultQueryLanguages:
    """This class contains the result of a OcrInfoQueryLanguages request.

    Attributes:
        internal_langs (Union[Unset, List[str]]):
        external_langs (Union[Unset, List[str]]):
    """

    internal_langs: Union[Unset, List[str]] = UNSET
    external_langs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.internal_langs, Unset):
            internal_langs = self.internal_langs

        external_langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.external_langs, Unset):
            external_langs = self.external_langs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internal_langs is not UNSET:
            field_dict["internalLangs"] = internal_langs
        if external_langs is not UNSET:
            field_dict["externalLangs"] = external_langs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        internal_langs = cast(List[str], d.pop("internalLangs", UNSET))

        external_langs = cast(List[str], d.pop("externalLangs", UNSET))

        ocr_result_query_languages = cls(
            internal_langs=internal_langs,
            external_langs=external_langs,
        )

        ocr_result_query_languages.additional_properties = d
        return ocr_result_query_languages

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
