from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_diagram_z import WFDiagramZ


T = TypeVar("T", bound="WFDiagramC")


@_attrs_define
class WFDiagramC:
    """<p>
    Constants for workflows.
     </p>

        Attributes:
            mb_name_translation_key (Union[Unset, str]): Member bit: nameTranslationKey
            adhoc_wf_finish_script_prefix (Union[Unset, str]): Prefix of all scripts selectable as finish scripts for adhoc
                workflows
            mb_t_stamp (Union[Unset, str]): Member bit: TStamp
            mb_active_acl_items (Union[Unset, str]):
            mb_version (Union[Unset, str]): Member bit: access
            mb_start_date_iso (Union[Unset, str]):
            mb_active_acl (Union[Unset, str]): Member bit: {@link WFDiagram#activeAcl}.
            mb_template_id (Union[Unset, str]): Member bit: templateId
            mb_lean (Union[Unset, WFDiagramZ]): This class encapsulates the constants of the WFDiagramC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_obj_id (Union[Unset, str]): Object ID
            mb_time_limit_user_id (Union[Unset, str]): Member bit: Alert user.
            mb_acl (Union[Unset, str]): Member bit: acl and aclItems.
            mb_id (Union[Unset, str]): ID
            max_subnodes (Union[Unset, int]): Maximum number of subnodes.
            mb_completion_date (Union[Unset, str]): Completed at this date.
            mb_owner_name (Union[Unset, str]):
            mb_completion_date_iso (Union[Unset, str]):
            mb_acl_items (Union[Unset, str]):
            mb_guid (Union[Unset, str]): Member bit: Guid
            mb_deleted (Union[Unset, str]): Member bit: deleted
            mb_flags (Union[Unset, str]): Member bit: flags
            mb_matrix (Union[Unset, str]): Node matrix.
            mb_package_name (Union[Unset, str]): Member bit: {@link WFDiagram#packageName}.
            mb_process_on_server_id (Union[Unset, str]): Member bit: processOnServerId
            mb_name (Union[Unset, str]): Name
            mb_sub_workflows (Union[Unset, str]): Member bit: {@link WFDiagram#subWorkflows}.
            ln_guid (Union[Unset, int]): Maximum length of workflow GUID.
            mb_t_stamp_sync (Union[Unset, str]): Member bit: TStampSync
            ln_name_translation_key (Union[Unset, int]): Maximum length of the name's translation key.
            ln_name (Union[Unset, int]): Maximum length of workflow name.
            mb_obj_name (Union[Unset, str]): Member bit: objName
            mb_time_limit_iso (Union[Unset, str]):
            mb_prio (Union[Unset, str]): Member bit: prio
            mb_access (Union[Unset, str]): Member bit: access
            mb_only_lock (Union[Unset, WFDiagramZ]): This class encapsulates the constants of the WFDiagramC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_time_limit (Union[Unset, str]): Member bit: Time-limit.
            mb_all_members (Union[Unset, str]): All elements.
            ln_t_stamp (Union[Unset, int]): Maximum length of workflow TStamp.
            mb_nodes (Union[Unset, str]): Nodes.
            mb_lean_members (Union[Unset, str]):
            mb_time_limit_escalations (Union[Unset, str]): Member bit: timeLimitEscalation
            template_id_adhoc (Union[Unset, int]): Compare this value to WFDiagram.
                templateId to check whether the workflow was started as an
                 adhoc workflow. This member is for convenience. You can also check the flag FLAG_ROOT_ADHOC of
                 the root node.
            mb_all (Union[Unset, WFDiagramZ]): This class encapsulates the constants of the WFDiagramC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_type (Union[Unset, str]):
            mb_start_date (Union[Unset, str]): Member bit: StartDate.
            mb_lock_id (Union[Unset, str]): Member bit: lockId and lockName
            mb_obj_type (Union[Unset, str]): Object type.
            mb_owner_id (Union[Unset, str]): Member bit: ownerId and ownerName
            mb_template_name (Union[Unset, str]):
            mb_call_node_id (Union[Unset, str]): Member bit: {@link WFDiagram#callNodeId}.
            mb_nodes_overview (Union[Unset, str]): Nodes required for worfklow overview in ELO Java Client.
                Includes begin node, active nodes,
                 exceeded nodes.
            mb_time_limit_user_name (Union[Unset, str]):
            ln_process_on_server_id (Union[Unset, int]): Maximum length of processOnServerId.
    """

    mb_name_translation_key: Union[Unset, str] = UNSET
    adhoc_wf_finish_script_prefix: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_active_acl_items: Union[Unset, str] = UNSET
    mb_version: Union[Unset, str] = UNSET
    mb_start_date_iso: Union[Unset, str] = UNSET
    mb_active_acl: Union[Unset, str] = UNSET
    mb_template_id: Union[Unset, str] = UNSET
    mb_lean: Union[Unset, "WFDiagramZ"] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_time_limit_user_id: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    max_subnodes: Union[Unset, int] = UNSET
    mb_completion_date: Union[Unset, str] = UNSET
    mb_owner_name: Union[Unset, str] = UNSET
    mb_completion_date_iso: Union[Unset, str] = UNSET
    mb_acl_items: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_matrix: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_process_on_server_id: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_sub_workflows: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_obj_name: Union[Unset, str] = UNSET
    mb_time_limit_iso: Union[Unset, str] = UNSET
    mb_prio: Union[Unset, str] = UNSET
    mb_access: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "WFDiagramZ"] = UNSET
    mb_time_limit: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_nodes: Union[Unset, str] = UNSET
    mb_lean_members: Union[Unset, str] = UNSET
    mb_time_limit_escalations: Union[Unset, str] = UNSET
    template_id_adhoc: Union[Unset, int] = UNSET
    mb_all: Union[Unset, "WFDiagramZ"] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_start_date: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_obj_type: Union[Unset, str] = UNSET
    mb_owner_id: Union[Unset, str] = UNSET
    mb_template_name: Union[Unset, str] = UNSET
    mb_call_node_id: Union[Unset, str] = UNSET
    mb_nodes_overview: Union[Unset, str] = UNSET
    mb_time_limit_user_name: Union[Unset, str] = UNSET
    ln_process_on_server_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_name_translation_key = self.mb_name_translation_key

        adhoc_wf_finish_script_prefix = self.adhoc_wf_finish_script_prefix

        mb_t_stamp = self.mb_t_stamp

        mb_active_acl_items = self.mb_active_acl_items

        mb_version = self.mb_version

        mb_start_date_iso = self.mb_start_date_iso

        mb_active_acl = self.mb_active_acl

        mb_template_id = self.mb_template_id

        mb_lean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_lean, Unset):
            mb_lean = self.mb_lean.to_dict()

        mb_obj_id = self.mb_obj_id

        mb_time_limit_user_id = self.mb_time_limit_user_id

        mb_acl = self.mb_acl

        mb_id = self.mb_id

        max_subnodes = self.max_subnodes

        mb_completion_date = self.mb_completion_date

        mb_owner_name = self.mb_owner_name

        mb_completion_date_iso = self.mb_completion_date_iso

        mb_acl_items = self.mb_acl_items

        mb_guid = self.mb_guid

        mb_deleted = self.mb_deleted

        mb_flags = self.mb_flags

        mb_matrix = self.mb_matrix

        mb_package_name = self.mb_package_name

        mb_process_on_server_id = self.mb_process_on_server_id

        mb_name = self.mb_name

        mb_sub_workflows = self.mb_sub_workflows

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_name_translation_key = self.ln_name_translation_key

        ln_name = self.ln_name

        mb_obj_name = self.mb_obj_name

        mb_time_limit_iso = self.mb_time_limit_iso

        mb_prio = self.mb_prio

        mb_access = self.mb_access

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_time_limit = self.mb_time_limit

        mb_all_members = self.mb_all_members

        ln_t_stamp = self.ln_t_stamp

        mb_nodes = self.mb_nodes

        mb_lean_members = self.mb_lean_members

        mb_time_limit_escalations = self.mb_time_limit_escalations

        template_id_adhoc = self.template_id_adhoc

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_type = self.mb_type

        mb_start_date = self.mb_start_date

        mb_lock_id = self.mb_lock_id

        mb_obj_type = self.mb_obj_type

        mb_owner_id = self.mb_owner_id

        mb_template_name = self.mb_template_name

        mb_call_node_id = self.mb_call_node_id

        mb_nodes_overview = self.mb_nodes_overview

        mb_time_limit_user_name = self.mb_time_limit_user_name

        ln_process_on_server_id = self.ln_process_on_server_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if adhoc_wf_finish_script_prefix is not UNSET:
            field_dict["ADHOC_WF_FINISH_SCRIPT_PREFIX"] = adhoc_wf_finish_script_prefix
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_active_acl_items is not UNSET:
            field_dict["mbActiveAclItems"] = mb_active_acl_items
        if mb_version is not UNSET:
            field_dict["mbVersion"] = mb_version
        if mb_start_date_iso is not UNSET:
            field_dict["mbStartDateIso"] = mb_start_date_iso
        if mb_active_acl is not UNSET:
            field_dict["mbActiveAcl"] = mb_active_acl
        if mb_template_id is not UNSET:
            field_dict["mbTemplateId"] = mb_template_id
        if mb_lean is not UNSET:
            field_dict["mbLean"] = mb_lean
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_time_limit_user_id is not UNSET:
            field_dict["mbTimeLimitUserId"] = mb_time_limit_user_id
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if max_subnodes is not UNSET:
            field_dict["MAX_SUBNODES"] = max_subnodes
        if mb_completion_date is not UNSET:
            field_dict["mbCompletionDate"] = mb_completion_date
        if mb_owner_name is not UNSET:
            field_dict["mbOwnerName"] = mb_owner_name
        if mb_completion_date_iso is not UNSET:
            field_dict["mbCompletionDateIso"] = mb_completion_date_iso
        if mb_acl_items is not UNSET:
            field_dict["mbAclItems"] = mb_acl_items
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_matrix is not UNSET:
            field_dict["mbMatrix"] = mb_matrix
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_process_on_server_id is not UNSET:
            field_dict["mbProcessOnServerId"] = mb_process_on_server_id
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_sub_workflows is not UNSET:
            field_dict["mbSubWorkflows"] = mb_sub_workflows
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_obj_name is not UNSET:
            field_dict["mbObjName"] = mb_obj_name
        if mb_time_limit_iso is not UNSET:
            field_dict["mbTimeLimitIso"] = mb_time_limit_iso
        if mb_prio is not UNSET:
            field_dict["mbPrio"] = mb_prio
        if mb_access is not UNSET:
            field_dict["mbAccess"] = mb_access
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_time_limit is not UNSET:
            field_dict["mbTimeLimit"] = mb_time_limit
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_nodes is not UNSET:
            field_dict["mbNodes"] = mb_nodes
        if mb_lean_members is not UNSET:
            field_dict["mbLeanMembers"] = mb_lean_members
        if mb_time_limit_escalations is not UNSET:
            field_dict["mbTimeLimitEscalations"] = mb_time_limit_escalations
        if template_id_adhoc is not UNSET:
            field_dict["TEMPLATE_ID_ADHOC"] = template_id_adhoc
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_start_date is not UNSET:
            field_dict["mbStartDate"] = mb_start_date
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_obj_type is not UNSET:
            field_dict["mbObjType"] = mb_obj_type
        if mb_owner_id is not UNSET:
            field_dict["mbOwnerId"] = mb_owner_id
        if mb_template_name is not UNSET:
            field_dict["mbTemplateName"] = mb_template_name
        if mb_call_node_id is not UNSET:
            field_dict["mbCallNodeId"] = mb_call_node_id
        if mb_nodes_overview is not UNSET:
            field_dict["mbNodesOverview"] = mb_nodes_overview
        if mb_time_limit_user_name is not UNSET:
            field_dict["mbTimeLimitUserName"] = mb_time_limit_user_name
        if ln_process_on_server_id is not UNSET:
            field_dict["lnProcessOnServerId"] = ln_process_on_server_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_diagram_z import WFDiagramZ

        d = src_dict.copy()
        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        adhoc_wf_finish_script_prefix = d.pop("ADHOC_WF_FINISH_SCRIPT_PREFIX", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_active_acl_items = d.pop("mbActiveAclItems", UNSET)

        mb_version = d.pop("mbVersion", UNSET)

        mb_start_date_iso = d.pop("mbStartDateIso", UNSET)

        mb_active_acl = d.pop("mbActiveAcl", UNSET)

        mb_template_id = d.pop("mbTemplateId", UNSET)

        _mb_lean = d.pop("mbLean", UNSET)
        mb_lean: Union[Unset, WFDiagramZ]
        if isinstance(_mb_lean, Unset):
            mb_lean = UNSET
        else:
            mb_lean = WFDiagramZ.from_dict(_mb_lean)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_time_limit_user_id = d.pop("mbTimeLimitUserId", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        mb_id = d.pop("mbId", UNSET)

        max_subnodes = d.pop("MAX_SUBNODES", UNSET)

        mb_completion_date = d.pop("mbCompletionDate", UNSET)

        mb_owner_name = d.pop("mbOwnerName", UNSET)

        mb_completion_date_iso = d.pop("mbCompletionDateIso", UNSET)

        mb_acl_items = d.pop("mbAclItems", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_matrix = d.pop("mbMatrix", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_process_on_server_id = d.pop("mbProcessOnServerId", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_sub_workflows = d.pop("mbSubWorkflows", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_obj_name = d.pop("mbObjName", UNSET)

        mb_time_limit_iso = d.pop("mbTimeLimitIso", UNSET)

        mb_prio = d.pop("mbPrio", UNSET)

        mb_access = d.pop("mbAccess", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, WFDiagramZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = WFDiagramZ.from_dict(_mb_only_lock)

        mb_time_limit = d.pop("mbTimeLimit", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_nodes = d.pop("mbNodes", UNSET)

        mb_lean_members = d.pop("mbLeanMembers", UNSET)

        mb_time_limit_escalations = d.pop("mbTimeLimitEscalations", UNSET)

        template_id_adhoc = d.pop("TEMPLATE_ID_ADHOC", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, WFDiagramZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = WFDiagramZ.from_dict(_mb_all)

        mb_type = d.pop("mbType", UNSET)

        mb_start_date = d.pop("mbStartDate", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_obj_type = d.pop("mbObjType", UNSET)

        mb_owner_id = d.pop("mbOwnerId", UNSET)

        mb_template_name = d.pop("mbTemplateName", UNSET)

        mb_call_node_id = d.pop("mbCallNodeId", UNSET)

        mb_nodes_overview = d.pop("mbNodesOverview", UNSET)

        mb_time_limit_user_name = d.pop("mbTimeLimitUserName", UNSET)

        ln_process_on_server_id = d.pop("lnProcessOnServerId", UNSET)

        wf_diagram_c = cls(
            mb_name_translation_key=mb_name_translation_key,
            adhoc_wf_finish_script_prefix=adhoc_wf_finish_script_prefix,
            mb_t_stamp=mb_t_stamp,
            mb_active_acl_items=mb_active_acl_items,
            mb_version=mb_version,
            mb_start_date_iso=mb_start_date_iso,
            mb_active_acl=mb_active_acl,
            mb_template_id=mb_template_id,
            mb_lean=mb_lean,
            mb_obj_id=mb_obj_id,
            mb_time_limit_user_id=mb_time_limit_user_id,
            mb_acl=mb_acl,
            mb_id=mb_id,
            max_subnodes=max_subnodes,
            mb_completion_date=mb_completion_date,
            mb_owner_name=mb_owner_name,
            mb_completion_date_iso=mb_completion_date_iso,
            mb_acl_items=mb_acl_items,
            mb_guid=mb_guid,
            mb_deleted=mb_deleted,
            mb_flags=mb_flags,
            mb_matrix=mb_matrix,
            mb_package_name=mb_package_name,
            mb_process_on_server_id=mb_process_on_server_id,
            mb_name=mb_name,
            mb_sub_workflows=mb_sub_workflows,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_name_translation_key=ln_name_translation_key,
            ln_name=ln_name,
            mb_obj_name=mb_obj_name,
            mb_time_limit_iso=mb_time_limit_iso,
            mb_prio=mb_prio,
            mb_access=mb_access,
            mb_only_lock=mb_only_lock,
            mb_time_limit=mb_time_limit,
            mb_all_members=mb_all_members,
            ln_t_stamp=ln_t_stamp,
            mb_nodes=mb_nodes,
            mb_lean_members=mb_lean_members,
            mb_time_limit_escalations=mb_time_limit_escalations,
            template_id_adhoc=template_id_adhoc,
            mb_all=mb_all,
            mb_type=mb_type,
            mb_start_date=mb_start_date,
            mb_lock_id=mb_lock_id,
            mb_obj_type=mb_obj_type,
            mb_owner_id=mb_owner_id,
            mb_template_name=mb_template_name,
            mb_call_node_id=mb_call_node_id,
            mb_nodes_overview=mb_nodes_overview,
            mb_time_limit_user_name=mb_time_limit_user_name,
            ln_process_on_server_id=ln_process_on_server_id,
        )

        wf_diagram_c.additional_properties = d
        return wf_diagram_c

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
