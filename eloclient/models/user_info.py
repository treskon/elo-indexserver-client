from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString
    from ..models.session_info import SessionInfo
    from ..models.user_name import UserName


T = TypeVar("T", bound="UserInfo")


@_attrs_define
class UserInfo:
    """<p>
    Data class containing the user information data for the user logged in to the Index server. User
     information includes ID, name, rights, parent, etc.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            parent (Union[Unset, int]): User ID of the users parent (users adminstrator).
            sessions (Union[Unset, List['SessionInfo']]):
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            ldap_properties (Union[Unset, MapToString]):
            flags2 (Union[Unset, int]): Second bitset of user rights.
            flags (Union[Unset, int]): User rights. Possible values are combinations of <code>AccessC.FLAG_*</code>
                constants.
            group_list (Union[Unset, List[int]]):
            type (Union[Unset, int]): User type. <code>TYPE_USER</code> for user, <code>TYPE_GROUP</code> for group.
            keylist (Union[Unset, List[int]]):
            user_props (Union[Unset, List[str]]):
            superior_id (Union[Unset, int]): ID of the users superior.
                If the user does not have a superior, this value is equal to
                 <code>id</code>.
            available_roles (Union[Unset, List['UserName']]):
            internal_user (Union[Unset, bool]): The flag for a group which will not be removed by LDAP replication.
            t_stamp (Union[Unset, str]): Timestamp The format is JJJJ.MM.DD.hh.mm.
                ss
            last_login_iso (Union[Unset, str]): Last login timestamp (in timezone UTC). This value is read-only and
                undefined for groups.
                Only
                 the date part is valid.
            name (Union[Unset, str]): User name
            guid (Union[Unset, str]): GUID
            id (Union[Unset, int]): User identifier
            package_name (Union[Unset, str]): The package name of UserInfo
            workspace_info (Union[Unset, str]): Workspace related data.
            pwd (Union[Unset, str]): User password
            org_unit_ids (Union[Unset, List[int]]):
            desc (Union[Unset, str]): User description.
    """

    parent: Union[Unset, int] = UNSET
    sessions: Union[Unset, List["SessionInfo"]] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    ldap_properties: Union[Unset, "MapToString"] = UNSET
    flags2: Union[Unset, int] = UNSET
    flags: Union[Unset, int] = UNSET
    group_list: Union[Unset, List[int]] = UNSET
    type: Union[Unset, int] = UNSET
    keylist: Union[Unset, List[int]] = UNSET
    user_props: Union[Unset, List[str]] = UNSET
    superior_id: Union[Unset, int] = UNSET
    available_roles: Union[Unset, List["UserName"]] = UNSET
    internal_user: Union[Unset, bool] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    last_login_iso: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    package_name: Union[Unset, str] = UNSET
    workspace_info: Union[Unset, str] = UNSET
    pwd: Union[Unset, str] = UNSET
    org_unit_ids: Union[Unset, List[int]] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent = self.parent

        sessions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sessions, Unset):
            sessions = []
            for sessions_item_data in self.sessions:
                sessions_item = sessions_item_data.to_dict()
                sessions.append(sessions_item)

        t_stamp_sync = self.t_stamp_sync

        ldap_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ldap_properties, Unset):
            ldap_properties = self.ldap_properties.to_dict()

        flags2 = self.flags2

        flags = self.flags

        group_list: Union[Unset, List[int]] = UNSET
        if not isinstance(self.group_list, Unset):
            group_list = self.group_list

        type = self.type

        keylist: Union[Unset, List[int]] = UNSET
        if not isinstance(self.keylist, Unset):
            keylist = self.keylist

        user_props: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_props, Unset):
            user_props = self.user_props

        superior_id = self.superior_id

        available_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_roles, Unset):
            available_roles = []
            for componentsschemas_list_of_user_name_item_data in self.available_roles:
                componentsschemas_list_of_user_name_item = componentsschemas_list_of_user_name_item_data.to_dict()
                available_roles.append(componentsschemas_list_of_user_name_item)

        internal_user = self.internal_user

        t_stamp = self.t_stamp

        last_login_iso = self.last_login_iso

        name = self.name

        guid = self.guid

        id = self.id

        package_name = self.package_name

        workspace_info = self.workspace_info

        pwd = self.pwd

        org_unit_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.org_unit_ids, Unset):
            org_unit_ids = self.org_unit_ids

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent is not UNSET:
            field_dict["parent"] = parent
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if t_stamp_sync is not UNSET:
            field_dict["tStampSync"] = t_stamp_sync
        if ldap_properties is not UNSET:
            field_dict["ldapProperties"] = ldap_properties
        if flags2 is not UNSET:
            field_dict["flags2"] = flags2
        if flags is not UNSET:
            field_dict["flags"] = flags
        if group_list is not UNSET:
            field_dict["groupList"] = group_list
        if type is not UNSET:
            field_dict["type"] = type
        if keylist is not UNSET:
            field_dict["keylist"] = keylist
        if user_props is not UNSET:
            field_dict["userProps"] = user_props
        if superior_id is not UNSET:
            field_dict["superiorId"] = superior_id
        if available_roles is not UNSET:
            field_dict["availableRoles"] = available_roles
        if internal_user is not UNSET:
            field_dict["internalUser"] = internal_user
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if last_login_iso is not UNSET:
            field_dict["lastLoginIso"] = last_login_iso
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if workspace_info is not UNSET:
            field_dict["workspaceInfo"] = workspace_info
        if pwd is not UNSET:
            field_dict["pwd"] = pwd
        if org_unit_ids is not UNSET:
            field_dict["orgUnitIds"] = org_unit_ids
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString
        from ..models.session_info import SessionInfo
        from ..models.user_name import UserName

        d = src_dict.copy()
        parent = d.pop("parent", UNSET)

        sessions = []
        _sessions = d.pop("sessions", UNSET)
        for sessions_item_data in _sessions or []:
            sessions_item = SessionInfo.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        t_stamp_sync = d.pop("tStampSync", UNSET)

        _ldap_properties = d.pop("ldapProperties", UNSET)
        ldap_properties: Union[Unset, MapToString]
        if isinstance(_ldap_properties, Unset):
            ldap_properties = UNSET
        else:
            ldap_properties = MapToString.from_dict(_ldap_properties)

        flags2 = d.pop("flags2", UNSET)

        flags = d.pop("flags", UNSET)

        group_list = cast(List[int], d.pop("groupList", UNSET))

        type = d.pop("type", UNSET)

        keylist = cast(List[int], d.pop("keylist", UNSET))

        user_props = cast(List[str], d.pop("userProps", UNSET))

        superior_id = d.pop("superiorId", UNSET)

        available_roles = []
        _available_roles = d.pop("availableRoles", UNSET)
        for componentsschemas_list_of_user_name_item_data in _available_roles or []:
            componentsschemas_list_of_user_name_item = UserName.from_dict(componentsschemas_list_of_user_name_item_data)

            available_roles.append(componentsschemas_list_of_user_name_item)

        internal_user = d.pop("internalUser", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        last_login_iso = d.pop("lastLoginIso", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        package_name = d.pop("packageName", UNSET)

        workspace_info = d.pop("workspaceInfo", UNSET)

        pwd = d.pop("pwd", UNSET)

        org_unit_ids = cast(List[int], d.pop("orgUnitIds", UNSET))

        desc = d.pop("desc", UNSET)

        user_info = cls(
            parent=parent,
            sessions=sessions,
            t_stamp_sync=t_stamp_sync,
            ldap_properties=ldap_properties,
            flags2=flags2,
            flags=flags,
            group_list=group_list,
            type=type,
            keylist=keylist,
            user_props=user_props,
            superior_id=superior_id,
            available_roles=available_roles,
            internal_user=internal_user,
            t_stamp=t_stamp,
            last_login_iso=last_login_iso,
            name=name,
            guid=guid,
            id=id,
            package_name=package_name,
            workspace_info=workspace_info,
            pwd=pwd,
            org_unit_ids=org_unit_ids,
            desc=desc,
        )

        user_info.additional_properties = d
        return user_info

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
