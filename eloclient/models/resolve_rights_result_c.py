from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveRightsResultC")


@_attrs_define
class ResolveRightsResultC:
    """Constants for {@link ResolveRightsResult}.

    Attributes:
        substitution (Union[Unset, int]): Indicates that the user got the right by a substitution rule.
        direct (Union[Unset, int]): Indicates that the user got the right directly.
        inherited (Union[Unset, int]): Indicates that the user got the right by inheritance of a group.
    """

    substitution: Union[Unset, int] = UNSET
    direct: Union[Unset, int] = UNSET
    inherited: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substitution = self.substitution

        direct = self.direct

        inherited = self.inherited

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substitution is not UNSET:
            field_dict["SUBSTITUTION"] = substitution
        if direct is not UNSET:
            field_dict["DIRECT"] = direct
        if inherited is not UNSET:
            field_dict["INHERITED"] = inherited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        substitution = d.pop("SUBSTITUTION", UNSET)

        direct = d.pop("DIRECT", UNSET)

        inherited = d.pop("INHERITED", UNSET)

        resolve_rights_result_c = cls(
            substitution=substitution,
            direct=direct,
            inherited=inherited,
        )

        resolve_rights_result_c.additional_properties = d
        return resolve_rights_result_c

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
