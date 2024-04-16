from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.substitution import Substitution


T = TypeVar("T", bound="SubstitutionsResult")


@_attrs_define
class SubstitutionsResult:
    """Object returned by {@link IXServicePortIF#checkinSubstitutions}() and
    {@link IXServicePortIF#checkoutSubstitutions}().

        Attributes:
            substitution_guids (Union[Unset, List[str]]):
            substitutions (Union[Unset, List['Substitution']]):
    """

    substitution_guids: Union[Unset, List[str]] = UNSET
    substitutions: Union[Unset, List["Substitution"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substitution_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.substitution_guids, Unset):
            substitution_guids = self.substitution_guids

        substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitutions, Unset):
            substitutions = []
            for componentsschemas_list_of_substitution_item_data in self.substitutions:
                componentsschemas_list_of_substitution_item = componentsschemas_list_of_substitution_item_data.to_dict()
                substitutions.append(componentsschemas_list_of_substitution_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substitution_guids is not UNSET:
            field_dict["substitutionGuids"] = substitution_guids
        if substitutions is not UNSET:
            field_dict["substitutions"] = substitutions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.substitution import Substitution

        d = src_dict.copy()
        substitution_guids = cast(List[str], d.pop("substitutionGuids", UNSET))

        substitutions = []
        _substitutions = d.pop("substitutions", UNSET)
        for componentsschemas_list_of_substitution_item_data in _substitutions or []:
            componentsschemas_list_of_substitution_item = Substitution.from_dict(
                componentsschemas_list_of_substitution_item_data
            )

            substitutions.append(componentsschemas_list_of_substitution_item)

        substitutions_result = cls(
            substitution_guids=substitution_guids,
            substitutions=substitutions,
        )

        substitutions_result.additional_properties = d
        return substitutions_result

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
