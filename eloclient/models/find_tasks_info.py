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
    """This class contains the search criteria that are required for locating a task (reminders, workflow tasks or
    activity).

        Attributes:
            end_date_iso (Union[Unset, str]): Collect tasks up to this date.
            highest_priority (Union[Unset, int]): Collect tasks of this or lower priority.
            incl_activities (Union[Unset, bool]): Collect activities.
            incl_deputy (Union[Unset, bool]): <p>
                Collect tasks received from users for which the current user is a substitute.
                 </p>
                 <p>
                 ELO 12+: {@link #inclGroup} must be set to <code>true</code> to enable this option.
                 </p>
            incl_group (Union[Unset, bool]): Collect tasks of the users groups.
            incl_reminders (Union[Unset, bool]): Collect reminders.
            incl_workflows (Union[Unset, bool]): Collect workflows.
            lowest_priority (Union[Unset, int]): Collect tasks of this or higher priority.
            obj_id (Union[Unset, str]): Collect tasks for this Sord (ID or GUID).
            sort_order (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the UserTaskSortOrderC
                class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            start_date_iso (Union[Unset, str]): Collect tasks beginning at this date.
            over_time_limit (Union[Unset, bool]): Collect nodes that exceeded the time limit.
                Workflow only
            incl_over_time_for_superior (Union[Unset, bool]): Collect tasks for a superior as defined in the escalation
                options.
                When a workflow task exceeds its time limit, and
                 the current user is assigned in the time limit options of this task, then the user receives this task from
                 findFirstTasks/findNextTasks although she or he is not the owner of the task. If an entire workflow is over
                time,
                 the user receives the start node of the workflow. This option applies to workflow tasks only.
            user_ids (Union[Unset, List[str]]):
            incl_deleted (Union[Unset, bool]): Select tasks for deleted folders and documents too.
            all_users (Union[Unset, bool]): Collect tasks from all users.
                This member is ignored, if the current user does not have administrator privileges
                 {@link AccessC#FLAG_ADMIN}. If set to true, element {@link #userIds} is ignored and the tasks of all users are
                 selected.
            sord_z (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            task_name (Union[Unset, str]): Select tasks with this name. The task name of a Reminder is Reminder.name.
                The task name of an Activity is
                 Activity.name. The task name of a workflow node is WFNode.name and WFCollectNode.nodeName. This element can
                contain
                 wildcard characters. The underlying database column is by default not indexed. Thus, selecting only by taskName
                 will result in a full table scan.
            update_in_use_date (Union[Unset, bool]): Update WFNode.inUseDateIso for selected tasks.
            incl_activity_types (Union[Unset, List[str]]):
            incl_hidden (Union[Unset, bool]): Inlcude hidden tasks. Currently this only affects workflows.
            time_limit_bias (Union[Unset, int]): Time limit bias. This value added to each {@link WFNode#timeLimit} before
                evaluating whether the node is over time.
                It is measured in minutes. Indexserver uses a timeLimitBias of 1min when looking for over-timed nodes to be
                 forwarded automatically through a {@link WFNodeMatrixC#IF_OVERTIME} edge.
            find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
                find results.
    """

    end_date_iso: Union[Unset, str] = UNSET
    highest_priority: Union[Unset, int] = UNSET
    incl_activities: Union[Unset, bool] = UNSET
    incl_deputy: Union[Unset, bool] = UNSET
    incl_group: Union[Unset, bool] = UNSET
    incl_reminders: Union[Unset, bool] = UNSET
    incl_workflows: Union[Unset, bool] = UNSET
    lowest_priority: Union[Unset, int] = UNSET
    obj_id: Union[Unset, str] = UNSET
    sort_order: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    incl_over_time_for_superior: Union[Unset, bool] = UNSET
    user_ids: Union[Unset, List[str]] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    all_users: Union[Unset, bool] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    task_name: Union[Unset, str] = UNSET
    update_in_use_date: Union[Unset, bool] = UNSET
    incl_activity_types: Union[Unset, List[str]] = UNSET
    incl_hidden: Union[Unset, bool] = UNSET
    time_limit_bias: Union[Unset, int] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_date_iso = self.end_date_iso
        highest_priority = self.highest_priority
        incl_activities = self.incl_activities
        incl_deputy = self.incl_deputy
        incl_group = self.incl_group
        incl_reminders = self.incl_reminders
        incl_workflows = self.incl_workflows
        lowest_priority = self.lowest_priority
        obj_id = self.obj_id
        sort_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.to_dict()

        start_date_iso = self.start_date_iso
        over_time_limit = self.over_time_limit
        incl_over_time_for_superior = self.incl_over_time_for_superior
        user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        incl_deleted = self.incl_deleted
        all_users = self.all_users
        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        task_name = self.task_name
        update_in_use_date = self.update_in_use_date
        incl_activity_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.incl_activity_types, Unset):
            incl_activity_types = self.incl_activity_types

        incl_hidden = self.incl_hidden
        time_limit_bias = self.time_limit_bias
        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date_iso is not UNSET:
            field_dict["endDateIso"] = end_date_iso
        if highest_priority is not UNSET:
            field_dict["highestPriority"] = highest_priority
        if incl_activities is not UNSET:
            field_dict["inclActivities"] = incl_activities
        if incl_deputy is not UNSET:
            field_dict["inclDeputy"] = incl_deputy
        if incl_group is not UNSET:
            field_dict["inclGroup"] = incl_group
        if incl_reminders is not UNSET:
            field_dict["inclReminders"] = incl_reminders
        if incl_workflows is not UNSET:
            field_dict["inclWorkflows"] = incl_workflows
        if lowest_priority is not UNSET:
            field_dict["lowestPriority"] = lowest_priority
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if start_date_iso is not UNSET:
            field_dict["startDateIso"] = start_date_iso
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if incl_over_time_for_superior is not UNSET:
            field_dict["inclOverTimeForSuperior"] = incl_over_time_for_superior
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted
        if all_users is not UNSET:
            field_dict["allUsers"] = all_users
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if task_name is not UNSET:
            field_dict["taskName"] = task_name
        if update_in_use_date is not UNSET:
            field_dict["updateInUseDate"] = update_in_use_date
        if incl_activity_types is not UNSET:
            field_dict["inclActivityTypes"] = incl_activity_types
        if incl_hidden is not UNSET:
            field_dict["inclHidden"] = incl_hidden
        if time_limit_bias is not UNSET:
            field_dict["timeLimitBias"] = time_limit_bias
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.sord_z import SordZ
        from ..models.user_task_sort_order_z import UserTaskSortOrderZ

        d = src_dict.copy()
        end_date_iso = d.pop("endDateIso", UNSET)

        highest_priority = d.pop("highestPriority", UNSET)

        incl_activities = d.pop("inclActivities", UNSET)

        incl_deputy = d.pop("inclDeputy", UNSET)

        incl_group = d.pop("inclGroup", UNSET)

        incl_reminders = d.pop("inclReminders", UNSET)

        incl_workflows = d.pop("inclWorkflows", UNSET)

        lowest_priority = d.pop("lowestPriority", UNSET)

        obj_id = d.pop("objId", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = UserTaskSortOrderZ.from_dict(_sort_order)

        start_date_iso = d.pop("startDateIso", UNSET)

        over_time_limit = d.pop("overTimeLimit", UNSET)

        incl_over_time_for_superior = d.pop("inclOverTimeForSuperior", UNSET)

        user_ids = cast(List[str], d.pop("userIds", UNSET))

        incl_deleted = d.pop("inclDeleted", UNSET)

        all_users = d.pop("allUsers", UNSET)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        task_name = d.pop("taskName", UNSET)

        update_in_use_date = d.pop("updateInUseDate", UNSET)

        incl_activity_types = cast(List[str], d.pop("inclActivityTypes", UNSET))

        incl_hidden = d.pop("inclHidden", UNSET)

        time_limit_bias = d.pop("timeLimitBias", UNSET)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        find_tasks_info = cls(
            end_date_iso=end_date_iso,
            highest_priority=highest_priority,
            incl_activities=incl_activities,
            incl_deputy=incl_deputy,
            incl_group=incl_group,
            incl_reminders=incl_reminders,
            incl_workflows=incl_workflows,
            lowest_priority=lowest_priority,
            obj_id=obj_id,
            sort_order=sort_order,
            start_date_iso=start_date_iso,
            over_time_limit=over_time_limit,
            incl_over_time_for_superior=incl_over_time_for_superior,
            user_ids=user_ids,
            incl_deleted=incl_deleted,
            all_users=all_users,
            sord_z=sord_z,
            task_name=task_name,
            update_in_use_date=update_in_use_date,
            incl_activity_types=incl_activity_types,
            incl_hidden=incl_hidden,
            time_limit_bias=time_limit_bias,
            find_result_access_mode=find_result_access_mode,
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
