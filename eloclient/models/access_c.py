from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessC")


@_attrs_define
class AccessC:
    """<p>
    This class defines constants for access rights.
     </p>
     <p>
     The

     <pre>
     <code>FLAG_*</code>
     </pre>

     constants are used in

     <pre>
     <code>UserInfo.flags.
     The <pre><code>LUR_*</code>
     </pre>

     constants are used in access control lists.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            flags_not_to_inherit (Union[Unset, int]): Rights (UserInfo.flags) which are not inherited from groups the user
                is a member.
            lur_write (Union[Unset, int]): Access control right for writing an archive entry.
            flag2_all (Union[Unset, int]): User right: all rights for {@link UserInfo#flags2}. Default flags2 value for
                administrators.
            flag_deldoc (Union[Unset, int]): Delete documents.
            flag2_functional_role (Union[Unset, int]): Functional role that can be chosen by the user.
            flag2_visible_user (Union[Unset, int]): User right: user is visible in a select box. This value has to be used
                in the UserInfo.
                flags2
                 member.
            flags_exclusive_for_groups (Union[Unset, int]): These rights are removed from UserInfo.flags if UserInfo.type ==
                UserInfoC.
                TYPE_USER
            flag_hasfileaccess (Union[Unset, int]): Read document file.
            flag2_is_dms_desktop_user (Union[Unset, int]): User right: user works with ELO DMS Desktop. This value has to be
                used in the UserInfo.
                flags2
                 member.
            flag_admin (Union[Unset, int]): Main administrator, can edit all users and groups.
            flag_ignoreacl (Union[Unset, int]): Ignore access control lists.
            flags_not_to_substitute (Union[Unset, int]): Rights (UserInfo.flags) which are not substituted.
                EIX-864
            lur_list (Union[Unset, int]): Insert or remove an entry to the list of subentries of a Sord.
            flag_editduedate (Union[Unset, int]): Edit expiration date of archive entries.
            flag_nologin (Union[Unset, int]): User cannot login. This is not a right but a prohibition.
            flag_editacl (Union[Unset, int]): Edit security settings.
            flag_editswl (Union[Unset, int]): Edit catchwords.
            flag_editdocs (Union[Unset, int]): Edit documents: checkin, checkout.
            flag_delreadonly (Union[Unset, int]): Delete read only documents.
            flag_changepath (Union[Unset, int]): Change storage path settings.
            flag2_extend_workflow_rights (Union[Unset, int]): User right: extend ACL during workflow execution.
                This value has to be used in the
                 UserInfo.flags2 member.
            flag_subadmin (Union[Unset, int]): Administrator, can edit only the users and groups he created.
            flag2_analytics_discover (Union[Unset, int]): User right: analytics discover.
                This right allows a user to access the 'discover' area at ELO
                 Analytics and to edit searches.
            lur_nothing (Union[Unset, int]): No access.
            flag_export (Union[Unset, int]): Export.
            lur_edit (Union[Unset, int]): Access control right for beeing able to checkin a new document version.
            flag_editconfig (Union[Unset, int]): Edit master data
            flag_sapadmin (Union[Unset, int]): SAP administrator.
            flag_editwf (Union[Unset, int]): Edit work flows.
            lur_read (Union[Unset, int]): Access control right for reading an archive entry.
            lur_space (Union[Unset, int]): Access control right to combine rights for an object contained in a workspace.
            flag2_analytics_visualize (Union[Unset, int]): User right: analytics visualize.
                This right allows a user to access the 'visualize' area at ELO
                 Analytics and to edit visualizations.
            flag_editact (Union[Unset, int]): Edit activity projects.
            lur_all (Union[Unset, int]): All access control rights.
            flag_all (Union[Unset, int]): All rights (without flag
                <pre>
                 <code>FLAG_NOLOGIN</code>
                 </pre>

                 and

                 <pre>
                 <code>FLAG_IS_OPTION_GROUP</code>
                 </pre>

                 ).
            flag_changepw (Union[Unset, int]): Change password.
            flag2_analytics_dashboard_view (Union[Unset, int]): User right: analytics dashboard view. This right allows a
                user to view predefined dashboards.
            lur_permission (Union[Unset, int]): Access control right to change ACL of an object.
            lur_delete (Union[Unset, int]): Access control right for deleting an archive entry.
            flag_import (Union[Unset, int]): Import.
            flag2_wf_controller (Union[Unset, int]): User right: workflow controller.
                This right allows a user to read all active workflows - even
                 those where she or he is not involved. In IX 8.x, this functionality was implemented by the IX
                 option usersCanReadAllActiveWorkflows. IX 9.x does not support this option, since it was a
                 quick and very limited solution to archive compatibility with Windows Client.
            flags2_not_to_substitute (Union[Unset, int]): Rights (UserInfo.flags2) which are not substituted.
                EIX-864, RID11413
            flag2_visible_feed_user (Union[Unset, int]): User right: user is visible in document feed. This value has to be
                used in the UserInfo.
                flags2
                 member.
            flag_is_option_group (Union[Unset, int]): This flag marks an option group.
            flag_startwf (Union[Unset, int]): Start work flows.
            flag_author (Union[Unset, int]): Author for release documents
            flag2_analytics_dashboard_edit (Union[Unset, int]): User right: analytics dashboard edit.
                This right allows a user to access the 'dashboard' area
                 at ELO Analytics and to edit dashboards.
            flag2_desktop_client_plus (Union[Unset, int]): Allows to use Desktop Client Plus. This value has to be used in
                the UserInfo.flags2 member.
            flags2_not_to_inherit (Union[Unset, int]): Rights (UserInfo.flags2) which are not inherited from groups the user
                is a member.
            flag_changerev (Union[Unset, int]): Change the archiving mode of a document.
            flag_delstruc (Union[Unset, int]): Delete archive entries.
            flag_editscan (Union[Unset, int]): Edit scanner settings.
            flag_delversion (Union[Unset, int]): Delete a document version in history
            flag_changemask (Union[Unset, int]): Change the storage mask of an existing (not new) archive entry.
            flag2_interactive_login (Union[Unset, int]): User right: Allow interactive login. This value has to be used in
                the UserInfo.flags2 member.
            flag2_last (Union[Unset, int]): Highest bit currently used in {@link UserInfo#flags2}. Reserved.
            flag2_show_extra_info (Union[Unset, int]): User right: user can see additional keywording information.
                This value has to be used in the
                 UserInfo.flags2 member.
            flag2_limited_client (Union[Unset, int]): User right: limited client. This right limits the functionality of the
                client application.
                In
                 AdminConsole, this flag ist named "ELOxc Client User, Email only".
            flag_editscript (Union[Unset, int]): Create, edit, delete scripts.
            flag_editrepl (Union[Unset, int]): Edit replication set assignment.
            flag_editmask (Union[Unset, int]): Create, edit, delete storage masks.
            flag_editstructure (Union[Unset, int]): Edit archive structure: create, edit, move archive entries.
            flag2_can_be_substituted (Union[Unset, int]): Group right: This group can be substituted to an other user.
                <p>
                 This right cannot be inherited by sub groups and is not inherited by substituted groups or
                 users.
                 </p>
    """

    flags_not_to_inherit: Union[Unset, int] = UNSET
    lur_write: Union[Unset, int] = UNSET
    flag2_all: Union[Unset, int] = UNSET
    flag_deldoc: Union[Unset, int] = UNSET
    flag2_functional_role: Union[Unset, int] = UNSET
    flag2_visible_user: Union[Unset, int] = UNSET
    flags_exclusive_for_groups: Union[Unset, int] = UNSET
    flag_hasfileaccess: Union[Unset, int] = UNSET
    flag2_is_dms_desktop_user: Union[Unset, int] = UNSET
    flag_admin: Union[Unset, int] = UNSET
    flag_ignoreacl: Union[Unset, int] = UNSET
    flags_not_to_substitute: Union[Unset, int] = UNSET
    lur_list: Union[Unset, int] = UNSET
    flag_editduedate: Union[Unset, int] = UNSET
    flag_nologin: Union[Unset, int] = UNSET
    flag_editacl: Union[Unset, int] = UNSET
    flag_editswl: Union[Unset, int] = UNSET
    flag_editdocs: Union[Unset, int] = UNSET
    flag_delreadonly: Union[Unset, int] = UNSET
    flag_changepath: Union[Unset, int] = UNSET
    flag2_extend_workflow_rights: Union[Unset, int] = UNSET
    flag_subadmin: Union[Unset, int] = UNSET
    flag2_analytics_discover: Union[Unset, int] = UNSET
    lur_nothing: Union[Unset, int] = UNSET
    flag_export: Union[Unset, int] = UNSET
    lur_edit: Union[Unset, int] = UNSET
    flag_editconfig: Union[Unset, int] = UNSET
    flag_sapadmin: Union[Unset, int] = UNSET
    flag_editwf: Union[Unset, int] = UNSET
    lur_read: Union[Unset, int] = UNSET
    lur_space: Union[Unset, int] = UNSET
    flag2_analytics_visualize: Union[Unset, int] = UNSET
    flag_editact: Union[Unset, int] = UNSET
    lur_all: Union[Unset, int] = UNSET
    flag_all: Union[Unset, int] = UNSET
    flag_changepw: Union[Unset, int] = UNSET
    flag2_analytics_dashboard_view: Union[Unset, int] = UNSET
    lur_permission: Union[Unset, int] = UNSET
    lur_delete: Union[Unset, int] = UNSET
    flag_import: Union[Unset, int] = UNSET
    flag2_wf_controller: Union[Unset, int] = UNSET
    flags2_not_to_substitute: Union[Unset, int] = UNSET
    flag2_visible_feed_user: Union[Unset, int] = UNSET
    flag_is_option_group: Union[Unset, int] = UNSET
    flag_startwf: Union[Unset, int] = UNSET
    flag_author: Union[Unset, int] = UNSET
    flag2_analytics_dashboard_edit: Union[Unset, int] = UNSET
    flag2_desktop_client_plus: Union[Unset, int] = UNSET
    flags2_not_to_inherit: Union[Unset, int] = UNSET
    flag_changerev: Union[Unset, int] = UNSET
    flag_delstruc: Union[Unset, int] = UNSET
    flag_editscan: Union[Unset, int] = UNSET
    flag_delversion: Union[Unset, int] = UNSET
    flag_changemask: Union[Unset, int] = UNSET
    flag2_interactive_login: Union[Unset, int] = UNSET
    flag2_last: Union[Unset, int] = UNSET
    flag2_show_extra_info: Union[Unset, int] = UNSET
    flag2_limited_client: Union[Unset, int] = UNSET
    flag_editscript: Union[Unset, int] = UNSET
    flag_editrepl: Union[Unset, int] = UNSET
    flag_editmask: Union[Unset, int] = UNSET
    flag_editstructure: Union[Unset, int] = UNSET
    flag2_can_be_substituted: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flags_not_to_inherit = self.flags_not_to_inherit

        lur_write = self.lur_write

        flag2_all = self.flag2_all

        flag_deldoc = self.flag_deldoc

        flag2_functional_role = self.flag2_functional_role

        flag2_visible_user = self.flag2_visible_user

        flags_exclusive_for_groups = self.flags_exclusive_for_groups

        flag_hasfileaccess = self.flag_hasfileaccess

        flag2_is_dms_desktop_user = self.flag2_is_dms_desktop_user

        flag_admin = self.flag_admin

        flag_ignoreacl = self.flag_ignoreacl

        flags_not_to_substitute = self.flags_not_to_substitute

        lur_list = self.lur_list

        flag_editduedate = self.flag_editduedate

        flag_nologin = self.flag_nologin

        flag_editacl = self.flag_editacl

        flag_editswl = self.flag_editswl

        flag_editdocs = self.flag_editdocs

        flag_delreadonly = self.flag_delreadonly

        flag_changepath = self.flag_changepath

        flag2_extend_workflow_rights = self.flag2_extend_workflow_rights

        flag_subadmin = self.flag_subadmin

        flag2_analytics_discover = self.flag2_analytics_discover

        lur_nothing = self.lur_nothing

        flag_export = self.flag_export

        lur_edit = self.lur_edit

        flag_editconfig = self.flag_editconfig

        flag_sapadmin = self.flag_sapadmin

        flag_editwf = self.flag_editwf

        lur_read = self.lur_read

        lur_space = self.lur_space

        flag2_analytics_visualize = self.flag2_analytics_visualize

        flag_editact = self.flag_editact

        lur_all = self.lur_all

        flag_all = self.flag_all

        flag_changepw = self.flag_changepw

        flag2_analytics_dashboard_view = self.flag2_analytics_dashboard_view

        lur_permission = self.lur_permission

        lur_delete = self.lur_delete

        flag_import = self.flag_import

        flag2_wf_controller = self.flag2_wf_controller

        flags2_not_to_substitute = self.flags2_not_to_substitute

        flag2_visible_feed_user = self.flag2_visible_feed_user

        flag_is_option_group = self.flag_is_option_group

        flag_startwf = self.flag_startwf

        flag_author = self.flag_author

        flag2_analytics_dashboard_edit = self.flag2_analytics_dashboard_edit

        flag2_desktop_client_plus = self.flag2_desktop_client_plus

        flags2_not_to_inherit = self.flags2_not_to_inherit

        flag_changerev = self.flag_changerev

        flag_delstruc = self.flag_delstruc

        flag_editscan = self.flag_editscan

        flag_delversion = self.flag_delversion

        flag_changemask = self.flag_changemask

        flag2_interactive_login = self.flag2_interactive_login

        flag2_last = self.flag2_last

        flag2_show_extra_info = self.flag2_show_extra_info

        flag2_limited_client = self.flag2_limited_client

        flag_editscript = self.flag_editscript

        flag_editrepl = self.flag_editrepl

        flag_editmask = self.flag_editmask

        flag_editstructure = self.flag_editstructure

        flag2_can_be_substituted = self.flag2_can_be_substituted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flags_not_to_inherit is not UNSET:
            field_dict["FLAGS_NOT_TO_INHERIT"] = flags_not_to_inherit
        if lur_write is not UNSET:
            field_dict["LUR_WRITE"] = lur_write
        if flag2_all is not UNSET:
            field_dict["FLAG2_ALL"] = flag2_all
        if flag_deldoc is not UNSET:
            field_dict["FLAG_DELDOC"] = flag_deldoc
        if flag2_functional_role is not UNSET:
            field_dict["FLAG2_FUNCTIONAL_ROLE"] = flag2_functional_role
        if flag2_visible_user is not UNSET:
            field_dict["FLAG2_VISIBLE_USER"] = flag2_visible_user
        if flags_exclusive_for_groups is not UNSET:
            field_dict["FLAGS_EXCLUSIVE_FOR_GROUPS"] = flags_exclusive_for_groups
        if flag_hasfileaccess is not UNSET:
            field_dict["FLAG_HASFILEACCESS"] = flag_hasfileaccess
        if flag2_is_dms_desktop_user is not UNSET:
            field_dict["FLAG2_IS_DMS_DESKTOP_USER"] = flag2_is_dms_desktop_user
        if flag_admin is not UNSET:
            field_dict["FLAG_ADMIN"] = flag_admin
        if flag_ignoreacl is not UNSET:
            field_dict["FLAG_IGNOREACL"] = flag_ignoreacl
        if flags_not_to_substitute is not UNSET:
            field_dict["FLAGS_NOT_TO_SUBSTITUTE"] = flags_not_to_substitute
        if lur_list is not UNSET:
            field_dict["LUR_LIST"] = lur_list
        if flag_editduedate is not UNSET:
            field_dict["FLAG_EDITDUEDATE"] = flag_editduedate
        if flag_nologin is not UNSET:
            field_dict["FLAG_NOLOGIN"] = flag_nologin
        if flag_editacl is not UNSET:
            field_dict["FLAG_EDITACL"] = flag_editacl
        if flag_editswl is not UNSET:
            field_dict["FLAG_EDITSWL"] = flag_editswl
        if flag_editdocs is not UNSET:
            field_dict["FLAG_EDITDOCS"] = flag_editdocs
        if flag_delreadonly is not UNSET:
            field_dict["FLAG_DELREADONLY"] = flag_delreadonly
        if flag_changepath is not UNSET:
            field_dict["FLAG_CHANGEPATH"] = flag_changepath
        if flag2_extend_workflow_rights is not UNSET:
            field_dict["FLAG2_EXTEND_WORKFLOW_RIGHTS"] = flag2_extend_workflow_rights
        if flag_subadmin is not UNSET:
            field_dict["FLAG_SUBADMIN"] = flag_subadmin
        if flag2_analytics_discover is not UNSET:
            field_dict["FLAG2_ANALYTICS_DISCOVER"] = flag2_analytics_discover
        if lur_nothing is not UNSET:
            field_dict["LUR_NOTHING"] = lur_nothing
        if flag_export is not UNSET:
            field_dict["FLAG_EXPORT"] = flag_export
        if lur_edit is not UNSET:
            field_dict["LUR_EDIT"] = lur_edit
        if flag_editconfig is not UNSET:
            field_dict["FLAG_EDITCONFIG"] = flag_editconfig
        if flag_sapadmin is not UNSET:
            field_dict["FLAG_SAPADMIN"] = flag_sapadmin
        if flag_editwf is not UNSET:
            field_dict["FLAG_EDITWF"] = flag_editwf
        if lur_read is not UNSET:
            field_dict["LUR_READ"] = lur_read
        if lur_space is not UNSET:
            field_dict["LUR_SPACE"] = lur_space
        if flag2_analytics_visualize is not UNSET:
            field_dict["FLAG2_ANALYTICS_VISUALIZE"] = flag2_analytics_visualize
        if flag_editact is not UNSET:
            field_dict["FLAG_EDITACT"] = flag_editact
        if lur_all is not UNSET:
            field_dict["LUR_ALL"] = lur_all
        if flag_all is not UNSET:
            field_dict["FLAG_ALL"] = flag_all
        if flag_changepw is not UNSET:
            field_dict["FLAG_CHANGEPW"] = flag_changepw
        if flag2_analytics_dashboard_view is not UNSET:
            field_dict["FLAG2_ANALYTICS_DASHBOARD_VIEW"] = flag2_analytics_dashboard_view
        if lur_permission is not UNSET:
            field_dict["LUR_PERMISSION"] = lur_permission
        if lur_delete is not UNSET:
            field_dict["LUR_DELETE"] = lur_delete
        if flag_import is not UNSET:
            field_dict["FLAG_IMPORT"] = flag_import
        if flag2_wf_controller is not UNSET:
            field_dict["FLAG2_WF_CONTROLLER"] = flag2_wf_controller
        if flags2_not_to_substitute is not UNSET:
            field_dict["FLAGS2_NOT_TO_SUBSTITUTE"] = flags2_not_to_substitute
        if flag2_visible_feed_user is not UNSET:
            field_dict["FLAG2_VISIBLE_FEED_USER"] = flag2_visible_feed_user
        if flag_is_option_group is not UNSET:
            field_dict["FLAG_IS_OPTION_GROUP"] = flag_is_option_group
        if flag_startwf is not UNSET:
            field_dict["FLAG_STARTWF"] = flag_startwf
        if flag_author is not UNSET:
            field_dict["FLAG_AUTHOR"] = flag_author
        if flag2_analytics_dashboard_edit is not UNSET:
            field_dict["FLAG2_ANALYTICS_DASHBOARD_EDIT"] = flag2_analytics_dashboard_edit
        if flag2_desktop_client_plus is not UNSET:
            field_dict["FLAG2_DESKTOP_CLIENT_PLUS"] = flag2_desktop_client_plus
        if flags2_not_to_inherit is not UNSET:
            field_dict["FLAGS2_NOT_TO_INHERIT"] = flags2_not_to_inherit
        if flag_changerev is not UNSET:
            field_dict["FLAG_CHANGEREV"] = flag_changerev
        if flag_delstruc is not UNSET:
            field_dict["FLAG_DELSTRUC"] = flag_delstruc
        if flag_editscan is not UNSET:
            field_dict["FLAG_EDITSCAN"] = flag_editscan
        if flag_delversion is not UNSET:
            field_dict["FLAG_DELVERSION"] = flag_delversion
        if flag_changemask is not UNSET:
            field_dict["FLAG_CHANGEMASK"] = flag_changemask
        if flag2_interactive_login is not UNSET:
            field_dict["FLAG2_INTERACTIVE_LOGIN"] = flag2_interactive_login
        if flag2_last is not UNSET:
            field_dict["FLAG2_LAST"] = flag2_last
        if flag2_show_extra_info is not UNSET:
            field_dict["FLAG2_SHOW_EXTRA_INFO"] = flag2_show_extra_info
        if flag2_limited_client is not UNSET:
            field_dict["FLAG2_LIMITED_CLIENT"] = flag2_limited_client
        if flag_editscript is not UNSET:
            field_dict["FLAG_EDITSCRIPT"] = flag_editscript
        if flag_editrepl is not UNSET:
            field_dict["FLAG_EDITREPL"] = flag_editrepl
        if flag_editmask is not UNSET:
            field_dict["FLAG_EDITMASK"] = flag_editmask
        if flag_editstructure is not UNSET:
            field_dict["FLAG_EDITSTRUCTURE"] = flag_editstructure
        if flag2_can_be_substituted is not UNSET:
            field_dict["FLAG2_CAN_BE_SUBSTITUTED"] = flag2_can_be_substituted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flags_not_to_inherit = d.pop("FLAGS_NOT_TO_INHERIT", UNSET)

        lur_write = d.pop("LUR_WRITE", UNSET)

        flag2_all = d.pop("FLAG2_ALL", UNSET)

        flag_deldoc = d.pop("FLAG_DELDOC", UNSET)

        flag2_functional_role = d.pop("FLAG2_FUNCTIONAL_ROLE", UNSET)

        flag2_visible_user = d.pop("FLAG2_VISIBLE_USER", UNSET)

        flags_exclusive_for_groups = d.pop("FLAGS_EXCLUSIVE_FOR_GROUPS", UNSET)

        flag_hasfileaccess = d.pop("FLAG_HASFILEACCESS", UNSET)

        flag2_is_dms_desktop_user = d.pop("FLAG2_IS_DMS_DESKTOP_USER", UNSET)

        flag_admin = d.pop("FLAG_ADMIN", UNSET)

        flag_ignoreacl = d.pop("FLAG_IGNOREACL", UNSET)

        flags_not_to_substitute = d.pop("FLAGS_NOT_TO_SUBSTITUTE", UNSET)

        lur_list = d.pop("LUR_LIST", UNSET)

        flag_editduedate = d.pop("FLAG_EDITDUEDATE", UNSET)

        flag_nologin = d.pop("FLAG_NOLOGIN", UNSET)

        flag_editacl = d.pop("FLAG_EDITACL", UNSET)

        flag_editswl = d.pop("FLAG_EDITSWL", UNSET)

        flag_editdocs = d.pop("FLAG_EDITDOCS", UNSET)

        flag_delreadonly = d.pop("FLAG_DELREADONLY", UNSET)

        flag_changepath = d.pop("FLAG_CHANGEPATH", UNSET)

        flag2_extend_workflow_rights = d.pop("FLAG2_EXTEND_WORKFLOW_RIGHTS", UNSET)

        flag_subadmin = d.pop("FLAG_SUBADMIN", UNSET)

        flag2_analytics_discover = d.pop("FLAG2_ANALYTICS_DISCOVER", UNSET)

        lur_nothing = d.pop("LUR_NOTHING", UNSET)

        flag_export = d.pop("FLAG_EXPORT", UNSET)

        lur_edit = d.pop("LUR_EDIT", UNSET)

        flag_editconfig = d.pop("FLAG_EDITCONFIG", UNSET)

        flag_sapadmin = d.pop("FLAG_SAPADMIN", UNSET)

        flag_editwf = d.pop("FLAG_EDITWF", UNSET)

        lur_read = d.pop("LUR_READ", UNSET)

        lur_space = d.pop("LUR_SPACE", UNSET)

        flag2_analytics_visualize = d.pop("FLAG2_ANALYTICS_VISUALIZE", UNSET)

        flag_editact = d.pop("FLAG_EDITACT", UNSET)

        lur_all = d.pop("LUR_ALL", UNSET)

        flag_all = d.pop("FLAG_ALL", UNSET)

        flag_changepw = d.pop("FLAG_CHANGEPW", UNSET)

        flag2_analytics_dashboard_view = d.pop("FLAG2_ANALYTICS_DASHBOARD_VIEW", UNSET)

        lur_permission = d.pop("LUR_PERMISSION", UNSET)

        lur_delete = d.pop("LUR_DELETE", UNSET)

        flag_import = d.pop("FLAG_IMPORT", UNSET)

        flag2_wf_controller = d.pop("FLAG2_WF_CONTROLLER", UNSET)

        flags2_not_to_substitute = d.pop("FLAGS2_NOT_TO_SUBSTITUTE", UNSET)

        flag2_visible_feed_user = d.pop("FLAG2_VISIBLE_FEED_USER", UNSET)

        flag_is_option_group = d.pop("FLAG_IS_OPTION_GROUP", UNSET)

        flag_startwf = d.pop("FLAG_STARTWF", UNSET)

        flag_author = d.pop("FLAG_AUTHOR", UNSET)

        flag2_analytics_dashboard_edit = d.pop("FLAG2_ANALYTICS_DASHBOARD_EDIT", UNSET)

        flag2_desktop_client_plus = d.pop("FLAG2_DESKTOP_CLIENT_PLUS", UNSET)

        flags2_not_to_inherit = d.pop("FLAGS2_NOT_TO_INHERIT", UNSET)

        flag_changerev = d.pop("FLAG_CHANGEREV", UNSET)

        flag_delstruc = d.pop("FLAG_DELSTRUC", UNSET)

        flag_editscan = d.pop("FLAG_EDITSCAN", UNSET)

        flag_delversion = d.pop("FLAG_DELVERSION", UNSET)

        flag_changemask = d.pop("FLAG_CHANGEMASK", UNSET)

        flag2_interactive_login = d.pop("FLAG2_INTERACTIVE_LOGIN", UNSET)

        flag2_last = d.pop("FLAG2_LAST", UNSET)

        flag2_show_extra_info = d.pop("FLAG2_SHOW_EXTRA_INFO", UNSET)

        flag2_limited_client = d.pop("FLAG2_LIMITED_CLIENT", UNSET)

        flag_editscript = d.pop("FLAG_EDITSCRIPT", UNSET)

        flag_editrepl = d.pop("FLAG_EDITREPL", UNSET)

        flag_editmask = d.pop("FLAG_EDITMASK", UNSET)

        flag_editstructure = d.pop("FLAG_EDITSTRUCTURE", UNSET)

        flag2_can_be_substituted = d.pop("FLAG2_CAN_BE_SUBSTITUTED", UNSET)

        access_c = cls(
            flags_not_to_inherit=flags_not_to_inherit,
            lur_write=lur_write,
            flag2_all=flag2_all,
            flag_deldoc=flag_deldoc,
            flag2_functional_role=flag2_functional_role,
            flag2_visible_user=flag2_visible_user,
            flags_exclusive_for_groups=flags_exclusive_for_groups,
            flag_hasfileaccess=flag_hasfileaccess,
            flag2_is_dms_desktop_user=flag2_is_dms_desktop_user,
            flag_admin=flag_admin,
            flag_ignoreacl=flag_ignoreacl,
            flags_not_to_substitute=flags_not_to_substitute,
            lur_list=lur_list,
            flag_editduedate=flag_editduedate,
            flag_nologin=flag_nologin,
            flag_editacl=flag_editacl,
            flag_editswl=flag_editswl,
            flag_editdocs=flag_editdocs,
            flag_delreadonly=flag_delreadonly,
            flag_changepath=flag_changepath,
            flag2_extend_workflow_rights=flag2_extend_workflow_rights,
            flag_subadmin=flag_subadmin,
            flag2_analytics_discover=flag2_analytics_discover,
            lur_nothing=lur_nothing,
            flag_export=flag_export,
            lur_edit=lur_edit,
            flag_editconfig=flag_editconfig,
            flag_sapadmin=flag_sapadmin,
            flag_editwf=flag_editwf,
            lur_read=lur_read,
            lur_space=lur_space,
            flag2_analytics_visualize=flag2_analytics_visualize,
            flag_editact=flag_editact,
            lur_all=lur_all,
            flag_all=flag_all,
            flag_changepw=flag_changepw,
            flag2_analytics_dashboard_view=flag2_analytics_dashboard_view,
            lur_permission=lur_permission,
            lur_delete=lur_delete,
            flag_import=flag_import,
            flag2_wf_controller=flag2_wf_controller,
            flags2_not_to_substitute=flags2_not_to_substitute,
            flag2_visible_feed_user=flag2_visible_feed_user,
            flag_is_option_group=flag_is_option_group,
            flag_startwf=flag_startwf,
            flag_author=flag_author,
            flag2_analytics_dashboard_edit=flag2_analytics_dashboard_edit,
            flag2_desktop_client_plus=flag2_desktop_client_plus,
            flags2_not_to_inherit=flags2_not_to_inherit,
            flag_changerev=flag_changerev,
            flag_delstruc=flag_delstruc,
            flag_editscan=flag_editscan,
            flag_delversion=flag_delversion,
            flag_changemask=flag_changemask,
            flag2_interactive_login=flag2_interactive_login,
            flag2_last=flag2_last,
            flag2_show_extra_info=flag2_show_extra_info,
            flag2_limited_client=flag2_limited_client,
            flag_editscript=flag_editscript,
            flag_editrepl=flag_editrepl,
            flag_editmask=flag_editmask,
            flag_editstructure=flag_editstructure,
            flag2_can_be_substituted=flag2_can_be_substituted,
        )

        access_c.additional_properties = d
        return access_c

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
