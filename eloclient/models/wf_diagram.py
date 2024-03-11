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
        acl (Union[Unset, str]): Access control list in the internal format. It defines who is able to edit the
            workflow.
            This member is only valid
             for workflow templates.
        acl_items (Union[Unset, List['AclItem']]):
        active_acl (Union[Unset, str]): Access control list in the internal format. It defines who is able to edit the
            workflow.
            This member is only valid
             for active workflows.
        active_acl_items (Union[Unset, List['AclItem']]):
        completion_date_iso (Union[Unset, str]): Date of completion in ISO format.
        deleted (Union[Unset, bool]): Flag that indicates whether the workflow template is deleted. Only valid for
            template workflows.
        id (Union[Unset, int]): Workflow ID.
        lock_id (Union[Unset, int]): The ID of the user who has currently locked the workflow.
        lock_name (Union[Unset, str]): The name of the user who has currently locked the workflow.
        matrix (Union[Unset, WFNodeMatrix]): <p>
            Stores the relationship between workflow nodes
             </p>
             <p>
             Administers the bridges(connections) in a workflow diagram. These are objects of type WorkFlowNodeAssoc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office
             </p>
        name (Union[Unset, str]): Workflow name.
        nodes (Union[Unset, List['WFNode']]):
        obj_id (Union[Unset, str]): ID or GUID of the associated folder or document object.
            checkoutWorkFlow will always return the numeric object ID
             in this field. checkinWorkFlow is able to receive a GUID too.
        obj_type (Union[Unset, int]): Sord type of the associated folder or document.
        owner_id (Union[Unset, int]): ID of the user who has started the workflow.
        owner_name (Union[Unset, str]): Name of the user who has started the workflow.
        prio (Union[Unset, int]): Workflow priortiy: 0...high, 1...medium, 2...low.
        start_date_iso (Union[Unset, str]): Date of start in ISO format.
        template_id (Union[Unset, int]): The workflow was started based on this workflow template.
            This member is only valid for active and finished
             workflows.
        template_name (Union[Unset, str]): The workflow was started based on the workflow template with this name.
            This member is only valid for active and
             finished workflows.
        time_limit (Union[Unset, int]): Time-limit for the entire workflow in minutes.
        time_limit_iso (Union[Unset, str]): The entire workflow should be finished by this date. Otherwise the time-
            limit is exceeded.
            This member is only
             valid for active and finished workflows. Read-only.
        time_limit_user_id (Union[Unset, int]): The ID of the user that should be informed,if the time-limit for the
            workflow is exceeded.
            The Indexserver does not
             send any notification to the user. The client application is responsible for doing this.
        time_limit_user_name (Union[Unset, str]): The name of the user that should be informed, if the time-limit is
            exceeded.
            When writing a workflow with
             checkinWorkFlow, this value has preceedence before timeLimitUserId. Set timeLimitUserName to an empty string,
            if
             timeLimitUserId should be used.
        type (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        over_time_limit (Union[Unset, bool]): True, if the workflow exceeds the time limit. Read-only.
        flags (Union[Unset, int]): Flags of the begin node. This value is a combination of the node flags suitable to
            begin nodes, e. g.
            WFNodeC.FLAG_WORKINGDAYS. To ensure compatibility with older client programs, the WFNode.flags of the start node
             are or-ed with the WFDiagram.flags.
        access (Union[Unset, int]): Access rights to the workflow template for the current user. A combination of LUR_*
            constants. Read-only.
        version (Union[Unset, WFVersion]): Version information for a workflow template.
        guid (Union[Unset, str]): GUID
        t_stamp (Union[Unset, str]): TStamp
        process_on_server_id (Union[Unset, str]): If not empty, the workflow can only be continued on this server (resp.
            replication branch).
            The current server ID
             can be read by getServerInfo(). This member is only valid for ACTIVE or FINISHED workflows.
        time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
        obj_name (Union[Unset, str]): Sord name. Readonly.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link WFDiagram#name}.
        hidden (Union[Unset, bool]): Indicates whether this workflow is hidden.
        parent_flow_id (Union[Unset, int]): ID of the parent workflow.
        call_node_id (Union[Unset, int]): The call node id of the main workflow, which call this sub workflow.
        sub_workflows (Union[Unset, MapToWFDiagram]):
        package_name (Union[Unset, str]): Package name of WFDiagram
    """

    acl: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    active_acl: Union[Unset, str] = UNSET
    active_acl_items: Union[Unset, List["AclItem"]] = UNSET
    completion_date_iso: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    matrix: Union[Unset, "WFNodeMatrix"] = UNSET
    name: Union[Unset, str] = UNSET
    nodes: Union[Unset, List["WFNode"]] = UNSET
    obj_id: Union[Unset, str] = UNSET
    obj_type: Union[Unset, int] = UNSET
    owner_id: Union[Unset, int] = UNSET
    owner_name: Union[Unset, str] = UNSET
    prio: Union[Unset, int] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    template_id: Union[Unset, int] = UNSET
    template_name: Union[Unset, str] = UNSET
    time_limit: Union[Unset, int] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    time_limit_user_id: Union[Unset, int] = UNSET
    time_limit_user_name: Union[Unset, str] = UNSET
    type: Union[Unset, "WFTypeZ"] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    flags: Union[Unset, int] = UNSET
    access: Union[Unset, int] = UNSET
    version: Union[Unset, "WFVersion"] = UNSET
    guid: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    process_on_server_id: Union[Unset, str] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    obj_name: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    parent_flow_id: Union[Unset, int] = UNSET
    call_node_id: Union[Unset, int] = UNSET
    sub_workflows: Union[Unset, "MapToWFDiagram"] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acl = self.acl
        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()

                acl_items.append(acl_items_item)

        active_acl = self.active_acl
        active_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.active_acl_items, Unset):
            active_acl_items = []
            for active_acl_items_item_data in self.active_acl_items:
                active_acl_items_item = active_acl_items_item_data.to_dict()

                active_acl_items.append(active_acl_items_item)

        completion_date_iso = self.completion_date_iso
        deleted = self.deleted
        id = self.id
        lock_id = self.lock_id
        lock_name = self.lock_name
        matrix: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.matrix, Unset):
            matrix = self.matrix.to_dict()

        name = self.name
        nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()

                nodes.append(nodes_item)

        obj_id = self.obj_id
        obj_type = self.obj_type
        owner_id = self.owner_id
        owner_name = self.owner_name
        prio = self.prio
        start_date_iso = self.start_date_iso
        template_id = self.template_id
        template_name = self.template_name
        time_limit = self.time_limit
        time_limit_iso = self.time_limit_iso
        time_limit_user_id = self.time_limit_user_id
        time_limit_user_name = self.time_limit_user_name
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        over_time_limit = self.over_time_limit
        flags = self.flags
        access = self.access
        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        guid = self.guid
        t_stamp = self.t_stamp
        process_on_server_id = self.process_on_server_id
        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()

                time_limit_escalations.append(time_limit_escalations_item)

        obj_name = self.obj_name
        t_stamp_sync = self.t_stamp_sync
        name_translation_key = self.name_translation_key
        hidden = self.hidden
        parent_flow_id = self.parent_flow_id
        call_node_id = self.call_node_id
        sub_workflows: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sub_workflows, Unset):
            sub_workflows = self.sub_workflows.to_dict()

        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acl is not UNSET:
            field_dict["acl"] = acl
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if active_acl is not UNSET:
            field_dict["activeAcl"] = active_acl
        if active_acl_items is not UNSET:
            field_dict["activeAclItems"] = active_acl_items
        if completion_date_iso is not UNSET:
            field_dict["completionDateIso"] = completion_date_iso
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if id is not UNSET:
            field_dict["id"] = id
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if matrix is not UNSET:
            field_dict["matrix"] = matrix
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if obj_type is not UNSET:
            field_dict["objType"] = obj_type
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if prio is not UNSET:
            field_dict["prio"] = prio
        if start_date_iso is not UNSET:
            field_dict["startDateIso"] = start_date_iso
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if time_limit_user_id is not UNSET:
            field_dict["timeLimitUserId"] = time_limit_user_id
        if time_limit_user_name is not UNSET:
            field_dict["timeLimitUserName"] = time_limit_user_name
        if type is not UNSET:
            field_dict["type"] = type
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if flags is not UNSET:
            field_dict["flags"] = flags
        if access is not UNSET:
            field_dict["access"] = access
        if version is not UNSET:
            field_dict["version"] = version
        if guid is not UNSET:
            field_dict["guid"] = guid
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if process_on_server_id is not UNSET:
            field_dict["processOnServerId"] = process_on_server_id
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if obj_name is not UNSET:
            field_dict["objName"] = obj_name
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if parent_flow_id is not UNSET:
            field_dict["parentFlowId"] = parent_flow_id
        if call_node_id is not UNSET:
            field_dict["callNodeId"] = call_node_id
        if sub_workflows is not UNSET:
            field_dict["subWorkflows"] = sub_workflows
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

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
        acl = d.pop("acl", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        active_acl = d.pop("activeAcl", UNSET)

        active_acl_items = []
        _active_acl_items = d.pop("activeAclItems", UNSET)
        for active_acl_items_item_data in _active_acl_items or []:
            active_acl_items_item = AclItem.from_dict(active_acl_items_item_data)

            active_acl_items.append(active_acl_items_item)

        completion_date_iso = d.pop("completionDateIso", UNSET)

        deleted = d.pop("deleted", UNSET)

        id = d.pop("id", UNSET)

        lock_id = d.pop("lockId", UNSET)

        lock_name = d.pop("lockName", UNSET)

        _matrix = d.pop("matrix", UNSET)
        matrix: Union[Unset, WFNodeMatrix]
        if isinstance(_matrix, Unset):
            matrix = UNSET
        else:
            matrix = WFNodeMatrix.from_dict(_matrix)

        name = d.pop("name", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = WFNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        obj_id = d.pop("objId", UNSET)

        obj_type = d.pop("objType", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        prio = d.pop("prio", UNSET)

        start_date_iso = d.pop("startDateIso", UNSET)

        template_id = d.pop("templateId", UNSET)

        template_name = d.pop("templateName", UNSET)

        time_limit = d.pop("timeLimit", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        time_limit_user_id = d.pop("timeLimitUserId", UNSET)

        time_limit_user_name = d.pop("timeLimitUserName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, WFTypeZ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WFTypeZ.from_dict(_type)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        flags = d.pop("flags", UNSET)

        access = d.pop("access", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, WFVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = WFVersion.from_dict(_version)

        guid = d.pop("guid", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        process_on_server_id = d.pop("processOnServerId", UNSET)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        obj_name = d.pop("objName", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        hidden = d.pop("hidden", UNSET)

        parent_flow_id = d.pop("parentFlowId", UNSET)

        call_node_id = d.pop("callNodeId", UNSET)

        _sub_workflows = d.pop("subWorkflows", UNSET)
        sub_workflows: Union[Unset, MapToWFDiagram]
        if isinstance(_sub_workflows, Unset):
            sub_workflows = UNSET
        else:
            sub_workflows = MapToWFDiagram.from_dict(_sub_workflows)

        package_name = d.pop("packageName", UNSET)

        wf_diagram = cls(
            acl=acl,
            acl_items=acl_items,
            active_acl=active_acl,
            active_acl_items=active_acl_items,
            completion_date_iso=completion_date_iso,
            deleted=deleted,
            id=id,
            lock_id=lock_id,
            lock_name=lock_name,
            matrix=matrix,
            name=name,
            nodes=nodes,
            obj_id=obj_id,
            obj_type=obj_type,
            owner_id=owner_id,
            owner_name=owner_name,
            prio=prio,
            start_date_iso=start_date_iso,
            template_id=template_id,
            template_name=template_name,
            time_limit=time_limit,
            time_limit_iso=time_limit_iso,
            time_limit_user_id=time_limit_user_id,
            time_limit_user_name=time_limit_user_name,
            type=type,
            over_time_limit=over_time_limit,
            flags=flags,
            access=access,
            version=version,
            guid=guid,
            t_stamp=t_stamp,
            process_on_server_id=process_on_server_id,
            time_limit_escalations=time_limit_escalations,
            obj_name=obj_name,
            t_stamp_sync=t_stamp_sync,
            name_translation_key=name_translation_key,
            hidden=hidden,
            parent_flow_id=parent_flow_id,
            call_node_id=call_node_id,
            sub_workflows=sub_workflows,
            package_name=package_name,
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
