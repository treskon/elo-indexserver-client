from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="SordC")


@_attrs_define
class SordC:
    """<p>
    Constants for indexing information. Each member of this class with prefix "mb" has a
     corresponding member in class <code>Sord</code>
     </p>

        Attributes:
            guid_sap_smart_link (Union[Unset, str]): GUID of folder "/Administration/Smart Link Base", used for SAP
                integration
            mb_links (Union[Unset, str]): GUIDs of linked archive entries.
            lbt_document_max (Union[Unset, int]): <code>Sord</code> objects with type greater or equal than
                <code>LBT_DOCUMENT</code> and less or
                equal than <code>LBT_DOCUMENT_MAX</code> are documents.
            guid_administration_base (Union[Unset, str]): GUID of folder "Administration". This folder contains "Replication
                Base", "Scripting Base" etc.
            guid_workflow_icons_base (Union[Unset, str]): Archive folder that contains the icons for the workflow nodes.
            mb_small_document_content (Union[Unset, str]): Return the content of a "small" document in
                <code>DocVersion.fileData</code>.
                Reading small
                 documents is up to 3 times faster this way. The IX configuration defines the maximum size of a
                 "small" document (e. g. less than 100KB).
            guid_space_administration_folder (Union[Unset, str]): GUID of administration folder for spaces.
                EIX-2987
            mb_x_date_iso (Union[Unset, str]):
            mb_details (Union[Unset, str]):
            guid_scripting_base (Union[Unset, str]): GUID of folder "Scripting Base"
            lbt_archive (Union[Unset, int]): There is one <code>Sord</code> object inside the archive database with ID 1.
                It contains some
                 archive configuration and has this type:
            guid_wfnode_icon_cycle_end (Union[Unset, str]): Object-GUID of icon file for cycle node.
            mb_del_date_iso (Union[Unset, str]):
            guid_wfnode_icon_set_server_id (Union[Unset, str]): Object-GUID of icon file for server node.
            mb_lean (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_min_doc_version (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            desc_delim (Union[Unset, str]): The objdesc column in the database is splitted into a visible and an invisible
                part.
                This
                 constant is the delimiter between them.
            mb_checkout (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            guid_replication_base (Union[Unset, str]): GUID of folder "Replication Base"
            guid_teamroom_base_folder (Union[Unset, str]): GUID of base folder for team room folders.
                EIX-2138
            mb_doc_version_members (Union[Unset, str]): Version information of the current document work version.
            mb_obj_keys (Union[Unset, str]): Index lines.
            guid_wfnode_icon_terminate (Union[Unset, str]): reserved
            guid_win_scripting_base (Union[Unset, str]): Archive folder /Administration/ELOscripts, VB scripts for Windows
                Client.
            attachment_flag_in_dochistory (Union[Unset, int]): Implementation detail: This flag is added to the object ID in
                the table "dochistory" to
                differentiate between documents and attachments.
            lbt_document (Union[Unset, int]): <code>Sord</code> objects with type greater or equal than
                <code>LBT_DOCUMENT</code> and less or
                equal than <code>LBT_DOCUMENT_MAX</code> are documents.
            mb_write_only_members (Union[Unset, str]): This members are write-only and were not read in checkoutSord,
                checkoutDoc, findFirstSords.
                mbSDesc, mbSName
            guid_wfnode_icon_beginnode (Union[Unset, str]): Object-GUID of icon file for begin node.
            guid_textreader_folder (Union[Unset, str]): Object-GUID of ELO Textreader folder.
            mb_all_index (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_owner_name (Union[Unset, str]):
            mb_hidden_text (Union[Unset, str]):
            mb_read_only_members (Union[Unset, str]): This members are read-only and ignored in checkinSord
            guid_wfnode_icon_splitnode (Union[Unset, str]): Object-GUID of icon file for split node.
            guid_apps_folder (Union[Unset, str]): GUID of folder "/Administration/ELO-Apps".
            eloindex_user_folder_private (Union[Unset, str]): Index value ELOINDEX of sub-folder "private" of a users
                folder.
            mb_acl_items (Union[Unset, str]): ACL in a human readable format.
            mb_repl_names (Union[Unset, str]): Replication set names.
            guid_wfnode_icon_cycle_begin (Union[Unset, str]): Object-GUID of icon file for cycle node.
            mb_content_stream (Union[Unset, str]): Document file content is supplied in {@link FileData#stream}.
            mb_deleted (Union[Unset, str]):
            mb_min_members (Union[Unset, str]): Includes: mbLeanMembers without mbObjKeys
            guid_wfnode_icon_pluginnode (Union[Unset, str]): Object-GUID of icon file for plugin node.
                This node is intended to trigger external events or
                 to address external systems. OnEnter is handled synchronously. It waits for a result of the
                 event. OnExit is handled asynchronously. The WF continues without waiting for the event. DB
                 transaction is terminated before OnEnter is executed.
            mb_aspect_objects (Union[Unset, str]): If {@link DocMask#dataOrganisation} = {@link
                DocMaskC#DATA_ORGANISATION_ASPECT} then the data
                of index lines is contained in aspect objects (Map values of arbitrary type).
            type_user_folder (Union[Unset, int]): Sord type of user folder.
                User folders are stored under folder Administration/Users and this
                 value is used as {@link Sord#type}.
            mb_ref_paths (Union[Unset, str]): Reference paths.
            guid_wfnode_icon_collectnode (Union[Unset, str]): Object-GUID of icon file for collect node.
            mb_desc (Union[Unset, str]): Description and Hidden Text
            ln_desc (Union[Unset, int]): Length of description + hidden text
            mb_parent_ids (Union[Unset, str]): GUIDs of parents that reference <code>this</code>
            mb_only_id (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_min (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            guid_ix_scripting_base (Union[Unset, str]): GUID of folder "IndexServer Scripting Base"
            guid_wfnode_icon_ifnode (Union[Unset, str]): Object-GUID of icon file for decision node.
            mb_all_members_lazy (Union[Unset, str]): As {@link #mbAllMembers} but provides {@link Sord#refPaths} for lazy
                loading.
            guid_cold_background_images (Union[Unset, str]): Archive folder /Administration/COLD Background Images
            mb_repl_set (Union[Unset, str]): Replication set.
            mb_doc_version (Union[Unset, str]):
            mb_only_lock (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_all_members (Union[Unset, str]): All members - without mbSmallDocumentContent
            mb_checkout_preview (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_only_unlock (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            eloindex_user_folder_data (Union[Unset, str]): Index value ELOINDEX of sub-folder "data" of a users folder.
                The "data" sub-folder of a user
                 folder can be read as follows:
                 <code>String objId = "OKEY:ELOINDEX=" + ELOINDEX_USER_FOLDER_DATA + user-guid</code>
                 <code>EditInfo ed = conn.ix().checkoutSord(objId, ...)</code>
            mb_phys_path (Union[Unset, str]): Set this option to return the physical path of the document in the DocVersion
                object.
                This
                 Option requires always a request to Document Manager.
            mb_lean_members (Union[Unset, str]): Includes: ObjDataC.
                mbAllMembers with mbAclItems, mbObjKeys
            mb_all (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            guid_space_base_folder (Union[Unset, str]): GUID of base folder for spaces.
                EIX-2987
            mb_preview (Union[Unset, str]): Detects whether there is a preview for a given document availiable.
            mb_att_version_members (Union[Unset, str]): Member bit for Sord.
                attVersion
            mb_links_go_out (Union[Unset, str]):
            guid_wfnode_icon_personnode (Union[Unset, str]): Object-GUID of icon file for person node.
            guid_trnotconv_folder (Union[Unset, str]): Object-GUID of ELO Textreader not converted documents folder.
            eloindex_user_folder_inbox (Union[Unset, str]): Index value ELOINDEX of sub-folder "inbox" of a users folder.
            mb_links_come_in (Union[Unset, str]):
            mb_repl_members (Union[Unset, str]): Includes: ObjDataC.
                mbAllMembers with mbObjKeys
            eloindex_user_folder_data_profile (Union[Unset, str]): Index value ELOINDEX of sub-folder "data/elo.profile" of
                a users folder.
            mb_i_date_iso (Union[Unset, str]):
            mb_only_guid (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            guid_users_folder (Union[Unset, str]): Object-GUID of users folder.
    """

    guid_sap_smart_link: Union[Unset, str] = UNSET
    mb_links: Union[Unset, str] = UNSET
    lbt_document_max: Union[Unset, int] = UNSET
    guid_administration_base: Union[Unset, str] = UNSET
    guid_workflow_icons_base: Union[Unset, str] = UNSET
    mb_small_document_content: Union[Unset, str] = UNSET
    guid_space_administration_folder: Union[Unset, str] = UNSET
    mb_x_date_iso: Union[Unset, str] = UNSET
    mb_details: Union[Unset, str] = UNSET
    guid_scripting_base: Union[Unset, str] = UNSET
    lbt_archive: Union[Unset, int] = UNSET
    guid_wfnode_icon_cycle_end: Union[Unset, str] = UNSET
    mb_del_date_iso: Union[Unset, str] = UNSET
    guid_wfnode_icon_set_server_id: Union[Unset, str] = UNSET
    mb_lean: Union[Unset, "SordZ"] = UNSET
    mb_min_doc_version: Union[Unset, "SordZ"] = UNSET
    desc_delim: Union[Unset, str] = UNSET
    mb_checkout: Union[Unset, "SordZ"] = UNSET
    guid_replication_base: Union[Unset, str] = UNSET
    guid_teamroom_base_folder: Union[Unset, str] = UNSET
    mb_doc_version_members: Union[Unset, str] = UNSET
    mb_obj_keys: Union[Unset, str] = UNSET
    guid_wfnode_icon_terminate: Union[Unset, str] = UNSET
    guid_win_scripting_base: Union[Unset, str] = UNSET
    attachment_flag_in_dochistory: Union[Unset, int] = UNSET
    lbt_document: Union[Unset, int] = UNSET
    mb_write_only_members: Union[Unset, str] = UNSET
    guid_wfnode_icon_beginnode: Union[Unset, str] = UNSET
    guid_textreader_folder: Union[Unset, str] = UNSET
    mb_all_index: Union[Unset, "SordZ"] = UNSET
    mb_owner_name: Union[Unset, str] = UNSET
    mb_hidden_text: Union[Unset, str] = UNSET
    mb_read_only_members: Union[Unset, str] = UNSET
    guid_wfnode_icon_splitnode: Union[Unset, str] = UNSET
    guid_apps_folder: Union[Unset, str] = UNSET
    eloindex_user_folder_private: Union[Unset, str] = UNSET
    mb_acl_items: Union[Unset, str] = UNSET
    mb_repl_names: Union[Unset, str] = UNSET
    guid_wfnode_icon_cycle_begin: Union[Unset, str] = UNSET
    mb_content_stream: Union[Unset, str] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    mb_min_members: Union[Unset, str] = UNSET
    guid_wfnode_icon_pluginnode: Union[Unset, str] = UNSET
    mb_aspect_objects: Union[Unset, str] = UNSET
    type_user_folder: Union[Unset, int] = UNSET
    mb_ref_paths: Union[Unset, str] = UNSET
    guid_wfnode_icon_collectnode: Union[Unset, str] = UNSET
    mb_desc: Union[Unset, str] = UNSET
    ln_desc: Union[Unset, int] = UNSET
    mb_parent_ids: Union[Unset, str] = UNSET
    mb_only_id: Union[Unset, "SordZ"] = UNSET
    mb_min: Union[Unset, "SordZ"] = UNSET
    guid_ix_scripting_base: Union[Unset, str] = UNSET
    guid_wfnode_icon_ifnode: Union[Unset, str] = UNSET
    mb_all_members_lazy: Union[Unset, str] = UNSET
    guid_cold_background_images: Union[Unset, str] = UNSET
    mb_repl_set: Union[Unset, str] = UNSET
    mb_doc_version: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "SordZ"] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_checkout_preview: Union[Unset, "SordZ"] = UNSET
    mb_only_unlock: Union[Unset, "SordZ"] = UNSET
    eloindex_user_folder_data: Union[Unset, str] = UNSET
    mb_phys_path: Union[Unset, str] = UNSET
    mb_lean_members: Union[Unset, str] = UNSET
    mb_all: Union[Unset, "SordZ"] = UNSET
    guid_space_base_folder: Union[Unset, str] = UNSET
    mb_preview: Union[Unset, str] = UNSET
    mb_att_version_members: Union[Unset, str] = UNSET
    mb_links_go_out: Union[Unset, str] = UNSET
    guid_wfnode_icon_personnode: Union[Unset, str] = UNSET
    guid_trnotconv_folder: Union[Unset, str] = UNSET
    eloindex_user_folder_inbox: Union[Unset, str] = UNSET
    mb_links_come_in: Union[Unset, str] = UNSET
    mb_repl_members: Union[Unset, str] = UNSET
    eloindex_user_folder_data_profile: Union[Unset, str] = UNSET
    mb_i_date_iso: Union[Unset, str] = UNSET
    mb_only_guid: Union[Unset, "SordZ"] = UNSET
    guid_users_folder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid_sap_smart_link = self.guid_sap_smart_link

        mb_links = self.mb_links

        lbt_document_max = self.lbt_document_max

        guid_administration_base = self.guid_administration_base

        guid_workflow_icons_base = self.guid_workflow_icons_base

        mb_small_document_content = self.mb_small_document_content

        guid_space_administration_folder = self.guid_space_administration_folder

        mb_x_date_iso = self.mb_x_date_iso

        mb_details = self.mb_details

        guid_scripting_base = self.guid_scripting_base

        lbt_archive = self.lbt_archive

        guid_wfnode_icon_cycle_end = self.guid_wfnode_icon_cycle_end

        mb_del_date_iso = self.mb_del_date_iso

        guid_wfnode_icon_set_server_id = self.guid_wfnode_icon_set_server_id

        mb_lean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_lean, Unset):
            mb_lean = self.mb_lean.to_dict()

        mb_min_doc_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_min_doc_version, Unset):
            mb_min_doc_version = self.mb_min_doc_version.to_dict()

        desc_delim = self.desc_delim

        mb_checkout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_checkout, Unset):
            mb_checkout = self.mb_checkout.to_dict()

        guid_replication_base = self.guid_replication_base

        guid_teamroom_base_folder = self.guid_teamroom_base_folder

        mb_doc_version_members = self.mb_doc_version_members

        mb_obj_keys = self.mb_obj_keys

        guid_wfnode_icon_terminate = self.guid_wfnode_icon_terminate

        guid_win_scripting_base = self.guid_win_scripting_base

        attachment_flag_in_dochistory = self.attachment_flag_in_dochistory

        lbt_document = self.lbt_document

        mb_write_only_members = self.mb_write_only_members

        guid_wfnode_icon_beginnode = self.guid_wfnode_icon_beginnode

        guid_textreader_folder = self.guid_textreader_folder

        mb_all_index: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_index, Unset):
            mb_all_index = self.mb_all_index.to_dict()

        mb_owner_name = self.mb_owner_name

        mb_hidden_text = self.mb_hidden_text

        mb_read_only_members = self.mb_read_only_members

        guid_wfnode_icon_splitnode = self.guid_wfnode_icon_splitnode

        guid_apps_folder = self.guid_apps_folder

        eloindex_user_folder_private = self.eloindex_user_folder_private

        mb_acl_items = self.mb_acl_items

        mb_repl_names = self.mb_repl_names

        guid_wfnode_icon_cycle_begin = self.guid_wfnode_icon_cycle_begin

        mb_content_stream = self.mb_content_stream

        mb_deleted = self.mb_deleted

        mb_min_members = self.mb_min_members

        guid_wfnode_icon_pluginnode = self.guid_wfnode_icon_pluginnode

        mb_aspect_objects = self.mb_aspect_objects

        type_user_folder = self.type_user_folder

        mb_ref_paths = self.mb_ref_paths

        guid_wfnode_icon_collectnode = self.guid_wfnode_icon_collectnode

        mb_desc = self.mb_desc

        ln_desc = self.ln_desc

        mb_parent_ids = self.mb_parent_ids

        mb_only_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_id, Unset):
            mb_only_id = self.mb_only_id.to_dict()

        mb_min: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_min, Unset):
            mb_min = self.mb_min.to_dict()

        guid_ix_scripting_base = self.guid_ix_scripting_base

        guid_wfnode_icon_ifnode = self.guid_wfnode_icon_ifnode

        mb_all_members_lazy = self.mb_all_members_lazy

        guid_cold_background_images = self.guid_cold_background_images

        mb_repl_set = self.mb_repl_set

        mb_doc_version = self.mb_doc_version

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_all_members = self.mb_all_members

        mb_checkout_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_checkout_preview, Unset):
            mb_checkout_preview = self.mb_checkout_preview.to_dict()

        mb_only_unlock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_unlock, Unset):
            mb_only_unlock = self.mb_only_unlock.to_dict()

        eloindex_user_folder_data = self.eloindex_user_folder_data

        mb_phys_path = self.mb_phys_path

        mb_lean_members = self.mb_lean_members

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        guid_space_base_folder = self.guid_space_base_folder

        mb_preview = self.mb_preview

        mb_att_version_members = self.mb_att_version_members

        mb_links_go_out = self.mb_links_go_out

        guid_wfnode_icon_personnode = self.guid_wfnode_icon_personnode

        guid_trnotconv_folder = self.guid_trnotconv_folder

        eloindex_user_folder_inbox = self.eloindex_user_folder_inbox

        mb_links_come_in = self.mb_links_come_in

        mb_repl_members = self.mb_repl_members

        eloindex_user_folder_data_profile = self.eloindex_user_folder_data_profile

        mb_i_date_iso = self.mb_i_date_iso

        mb_only_guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_guid, Unset):
            mb_only_guid = self.mb_only_guid.to_dict()

        guid_users_folder = self.guid_users_folder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid_sap_smart_link is not UNSET:
            field_dict["GUID_SAP_SMART_LINK"] = guid_sap_smart_link
        if mb_links is not UNSET:
            field_dict["mbLinks"] = mb_links
        if lbt_document_max is not UNSET:
            field_dict["LBT_DOCUMENT_MAX"] = lbt_document_max
        if guid_administration_base is not UNSET:
            field_dict["GUID_ADMINISTRATION_BASE"] = guid_administration_base
        if guid_workflow_icons_base is not UNSET:
            field_dict["GUID_WORKFLOW_ICONS_BASE"] = guid_workflow_icons_base
        if mb_small_document_content is not UNSET:
            field_dict["mbSmallDocumentContent"] = mb_small_document_content
        if guid_space_administration_folder is not UNSET:
            field_dict["GUID_SPACE_ADMINISTRATION_FOLDER"] = guid_space_administration_folder
        if mb_x_date_iso is not UNSET:
            field_dict["mbXDateIso"] = mb_x_date_iso
        if mb_details is not UNSET:
            field_dict["mbDetails"] = mb_details
        if guid_scripting_base is not UNSET:
            field_dict["GUID_SCRIPTING_BASE"] = guid_scripting_base
        if lbt_archive is not UNSET:
            field_dict["LBT_ARCHIVE"] = lbt_archive
        if guid_wfnode_icon_cycle_end is not UNSET:
            field_dict["GUID_WFNODE_ICON_CYCLE_END"] = guid_wfnode_icon_cycle_end
        if mb_del_date_iso is not UNSET:
            field_dict["mbDelDateIso"] = mb_del_date_iso
        if guid_wfnode_icon_set_server_id is not UNSET:
            field_dict["GUID_WFNODE_ICON_SET_SERVER_ID"] = guid_wfnode_icon_set_server_id
        if mb_lean is not UNSET:
            field_dict["mbLean"] = mb_lean
        if mb_min_doc_version is not UNSET:
            field_dict["mbMinDocVersion"] = mb_min_doc_version
        if desc_delim is not UNSET:
            field_dict["DESC_DELIM"] = desc_delim
        if mb_checkout is not UNSET:
            field_dict["mbCheckout"] = mb_checkout
        if guid_replication_base is not UNSET:
            field_dict["GUID_REPLICATION_BASE"] = guid_replication_base
        if guid_teamroom_base_folder is not UNSET:
            field_dict["GUID_TEAMROOM_BASE_FOLDER"] = guid_teamroom_base_folder
        if mb_doc_version_members is not UNSET:
            field_dict["mbDocVersionMembers"] = mb_doc_version_members
        if mb_obj_keys is not UNSET:
            field_dict["mbObjKeys"] = mb_obj_keys
        if guid_wfnode_icon_terminate is not UNSET:
            field_dict["GUID_WFNODE_ICON_TERMINATE"] = guid_wfnode_icon_terminate
        if guid_win_scripting_base is not UNSET:
            field_dict["GUID_WIN_SCRIPTING_BASE"] = guid_win_scripting_base
        if attachment_flag_in_dochistory is not UNSET:
            field_dict["ATTACHMENT_FLAG_IN_DOCHISTORY"] = attachment_flag_in_dochistory
        if lbt_document is not UNSET:
            field_dict["LBT_DOCUMENT"] = lbt_document
        if mb_write_only_members is not UNSET:
            field_dict["mbWriteOnlyMembers"] = mb_write_only_members
        if guid_wfnode_icon_beginnode is not UNSET:
            field_dict["GUID_WFNODE_ICON_BEGINNODE"] = guid_wfnode_icon_beginnode
        if guid_textreader_folder is not UNSET:
            field_dict["GUID_TEXTREADER_FOLDER"] = guid_textreader_folder
        if mb_all_index is not UNSET:
            field_dict["mbAllIndex"] = mb_all_index
        if mb_owner_name is not UNSET:
            field_dict["mbOwnerName"] = mb_owner_name
        if mb_hidden_text is not UNSET:
            field_dict["mbHiddenText"] = mb_hidden_text
        if mb_read_only_members is not UNSET:
            field_dict["mbReadOnlyMembers"] = mb_read_only_members
        if guid_wfnode_icon_splitnode is not UNSET:
            field_dict["GUID_WFNODE_ICON_SPLITNODE"] = guid_wfnode_icon_splitnode
        if guid_apps_folder is not UNSET:
            field_dict["GUID_APPS_FOLDER"] = guid_apps_folder
        if eloindex_user_folder_private is not UNSET:
            field_dict["ELOINDEX_USER_FOLDER_PRIVATE"] = eloindex_user_folder_private
        if mb_acl_items is not UNSET:
            field_dict["mbAclItems"] = mb_acl_items
        if mb_repl_names is not UNSET:
            field_dict["mbReplNames"] = mb_repl_names
        if guid_wfnode_icon_cycle_begin is not UNSET:
            field_dict["GUID_WFNODE_ICON_CYCLE_BEGIN"] = guid_wfnode_icon_cycle_begin
        if mb_content_stream is not UNSET:
            field_dict["mbContentStream"] = mb_content_stream
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if mb_min_members is not UNSET:
            field_dict["mbMinMembers"] = mb_min_members
        if guid_wfnode_icon_pluginnode is not UNSET:
            field_dict["GUID_WFNODE_ICON_PLUGINNODE"] = guid_wfnode_icon_pluginnode
        if mb_aspect_objects is not UNSET:
            field_dict["mbAspectObjects"] = mb_aspect_objects
        if type_user_folder is not UNSET:
            field_dict["TYPE_USER_FOLDER"] = type_user_folder
        if mb_ref_paths is not UNSET:
            field_dict["mbRefPaths"] = mb_ref_paths
        if guid_wfnode_icon_collectnode is not UNSET:
            field_dict["GUID_WFNODE_ICON_COLLECTNODE"] = guid_wfnode_icon_collectnode
        if mb_desc is not UNSET:
            field_dict["mbDesc"] = mb_desc
        if ln_desc is not UNSET:
            field_dict["lnDesc"] = ln_desc
        if mb_parent_ids is not UNSET:
            field_dict["mbParentIds"] = mb_parent_ids
        if mb_only_id is not UNSET:
            field_dict["mbOnlyId"] = mb_only_id
        if mb_min is not UNSET:
            field_dict["mbMin"] = mb_min
        if guid_ix_scripting_base is not UNSET:
            field_dict["GUID_IX_SCRIPTING_BASE"] = guid_ix_scripting_base
        if guid_wfnode_icon_ifnode is not UNSET:
            field_dict["GUID_WFNODE_ICON_IFNODE"] = guid_wfnode_icon_ifnode
        if mb_all_members_lazy is not UNSET:
            field_dict["mbAllMembersLazy"] = mb_all_members_lazy
        if guid_cold_background_images is not UNSET:
            field_dict["GUID_COLD_BACKGROUND_IMAGES"] = guid_cold_background_images
        if mb_repl_set is not UNSET:
            field_dict["mbReplSet"] = mb_repl_set
        if mb_doc_version is not UNSET:
            field_dict["mbDocVersion"] = mb_doc_version
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_checkout_preview is not UNSET:
            field_dict["mbCheckoutPreview"] = mb_checkout_preview
        if mb_only_unlock is not UNSET:
            field_dict["mbOnlyUnlock"] = mb_only_unlock
        if eloindex_user_folder_data is not UNSET:
            field_dict["ELOINDEX_USER_FOLDER_DATA"] = eloindex_user_folder_data
        if mb_phys_path is not UNSET:
            field_dict["mbPhysPath"] = mb_phys_path
        if mb_lean_members is not UNSET:
            field_dict["mbLeanMembers"] = mb_lean_members
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if guid_space_base_folder is not UNSET:
            field_dict["GUID_SPACE_BASE_FOLDER"] = guid_space_base_folder
        if mb_preview is not UNSET:
            field_dict["mbPreview"] = mb_preview
        if mb_att_version_members is not UNSET:
            field_dict["mbAttVersionMembers"] = mb_att_version_members
        if mb_links_go_out is not UNSET:
            field_dict["mbLinksGoOut"] = mb_links_go_out
        if guid_wfnode_icon_personnode is not UNSET:
            field_dict["GUID_WFNODE_ICON_PERSONNODE"] = guid_wfnode_icon_personnode
        if guid_trnotconv_folder is not UNSET:
            field_dict["GUID_TRNOTCONV_FOLDER"] = guid_trnotconv_folder
        if eloindex_user_folder_inbox is not UNSET:
            field_dict["ELOINDEX_USER_FOLDER_INBOX"] = eloindex_user_folder_inbox
        if mb_links_come_in is not UNSET:
            field_dict["mbLinksComeIn"] = mb_links_come_in
        if mb_repl_members is not UNSET:
            field_dict["mbReplMembers"] = mb_repl_members
        if eloindex_user_folder_data_profile is not UNSET:
            field_dict["ELOINDEX_USER_FOLDER_DATA_PROFILE"] = eloindex_user_folder_data_profile
        if mb_i_date_iso is not UNSET:
            field_dict["mbIDateIso"] = mb_i_date_iso
        if mb_only_guid is not UNSET:
            field_dict["mbOnlyGuid"] = mb_only_guid
        if guid_users_folder is not UNSET:
            field_dict["GUID_USERS_FOLDER"] = guid_users_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        guid_sap_smart_link = d.pop("GUID_SAP_SMART_LINK", UNSET)

        mb_links = d.pop("mbLinks", UNSET)

        lbt_document_max = d.pop("LBT_DOCUMENT_MAX", UNSET)

        guid_administration_base = d.pop("GUID_ADMINISTRATION_BASE", UNSET)

        guid_workflow_icons_base = d.pop("GUID_WORKFLOW_ICONS_BASE", UNSET)

        mb_small_document_content = d.pop("mbSmallDocumentContent", UNSET)

        guid_space_administration_folder = d.pop("GUID_SPACE_ADMINISTRATION_FOLDER", UNSET)

        mb_x_date_iso = d.pop("mbXDateIso", UNSET)

        mb_details = d.pop("mbDetails", UNSET)

        guid_scripting_base = d.pop("GUID_SCRIPTING_BASE", UNSET)

        lbt_archive = d.pop("LBT_ARCHIVE", UNSET)

        guid_wfnode_icon_cycle_end = d.pop("GUID_WFNODE_ICON_CYCLE_END", UNSET)

        mb_del_date_iso = d.pop("mbDelDateIso", UNSET)

        guid_wfnode_icon_set_server_id = d.pop("GUID_WFNODE_ICON_SET_SERVER_ID", UNSET)

        _mb_lean = d.pop("mbLean", UNSET)
        mb_lean: Union[Unset, SordZ]
        if isinstance(_mb_lean, Unset):
            mb_lean = UNSET
        else:
            mb_lean = SordZ.from_dict(_mb_lean)

        _mb_min_doc_version = d.pop("mbMinDocVersion", UNSET)
        mb_min_doc_version: Union[Unset, SordZ]
        if isinstance(_mb_min_doc_version, Unset):
            mb_min_doc_version = UNSET
        else:
            mb_min_doc_version = SordZ.from_dict(_mb_min_doc_version)

        desc_delim = d.pop("DESC_DELIM", UNSET)

        _mb_checkout = d.pop("mbCheckout", UNSET)
        mb_checkout: Union[Unset, SordZ]
        if isinstance(_mb_checkout, Unset):
            mb_checkout = UNSET
        else:
            mb_checkout = SordZ.from_dict(_mb_checkout)

        guid_replication_base = d.pop("GUID_REPLICATION_BASE", UNSET)

        guid_teamroom_base_folder = d.pop("GUID_TEAMROOM_BASE_FOLDER", UNSET)

        mb_doc_version_members = d.pop("mbDocVersionMembers", UNSET)

        mb_obj_keys = d.pop("mbObjKeys", UNSET)

        guid_wfnode_icon_terminate = d.pop("GUID_WFNODE_ICON_TERMINATE", UNSET)

        guid_win_scripting_base = d.pop("GUID_WIN_SCRIPTING_BASE", UNSET)

        attachment_flag_in_dochistory = d.pop("ATTACHMENT_FLAG_IN_DOCHISTORY", UNSET)

        lbt_document = d.pop("LBT_DOCUMENT", UNSET)

        mb_write_only_members = d.pop("mbWriteOnlyMembers", UNSET)

        guid_wfnode_icon_beginnode = d.pop("GUID_WFNODE_ICON_BEGINNODE", UNSET)

        guid_textreader_folder = d.pop("GUID_TEXTREADER_FOLDER", UNSET)

        _mb_all_index = d.pop("mbAllIndex", UNSET)
        mb_all_index: Union[Unset, SordZ]
        if isinstance(_mb_all_index, Unset):
            mb_all_index = UNSET
        else:
            mb_all_index = SordZ.from_dict(_mb_all_index)

        mb_owner_name = d.pop("mbOwnerName", UNSET)

        mb_hidden_text = d.pop("mbHiddenText", UNSET)

        mb_read_only_members = d.pop("mbReadOnlyMembers", UNSET)

        guid_wfnode_icon_splitnode = d.pop("GUID_WFNODE_ICON_SPLITNODE", UNSET)

        guid_apps_folder = d.pop("GUID_APPS_FOLDER", UNSET)

        eloindex_user_folder_private = d.pop("ELOINDEX_USER_FOLDER_PRIVATE", UNSET)

        mb_acl_items = d.pop("mbAclItems", UNSET)

        mb_repl_names = d.pop("mbReplNames", UNSET)

        guid_wfnode_icon_cycle_begin = d.pop("GUID_WFNODE_ICON_CYCLE_BEGIN", UNSET)

        mb_content_stream = d.pop("mbContentStream", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        mb_min_members = d.pop("mbMinMembers", UNSET)

        guid_wfnode_icon_pluginnode = d.pop("GUID_WFNODE_ICON_PLUGINNODE", UNSET)

        mb_aspect_objects = d.pop("mbAspectObjects", UNSET)

        type_user_folder = d.pop("TYPE_USER_FOLDER", UNSET)

        mb_ref_paths = d.pop("mbRefPaths", UNSET)

        guid_wfnode_icon_collectnode = d.pop("GUID_WFNODE_ICON_COLLECTNODE", UNSET)

        mb_desc = d.pop("mbDesc", UNSET)

        ln_desc = d.pop("lnDesc", UNSET)

        mb_parent_ids = d.pop("mbParentIds", UNSET)

        _mb_only_id = d.pop("mbOnlyId", UNSET)
        mb_only_id: Union[Unset, SordZ]
        if isinstance(_mb_only_id, Unset):
            mb_only_id = UNSET
        else:
            mb_only_id = SordZ.from_dict(_mb_only_id)

        _mb_min = d.pop("mbMin", UNSET)
        mb_min: Union[Unset, SordZ]
        if isinstance(_mb_min, Unset):
            mb_min = UNSET
        else:
            mb_min = SordZ.from_dict(_mb_min)

        guid_ix_scripting_base = d.pop("GUID_IX_SCRIPTING_BASE", UNSET)

        guid_wfnode_icon_ifnode = d.pop("GUID_WFNODE_ICON_IFNODE", UNSET)

        mb_all_members_lazy = d.pop("mbAllMembersLazy", UNSET)

        guid_cold_background_images = d.pop("GUID_COLD_BACKGROUND_IMAGES", UNSET)

        mb_repl_set = d.pop("mbReplSet", UNSET)

        mb_doc_version = d.pop("mbDocVersion", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, SordZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = SordZ.from_dict(_mb_only_lock)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        _mb_checkout_preview = d.pop("mbCheckoutPreview", UNSET)
        mb_checkout_preview: Union[Unset, SordZ]
        if isinstance(_mb_checkout_preview, Unset):
            mb_checkout_preview = UNSET
        else:
            mb_checkout_preview = SordZ.from_dict(_mb_checkout_preview)

        _mb_only_unlock = d.pop("mbOnlyUnlock", UNSET)
        mb_only_unlock: Union[Unset, SordZ]
        if isinstance(_mb_only_unlock, Unset):
            mb_only_unlock = UNSET
        else:
            mb_only_unlock = SordZ.from_dict(_mb_only_unlock)

        eloindex_user_folder_data = d.pop("ELOINDEX_USER_FOLDER_DATA", UNSET)

        mb_phys_path = d.pop("mbPhysPath", UNSET)

        mb_lean_members = d.pop("mbLeanMembers", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, SordZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = SordZ.from_dict(_mb_all)

        guid_space_base_folder = d.pop("GUID_SPACE_BASE_FOLDER", UNSET)

        mb_preview = d.pop("mbPreview", UNSET)

        mb_att_version_members = d.pop("mbAttVersionMembers", UNSET)

        mb_links_go_out = d.pop("mbLinksGoOut", UNSET)

        guid_wfnode_icon_personnode = d.pop("GUID_WFNODE_ICON_PERSONNODE", UNSET)

        guid_trnotconv_folder = d.pop("GUID_TRNOTCONV_FOLDER", UNSET)

        eloindex_user_folder_inbox = d.pop("ELOINDEX_USER_FOLDER_INBOX", UNSET)

        mb_links_come_in = d.pop("mbLinksComeIn", UNSET)

        mb_repl_members = d.pop("mbReplMembers", UNSET)

        eloindex_user_folder_data_profile = d.pop("ELOINDEX_USER_FOLDER_DATA_PROFILE", UNSET)

        mb_i_date_iso = d.pop("mbIDateIso", UNSET)

        _mb_only_guid = d.pop("mbOnlyGuid", UNSET)
        mb_only_guid: Union[Unset, SordZ]
        if isinstance(_mb_only_guid, Unset):
            mb_only_guid = UNSET
        else:
            mb_only_guid = SordZ.from_dict(_mb_only_guid)

        guid_users_folder = d.pop("GUID_USERS_FOLDER", UNSET)

        sord_c = cls(
            guid_sap_smart_link=guid_sap_smart_link,
            mb_links=mb_links,
            lbt_document_max=lbt_document_max,
            guid_administration_base=guid_administration_base,
            guid_workflow_icons_base=guid_workflow_icons_base,
            mb_small_document_content=mb_small_document_content,
            guid_space_administration_folder=guid_space_administration_folder,
            mb_x_date_iso=mb_x_date_iso,
            mb_details=mb_details,
            guid_scripting_base=guid_scripting_base,
            lbt_archive=lbt_archive,
            guid_wfnode_icon_cycle_end=guid_wfnode_icon_cycle_end,
            mb_del_date_iso=mb_del_date_iso,
            guid_wfnode_icon_set_server_id=guid_wfnode_icon_set_server_id,
            mb_lean=mb_lean,
            mb_min_doc_version=mb_min_doc_version,
            desc_delim=desc_delim,
            mb_checkout=mb_checkout,
            guid_replication_base=guid_replication_base,
            guid_teamroom_base_folder=guid_teamroom_base_folder,
            mb_doc_version_members=mb_doc_version_members,
            mb_obj_keys=mb_obj_keys,
            guid_wfnode_icon_terminate=guid_wfnode_icon_terminate,
            guid_win_scripting_base=guid_win_scripting_base,
            attachment_flag_in_dochistory=attachment_flag_in_dochistory,
            lbt_document=lbt_document,
            mb_write_only_members=mb_write_only_members,
            guid_wfnode_icon_beginnode=guid_wfnode_icon_beginnode,
            guid_textreader_folder=guid_textreader_folder,
            mb_all_index=mb_all_index,
            mb_owner_name=mb_owner_name,
            mb_hidden_text=mb_hidden_text,
            mb_read_only_members=mb_read_only_members,
            guid_wfnode_icon_splitnode=guid_wfnode_icon_splitnode,
            guid_apps_folder=guid_apps_folder,
            eloindex_user_folder_private=eloindex_user_folder_private,
            mb_acl_items=mb_acl_items,
            mb_repl_names=mb_repl_names,
            guid_wfnode_icon_cycle_begin=guid_wfnode_icon_cycle_begin,
            mb_content_stream=mb_content_stream,
            mb_deleted=mb_deleted,
            mb_min_members=mb_min_members,
            guid_wfnode_icon_pluginnode=guid_wfnode_icon_pluginnode,
            mb_aspect_objects=mb_aspect_objects,
            type_user_folder=type_user_folder,
            mb_ref_paths=mb_ref_paths,
            guid_wfnode_icon_collectnode=guid_wfnode_icon_collectnode,
            mb_desc=mb_desc,
            ln_desc=ln_desc,
            mb_parent_ids=mb_parent_ids,
            mb_only_id=mb_only_id,
            mb_min=mb_min,
            guid_ix_scripting_base=guid_ix_scripting_base,
            guid_wfnode_icon_ifnode=guid_wfnode_icon_ifnode,
            mb_all_members_lazy=mb_all_members_lazy,
            guid_cold_background_images=guid_cold_background_images,
            mb_repl_set=mb_repl_set,
            mb_doc_version=mb_doc_version,
            mb_only_lock=mb_only_lock,
            mb_all_members=mb_all_members,
            mb_checkout_preview=mb_checkout_preview,
            mb_only_unlock=mb_only_unlock,
            eloindex_user_folder_data=eloindex_user_folder_data,
            mb_phys_path=mb_phys_path,
            mb_lean_members=mb_lean_members,
            mb_all=mb_all,
            guid_space_base_folder=guid_space_base_folder,
            mb_preview=mb_preview,
            mb_att_version_members=mb_att_version_members,
            mb_links_go_out=mb_links_go_out,
            guid_wfnode_icon_personnode=guid_wfnode_icon_personnode,
            guid_trnotconv_folder=guid_trnotconv_folder,
            eloindex_user_folder_inbox=eloindex_user_folder_inbox,
            mb_links_come_in=mb_links_come_in,
            mb_repl_members=mb_repl_members,
            eloindex_user_folder_data_profile=eloindex_user_folder_data_profile,
            mb_i_date_iso=mb_i_date_iso,
            mb_only_guid=mb_only_guid,
            guid_users_folder=guid_users_folder,
        )

        sord_c.additional_properties = d
        return sord_c

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
