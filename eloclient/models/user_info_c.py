from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserInfoC")


@_attrs_define
class UserInfoC:
    """<p>
    Constants related to user information.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_superior_id (Union[Unset, str]): Member bit {@link UserInfo#superiorId}
            ldap_prop_object_class (Union[Unset, str]): Object class
            ldap_key_online_mailbox_enabled (Union[Unset, str]): IsMailboxEnabled. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_exch_recipient_type_details (Union[Unset, str]): msExchRecipientTypeDetails
            ldap_key_sam_account_type (Union[Unset, str]): Contains information about every account type object.
                Key to access the map
                 UserInfo.ldapProperties
            ldap_key_mail_nick_name (Union[Unset, str]): Mail nick name. Key to access the map UserInfo.
                ldapProperties
            mb_user_props (Union[Unset, str]): Member bit {@link UserInfo#userProps}
            ldap_key_exch_recipient_type_details (Union[Unset, str]): msExchRecipientTypeDetails. Key to access the map
                UserInfo.
                ldapProperties
            ldap_prop_exch_owning_server (Union[Unset, str]): msExchOwningServer
            guid_eloservice (Union[Unset, str]): GUID of the default service user.
            ldap_key_legacy_exchange_dn (Union[Unset, str]): LegacyExchangeDN. Key to access the map UserInfo.
                ldapProperties
            mb_flags_2 (Union[Unset, str]): Member bit {@link UserInfo#flags2}
            ln_ldap_prop_key (Union[Unset, int]): Maximum length of LDAP property key.
            max_name (Union[Unset, int]): Maximum user name length.
            type_userid_owner (Union[Unset, int]): Type value for the current user
            mb_last_login_iso (Union[Unset, str]): Member bit {@link UserInfo#lastLoginIso}
            ldap_prop_object_guid (Union[Unset, str]): The unique identifier for an object
            ldap_prop_exch_recipient_display_type (Union[Unset, str]): msExchRecipientDisplayType
            prop_name_email (Union[Unset, int]):
            ln_user_prop (Union[Unset, int]): Maximum user property length
            id_everyone_group (Union[Unset, int]): Every user is in the group "Everyone". This is the internal ID for this
                group.
            mb_group_list (Union[Unset, str]): Member bit {@link UserInfo#groupList}
            max_groups (Union[Unset, int]): Maximum number of groups per user.
            ldap_key_group_type (Union[Unset, str]): Group type. Key to access the map UserInfo.
                ldapProperties
            ldap_key_user_principal_name (Union[Unset, str]): User principal name. Key to access the map UserInfo.
                ldapProperties
            ldap_key_object_class (Union[Unset, str]): Object class. Key to access the map UserInfo.
                ldapProperties
            mb_ldap_properties (Union[Unset, str]): Member bit {@link UserInfo#ldapProperties}
            ldap_prop_sam_account_name (Union[Unset, str]): NT account name
            mb_guid (Union[Unset, str]): Member bit {@link UserInfo#guid}
            ldap_prop_member_of (Union[Unset, str]): Member of
            ldap_prop_legacy_exchange_dn (Union[Unset, str]): LegacyExchangeDN
            prop_action (Union[Unset, int]): This user property is used to trigger actions in the client application.
                The value of the
                 property is found at UserInfo.userProps[UserInfoC.PROP_ACTION]. If the value contains the
                 String {@link #PROP_ACTION_USER_SHOULD_CHANGE_PASSWORD} the user should change the password .
                 If the value contains the String {@link #PROP_ACTION_USER_MUST_CHANGE_PASSWORD}, the user must
                 change the password. If the value contains the String {@link #PROP_ACTION_END_PASSWORD_DATE},
                 the password expires at the ISO date defined by the next 10 characters. E.g. "EX20120405" means
                 that the password expires at April 5, 2012.
            ldap_key_distinguished_name (Union[Unset, str]): Distinguished name. Key to access the map UserInfo.
                ldapProperties
            mb_desc (Union[Unset, str]): Member bit {@link UserInfo#desc}
            mb_sessions (Union[Unset, str]): Member bit {@link UserInfo#sessions}
            mb_package_name (Union[Unset, str]): Member bit {@link UserInfo#packageName}
            mb_pwd (Union[Unset, str]): Member bit {@link UserInfo#pwd}
            ln_desc (Union[Unset, int]): Maximum user desc length
            mb_name (Union[Unset, str]): Member bit {@link UserInfo#name}
            ldap_key_online (Union[Unset, str]): Online. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_exch_delegate_list_link (Union[Unset, str]): msExchDelegateListLink
            unlock_archive (Union[Unset, str]): Pass this value to unlock the archive.
            ldap_prop_online_mailbox_enabled (Union[Unset, str]): IsMailboxEnabled
            mb_t_stamp_sync (Union[Unset, str]): Member bit {@link UserInfo#tStampSync}
            ln_name (Union[Unset, int]): Maximum user name length
            ldap_prop_object_category (Union[Unset, str]): Object category
            ldap_key_exch_delegate_list_link (Union[Unset, str]): msExchDelegateListLink. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_cn (Union[Unset, str]): Common name
            ldap_key_online_mail (Union[Unset, str]): PrimarySmtpAddress. Key to access the map UserInfo.
                ldapProperties
            type_user (Union[Unset, int]): Type value for an user.
            type_group (Union[Unset, int]): Type value for a group.
            ldap_prop_admin_display_name (Union[Unset, str]): adminDisplayName
            ldap_key_user_account_control (Union[Unset, str]): Flags that control the behavior of the user account.
                Key to access the map
                 UserInfo.ldapProperties
            max_persistent_groups (Union[Unset, int]): Maximum number of persistent groups per user.
            prop_action_user_must_change_password (Union[Unset, str]): The user must change the password.
            ldap_prop_mail_nick_name (Union[Unset, str]): Mail nick name
            ldap_key_exch_journal_rcpt (Union[Unset, str]): msExchMessageJournalRecipient. Key to access the map UserInfo.
                ldapProperties
            ldap_key_member_of (Union[Unset, str]): Member of. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_online_recipient_type_details (Union[Unset, str]): RecipientTypeDetails
            ldap_key_admin_display_name (Union[Unset, str]): adminDisplayName. Key to access the map UserInfo.
                ldapProperties
            ln_pwd (Union[Unset, int]): Maximum user password length
            ldap_prop_online_guid (Union[Unset, str]): Guid
            id_administrator (Union[Unset, int]): User ID of main administrator.
            ldap_key_cn (Union[Unset, str]): Common name. Key to access the map UserInfo.
                ldapProperties
            mb_t_stamp (Union[Unset, str]): Member bit {@link UserInfo#tStamp}
            ldap_prop_distinguished_name (Union[Unset, str]): Distinguished name
            prop_guid (Union[Unset, int]): User property GUID.
            ldap_key_manager (Union[Unset, str]): Manager.
            ldap_prop_sam_account_type (Union[Unset, str]): Contains information about every account type object
            ldap_key_mail (Union[Unset, str]): Mail. Key to access the map UserInfo.
                ldapProperties
            mb_parent (Union[Unset, str]): Member bit {@link UserInfo#parent}
            ldap_key_online_guid (Union[Unset, str]): Guid. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_mail (Union[Unset, str]): Mail
            mb_org_unit_ids (Union[Unset, str]): Member bit {@link UserInfo#orgUnitIds}
            ldap_key_exch_hide_from_address_lists (Union[Unset, str]): msExchHideFromAddressLists. Key to access the map
                UserInfo.
                ldapProperties
            guid_administrator (Union[Unset, str]): GUID of main administrator
            mb_id (Union[Unset, str]): Member bit {@link UserInfo#id}
            ldap_prop_name (Union[Unset, str]): Name
            ldap_prop_exch_journal_rcpt (Union[Unset, str]): msExchMessageJournalRecipient
            ldap_key_display_name (Union[Unset, str]): Display name. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_display_name (Union[Unset, str]): Display name
            ldap_key_ms_exchange_mailbox_guid (Union[Unset, str]): Mailbox globally unique identifier. Key to access the map
                UserInfo.
                ldapProperties
            ldap_prop_ms_exchange_mailbox_guid (Union[Unset, str]): Mailbox globally unique identifier
            ldap_prop_fqdn (Union[Unset, str]): Full Qualified Domain Name
            ldap_key_domain (Union[Unset, str]): Domain.
            guid_everyone_group (Union[Unset, str]): GUID of group "Everybody"
            ldap_key_exch_owning_server (Union[Unset, str]): msExchOwningServer. Key to access the map UserInfo.
                ldapProperties
            ldap_key_online_recipient_type_details (Union[Unset, str]): RecipientTypeDetails. Key to access the map
                UserInfo.
                ldapProperties
            prop_action_end_password_date (Union[Unset, str]): The password expires.
            max_userprop (Union[Unset, int]): Maximum number of user properties.
            mb_flags (Union[Unset, str]): Member bit {@link UserInfo#flags}
            ldap_key_object_sid (Union[Unset, str]): A binary value that specifies the security identifier (SID) of the
                user.
                Key to access the map
                 UserInfo.ldapProperties
            mb_internal_user (Union[Unset, str]): Member bit {@link UserInfo#internalUser}
            ldap_key_exch_pubfolder_mailbox (Union[Unset, str]): msExchPublicFolderMailbox. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_exch_hide_from_address_lists (Union[Unset, str]): msExchHideFromAddressLists
            mb_workspace_info (Union[Unset, str]): Member bit {@link UserInfo#workspaceInfo}.
            ldap_prop_group_type (Union[Unset, str]): Group type
            ldap_key_proxy_addresses (Union[Unset, str]): Proxy addresses. Key to access the map UserInfo.
                ldapProperties
            ldap_prop_proxy_addresses (Union[Unset, str]): Proxy addresses
            ldap_prop_user_account_control (Union[Unset, str]): Flags that control the behavior of the user account
            ldap_key_sam_account_name (Union[Unset, str]): NT account name. Key to access the map UserInfo.
                ldapProperties
            pwd_value_ignore (Union[Unset, str]): This value can be set for UserInfo.
                pwd to
            mb_keylist (Union[Unset, str]): Member bit {@link UserInfo#keylist}
            prop_userdefined_3 (Union[Unset, int]): <p>
                User property defined by user
                 </p>
                 <p>
                 Constant to access array {@link UserInfo#userProps}.
                 </p>
            prop_userdefined_4 (Union[Unset, int]): <p>
                User property defined by user
                 </p>
                 <p>
                 Constant to access array {@link UserInfo#userProps}.
                 </p>
            prop_userdefined_1 (Union[Unset, int]): <p>
                User property defined by user
                 </p>
                 <p>
                 Constant to access array {@link UserInfo#userProps}.
                 </p>
            mb_type (Union[Unset, str]): Member bit {@link UserInfo#type}
            prop_userdefined_2 (Union[Unset, int]): <p>
                User property defined by user
                 </p>
                 <p>
                 Constant to access array {@link UserInfo#userProps}.
                 </p>
            ldap_key_object_category (Union[Unset, str]): Object category. Key to access the map UserInfo.
                ldapProperties
            ldap_key_name (Union[Unset, str]): Name. Key to access the map UserInfo.ldapProperties.
            id_administrators_group (Union[Unset, int]): Group ID of administrators.
            max_key (Union[Unset, int]): Maximum number of keys.
            prop_action_user_should_change_password (Union[Unset, str]): The user should change the password.
            prop_name_os (Union[Unset, int]):
            ldap_prop_online_mail (Union[Unset, str]): PrimarySmtpAddress
            ldap_prop_exch_pubfolder_mailbox (Union[Unset, str]): msExchPublicFolderMailbox
            ldap_key_fqdn (Union[Unset, str]): Full Qualified Domain Name. Key to access the map UserInfo.
                ldapProperties
            prop_userdefined_5 (Union[Unset, int]): <p>
                User property defined by user
                 </p>
                 <p>
                 Constant to access array {@link UserInfo#userProps}.
                 </p>
            ln_ldap_prop_value (Union[Unset, int]): Maximum length of LDAP property value.
            ldap_key_exch_recipient_display_type (Union[Unset, str]): msExchRecipientDisplayType. Key to access the map
                UserInfo.
                ldapProperties
            update_user_data_background_job_name (Union[Unset, str]): Background job name that updates a large number of
                user objects.
            ldap_key_object_guid (Union[Unset, str]): The unique identifier for an object. Key to access the map UserInfo.
                ldapProperties
            max_users (Union[Unset, int]): Maximale number of users and groups.
            ldap_prop_online (Union[Unset, str]): Online
            ldap_prop_object_sid (Union[Unset, str]): A binary value that specifies the security identifier (SID) of the
                user.
            ldap_prop_user_principal_name (Union[Unset, str]): User principal name
    """

    mb_superior_id: Union[Unset, str] = UNSET
    ldap_prop_object_class: Union[Unset, str] = UNSET
    ldap_key_online_mailbox_enabled: Union[Unset, str] = UNSET
    ldap_prop_exch_recipient_type_details: Union[Unset, str] = UNSET
    ldap_key_sam_account_type: Union[Unset, str] = UNSET
    ldap_key_mail_nick_name: Union[Unset, str] = UNSET
    mb_user_props: Union[Unset, str] = UNSET
    ldap_key_exch_recipient_type_details: Union[Unset, str] = UNSET
    ldap_prop_exch_owning_server: Union[Unset, str] = UNSET
    guid_eloservice: Union[Unset, str] = UNSET
    ldap_key_legacy_exchange_dn: Union[Unset, str] = UNSET
    mb_flags_2: Union[Unset, str] = UNSET
    ln_ldap_prop_key: Union[Unset, int] = UNSET
    max_name: Union[Unset, int] = UNSET
    type_userid_owner: Union[Unset, int] = UNSET
    mb_last_login_iso: Union[Unset, str] = UNSET
    ldap_prop_object_guid: Union[Unset, str] = UNSET
    ldap_prop_exch_recipient_display_type: Union[Unset, str] = UNSET
    prop_name_email: Union[Unset, int] = UNSET
    ln_user_prop: Union[Unset, int] = UNSET
    id_everyone_group: Union[Unset, int] = UNSET
    mb_group_list: Union[Unset, str] = UNSET
    max_groups: Union[Unset, int] = UNSET
    ldap_key_group_type: Union[Unset, str] = UNSET
    ldap_key_user_principal_name: Union[Unset, str] = UNSET
    ldap_key_object_class: Union[Unset, str] = UNSET
    mb_ldap_properties: Union[Unset, str] = UNSET
    ldap_prop_sam_account_name: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ldap_prop_member_of: Union[Unset, str] = UNSET
    ldap_prop_legacy_exchange_dn: Union[Unset, str] = UNSET
    prop_action: Union[Unset, int] = UNSET
    ldap_key_distinguished_name: Union[Unset, str] = UNSET
    mb_desc: Union[Unset, str] = UNSET
    mb_sessions: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_pwd: Union[Unset, str] = UNSET
    ln_desc: Union[Unset, int] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ldap_key_online: Union[Unset, str] = UNSET
    ldap_prop_exch_delegate_list_link: Union[Unset, str] = UNSET
    unlock_archive: Union[Unset, str] = UNSET
    ldap_prop_online_mailbox_enabled: Union[Unset, str] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    ldap_prop_object_category: Union[Unset, str] = UNSET
    ldap_key_exch_delegate_list_link: Union[Unset, str] = UNSET
    ldap_prop_cn: Union[Unset, str] = UNSET
    ldap_key_online_mail: Union[Unset, str] = UNSET
    type_user: Union[Unset, int] = UNSET
    type_group: Union[Unset, int] = UNSET
    ldap_prop_admin_display_name: Union[Unset, str] = UNSET
    ldap_key_user_account_control: Union[Unset, str] = UNSET
    max_persistent_groups: Union[Unset, int] = UNSET
    prop_action_user_must_change_password: Union[Unset, str] = UNSET
    ldap_prop_mail_nick_name: Union[Unset, str] = UNSET
    ldap_key_exch_journal_rcpt: Union[Unset, str] = UNSET
    ldap_key_member_of: Union[Unset, str] = UNSET
    ldap_prop_online_recipient_type_details: Union[Unset, str] = UNSET
    ldap_key_admin_display_name: Union[Unset, str] = UNSET
    ln_pwd: Union[Unset, int] = UNSET
    ldap_prop_online_guid: Union[Unset, str] = UNSET
    id_administrator: Union[Unset, int] = UNSET
    ldap_key_cn: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ldap_prop_distinguished_name: Union[Unset, str] = UNSET
    prop_guid: Union[Unset, int] = UNSET
    ldap_key_manager: Union[Unset, str] = UNSET
    ldap_prop_sam_account_type: Union[Unset, str] = UNSET
    ldap_key_mail: Union[Unset, str] = UNSET
    mb_parent: Union[Unset, str] = UNSET
    ldap_key_online_guid: Union[Unset, str] = UNSET
    ldap_prop_mail: Union[Unset, str] = UNSET
    mb_org_unit_ids: Union[Unset, str] = UNSET
    ldap_key_exch_hide_from_address_lists: Union[Unset, str] = UNSET
    guid_administrator: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    ldap_prop_name: Union[Unset, str] = UNSET
    ldap_prop_exch_journal_rcpt: Union[Unset, str] = UNSET
    ldap_key_display_name: Union[Unset, str] = UNSET
    ldap_prop_display_name: Union[Unset, str] = UNSET
    ldap_key_ms_exchange_mailbox_guid: Union[Unset, str] = UNSET
    ldap_prop_ms_exchange_mailbox_guid: Union[Unset, str] = UNSET
    ldap_prop_fqdn: Union[Unset, str] = UNSET
    ldap_key_domain: Union[Unset, str] = UNSET
    guid_everyone_group: Union[Unset, str] = UNSET
    ldap_key_exch_owning_server: Union[Unset, str] = UNSET
    ldap_key_online_recipient_type_details: Union[Unset, str] = UNSET
    prop_action_end_password_date: Union[Unset, str] = UNSET
    max_userprop: Union[Unset, int] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    ldap_key_object_sid: Union[Unset, str] = UNSET
    mb_internal_user: Union[Unset, str] = UNSET
    ldap_key_exch_pubfolder_mailbox: Union[Unset, str] = UNSET
    ldap_prop_exch_hide_from_address_lists: Union[Unset, str] = UNSET
    mb_workspace_info: Union[Unset, str] = UNSET
    ldap_prop_group_type: Union[Unset, str] = UNSET
    ldap_key_proxy_addresses: Union[Unset, str] = UNSET
    ldap_prop_proxy_addresses: Union[Unset, str] = UNSET
    ldap_prop_user_account_control: Union[Unset, str] = UNSET
    ldap_key_sam_account_name: Union[Unset, str] = UNSET
    pwd_value_ignore: Union[Unset, str] = UNSET
    mb_keylist: Union[Unset, str] = UNSET
    prop_userdefined_3: Union[Unset, int] = UNSET
    prop_userdefined_4: Union[Unset, int] = UNSET
    prop_userdefined_1: Union[Unset, int] = UNSET
    mb_type: Union[Unset, str] = UNSET
    prop_userdefined_2: Union[Unset, int] = UNSET
    ldap_key_object_category: Union[Unset, str] = UNSET
    ldap_key_name: Union[Unset, str] = UNSET
    id_administrators_group: Union[Unset, int] = UNSET
    max_key: Union[Unset, int] = UNSET
    prop_action_user_should_change_password: Union[Unset, str] = UNSET
    prop_name_os: Union[Unset, int] = UNSET
    ldap_prop_online_mail: Union[Unset, str] = UNSET
    ldap_prop_exch_pubfolder_mailbox: Union[Unset, str] = UNSET
    ldap_key_fqdn: Union[Unset, str] = UNSET
    prop_userdefined_5: Union[Unset, int] = UNSET
    ln_ldap_prop_value: Union[Unset, int] = UNSET
    ldap_key_exch_recipient_display_type: Union[Unset, str] = UNSET
    update_user_data_background_job_name: Union[Unset, str] = UNSET
    ldap_key_object_guid: Union[Unset, str] = UNSET
    max_users: Union[Unset, int] = UNSET
    ldap_prop_online: Union[Unset, str] = UNSET
    ldap_prop_object_sid: Union[Unset, str] = UNSET
    ldap_prop_user_principal_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_superior_id = self.mb_superior_id

        ldap_prop_object_class = self.ldap_prop_object_class

        ldap_key_online_mailbox_enabled = self.ldap_key_online_mailbox_enabled

        ldap_prop_exch_recipient_type_details = self.ldap_prop_exch_recipient_type_details

        ldap_key_sam_account_type = self.ldap_key_sam_account_type

        ldap_key_mail_nick_name = self.ldap_key_mail_nick_name

        mb_user_props = self.mb_user_props

        ldap_key_exch_recipient_type_details = self.ldap_key_exch_recipient_type_details

        ldap_prop_exch_owning_server = self.ldap_prop_exch_owning_server

        guid_eloservice = self.guid_eloservice

        ldap_key_legacy_exchange_dn = self.ldap_key_legacy_exchange_dn

        mb_flags_2 = self.mb_flags_2

        ln_ldap_prop_key = self.ln_ldap_prop_key

        max_name = self.max_name

        type_userid_owner = self.type_userid_owner

        mb_last_login_iso = self.mb_last_login_iso

        ldap_prop_object_guid = self.ldap_prop_object_guid

        ldap_prop_exch_recipient_display_type = self.ldap_prop_exch_recipient_display_type

        prop_name_email = self.prop_name_email

        ln_user_prop = self.ln_user_prop

        id_everyone_group = self.id_everyone_group

        mb_group_list = self.mb_group_list

        max_groups = self.max_groups

        ldap_key_group_type = self.ldap_key_group_type

        ldap_key_user_principal_name = self.ldap_key_user_principal_name

        ldap_key_object_class = self.ldap_key_object_class

        mb_ldap_properties = self.mb_ldap_properties

        ldap_prop_sam_account_name = self.ldap_prop_sam_account_name

        mb_guid = self.mb_guid

        ldap_prop_member_of = self.ldap_prop_member_of

        ldap_prop_legacy_exchange_dn = self.ldap_prop_legacy_exchange_dn

        prop_action = self.prop_action

        ldap_key_distinguished_name = self.ldap_key_distinguished_name

        mb_desc = self.mb_desc

        mb_sessions = self.mb_sessions

        mb_package_name = self.mb_package_name

        mb_pwd = self.mb_pwd

        ln_desc = self.ln_desc

        mb_name = self.mb_name

        ldap_key_online = self.ldap_key_online

        ldap_prop_exch_delegate_list_link = self.ldap_prop_exch_delegate_list_link

        unlock_archive = self.unlock_archive

        ldap_prop_online_mailbox_enabled = self.ldap_prop_online_mailbox_enabled

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_name = self.ln_name

        ldap_prop_object_category = self.ldap_prop_object_category

        ldap_key_exch_delegate_list_link = self.ldap_key_exch_delegate_list_link

        ldap_prop_cn = self.ldap_prop_cn

        ldap_key_online_mail = self.ldap_key_online_mail

        type_user = self.type_user

        type_group = self.type_group

        ldap_prop_admin_display_name = self.ldap_prop_admin_display_name

        ldap_key_user_account_control = self.ldap_key_user_account_control

        max_persistent_groups = self.max_persistent_groups

        prop_action_user_must_change_password = self.prop_action_user_must_change_password

        ldap_prop_mail_nick_name = self.ldap_prop_mail_nick_name

        ldap_key_exch_journal_rcpt = self.ldap_key_exch_journal_rcpt

        ldap_key_member_of = self.ldap_key_member_of

        ldap_prop_online_recipient_type_details = self.ldap_prop_online_recipient_type_details

        ldap_key_admin_display_name = self.ldap_key_admin_display_name

        ln_pwd = self.ln_pwd

        ldap_prop_online_guid = self.ldap_prop_online_guid

        id_administrator = self.id_administrator

        ldap_key_cn = self.ldap_key_cn

        mb_t_stamp = self.mb_t_stamp

        ldap_prop_distinguished_name = self.ldap_prop_distinguished_name

        prop_guid = self.prop_guid

        ldap_key_manager = self.ldap_key_manager

        ldap_prop_sam_account_type = self.ldap_prop_sam_account_type

        ldap_key_mail = self.ldap_key_mail

        mb_parent = self.mb_parent

        ldap_key_online_guid = self.ldap_key_online_guid

        ldap_prop_mail = self.ldap_prop_mail

        mb_org_unit_ids = self.mb_org_unit_ids

        ldap_key_exch_hide_from_address_lists = self.ldap_key_exch_hide_from_address_lists

        guid_administrator = self.guid_administrator

        mb_id = self.mb_id

        ldap_prop_name = self.ldap_prop_name

        ldap_prop_exch_journal_rcpt = self.ldap_prop_exch_journal_rcpt

        ldap_key_display_name = self.ldap_key_display_name

        ldap_prop_display_name = self.ldap_prop_display_name

        ldap_key_ms_exchange_mailbox_guid = self.ldap_key_ms_exchange_mailbox_guid

        ldap_prop_ms_exchange_mailbox_guid = self.ldap_prop_ms_exchange_mailbox_guid

        ldap_prop_fqdn = self.ldap_prop_fqdn

        ldap_key_domain = self.ldap_key_domain

        guid_everyone_group = self.guid_everyone_group

        ldap_key_exch_owning_server = self.ldap_key_exch_owning_server

        ldap_key_online_recipient_type_details = self.ldap_key_online_recipient_type_details

        prop_action_end_password_date = self.prop_action_end_password_date

        max_userprop = self.max_userprop

        mb_flags = self.mb_flags

        ldap_key_object_sid = self.ldap_key_object_sid

        mb_internal_user = self.mb_internal_user

        ldap_key_exch_pubfolder_mailbox = self.ldap_key_exch_pubfolder_mailbox

        ldap_prop_exch_hide_from_address_lists = self.ldap_prop_exch_hide_from_address_lists

        mb_workspace_info = self.mb_workspace_info

        ldap_prop_group_type = self.ldap_prop_group_type

        ldap_key_proxy_addresses = self.ldap_key_proxy_addresses

        ldap_prop_proxy_addresses = self.ldap_prop_proxy_addresses

        ldap_prop_user_account_control = self.ldap_prop_user_account_control

        ldap_key_sam_account_name = self.ldap_key_sam_account_name

        pwd_value_ignore = self.pwd_value_ignore

        mb_keylist = self.mb_keylist

        prop_userdefined_3 = self.prop_userdefined_3

        prop_userdefined_4 = self.prop_userdefined_4

        prop_userdefined_1 = self.prop_userdefined_1

        mb_type = self.mb_type

        prop_userdefined_2 = self.prop_userdefined_2

        ldap_key_object_category = self.ldap_key_object_category

        ldap_key_name = self.ldap_key_name

        id_administrators_group = self.id_administrators_group

        max_key = self.max_key

        prop_action_user_should_change_password = self.prop_action_user_should_change_password

        prop_name_os = self.prop_name_os

        ldap_prop_online_mail = self.ldap_prop_online_mail

        ldap_prop_exch_pubfolder_mailbox = self.ldap_prop_exch_pubfolder_mailbox

        ldap_key_fqdn = self.ldap_key_fqdn

        prop_userdefined_5 = self.prop_userdefined_5

        ln_ldap_prop_value = self.ln_ldap_prop_value

        ldap_key_exch_recipient_display_type = self.ldap_key_exch_recipient_display_type

        update_user_data_background_job_name = self.update_user_data_background_job_name

        ldap_key_object_guid = self.ldap_key_object_guid

        max_users = self.max_users

        ldap_prop_online = self.ldap_prop_online

        ldap_prop_object_sid = self.ldap_prop_object_sid

        ldap_prop_user_principal_name = self.ldap_prop_user_principal_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_superior_id is not UNSET:
            field_dict["mbSuperiorId"] = mb_superior_id
        if ldap_prop_object_class is not UNSET:
            field_dict["LDAP_PROP_OBJECT_CLASS"] = ldap_prop_object_class
        if ldap_key_online_mailbox_enabled is not UNSET:
            field_dict["LDAP_KEY_ONLINE_MAILBOX_ENABLED"] = ldap_key_online_mailbox_enabled
        if ldap_prop_exch_recipient_type_details is not UNSET:
            field_dict["LDAP_PROP_EXCH_RECIPIENT_TYPE_DETAILS"] = ldap_prop_exch_recipient_type_details
        if ldap_key_sam_account_type is not UNSET:
            field_dict["LDAP_KEY_SAM_ACCOUNT_TYPE"] = ldap_key_sam_account_type
        if ldap_key_mail_nick_name is not UNSET:
            field_dict["LDAP_KEY_MAIL_NICK_NAME"] = ldap_key_mail_nick_name
        if mb_user_props is not UNSET:
            field_dict["mbUserProps"] = mb_user_props
        if ldap_key_exch_recipient_type_details is not UNSET:
            field_dict["LDAP_KEY_EXCH_RECIPIENT_TYPE_DETAILS"] = ldap_key_exch_recipient_type_details
        if ldap_prop_exch_owning_server is not UNSET:
            field_dict["LDAP_PROP_EXCH_OWNING_SERVER"] = ldap_prop_exch_owning_server
        if guid_eloservice is not UNSET:
            field_dict["GUID_ELOSERVICE"] = guid_eloservice
        if ldap_key_legacy_exchange_dn is not UNSET:
            field_dict["LDAP_KEY_LEGACY_EXCHANGE_DN"] = ldap_key_legacy_exchange_dn
        if mb_flags_2 is not UNSET:
            field_dict["mbFlags2"] = mb_flags_2
        if ln_ldap_prop_key is not UNSET:
            field_dict["lnLdapPropKey"] = ln_ldap_prop_key
        if max_name is not UNSET:
            field_dict["MAX_NAME"] = max_name
        if type_userid_owner is not UNSET:
            field_dict["TYPE_USERID_OWNER"] = type_userid_owner
        if mb_last_login_iso is not UNSET:
            field_dict["mbLastLoginIso"] = mb_last_login_iso
        if ldap_prop_object_guid is not UNSET:
            field_dict["LDAP_PROP_OBJECT_GUID"] = ldap_prop_object_guid
        if ldap_prop_exch_recipient_display_type is not UNSET:
            field_dict["LDAP_PROP_EXCH_RECIPIENT_DISPLAY_TYPE"] = ldap_prop_exch_recipient_display_type
        if prop_name_email is not UNSET:
            field_dict["PROP_NAME_EMAIL"] = prop_name_email
        if ln_user_prop is not UNSET:
            field_dict["lnUserProp"] = ln_user_prop
        if id_everyone_group is not UNSET:
            field_dict["ID_EVERYONE_GROUP"] = id_everyone_group
        if mb_group_list is not UNSET:
            field_dict["mbGroupList"] = mb_group_list
        if max_groups is not UNSET:
            field_dict["MAX_GROUPS"] = max_groups
        if ldap_key_group_type is not UNSET:
            field_dict["LDAP_KEY_GROUP_TYPE"] = ldap_key_group_type
        if ldap_key_user_principal_name is not UNSET:
            field_dict["LDAP_KEY_USER_PRINCIPAL_NAME"] = ldap_key_user_principal_name
        if ldap_key_object_class is not UNSET:
            field_dict["LDAP_KEY_OBJECT_CLASS"] = ldap_key_object_class
        if mb_ldap_properties is not UNSET:
            field_dict["mbLdapProperties"] = mb_ldap_properties
        if ldap_prop_sam_account_name is not UNSET:
            field_dict["LDAP_PROP_SAM_ACCOUNT_NAME"] = ldap_prop_sam_account_name
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ldap_prop_member_of is not UNSET:
            field_dict["LDAP_PROP_MEMBER_OF"] = ldap_prop_member_of
        if ldap_prop_legacy_exchange_dn is not UNSET:
            field_dict["LDAP_PROP_LEGACY_EXCHANGE_DN"] = ldap_prop_legacy_exchange_dn
        if prop_action is not UNSET:
            field_dict["PROP_ACTION"] = prop_action
        if ldap_key_distinguished_name is not UNSET:
            field_dict["LDAP_KEY_DISTINGUISHED_NAME"] = ldap_key_distinguished_name
        if mb_desc is not UNSET:
            field_dict["mbDesc"] = mb_desc
        if mb_sessions is not UNSET:
            field_dict["mbSessions"] = mb_sessions
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_pwd is not UNSET:
            field_dict["mbPwd"] = mb_pwd
        if ln_desc is not UNSET:
            field_dict["lnDesc"] = ln_desc
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ldap_key_online is not UNSET:
            field_dict["LDAP_KEY_ONLINE"] = ldap_key_online
        if ldap_prop_exch_delegate_list_link is not UNSET:
            field_dict["LDAP_PROP_EXCH_DELEGATE_LIST_LINK"] = ldap_prop_exch_delegate_list_link
        if unlock_archive is not UNSET:
            field_dict["UNLOCK_ARCHIVE"] = unlock_archive
        if ldap_prop_online_mailbox_enabled is not UNSET:
            field_dict["LDAP_PROP_ONLINE_MAILBOX_ENABLED"] = ldap_prop_online_mailbox_enabled
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if ldap_prop_object_category is not UNSET:
            field_dict["LDAP_PROP_OBJECT_CATEGORY"] = ldap_prop_object_category
        if ldap_key_exch_delegate_list_link is not UNSET:
            field_dict["LDAP_KEY_EXCH_DELEGATE_LIST_LINK"] = ldap_key_exch_delegate_list_link
        if ldap_prop_cn is not UNSET:
            field_dict["LDAP_PROP_CN"] = ldap_prop_cn
        if ldap_key_online_mail is not UNSET:
            field_dict["LDAP_KEY_ONLINE_MAIL"] = ldap_key_online_mail
        if type_user is not UNSET:
            field_dict["TYPE_USER"] = type_user
        if type_group is not UNSET:
            field_dict["TYPE_GROUP"] = type_group
        if ldap_prop_admin_display_name is not UNSET:
            field_dict["LDAP_PROP_ADMIN_DISPLAY_NAME"] = ldap_prop_admin_display_name
        if ldap_key_user_account_control is not UNSET:
            field_dict["LDAP_KEY_USER_ACCOUNT_CONTROL"] = ldap_key_user_account_control
        if max_persistent_groups is not UNSET:
            field_dict["MAX_PERSISTENT_GROUPS"] = max_persistent_groups
        if prop_action_user_must_change_password is not UNSET:
            field_dict["PROP_ACTION_USER_MUST_CHANGE_PASSWORD"] = prop_action_user_must_change_password
        if ldap_prop_mail_nick_name is not UNSET:
            field_dict["LDAP_PROP_MAIL_NICK_NAME"] = ldap_prop_mail_nick_name
        if ldap_key_exch_journal_rcpt is not UNSET:
            field_dict["LDAP_KEY_EXCH_JOURNAL_RCPT"] = ldap_key_exch_journal_rcpt
        if ldap_key_member_of is not UNSET:
            field_dict["LDAP_KEY_MEMBER_OF"] = ldap_key_member_of
        if ldap_prop_online_recipient_type_details is not UNSET:
            field_dict["LDAP_PROP_ONLINE_RECIPIENT_TYPE_DETAILS"] = ldap_prop_online_recipient_type_details
        if ldap_key_admin_display_name is not UNSET:
            field_dict["LDAP_KEY_ADMIN_DISPLAY_NAME"] = ldap_key_admin_display_name
        if ln_pwd is not UNSET:
            field_dict["lnPwd"] = ln_pwd
        if ldap_prop_online_guid is not UNSET:
            field_dict["LDAP_PROP_ONLINE_GUID"] = ldap_prop_online_guid
        if id_administrator is not UNSET:
            field_dict["ID_ADMINISTRATOR"] = id_administrator
        if ldap_key_cn is not UNSET:
            field_dict["LDAP_KEY_CN"] = ldap_key_cn
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ldap_prop_distinguished_name is not UNSET:
            field_dict["LDAP_PROP_DISTINGUISHED_NAME"] = ldap_prop_distinguished_name
        if prop_guid is not UNSET:
            field_dict["PROP_GUID"] = prop_guid
        if ldap_key_manager is not UNSET:
            field_dict["LDAP_KEY_MANAGER"] = ldap_key_manager
        if ldap_prop_sam_account_type is not UNSET:
            field_dict["LDAP_PROP_SAM_ACCOUNT_TYPE"] = ldap_prop_sam_account_type
        if ldap_key_mail is not UNSET:
            field_dict["LDAP_KEY_MAIL"] = ldap_key_mail
        if mb_parent is not UNSET:
            field_dict["mbParent"] = mb_parent
        if ldap_key_online_guid is not UNSET:
            field_dict["LDAP_KEY_ONLINE_GUID"] = ldap_key_online_guid
        if ldap_prop_mail is not UNSET:
            field_dict["LDAP_PROP_MAIL"] = ldap_prop_mail
        if mb_org_unit_ids is not UNSET:
            field_dict["mbOrgUnitIds"] = mb_org_unit_ids
        if ldap_key_exch_hide_from_address_lists is not UNSET:
            field_dict["LDAP_KEY_EXCH_HIDE_FROM_ADDRESS_LISTS"] = ldap_key_exch_hide_from_address_lists
        if guid_administrator is not UNSET:
            field_dict["GUID_ADMINISTRATOR"] = guid_administrator
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if ldap_prop_name is not UNSET:
            field_dict["LDAP_PROP_NAME"] = ldap_prop_name
        if ldap_prop_exch_journal_rcpt is not UNSET:
            field_dict["LDAP_PROP_EXCH_JOURNAL_RCPT"] = ldap_prop_exch_journal_rcpt
        if ldap_key_display_name is not UNSET:
            field_dict["LDAP_KEY_DISPLAY_NAME"] = ldap_key_display_name
        if ldap_prop_display_name is not UNSET:
            field_dict["LDAP_PROP_DISPLAY_NAME"] = ldap_prop_display_name
        if ldap_key_ms_exchange_mailbox_guid is not UNSET:
            field_dict["LDAP_KEY_MS_EXCHANGE_MAILBOX_GUID"] = ldap_key_ms_exchange_mailbox_guid
        if ldap_prop_ms_exchange_mailbox_guid is not UNSET:
            field_dict["LDAP_PROP_MS_EXCHANGE_MAILBOX_GUID"] = ldap_prop_ms_exchange_mailbox_guid
        if ldap_prop_fqdn is not UNSET:
            field_dict["LDAP_PROP_FQDN"] = ldap_prop_fqdn
        if ldap_key_domain is not UNSET:
            field_dict["LDAP_KEY_DOMAIN"] = ldap_key_domain
        if guid_everyone_group is not UNSET:
            field_dict["GUID_EVERYONE_GROUP"] = guid_everyone_group
        if ldap_key_exch_owning_server is not UNSET:
            field_dict["LDAP_KEY_EXCH_OWNING_SERVER"] = ldap_key_exch_owning_server
        if ldap_key_online_recipient_type_details is not UNSET:
            field_dict["LDAP_KEY_ONLINE_RECIPIENT_TYPE_DETAILS"] = ldap_key_online_recipient_type_details
        if prop_action_end_password_date is not UNSET:
            field_dict["PROP_ACTION_END_PASSWORD_DATE"] = prop_action_end_password_date
        if max_userprop is not UNSET:
            field_dict["MAX_USERPROP"] = max_userprop
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if ldap_key_object_sid is not UNSET:
            field_dict["LDAP_KEY_OBJECT_SID"] = ldap_key_object_sid
        if mb_internal_user is not UNSET:
            field_dict["mbInternalUser"] = mb_internal_user
        if ldap_key_exch_pubfolder_mailbox is not UNSET:
            field_dict["LDAP_KEY_EXCH_PUBFOLDER_MAILBOX"] = ldap_key_exch_pubfolder_mailbox
        if ldap_prop_exch_hide_from_address_lists is not UNSET:
            field_dict["LDAP_PROP_EXCH_HIDE_FROM_ADDRESS_LISTS"] = ldap_prop_exch_hide_from_address_lists
        if mb_workspace_info is not UNSET:
            field_dict["mbWorkspaceInfo"] = mb_workspace_info
        if ldap_prop_group_type is not UNSET:
            field_dict["LDAP_PROP_GROUP_TYPE"] = ldap_prop_group_type
        if ldap_key_proxy_addresses is not UNSET:
            field_dict["LDAP_KEY_PROXY_ADDRESSES"] = ldap_key_proxy_addresses
        if ldap_prop_proxy_addresses is not UNSET:
            field_dict["LDAP_PROP_PROXY_ADDRESSES"] = ldap_prop_proxy_addresses
        if ldap_prop_user_account_control is not UNSET:
            field_dict["LDAP_PROP_USER_ACCOUNT_CONTROL"] = ldap_prop_user_account_control
        if ldap_key_sam_account_name is not UNSET:
            field_dict["LDAP_KEY_SAM_ACCOUNT_NAME"] = ldap_key_sam_account_name
        if pwd_value_ignore is not UNSET:
            field_dict["PWD_VALUE_IGNORE"] = pwd_value_ignore
        if mb_keylist is not UNSET:
            field_dict["mbKeylist"] = mb_keylist
        if prop_userdefined_3 is not UNSET:
            field_dict["PROP_USERDEFINED_3"] = prop_userdefined_3
        if prop_userdefined_4 is not UNSET:
            field_dict["PROP_USERDEFINED_4"] = prop_userdefined_4
        if prop_userdefined_1 is not UNSET:
            field_dict["PROP_USERDEFINED_1"] = prop_userdefined_1
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if prop_userdefined_2 is not UNSET:
            field_dict["PROP_USERDEFINED_2"] = prop_userdefined_2
        if ldap_key_object_category is not UNSET:
            field_dict["LDAP_KEY_OBJECT_CATEGORY"] = ldap_key_object_category
        if ldap_key_name is not UNSET:
            field_dict["LDAP_KEY_NAME"] = ldap_key_name
        if id_administrators_group is not UNSET:
            field_dict["ID_ADMINISTRATORS_GROUP"] = id_administrators_group
        if max_key is not UNSET:
            field_dict["MAX_KEY"] = max_key
        if prop_action_user_should_change_password is not UNSET:
            field_dict["PROP_ACTION_USER_SHOULD_CHANGE_PASSWORD"] = prop_action_user_should_change_password
        if prop_name_os is not UNSET:
            field_dict["PROP_NAME_OS"] = prop_name_os
        if ldap_prop_online_mail is not UNSET:
            field_dict["LDAP_PROP_ONLINE_MAIL"] = ldap_prop_online_mail
        if ldap_prop_exch_pubfolder_mailbox is not UNSET:
            field_dict["LDAP_PROP_EXCH_PUBFOLDER_MAILBOX"] = ldap_prop_exch_pubfolder_mailbox
        if ldap_key_fqdn is not UNSET:
            field_dict["LDAP_KEY_FQDN"] = ldap_key_fqdn
        if prop_userdefined_5 is not UNSET:
            field_dict["PROP_USERDEFINED_5"] = prop_userdefined_5
        if ln_ldap_prop_value is not UNSET:
            field_dict["lnLdapPropValue"] = ln_ldap_prop_value
        if ldap_key_exch_recipient_display_type is not UNSET:
            field_dict["LDAP_KEY_EXCH_RECIPIENT_DISPLAY_TYPE"] = ldap_key_exch_recipient_display_type
        if update_user_data_background_job_name is not UNSET:
            field_dict["UPDATE_USER_DATA_BACKGROUND_JOB_NAME"] = update_user_data_background_job_name
        if ldap_key_object_guid is not UNSET:
            field_dict["LDAP_KEY_OBJECT_GUID"] = ldap_key_object_guid
        if max_users is not UNSET:
            field_dict["MAX_USERS"] = max_users
        if ldap_prop_online is not UNSET:
            field_dict["LDAP_PROP_ONLINE"] = ldap_prop_online
        if ldap_prop_object_sid is not UNSET:
            field_dict["LDAP_PROP_OBJECT_SID"] = ldap_prop_object_sid
        if ldap_prop_user_principal_name is not UNSET:
            field_dict["LDAP_PROP_USER_PRINCIPAL_NAME"] = ldap_prop_user_principal_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_superior_id = d.pop("mbSuperiorId", UNSET)

        ldap_prop_object_class = d.pop("LDAP_PROP_OBJECT_CLASS", UNSET)

        ldap_key_online_mailbox_enabled = d.pop("LDAP_KEY_ONLINE_MAILBOX_ENABLED", UNSET)

        ldap_prop_exch_recipient_type_details = d.pop("LDAP_PROP_EXCH_RECIPIENT_TYPE_DETAILS", UNSET)

        ldap_key_sam_account_type = d.pop("LDAP_KEY_SAM_ACCOUNT_TYPE", UNSET)

        ldap_key_mail_nick_name = d.pop("LDAP_KEY_MAIL_NICK_NAME", UNSET)

        mb_user_props = d.pop("mbUserProps", UNSET)

        ldap_key_exch_recipient_type_details = d.pop("LDAP_KEY_EXCH_RECIPIENT_TYPE_DETAILS", UNSET)

        ldap_prop_exch_owning_server = d.pop("LDAP_PROP_EXCH_OWNING_SERVER", UNSET)

        guid_eloservice = d.pop("GUID_ELOSERVICE", UNSET)

        ldap_key_legacy_exchange_dn = d.pop("LDAP_KEY_LEGACY_EXCHANGE_DN", UNSET)

        mb_flags_2 = d.pop("mbFlags2", UNSET)

        ln_ldap_prop_key = d.pop("lnLdapPropKey", UNSET)

        max_name = d.pop("MAX_NAME", UNSET)

        type_userid_owner = d.pop("TYPE_USERID_OWNER", UNSET)

        mb_last_login_iso = d.pop("mbLastLoginIso", UNSET)

        ldap_prop_object_guid = d.pop("LDAP_PROP_OBJECT_GUID", UNSET)

        ldap_prop_exch_recipient_display_type = d.pop("LDAP_PROP_EXCH_RECIPIENT_DISPLAY_TYPE", UNSET)

        prop_name_email = d.pop("PROP_NAME_EMAIL", UNSET)

        ln_user_prop = d.pop("lnUserProp", UNSET)

        id_everyone_group = d.pop("ID_EVERYONE_GROUP", UNSET)

        mb_group_list = d.pop("mbGroupList", UNSET)

        max_groups = d.pop("MAX_GROUPS", UNSET)

        ldap_key_group_type = d.pop("LDAP_KEY_GROUP_TYPE", UNSET)

        ldap_key_user_principal_name = d.pop("LDAP_KEY_USER_PRINCIPAL_NAME", UNSET)

        ldap_key_object_class = d.pop("LDAP_KEY_OBJECT_CLASS", UNSET)

        mb_ldap_properties = d.pop("mbLdapProperties", UNSET)

        ldap_prop_sam_account_name = d.pop("LDAP_PROP_SAM_ACCOUNT_NAME", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ldap_prop_member_of = d.pop("LDAP_PROP_MEMBER_OF", UNSET)

        ldap_prop_legacy_exchange_dn = d.pop("LDAP_PROP_LEGACY_EXCHANGE_DN", UNSET)

        prop_action = d.pop("PROP_ACTION", UNSET)

        ldap_key_distinguished_name = d.pop("LDAP_KEY_DISTINGUISHED_NAME", UNSET)

        mb_desc = d.pop("mbDesc", UNSET)

        mb_sessions = d.pop("mbSessions", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_pwd = d.pop("mbPwd", UNSET)

        ln_desc = d.pop("lnDesc", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ldap_key_online = d.pop("LDAP_KEY_ONLINE", UNSET)

        ldap_prop_exch_delegate_list_link = d.pop("LDAP_PROP_EXCH_DELEGATE_LIST_LINK", UNSET)

        unlock_archive = d.pop("UNLOCK_ARCHIVE", UNSET)

        ldap_prop_online_mailbox_enabled = d.pop("LDAP_PROP_ONLINE_MAILBOX_ENABLED", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_name = d.pop("lnName", UNSET)

        ldap_prop_object_category = d.pop("LDAP_PROP_OBJECT_CATEGORY", UNSET)

        ldap_key_exch_delegate_list_link = d.pop("LDAP_KEY_EXCH_DELEGATE_LIST_LINK", UNSET)

        ldap_prop_cn = d.pop("LDAP_PROP_CN", UNSET)

        ldap_key_online_mail = d.pop("LDAP_KEY_ONLINE_MAIL", UNSET)

        type_user = d.pop("TYPE_USER", UNSET)

        type_group = d.pop("TYPE_GROUP", UNSET)

        ldap_prop_admin_display_name = d.pop("LDAP_PROP_ADMIN_DISPLAY_NAME", UNSET)

        ldap_key_user_account_control = d.pop("LDAP_KEY_USER_ACCOUNT_CONTROL", UNSET)

        max_persistent_groups = d.pop("MAX_PERSISTENT_GROUPS", UNSET)

        prop_action_user_must_change_password = d.pop("PROP_ACTION_USER_MUST_CHANGE_PASSWORD", UNSET)

        ldap_prop_mail_nick_name = d.pop("LDAP_PROP_MAIL_NICK_NAME", UNSET)

        ldap_key_exch_journal_rcpt = d.pop("LDAP_KEY_EXCH_JOURNAL_RCPT", UNSET)

        ldap_key_member_of = d.pop("LDAP_KEY_MEMBER_OF", UNSET)

        ldap_prop_online_recipient_type_details = d.pop("LDAP_PROP_ONLINE_RECIPIENT_TYPE_DETAILS", UNSET)

        ldap_key_admin_display_name = d.pop("LDAP_KEY_ADMIN_DISPLAY_NAME", UNSET)

        ln_pwd = d.pop("lnPwd", UNSET)

        ldap_prop_online_guid = d.pop("LDAP_PROP_ONLINE_GUID", UNSET)

        id_administrator = d.pop("ID_ADMINISTRATOR", UNSET)

        ldap_key_cn = d.pop("LDAP_KEY_CN", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ldap_prop_distinguished_name = d.pop("LDAP_PROP_DISTINGUISHED_NAME", UNSET)

        prop_guid = d.pop("PROP_GUID", UNSET)

        ldap_key_manager = d.pop("LDAP_KEY_MANAGER", UNSET)

        ldap_prop_sam_account_type = d.pop("LDAP_PROP_SAM_ACCOUNT_TYPE", UNSET)

        ldap_key_mail = d.pop("LDAP_KEY_MAIL", UNSET)

        mb_parent = d.pop("mbParent", UNSET)

        ldap_key_online_guid = d.pop("LDAP_KEY_ONLINE_GUID", UNSET)

        ldap_prop_mail = d.pop("LDAP_PROP_MAIL", UNSET)

        mb_org_unit_ids = d.pop("mbOrgUnitIds", UNSET)

        ldap_key_exch_hide_from_address_lists = d.pop("LDAP_KEY_EXCH_HIDE_FROM_ADDRESS_LISTS", UNSET)

        guid_administrator = d.pop("GUID_ADMINISTRATOR", UNSET)

        mb_id = d.pop("mbId", UNSET)

        ldap_prop_name = d.pop("LDAP_PROP_NAME", UNSET)

        ldap_prop_exch_journal_rcpt = d.pop("LDAP_PROP_EXCH_JOURNAL_RCPT", UNSET)

        ldap_key_display_name = d.pop("LDAP_KEY_DISPLAY_NAME", UNSET)

        ldap_prop_display_name = d.pop("LDAP_PROP_DISPLAY_NAME", UNSET)

        ldap_key_ms_exchange_mailbox_guid = d.pop("LDAP_KEY_MS_EXCHANGE_MAILBOX_GUID", UNSET)

        ldap_prop_ms_exchange_mailbox_guid = d.pop("LDAP_PROP_MS_EXCHANGE_MAILBOX_GUID", UNSET)

        ldap_prop_fqdn = d.pop("LDAP_PROP_FQDN", UNSET)

        ldap_key_domain = d.pop("LDAP_KEY_DOMAIN", UNSET)

        guid_everyone_group = d.pop("GUID_EVERYONE_GROUP", UNSET)

        ldap_key_exch_owning_server = d.pop("LDAP_KEY_EXCH_OWNING_SERVER", UNSET)

        ldap_key_online_recipient_type_details = d.pop("LDAP_KEY_ONLINE_RECIPIENT_TYPE_DETAILS", UNSET)

        prop_action_end_password_date = d.pop("PROP_ACTION_END_PASSWORD_DATE", UNSET)

        max_userprop = d.pop("MAX_USERPROP", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        ldap_key_object_sid = d.pop("LDAP_KEY_OBJECT_SID", UNSET)

        mb_internal_user = d.pop("mbInternalUser", UNSET)

        ldap_key_exch_pubfolder_mailbox = d.pop("LDAP_KEY_EXCH_PUBFOLDER_MAILBOX", UNSET)

        ldap_prop_exch_hide_from_address_lists = d.pop("LDAP_PROP_EXCH_HIDE_FROM_ADDRESS_LISTS", UNSET)

        mb_workspace_info = d.pop("mbWorkspaceInfo", UNSET)

        ldap_prop_group_type = d.pop("LDAP_PROP_GROUP_TYPE", UNSET)

        ldap_key_proxy_addresses = d.pop("LDAP_KEY_PROXY_ADDRESSES", UNSET)

        ldap_prop_proxy_addresses = d.pop("LDAP_PROP_PROXY_ADDRESSES", UNSET)

        ldap_prop_user_account_control = d.pop("LDAP_PROP_USER_ACCOUNT_CONTROL", UNSET)

        ldap_key_sam_account_name = d.pop("LDAP_KEY_SAM_ACCOUNT_NAME", UNSET)

        pwd_value_ignore = d.pop("PWD_VALUE_IGNORE", UNSET)

        mb_keylist = d.pop("mbKeylist", UNSET)

        prop_userdefined_3 = d.pop("PROP_USERDEFINED_3", UNSET)

        prop_userdefined_4 = d.pop("PROP_USERDEFINED_4", UNSET)

        prop_userdefined_1 = d.pop("PROP_USERDEFINED_1", UNSET)

        mb_type = d.pop("mbType", UNSET)

        prop_userdefined_2 = d.pop("PROP_USERDEFINED_2", UNSET)

        ldap_key_object_category = d.pop("LDAP_KEY_OBJECT_CATEGORY", UNSET)

        ldap_key_name = d.pop("LDAP_KEY_NAME", UNSET)

        id_administrators_group = d.pop("ID_ADMINISTRATORS_GROUP", UNSET)

        max_key = d.pop("MAX_KEY", UNSET)

        prop_action_user_should_change_password = d.pop("PROP_ACTION_USER_SHOULD_CHANGE_PASSWORD", UNSET)

        prop_name_os = d.pop("PROP_NAME_OS", UNSET)

        ldap_prop_online_mail = d.pop("LDAP_PROP_ONLINE_MAIL", UNSET)

        ldap_prop_exch_pubfolder_mailbox = d.pop("LDAP_PROP_EXCH_PUBFOLDER_MAILBOX", UNSET)

        ldap_key_fqdn = d.pop("LDAP_KEY_FQDN", UNSET)

        prop_userdefined_5 = d.pop("PROP_USERDEFINED_5", UNSET)

        ln_ldap_prop_value = d.pop("lnLdapPropValue", UNSET)

        ldap_key_exch_recipient_display_type = d.pop("LDAP_KEY_EXCH_RECIPIENT_DISPLAY_TYPE", UNSET)

        update_user_data_background_job_name = d.pop("UPDATE_USER_DATA_BACKGROUND_JOB_NAME", UNSET)

        ldap_key_object_guid = d.pop("LDAP_KEY_OBJECT_GUID", UNSET)

        max_users = d.pop("MAX_USERS", UNSET)

        ldap_prop_online = d.pop("LDAP_PROP_ONLINE", UNSET)

        ldap_prop_object_sid = d.pop("LDAP_PROP_OBJECT_SID", UNSET)

        ldap_prop_user_principal_name = d.pop("LDAP_PROP_USER_PRINCIPAL_NAME", UNSET)

        user_info_c = cls(
            mb_superior_id=mb_superior_id,
            ldap_prop_object_class=ldap_prop_object_class,
            ldap_key_online_mailbox_enabled=ldap_key_online_mailbox_enabled,
            ldap_prop_exch_recipient_type_details=ldap_prop_exch_recipient_type_details,
            ldap_key_sam_account_type=ldap_key_sam_account_type,
            ldap_key_mail_nick_name=ldap_key_mail_nick_name,
            mb_user_props=mb_user_props,
            ldap_key_exch_recipient_type_details=ldap_key_exch_recipient_type_details,
            ldap_prop_exch_owning_server=ldap_prop_exch_owning_server,
            guid_eloservice=guid_eloservice,
            ldap_key_legacy_exchange_dn=ldap_key_legacy_exchange_dn,
            mb_flags_2=mb_flags_2,
            ln_ldap_prop_key=ln_ldap_prop_key,
            max_name=max_name,
            type_userid_owner=type_userid_owner,
            mb_last_login_iso=mb_last_login_iso,
            ldap_prop_object_guid=ldap_prop_object_guid,
            ldap_prop_exch_recipient_display_type=ldap_prop_exch_recipient_display_type,
            prop_name_email=prop_name_email,
            ln_user_prop=ln_user_prop,
            id_everyone_group=id_everyone_group,
            mb_group_list=mb_group_list,
            max_groups=max_groups,
            ldap_key_group_type=ldap_key_group_type,
            ldap_key_user_principal_name=ldap_key_user_principal_name,
            ldap_key_object_class=ldap_key_object_class,
            mb_ldap_properties=mb_ldap_properties,
            ldap_prop_sam_account_name=ldap_prop_sam_account_name,
            mb_guid=mb_guid,
            ldap_prop_member_of=ldap_prop_member_of,
            ldap_prop_legacy_exchange_dn=ldap_prop_legacy_exchange_dn,
            prop_action=prop_action,
            ldap_key_distinguished_name=ldap_key_distinguished_name,
            mb_desc=mb_desc,
            mb_sessions=mb_sessions,
            mb_package_name=mb_package_name,
            mb_pwd=mb_pwd,
            ln_desc=ln_desc,
            mb_name=mb_name,
            ldap_key_online=ldap_key_online,
            ldap_prop_exch_delegate_list_link=ldap_prop_exch_delegate_list_link,
            unlock_archive=unlock_archive,
            ldap_prop_online_mailbox_enabled=ldap_prop_online_mailbox_enabled,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_name=ln_name,
            ldap_prop_object_category=ldap_prop_object_category,
            ldap_key_exch_delegate_list_link=ldap_key_exch_delegate_list_link,
            ldap_prop_cn=ldap_prop_cn,
            ldap_key_online_mail=ldap_key_online_mail,
            type_user=type_user,
            type_group=type_group,
            ldap_prop_admin_display_name=ldap_prop_admin_display_name,
            ldap_key_user_account_control=ldap_key_user_account_control,
            max_persistent_groups=max_persistent_groups,
            prop_action_user_must_change_password=prop_action_user_must_change_password,
            ldap_prop_mail_nick_name=ldap_prop_mail_nick_name,
            ldap_key_exch_journal_rcpt=ldap_key_exch_journal_rcpt,
            ldap_key_member_of=ldap_key_member_of,
            ldap_prop_online_recipient_type_details=ldap_prop_online_recipient_type_details,
            ldap_key_admin_display_name=ldap_key_admin_display_name,
            ln_pwd=ln_pwd,
            ldap_prop_online_guid=ldap_prop_online_guid,
            id_administrator=id_administrator,
            ldap_key_cn=ldap_key_cn,
            mb_t_stamp=mb_t_stamp,
            ldap_prop_distinguished_name=ldap_prop_distinguished_name,
            prop_guid=prop_guid,
            ldap_key_manager=ldap_key_manager,
            ldap_prop_sam_account_type=ldap_prop_sam_account_type,
            ldap_key_mail=ldap_key_mail,
            mb_parent=mb_parent,
            ldap_key_online_guid=ldap_key_online_guid,
            ldap_prop_mail=ldap_prop_mail,
            mb_org_unit_ids=mb_org_unit_ids,
            ldap_key_exch_hide_from_address_lists=ldap_key_exch_hide_from_address_lists,
            guid_administrator=guid_administrator,
            mb_id=mb_id,
            ldap_prop_name=ldap_prop_name,
            ldap_prop_exch_journal_rcpt=ldap_prop_exch_journal_rcpt,
            ldap_key_display_name=ldap_key_display_name,
            ldap_prop_display_name=ldap_prop_display_name,
            ldap_key_ms_exchange_mailbox_guid=ldap_key_ms_exchange_mailbox_guid,
            ldap_prop_ms_exchange_mailbox_guid=ldap_prop_ms_exchange_mailbox_guid,
            ldap_prop_fqdn=ldap_prop_fqdn,
            ldap_key_domain=ldap_key_domain,
            guid_everyone_group=guid_everyone_group,
            ldap_key_exch_owning_server=ldap_key_exch_owning_server,
            ldap_key_online_recipient_type_details=ldap_key_online_recipient_type_details,
            prop_action_end_password_date=prop_action_end_password_date,
            max_userprop=max_userprop,
            mb_flags=mb_flags,
            ldap_key_object_sid=ldap_key_object_sid,
            mb_internal_user=mb_internal_user,
            ldap_key_exch_pubfolder_mailbox=ldap_key_exch_pubfolder_mailbox,
            ldap_prop_exch_hide_from_address_lists=ldap_prop_exch_hide_from_address_lists,
            mb_workspace_info=mb_workspace_info,
            ldap_prop_group_type=ldap_prop_group_type,
            ldap_key_proxy_addresses=ldap_key_proxy_addresses,
            ldap_prop_proxy_addresses=ldap_prop_proxy_addresses,
            ldap_prop_user_account_control=ldap_prop_user_account_control,
            ldap_key_sam_account_name=ldap_key_sam_account_name,
            pwd_value_ignore=pwd_value_ignore,
            mb_keylist=mb_keylist,
            prop_userdefined_3=prop_userdefined_3,
            prop_userdefined_4=prop_userdefined_4,
            prop_userdefined_1=prop_userdefined_1,
            mb_type=mb_type,
            prop_userdefined_2=prop_userdefined_2,
            ldap_key_object_category=ldap_key_object_category,
            ldap_key_name=ldap_key_name,
            id_administrators_group=id_administrators_group,
            max_key=max_key,
            prop_action_user_should_change_password=prop_action_user_should_change_password,
            prop_name_os=prop_name_os,
            ldap_prop_online_mail=ldap_prop_online_mail,
            ldap_prop_exch_pubfolder_mailbox=ldap_prop_exch_pubfolder_mailbox,
            ldap_key_fqdn=ldap_key_fqdn,
            prop_userdefined_5=prop_userdefined_5,
            ln_ldap_prop_value=ln_ldap_prop_value,
            ldap_key_exch_recipient_display_type=ldap_key_exch_recipient_display_type,
            update_user_data_background_job_name=update_user_data_background_job_name,
            ldap_key_object_guid=ldap_key_object_guid,
            max_users=max_users,
            ldap_prop_online=ldap_prop_online,
            ldap_prop_object_sid=ldap_prop_object_sid,
            ldap_prop_user_principal_name=ldap_prop_user_principal_name,
        )

        user_info_c.additional_properties = d
        return user_info_c

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
