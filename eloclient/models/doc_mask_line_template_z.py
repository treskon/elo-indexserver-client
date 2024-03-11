from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskLineTemplateZ")


@_attrs_define
class DocMaskLineTemplateZ:
    """This class encapsulates the constants of the DocMaskLineTemplateC class.

    Attributes:
        bset (Union[Unset, str]):
    """

    bset: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset = self.bset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset is not UNSET:
            field_dict["bset"] = bset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bset = d.pop("bset", UNSET)

        doc_mask_line_template_z = cls(
            bset=bset,
        )

        doc_mask_line_template_z.additional_properties = d
        return doc_mask_line_template_z

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