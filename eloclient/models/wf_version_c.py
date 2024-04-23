from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFVersionC")


@_attrs_define
class WFVersionC:
    """Constants for WFVersion

    Attributes:
        ln_comment (Union[Unset, int]): Length of WFVersion.comment.
        ln_version (Union[Unset, int]): Length of WFVersion.version.
    """

    ln_comment: Union[Unset, int] = UNSET
    ln_version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_comment = self.ln_comment

        ln_version = self.ln_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if ln_version is not UNSET:
            field_dict["lnVersion"] = ln_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_comment = d.pop("lnComment", UNSET)

        ln_version = d.pop("lnVersion", UNSET)

        wf_version_c = cls(
            ln_comment=ln_comment,
            ln_version=ln_version,
        )

        wf_version_c.additional_properties = d
        return wf_version_c

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
