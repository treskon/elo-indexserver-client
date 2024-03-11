from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.substitution_z import SubstitutionZ


T = TypeVar("T", bound="SubstitutionC")


@_attrs_define
class SubstitutionC:
    """<p>
    Bit constants for members of {@link Substitution}
     </p>

        Attributes:
            mb_user_name (Union[Unset, str]): Member bit to select {@link Substitution#userName}
            mb_substitute_name (Union[Unset, str]): Member bit to select {@link Substitution#substituteName}
            mb_creator_name (Union[Unset, str]): Member bit to select {@link Substitution#creatorName}
            mb_substituion_periods (Union[Unset, str]): Member bit to select {@link Substitution#substitutionPeriods}
            mb_status (Union[Unset, str]): Member bit to select {@link Substitution#status}
            mb_lock_name (Union[Unset, str]): Member bit to select {@link Substitution#lockName}
            mb_substitute_type (Union[Unset, str]): Member bit to select {@link Substitution#substituteType}
            mb_all_members (Union[Unset, str]): Select all members
            mb_all (Union[Unset, SubstitutionZ]): This class encapsulates the constants of {@link SubstitutionC}
    """

    mb_user_name: Union[Unset, str] = UNSET
    mb_substitute_name: Union[Unset, str] = UNSET
    mb_creator_name: Union[Unset, str] = UNSET
    mb_substituion_periods: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_lock_name: Union[Unset, str] = UNSET
    mb_substitute_type: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_all: Union[Unset, "SubstitutionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_user_name = self.mb_user_name
        mb_substitute_name = self.mb_substitute_name
        mb_creator_name = self.mb_creator_name
        mb_substituion_periods = self.mb_substituion_periods
        mb_status = self.mb_status
        mb_lock_name = self.mb_lock_name
        mb_substitute_type = self.mb_substitute_type
        mb_all_members = self.mb_all_members
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if mb_substitute_name is not UNSET:
            field_dict["mbSubstituteName"] = mb_substitute_name
        if mb_creator_name is not UNSET:
            field_dict["mbCreatorName"] = mb_creator_name
        if mb_substituion_periods is not UNSET:
            field_dict["mbSubstituionPeriods"] = mb_substituion_periods
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_lock_name is not UNSET:
            field_dict["mbLockName"] = mb_lock_name
        if mb_substitute_type is not UNSET:
            field_dict["mbSubstituteType"] = mb_substitute_type
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.substitution_z import SubstitutionZ

        d = src_dict.copy()
        mb_user_name = d.pop("mbUserName", UNSET)

        mb_substitute_name = d.pop("mbSubstituteName", UNSET)

        mb_creator_name = d.pop("mbCreatorName", UNSET)

        mb_substituion_periods = d.pop("mbSubstituionPeriods", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_lock_name = d.pop("mbLockName", UNSET)

        mb_substitute_type = d.pop("mbSubstituteType", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, SubstitutionZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = SubstitutionZ.from_dict(_mb_all)

        substitution_c = cls(
            mb_user_name=mb_user_name,
            mb_substitute_name=mb_substitute_name,
            mb_creator_name=mb_creator_name,
            mb_substituion_periods=mb_substituion_periods,
            mb_status=mb_status,
            mb_lock_name=mb_lock_name,
            mb_substitute_type=mb_substitute_type,
            mb_all_members=mb_all_members,
            mb_all=mb_all,
        )

        substitution_c.additional_properties = d
        return substitution_c

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
