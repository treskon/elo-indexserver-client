from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubstitutionDataC")


@_attrs_define
class SubstitutionDataC:
    """<p>
    Bit constants which mirror the database classes.
     </p>
     <i>For internal use only. Use {@link SubstitutionC} instead.</i>

        Attributes:
            mb_guid (Union[Unset, str]): DB column referenced by {@link Substitution#guid}
            mb_user_id (Union[Unset, str]): DB column referenced by {@link Substitution#userId} and {@link
                Substitution#userName}
            mb_substitute_id (Union[Unset, str]): DB column referenced by {@link Substitution#substituteId} and {@link
                Substitution#substituteName}
            mb_creator_id (Union[Unset, str]): DB column referenced by {@link Substitution#creatorId} and {@link
                Substitution#creatorName}
            mb_settings (Union[Unset, str]): DB column referenced by {@link Substitution#settings}
            mb_groups_to_inherit_rights (Union[Unset, str]): DB column referenced by {@link
                Substitution#groupsToInheritRights}
            mb_forwarded_to (Union[Unset, str]): DB column referenced by {@link Substitution#forwardedTo}
            mb_forwarded_from (Union[Unset, str]): DB column referenced by {@link Substitution#forwardedFrom}
            mb_message (Union[Unset, str]): DB column referenced by {@link Substitution#message}
            mb_lock_id (Union[Unset, str]): DB column referenced by {@link Substitution#lockId} and {@link
                Substitution#lockName}
            mb_tstamp (Union[Unset, str]): DB column referenced by {@link Substitution#tstamp}
            mb_tstampsync (Union[Unset, str]): DB column referenced by {@link Substitution#tstampsync}
            mb_forwarded_by (Union[Unset, str]): DB column referenced by {@link Substitution#forwardedBy}
            mb_all_members_db (Union[Unset, str]): For internal use only
            ln_guid (Union[Unset, int]): Max length of DB column {@link #mbGuid}
            ln_groups_to_inherit_rights (Union[Unset, int]): Max length of DB column {@link #mbGroupsToInheritRights}
            ln_forwarded_to (Union[Unset, int]): Max length of DB column {@link #mbForwardedTo}
            ln_forwarded_from (Union[Unset, int]): Max length of DB column {@link #mbForwardedFrom}
            ln_message (Union[Unset, int]): Max length of DB column {@link #mbMessage}
            ln_tstamp (Union[Unset, int]): Max length of DB column {@link #mbTstamp}
            ln_tstampsync (Union[Unset, int]): Max length of DB column {@link #mbTstampsync}
            ln_forwarded_by (Union[Unset, int]): Max length of DB column {@link #mbForwardedBy}
    """

    mb_guid: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_substitute_id: Union[Unset, str] = UNSET
    mb_creator_id: Union[Unset, str] = UNSET
    mb_settings: Union[Unset, str] = UNSET
    mb_groups_to_inherit_rights: Union[Unset, str] = UNSET
    mb_forwarded_to: Union[Unset, str] = UNSET
    mb_forwarded_from: Union[Unset, str] = UNSET
    mb_message: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_tstamp: Union[Unset, str] = UNSET
    mb_tstampsync: Union[Unset, str] = UNSET
    mb_forwarded_by: Union[Unset, str] = UNSET
    mb_all_members_db: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    ln_groups_to_inherit_rights: Union[Unset, int] = UNSET
    ln_forwarded_to: Union[Unset, int] = UNSET
    ln_forwarded_from: Union[Unset, int] = UNSET
    ln_message: Union[Unset, int] = UNSET
    ln_tstamp: Union[Unset, int] = UNSET
    ln_tstampsync: Union[Unset, int] = UNSET
    ln_forwarded_by: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_guid = self.mb_guid
        mb_user_id = self.mb_user_id
        mb_substitute_id = self.mb_substitute_id
        mb_creator_id = self.mb_creator_id
        mb_settings = self.mb_settings
        mb_groups_to_inherit_rights = self.mb_groups_to_inherit_rights
        mb_forwarded_to = self.mb_forwarded_to
        mb_forwarded_from = self.mb_forwarded_from
        mb_message = self.mb_message
        mb_lock_id = self.mb_lock_id
        mb_tstamp = self.mb_tstamp
        mb_tstampsync = self.mb_tstampsync
        mb_forwarded_by = self.mb_forwarded_by
        mb_all_members_db = self.mb_all_members_db
        ln_guid = self.ln_guid
        ln_groups_to_inherit_rights = self.ln_groups_to_inherit_rights
        ln_forwarded_to = self.ln_forwarded_to
        ln_forwarded_from = self.ln_forwarded_from
        ln_message = self.ln_message
        ln_tstamp = self.ln_tstamp
        ln_tstampsync = self.ln_tstampsync
        ln_forwarded_by = self.ln_forwarded_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_substitute_id is not UNSET:
            field_dict["mbSubstituteId"] = mb_substitute_id
        if mb_creator_id is not UNSET:
            field_dict["mbCreatorId"] = mb_creator_id
        if mb_settings is not UNSET:
            field_dict["mbSettings"] = mb_settings
        if mb_groups_to_inherit_rights is not UNSET:
            field_dict["mbGroupsToInheritRights"] = mb_groups_to_inherit_rights
        if mb_forwarded_to is not UNSET:
            field_dict["mbForwardedTo"] = mb_forwarded_to
        if mb_forwarded_from is not UNSET:
            field_dict["mbForwardedFrom"] = mb_forwarded_from
        if mb_message is not UNSET:
            field_dict["mbMessage"] = mb_message
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_tstamp is not UNSET:
            field_dict["mbTstamp"] = mb_tstamp
        if mb_tstampsync is not UNSET:
            field_dict["mbTstampsync"] = mb_tstampsync
        if mb_forwarded_by is not UNSET:
            field_dict["mbForwardedBy"] = mb_forwarded_by
        if mb_all_members_db is not UNSET:
            field_dict["mbAllMembersDB"] = mb_all_members_db
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if ln_groups_to_inherit_rights is not UNSET:
            field_dict["lnGroupsToInheritRights"] = ln_groups_to_inherit_rights
        if ln_forwarded_to is not UNSET:
            field_dict["lnForwardedTo"] = ln_forwarded_to
        if ln_forwarded_from is not UNSET:
            field_dict["lnForwardedFrom"] = ln_forwarded_from
        if ln_message is not UNSET:
            field_dict["lnMessage"] = ln_message
        if ln_tstamp is not UNSET:
            field_dict["lnTstamp"] = ln_tstamp
        if ln_tstampsync is not UNSET:
            field_dict["lnTstampsync"] = ln_tstampsync
        if ln_forwarded_by is not UNSET:
            field_dict["lnForwardedBy"] = ln_forwarded_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_guid = d.pop("mbGuid", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_substitute_id = d.pop("mbSubstituteId", UNSET)

        mb_creator_id = d.pop("mbCreatorId", UNSET)

        mb_settings = d.pop("mbSettings", UNSET)

        mb_groups_to_inherit_rights = d.pop("mbGroupsToInheritRights", UNSET)

        mb_forwarded_to = d.pop("mbForwardedTo", UNSET)

        mb_forwarded_from = d.pop("mbForwardedFrom", UNSET)

        mb_message = d.pop("mbMessage", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_tstamp = d.pop("mbTstamp", UNSET)

        mb_tstampsync = d.pop("mbTstampsync", UNSET)

        mb_forwarded_by = d.pop("mbForwardedBy", UNSET)

        mb_all_members_db = d.pop("mbAllMembersDB", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        ln_groups_to_inherit_rights = d.pop("lnGroupsToInheritRights", UNSET)

        ln_forwarded_to = d.pop("lnForwardedTo", UNSET)

        ln_forwarded_from = d.pop("lnForwardedFrom", UNSET)

        ln_message = d.pop("lnMessage", UNSET)

        ln_tstamp = d.pop("lnTstamp", UNSET)

        ln_tstampsync = d.pop("lnTstampsync", UNSET)

        ln_forwarded_by = d.pop("lnForwardedBy", UNSET)

        substitution_data_c = cls(
            mb_guid=mb_guid,
            mb_user_id=mb_user_id,
            mb_substitute_id=mb_substitute_id,
            mb_creator_id=mb_creator_id,
            mb_settings=mb_settings,
            mb_groups_to_inherit_rights=mb_groups_to_inherit_rights,
            mb_forwarded_to=mb_forwarded_to,
            mb_forwarded_from=mb_forwarded_from,
            mb_message=mb_message,
            mb_lock_id=mb_lock_id,
            mb_tstamp=mb_tstamp,
            mb_tstampsync=mb_tstampsync,
            mb_forwarded_by=mb_forwarded_by,
            mb_all_members_db=mb_all_members_db,
            ln_guid=ln_guid,
            ln_groups_to_inherit_rights=ln_groups_to_inherit_rights,
            ln_forwarded_to=ln_forwarded_to,
            ln_forwarded_from=ln_forwarded_from,
            ln_message=ln_message,
            ln_tstamp=ln_tstamp,
            ln_tstampsync=ln_tstampsync,
            ln_forwarded_by=ln_forwarded_by,
        )

        substitution_data_c.additional_properties = d
        return substitution_data_c

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
