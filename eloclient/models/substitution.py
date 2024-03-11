from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.substitution_period import SubstitutionPeriod
    from ..models.substitution_settings import SubstitutionSettings
    from ..models.substitution_status import SubstitutionStatus


T = TypeVar("T", bound="Substitution")


@_attrs_define
class Substitution:
    """A Substitution is used to create, update and read substitutions.

    Attributes:
        guid (Union[Unset, str]): <p>
            GUID of substitution
             </p>
             <p>
             A new substitution is saved if guid is empty on checkin. An existing substitution is updated if a guid is
            provided.
             </p>
        user_id (Union[Unset, int]): <p>
            The user or group which is substituted by this object.
             </p>
             <p>
             This variable is ignored when calling {@link IXServicePortIF#checkinSubstitutions} if {@link #userName} is set.
             </p>
        user_name (Union[Unset, str]): <p>
            The user or group which is substituted by this object.
             </p>
             <p>
             {@link #userId} is ignored if this member is set when calling {@link IXServicePortIF#checkinSubstitutions}.
             </p>
        substitute_id (Union[Unset, int]): <p>
            User or group to whom the substitution is directed.
             </p>
             <p>
             This variable is ignored when calling {@link IXServicePortIF#checkinSubstitutions} if {@link #substituteName}
            is
             set.
             </p>
        substitute_name (Union[Unset, str]): <p>
            User or group to whom the substitution is directed.
             </p>
             <p>
             {@link #substituteId} is ignored if this member is set when calling {@link
            IXServicePortIF#checkinSubstitutions}.
             </p>
        substitute_type (Union[Unset, int]): <p>
            Type of the substitute.
             </p>
             <p>
             Read-only, refers to {@link UserInfoC#TYPE_GROUP} or {@link UserInfoC#TYPE_USER}
             </p>
        creator_id (Union[Unset, int]): <p>
            User who created the Substitution. Read-only.
             </p>
        creator_name (Union[Unset, str]): <p>
            User who created the Substitution. Read-only.
             </p>
        access (Union[Unset, int]): The current users access rights for this Substitution. Returns a combination of
            AccessC.LUR_ constants. Read-only.
        groups_to_inherit_rights (Union[Unset, List[int]]):
        substitution_periods (Union[Unset, List['SubstitutionPeriod']]):
        settings (Union[Unset, SubstitutionSettings]): This class wraps various boolean settings and parameters for
            {@link Substitution}
        status (Union[Unset, SubstitutionStatus]): The substitution status is used to inform if a substitution is
            currently deactivated or activated.
            If activated, it
             also informs how it was activated (either by a {@link SubstitutionPeriod} or manually)
        forwarded_to (Union[Unset, str]): <p>
            If a substitution was forwarded to an other one, this references the {@link #guid} of the substitution it was
             forwarded to.
             </p>
             Read-only.
        forwarded_from (Union[Unset, str]): <p>
            If a substitution was forwarded to an other one, this references the {@link #guid} of the substitution it was
             forwarded from.
             </p>
             Read-only.
        message (Union[Unset, str]): Message to add to the substitution.
        lock_id (Union[Unset, int]): <p>
            User ID of the user that has locked the Substitution
             </p>
             <p>
             If -1, no lock is held. Read-only, ignored in {@link IXServicePortIF#checkinSubstitutions}
             </p>
        lock_name (Union[Unset, str]): <p>
            Name of the user that has locked the Substitution
             </p>
             <p>
             Read-only, ignored in {@link IXServicePortIF#checkinSubstitutions}
             </p>
        tstamp (Union[Unset, str]): Timestamp of last update. Read-only.
        tstampsync (Union[Unset, str]): Timestamp of last update. Read-only.
        forwarded_by (Union[Unset, List[int]]):
    """

    guid: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    substitute_id: Union[Unset, int] = UNSET
    substitute_name: Union[Unset, str] = UNSET
    substitute_type: Union[Unset, int] = UNSET
    creator_id: Union[Unset, int] = UNSET
    creator_name: Union[Unset, str] = UNSET
    access: Union[Unset, int] = UNSET
    groups_to_inherit_rights: Union[Unset, List[int]] = UNSET
    substitution_periods: Union[Unset, List["SubstitutionPeriod"]] = UNSET
    settings: Union[Unset, "SubstitutionSettings"] = UNSET
    status: Union[Unset, "SubstitutionStatus"] = UNSET
    forwarded_to: Union[Unset, str] = UNSET
    forwarded_from: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    lock_id: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    tstamp: Union[Unset, str] = UNSET
    tstampsync: Union[Unset, str] = UNSET
    forwarded_by: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        user_id = self.user_id
        user_name = self.user_name
        substitute_id = self.substitute_id
        substitute_name = self.substitute_name
        substitute_type = self.substitute_type
        creator_id = self.creator_id
        creator_name = self.creator_name
        access = self.access
        groups_to_inherit_rights: Union[Unset, List[int]] = UNSET
        if not isinstance(self.groups_to_inherit_rights, Unset):
            groups_to_inherit_rights = self.groups_to_inherit_rights

        substitution_periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitution_periods, Unset):
            substitution_periods = []
            for componentsschemas_list_of_substitution_period_item_data in self.substitution_periods:
                componentsschemas_list_of_substitution_period_item = (
                    componentsschemas_list_of_substitution_period_item_data.to_dict()
                )

                substitution_periods.append(componentsschemas_list_of_substitution_period_item)

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        forwarded_to = self.forwarded_to
        forwarded_from = self.forwarded_from
        message = self.message
        lock_id = self.lock_id
        lock_name = self.lock_name
        tstamp = self.tstamp
        tstampsync = self.tstampsync
        forwarded_by: Union[Unset, List[int]] = UNSET
        if not isinstance(self.forwarded_by, Unset):
            forwarded_by = self.forwarded_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if substitute_id is not UNSET:
            field_dict["substituteId"] = substitute_id
        if substitute_name is not UNSET:
            field_dict["substituteName"] = substitute_name
        if substitute_type is not UNSET:
            field_dict["substituteType"] = substitute_type
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name
        if access is not UNSET:
            field_dict["access"] = access
        if groups_to_inherit_rights is not UNSET:
            field_dict["groupsToInheritRights"] = groups_to_inherit_rights
        if substitution_periods is not UNSET:
            field_dict["substitutionPeriods"] = substitution_periods
        if settings is not UNSET:
            field_dict["settings"] = settings
        if status is not UNSET:
            field_dict["status"] = status
        if forwarded_to is not UNSET:
            field_dict["forwardedTo"] = forwarded_to
        if forwarded_from is not UNSET:
            field_dict["forwardedFrom"] = forwarded_from
        if message is not UNSET:
            field_dict["message"] = message
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if tstamp is not UNSET:
            field_dict["tstamp"] = tstamp
        if tstampsync is not UNSET:
            field_dict["tstampsync"] = tstampsync
        if forwarded_by is not UNSET:
            field_dict["forwardedBy"] = forwarded_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.substitution_period import SubstitutionPeriod
        from ..models.substitution_settings import SubstitutionSettings
        from ..models.substitution_status import SubstitutionStatus

        d = src_dict.copy()
        guid = d.pop("guid", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        substitute_id = d.pop("substituteId", UNSET)

        substitute_name = d.pop("substituteName", UNSET)

        substitute_type = d.pop("substituteType", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        creator_name = d.pop("creatorName", UNSET)

        access = d.pop("access", UNSET)

        groups_to_inherit_rights = cast(List[int], d.pop("groupsToInheritRights", UNSET))

        substitution_periods = []
        _substitution_periods = d.pop("substitutionPeriods", UNSET)
        for componentsschemas_list_of_substitution_period_item_data in _substitution_periods or []:
            componentsschemas_list_of_substitution_period_item = SubstitutionPeriod.from_dict(
                componentsschemas_list_of_substitution_period_item_data
            )

            substitution_periods.append(componentsschemas_list_of_substitution_period_item)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, SubstitutionSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = SubstitutionSettings.from_dict(_settings)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SubstitutionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubstitutionStatus.from_dict(_status)

        forwarded_to = d.pop("forwardedTo", UNSET)

        forwarded_from = d.pop("forwardedFrom", UNSET)

        message = d.pop("message", UNSET)

        lock_id = d.pop("lockId", UNSET)

        lock_name = d.pop("lockName", UNSET)

        tstamp = d.pop("tstamp", UNSET)

        tstampsync = d.pop("tstampsync", UNSET)

        forwarded_by = cast(List[int], d.pop("forwardedBy", UNSET))

        substitution = cls(
            guid=guid,
            user_id=user_id,
            user_name=user_name,
            substitute_id=substitute_id,
            substitute_name=substitute_name,
            substitute_type=substitute_type,
            creator_id=creator_id,
            creator_name=creator_name,
            access=access,
            groups_to_inherit_rights=groups_to_inherit_rights,
            substitution_periods=substitution_periods,
            settings=settings,
            status=status,
            forwarded_to=forwarded_to,
            forwarded_from=forwarded_from,
            message=message,
            lock_id=lock_id,
            lock_name=lock_name,
            tstamp=tstamp,
            tstampsync=tstampsync,
            forwarded_by=forwarded_by,
        )

        substitution.additional_properties = d
        return substitution

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
