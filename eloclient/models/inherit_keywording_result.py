from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InheritKeywordingResult")


@_attrs_define
class InheritKeywordingResult:
    """Return values for server event {@link IXServerEvents#onInheritKeywording}.

    Attributes:
        apply_default (Union[Unset, InheritKeywordingResult]): Return values for server event {@link
            IXServerEvents#onInheritKeywording}.
        nothing (Union[Unset, InheritKeywordingResult]): Return values for server event {@link
            IXServerEvents#onInheritKeywording}.
        inherited (Union[Unset, InheritKeywordingResult]): Return values for server event {@link
            IXServerEvents#onInheritKeywording}.
    """

    apply_default: Union[Unset, "InheritKeywordingResult"] = UNSET
    nothing: Union[Unset, "InheritKeywordingResult"] = UNSET
    inherited: Union[Unset, "InheritKeywordingResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        apply_default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.apply_default, Unset):
            apply_default = self.apply_default.to_dict()

        nothing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nothing, Unset):
            nothing = self.nothing.to_dict()

        inherited: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inherited, Unset):
            inherited = self.inherited.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apply_default is not UNSET:
            field_dict["APPLY_DEFAULT"] = apply_default
        if nothing is not UNSET:
            field_dict["NOTHING"] = nothing
        if inherited is not UNSET:
            field_dict["INHERITED"] = inherited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _apply_default = d.pop("APPLY_DEFAULT", UNSET)
        apply_default: Union[Unset, InheritKeywordingResult]
        if isinstance(_apply_default, Unset):
            apply_default = UNSET
        else:
            apply_default = InheritKeywordingResult.from_dict(_apply_default)

        _nothing = d.pop("NOTHING", UNSET)
        nothing: Union[Unset, InheritKeywordingResult]
        if isinstance(_nothing, Unset):
            nothing = UNSET
        else:
            nothing = InheritKeywordingResult.from_dict(_nothing)

        _inherited = d.pop("INHERITED", UNSET)
        inherited: Union[Unset, InheritKeywordingResult]
        if isinstance(_inherited, Unset):
            inherited = UNSET
        else:
            inherited = InheritKeywordingResult.from_dict(_inherited)

        inherit_keywording_result = cls(
            apply_default=apply_default,
            nothing=nothing,
            inherited=inherited,
        )

        inherit_keywording_result.additional_properties = d
        return inherit_keywording_result

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
