from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSubstitutionsInfo")


@_attrs_define
class DeleteSubstitutionsInfo:
    """Define which substitutions should be deleted.

    Attributes:
        substitution_guids (Union[Unset, List[str]]):
    """

    substitution_guids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substitution_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.substitution_guids, Unset):
            substitution_guids = self.substitution_guids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substitution_guids is not UNSET:
            field_dict["substitutionGuids"] = substitution_guids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        substitution_guids = cast(List[str], d.pop("substitutionGuids", UNSET))

        delete_substitutions_info = cls(
            substitution_guids=substitution_guids,
        )

        delete_substitutions_info.additional_properties = d
        return delete_substitutions_info

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
