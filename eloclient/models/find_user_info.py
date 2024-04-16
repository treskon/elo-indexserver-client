from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_users_z import CheckoutUsersZ
    from ..models.find_result_access_mode import FindResultAccessMode
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="FindUserInfo")


@_attrs_define
class FindUserInfo:
    """This class describes the search criteria for {@link IXServicePortIF#findFirstUsers}.
    The wildcards defined by {@link SessionOptionsC#DB_WILDCARDS} can be used for {@link #name},
     {@link #desc}, {@link #property}, and {@link #ldapProperty}.

     Members {@link #name}, {@link #desc}, {@link #property}, and {@link #ldapProperty} are combined
     by OR. Other members are combinded by AND.

        Attributes:
            has_not_flags (Union[Unset, int]): Select only users that have non this {@link UserInfo#flags} set.
                The selected users are found
                 by testing (UserInfo#flags &amp; hasNotFlags) == 0.
            ldap_property (Union[Unset, KeyValue]): This class contains a name and an associated value.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            checkout_users_z (Union[Unset, CheckoutUsersZ]): This class encapsulates the constants of CheckoutUsersC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            has_flags (Union[Unset, int]): Select only users that have all of this {@link UserInfo#flags} set. A value of 0
                is ignored.
                The selected users are found by testing (UserInfo#flags &amp; hasFlags) == hasFlags.
            only_users (Union[Unset, bool]): <p>
                Search for users only.
                 </p>

                 <p>
                 If this member is set to <code>true</code>, flags provided by {@link #checkoutUsersZ} are
                 ignored.
                 </p>
            only_groups (Union[Unset, bool]): <p>
                Search for groups only.
                 </p>

                 <p>
                 If this member is set to <code>true</code>, flags provided by {@link #checkoutUsersZ} are
                 ignored.
                 </p>
            has_not_flags_2 (Union[Unset, int]): Select only users that have none this {@link UserInfo#flags2} set.
                The selected users are found
                 by testing (UserInfo#flags2 &amp; hasNotFlags2) == 0.
            user_ids (Union[Unset, List[str]]):
            sort_order (Union[Unset, int]): Specify how the results should be ordered.
                Valid values are {@link SortOrderC#USERNAME} and
                 {@link SortOrderC#IUSERNAME}. Sorted results are returned in FindResult#sortedResult.
            name (Union[Unset, str]): Find by user name. Search over {@link UserInfo#name}.
            property_ (Union[Unset, KeyValue]): This class contains a name and an associated value.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
                find results.
            return_user_info_map (Union[Unset, bool]): Return entire information about each user.
                If true, {@link UserInfo} objects are returned in
                 {@link FindResult#userInfos}. If false, {@link UserName} objects are returned in
                 {@link FindResult#userNames}. Additionally, FindResult#sortedResult returns a sorted list of
                 either UserInfo or UserName objects.
            has_flags_2 (Union[Unset, int]): Select only users that have all of this {@link UserInfo#flags2} set. A value of
                0 is ignored.
                The selected users are found by testing (UserInfo#flags2 &amp; hasFlags2) == hasFlags2.
            workspace_info (Union[Unset, str]): Workspace related data.
            desc (Union[Unset, str]): Find by user description. Search over {@link UserInfo#desc}.
    """

    has_not_flags: Union[Unset, int] = UNSET
    ldap_property: Union[Unset, "KeyValue"] = UNSET
    checkout_users_z: Union[Unset, "CheckoutUsersZ"] = UNSET
    has_flags: Union[Unset, int] = UNSET
    only_users: Union[Unset, bool] = UNSET
    only_groups: Union[Unset, bool] = UNSET
    has_not_flags_2: Union[Unset, int] = UNSET
    user_ids: Union[Unset, List[str]] = UNSET
    sort_order: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    property_: Union[Unset, "KeyValue"] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    return_user_info_map: Union[Unset, bool] = UNSET
    has_flags_2: Union[Unset, int] = UNSET
    workspace_info: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_not_flags = self.has_not_flags

        ldap_property: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ldap_property, Unset):
            ldap_property = self.ldap_property.to_dict()

        checkout_users_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_users_z, Unset):
            checkout_users_z = self.checkout_users_z.to_dict()

        has_flags = self.has_flags

        only_users = self.only_users

        only_groups = self.only_groups

        has_not_flags_2 = self.has_not_flags_2

        user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        sort_order = self.sort_order

        name = self.name

        property_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        return_user_info_map = self.return_user_info_map

        has_flags_2 = self.has_flags_2

        workspace_info = self.workspace_info

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_not_flags is not UNSET:
            field_dict["hasNotFlags"] = has_not_flags
        if ldap_property is not UNSET:
            field_dict["ldapProperty"] = ldap_property
        if checkout_users_z is not UNSET:
            field_dict["checkoutUsersZ"] = checkout_users_z
        if has_flags is not UNSET:
            field_dict["hasFlags"] = has_flags
        if only_users is not UNSET:
            field_dict["onlyUsers"] = only_users
        if only_groups is not UNSET:
            field_dict["onlyGroups"] = only_groups
        if has_not_flags_2 is not UNSET:
            field_dict["hasNotFlags2"] = has_not_flags_2
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if name is not UNSET:
            field_dict["name"] = name
        if property_ is not UNSET:
            field_dict["property"] = property_
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode
        if return_user_info_map is not UNSET:
            field_dict["returnUserInfoMap"] = return_user_info_map
        if has_flags_2 is not UNSET:
            field_dict["hasFlags2"] = has_flags_2
        if workspace_info is not UNSET:
            field_dict["workspaceInfo"] = workspace_info
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_users_z import CheckoutUsersZ
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        has_not_flags = d.pop("hasNotFlags", UNSET)

        _ldap_property = d.pop("ldapProperty", UNSET)
        ldap_property: Union[Unset, KeyValue]
        if isinstance(_ldap_property, Unset):
            ldap_property = UNSET
        else:
            ldap_property = KeyValue.from_dict(_ldap_property)

        _checkout_users_z = d.pop("checkoutUsersZ", UNSET)
        checkout_users_z: Union[Unset, CheckoutUsersZ]
        if isinstance(_checkout_users_z, Unset):
            checkout_users_z = UNSET
        else:
            checkout_users_z = CheckoutUsersZ.from_dict(_checkout_users_z)

        has_flags = d.pop("hasFlags", UNSET)

        only_users = d.pop("onlyUsers", UNSET)

        only_groups = d.pop("onlyGroups", UNSET)

        has_not_flags_2 = d.pop("hasNotFlags2", UNSET)

        user_ids = cast(List[str], d.pop("userIds", UNSET))

        sort_order = d.pop("sortOrder", UNSET)

        name = d.pop("name", UNSET)

        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, KeyValue]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = KeyValue.from_dict(_property_)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        return_user_info_map = d.pop("returnUserInfoMap", UNSET)

        has_flags_2 = d.pop("hasFlags2", UNSET)

        workspace_info = d.pop("workspaceInfo", UNSET)

        desc = d.pop("desc", UNSET)

        find_user_info = cls(
            has_not_flags=has_not_flags,
            ldap_property=ldap_property,
            checkout_users_z=checkout_users_z,
            has_flags=has_flags,
            only_users=only_users,
            only_groups=only_groups,
            has_not_flags_2=has_not_flags_2,
            user_ids=user_ids,
            sort_order=sort_order,
            name=name,
            property_=property_,
            find_result_access_mode=find_result_access_mode,
            return_user_info_map=return_user_info_map,
            has_flags_2=has_flags_2,
            workspace_info=workspace_info,
            desc=desc,
        )

        find_user_info.additional_properties = d
        return find_user_info

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
