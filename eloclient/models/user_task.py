from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity import Activity
    from ..models.reminder import Reminder
    from ..models.sord import Sord
    from ..models.wf_collect_node import WFCollectNode


T = TypeVar("T", bound="UserTask")


@_attrs_define
class UserTask:
    """Describes the tasks assigned to a user. ix.
    findFirstTasks returns the tasks for a user in the
     form of UserTask objects. Either activity, reminder or workflow is set depending upon whether the
     task is an activity, reminder or workflow task.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            wf_node (Union[Unset, WFCollectNode]): <p>
                Data used to display a workflow node int the task view.
                 </p>
                 <p>
                 This class bundles the data which is required for displaying a workflow node. The class is used
                 by <code>findFirstTasks</code>
                 </p>
            activity (Union[Unset, Activity]): This class represents an activity.
                <p>
                 An activity is a task delegated to an instance outside the ELO system. It is created when the
                 task is sent to the instance and deleted, if it is received back. An activity defines a date for
                 expecting the response, <code>dueDateIso</code>. At this date, the activity appears in the task
                 list of the initiator. If the task is finished, the initiator sets the <code>backAt</code> member
                 and the activity is closed.
                 </p>
                 <p>
                 Activities can be used to observe a document or a folder. For each modification, a ELO_NOTIFY
                 activity is created and displayed in the task list of the user that wants to observe the object.
                 </p>
                 <p>
                 An activity object is an instance on an activity project. The project defines the properties the
                 user can edit or select to provide more information to the task.
                 </p>
            reminder (Union[Unset, Reminder]):
            sord (Union[Unset, Sord]): <p>
                Indexing information of an archive entry.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    wf_node: Union[Unset, "WFCollectNode"] = UNSET
    activity: Union[Unset, "Activity"] = UNSET
    reminder: Union[Unset, "Reminder"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wf_node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wf_node, Unset):
            wf_node = self.wf_node.to_dict()

        activity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        reminder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reminder, Unset):
            reminder = self.reminder.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wf_node is not UNSET:
            field_dict["wfNode"] = wf_node
        if activity is not UNSET:
            field_dict["activity"] = activity
        if reminder is not UNSET:
            field_dict["reminder"] = reminder
        if sord is not UNSET:
            field_dict["sord"] = sord

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity import Activity
        from ..models.reminder import Reminder
        from ..models.sord import Sord
        from ..models.wf_collect_node import WFCollectNode

        d = src_dict.copy()
        _wf_node = d.pop("wfNode", UNSET)
        wf_node: Union[Unset, WFCollectNode]
        if isinstance(_wf_node, Unset):
            wf_node = UNSET
        else:
            wf_node = WFCollectNode.from_dict(_wf_node)

        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, Activity]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = Activity.from_dict(_activity)

        _reminder = d.pop("reminder", UNSET)
        reminder: Union[Unset, Reminder]
        if isinstance(_reminder, Unset):
            reminder = UNSET
        else:
            reminder = Reminder.from_dict(_reminder)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        user_task = cls(
            wf_node=wf_node,
            activity=activity,
            reminder=reminder,
            sord=sord,
        )

        user_task.additional_properties = d
        return user_task

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
