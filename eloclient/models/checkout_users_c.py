from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_users_z import CheckoutUsersZ


T = TypeVar("T", bound="CheckoutUsersC")


@_attrs_define
class CheckoutUsersC:
    """<p>
    Constants to select users and groups
     </p>

        Attributes:
            bset_all_users_and_groups (Union[Unset, str]): Internal use only.
            by_ids (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            all_groups (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_groups_of_member (Union[Unset, str]): Internal use only.
            bset_members_of_group (Union[Unset, str]): Internal use only.
            bset_by_ids (Union[Unset, str]): Internal use only.
            members_of_group_recursive (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            members_of_group (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            users_of_group_recursive (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            all_users_and_groups (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            by_ids_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            members_of_group_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_users_of_subadmin (Union[Unset, str]): Internal use only.
            bset_users_of_superior (Union[Unset, str]): Internal use only.
            all_groups_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_all_users (Union[Unset, str]): Internal use only.
            bset_members_of_group_recursive (Union[Unset, str]): Internal use only.
            groups_of_member (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_all_groups (Union[Unset, str]): Internal use only.
            bset_users_of_group_recursive (Union[Unset, str]): Internal use only.
            nothing (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            all_users_and_groups_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            users_of_superior_or_subadmin (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_users_of_group (Union[Unset, str]): Internal use only.
            bset_nothing (Union[Unset, str]): Internal use only.
            bset_members_of_orgunit (Union[Unset, str]): Internal use only.
            bset_groups_of_member_recursive (Union[Unset, str]): Internal use only.
            bset_users_of_superior_or_subadmin (Union[Unset, str]): Internal use only.
            all_users_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            session_users_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_session_info (Union[Unset, str]): Internal use only.
            members_of_group_recursive_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            members_of_orgunit (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            all_users (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            users_of_group_recursive_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_subadmins (Union[Unset, str]): Internal use only.
            users_of_group_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            groups_of_member_recursive_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_select_mask (Union[Unset, str]): Internal use only.
            groups_of_member_raw (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            groups_of_member_recursive (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of
                CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            session_users (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            subadmins (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_effective_rights (Union[Unset, str]): Internal use only.
            bset_my_users (Union[Unset, str]): Internal use only.
            users_of_subadmin (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            users_of_superior (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            users_of_group (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    bset_all_users_and_groups: Union[Unset, str] = UNSET
    by_ids: Union[Unset, "CheckoutUsersZ"] = UNSET
    all_groups: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_groups_of_member: Union[Unset, str] = UNSET
    bset_members_of_group: Union[Unset, str] = UNSET
    bset_by_ids: Union[Unset, str] = UNSET
    members_of_group_recursive: Union[Unset, "CheckoutUsersZ"] = UNSET
    members_of_group: Union[Unset, "CheckoutUsersZ"] = UNSET
    users_of_group_recursive: Union[Unset, "CheckoutUsersZ"] = UNSET
    all_users_and_groups: Union[Unset, "CheckoutUsersZ"] = UNSET
    by_ids_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    members_of_group_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_users_of_subadmin: Union[Unset, str] = UNSET
    bset_users_of_superior: Union[Unset, str] = UNSET
    all_groups_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_all_users: Union[Unset, str] = UNSET
    bset_members_of_group_recursive: Union[Unset, str] = UNSET
    groups_of_member: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_all_groups: Union[Unset, str] = UNSET
    bset_users_of_group_recursive: Union[Unset, str] = UNSET
    nothing: Union[Unset, "CheckoutUsersZ"] = UNSET
    all_users_and_groups_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    users_of_superior_or_subadmin: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_users_of_group: Union[Unset, str] = UNSET
    bset_nothing: Union[Unset, str] = UNSET
    bset_members_of_orgunit: Union[Unset, str] = UNSET
    bset_groups_of_member_recursive: Union[Unset, str] = UNSET
    bset_users_of_superior_or_subadmin: Union[Unset, str] = UNSET
    all_users_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    session_users_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_session_info: Union[Unset, str] = UNSET
    members_of_group_recursive_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    members_of_orgunit: Union[Unset, "CheckoutUsersZ"] = UNSET
    all_users: Union[Unset, "CheckoutUsersZ"] = UNSET
    users_of_group_recursive_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_subadmins: Union[Unset, str] = UNSET
    users_of_group_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    groups_of_member_recursive_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_select_mask: Union[Unset, str] = UNSET
    groups_of_member_raw: Union[Unset, "CheckoutUsersZ"] = UNSET
    groups_of_member_recursive: Union[Unset, "CheckoutUsersZ"] = UNSET
    session_users: Union[Unset, "CheckoutUsersZ"] = UNSET
    subadmins: Union[Unset, "CheckoutUsersZ"] = UNSET
    bset_effective_rights: Union[Unset, str] = UNSET
    bset_my_users: Union[Unset, str] = UNSET
    users_of_subadmin: Union[Unset, "CheckoutUsersZ"] = UNSET
    users_of_superior: Union[Unset, "CheckoutUsersZ"] = UNSET
    users_of_group: Union[Unset, "CheckoutUsersZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_all_users_and_groups = self.bset_all_users_and_groups

        by_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_ids, Unset):
            by_ids = self.by_ids.to_dict()

        all_groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_groups, Unset):
            all_groups = self.all_groups.to_dict()

        bset_groups_of_member = self.bset_groups_of_member

        bset_members_of_group = self.bset_members_of_group

        bset_by_ids = self.bset_by_ids

        members_of_group_recursive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members_of_group_recursive, Unset):
            members_of_group_recursive = self.members_of_group_recursive.to_dict()

        members_of_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members_of_group, Unset):
            members_of_group = self.members_of_group.to_dict()

        users_of_group_recursive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_group_recursive, Unset):
            users_of_group_recursive = self.users_of_group_recursive.to_dict()

        all_users_and_groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_users_and_groups, Unset):
            all_users_and_groups = self.all_users_and_groups.to_dict()

        by_ids_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_ids_raw, Unset):
            by_ids_raw = self.by_ids_raw.to_dict()

        members_of_group_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members_of_group_raw, Unset):
            members_of_group_raw = self.members_of_group_raw.to_dict()

        bset_users_of_subadmin = self.bset_users_of_subadmin

        bset_users_of_superior = self.bset_users_of_superior

        all_groups_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_groups_raw, Unset):
            all_groups_raw = self.all_groups_raw.to_dict()

        bset_all_users = self.bset_all_users

        bset_members_of_group_recursive = self.bset_members_of_group_recursive

        groups_of_member: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups_of_member, Unset):
            groups_of_member = self.groups_of_member.to_dict()

        bset_all_groups = self.bset_all_groups

        bset_users_of_group_recursive = self.bset_users_of_group_recursive

        nothing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nothing, Unset):
            nothing = self.nothing.to_dict()

        all_users_and_groups_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_users_and_groups_raw, Unset):
            all_users_and_groups_raw = self.all_users_and_groups_raw.to_dict()

        users_of_superior_or_subadmin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_superior_or_subadmin, Unset):
            users_of_superior_or_subadmin = self.users_of_superior_or_subadmin.to_dict()

        bset_users_of_group = self.bset_users_of_group

        bset_nothing = self.bset_nothing

        bset_members_of_orgunit = self.bset_members_of_orgunit

        bset_groups_of_member_recursive = self.bset_groups_of_member_recursive

        bset_users_of_superior_or_subadmin = self.bset_users_of_superior_or_subadmin

        all_users_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_users_raw, Unset):
            all_users_raw = self.all_users_raw.to_dict()

        session_users_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_users_raw, Unset):
            session_users_raw = self.session_users_raw.to_dict()

        bset_session_info = self.bset_session_info

        members_of_group_recursive_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members_of_group_recursive_raw, Unset):
            members_of_group_recursive_raw = self.members_of_group_recursive_raw.to_dict()

        members_of_orgunit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members_of_orgunit, Unset):
            members_of_orgunit = self.members_of_orgunit.to_dict()

        all_users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_users, Unset):
            all_users = self.all_users.to_dict()

        users_of_group_recursive_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_group_recursive_raw, Unset):
            users_of_group_recursive_raw = self.users_of_group_recursive_raw.to_dict()

        bset_subadmins = self.bset_subadmins

        users_of_group_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_group_raw, Unset):
            users_of_group_raw = self.users_of_group_raw.to_dict()

        groups_of_member_recursive_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups_of_member_recursive_raw, Unset):
            groups_of_member_recursive_raw = self.groups_of_member_recursive_raw.to_dict()

        bset_select_mask = self.bset_select_mask

        groups_of_member_raw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups_of_member_raw, Unset):
            groups_of_member_raw = self.groups_of_member_raw.to_dict()

        groups_of_member_recursive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups_of_member_recursive, Unset):
            groups_of_member_recursive = self.groups_of_member_recursive.to_dict()

        session_users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_users, Unset):
            session_users = self.session_users.to_dict()

        subadmins: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subadmins, Unset):
            subadmins = self.subadmins.to_dict()

        bset_effective_rights = self.bset_effective_rights

        bset_my_users = self.bset_my_users

        users_of_subadmin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_subadmin, Unset):
            users_of_subadmin = self.users_of_subadmin.to_dict()

        users_of_superior: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_superior, Unset):
            users_of_superior = self.users_of_superior.to_dict()

        users_of_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_of_group, Unset):
            users_of_group = self.users_of_group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_all_users_and_groups is not UNSET:
            field_dict["bsetALL_USERS_AND_GROUPS"] = bset_all_users_and_groups
        if by_ids is not UNSET:
            field_dict["BY_IDS"] = by_ids
        if all_groups is not UNSET:
            field_dict["ALL_GROUPS"] = all_groups
        if bset_groups_of_member is not UNSET:
            field_dict["bsetGROUPS_OF_MEMBER"] = bset_groups_of_member
        if bset_members_of_group is not UNSET:
            field_dict["bsetMEMBERS_OF_GROUP"] = bset_members_of_group
        if bset_by_ids is not UNSET:
            field_dict["bsetBY_IDS"] = bset_by_ids
        if members_of_group_recursive is not UNSET:
            field_dict["MEMBERS_OF_GROUP_RECURSIVE"] = members_of_group_recursive
        if members_of_group is not UNSET:
            field_dict["MEMBERS_OF_GROUP"] = members_of_group
        if users_of_group_recursive is not UNSET:
            field_dict["USERS_OF_GROUP_RECURSIVE"] = users_of_group_recursive
        if all_users_and_groups is not UNSET:
            field_dict["ALL_USERS_AND_GROUPS"] = all_users_and_groups
        if by_ids_raw is not UNSET:
            field_dict["BY_IDS_RAW"] = by_ids_raw
        if members_of_group_raw is not UNSET:
            field_dict["MEMBERS_OF_GROUP_RAW"] = members_of_group_raw
        if bset_users_of_subadmin is not UNSET:
            field_dict["bsetUSERS_OF_SUBADMIN"] = bset_users_of_subadmin
        if bset_users_of_superior is not UNSET:
            field_dict["bsetUSERS_OF_SUPERIOR"] = bset_users_of_superior
        if all_groups_raw is not UNSET:
            field_dict["ALL_GROUPS_RAW"] = all_groups_raw
        if bset_all_users is not UNSET:
            field_dict["bsetALL_USERS"] = bset_all_users
        if bset_members_of_group_recursive is not UNSET:
            field_dict["bsetMEMBERS_OF_GROUP_RECURSIVE"] = bset_members_of_group_recursive
        if groups_of_member is not UNSET:
            field_dict["GROUPS_OF_MEMBER"] = groups_of_member
        if bset_all_groups is not UNSET:
            field_dict["bsetALL_GROUPS"] = bset_all_groups
        if bset_users_of_group_recursive is not UNSET:
            field_dict["bsetUSERS_OF_GROUP_RECURSIVE"] = bset_users_of_group_recursive
        if nothing is not UNSET:
            field_dict["NOTHING"] = nothing
        if all_users_and_groups_raw is not UNSET:
            field_dict["ALL_USERS_AND_GROUPS_RAW"] = all_users_and_groups_raw
        if users_of_superior_or_subadmin is not UNSET:
            field_dict["USERS_OF_SUPERIOR_OR_SUBADMIN"] = users_of_superior_or_subadmin
        if bset_users_of_group is not UNSET:
            field_dict["bsetUSERS_OF_GROUP"] = bset_users_of_group
        if bset_nothing is not UNSET:
            field_dict["bsetNOTHING"] = bset_nothing
        if bset_members_of_orgunit is not UNSET:
            field_dict["bsetMEMBERS_OF_ORGUNIT"] = bset_members_of_orgunit
        if bset_groups_of_member_recursive is not UNSET:
            field_dict["bsetGROUPS_OF_MEMBER_RECURSIVE"] = bset_groups_of_member_recursive
        if bset_users_of_superior_or_subadmin is not UNSET:
            field_dict["bsetUSERS_OF_SUPERIOR_OR_SUBADMIN"] = bset_users_of_superior_or_subadmin
        if all_users_raw is not UNSET:
            field_dict["ALL_USERS_RAW"] = all_users_raw
        if session_users_raw is not UNSET:
            field_dict["SESSION_USERS_RAW"] = session_users_raw
        if bset_session_info is not UNSET:
            field_dict["bsetSESSION_INFO"] = bset_session_info
        if members_of_group_recursive_raw is not UNSET:
            field_dict["MEMBERS_OF_GROUP_RECURSIVE_RAW"] = members_of_group_recursive_raw
        if members_of_orgunit is not UNSET:
            field_dict["MEMBERS_OF_ORGUNIT"] = members_of_orgunit
        if all_users is not UNSET:
            field_dict["ALL_USERS"] = all_users
        if users_of_group_recursive_raw is not UNSET:
            field_dict["USERS_OF_GROUP_RECURSIVE_RAW"] = users_of_group_recursive_raw
        if bset_subadmins is not UNSET:
            field_dict["bsetSUBADMINS"] = bset_subadmins
        if users_of_group_raw is not UNSET:
            field_dict["USERS_OF_GROUP_RAW"] = users_of_group_raw
        if groups_of_member_recursive_raw is not UNSET:
            field_dict["GROUPS_OF_MEMBER_RECURSIVE_RAW"] = groups_of_member_recursive_raw
        if bset_select_mask is not UNSET:
            field_dict["bsetSELECT_MASK"] = bset_select_mask
        if groups_of_member_raw is not UNSET:
            field_dict["GROUPS_OF_MEMBER_RAW"] = groups_of_member_raw
        if groups_of_member_recursive is not UNSET:
            field_dict["GROUPS_OF_MEMBER_RECURSIVE"] = groups_of_member_recursive
        if session_users is not UNSET:
            field_dict["SESSION_USERS"] = session_users
        if subadmins is not UNSET:
            field_dict["SUBADMINS"] = subadmins
        if bset_effective_rights is not UNSET:
            field_dict["bsetEFFECTIVE_RIGHTS"] = bset_effective_rights
        if bset_my_users is not UNSET:
            field_dict["bsetMY_USERS"] = bset_my_users
        if users_of_subadmin is not UNSET:
            field_dict["USERS_OF_SUBADMIN"] = users_of_subadmin
        if users_of_superior is not UNSET:
            field_dict["USERS_OF_SUPERIOR"] = users_of_superior
        if users_of_group is not UNSET:
            field_dict["USERS_OF_GROUP"] = users_of_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_users_z import CheckoutUsersZ

        d = src_dict.copy()
        bset_all_users_and_groups = d.pop("bsetALL_USERS_AND_GROUPS", UNSET)

        _by_ids = d.pop("BY_IDS", UNSET)
        by_ids: Union[Unset, CheckoutUsersZ]
        if isinstance(_by_ids, Unset):
            by_ids = UNSET
        else:
            by_ids = CheckoutUsersZ.from_dict(_by_ids)

        _all_groups = d.pop("ALL_GROUPS", UNSET)
        all_groups: Union[Unset, CheckoutUsersZ]
        if isinstance(_all_groups, Unset):
            all_groups = UNSET
        else:
            all_groups = CheckoutUsersZ.from_dict(_all_groups)

        bset_groups_of_member = d.pop("bsetGROUPS_OF_MEMBER", UNSET)

        bset_members_of_group = d.pop("bsetMEMBERS_OF_GROUP", UNSET)

        bset_by_ids = d.pop("bsetBY_IDS", UNSET)

        _members_of_group_recursive = d.pop("MEMBERS_OF_GROUP_RECURSIVE", UNSET)
        members_of_group_recursive: Union[Unset, CheckoutUsersZ]
        if isinstance(_members_of_group_recursive, Unset):
            members_of_group_recursive = UNSET
        else:
            members_of_group_recursive = CheckoutUsersZ.from_dict(_members_of_group_recursive)

        _members_of_group = d.pop("MEMBERS_OF_GROUP", UNSET)
        members_of_group: Union[Unset, CheckoutUsersZ]
        if isinstance(_members_of_group, Unset):
            members_of_group = UNSET
        else:
            members_of_group = CheckoutUsersZ.from_dict(_members_of_group)

        _users_of_group_recursive = d.pop("USERS_OF_GROUP_RECURSIVE", UNSET)
        users_of_group_recursive: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_group_recursive, Unset):
            users_of_group_recursive = UNSET
        else:
            users_of_group_recursive = CheckoutUsersZ.from_dict(_users_of_group_recursive)

        _all_users_and_groups = d.pop("ALL_USERS_AND_GROUPS", UNSET)
        all_users_and_groups: Union[Unset, CheckoutUsersZ]
        if isinstance(_all_users_and_groups, Unset):
            all_users_and_groups = UNSET
        else:
            all_users_and_groups = CheckoutUsersZ.from_dict(_all_users_and_groups)

        _by_ids_raw = d.pop("BY_IDS_RAW", UNSET)
        by_ids_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_by_ids_raw, Unset):
            by_ids_raw = UNSET
        else:
            by_ids_raw = CheckoutUsersZ.from_dict(_by_ids_raw)

        _members_of_group_raw = d.pop("MEMBERS_OF_GROUP_RAW", UNSET)
        members_of_group_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_members_of_group_raw, Unset):
            members_of_group_raw = UNSET
        else:
            members_of_group_raw = CheckoutUsersZ.from_dict(_members_of_group_raw)

        bset_users_of_subadmin = d.pop("bsetUSERS_OF_SUBADMIN", UNSET)

        bset_users_of_superior = d.pop("bsetUSERS_OF_SUPERIOR", UNSET)

        _all_groups_raw = d.pop("ALL_GROUPS_RAW", UNSET)
        all_groups_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_all_groups_raw, Unset):
            all_groups_raw = UNSET
        else:
            all_groups_raw = CheckoutUsersZ.from_dict(_all_groups_raw)

        bset_all_users = d.pop("bsetALL_USERS", UNSET)

        bset_members_of_group_recursive = d.pop("bsetMEMBERS_OF_GROUP_RECURSIVE", UNSET)

        _groups_of_member = d.pop("GROUPS_OF_MEMBER", UNSET)
        groups_of_member: Union[Unset, CheckoutUsersZ]
        if isinstance(_groups_of_member, Unset):
            groups_of_member = UNSET
        else:
            groups_of_member = CheckoutUsersZ.from_dict(_groups_of_member)

        bset_all_groups = d.pop("bsetALL_GROUPS", UNSET)

        bset_users_of_group_recursive = d.pop("bsetUSERS_OF_GROUP_RECURSIVE", UNSET)

        _nothing = d.pop("NOTHING", UNSET)
        nothing: Union[Unset, CheckoutUsersZ]
        if isinstance(_nothing, Unset):
            nothing = UNSET
        else:
            nothing = CheckoutUsersZ.from_dict(_nothing)

        _all_users_and_groups_raw = d.pop("ALL_USERS_AND_GROUPS_RAW", UNSET)
        all_users_and_groups_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_all_users_and_groups_raw, Unset):
            all_users_and_groups_raw = UNSET
        else:
            all_users_and_groups_raw = CheckoutUsersZ.from_dict(_all_users_and_groups_raw)

        _users_of_superior_or_subadmin = d.pop("USERS_OF_SUPERIOR_OR_SUBADMIN", UNSET)
        users_of_superior_or_subadmin: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_superior_or_subadmin, Unset):
            users_of_superior_or_subadmin = UNSET
        else:
            users_of_superior_or_subadmin = CheckoutUsersZ.from_dict(_users_of_superior_or_subadmin)

        bset_users_of_group = d.pop("bsetUSERS_OF_GROUP", UNSET)

        bset_nothing = d.pop("bsetNOTHING", UNSET)

        bset_members_of_orgunit = d.pop("bsetMEMBERS_OF_ORGUNIT", UNSET)

        bset_groups_of_member_recursive = d.pop("bsetGROUPS_OF_MEMBER_RECURSIVE", UNSET)

        bset_users_of_superior_or_subadmin = d.pop("bsetUSERS_OF_SUPERIOR_OR_SUBADMIN", UNSET)

        _all_users_raw = d.pop("ALL_USERS_RAW", UNSET)
        all_users_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_all_users_raw, Unset):
            all_users_raw = UNSET
        else:
            all_users_raw = CheckoutUsersZ.from_dict(_all_users_raw)

        _session_users_raw = d.pop("SESSION_USERS_RAW", UNSET)
        session_users_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_session_users_raw, Unset):
            session_users_raw = UNSET
        else:
            session_users_raw = CheckoutUsersZ.from_dict(_session_users_raw)

        bset_session_info = d.pop("bsetSESSION_INFO", UNSET)

        _members_of_group_recursive_raw = d.pop("MEMBERS_OF_GROUP_RECURSIVE_RAW", UNSET)
        members_of_group_recursive_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_members_of_group_recursive_raw, Unset):
            members_of_group_recursive_raw = UNSET
        else:
            members_of_group_recursive_raw = CheckoutUsersZ.from_dict(_members_of_group_recursive_raw)

        _members_of_orgunit = d.pop("MEMBERS_OF_ORGUNIT", UNSET)
        members_of_orgunit: Union[Unset, CheckoutUsersZ]
        if isinstance(_members_of_orgunit, Unset):
            members_of_orgunit = UNSET
        else:
            members_of_orgunit = CheckoutUsersZ.from_dict(_members_of_orgunit)

        _all_users = d.pop("ALL_USERS", UNSET)
        all_users: Union[Unset, CheckoutUsersZ]
        if isinstance(_all_users, Unset):
            all_users = UNSET
        else:
            all_users = CheckoutUsersZ.from_dict(_all_users)

        _users_of_group_recursive_raw = d.pop("USERS_OF_GROUP_RECURSIVE_RAW", UNSET)
        users_of_group_recursive_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_group_recursive_raw, Unset):
            users_of_group_recursive_raw = UNSET
        else:
            users_of_group_recursive_raw = CheckoutUsersZ.from_dict(_users_of_group_recursive_raw)

        bset_subadmins = d.pop("bsetSUBADMINS", UNSET)

        _users_of_group_raw = d.pop("USERS_OF_GROUP_RAW", UNSET)
        users_of_group_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_group_raw, Unset):
            users_of_group_raw = UNSET
        else:
            users_of_group_raw = CheckoutUsersZ.from_dict(_users_of_group_raw)

        _groups_of_member_recursive_raw = d.pop("GROUPS_OF_MEMBER_RECURSIVE_RAW", UNSET)
        groups_of_member_recursive_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_groups_of_member_recursive_raw, Unset):
            groups_of_member_recursive_raw = UNSET
        else:
            groups_of_member_recursive_raw = CheckoutUsersZ.from_dict(_groups_of_member_recursive_raw)

        bset_select_mask = d.pop("bsetSELECT_MASK", UNSET)

        _groups_of_member_raw = d.pop("GROUPS_OF_MEMBER_RAW", UNSET)
        groups_of_member_raw: Union[Unset, CheckoutUsersZ]
        if isinstance(_groups_of_member_raw, Unset):
            groups_of_member_raw = UNSET
        else:
            groups_of_member_raw = CheckoutUsersZ.from_dict(_groups_of_member_raw)

        _groups_of_member_recursive = d.pop("GROUPS_OF_MEMBER_RECURSIVE", UNSET)
        groups_of_member_recursive: Union[Unset, CheckoutUsersZ]
        if isinstance(_groups_of_member_recursive, Unset):
            groups_of_member_recursive = UNSET
        else:
            groups_of_member_recursive = CheckoutUsersZ.from_dict(_groups_of_member_recursive)

        _session_users = d.pop("SESSION_USERS", UNSET)
        session_users: Union[Unset, CheckoutUsersZ]
        if isinstance(_session_users, Unset):
            session_users = UNSET
        else:
            session_users = CheckoutUsersZ.from_dict(_session_users)

        _subadmins = d.pop("SUBADMINS", UNSET)
        subadmins: Union[Unset, CheckoutUsersZ]
        if isinstance(_subadmins, Unset):
            subadmins = UNSET
        else:
            subadmins = CheckoutUsersZ.from_dict(_subadmins)

        bset_effective_rights = d.pop("bsetEFFECTIVE_RIGHTS", UNSET)

        bset_my_users = d.pop("bsetMY_USERS", UNSET)

        _users_of_subadmin = d.pop("USERS_OF_SUBADMIN", UNSET)
        users_of_subadmin: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_subadmin, Unset):
            users_of_subadmin = UNSET
        else:
            users_of_subadmin = CheckoutUsersZ.from_dict(_users_of_subadmin)

        _users_of_superior = d.pop("USERS_OF_SUPERIOR", UNSET)
        users_of_superior: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_superior, Unset):
            users_of_superior = UNSET
        else:
            users_of_superior = CheckoutUsersZ.from_dict(_users_of_superior)

        _users_of_group = d.pop("USERS_OF_GROUP", UNSET)
        users_of_group: Union[Unset, CheckoutUsersZ]
        if isinstance(_users_of_group, Unset):
            users_of_group = UNSET
        else:
            users_of_group = CheckoutUsersZ.from_dict(_users_of_group)

        checkout_users_c = cls(
            bset_all_users_and_groups=bset_all_users_and_groups,
            by_ids=by_ids,
            all_groups=all_groups,
            bset_groups_of_member=bset_groups_of_member,
            bset_members_of_group=bset_members_of_group,
            bset_by_ids=bset_by_ids,
            members_of_group_recursive=members_of_group_recursive,
            members_of_group=members_of_group,
            users_of_group_recursive=users_of_group_recursive,
            all_users_and_groups=all_users_and_groups,
            by_ids_raw=by_ids_raw,
            members_of_group_raw=members_of_group_raw,
            bset_users_of_subadmin=bset_users_of_subadmin,
            bset_users_of_superior=bset_users_of_superior,
            all_groups_raw=all_groups_raw,
            bset_all_users=bset_all_users,
            bset_members_of_group_recursive=bset_members_of_group_recursive,
            groups_of_member=groups_of_member,
            bset_all_groups=bset_all_groups,
            bset_users_of_group_recursive=bset_users_of_group_recursive,
            nothing=nothing,
            all_users_and_groups_raw=all_users_and_groups_raw,
            users_of_superior_or_subadmin=users_of_superior_or_subadmin,
            bset_users_of_group=bset_users_of_group,
            bset_nothing=bset_nothing,
            bset_members_of_orgunit=bset_members_of_orgunit,
            bset_groups_of_member_recursive=bset_groups_of_member_recursive,
            bset_users_of_superior_or_subadmin=bset_users_of_superior_or_subadmin,
            all_users_raw=all_users_raw,
            session_users_raw=session_users_raw,
            bset_session_info=bset_session_info,
            members_of_group_recursive_raw=members_of_group_recursive_raw,
            members_of_orgunit=members_of_orgunit,
            all_users=all_users,
            users_of_group_recursive_raw=users_of_group_recursive_raw,
            bset_subadmins=bset_subadmins,
            users_of_group_raw=users_of_group_raw,
            groups_of_member_recursive_raw=groups_of_member_recursive_raw,
            bset_select_mask=bset_select_mask,
            groups_of_member_raw=groups_of_member_raw,
            groups_of_member_recursive=groups_of_member_recursive,
            session_users=session_users,
            subadmins=subadmins,
            bset_effective_rights=bset_effective_rights,
            bset_my_users=bset_my_users,
            users_of_subadmin=users_of_subadmin,
            users_of_superior=users_of_superior,
            users_of_group=users_of_group,
        )

        checkout_users_c.additional_properties = d
        return checkout_users_c

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
