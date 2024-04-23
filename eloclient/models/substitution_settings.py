from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubstitutionSettings")


@_attrs_define
class SubstitutionSettings:
    """This class wraps various boolean settings and parameters for {@link Substitution}

    Attributes:
        can_access_postbox (Union[Unset, bool]): Define if the substitute can access the user's postbox.
        can_be_activated_manually (Union[Unset, bool]): Define if the substitution can be activated manually.
        activate_periods_automatically (Union[Unset, bool]): Define if substitution is activated automatically during a
            {@link SubstitutionPeriod}.
        superior_substitution (Union[Unset, bool]): <p>
            Defines if a substitution was created as a superior substitution with all rights set.
             </p>
             <p>
             This flag cannot be set by a user himself, but the superior and administrators.
             </p>
             <p>
             To create such a substitution, call {@link IXServicePortIF#createSuperiorSubstitution}.
             </p>
        is_activated_manually (Union[Unset, bool]): Is the substitution activated manually by calling
            {@link IXServicePortIF#activateSubstitution(de.elo.ix.client.ClientInfo, String, de.elo.ix.client.LockZ)}
             <i>Read-only</i>
        inherit_effective_principal_rights (Union[Unset, bool]): If set to true, the principals effective rights (with
            all groups and so on) are inherited to
            the substitute. The substitute then is able to do everything the principal could.
        can_access_personal_tasks (Union[Unset, bool]): Define if the substitute is allowed to find and access tasks
            (e.g.
            {@link WFDiagram},
             {@link Activity}, {@link Reminder}) which are assigned to the user ({@link Substitution#userId}
             himself and not a substituted group ({@link Substitution#groupsToInheritRights}.
        can_be_forwarded (Union[Unset, bool]): Define if the the substitution can be forwarded to an other user.
    """

    can_access_postbox: Union[Unset, bool] = UNSET
    can_be_activated_manually: Union[Unset, bool] = UNSET
    activate_periods_automatically: Union[Unset, bool] = UNSET
    superior_substitution: Union[Unset, bool] = UNSET
    is_activated_manually: Union[Unset, bool] = UNSET
    inherit_effective_principal_rights: Union[Unset, bool] = UNSET
    can_access_personal_tasks: Union[Unset, bool] = UNSET
    can_be_forwarded: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_access_postbox = self.can_access_postbox

        can_be_activated_manually = self.can_be_activated_manually

        activate_periods_automatically = self.activate_periods_automatically

        superior_substitution = self.superior_substitution

        is_activated_manually = self.is_activated_manually

        inherit_effective_principal_rights = self.inherit_effective_principal_rights

        can_access_personal_tasks = self.can_access_personal_tasks

        can_be_forwarded = self.can_be_forwarded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_access_postbox is not UNSET:
            field_dict["canAccessPostbox"] = can_access_postbox
        if can_be_activated_manually is not UNSET:
            field_dict["canBeActivatedManually"] = can_be_activated_manually
        if activate_periods_automatically is not UNSET:
            field_dict["activatePeriodsAutomatically"] = activate_periods_automatically
        if superior_substitution is not UNSET:
            field_dict["superiorSubstitution"] = superior_substitution
        if is_activated_manually is not UNSET:
            field_dict["isActivatedManually"] = is_activated_manually
        if inherit_effective_principal_rights is not UNSET:
            field_dict["inheritEffectivePrincipalRights"] = inherit_effective_principal_rights
        if can_access_personal_tasks is not UNSET:
            field_dict["canAccessPersonalTasks"] = can_access_personal_tasks
        if can_be_forwarded is not UNSET:
            field_dict["canBeForwarded"] = can_be_forwarded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_access_postbox = d.pop("canAccessPostbox", UNSET)

        can_be_activated_manually = d.pop("canBeActivatedManually", UNSET)

        activate_periods_automatically = d.pop("activatePeriodsAutomatically", UNSET)

        superior_substitution = d.pop("superiorSubstitution", UNSET)

        is_activated_manually = d.pop("isActivatedManually", UNSET)

        inherit_effective_principal_rights = d.pop("inheritEffectivePrincipalRights", UNSET)

        can_access_personal_tasks = d.pop("canAccessPersonalTasks", UNSET)

        can_be_forwarded = d.pop("canBeForwarded", UNSET)

        substitution_settings = cls(
            can_access_postbox=can_access_postbox,
            can_be_activated_manually=can_be_activated_manually,
            activate_periods_automatically=activate_periods_automatically,
            superior_substitution=superior_substitution,
            is_activated_manually=is_activated_manually,
            inherit_effective_principal_rights=inherit_effective_principal_rights,
            can_access_personal_tasks=can_access_personal_tasks,
            can_be_forwarded=can_be_forwarded,
        )

        substitution_settings.additional_properties = d
        return substitution_settings

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
