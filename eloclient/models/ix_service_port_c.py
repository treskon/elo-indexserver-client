from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_c import AccessC
    from ..models.acl_item_c import AclItemC
    from ..models.action_c import ActionC
    from ..models.activity_c import ActivityC
    from ..models.activity_project_c import ActivityProjectC
    from ..models.admin_mode_c import AdminModeC
    from ..models.alert_c import AlertC
    from ..models.any_c import AnyC
    from ..models.archive_statistics_options_c import ArchiveStatisticsOptionsC
    from ..models.archiving_mode_c import ArchivingModeC
    from ..models.aspect_assoc_c import AspectAssocC
    from ..models.aspect_c import AspectC
    from ..models.aspect_line_c import AspectLineC
    from ..models.checkin_users_c import CheckinUsersC
    from ..models.checkout_users_c import CheckoutUsersC
    from ..models.client_info_c import ClientInfoC
    from ..models.color_data_c import ColorDataC
    from ..models.config_file_c import ConfigFileC
    from ..models.copy_sord_c import CopySordC
    from ..models.counter_info_c import CounterInfoC
    from ..models.crypt_info_c import CryptInfoC
    from ..models.doc_mask_c import DocMaskC
    from ..models.doc_mask_inherit_c import DocMaskInheritC
    from ..models.doc_mask_line_c import DocMaskLineC
    from ..models.doc_mask_line_template_c import DocMaskLineTemplateC
    from ..models.doc_version_c import DocVersionC
    from ..models.e_search_params_c import ESearchParamsC
    from ..models.edit_info_c import EditInfoC
    from ..models.elo_ix_opt_c import EloIxOptC
    from ..models.event_bus_c import EventBusC
    from ..models.export_options_c import ExportOptionsC
    from ..models.feed_c import FeedC
    from ..models.file_data_c import FileDataC
    from ..models.find_actions_info_c import FindActionsInfoC
    from ..models.find_direct_c import FindDirectC
    from ..models.fulltext_config_c import FulltextConfigC
    from ..models.import_options_c import ImportOptionsC
    from ..models.index_value_c import IndexValueC
    from ..models.invalidate_cache_c import InvalidateCacheC
    from ..models.ix_exception_c import IXExceptionC
    from ..models.keyword_c import KeywordC
    from ..models.link_sord_c import LinkSordC
    from ..models.lock_c import LockC
    from ..models.map_data_c import MapDataC
    from ..models.map_domain_c import MapDomainC
    from ..models.map_hist_c import MapHistC
    from ..models.navigation_info_c import NavigationInfoC
    from ..models.note_c import NoteC
    from ..models.note_freehand_c import NoteFreehandC
    from ..models.note_template_c import NoteTemplateC
    from ..models.obj_key_c import ObjKeyC
    from ..models.ocr_info_c import OcrInfoC
    from ..models.org_unit_info_c import OrgUnitInfoC
    from ..models.package_c import PackageC
    from ..models.package_data_c import PackageDataC
    from ..models.package_level_data_c import PackageLevelDataC
    from ..models.preview_image_info_c import PreviewImageInfoC
    from ..models.process_info_c import ProcessInfoC
    from ..models.public_download_c import PublicDownloadC
    from ..models.reminder_c import ReminderC
    from ..models.repl_set_name_c import ReplSetNameC
    from ..models.report_c import ReportC
    from ..models.report_info_c import ReportInfoC
    from ..models.report_mode_c import ReportModeC
    from ..models.report_options_c import ReportOptionsC
    from ..models.resolve_rights_result_c import ResolveRightsResultC
    from ..models.search_mode_c import SearchModeC
    from ..models.search_terms_c import SearchTermsC
    from ..models.server_info_dmc import ServerInfoDMC
    from ..models.server_state_c import ServerStateC
    from ..models.session_options_c import SessionOptionsC
    from ..models.sord_c import SordC
    from ..models.sord_hist_c import SordHistC
    from ..models.sord_hist_key_c import SordHistKeyC
    from ..models.sord_type_c import SordTypeC
    from ..models.sort_order_c import SortOrderC
    from ..models.store_info_c import StoreInfoC
    from ..models.subs_info_c import SubsInfoC
    from ..models.subscription_c import SubscriptionC
    from ..models.substitution_c import SubstitutionC
    from ..models.thesaurus_c import ThesaurusC
    from ..models.translate_term_c import TranslateTermC
    from ..models.user_info_c import UserInfoC
    from ..models.user_profile_c import UserProfileC
    from ..models.user_task_priority_c import UserTaskPriorityC
    from ..models.user_task_sort_order_c import UserTaskSortOrderC
    from ..models.vt_doc_c import VtDocC
    from ..models.wf_diagram_c import WFDiagramC
    from ..models.wf_node_c import WFNodeC
    from ..models.wf_node_history_c import WFNodeHistoryC
    from ..models.wf_node_matrix_c import WFNodeMatrixC
    from ..models.wf_take_node_c import WFTakeNodeC
    from ..models.wf_type_c import WFTypeC
    from ..models.wf_version_c import WFVersionC
    from ..models.workflow_export_options_c import WorkflowExportOptionsC


T = TypeVar("T", bound="IXServicePortC")


