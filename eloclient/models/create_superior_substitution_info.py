from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSuperiorSubstitutionInfo")


@_attrs_define
class CreateSuperiorSubstitutionInfo:
    """Define how a superior substitution is created.
    <p>
     A superior has the right to substitute any of its subordinates.
     </p>
     <p>
     A superior substitution has {@link SubstitutionSettings#superiorSubstitution} set to true.
     </p>

        Attributes:
            user_to_substitute_id (Union[Unset, int]): <p>
                User to be substituted by superior.
                 </p>
                 <p>
                 This value is ignored if {@link #userToSubstituteName} is set.
                 </p>
            user_to_substitute_name (Union[Unset, str]): <p>
                User to be substituted by superior.
                 </p>
                 <p>
                 {@link #userToSubstituteId} is ignored if this member is set.
                 </p>
    """

    user_to_substitute_id: Union[Unset, int] = UNSET
    user_to_substitute_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_to_substitute_id = self.user_to_substitute_id

        user_to_substitute_name = self.user_to_substitute_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_to_substitute_id is not UNSET:
            field_dict["userToSubstituteId"] = user_to_substitute_id
        if user_to_substitute_name is not UNSET:
            field_dict["userToSubstituteName"] = user_to_substitute_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_to_substitute_id = d.pop("userToSubstituteId", UNSET)

        user_to_substitute_name = d.pop("userToSubstituteName", UNSET)

        create_superior_substitution_info = cls(
            user_to_substitute_id=user_to_substitute_id,
            user_to_substitute_name=user_to_substitute_name,
        )

        create_superior_substitution_info.additional_properties = d
        return create_superior_substitution_info

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
