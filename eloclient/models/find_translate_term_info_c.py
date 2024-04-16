from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindTranslateTermInfoC")


@_attrs_define
class FindTranslateTermInfoC:
    """Constants for {@link #FindTranslateTermInfo}.

    Attributes:
        all_translations_from_propery_files (Union[Unset, List[str]]):
    """

    all_translations_from_propery_files: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_translations_from_propery_files: Union[Unset, List[str]] = UNSET
        if not isinstance(self.all_translations_from_propery_files, Unset):
            all_translations_from_propery_files = self.all_translations_from_propery_files

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_translations_from_propery_files is not UNSET:
            field_dict["ALL_TRANSLATIONS_FROM_PROPERY_FILES"] = all_translations_from_propery_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        all_translations_from_propery_files = cast(List[str], d.pop("ALL_TRANSLATIONS_FROM_PROPERY_FILES", UNSET))

        find_translate_term_info_c = cls(
            all_translations_from_propery_files=all_translations_from_propery_files,
        )

        find_translate_term_info_c.additional_properties = d
        return find_translate_term_info_c

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