@_attrs_define
class IXServicePortC:
    """<p>
    Constants for options and classes used by Indexserver.
     </p>

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            stream_version (Union[Unset, str]): Version information used in binary serialization.
            lock (Union[Unset, LockC]): <p>
                Constants to lock data against concurrent modification.
                 </p>
            workflow_node (Union[Unset, WFNodeC]): <p>
                Constants for <code>WorkFlowNode</code>.
                 </p>
            event_bus (Union[Unset, EventBusC]): Constants related to the event bus API.
            client_info (Union[Unset, ClientInfoC]): Constants for ClientInfo. These constanse are only for internal usage.
            admin_mode (Union[Unset, AdminModeC]): Constants for the administration mode.
            workflow_type (Union[Unset, WFTypeC]): Constants class for WFType. This class describes the workflow
                type/status.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            checkout_users (Union[Unset, CheckoutUsersC]): <p>
                Constants to select users and groups
                 </p>
            resolve_rights (Union[Unset, ResolveRightsResultC]): Constants for {@link ResolveRightsResult}.
            session_options (Union[Unset, SessionOptionsC]): Constants of SessionOptions.
            doc_version (Union[Unset, DocVersionC]):
            process_info (Union[Unset, ProcessInfoC]): Constants class for the ProcessInfo class.
                Errors: The error modes are ordered by increasing failure tolerance. In most cases a tree walk
                 will traverse nodes in prefix mode except scripts, that may have an user defined processing
                 position, so the operational success of a given node directly influences further processing.
                 ERRORMODE_ALL, the zero failure tolerance, stops the job (nearly) immediately, while
                 ERRORMODE_SKIP_SUBTREE just skips subtree traversals, but continues with lists or siblings. If
                 you pass ERRORMODE_SKIP_PROCINFO the sequence of ProcessInfo members will be executed completely,
                 whether errors occur or not. The most tolerant mode is ERRORMODE_SKIP_PROCINFO where only errors
                 impeding further traversing stop the job.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            search_mode (Union[Unset, SearchModeC]): <p>
                This class defines options used in <code>FindOptions.searchMode</code>.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            find_actions_info (Union[Unset, FindActionsInfoC]): Constants for FindActionInfo and findFirstActions.
            export_options (Union[Unset, ExportOptionsC]): Constants class for the ExportOptions class.
                Contains constants used when exporting objects from
                 the ELO archive.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            doc_mask (Union[Unset, DocMaskC]): <p>
                Constants related to class <code>DocMask</code>. Some of the <code>MFG_</code> values are used in
                 the member <code>Flags</code> of class <code>Sord</code> too. Each member of this class with
                 prefix "mb" has a corresponding member in class <code>DocMask</code>
                 </p>
                 *
                 </p>
            obj_key (Union[Unset, ObjKeyC]): <p>
                Constants for the ObjKey class.
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            ixexception (Union[Unset, IXExceptionC]): This class contains constant definitions for Indexserver error numbers
                used in Indexserver
                exceptions.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            report_options (Union[Unset, ReportOptionsC]): Constants for report mode
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
                 An ERP code is assigned to one or more action codes.
            checkin_users (Union[Unset, CheckinUsersC]): <p>
                Constants for the function <code>checkinUsers</code>.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation:
                 </p>
            config_file (Union[Unset, ConfigFileC]): Constants for the ConfigFile class. These are used for accessing server
                directories.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            workflow_node_history (Union[Unset, WFNodeHistoryC]): <p>Bit constants for members of WFNodeHistory</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            nav_info (Union[Unset, NavigationInfoC]): Constants class for the NavigationInfo class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            server_info_dm (Union[Unset, ServerInfoDMC]): Constants used by the members of the class ServerInfoDM.
            ocr_info (Union[Unset, OcrInfoC]): Constants for OCR processing.
            search_terms (Union[Unset, SearchTermsC]):
            map_hist (Union[Unset, MapHistC]): Element selectors for class MapHist.
            workflow_version (Union[Unset, WFVersionC]): Constants for WFVersion
            preview_image_info (Union[Unset, PreviewImageInfoC]):
            translate_term (Union[Unset, TranslateTermC]): Constants for class TranslateTerm.
            edit_info (Union[Unset, EditInfoC]): <p>
                Constants to read data for editing the indexing information of an archive entry
                 </p>
            fulltext_config (Union[Unset, FulltextConfigC]): Constants for class FulltextConfig.
            subscription (Union[Unset, SubscriptionC]):
            docmask_inherit (Union[Unset, DocMaskInheritC]): <p>Bit constants for members of DocMaskInherit</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            user_task_priority (Union[Unset, UserTaskPriorityC]):
            user_task_sort_order (Union[Unset, UserTaskSortOrderC]):
            server_state (Union[Unset, ServerStateC]): <p>Bit constants for members of ServerState</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            indexvalue (Union[Unset, IndexValueC]): This class defines the constants for the type member in IndexValue.
            repl_set_name (Union[Unset, ReplSetNameC]): <p>Bit constants for members of ReplSetName</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            subs_info (Union[Unset, SubsInfoC]): Constants for class SubsInfo.
            sort_order (Union[Unset, SortOrderC]): This class contains constants for sorting of archive entries and search
                results.
            org_unit_info (Union[Unset, OrgUnitInfoC]): <p>
                Constants related to organizational unit information.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2013
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            doc_mask_line (Union[Unset, DocMaskLineC]): <p>
                Constants for class <code>DocMaskLine</code>
                 </p>
                 <p>
                 Copyright: Copyright (c) 2003
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            import_options (Union[Unset, ImportOptionsC]): Defines the Options of an Import. Each Option is represented by
                one bit.
                Several Options can be put together by a
                 bit-logic and.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            workflow (Union[Unset, WFDiagramC]): <p>
                Constants for workflows.
                 </p>
            note_freehand (Union[Unset, NoteFreehandC]): Constants for NoteFreehand
            copy_sord (Union[Unset, CopySordC]): Constants to copy or move archive entries, or to create a logical link.
                These constants are used as parameters in the
                 copySord function.
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            workflow_node_assoc_type (Union[Unset, WFNodeMatrixC]): These constants describe the type of connection between
                two nodes.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            activity_project (Union[Unset, ActivityProjectC]): Constants for class ActivityProject.
            elo_ix_opt (Union[Unset, EloIxOptC]):
            report_info (Union[Unset, ReportInfoC]): Report information.
                <p>
                 Indexserver writes the following report entries
                 </p>
                 <table border="2">
                 <tr>
                 <td>ReportInfo.action</td>
                 <td>ReportInfo.objId</td>
                 <td>ReportInfo.extra1</td>
                 <td>ReportInfo.extra2</td>
                 <td>ReportInfo.comment</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LOGIN</td>
                 <td>0</td>
                 <td>SSO User ID</td>
                 <td>[EXTRA2_SSO_LOGIN]</td>
                 <td>Computer name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LOGOUT</td>
                 <td>0</td>
                 <td>0</td>
                 <td>0</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LOCK_ARCHIVE</td>
                 <td>0</td>
                 <td>Key ID</td>
                 <td>0</td>
                 <td>Key name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_USER</td>
                 <td>0</td>
                 <td>User ID</td>
                 <td>User Flags</td>
                 <td>User name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_USER</td>
                 <td>0</td>
                 <td>User ID</td>
                 <td>User Flags</td>
                 <td>User name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_USER</td>
                 <td>0</td>
                 <td>User ID</td>
                 <td>User Flags</td>
                 <td>User name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_KEY</td>
                 <td>0</td>
                 <td>Key ID</td>
                 <td>0</td>
                 <td>Key name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_KEY</td>
                 <td>0</td>
                 <td>Key ID</td>
                 <td>0</td>
                 <td>Key name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_KEY</td>
                 <td>0</td>
                 <td>Key ID</td>
                 <td>0</td>
                 <td>Key name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_SORD</td>
                 <td>Object ID</td>
                 <td>Object type</td>
                 <td>Storage mask ID</td>
                 <td>Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKOUT_SORD</td>
                 <td>Object ID</td>
                 <td>0</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_SORD</td>
                 <td>Object ID</td>
                 <td>0</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_SORD</td>
                 <td>Object ID</td>
                 <td>Object type</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_REFERENCE</td>
                 <td>Object ID</td>
                 <td>Parent ID</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_COPY_SORD</td>
                 <td>unsupported</td>
                 <td></td>
                 <td></td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_REFERENCE_SORD</td>
                 <td>Parent ID</td>
                 <td>Object ID</td>
                 <td></td>
                 <td>Parent name, Object name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_MOVE_SORD</td>
                 <td>New parent ID</td>
                 <td>Object ID</td>
                 <td>Old parent ID</td>
                 <td>New parent name, old parent name, Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LINK_SORD</td>
                 <td>From object ID</td>
                 <td>To object ID</td>
                 <td></td>
                 <td>From Sord name, To Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_UNLINK_SORD</td>
                 <td>From object ID</td>
                 <td>To object ID</td>
                 <td></td>
                 <td>From Sord name, To Sord name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKOUT_DOCVERSION</td>
                 <td>Object ID</td>
                 <td>Document version ID</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Objektname, Versionsnummer</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_DOCVERSION</td>
                 <td>Objekt-ID</td>
                 <td>Doc-ID</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Objektname, Versionsnummer</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_DOC_MASK</td>
                 <td>0</td>
                 <td>Mask-ID</td>
                 <td>0</td>
                 <td>Maskname</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_DOC_MASK</td>
                 <td>0</td>
                 <td>Mask-ID</td>
                 <td>0</td>
                 <td>Maskname</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_DOC_MASK</td>
                 <td>0</td>
                 <td>Mask-ID</td>
                 <td>replace with Mask-ID</td>
                 <td>Maskname</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_REPL_NAME</td>
                 <td>0</td>
                 <td>Repl-ID</td>
                 <td>0</td>
                 <td>ReplSet-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_REPORT_OPTIONS</td>
                 <td>0</td>
                 <td>0</td>
                 <td>0</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_REPORT</td>
                 <td>0</td>
                 <td>endDate</td>
                 <td>0</td>
                 <td>TS-End-Date</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_COLOR</td>
                 <td>0</td>
                 <td>Color-ID</td>
                 <td>rgb</td>
                 <td>Color-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_USER_PROFILE</td>
                 <td>0</td>
                 <td>For User-ID</td>
                 <td>0</td>
                 <td>User-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_USER_PROFILE</td>
                 <td>0</td>
                 <td>For User-ID</td>
                 <td>0</td>
                 <td>User-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_WORKFLOW</td>
                 <td>0</td>
                 <td>Workflow-ID</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Workflow-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_WORKFLOW</td>
                 <td>0</td>
                 <td>Workflow-ID</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Workflow-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_WORKFLOW</td>
                 <td>0</td>
                 <td>Workflow-ID</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Workflow name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_EDIT_WORKFLOW_NODE</td>
                 <td>Object-ID</td>
                 <td>Workflow-ID</td>
                 <td>Node-ID</td>
                 <td>Node name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_START_WORKFLOW</td>
                 <td>Object-ID</td>
                 <td>Workflow-ID</td>
                 <td>Template-WF-ID</td>
                 <td>Workflow name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_START_ADHOC_WORKFLOW</td>
                 <td>Object-ID</td>
                 <td>Workflow-ID</td>
                 <td>0</td>
                 <td>Workflow name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_TERMINATE_WORKFLOW</td>
                 <td>Object-ID</td>
                 <td>Workflow-ID</td>
                 <td>0</td>
                 <td>Workflow-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_CONFIG_FILE</td>
                 <td>0</td>
                 <td>0</td>
                 <td>0</td>
                 <td>Config file name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_CONFIG_FILE</td>
                 <td>0</td>
                 <td>0</td>
                 <td>0</td>
                 <td>Config file name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_COUNTER</td>
                 <td>0</td>
                 <td>Value</td>
                 <td>0</td>
                 <td>Counter-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_COUNTER</td>
                 <td>0</td>
                 <td>0</td>
                 <td>0</td>
                 <td>Counter-Name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_INCREMENT_COUNTER</td>
                 <td>0</td>
                 <td>Value</td>
                 <td>0</td>
                 <td>Counter name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_SORD_TYPE</td>
                 <td>0</td>
                 <td>ID (Sord.type)</td>
                 <td>0</td>
                 <td>Type name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_SORD_TYPE</td>
                 <td>0</td>
                 <td>ID (Sord.type)</td>
                 <td>0</td>
                 <td>Type name</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_NOTE</td>
                 <td>Objekt-ID</td>
                 <td>Note-ID (internal)</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Note-Guid</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_NOTE</td>
                 <td>Objekt-ID</td>
                 <td>Note-ID (internal)</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Note-Guid</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_NOTE</td>
                 <td>Objekt-ID</td>
                 <td>Note-ID (internal)</td>
                 <td>combination of EXTRA2_*</td>
                 <td>Note-Guid</td>
                 </tr>
                 <tr>
                 <td>ACT_DM_READDOC</td>
                 <td>Objekt-ID</td>
                 <td>Doc-ID</td>
                 <td>0</td>
                 <td>&nbsp;</td>
                 </tr>

                 <tr>
                 <td>ACT_IX_SUBSTITUTION_NEW</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_CHANGE</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_DELETE</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_ACTIVATE</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_DEACTIVATE</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>&nbsp;</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_TRANSFER</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>previous substituteId</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_FORWARD</td>
                 <td>0</td>
                 <td>{@link Substitution#userId}</td>
                 <td>{@link Substitution#substituteId}</td>
                 <td>previous substituteId</td>
                 </tr>

                 </table>

                 <p>
                 To enable or disable reporting of actions, action codes have to be transformed into ERP codes
                 first. One ERP code can subsume serverel action codes. The ERP codes can be used in
                 checkinReportOptions to manipulate reporting. Furthermore they can be used in
                 findFirstReportInfos, FindReportInfo, to search for reported actions. The following table shows
                 how actions codes are mapped to report options.
                 </p>

                 <table border="2">
                 <tr>
                 <td>Action code, ReportInfoC</td>
                 <td>ERP code, ReportOptionsC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_ELOSTART</td>
                 <td>ERP_LOGOPENARC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_ELOEND</td>
                 <td>ERP_LOGCLOSEARC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_COMPLAIN</td>
                 <td>ERP_LOGCOMPLAIN</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_DELETEDOCS</td>
                 <td>ERP_LOGERADOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_KEYCHANGED</td>
                 <td>ERP_LOGCHANGEKEY</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_USERCHANGED</td>
                 <td>ERP_LOGUSERDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_COLORCHANGED</td>
                 <td>ERP_LOGCHANGEKIND</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_PATHCHANGED</td>
                 <td>ERP_LOGPATHDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_MASKCHANGED</td>
                 <td>ERP_LOGMASKDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_PWDCHANGED</td>
                 <td>ERP_LOGCHANGEPWD</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CREATEDOC</td>
                 <td>ERP_LOGCREATEDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_EDITDOC</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHANGEDOC</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHANGEATTACH</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_VIEWDOC</td>
                 <td>ERP_LOGVIEWDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_ERASEDOC</td>
                 <td>ERP_LOGERADOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_MOVEDOC</td>
                 <td>ERP_LOGMOVEDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_REFDOC</td>
                 <td>ERP_LOGREFDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHANGEKEY</td>
                 <td>ERP_LOGCHANGEKEY</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHANGEKIND</td>
                 <td>ERP_LOGCHANGEKIND</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CONVERT_FORMAT</td>
                 <td>ERP_CONVERT_FORMAT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHECKOUT</td>
                 <td>ERP_CHECKOUT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHECKIN</td>
                 <td>ERP_CHECKIN</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CREATESOR</td>
                 <td>ERP_LOGCREATESOR</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CHANGESOR</td>
                 <td>ERP_LOGEDITDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_EDITSOR</td>
                 <td>ERP_LOGEDITDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_ERASESOR</td>
                 <td>ERP_LOGERASOR</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_MOVESOR</td>
                 <td>ERP_LOGMOVESOR</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_REFSOR</td>
                 <td>ERP_LOGREFSOR</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_ADDREF</td>
                 <td>ERP_LOGREFDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_ERASEREF</td>
                 <td>ERP_LOGERAREF</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_MOVEREF</td>
                 <td>ERP_LOGMOVEDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVNEW</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVCHANGE</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVDELETE</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVSEND</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVRECEIVE</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVNEWSEND</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_WVCHANGESEND</td>
                 <td>ERP_WV</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTFIRST</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTDELETE</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTDOCBUILD</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTEDIT</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTSCHLAGWORT</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTCOPYTO</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTMOVETO</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTMOVE</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTCOLLECT</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTNEWOLE</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTEXPAND</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTIMPORT</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_POSTLAST</td>
                 <td>ERP_POSTBOX</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_CREATEFLOWTEMPL</td>
                 <td>ERP_CREATEFLOWTEMPL</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_EDITFLOWTEMPL</td>
                 <td>ERP_EDITFLOWTEMPL</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_DELFLOWTEMPL</td>
                 <td>ERP_DELFLOWTEMPL</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_STARTFLOW</td>
                 <td>ERP_STARTFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_RECEIVEFLOW</td>
                 <td>ERP_RECEIVEFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_FORWARDFLOW</td>
                 <td>ERP_FORWARDFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_EDITFLOWACTIVE</td>
                 <td>ERP_EDITFLOWACTIVE</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_DELFLOWACTIVE</td>
                 <td>ERP_DELFLOWACTIVE</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_FLOWTIMELIMIT</td>
                 <td>ERP_FLOWTIMELIMT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_FLOWERRORYESNO</td>
                 <td>ERP_FLOWERRORYESNO</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_REPORTCHANGED</td>
                 <td>ERP_VERSCHIEDEN</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_MASKTEXTTOOLONG</td>
                 <td>ERP_VERSCHIEDEN</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_NEWVERT</td>
                 <td>ERP_NEWVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_DELVERT</td>
                 <td>ERP_DELVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_FREEVERT</td>
                 <td>ERP_FREEVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_REMOVEVERT</td>
                 <td>ERP_REMOVEVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_SETVERT</td>
                 <td>ERP_SETVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_RESETVERT</td>
                 <td>ERP_RESETVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_SHOWDOC</td>
                 <td>ERP_SHOWDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_SHOWSOR</td>
                 <td>ERP_SHOWSOR</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_DELVERSION</td>
                 <td>ERP_DELVERSION</td>
                 </tr>
                 <tr>
                 <td>ACT_CLIENT_PICKPOST</td>
                 <td>ERP_PICKPOST</td>
                 </tr>
                 <tr>
                 <td>ACT_DM_READDOC</td>
                 <td>ERP_LOGVIEWDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LOGIN</td>
                 <td>ERP_LOGOPENARC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LOGOUT</td>
                 <td>ERP_LOGCLOSEARC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LOCK_ARCHIVE</td>
                 <td>ERP_LOGCHANGEKEY</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_USER</td>
                 <td>ERP_LOGUSERDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_USER</td>
                 <td>ERP_LOGUSERDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_USER</td>
                 <td>ERP_LOGUSERDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_KEY</td>
                 <td>ERP_LOGCHANGEKEY</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_KEY</td>
                 <td>ERP_LOGCHANGEKEY</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_KEY</td>
                 <td>ERP_LOGCHANGEKEY</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_SORD</td>
                 <td>ERP_LOGCREATEDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKOUT_SORD</td>
                 <td>ERP_LOGVIEWDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_SORD</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_SORD</td>
                 <td>ERP_LOGERADOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_REFERENCE</td>
                 <td>ERP_LOGERAREF</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_COPY_SORD</td>
                 <td>ERP_LOGCREATEDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_REFERENCE_SORD</td>
                 <td>ERP_LOGREFDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_MOVE_SORD</td>
                 <td>ERP_LOGMOVEDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_LINK_SORD</td>
                 <td>ERP_LOGREFDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_UNLINK_SORD</td>
                 <td>ERP_LOGREFDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKOUT_DOCVERSION</td>
                 <td>ERP_LOGVIEWDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_DOCVERSION</td>
                 <td>ERP_CHECKIN</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_DOC_MASK</td>
                 <td>ERP_LOGMASKDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_DOC_MASK</td>
                 <td>ERP_LOGMASKDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_DOC_MASK</td>
                 <td>ERP_LOGMASKDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_REPL_NAME</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_REPORT_OPTIONS</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_REPORT</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_COLOR</td>
                 <td>ERP_LOGCOLORDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_USER_PROFILE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_USER_PROFILE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_WORKFLOW</td>
                 <td>ERP_CREATEFLOWTEMPL</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_WORKFLOW</td>
                 <td>ERP_EDITFLOWTEMPL</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_WORKFLOW</td>
                 <td>ERP_DELFLOWTEMPL</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_EDIT_WORKFLOW_NODE</td>
                 <td>ERP_FORWARDFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_START_WORKFLOW</td>
                 <td>ERP_STARTFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_START_ADHOC_WORKFLOW</td>
                 <td>ERP_STARTFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_TERMINATE_WORKFLOW</td>
                 <td>ERP_FORWARDFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_TAKE_WORKFLOW_NODE</td>
                 <td>ERP_FORWARDFLOW</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_CONFIG_FILE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_CONFIG_FILE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_COUNTER</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_COUNTER</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_INCREMENT_COUNTER</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_SORD_TYPE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_SORD_TYPE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CREATE_NOTE</td>
                 <td>ERP_LOGKEYDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_NOTE</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKOUT_NOTE</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_NOTE</td>
                 <td>ERP_LOGEDITDOC</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_NEWVERT</td>
                 <td>ERP_NEWVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELVERT</td>
                 <td>ERP_DELVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_FREEVERT</td>
                 <td>ERP_FREEVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_REMOVEVERT</td>
                 <td>ERP_REMOVEVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SETVERT</td>
                 <td>ERP_SETVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_RESETVERT</td>
                 <td>ERP_RESETVERT</td>
                 </tr>
                 <tr>
                 <td>ACT_DM_READDOC</td>
                 <td>ERP_DM_READDOC</td>
                 </tr>

                 <tr>
                 <td>ACT_IX_SUBSTITUTION_NEW</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_CHANGE</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_DELETE</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_ACTIVATE</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_DEACTIVATE</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_TRANSFER</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_SUBSTITUTION_FORWARD</td>
                 <td>ERP_SUBSTITUTIONS</td>
                 </tr>

                 <tr>
                 <td>ACT_IX_CREATE_ASPECT</td>
                 <td>ERP_LOGASPECTDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_CHECKIN_ASPECT</td>
                 <td>ERP_LOGASPECTDATA</td>
                 </tr>
                 <tr>
                 <td>ACT_IX_DELETE_ASPECT</td>
                 <td>ERP_LOGASPECTDATA</td>
                 </tr>
                 *
                 </table>
            keyword (Union[Unset, KeywordC]):
            alert (Union[Unset, AlertC]):
            take_node (Union[Unset, WFTakeNodeC]): Constant class for controlling the taking over(passing to another user)
                of a workflow object.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            aspect_line (Union[Unset, AspectLineC]): <p>
                Constants for class <code>AspectLine</code>
                 </p>
                 <p>
                 Copyright: Copyright (c) 2019
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            color (Union[Unset, ColorDataC]):
            package (Union[Unset, PackageC]): Constants for the class PackageDataC
            vt_doc (Union[Unset, VtDocC]): <p>Bit constants for members of VtDoc</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            sord_type (Union[Unset, SordTypeC]): Constants for folder or document types.
            substitution (Union[Unset, SubstitutionC]): <p>
                Bit constants for members of {@link Substitution}
                 </p>
            doc_mask_line_template (Union[Unset, DocMaskLineTemplateC]): <p>
                Constants related to class <code>DocMaskLineTemplate</code>.
            sord (Union[Unset, SordC]): <p>
                Constants for indexing information. Each member of this class with prefix "mb" has a
                 corresponding member in class <code>Sord</code>
                 </p>
            report_mode (Union[Unset, ReportModeC]):
            user_info (Union[Unset, UserInfoC]): <p>
                Constants related to user information.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            map_config (Union[Unset, MapDomainC]): This class defines constants for the predefined map tables.
            package_level (Union[Unset, PackageLevelDataC]): <p>Bit constants for members of PackageLevelData</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            acl_item (Union[Unset, AclItemC]): <p>
                Types of ACL items.
                 </p>
            invalidate_cache (Union[Unset, InvalidateCacheC]): Constants for cache invalidation.
                This constans can be used as bit combination in function
                 invalidateCache.
            counter_info (Union[Unset, CounterInfoC]): Constants class for the CounterInfo class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            aspect_assoc (Union[Unset, AspectAssocC]): <p>Bit constants for members of AspectAssoc</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            link_sord (Union[Unset, LinkSordC]): Constants for linkSord(...).
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            feed (Union[Unset, FeedC]): Constants for class Feed.
            map_data (Union[Unset, MapDataC]): Constant class for MapData
            any_ (Union[Unset, AnyC]): This class defines the constants for the type member in Any.
            reminder (Union[Unset, ReminderC]):
            public_download (Union[Unset, PublicDownloadC]): Constants for class PublicDownload.
            e_search_params (Union[Unset, ESearchParamsC]): <p>
                Constants for searchIn selector.
                 </p>
                 <p>
                 Example for multiple selection to search in title and fulltext:<br>
                 <code>searchIn = SearchObjectC.TITLE | SearchObjectC.FULLTEXT</code>
                 </p>
            file_data (Union[Unset, FileDataC]): Member constants for class FileData.
            note (Union[Unset, NoteC]): <p>
                Constants for notes.
                 </p>
            user_profile (Union[Unset, UserProfileC]): The constants in this class exist due to compatibility requirements
                with older Index Server
                versions, which gave back formatted data (Sord.xDataDispl).

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            package_data (Union[Unset, PackageDataC]): <p>Bit constants for members of PackageData</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            access (Union[Unset, AccessC]): <p>
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
            sord_hist (Union[Unset, SordHistC]): Constanst for class SordHist.
            find_direct (Union[Unset, FindDirectC]): Constants used in class FindDirect
            archiving_mode (Union[Unset, ArchivingModeC]):
            archive_statistics_options (Union[Unset, ArchiveStatisticsOptionsC]): An object of this class controls the
                function getArchiveStatistics.
            report (Union[Unset, ReportC]): <p>Bit constants for members of ReportInfo</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            map_domain (Union[Unset, MapDomainC]): This class defines constants for the predefined map tables.
            sord_hist_key (Union[Unset, SordHistKeyC]):
            crypt_info (Union[Unset, CryptInfoC]):
            workflow_export_options (Union[Unset, WorkflowExportOptionsC]): Contants related to the workflow export.
            thesaurus (Union[Unset, ThesaurusC]): <p>Bit constants for members of Thesaurus</p>
                <p>Copyright: Copyright (c) 2003</p>
                 <p>Organisation: ELO Digital Office GmbH</p>
            action (Union[Unset, ActionC]): Constants for class Action.
            store_info (Union[Unset, StoreInfoC]): Definition of a document path.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            aspect (Union[Unset, AspectC]): <p>
                Constants related to class <code>Aspect</code>.
            note_template (Union[Unset, NoteTemplateC]): Constants for class NoteTemplate
            activity (Union[Unset, ActivityC]): Constants for class Activity.
    """

    stream_version: Union[Unset, str] = UNSET
    lock: Union[Unset, "LockC"] = UNSET
    workflow_node: Union[Unset, "WFNodeC"] = UNSET
    event_bus: Union[Unset, "EventBusC"] = UNSET
    client_info: Union[Unset, "ClientInfoC"] = UNSET
    admin_mode: Union[Unset, "AdminModeC"] = UNSET
    workflow_type: Union[Unset, "WFTypeC"] = UNSET
    checkout_users: Union[Unset, "CheckoutUsersC"] = UNSET
    resolve_rights: Union[Unset, "ResolveRightsResultC"] = UNSET
    session_options: Union[Unset, "SessionOptionsC"] = UNSET
    doc_version: Union[Unset, "DocVersionC"] = UNSET
    process_info: Union[Unset, "ProcessInfoC"] = UNSET
    search_mode: Union[Unset, "SearchModeC"] = UNSET
    find_actions_info: Union[Unset, "FindActionsInfoC"] = UNSET
    export_options: Union[Unset, "ExportOptionsC"] = UNSET
    doc_mask: Union[Unset, "DocMaskC"] = UNSET
    obj_key: Union[Unset, "ObjKeyC"] = UNSET
    ixexception: Union[Unset, "IXExceptionC"] = UNSET
    report_options: Union[Unset, "ReportOptionsC"] = UNSET
    checkin_users: Union[Unset, "CheckinUsersC"] = UNSET
    config_file: Union[Unset, "ConfigFileC"] = UNSET
    workflow_node_history: Union[Unset, "WFNodeHistoryC"] = UNSET
    nav_info: Union[Unset, "NavigationInfoC"] = UNSET
    server_info_dm: Union[Unset, "ServerInfoDMC"] = UNSET
    ocr_info: Union[Unset, "OcrInfoC"] = UNSET
    search_terms: Union[Unset, "SearchTermsC"] = UNSET
    map_hist: Union[Unset, "MapHistC"] = UNSET
    workflow_version: Union[Unset, "WFVersionC"] = UNSET
    preview_image_info: Union[Unset, "PreviewImageInfoC"] = UNSET
    translate_term: Union[Unset, "TranslateTermC"] = UNSET
    edit_info: Union[Unset, "EditInfoC"] = UNSET
    fulltext_config: Union[Unset, "FulltextConfigC"] = UNSET
    subscription: Union[Unset, "SubscriptionC"] = UNSET
    docmask_inherit: Union[Unset, "DocMaskInheritC"] = UNSET
    user_task_priority: Union[Unset, "UserTaskPriorityC"] = UNSET
    user_task_sort_order: Union[Unset, "UserTaskSortOrderC"] = UNSET
    server_state: Union[Unset, "ServerStateC"] = UNSET
    indexvalue: Union[Unset, "IndexValueC"] = UNSET
    repl_set_name: Union[Unset, "ReplSetNameC"] = UNSET
    subs_info: Union[Unset, "SubsInfoC"] = UNSET
    sort_order: Union[Unset, "SortOrderC"] = UNSET
    org_unit_info: Union[Unset, "OrgUnitInfoC"] = UNSET
    doc_mask_line: Union[Unset, "DocMaskLineC"] = UNSET
    import_options: Union[Unset, "ImportOptionsC"] = UNSET
    workflow: Union[Unset, "WFDiagramC"] = UNSET
    note_freehand: Union[Unset, "NoteFreehandC"] = UNSET
    copy_sord: Union[Unset, "CopySordC"] = UNSET
    workflow_node_assoc_type: Union[Unset, "WFNodeMatrixC"] = UNSET
    activity_project: Union[Unset, "ActivityProjectC"] = UNSET
    elo_ix_opt: Union[Unset, "EloIxOptC"] = UNSET
    report_info: Union[Unset, "ReportInfoC"] = UNSET
    keyword: Union[Unset, "KeywordC"] = UNSET
    alert: Union[Unset, "AlertC"] = UNSET
    take_node: Union[Unset, "WFTakeNodeC"] = UNSET
    aspect_line: Union[Unset, "AspectLineC"] = UNSET
    color: Union[Unset, "ColorDataC"] = UNSET
    package: Union[Unset, "PackageC"] = UNSET
    vt_doc: Union[Unset, "VtDocC"] = UNSET
    sord_type: Union[Unset, "SordTypeC"] = UNSET
    substitution: Union[Unset, "SubstitutionC"] = UNSET
    doc_mask_line_template: Union[Unset, "DocMaskLineTemplateC"] = UNSET
    sord: Union[Unset, "SordC"] = UNSET
    report_mode: Union[Unset, "ReportModeC"] = UNSET
    user_info: Union[Unset, "UserInfoC"] = UNSET
    map_config: Union[Unset, "MapDomainC"] = UNSET
    package_level: Union[Unset, "PackageLevelDataC"] = UNSET
    acl_item: Union[Unset, "AclItemC"] = UNSET
    invalidate_cache: Union[Unset, "InvalidateCacheC"] = UNSET
    counter_info: Union[Unset, "CounterInfoC"] = UNSET
    aspect_assoc: Union[Unset, "AspectAssocC"] = UNSET
    link_sord: Union[Unset, "LinkSordC"] = UNSET
    feed: Union[Unset, "FeedC"] = UNSET
    map_data: Union[Unset, "MapDataC"] = UNSET
    any_: Union[Unset, "AnyC"] = UNSET
    reminder: Union[Unset, "ReminderC"] = UNSET
    public_download: Union[Unset, "PublicDownloadC"] = UNSET
    e_search_params: Union[Unset, "ESearchParamsC"] = UNSET
    file_data: Union[Unset, "FileDataC"] = UNSET
    note: Union[Unset, "NoteC"] = UNSET
    user_profile: Union[Unset, "UserProfileC"] = UNSET
    package_data: Union[Unset, "PackageDataC"] = UNSET
    access: Union[Unset, "AccessC"] = UNSET
    sord_hist: Union[Unset, "SordHistC"] = UNSET
    find_direct: Union[Unset, "FindDirectC"] = UNSET
    archiving_mode: Union[Unset, "ArchivingModeC"] = UNSET
    archive_statistics_options: Union[Unset, "ArchiveStatisticsOptionsC"] = UNSET
    report: Union[Unset, "ReportC"] = UNSET
    map_domain: Union[Unset, "MapDomainC"] = UNSET
    sord_hist_key: Union[Unset, "SordHistKeyC"] = UNSET
    crypt_info: Union[Unset, "CryptInfoC"] = UNSET
    workflow_export_options: Union[Unset, "WorkflowExportOptionsC"] = UNSET
    thesaurus: Union[Unset, "ThesaurusC"] = UNSET
    action: Union[Unset, "ActionC"] = UNSET
    store_info: Union[Unset, "StoreInfoC"] = UNSET
    aspect: Union[Unset, "AspectC"] = UNSET
    note_template: Union[Unset, "NoteTemplateC"] = UNSET
    activity: Union[Unset, "ActivityC"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stream_version = self.stream_version

        lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock.to_dict()

        workflow_node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_node, Unset):
            workflow_node = self.workflow_node.to_dict()

        event_bus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_bus, Unset):
            event_bus = self.event_bus.to_dict()

        client_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_info, Unset):
            client_info = self.client_info.to_dict()

        admin_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.admin_mode, Unset):
            admin_mode = self.admin_mode.to_dict()

        workflow_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.to_dict()

        checkout_users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_users, Unset):
            checkout_users = self.checkout_users.to_dict()

        resolve_rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolve_rights, Unset):
            resolve_rights = self.resolve_rights.to_dict()

        session_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_options, Unset):
            session_options = self.session_options.to_dict()

        doc_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_version, Unset):
            doc_version = self.doc_version.to_dict()

        process_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.process_info, Unset):
            process_info = self.process_info.to_dict()

        search_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_mode, Unset):
            search_mode = self.search_mode.to_dict()

        find_actions_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_actions_info, Unset):
            find_actions_info = self.find_actions_info.to_dict()

        export_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.export_options, Unset):
            export_options = self.export_options.to_dict()

        doc_mask: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask, Unset):
            doc_mask = self.doc_mask.to_dict()

        obj_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.obj_key, Unset):
            obj_key = self.obj_key.to_dict()

        ixexception: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ixexception, Unset):
            ixexception = self.ixexception.to_dict()

        report_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_options, Unset):
            report_options = self.report_options.to_dict()

        checkin_users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkin_users, Unset):
            checkin_users = self.checkin_users.to_dict()

        config_file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_file, Unset):
            config_file = self.config_file.to_dict()

        workflow_node_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_node_history, Unset):
            workflow_node_history = self.workflow_node_history.to_dict()

        nav_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nav_info, Unset):
            nav_info = self.nav_info.to_dict()

        server_info_dm: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_info_dm, Unset):
            server_info_dm = self.server_info_dm.to_dict()

        ocr_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ocr_info, Unset):
            ocr_info = self.ocr_info.to_dict()

        search_terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_terms, Unset):
            search_terms = self.search_terms.to_dict()

        map_hist: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_hist, Unset):
            map_hist = self.map_hist.to_dict()

        workflow_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_version, Unset):
            workflow_version = self.workflow_version.to_dict()

        preview_image_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview_image_info, Unset):
            preview_image_info = self.preview_image_info.to_dict()

        translate_term: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.translate_term, Unset):
            translate_term = self.translate_term.to_dict()

        edit_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_info, Unset):
            edit_info = self.edit_info.to_dict()

        fulltext_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulltext_config, Unset):
            fulltext_config = self.fulltext_config.to_dict()

        subscription: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        docmask_inherit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docmask_inherit, Unset):
            docmask_inherit = self.docmask_inherit.to_dict()

        user_task_priority: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_task_priority, Unset):
            user_task_priority = self.user_task_priority.to_dict()

        user_task_sort_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_task_sort_order, Unset):
            user_task_sort_order = self.user_task_sort_order.to_dict()

        server_state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_state, Unset):
            server_state = self.server_state.to_dict()

        indexvalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indexvalue, Unset):
            indexvalue = self.indexvalue.to_dict()

        repl_set_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repl_set_name, Unset):
            repl_set_name = self.repl_set_name.to_dict()

        subs_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subs_info, Unset):
            subs_info = self.subs_info.to_dict()

        sort_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.to_dict()

        org_unit_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_unit_info, Unset):
            org_unit_info = self.org_unit_info.to_dict()

        doc_mask_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask_line, Unset):
            doc_mask_line = self.doc_mask_line.to_dict()

        import_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_options, Unset):
            import_options = self.import_options.to_dict()

        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        note_freehand: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_freehand, Unset):
            note_freehand = self.note_freehand.to_dict()

        copy_sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_sord, Unset):
            copy_sord = self.copy_sord.to_dict()

        workflow_node_assoc_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_node_assoc_type, Unset):
            workflow_node_assoc_type = self.workflow_node_assoc_type.to_dict()

        activity_project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity_project, Unset):
            activity_project = self.activity_project.to_dict()

        elo_ix_opt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.elo_ix_opt, Unset):
            elo_ix_opt = self.elo_ix_opt.to_dict()

        report_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_info, Unset):
            report_info = self.report_info.to_dict()

        keyword: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict()

        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        take_node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.take_node, Unset):
            take_node = self.take_node.to_dict()

        aspect_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_line, Unset):
            aspect_line = self.aspect_line.to_dict()

        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        vt_doc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vt_doc, Unset):
            vt_doc = self.vt_doc.to_dict()

        sord_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_type, Unset):
            sord_type = self.sord_type.to_dict()

        substitution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.substitution, Unset):
            substitution = self.substitution.to_dict()

        doc_mask_line_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask_line_template, Unset):
            doc_mask_line_template = self.doc_mask_line_template.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        report_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_mode, Unset):
            report_mode = self.report_mode.to_dict()

        user_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        map_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_config, Unset):
            map_config = self.map_config.to_dict()

        package_level: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_level, Unset):
            package_level = self.package_level.to_dict()

        acl_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.acl_item, Unset):
            acl_item = self.acl_item.to_dict()

        invalidate_cache: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invalidate_cache, Unset):
            invalidate_cache = self.invalidate_cache.to_dict()

        counter_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.counter_info, Unset):
            counter_info = self.counter_info.to_dict()

        aspect_assoc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_assoc, Unset):
            aspect_assoc = self.aspect_assoc.to_dict()

        link_sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_sord, Unset):
            link_sord = self.link_sord.to_dict()

        feed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed, Unset):
            feed = self.feed.to_dict()

        map_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_data, Unset):
            map_data = self.map_data.to_dict()

        any_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.any_, Unset):
            any_ = self.any_.to_dict()

        reminder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reminder, Unset):
            reminder = self.reminder.to_dict()

        public_download: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_download, Unset):
            public_download = self.public_download.to_dict()

        e_search_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.e_search_params, Unset):
            e_search_params = self.e_search_params.to_dict()

        file_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_data, Unset):
            file_data = self.file_data.to_dict()

        note: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note, Unset):
            note = self.note.to_dict()

        user_profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_profile, Unset):
            user_profile = self.user_profile.to_dict()

        package_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_data, Unset):
            package_data = self.package_data.to_dict()

        access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        sord_hist: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_hist, Unset):
            sord_hist = self.sord_hist.to_dict()

        find_direct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_direct, Unset):
            find_direct = self.find_direct.to_dict()

        archiving_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.archiving_mode, Unset):
            archiving_mode = self.archiving_mode.to_dict()

        archive_statistics_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.archive_statistics_options, Unset):
            archive_statistics_options = self.archive_statistics_options.to_dict()

        report: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        map_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_domain, Unset):
            map_domain = self.map_domain.to_dict()

        sord_hist_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_hist_key, Unset):
            sord_hist_key = self.sord_hist_key.to_dict()

        crypt_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crypt_info, Unset):
            crypt_info = self.crypt_info.to_dict()

        workflow_export_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_export_options, Unset):
            workflow_export_options = self.workflow_export_options.to_dict()

        thesaurus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.thesaurus, Unset):
            thesaurus = self.thesaurus.to_dict()

        action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        store_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.store_info, Unset):
            store_info = self.store_info.to_dict()

        aspect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect, Unset):
            aspect = self.aspect.to_dict()

        note_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_template, Unset):
            note_template = self.note_template.to_dict()

        activity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stream_version is not UNSET:
            field_dict["STREAM_VERSION"] = stream_version
        if lock is not UNSET:
            field_dict["LOCK"] = lock
        if workflow_node is not UNSET:
            field_dict["WORKFLOW_NODE"] = workflow_node
        if event_bus is not UNSET:
            field_dict["EVENT_BUS"] = event_bus
        if client_info is not UNSET:
            field_dict["CLIENT_INFO"] = client_info
        if admin_mode is not UNSET:
            field_dict["ADMIN_MODE"] = admin_mode
        if workflow_type is not UNSET:
            field_dict["WORKFLOW_TYPE"] = workflow_type
        if checkout_users is not UNSET:
            field_dict["CHECKOUT_USERS"] = checkout_users
        if resolve_rights is not UNSET:
            field_dict["RESOLVE_RIGHTS"] = resolve_rights
        if session_options is not UNSET:
            field_dict["SESSION_OPTIONS"] = session_options
        if doc_version is not UNSET:
            field_dict["DOC_VERSION"] = doc_version
        if process_info is not UNSET:
            field_dict["PROCESS_INFO"] = process_info
        if search_mode is not UNSET:
            field_dict["SEARCH_MODE"] = search_mode
        if find_actions_info is not UNSET:
            field_dict["FIND_ACTIONS_INFO"] = find_actions_info
        if export_options is not UNSET:
            field_dict["EXPORT_OPTIONS"] = export_options
        if doc_mask is not UNSET:
            field_dict["DOC_MASK"] = doc_mask
        if obj_key is not UNSET:
            field_dict["OBJ_KEY"] = obj_key
        if ixexception is not UNSET:
            field_dict["IXEXCEPTION"] = ixexception
        if report_options is not UNSET:
            field_dict["REPORT_OPTIONS"] = report_options
        if checkin_users is not UNSET:
            field_dict["CHECKIN_USERS"] = checkin_users
        if config_file is not UNSET:
            field_dict["CONFIG_FILE"] = config_file
        if workflow_node_history is not UNSET:
            field_dict["WORKFLOW_NODE_HISTORY"] = workflow_node_history
        if nav_info is not UNSET:
            field_dict["NAV_INFO"] = nav_info
        if server_info_dm is not UNSET:
            field_dict["SERVER_INFO_DM"] = server_info_dm
        if ocr_info is not UNSET:
            field_dict["OCR_INFO"] = ocr_info
        if search_terms is not UNSET:
            field_dict["SEARCH_TERMS"] = search_terms
        if map_hist is not UNSET:
            field_dict["MAP_HIST"] = map_hist
        if workflow_version is not UNSET:
            field_dict["WORKFLOW_VERSION"] = workflow_version
        if preview_image_info is not UNSET:
            field_dict["PREVIEW_IMAGE_INFO"] = preview_image_info
        if translate_term is not UNSET:
            field_dict["TRANSLATE_TERM"] = translate_term
        if edit_info is not UNSET:
            field_dict["EDIT_INFO"] = edit_info
        if fulltext_config is not UNSET:
            field_dict["FULLTEXT_CONFIG"] = fulltext_config
        if subscription is not UNSET:
            field_dict["SUBSCRIPTION"] = subscription
        if docmask_inherit is not UNSET:
            field_dict["DOCMASK_INHERIT"] = docmask_inherit
        if user_task_priority is not UNSET:
            field_dict["USER_TASK_PRIORITY"] = user_task_priority
        if user_task_sort_order is not UNSET:
            field_dict["USER_TASK_SORT_ORDER"] = user_task_sort_order
        if server_state is not UNSET:
            field_dict["SERVER_STATE"] = server_state
        if indexvalue is not UNSET:
            field_dict["INDEXVALUE"] = indexvalue
        if repl_set_name is not UNSET:
            field_dict["REPL_SET_NAME"] = repl_set_name
        if subs_info is not UNSET:
            field_dict["SUBS_INFO"] = subs_info
        if sort_order is not UNSET:
            field_dict["SORT_ORDER"] = sort_order
        if org_unit_info is not UNSET:
            field_dict["ORG_UNIT_INFO"] = org_unit_info
        if doc_mask_line is not UNSET:
            field_dict["DOC_MASK_LINE"] = doc_mask_line
        if import_options is not UNSET:
            field_dict["IMPORT_OPTIONS"] = import_options
        if workflow is not UNSET:
            field_dict["WORKFLOW"] = workflow
        if note_freehand is not UNSET:
            field_dict["NOTE_FREEHAND"] = note_freehand
        if copy_sord is not UNSET:
            field_dict["COPY_SORD"] = copy_sord
        if workflow_node_assoc_type is not UNSET:
            field_dict["WORKFLOW_NODE_ASSOC_TYPE"] = workflow_node_assoc_type
        if activity_project is not UNSET:
            field_dict["ACTIVITY_PROJECT"] = activity_project
        if elo_ix_opt is not UNSET:
            field_dict["ELO_IX_OPT"] = elo_ix_opt
        if report_info is not UNSET:
            field_dict["REPORT_INFO"] = report_info
        if keyword is not UNSET:
            field_dict["KEYWORD"] = keyword
        if alert is not UNSET:
            field_dict["ALERT"] = alert
        if take_node is not UNSET:
            field_dict["TAKE_NODE"] = take_node
        if aspect_line is not UNSET:
            field_dict["ASPECT_LINE"] = aspect_line
        if color is not UNSET:
            field_dict["COLOR"] = color
        if package is not UNSET:
            field_dict["PACKAGE"] = package
        if vt_doc is not UNSET:
            field_dict["VT_DOC"] = vt_doc
        if sord_type is not UNSET:
            field_dict["SORD_TYPE"] = sord_type
        if substitution is not UNSET:
            field_dict["SUBSTITUTION"] = substitution
        if doc_mask_line_template is not UNSET:
            field_dict["DOC_MASK_LINE_TEMPLATE"] = doc_mask_line_template
        if sord is not UNSET:
            field_dict["SORD"] = sord
        if report_mode is not UNSET:
            field_dict["REPORT_MODE"] = report_mode
        if user_info is not UNSET:
            field_dict["USER_INFO"] = user_info
        if map_config is not UNSET:
            field_dict["MAP_CONFIG"] = map_config
        if package_level is not UNSET:
            field_dict["PACKAGE_LEVEL"] = package_level
        if acl_item is not UNSET:
            field_dict["ACL_ITEM"] = acl_item
        if invalidate_cache is not UNSET:
            field_dict["INVALIDATE_CACHE"] = invalidate_cache
        if counter_info is not UNSET:
            field_dict["COUNTER_INFO"] = counter_info
        if aspect_assoc is not UNSET:
            field_dict["ASPECT_ASSOC"] = aspect_assoc
        if link_sord is not UNSET:
            field_dict["LINK_SORD"] = link_sord
        if feed is not UNSET:
            field_dict["FEED"] = feed
        if map_data is not UNSET:
            field_dict["MAP_DATA"] = map_data
        if any_ is not UNSET:
            field_dict["ANY"] = any_
        if reminder is not UNSET:
            field_dict["REMINDER"] = reminder
        if public_download is not UNSET:
            field_dict["PUBLIC_DOWNLOAD"] = public_download
        if e_search_params is not UNSET:
            field_dict["E_SEARCH_PARAMS"] = e_search_params
        if file_data is not UNSET:
            field_dict["FILE_DATA"] = file_data
        if note is not UNSET:
            field_dict["NOTE"] = note
        if user_profile is not UNSET:
            field_dict["USER_PROFILE"] = user_profile
        if package_data is not UNSET:
            field_dict["PACKAGE_DATA"] = package_data
        if access is not UNSET:
            field_dict["ACCESS"] = access
        if sord_hist is not UNSET:
            field_dict["SORD_HIST"] = sord_hist
        if find_direct is not UNSET:
            field_dict["FIND_DIRECT"] = find_direct
        if archiving_mode is not UNSET:
            field_dict["ARCHIVING_MODE"] = archiving_mode
        if archive_statistics_options is not UNSET:
            field_dict["ARCHIVE_STATISTICS_OPTIONS"] = archive_statistics_options
        if report is not UNSET:
            field_dict["REPORT"] = report
        if map_domain is not UNSET:
            field_dict["MAP_DOMAIN"] = map_domain
        if sord_hist_key is not UNSET:
            field_dict["SORD_HIST_KEY"] = sord_hist_key
        if crypt_info is not UNSET:
            field_dict["CRYPT_INFO"] = crypt_info
        if workflow_export_options is not UNSET:
            field_dict["WORKFLOW_EXPORT_OPTIONS"] = workflow_export_options
        if thesaurus is not UNSET:
            field_dict["THESAURUS"] = thesaurus
        if action is not UNSET:
            field_dict["ACTION"] = action
        if store_info is not UNSET:
            field_dict["STORE_INFO"] = store_info
        if aspect is not UNSET:
            field_dict["ASPECT"] = aspect
        if note_template is not UNSET:
            field_dict["NOTE_TEMPLATE"] = note_template
        if activity is not UNSET:
            field_dict["ACTIVITY"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_c import AccessC
        from ..models.acl_item_c import AclItemC
        from ..models.action_c import ActionC
        from ..models.activity_c import ActivityC
        from ..models.activity_project_c import ActivityProjectC
        from ..models.admin_mode_c import AdminModeC
        from ..models.alert_c import AlertC
        from ..models.any_c import AnyC
        from ..models.archive_statistics_options_c import ArchiveStatisticsOptionsC
        from ..models.archiving_mode_c import ArchivingModeC
        from ..models.aspect_assoc_c import AspectAssocC
        from ..models.aspect_c import AspectC
        from ..models.aspect_line_c import AspectLineC
        from ..models.checkin_users_c import CheckinUsersC
        from ..models.checkout_users_c import CheckoutUsersC
        from ..models.client_info_c import ClientInfoC
        from ..models.color_data_c import ColorDataC
        from ..models.config_file_c import ConfigFileC
        from ..models.copy_sord_c import CopySordC
        from ..models.counter_info_c import CounterInfoC
        from ..models.crypt_info_c import CryptInfoC
        from ..models.doc_mask_c import DocMaskC
        from ..models.doc_mask_inherit_c import DocMaskInheritC
        from ..models.doc_mask_line_c import DocMaskLineC
        from ..models.doc_mask_line_template_c import DocMaskLineTemplateC
        from ..models.doc_version_c import DocVersionC
        from ..models.e_search_params_c import ESearchParamsC
        from ..models.edit_info_c import EditInfoC
        from ..models.elo_ix_opt_c import EloIxOptC
        from ..models.event_bus_c import EventBusC
        from ..models.export_options_c import ExportOptionsC
        from ..models.feed_c import FeedC
        from ..models.file_data_c import FileDataC
        from ..models.find_actions_info_c import FindActionsInfoC
        from ..models.find_direct_c import FindDirectC
        from ..models.fulltext_config_c import FulltextConfigC
        from ..models.import_options_c import ImportOptionsC
        from ..models.index_value_c import IndexValueC
        from ..models.invalidate_cache_c import InvalidateCacheC
        from ..models.ix_exception_c import IXExceptionC
        from ..models.keyword_c import KeywordC
        from ..models.link_sord_c import LinkSordC
        from ..models.lock_c import LockC
        from ..models.map_data_c import MapDataC
        from ..models.map_domain_c import MapDomainC
        from ..models.map_hist_c import MapHistC
        from ..models.navigation_info_c import NavigationInfoC
        from ..models.note_c import NoteC
        from ..models.note_freehand_c import NoteFreehandC
        from ..models.note_template_c import NoteTemplateC
        from ..models.obj_key_c import ObjKeyC
        from ..models.ocr_info_c import OcrInfoC
        from ..models.org_unit_info_c import OrgUnitInfoC
        from ..models.package_c import PackageC
        from ..models.package_data_c import PackageDataC
        from ..models.package_level_data_c import PackageLevelDataC
        from ..models.preview_image_info_c import PreviewImageInfoC
        from ..models.process_info_c import ProcessInfoC
        from ..models.public_download_c import PublicDownloadC
        from ..models.reminder_c import ReminderC
        from ..models.repl_set_name_c import ReplSetNameC
        from ..models.report_c import ReportC
        from ..models.report_info_c import ReportInfoC
        from ..models.report_mode_c import ReportModeC
        from ..models.report_options_c import ReportOptionsC
        from ..models.resolve_rights_result_c import ResolveRightsResultC
        from ..models.search_mode_c import SearchModeC
        from ..models.search_terms_c import SearchTermsC
        from ..models.server_info_dmc import ServerInfoDMC
        from ..models.server_state_c import ServerStateC
        from ..models.session_options_c import SessionOptionsC
        from ..models.sord_c import SordC
        from ..models.sord_hist_c import SordHistC
        from ..models.sord_hist_key_c import SordHistKeyC
        from ..models.sord_type_c import SordTypeC
        from ..models.sort_order_c import SortOrderC
        from ..models.store_info_c import StoreInfoC
        from ..models.subs_info_c import SubsInfoC
        from ..models.subscription_c import SubscriptionC
        from ..models.substitution_c import SubstitutionC
        from ..models.thesaurus_c import ThesaurusC
        from ..models.translate_term_c import TranslateTermC
        from ..models.user_info_c import UserInfoC
        from ..models.user_profile_c import UserProfileC
        from ..models.user_task_priority_c import UserTaskPriorityC
        from ..models.user_task_sort_order_c import UserTaskSortOrderC
        from ..models.vt_doc_c import VtDocC
        from ..models.wf_diagram_c import WFDiagramC
        from ..models.wf_node_c import WFNodeC
        from ..models.wf_node_history_c import WFNodeHistoryC
        from ..models.wf_node_matrix_c import WFNodeMatrixC
        from ..models.wf_take_node_c import WFTakeNodeC
        from ..models.wf_type_c import WFTypeC
        from ..models.wf_version_c import WFVersionC
        from ..models.workflow_export_options_c import WorkflowExportOptionsC

        d = src_dict.copy()
        stream_version = d.pop("STREAM_VERSION", UNSET)

        _lock = d.pop("LOCK", UNSET)
        lock: Union[Unset, LockC]
        if isinstance(_lock, Unset):
            lock = UNSET
        else:
            lock = LockC.from_dict(_lock)

        _workflow_node = d.pop("WORKFLOW_NODE", UNSET)
        workflow_node: Union[Unset, WFNodeC]
        if isinstance(_workflow_node, Unset):
            workflow_node = UNSET
        else:
            workflow_node = WFNodeC.from_dict(_workflow_node)

        _event_bus = d.pop("EVENT_BUS", UNSET)
        event_bus: Union[Unset, EventBusC]
        if isinstance(_event_bus, Unset):
            event_bus = UNSET
        else:
            event_bus = EventBusC.from_dict(_event_bus)

        _client_info = d.pop("CLIENT_INFO", UNSET)
        client_info: Union[Unset, ClientInfoC]
        if isinstance(_client_info, Unset):
            client_info = UNSET
        else:
            client_info = ClientInfoC.from_dict(_client_info)

        _admin_mode = d.pop("ADMIN_MODE", UNSET)
        admin_mode: Union[Unset, AdminModeC]
        if isinstance(_admin_mode, Unset):
            admin_mode = UNSET
        else:
            admin_mode = AdminModeC.from_dict(_admin_mode)

        _workflow_type = d.pop("WORKFLOW_TYPE", UNSET)
        workflow_type: Union[Unset, WFTypeC]
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = WFTypeC.from_dict(_workflow_type)

        _checkout_users = d.pop("CHECKOUT_USERS", UNSET)
        checkout_users: Union[Unset, CheckoutUsersC]
        if isinstance(_checkout_users, Unset):
            checkout_users = UNSET
        else:
            checkout_users = CheckoutUsersC.from_dict(_checkout_users)

        _resolve_rights = d.pop("RESOLVE_RIGHTS", UNSET)
        resolve_rights: Union[Unset, ResolveRightsResultC]
        if isinstance(_resolve_rights, Unset):
            resolve_rights = UNSET
        else:
            resolve_rights = ResolveRightsResultC.from_dict(_resolve_rights)

        _session_options = d.pop("SESSION_OPTIONS", UNSET)
        session_options: Union[Unset, SessionOptionsC]
        if isinstance(_session_options, Unset):
            session_options = UNSET
        else:
            session_options = SessionOptionsC.from_dict(_session_options)

        _doc_version = d.pop("DOC_VERSION", UNSET)
        doc_version: Union[Unset, DocVersionC]
        if isinstance(_doc_version, Unset):
            doc_version = UNSET
        else:
            doc_version = DocVersionC.from_dict(_doc_version)

        _process_info = d.pop("PROCESS_INFO", UNSET)
        process_info: Union[Unset, ProcessInfoC]
        if isinstance(_process_info, Unset):
            process_info = UNSET
        else:
            process_info = ProcessInfoC.from_dict(_process_info)

        _search_mode = d.pop("SEARCH_MODE", UNSET)
        search_mode: Union[Unset, SearchModeC]
        if isinstance(_search_mode, Unset):
            search_mode = UNSET
        else:
            search_mode = SearchModeC.from_dict(_search_mode)

        _find_actions_info = d.pop("FIND_ACTIONS_INFO", UNSET)
        find_actions_info: Union[Unset, FindActionsInfoC]
        if isinstance(_find_actions_info, Unset):
            find_actions_info = UNSET
        else:
            find_actions_info = FindActionsInfoC.from_dict(_find_actions_info)

        _export_options = d.pop("EXPORT_OPTIONS", UNSET)
        export_options: Union[Unset, ExportOptionsC]
        if isinstance(_export_options, Unset):
            export_options = UNSET
        else:
            export_options = ExportOptionsC.from_dict(_export_options)

        _doc_mask = d.pop("DOC_MASK", UNSET)
        doc_mask: Union[Unset, DocMaskC]
        if isinstance(_doc_mask, Unset):
            doc_mask = UNSET
        else:
            doc_mask = DocMaskC.from_dict(_doc_mask)

        _obj_key = d.pop("OBJ_KEY", UNSET)
        obj_key: Union[Unset, ObjKeyC]
        if isinstance(_obj_key, Unset):
            obj_key = UNSET
        else:
            obj_key = ObjKeyC.from_dict(_obj_key)

        _ixexception = d.pop("IXEXCEPTION", UNSET)
        ixexception: Union[Unset, IXExceptionC]
        if isinstance(_ixexception, Unset):
            ixexception = UNSET
        else:
            ixexception = IXExceptionC.from_dict(_ixexception)

        _report_options = d.pop("REPORT_OPTIONS", UNSET)
        report_options: Union[Unset, ReportOptionsC]
        if isinstance(_report_options, Unset):
            report_options = UNSET
        else:
            report_options = ReportOptionsC.from_dict(_report_options)

        _checkin_users = d.pop("CHECKIN_USERS", UNSET)
        checkin_users: Union[Unset, CheckinUsersC]
        if isinstance(_checkin_users, Unset):
            checkin_users = UNSET
        else:
            checkin_users = CheckinUsersC.from_dict(_checkin_users)

        _config_file = d.pop("CONFIG_FILE", UNSET)
        config_file: Union[Unset, ConfigFileC]
        if isinstance(_config_file, Unset):
            config_file = UNSET
        else:
            config_file = ConfigFileC.from_dict(_config_file)

        _workflow_node_history = d.pop("WORKFLOW_NODE_HISTORY", UNSET)
        workflow_node_history: Union[Unset, WFNodeHistoryC]
        if isinstance(_workflow_node_history, Unset):
            workflow_node_history = UNSET
        else:
            workflow_node_history = WFNodeHistoryC.from_dict(_workflow_node_history)

        _nav_info = d.pop("NAV_INFO", UNSET)
        nav_info: Union[Unset, NavigationInfoC]
        if isinstance(_nav_info, Unset):
            nav_info = UNSET
        else:
            nav_info = NavigationInfoC.from_dict(_nav_info)

        _server_info_dm = d.pop("SERVER_INFO_DM", UNSET)
        server_info_dm: Union[Unset, ServerInfoDMC]
        if isinstance(_server_info_dm, Unset):
            server_info_dm = UNSET
        else:
            server_info_dm = ServerInfoDMC.from_dict(_server_info_dm)

        _ocr_info = d.pop("OCR_INFO", UNSET)
        ocr_info: Union[Unset, OcrInfoC]
        if isinstance(_ocr_info, Unset):
            ocr_info = UNSET
        else:
            ocr_info = OcrInfoC.from_dict(_ocr_info)

        _search_terms = d.pop("SEARCH_TERMS", UNSET)
        search_terms: Union[Unset, SearchTermsC]
        if isinstance(_search_terms, Unset):
            search_terms = UNSET
        else:
            search_terms = SearchTermsC.from_dict(_search_terms)

        _map_hist = d.pop("MAP_HIST", UNSET)
        map_hist: Union[Unset, MapHistC]
        if isinstance(_map_hist, Unset):
            map_hist = UNSET
        else:
            map_hist = MapHistC.from_dict(_map_hist)

        _workflow_version = d.pop("WORKFLOW_VERSION", UNSET)
        workflow_version: Union[Unset, WFVersionC]
        if isinstance(_workflow_version, Unset):
            workflow_version = UNSET
        else:
            workflow_version = WFVersionC.from_dict(_workflow_version)

        _preview_image_info = d.pop("PREVIEW_IMAGE_INFO", UNSET)
        preview_image_info: Union[Unset, PreviewImageInfoC]
        if isinstance(_preview_image_info, Unset):
            preview_image_info = UNSET
        else:
            preview_image_info = PreviewImageInfoC.from_dict(_preview_image_info)

        _translate_term = d.pop("TRANSLATE_TERM", UNSET)
        translate_term: Union[Unset, TranslateTermC]
        if isinstance(_translate_term, Unset):
            translate_term = UNSET
        else:
            translate_term = TranslateTermC.from_dict(_translate_term)

        _edit_info = d.pop("EDIT_INFO", UNSET)
        edit_info: Union[Unset, EditInfoC]
        if isinstance(_edit_info, Unset):
            edit_info = UNSET
        else:
            edit_info = EditInfoC.from_dict(_edit_info)

        _fulltext_config = d.pop("FULLTEXT_CONFIG", UNSET)
        fulltext_config: Union[Unset, FulltextConfigC]
        if isinstance(_fulltext_config, Unset):
            fulltext_config = UNSET
        else:
            fulltext_config = FulltextConfigC.from_dict(_fulltext_config)

        _subscription = d.pop("SUBSCRIPTION", UNSET)
        subscription: Union[Unset, SubscriptionC]
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = SubscriptionC.from_dict(_subscription)

        _docmask_inherit = d.pop("DOCMASK_INHERIT", UNSET)
        docmask_inherit: Union[Unset, DocMaskInheritC]
        if isinstance(_docmask_inherit, Unset):
            docmask_inherit = UNSET
        else:
            docmask_inherit = DocMaskInheritC.from_dict(_docmask_inherit)

        _user_task_priority = d.pop("USER_TASK_PRIORITY", UNSET)
        user_task_priority: Union[Unset, UserTaskPriorityC]
        if isinstance(_user_task_priority, Unset):
            user_task_priority = UNSET
        else:
            user_task_priority = UserTaskPriorityC.from_dict(_user_task_priority)

        _user_task_sort_order = d.pop("USER_TASK_SORT_ORDER", UNSET)
        user_task_sort_order: Union[Unset, UserTaskSortOrderC]
        if isinstance(_user_task_sort_order, Unset):
            user_task_sort_order = UNSET
        else:
            user_task_sort_order = UserTaskSortOrderC.from_dict(_user_task_sort_order)

        _server_state = d.pop("SERVER_STATE", UNSET)
        server_state: Union[Unset, ServerStateC]
        if isinstance(_server_state, Unset):
            server_state = UNSET
        else:
            server_state = ServerStateC.from_dict(_server_state)

        _indexvalue = d.pop("INDEXVALUE", UNSET)
        indexvalue: Union[Unset, IndexValueC]
        if isinstance(_indexvalue, Unset):
            indexvalue = UNSET
        else:
            indexvalue = IndexValueC.from_dict(_indexvalue)

        _repl_set_name = d.pop("REPL_SET_NAME", UNSET)
        repl_set_name: Union[Unset, ReplSetNameC]
        if isinstance(_repl_set_name, Unset):
            repl_set_name = UNSET
        else:
            repl_set_name = ReplSetNameC.from_dict(_repl_set_name)

        _subs_info = d.pop("SUBS_INFO", UNSET)
        subs_info: Union[Unset, SubsInfoC]
        if isinstance(_subs_info, Unset):
            subs_info = UNSET
        else:
            subs_info = SubsInfoC.from_dict(_subs_info)

        _sort_order = d.pop("SORT_ORDER", UNSET)
        sort_order: Union[Unset, SortOrderC]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrderC.from_dict(_sort_order)

        _org_unit_info = d.pop("ORG_UNIT_INFO", UNSET)
        org_unit_info: Union[Unset, OrgUnitInfoC]
        if isinstance(_org_unit_info, Unset):
            org_unit_info = UNSET
        else:
            org_unit_info = OrgUnitInfoC.from_dict(_org_unit_info)

        _doc_mask_line = d.pop("DOC_MASK_LINE", UNSET)
        doc_mask_line: Union[Unset, DocMaskLineC]
        if isinstance(_doc_mask_line, Unset):
            doc_mask_line = UNSET
        else:
            doc_mask_line = DocMaskLineC.from_dict(_doc_mask_line)

        _import_options = d.pop("IMPORT_OPTIONS", UNSET)
        import_options: Union[Unset, ImportOptionsC]
        if isinstance(_import_options, Unset):
            import_options = UNSET
        else:
            import_options = ImportOptionsC.from_dict(_import_options)

        _workflow = d.pop("WORKFLOW", UNSET)
        workflow: Union[Unset, WFDiagramC]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WFDiagramC.from_dict(_workflow)

        _note_freehand = d.pop("NOTE_FREEHAND", UNSET)
        note_freehand: Union[Unset, NoteFreehandC]
        if isinstance(_note_freehand, Unset):
            note_freehand = UNSET
        else:
            note_freehand = NoteFreehandC.from_dict(_note_freehand)

        _copy_sord = d.pop("COPY_SORD", UNSET)
        copy_sord: Union[Unset, CopySordC]
        if isinstance(_copy_sord, Unset):
            copy_sord = UNSET
        else:
            copy_sord = CopySordC.from_dict(_copy_sord)

        _workflow_node_assoc_type = d.pop("WORKFLOW_NODE_ASSOC_TYPE", UNSET)
        workflow_node_assoc_type: Union[Unset, WFNodeMatrixC]
        if isinstance(_workflow_node_assoc_type, Unset):
            workflow_node_assoc_type = UNSET
        else:
            workflow_node_assoc_type = WFNodeMatrixC.from_dict(_workflow_node_assoc_type)

        _activity_project = d.pop("ACTIVITY_PROJECT", UNSET)
        activity_project: Union[Unset, ActivityProjectC]
        if isinstance(_activity_project, Unset):
            activity_project = UNSET
        else:
            activity_project = ActivityProjectC.from_dict(_activity_project)

        _elo_ix_opt = d.pop("ELO_IX_OPT", UNSET)
        elo_ix_opt: Union[Unset, EloIxOptC]
        if isinstance(_elo_ix_opt, Unset):
            elo_ix_opt = UNSET
        else:
            elo_ix_opt = EloIxOptC.from_dict(_elo_ix_opt)

        _report_info = d.pop("REPORT_INFO", UNSET)
        report_info: Union[Unset, ReportInfoC]
        if isinstance(_report_info, Unset):
            report_info = UNSET
        else:
            report_info = ReportInfoC.from_dict(_report_info)

        _keyword = d.pop("KEYWORD", UNSET)
        keyword: Union[Unset, KeywordC]
        if isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordC.from_dict(_keyword)

        _alert = d.pop("ALERT", UNSET)
        alert: Union[Unset, AlertC]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = AlertC.from_dict(_alert)

        _take_node = d.pop("TAKE_NODE", UNSET)
        take_node: Union[Unset, WFTakeNodeC]
        if isinstance(_take_node, Unset):
            take_node = UNSET
        else:
            take_node = WFTakeNodeC.from_dict(_take_node)

        _aspect_line = d.pop("ASPECT_LINE", UNSET)
        aspect_line: Union[Unset, AspectLineC]
        if isinstance(_aspect_line, Unset):
            aspect_line = UNSET
        else:
            aspect_line = AspectLineC.from_dict(_aspect_line)

        _color = d.pop("COLOR", UNSET)
        color: Union[Unset, ColorDataC]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = ColorDataC.from_dict(_color)

        _package = d.pop("PACKAGE", UNSET)
        package: Union[Unset, PackageC]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = PackageC.from_dict(_package)

        _vt_doc = d.pop("VT_DOC", UNSET)
        vt_doc: Union[Unset, VtDocC]
        if isinstance(_vt_doc, Unset):
            vt_doc = UNSET
        else:
            vt_doc = VtDocC.from_dict(_vt_doc)

        _sord_type = d.pop("SORD_TYPE", UNSET)
        sord_type: Union[Unset, SordTypeC]
        if isinstance(_sord_type, Unset):
            sord_type = UNSET
        else:
            sord_type = SordTypeC.from_dict(_sord_type)

        _substitution = d.pop("SUBSTITUTION", UNSET)
        substitution: Union[Unset, SubstitutionC]
        if isinstance(_substitution, Unset):
            substitution = UNSET
        else:
            substitution = SubstitutionC.from_dict(_substitution)

        _doc_mask_line_template = d.pop("DOC_MASK_LINE_TEMPLATE", UNSET)
        doc_mask_line_template: Union[Unset, DocMaskLineTemplateC]
        if isinstance(_doc_mask_line_template, Unset):
            doc_mask_line_template = UNSET
        else:
            doc_mask_line_template = DocMaskLineTemplateC.from_dict(_doc_mask_line_template)

        _sord = d.pop("SORD", UNSET)
        sord: Union[Unset, SordC]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = SordC.from_dict(_sord)

        _report_mode = d.pop("REPORT_MODE", UNSET)
        report_mode: Union[Unset, ReportModeC]
        if isinstance(_report_mode, Unset):
            report_mode = UNSET
        else:
            report_mode = ReportModeC.from_dict(_report_mode)

        _user_info = d.pop("USER_INFO", UNSET)
        user_info: Union[Unset, UserInfoC]
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = UserInfoC.from_dict(_user_info)

        _map_config = d.pop("MAP_CONFIG", UNSET)
        map_config: Union[Unset, MapDomainC]
        if isinstance(_map_config, Unset):
            map_config = UNSET
        else:
            map_config = MapDomainC.from_dict(_map_config)

        _package_level = d.pop("PACKAGE_LEVEL", UNSET)
        package_level: Union[Unset, PackageLevelDataC]
        if isinstance(_package_level, Unset):
            package_level = UNSET
        else:
            package_level = PackageLevelDataC.from_dict(_package_level)

        _acl_item = d.pop("ACL_ITEM", UNSET)
        acl_item: Union[Unset, AclItemC]
        if isinstance(_acl_item, Unset):
            acl_item = UNSET
        else:
            acl_item = AclItemC.from_dict(_acl_item)

        _invalidate_cache = d.pop("INVALIDATE_CACHE", UNSET)
        invalidate_cache: Union[Unset, InvalidateCacheC]
        if isinstance(_invalidate_cache, Unset):
            invalidate_cache = UNSET
        else:
            invalidate_cache = InvalidateCacheC.from_dict(_invalidate_cache)

        _counter_info = d.pop("COUNTER_INFO", UNSET)
        counter_info: Union[Unset, CounterInfoC]
        if isinstance(_counter_info, Unset):
            counter_info = UNSET
        else:
            counter_info = CounterInfoC.from_dict(_counter_info)

        _aspect_assoc = d.pop("ASPECT_ASSOC", UNSET)
        aspect_assoc: Union[Unset, AspectAssocC]
        if isinstance(_aspect_assoc, Unset):
            aspect_assoc = UNSET
        else:
            aspect_assoc = AspectAssocC.from_dict(_aspect_assoc)

        _link_sord = d.pop("LINK_SORD", UNSET)
        link_sord: Union[Unset, LinkSordC]
        if isinstance(_link_sord, Unset):
            link_sord = UNSET
        else:
            link_sord = LinkSordC.from_dict(_link_sord)

        _feed = d.pop("FEED", UNSET)
        feed: Union[Unset, FeedC]
        if isinstance(_feed, Unset):
            feed = UNSET
        else:
            feed = FeedC.from_dict(_feed)

        _map_data = d.pop("MAP_DATA", UNSET)
        map_data: Union[Unset, MapDataC]
        if isinstance(_map_data, Unset):
            map_data = UNSET
        else:
            map_data = MapDataC.from_dict(_map_data)

        _any_ = d.pop("ANY", UNSET)
        any_: Union[Unset, AnyC]
        if isinstance(_any_, Unset):
            any_ = UNSET
        else:
            any_ = AnyC.from_dict(_any_)

        _reminder = d.pop("REMINDER", UNSET)
        reminder: Union[Unset, ReminderC]
        if isinstance(_reminder, Unset):
            reminder = UNSET
        else:
            reminder = ReminderC.from_dict(_reminder)

        _public_download = d.pop("PUBLIC_DOWNLOAD", UNSET)
        public_download: Union[Unset, PublicDownloadC]
        if isinstance(_public_download, Unset):
            public_download = UNSET
        else:
            public_download = PublicDownloadC.from_dict(_public_download)

        _e_search_params = d.pop("E_SEARCH_PARAMS", UNSET)
        e_search_params: Union[Unset, ESearchParamsC]
        if isinstance(_e_search_params, Unset):
            e_search_params = UNSET
        else:
            e_search_params = ESearchParamsC.from_dict(_e_search_params)

        _file_data = d.pop("FILE_DATA", UNSET)
        file_data: Union[Unset, FileDataC]
        if isinstance(_file_data, Unset):
            file_data = UNSET
        else:
            file_data = FileDataC.from_dict(_file_data)

        _note = d.pop("NOTE", UNSET)
        note: Union[Unset, NoteC]
        if isinstance(_note, Unset):
            note = UNSET
        else:
            note = NoteC.from_dict(_note)

        _user_profile = d.pop("USER_PROFILE", UNSET)
        user_profile: Union[Unset, UserProfileC]
        if isinstance(_user_profile, Unset):
            user_profile = UNSET
        else:
            user_profile = UserProfileC.from_dict(_user_profile)

        _package_data = d.pop("PACKAGE_DATA", UNSET)
        package_data: Union[Unset, PackageDataC]
        if isinstance(_package_data, Unset):
            package_data = UNSET
        else:
            package_data = PackageDataC.from_dict(_package_data)

        _access = d.pop("ACCESS", UNSET)
        access: Union[Unset, AccessC]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = AccessC.from_dict(_access)

        _sord_hist = d.pop("SORD_HIST", UNSET)
        sord_hist: Union[Unset, SordHistC]
        if isinstance(_sord_hist, Unset):
            sord_hist = UNSET
        else:
            sord_hist = SordHistC.from_dict(_sord_hist)

        _find_direct = d.pop("FIND_DIRECT", UNSET)
        find_direct: Union[Unset, FindDirectC]
        if isinstance(_find_direct, Unset):
            find_direct = UNSET
        else:
            find_direct = FindDirectC.from_dict(_find_direct)

        _archiving_mode = d.pop("ARCHIVING_MODE", UNSET)
        archiving_mode: Union[Unset, ArchivingModeC]
        if isinstance(_archiving_mode, Unset):
            archiving_mode = UNSET
        else:
            archiving_mode = ArchivingModeC.from_dict(_archiving_mode)

        _archive_statistics_options = d.pop("ARCHIVE_STATISTICS_OPTIONS", UNSET)
        archive_statistics_options: Union[Unset, ArchiveStatisticsOptionsC]
        if isinstance(_archive_statistics_options, Unset):
            archive_statistics_options = UNSET
        else:
            archive_statistics_options = ArchiveStatisticsOptionsC.from_dict(_archive_statistics_options)

        _report = d.pop("REPORT", UNSET)
        report: Union[Unset, ReportC]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = ReportC.from_dict(_report)

        _map_domain = d.pop("MAP_DOMAIN", UNSET)
        map_domain: Union[Unset, MapDomainC]
        if isinstance(_map_domain, Unset):
            map_domain = UNSET
        else:
            map_domain = MapDomainC.from_dict(_map_domain)

        _sord_hist_key = d.pop("SORD_HIST_KEY", UNSET)
        sord_hist_key: Union[Unset, SordHistKeyC]
        if isinstance(_sord_hist_key, Unset):
            sord_hist_key = UNSET
        else:
            sord_hist_key = SordHistKeyC.from_dict(_sord_hist_key)

        _crypt_info = d.pop("CRYPT_INFO", UNSET)
        crypt_info: Union[Unset, CryptInfoC]
        if isinstance(_crypt_info, Unset):
            crypt_info = UNSET
        else:
            crypt_info = CryptInfoC.from_dict(_crypt_info)

        _workflow_export_options = d.pop("WORKFLOW_EXPORT_OPTIONS", UNSET)
        workflow_export_options: Union[Unset, WorkflowExportOptionsC]
        if isinstance(_workflow_export_options, Unset):
            workflow_export_options = UNSET
        else:
            workflow_export_options = WorkflowExportOptionsC.from_dict(_workflow_export_options)

        _thesaurus = d.pop("THESAURUS", UNSET)
        thesaurus: Union[Unset, ThesaurusC]
        if isinstance(_thesaurus, Unset):
            thesaurus = UNSET
        else:
            thesaurus = ThesaurusC.from_dict(_thesaurus)

        _action = d.pop("ACTION", UNSET)
        action: Union[Unset, ActionC]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ActionC.from_dict(_action)

        _store_info = d.pop("STORE_INFO", UNSET)
        store_info: Union[Unset, StoreInfoC]
        if isinstance(_store_info, Unset):
            store_info = UNSET
        else:
            store_info = StoreInfoC.from_dict(_store_info)

        _aspect = d.pop("ASPECT", UNSET)
        aspect: Union[Unset, AspectC]
        if isinstance(_aspect, Unset):
            aspect = UNSET
        else:
            aspect = AspectC.from_dict(_aspect)

        _note_template = d.pop("NOTE_TEMPLATE", UNSET)
        note_template: Union[Unset, NoteTemplateC]
        if isinstance(_note_template, Unset):
            note_template = UNSET
        else:
            note_template = NoteTemplateC.from_dict(_note_template)

        _activity = d.pop("ACTIVITY", UNSET)
        activity: Union[Unset, ActivityC]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ActivityC.from_dict(_activity)

        ix_service_port_c = cls(
            stream_version=stream_version,
            lock=lock,
            workflow_node=workflow_node,
            event_bus=event_bus,
            client_info=client_info,
            admin_mode=admin_mode,
            workflow_type=workflow_type,
            checkout_users=checkout_users,
            resolve_rights=resolve_rights,
            session_options=session_options,
            doc_version=doc_version,
            process_info=process_info,
            search_mode=search_mode,
            find_actions_info=find_actions_info,
            export_options=export_options,
            doc_mask=doc_mask,
            obj_key=obj_key,
            ixexception=ixexception,
            report_options=report_options,
            checkin_users=checkin_users,
            config_file=config_file,
            workflow_node_history=workflow_node_history,
            nav_info=nav_info,
            server_info_dm=server_info_dm,
            ocr_info=ocr_info,
            search_terms=search_terms,
            map_hist=map_hist,
            workflow_version=workflow_version,
            preview_image_info=preview_image_info,
            translate_term=translate_term,
            edit_info=edit_info,
            fulltext_config=fulltext_config,
            subscription=subscription,
            docmask_inherit=docmask_inherit,
            user_task_priority=user_task_priority,
            user_task_sort_order=user_task_sort_order,
            server_state=server_state,
            indexvalue=indexvalue,
            repl_set_name=repl_set_name,
            subs_info=subs_info,
            sort_order=sort_order,
            org_unit_info=org_unit_info,
            doc_mask_line=doc_mask_line,
            import_options=import_options,
            workflow=workflow,
            note_freehand=note_freehand,
            copy_sord=copy_sord,
            workflow_node_assoc_type=workflow_node_assoc_type,
            activity_project=activity_project,
            elo_ix_opt=elo_ix_opt,
            report_info=report_info,
            keyword=keyword,
            alert=alert,
            take_node=take_node,
            aspect_line=aspect_line,
            color=color,
            package=package,
            vt_doc=vt_doc,
            sord_type=sord_type,
            substitution=substitution,
            doc_mask_line_template=doc_mask_line_template,
            sord=sord,
            report_mode=report_mode,
            user_info=user_info,
            map_config=map_config,
            package_level=package_level,
            acl_item=acl_item,
            invalidate_cache=invalidate_cache,
            counter_info=counter_info,
            aspect_assoc=aspect_assoc,
            link_sord=link_sord,
            feed=feed,
            map_data=map_data,
            any_=any_,
            reminder=reminder,
            public_download=public_download,
            e_search_params=e_search_params,
            file_data=file_data,
            note=note,
            user_profile=user_profile,
            package_data=package_data,
            access=access,
            sord_hist=sord_hist,
            find_direct=find_direct,
            archiving_mode=archiving_mode,
            archive_statistics_options=archive_statistics_options,
            report=report,
            map_domain=map_domain,
            sord_hist_key=sord_hist_key,
            crypt_info=crypt_info,
            workflow_export_options=workflow_export_options,
            thesaurus=thesaurus,
            action=action,
            store_info=store_info,
            aspect=aspect,
            note_template=note_template,
            activity=activity,
        )

        ix_service_port_c.additional_properties = d
        return ix_service_port_c

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
