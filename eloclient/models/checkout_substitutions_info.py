from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutSubstitutionsInfo")


@_attrs_define
class CheckoutSubstitutionsInfo:
    """This object is used to define which substitutions should be returned by
    {@link IXServicePortIF#checkoutSubstitutions}.

     <p>
     The elements in one list are always search with an OR operation. If various list are provided,
     they are connected using OR (default) (set {@link #andOperator} to true to use AND operator)
     </p>

        Attributes:
            substitution_guids (Union[Unset, List[str]]):
            substitute_ids (Union[Unset, List[int]]):
            creator_names (Union[Unset, List[str]]):
            user_ids (Union[Unset, List[int]]):
            user_names (Union[Unset, List[str]]):
            creator_ids (Union[Unset, List[int]]):
            substitute_names (Union[Unset, List[str]]):
            include_substitutes_groups (Union[Unset, bool]): Include substitutions where {@link Substitution#substituteId}
                is set to the provided
                substitutes or any of their groups.
            and_operator (Union[Unset, bool]): Search for elements of different lists with OR operator (default) or AND (set
                value to true)
    """

    substitution_guids: Union[Unset, List[str]] = UNSET
    substitute_ids: Union[Unset, List[int]] = UNSET
    creator_names: Union[Unset, List[str]] = UNSET
    user_ids: Union[Unset, List[int]] = UNSET
    user_names: Union[Unset, List[str]] = UNSET
    creator_ids: Union[Unset, List[int]] = UNSET
    substitute_names: Union[Unset, List[str]] = UNSET
    include_substitutes_groups: Union[Unset, bool] = UNSET
    and_operator: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substitution_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.substitution_guids, Unset):
            substitution_guids = self.substitution_guids

        substitute_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.substitute_ids, Unset):
            substitute_ids = self.substitute_ids

        creator_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.creator_names, Unset):
            creator_names = self.creator_names

        user_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        user_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_names, Unset):
            user_names = self.user_names

        creator_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.creator_ids, Unset):
            creator_ids = self.creator_ids

        substitute_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.substitute_names, Unset):
            substitute_names = self.substitute_names

        include_substitutes_groups = self.include_substitutes_groups

        and_operator = self.and_operator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substitution_guids is not UNSET:
            field_dict["substitutionGuids"] = substitution_guids
        if substitute_ids is not UNSET:
            field_dict["substituteIds"] = substitute_ids
        if creator_names is not UNSET:
            field_dict["creatorNames"] = creator_names
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if user_names is not UNSET:
            field_dict["userNames"] = user_names
        if creator_ids is not UNSET:
            field_dict["creatorIds"] = creator_ids
        if substitute_names is not UNSET:
            field_dict["substituteNames"] = substitute_names
        if include_substitutes_groups is not UNSET:
            field_dict["includeSubstitutesGroups"] = include_substitutes_groups
        if and_operator is not UNSET:
            field_dict["andOperator"] = and_operator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        substitution_guids = cast(List[str], d.pop("substitutionGuids", UNSET))

        substitute_ids = cast(List[int], d.pop("substituteIds", UNSET))

        creator_names = cast(List[str], d.pop("creatorNames", UNSET))

        user_ids = cast(List[int], d.pop("userIds", UNSET))

        user_names = cast(List[str], d.pop("userNames", UNSET))

        creator_ids = cast(List[int], d.pop("creatorIds", UNSET))

        substitute_names = cast(List[str], d.pop("substituteNames", UNSET))

        include_substitutes_groups = d.pop("includeSubstitutesGroups", UNSET)

        and_operator = d.pop("andOperator", UNSET)

        checkout_substitutions_info = cls(
            substitution_guids=substitution_guids,
            substitute_ids=substitute_ids,
            creator_names=creator_names,
            user_ids=user_ids,
            user_names=user_names,
            creator_ids=creator_ids,
            substitute_names=substitute_names,
            include_substitutes_groups=include_substitutes_groups,
            and_operator=and_operator,
        )

        checkout_substitutions_info.additional_properties = d
        return checkout_substitutions_info

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
