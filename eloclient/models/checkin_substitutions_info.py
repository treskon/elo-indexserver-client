from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.substitution import Substitution


T = TypeVar("T", bound="CheckinSubstitutionsInfo")


@_attrs_define
class CheckinSubstitutionsInfo:
    """Object to define substitutions to be checked in.
    <p>
     Substitutions which do not have a {@link Substitution#guid} are new substitutions. If a
     {@link Substitution#guid} is set, the corresponding substitution is updated.
     </p>

        Attributes:
            substitutions (Union[Unset, List['Substitution']]):
    """

    substitutions: Union[Unset, List["Substitution"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitutions, Unset):
            substitutions = []
            for componentsschemas_list_of_substitution_item_data in self.substitutions:
                componentsschemas_list_of_substitution_item = componentsschemas_list_of_substitution_item_data.to_dict()
                substitutions.append(componentsschemas_list_of_substitution_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substitutions is not UNSET:
            field_dict["substitutions"] = substitutions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.substitution import Substitution

        d = src_dict.copy()
        substitutions = []
        _substitutions = d.pop("substitutions", UNSET)
        for componentsschemas_list_of_substitution_item_data in _substitutions or []:
            componentsschemas_list_of_substitution_item = Substitution.from_dict(
                componentsschemas_list_of_substitution_item_data
            )

            substitutions.append(componentsschemas_list_of_substitution_item)

        checkin_substitutions_info = cls(
            substitutions=substitutions,
        )

        checkin_substitutions_info.additional_properties = d
        return checkin_substitutions_info

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
