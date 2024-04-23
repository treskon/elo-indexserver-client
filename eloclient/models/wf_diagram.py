from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.map_to_wf_diagram import MapToWFDiagram
    from ..models.wf_node import WFNode
    from ..models.wf_node_matrix import WFNodeMatrix
    from ..models.wf_time_limit import WFTimeLimit
    from ..models.wf_type_z import WFTypeZ
    from ..models.wf_version import WFVersion


T = TypeVar("T", bound="WFDiagram")


@_attrs_define
class WFDiagram:
    """This class represents an active or finished workflow or a workflow template

    Attributes:
        access (Union[Unset, int]): Access rights to the workflow template for the current user. A combination of LUR_*
            constants.
            Read-only.
        process_on_server_id (Union[Unset, str]): If not empty, the workflow can only be continued on this server (resp.
            replication branch).
            The
             current server ID can be read by getServerInfo(). This member is only valid for ACTIVE or
             FINISHED workflows.
        hidden (Union[Unset, bool]): Indicates whether this workflow is hidden.
        time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
        flags (Union[Unset, int]): Flags of the begin node.
            This value is a combination of the node flags suitable to begin nodes,
             e. g. WFNodeC.FLAG_WORKINGDAYS. To ensure compatibility with older client programs, the
             WFNode.flags of the start node are or-ed with the WFDiagram.flags.
        acl (Union[Unset, str]): Access control list in the internal format. It defines who is able to edit the
            workflow.
            This
             member is only valid for workflow templates.
        active_acl (Union[Unset, str]): Access control list in the internal format. It defines who is able to edit the
            workflow.
            This
             member is only valid for active workflows.
        over_time_limit (Union[Unset, bool]): True, if the workflow exceeds the time limit. Read-only.
        matrix (Union[Unset, WFNodeMatrix]): <p>
            Stores the relationship between workflow nodes
             </p>
             <p>
             Administers the bridges(connections) in a workflow diagram. These are objects of type
             WorkFlowNodeAssoc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office
             </p>
        owner_id (Union[Unset, int]): ID of the user who has started the workflow.
        template_id (Union[Unset, int]): The workflow was started based on this workflow template.
            This member is only valid for active
             and finished workflows.
        type (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        owner_name (Union[Unset, str]): Name of the user who has started the workflow.
        completion_date_iso (Union[Unset, str]): Date of completion in ISO format.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        t_stamp (Union[Unset, str]): TStamp
        id (Union[Unset, int]): Workflow ID.
        package_name (Union[Unset, str]): Package name of WFDiagram
        prio (Union[Unset, int]): Workflow priortiy: 0...high, 1...medium, 2...low.
        lock_name (Union[Unset, str]): The name of the user who has currently locked the workflow.
        obj_type (Union[Unset, int]): Sord type of the associated folder or document.
        time_limit_iso (Union[Unset, str]): The entire workflow should be finished by this date. Otherwise the time-
            limit is exceeded.
            This
             member is only valid for active and finished workflows. Read-only.
        call_node_id (Union[Unset, int]): The call node id of the main workflow, which call this sub workflow.
        active_acl_items (Union[Unset, List['AclItem']]):
        obj_name (Union[Unset, str]): Sord name. Readonly.
        version (Union[Unset, WFVersion]): Version information for a workflow template.
        lock_id (Union[Unset, int]): The ID of the user who has currently locked the workflow.
        time_limit (Union[Unset, int]): Time-limit for the entire workflow in minutes.
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFDiagram#name}.
        parent_flow_id (Union[Unset, int]): ID of the parent workflow.
        deleted (Union[Unset, bool]): Flag that indicates whether the workflow template is deleted.
            Only valid for template
             workflows.
        nodes (Union[Unset, List['WFNode']]):
        template_name (Union[Unset, str]): The workflow was started based on the workflow template with this name.
            This member is only
             valid for active and finished workflows.
        sub_workflows (Union[Unset, MapToWFDiagram]):
        start_date_iso (Union[Unset, str]): Date of start in ISO format.
        acl_items (Union[Unset, List['AclItem']]):
        time_limit_user_name (Union[Unset, str]): The name of the user that should be informed, if the time-limit is
            exceeded.
            When writing a
             workflow with checkinWorkFlow, this value has preceedence before timeLimitUserId. Set
             timeLimitUserName to an empty string, if timeLimitUserId should be used.
        name (Union[Unset, str]): Workflow name.
        obj_id (Union[Unset, str]): ID or GUID of the associated folder or document object.
            checkoutWorkFlow will always return the
             numeric object ID in this field. checkinWorkFlow is able to receive a GUID too.
        guid (Union[Unset, str]): GUID
        time_limit_user_id (Union[Unset, int]): The ID of the user that should be informed,if the time-limit for the
            workflow is exceeded.
            The
             Indexserver does not send any notification to the user. The client application is responsible
             for doing this.
    """

    access: Union[Unset, int] = UNSET
    process_on_server_id: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    flags: Union[Unset, int] = UNSET
    acl: Union[Unset, str] = UNSET
    active_acl: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    matrix: Union[Unset, "WFNodeMatrix"] = UNSET
    owner_id: Union[Unset, int] = UNSET
    template_id: Union[Unset, int] = UNSET
    type: Union[Unset, "WFTypeZ"] = UNSET
    owner_name: Union[Unset, str] = UNSET
    completion_date_iso: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    package_name: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    obj_type: Union[Unset, int] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    call_node_id: Union[Unset, int] = UNSET
    active_acl_items: Union[Unset, List["AclItem"]] = UNSET
    obj_name: Union[Unset, str] = UNSET
    version: Union[Unset, "WFVersion"] = UNSET
    lock_id: Union[Unset, int] = UNSET
    time_limit: Union[Unset, int] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    parent_flow_id: Union[Unset, int] = UNSET
    deleted: Union[Unset, bool] = UNSET
    nodes: Union[Unset, List["WFNode"]] = UNSET
    template_name: Union[Unset, str] = UNSET
    sub_workflows: Union[Unset, "MapToWFDiagram"] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    time_limit_user_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    time_limit_user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access

        process_on_server_id = self.process_on_server_id

        hidden = self.hidden

        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()
                time_limit_escalations.append(time_limit_escalations_item)

        flags = self.flags

        acl = self.acl

        active_acl = self.active_acl

        over_time_limit = self.over_time_limit

        matrix: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.matrix, Unset):
            matrix = self.matrix.to_dict()

        owner_id = self.owner_id

        template_id = self.template_id

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        owner_name = self.owner_name

        completion_date_iso = self.completion_date_iso

        t_stamp_sync = self.t_stamp_sync

        t_stamp = self.t_stamp

        id = self.id

        package_name = self.package_name

        prio = self.prio

        lock_name = self.lock_name

        obj_type = self.obj_type

        time_limit_iso = self.time_limit_iso

        call_node_id = self.call_node_id

        active_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.active_acl_items, Unset):
            active_acl_items = []
            for active_acl_items_item_data in self.active_acl_items:
                active_acl_items_item = active_acl_items_item_data.to_dict()
                active_acl_items.append(active_acl_items_item)

        obj_name = self.obj_name

        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        lock_id = self.lock_id

        time_limit = self.time_limit

        name_translation_key = self.name_translation_key

        parent_flow_id = self.parent_flow_id

        deleted = self.deleted

        nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        template_name = self.template_name

        sub_workflows: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_workflows, Unset):
            sub_workflows = self.sub_workflows.to_dict()

        start_date_iso = self.start_date_iso

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        time_limit_user_name = self.time_limit_user_name

        name = self.name

        obj_id = self.obj_id

        guid = self.guid

        time_limit_user_id = self.time_limit_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if process_on_server_id is not UNSET:
            field_dict["processOnServerId"] = process_on_server_id
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if flags is not UNSET:
            field_dict["flags"] = flags
        if acl is not UNSET:
            field_dict["acl"] = acl
        if active_acl is not UNSET:
            field_dict["activeAcl"] = active_acl
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if matrix is not UNSET:
            field_dict["matrix"] = matrix
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if type is not UNSET:
            field_dict["type"] = type
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if completion_date_iso is not UNSET:
            field_dict["completionDateIso"] = completion_date_iso
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if id is not UNSET:
            field_dict["id"] = id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if prio is not UNSET:
            field_dict["prio"] = prio
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if call_node_id is not UNSET:
            field_dict["callNodeId"] = call_node_id
        if active_acl_items is not UNSET:
            field_dict["activeAclItems"] = active_acl_items
        if obj_name is not UNSET:
            field_dict["objName"] = obj_name
        if version is not UNSET:
            field_dict["version"] = version
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if parent_flow_id is not UNSET:
            field_dict["parentFlowId"] = parent_flow_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if sub_workflows is not UNSET:
            field_dict["subWorkflows"] = sub_workflows
        if start_date_iso is not UNSET:
            field_dict["startDateIso"] = start_date_iso
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if time_limit_user_name is not UNSET:
            field_dict["timeLimitUserName"] = time_limit_user_name
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if time_limit_user_id is not UNSET:
            field_dict["timeLimitUserId"] = time_limit_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.map_to_wf_diagram import MapToWFDiagram
        from ..models.wf_node import WFNode
        from ..models.wf_node_matrix import WFNodeMatrix
        from ..models.wf_time_limit import WFTimeLimit
        from ..models.wf_type_z import WFTypeZ
        from ..models.wf_version import WFVersion

        d = src_dict.copy()
        access = d.pop("access", UNSET)

        process_on_server_id = d.pop("processOnServerId", UNSET)

        hidden = d.pop("hidden", UNSET)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        flags = d.pop("flags", UNSET)

        acl = d.pop("acl", UNSET)

        active_acl = d.pop("activeAcl", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        _matrix = d.pop("matrix", UNSET)
        matrix: Union[Unset, WFNodeMatrix]
        if isinstance(_matrix, Unset):
            matrix = UNSET
        else:
            matrix = WFNodeMatrix.from_dict(_matrix)

        owner_id = d.pop("ownerId", UNSET)

        template_id = d.pop("templateId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, WFTypeZ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WFTypeZ.from_dict(_type)

        owner_name = d.pop("ownerName", UNSET)

        completion_date_iso = d.pop("completionDateIso", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        id = d.pop("id", UNSET)

        package_name = d.pop("packageName", UNSET)

        prio = d.pop("prio", UNSET)

        lock_name = d.pop("lockName", UNSET)

        obj_type = d.pop("objType", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        call_node_id = d.pop("callNodeId", UNSET)

        active_acl_items = []
        _active_acl_items = d.pop("activeAclItems", UNSET)
        for active_acl_items_item_data in _active_acl_items or []:
            active_acl_items_item = AclItem.from_dict(active_acl_items_item_data)

            active_acl_items.append(active_acl_items_item)

        obj_name = d.pop("objName", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, WFVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = WFVersion.from_dict(_version)

        lock_id = d.pop("lockId", UNSET)

        time_limit = d.pop("timeLimit", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        parent_flow_id = d.pop("parentFlowId", UNSET)

        deleted = d.pop("deleted", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = WFNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        template_name = d.pop("templateName", UNSET)

        _sub_workflows = d.pop("subWorkflows", UNSET)
        sub_workflows: Union[Unset, MapToWFDiagram]
        if isinstance(_sub_workflows, Unset):
            sub_workflows = UNSET
        else:
            sub_workflows = MapToWFDiagram.from_dict(_sub_workflows)

        start_date_iso = d.pop("startDateIso", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        time_limit_user_name = d.pop("timeLimitUserName", UNSET)

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        guid = d.pop("guid", UNSET)

        time_limit_user_id = d.pop("timeLimitUserId", UNSET)

        wf_diagram = cls(
            access=access,
            process_on_server_id=process_on_server_id,
            hidden=hidden,
            time_limit_escalations=time_limit_escalations,
            flags=flags,
            acl=acl,
            active_acl=active_acl,
            over_time_limit=over_time_limit,
            matrix=matrix,
            owner_id=owner_id,
            template_id=template_id,
            type=type,
            owner_name=owner_name,
            completion_date_iso=completion_date_iso,
            t_stamp_sync=t_stamp_sync,
            t_stamp=t_stamp,
            id=id,
            package_name=package_name,
            prio=prio,
            lock_name=lock_name,
            obj_type=obj_type,
            time_limit_iso=time_limit_iso,
            call_node_id=call_node_id,
            active_acl_items=active_acl_items,
            obj_name=obj_name,
            version=version,
            lock_id=lock_id,
            time_limit=time_limit,
            name_translation_key=name_translation_key,
            parent_flow_id=parent_flow_id,
            deleted=deleted,
            nodes=nodes,
            template_name=template_name,
            sub_workflows=sub_workflows,
            start_date_iso=start_date_iso,
            acl_items=acl_items,
            time_limit_user_name=time_limit_user_name,
            name=name,
            obj_id=obj_id,
            guid=guid,
            time_limit_user_id=time_limit_user_id,
        )

        wf_diagram.additional_properties = d
        return wf_diagram

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
