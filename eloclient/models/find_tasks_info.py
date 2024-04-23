from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_result_access_mode import FindResultAccessMode
    from ..models.sord_z import SordZ
    from ..models.user_task_sort_order_z import UserTaskSortOrderZ


T = TypeVar("T", bound="FindTasksInfo")


@_attrs_define
class FindTasksInfo:
    """This class contains the search criteria that are required for locating a task (reminders,
    workflow tasks or activity).

        Attributes:
            incl_reminders (Union[Unset, bool]): Collect reminders.
            incl_activities (Union[Unset, bool]): Collect activities.
            lowest_priority (Union[Unset, int]): Collect tasks of this or higher priority.
            sord_z (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            all_users (Union[Unset, bool]): Collect tasks from all users.
                This member is ignored, if the current user does not have
                 administrator privileges {@link AccessC#FLAG_ADMIN}. If set to true, element {@link #userIds}
                 is ignored and the tasks of all users are selected.
            end_date_iso (Union[Unset, str]): Collect tasks up to this date.
            over_time_limit (Union[Unset, bool]): Collect nodes that exceeded the time limit.
                Workflow only
            update_in_use_date (Union[Unset, bool]): Update WFNode.inUseDateIso for selected tasks.
            incl_deputy (Union[Unset, bool]): <p>
                Collect tasks received from users for which the current user is a substitute.
                 </p>
                 <p>
                 ELO 12+: {@link #inclGroup} must be set to <code>true</code> to enable this option.
                 </p>
            highest_priority (Union[Unset, int]): Collect tasks of this or lower priority.
            incl_group (Union[Unset, bool]): Collect tasks of the users groups.
            incl_activity_types (Union[Unset, List[str]]):
            incl_workflows (Union[Unset, bool]): Collect workflows.
            start_date_iso (Union[Unset, str]): Collect tasks beginning at this date.
            sort_order (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the UserTaskSortOrderC
                class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            user_ids (Union[Unset, List[str]]):
            incl_hidden (Union[Unset, bool]): Inlcude hidden tasks. Currently this only affects workflows.
            obj_id (Union[Unset, str]): Collect tasks for this Sord (ID or GUID).
            find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
                find results.
            task_name (Union[Unset, str]): Select tasks with this name. The task name of a Reminder is Reminder.name.
                The task name of an
                 Activity is Activity.name. The task name of a workflow node is WFNode.name and
                 WFCollectNode.nodeName. This element can contain wildcard characters. The underlying database
                 column is by default not indexed. Thus, selecting only by taskName will result in a full table
                 scan.
            incl_over_time_for_superior (Union[Unset, bool]): Collect tasks for a superior as defined in the escalation
                options.
                When a workflow task exceeds
                 its time limit, and the current user is assigned in the time limit options of this task, then
                 the user receives this task from findFirstTasks/findNextTasks although she or he is not the
                 owner of the task. If an entire workflow is over time, the user receives the start node of the
                 workflow. This option applies to workflow tasks only.
            incl_deleted (Union[Unset, bool]): Select tasks for deleted folders and documents too.
            time_limit_bias (Union[Unset, int]): Time limit bias.
                This value added to each {@link WFNode#timeLimit} before evaluating whether
                 the node is over time. It is measured in minutes. Indexserver uses a timeLimitBias of 1min when
                 looking for over-timed nodes to be forwarded automatically through a
                 {@link WFNodeMatrixC#IF_OVERTIME} edge.
    """

    incl_reminders: Union[Unset, bool] = UNSET
    incl_activities: Union[Unset, bool] = UNSET
    lowest_priority: Union[Unset, int] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    all_users: Union[Unset, bool] = UNSET
    end_date_iso: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    update_in_use_date: Union[Unset, bool] = UNSET
    incl_deputy: Union[Unset, bool] = UNSET
    highest_priority: Union[Unset, int] = UNSET
    incl_group: Union[Unset, bool] = UNSET
    incl_activity_types: Union[Unset, List[str]] = UNSET
    incl_workflows: Union[Unset, bool] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    sort_order: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    user_ids: Union[Unset, List[str]] = UNSET
    incl_hidden: Union[Unset, bool] = UNSET
    obj_id: Union[Unset, str] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    task_name: Union[Unset, str] = UNSET
    incl_over_time_for_superior: Union[Unset, bool] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    time_limit_bias: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incl_reminders = self.incl_reminders

        incl_activities = self.incl_activities

        lowest_priority = self.lowest_priority

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        all_users = self.all_users

        end_date_iso = self.end_date_iso

        over_time_limit = self.over_time_limit

        update_in_use_date = self.update_in_use_date

        incl_deputy = self.incl_deputy

        highest_priority = self.highest_priority

        incl_group = self.incl_group

        incl_activity_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.incl_activity_types, Unset):
            incl_activity_types = self.incl_activity_types

        incl_workflows = self.incl_workflows

        start_date_iso = self.start_date_iso

        sort_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.to_dict()

        user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        incl_hidden = self.incl_hidden

        obj_id = self.obj_id

        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        task_name = self.task_name

        incl_over_time_for_superior = self.incl_over_time_for_superior

        incl_deleted = self.incl_deleted

        time_limit_bias = self.time_limit_bias

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incl_reminders is not UNSET:
            field_dict["inclReminders"] = incl_reminders
        if incl_activities is not UNSET:
            field_dict["inclActivities"] = incl_activities
        if lowest_priority is not UNSET:
            field_dict["lowestPriority"] = lowest_priority
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if all_users is not UNSET:
            field_dict["allUsers"] = all_users
        if end_date_iso is not UNSET:
            field_dict["endDateIso"] = end_date_iso
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if update_in_use_date is not UNSET:
            field_dict["updateInUseDate"] = update_in_use_date
        if incl_deputy is not UNSET:
            field_dict["inclDeputy"] = incl_deputy
        if highest_priority is not UNSET:
            field_dict["highestPriority"] = highest_priority
        if incl_group is not UNSET:
            field_dict["inclGroup"] = incl_group
        if incl_activity_types is not UNSET:
            field_dict["inclActivityTypes"] = incl_activity_types
        if incl_workflows is not UNSET:
            field_dict["inclWorkflows"] = incl_workflows
        if start_date_iso is not UNSET:
            field_dict["startDateIso"] = start_date_iso
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if incl_hidden is not UNSET:
            field_dict["inclHidden"] = incl_hidden
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode
        if task_name is not UNSET:
            field_dict["taskName"] = task_name
        if incl_over_time_for_superior is not UNSET:
            field_dict["inclOverTimeForSuperior"] = incl_over_time_for_superior
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted
        if time_limit_bias is not UNSET:
            field_dict["timeLimitBias"] = time_limit_bias

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.sord_z import SordZ
        from ..models.user_task_sort_order_z import UserTaskSortOrderZ

        d = src_dict.copy()
        incl_reminders = d.pop("inclReminders", UNSET)

        incl_activities = d.pop("inclActivities", UNSET)

        lowest_priority = d.pop("lowestPriority", UNSET)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        all_users = d.pop("allUsers", UNSET)

        end_date_iso = d.pop("endDateIso", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        update_in_use_date = d.pop("updateInUseDate", UNSET)

        incl_deputy = d.pop("inclDeputy", UNSET)

        highest_priority = d.pop("highestPriority", UNSET)

        incl_group = d.pop("inclGroup", UNSET)

        incl_activity_types = cast(List[str], d.pop("inclActivityTypes", UNSET))

        incl_workflows = d.pop("inclWorkflows", UNSET)

        start_date_iso = d.pop("startDateIso", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = UserTaskSortOrderZ.from_dict(_sort_order)

        user_ids = cast(List[str], d.pop("userIds", UNSET))

        incl_hidden = d.pop("inclHidden", UNSET)

        obj_id = d.pop("objId", UNSET)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        task_name = d.pop("taskName", UNSET)

        incl_over_time_for_superior = d.pop("inclOverTimeForSuperior", UNSET)

        incl_deleted = d.pop("inclDeleted", UNSET)

        time_limit_bias = d.pop("timeLimitBias", UNSET)

        find_tasks_info = cls(
            incl_reminders=incl_reminders,
            incl_activities=incl_activities,
            lowest_priority=lowest_priority,
            sord_z=sord_z,
            all_users=all_users,
            end_date_iso=end_date_iso,
            over_time_limit=over_time_limit,
            update_in_use_date=update_in_use_date,
            incl_deputy=incl_deputy,
            highest_priority=highest_priority,
            incl_group=incl_group,
            incl_activity_types=incl_activity_types,
            incl_workflows=incl_workflows,
            start_date_iso=start_date_iso,
            sort_order=sort_order,
            user_ids=user_ids,
            incl_hidden=incl_hidden,
            obj_id=obj_id,
            find_result_access_mode=find_result_access_mode,
            task_name=task_name,
            incl_over_time_for_superior=incl_over_time_for_superior,
            incl_deleted=incl_deleted,
            time_limit_bias=time_limit_bias,
        )

        find_tasks_info.additional_properties = d
        return find_tasks_info

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
