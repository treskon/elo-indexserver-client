from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString
    from ..models.server import Server


T = TypeVar("T", bound="Domain")


@_attrs_define
class Domain:
    r""" This class defines how to connect to a domain controller, login a user and find her groups.

        Attributes:
            required_group (Union[Unset, str]): Users must be member of this LDAP group.
                Optional, short LDAP group name (not a DN) the user
                 must be a member of in order to login. The membership in this group is checked after the group
                 list has been collected. Hence, {@link #groupSearchDNList} and {@link #maxGroupNesting} have an
                 effect on this check too. The comparison to this value is case-sensitive.
            search_filter_for_person (Union[Unset, str]): Search filter for person.
                Defaults to "(&amp;(objectclass=person)(sAMAccountName={0}))"
            attributes_to_read (Union[Unset, List[str]]):
            filter_person (Union[Unset, str]): Filter expression used to find a person by her/his sAMAccountName.
            attribute_for_user_prop_os (Union[Unset, str]): LDAP attribute to be used as OS name for {@link
                UserInfoC#PROP_NAME_OS}.
                This value is either
                 {@link #AD_SAM_ACCOUNT_NAME} or {@link #AD_USER_PRINCIPAL_NAME}. If set as
                 {@link #AD_USER_PRINCIPAL_NAME}, also set {@link #searchFilterForPerson} to
                 {@link #FILTER_PERSON_USER_PRINCIPAL_NAME}. Default is sAMAccountName.
            servers (Union[Unset, List['Server']]):
            ad_sam_account_name (Union[Unset, str]): LDAP attribute ID for sAMAccountName.
            filter_person_mail (Union[Unset, str]): Filter expression used to find a person by her mail address.
            connection_timeout_seconds (Union[Unset, int]): Timeout limit when connecting to a LDAP server.
            ad_user_principal_name (Union[Unset, str]): LDAP attribute ID for userPrincipalName.
            group_search_dn_list (Union[Unset, List[str]]):
            attribute_name_member_of (Union[Unset, str]): Name of attribute that contains the user's groups. Defaults to
                "memberOf".
            name_formatter (Union[Unset, str]): Format string to build a unique ELO account name from LDAP attributes.
                LDAP attributes have to
                 be enclosed in $. Examples: 1. $cn$, $department$ ; 2. $sAMAccountName$ $department$
            filter_person_user_principal_name (Union[Unset, str]): Filter expression used to find a person by her/his
                userPrinicpalName.
            ad_attribute_mail (Union[Unset, str]): LDAP attribute ID that specifies the mail address of a given user.
            default_attributes (Union[Unset, List[str]]):
            search_filter_for_mail (Union[Unset, str]): Search filter for mail address.
                Defaults to "(&amp;(objectclass=person)(mail={0}))"
            attribute_superior (Union[Unset, str]): Attribute to determine the superior of an ELO user. Set this attribute
                ID e.g.
                to
                 {@link #AD_ATTRIBUTE_MANAGER} to assign the superior of a user on login. This value is empty by
                 default, which means that ELO Administrator (user ID 0) is assigned as superior.
            ad_attribute_manager (Union[Unset, str]): AD attribute ID -manager- that specifies the superior of an ELO user.
            attribute_name_mail (Union[Unset, str]): Name of attribute that contains the user's mail address. Defaults to
                "mail".
            default_user_name (Union[Unset, str]): Optional user name to connect to the LDAP servers.
                This account must have the permission to
                 list the group associations of all users. It does not need to be an ELO account too.
            parent_of_new_user (Union[Unset, str]): Assign this user as parent for a new ELO user.
                ID, GUID or name of existing ELO user or group
                 that is assigned as UserInfo#parent when a new ELO user is created. This value is empty by
                 default, which means that ELO Administrator (user ID 0) is assigned as parent.
            max_group_nesting (Union[Unset, int]): Groups are collected recursively up to this depth. A value of 0 means no
                depth limit.
                This
                 value is ignored, if {@link #groupSearchDNList} is empty.
            search_filter_for_groups (Union[Unset, str]): Name of attribute that contains the user's groups.
                Defaults to "(&amp;(objectCategory=group)(member={0}))"
            default_user_password_encr (Union[Unset, str]): Optional encrypted user password to connect to the LDAP servers.
                This password can also be set
                 in plain text. It is automatically encrypted when stored into a file or database.
            person_search_dn_list (Union[Unset, List[str]]):
            search_time_limit_seconds (Union[Unset, int]): Search for groups can least up to this number of seconds.
            default_environment (Union[Unset, List[List[str]]]):
            domain_prefix (Union[Unset, str]): Domain prefix.
                The login name of the user is prefixed by this value to build the user property
                 {@link UserInfoC#PROP_NAME_OS}. When using this prefix, users should also use this prefix for
                 login. This value must end with a separator char, e.g. backslash. E.g. ELO\\
            filter_groups (Union[Unset, str]): Filter expression used to find groups of a given user.
            initial_context_environment (Union[Unset, MapToString]):
            name (Union[Unset, str]): Domain name. E.g. ELO.
                LOCAL
            ad_attribute_member_of (Union[Unset, str]): LDAP attribute ID that specifies the group list of a given user or
                group.
     """

    required_group: Union[Unset, str] = UNSET
    search_filter_for_person: Union[Unset, str] = UNSET
    attributes_to_read: Union[Unset, List[str]] = UNSET
    filter_person: Union[Unset, str] = UNSET
    attribute_for_user_prop_os: Union[Unset, str] = UNSET
    servers: Union[Unset, List["Server"]] = UNSET
    ad_sam_account_name: Union[Unset, str] = UNSET
    filter_person_mail: Union[Unset, str] = UNSET
    connection_timeout_seconds: Union[Unset, int] = UNSET
    ad_user_principal_name: Union[Unset, str] = UNSET
    group_search_dn_list: Union[Unset, List[str]] = UNSET
    attribute_name_member_of: Union[Unset, str] = UNSET
    name_formatter: Union[Unset, str] = UNSET
    filter_person_user_principal_name: Union[Unset, str] = UNSET
    ad_attribute_mail: Union[Unset, str] = UNSET
    default_attributes: Union[Unset, List[str]] = UNSET
    search_filter_for_mail: Union[Unset, str] = UNSET
    attribute_superior: Union[Unset, str] = UNSET
    ad_attribute_manager: Union[Unset, str] = UNSET
    attribute_name_mail: Union[Unset, str] = UNSET
    default_user_name: Union[Unset, str] = UNSET
    parent_of_new_user: Union[Unset, str] = UNSET
    max_group_nesting: Union[Unset, int] = UNSET
    search_filter_for_groups: Union[Unset, str] = UNSET
    default_user_password_encr: Union[Unset, str] = UNSET
    person_search_dn_list: Union[Unset, List[str]] = UNSET
    search_time_limit_seconds: Union[Unset, int] = UNSET
    default_environment: Union[Unset, List[List[str]]] = UNSET
    domain_prefix: Union[Unset, str] = UNSET
    filter_groups: Union[Unset, str] = UNSET
    initial_context_environment: Union[Unset, "MapToString"] = UNSET
    name: Union[Unset, str] = UNSET
    ad_attribute_member_of: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        required_group = self.required_group

        search_filter_for_person = self.search_filter_for_person

        attributes_to_read: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes_to_read, Unset):
            attributes_to_read = self.attributes_to_read

        filter_person = self.filter_person

        attribute_for_user_prop_os = self.attribute_for_user_prop_os

        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for componentsschemas_list_of_server_item_data in self.servers:
                componentsschemas_list_of_server_item = componentsschemas_list_of_server_item_data.to_dict()
                servers.append(componentsschemas_list_of_server_item)

        ad_sam_account_name = self.ad_sam_account_name

        filter_person_mail = self.filter_person_mail

        connection_timeout_seconds = self.connection_timeout_seconds

        ad_user_principal_name = self.ad_user_principal_name

        group_search_dn_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_search_dn_list, Unset):
            group_search_dn_list = self.group_search_dn_list

        attribute_name_member_of = self.attribute_name_member_of

        name_formatter = self.name_formatter

        filter_person_user_principal_name = self.filter_person_user_principal_name

        ad_attribute_mail = self.ad_attribute_mail

        default_attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.default_attributes, Unset):
            default_attributes = self.default_attributes

        search_filter_for_mail = self.search_filter_for_mail

        attribute_superior = self.attribute_superior

        ad_attribute_manager = self.ad_attribute_manager

        attribute_name_mail = self.attribute_name_mail

        default_user_name = self.default_user_name

        parent_of_new_user = self.parent_of_new_user

        max_group_nesting = self.max_group_nesting

        search_filter_for_groups = self.search_filter_for_groups

        default_user_password_encr = self.default_user_password_encr

        person_search_dn_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.person_search_dn_list, Unset):
            person_search_dn_list = self.person_search_dn_list

        search_time_limit_seconds = self.search_time_limit_seconds

        default_environment: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.default_environment, Unset):
            default_environment = []
            for componentsschemas_array_2_of_string_item_data in self.default_environment:
                componentsschemas_array_2_of_string_item = componentsschemas_array_2_of_string_item_data

                default_environment.append(componentsschemas_array_2_of_string_item)

        domain_prefix = self.domain_prefix

        filter_groups = self.filter_groups

        initial_context_environment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initial_context_environment, Unset):
            initial_context_environment = self.initial_context_environment.to_dict()

        name = self.name

        ad_attribute_member_of = self.ad_attribute_member_of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_group is not UNSET:
            field_dict["requiredGroup"] = required_group
        if search_filter_for_person is not UNSET:
            field_dict["searchFilterForPerson"] = search_filter_for_person
        if attributes_to_read is not UNSET:
            field_dict["attributesToRead"] = attributes_to_read
        if filter_person is not UNSET:
            field_dict["FILTER_PERSON"] = filter_person
        if attribute_for_user_prop_os is not UNSET:
            field_dict["attributeForUserPropOS"] = attribute_for_user_prop_os
        if servers is not UNSET:
            field_dict["servers"] = servers
        if ad_sam_account_name is not UNSET:
            field_dict["AD_SAM_ACCOUNT_NAME"] = ad_sam_account_name
        if filter_person_mail is not UNSET:
            field_dict["FILTER_PERSON_MAIL"] = filter_person_mail
        if connection_timeout_seconds is not UNSET:
            field_dict["connectionTimeoutSeconds"] = connection_timeout_seconds
        if ad_user_principal_name is not UNSET:
            field_dict["AD_USER_PRINCIPAL_NAME"] = ad_user_principal_name
        if group_search_dn_list is not UNSET:
            field_dict["groupSearchDNList"] = group_search_dn_list
        if attribute_name_member_of is not UNSET:
            field_dict["attributeNameMemberOf"] = attribute_name_member_of
        if name_formatter is not UNSET:
            field_dict["nameFormatter"] = name_formatter
        if filter_person_user_principal_name is not UNSET:
            field_dict["FILTER_PERSON_USER_PRINCIPAL_NAME"] = filter_person_user_principal_name
        if ad_attribute_mail is not UNSET:
            field_dict["AD_ATTRIBUTE_MAIL"] = ad_attribute_mail
        if default_attributes is not UNSET:
            field_dict["DEFAULT_ATTRIBUTES"] = default_attributes
        if search_filter_for_mail is not UNSET:
            field_dict["searchFilterForMail"] = search_filter_for_mail
        if attribute_superior is not UNSET:
            field_dict["attributeSuperior"] = attribute_superior
        if ad_attribute_manager is not UNSET:
            field_dict["AD_ATTRIBUTE_MANAGER"] = ad_attribute_manager
        if attribute_name_mail is not UNSET:
            field_dict["attributeNameMail"] = attribute_name_mail
        if default_user_name is not UNSET:
            field_dict["defaultUserName"] = default_user_name
        if parent_of_new_user is not UNSET:
            field_dict["parentOfNewUser"] = parent_of_new_user
        if max_group_nesting is not UNSET:
            field_dict["maxGroupNesting"] = max_group_nesting
        if search_filter_for_groups is not UNSET:
            field_dict["searchFilterForGroups"] = search_filter_for_groups
        if default_user_password_encr is not UNSET:
            field_dict["defaultUserPasswordEncr"] = default_user_password_encr
        if person_search_dn_list is not UNSET:
            field_dict["personSearchDNList"] = person_search_dn_list
        if search_time_limit_seconds is not UNSET:
            field_dict["searchTimeLimitSeconds"] = search_time_limit_seconds
        if default_environment is not UNSET:
            field_dict["DEFAULT_ENVIRONMENT"] = default_environment
        if domain_prefix is not UNSET:
            field_dict["domainPrefix"] = domain_prefix
        if filter_groups is not UNSET:
            field_dict["FILTER_GROUPS"] = filter_groups
        if initial_context_environment is not UNSET:
            field_dict["initialContextEnvironment"] = initial_context_environment
        if name is not UNSET:
            field_dict["name"] = name
        if ad_attribute_member_of is not UNSET:
            field_dict["AD_ATTRIBUTE_MEMBER_OF"] = ad_attribute_member_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString
        from ..models.server import Server

        d = src_dict.copy()
        required_group = d.pop("requiredGroup", UNSET)

        search_filter_for_person = d.pop("searchFilterForPerson", UNSET)

        attributes_to_read = cast(List[str], d.pop("attributesToRead", UNSET))

        filter_person = d.pop("FILTER_PERSON", UNSET)

        attribute_for_user_prop_os = d.pop("attributeForUserPropOS", UNSET)

        servers = []
        _servers = d.pop("servers", UNSET)
        for componentsschemas_list_of_server_item_data in _servers or []:
            componentsschemas_list_of_server_item = Server.from_dict(componentsschemas_list_of_server_item_data)

            servers.append(componentsschemas_list_of_server_item)

        ad_sam_account_name = d.pop("AD_SAM_ACCOUNT_NAME", UNSET)

        filter_person_mail = d.pop("FILTER_PERSON_MAIL", UNSET)

        connection_timeout_seconds = d.pop("connectionTimeoutSeconds", UNSET)

        ad_user_principal_name = d.pop("AD_USER_PRINCIPAL_NAME", UNSET)

        group_search_dn_list = cast(List[str], d.pop("groupSearchDNList", UNSET))

        attribute_name_member_of = d.pop("attributeNameMemberOf", UNSET)

        name_formatter = d.pop("nameFormatter", UNSET)

        filter_person_user_principal_name = d.pop("FILTER_PERSON_USER_PRINCIPAL_NAME", UNSET)

        ad_attribute_mail = d.pop("AD_ATTRIBUTE_MAIL", UNSET)

        default_attributes = cast(List[str], d.pop("DEFAULT_ATTRIBUTES", UNSET))

        search_filter_for_mail = d.pop("searchFilterForMail", UNSET)

        attribute_superior = d.pop("attributeSuperior", UNSET)

        ad_attribute_manager = d.pop("AD_ATTRIBUTE_MANAGER", UNSET)

        attribute_name_mail = d.pop("attributeNameMail", UNSET)

        default_user_name = d.pop("defaultUserName", UNSET)

        parent_of_new_user = d.pop("parentOfNewUser", UNSET)

        max_group_nesting = d.pop("maxGroupNesting", UNSET)

        search_filter_for_groups = d.pop("searchFilterForGroups", UNSET)

        default_user_password_encr = d.pop("defaultUserPasswordEncr", UNSET)

        person_search_dn_list = cast(List[str], d.pop("personSearchDNList", UNSET))

        search_time_limit_seconds = d.pop("searchTimeLimitSeconds", UNSET)

        default_environment = []
        _default_environment = d.pop("DEFAULT_ENVIRONMENT", UNSET)
        for componentsschemas_array_2_of_string_item_data in _default_environment or []:
            componentsschemas_array_2_of_string_item = cast(List[str], componentsschemas_array_2_of_string_item_data)

            default_environment.append(componentsschemas_array_2_of_string_item)

        domain_prefix = d.pop("domainPrefix", UNSET)

        filter_groups = d.pop("FILTER_GROUPS", UNSET)

        _initial_context_environment = d.pop("initialContextEnvironment", UNSET)
        initial_context_environment: Union[Unset, MapToString]
        if isinstance(_initial_context_environment, Unset):
            initial_context_environment = UNSET
        else:
            initial_context_environment = MapToString.from_dict(_initial_context_environment)

        name = d.pop("name", UNSET)

        ad_attribute_member_of = d.pop("AD_ATTRIBUTE_MEMBER_OF", UNSET)

        domain = cls(
            required_group=required_group,
            search_filter_for_person=search_filter_for_person,
            attributes_to_read=attributes_to_read,
            filter_person=filter_person,
            attribute_for_user_prop_os=attribute_for_user_prop_os,
            servers=servers,
            ad_sam_account_name=ad_sam_account_name,
            filter_person_mail=filter_person_mail,
            connection_timeout_seconds=connection_timeout_seconds,
            ad_user_principal_name=ad_user_principal_name,
            group_search_dn_list=group_search_dn_list,
            attribute_name_member_of=attribute_name_member_of,
            name_formatter=name_formatter,
            filter_person_user_principal_name=filter_person_user_principal_name,
            ad_attribute_mail=ad_attribute_mail,
            default_attributes=default_attributes,
            search_filter_for_mail=search_filter_for_mail,
            attribute_superior=attribute_superior,
            ad_attribute_manager=ad_attribute_manager,
            attribute_name_mail=attribute_name_mail,
            default_user_name=default_user_name,
            parent_of_new_user=parent_of_new_user,
            max_group_nesting=max_group_nesting,
            search_filter_for_groups=search_filter_for_groups,
            default_user_password_encr=default_user_password_encr,
            person_search_dn_list=person_search_dn_list,
            search_time_limit_seconds=search_time_limit_seconds,
            default_environment=default_environment,
            domain_prefix=domain_prefix,
            filter_groups=filter_groups,
            initial_context_environment=initial_context_environment,
            name=name,
            ad_attribute_member_of=ad_attribute_member_of,
        )

        domain.additional_properties = d
        return domain

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
