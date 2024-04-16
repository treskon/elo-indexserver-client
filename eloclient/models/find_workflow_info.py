from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_result_access_mode import FindResultAccessMode
    from ..models.sord_z import SordZ
    from ..models.wf_type_z import WFTypeZ


T = TypeVar("T", bound="FindWorkflowInfo")


@_attrs_define
class FindWorkflowInfo:
    """This class contains the search criteria for selecting workflows.
    <p>
     Copyright: Copyright (c) 2008, 2010
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            owner_ids (Union[Unset, List[str]]):
            sord_z (Union[Unset, SordZ]): <p>
                This class encapsulates the constants of <code>SordC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            exclude_user_groups (Union[Unset, bool]): If true, only select workflows of the users. The group workflows are
                excluded.
            active_user_ids (Union[Unset, List[str]]):
            over_time_limit (Union[Unset, bool]): Collect only WFs that exceeded the time limit.
                The entire WF or one of its nodes must be over
                 time.
            type (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            template_id (Union[Unset, str]): Workflow template ID or name.
                If not null and not empty, the result is constrained to workflows
                 based on this workflow template.
            completion_date_iso (Union[Unset, str]): Completion date.
                If not null and not empty, workflows completed at this date or in this date
                 range are returned. Only valid if <code>wfType=FINISHED</code>. A time span can be specified by
                 using "...".
            start_date_iso (Union[Unset, str]): Start date.
                If not null and not empty, workflows started at this date or in this date range are
                 returned. It can be a single date value or a time span of two ISO dates separated by "...". To
                 return workflows with a start date up to a given time, set startDateIso="..."+time (the first
                 time value can be omitted).
            user_ids (Union[Unset, List[str]]):
            incl_hidden (Union[Unset, bool]): If true, include hidden/technical workflows with the result.
            name (Union[Unset, str]): Workflow name.
                If not null and not empty, it the search is restricted to workflows named like
                 this value. It may contain wildcards, e. g. *bill*.
            obj_id (Union[Unset, str]): Object ID. Active and finished workflows only.
                If not null and not empty, only workflows
                 assigned to this object are returned.
            find_result_access_mode (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of
                find results.
            incl_deleted (Union[Unset, bool]): Only template workflows: include deleted templates.
    """

    owner_ids: Union[Unset, List[str]] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    exclude_user_groups: Union[Unset, bool] = UNSET
    active_user_ids: Union[Unset, List[str]] = UNSET
    over_time_limit: Union[Unset, bool] = UNSET
    type: Union[Unset, "WFTypeZ"] = UNSET
    template_id: Union[Unset, str] = UNSET
    completion_date_iso: Union[Unset, str] = UNSET
    start_date_iso: Union[Unset, str] = UNSET
    user_ids: Union[Unset, List[str]] = UNSET
    incl_hidden: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    find_result_access_mode: Union[Unset, "FindResultAccessMode"] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.owner_ids, Unset):
            owner_ids = self.owner_ids

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        exclude_user_groups = self.exclude_user_groups

        active_user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.active_user_ids, Unset):
            active_user_ids = self.active_user_ids

        over_time_limit = self.over_time_limit

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        template_id = self.template_id

        completion_date_iso = self.completion_date_iso

        start_date_iso = self.start_date_iso

        user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        incl_hidden = self.incl_hidden

        name = self.name

        obj_id = self.obj_id

        find_result_access_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result_access_mode, Unset):
            find_result_access_mode = self.find_result_access_mode.to_dict()

        incl_deleted = self.incl_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_ids is not UNSET:
            field_dict["ownerIds"] = owner_ids
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if exclude_user_groups is not UNSET:
            field_dict["excludeUserGroups"] = exclude_user_groups
        if active_user_ids is not UNSET:
            field_dict["activeUserIds"] = active_user_ids
        if over_time_limit is not UNSET:
            field_dict["overTimeLimit"] = over_time_limit
        if type is not UNSET:
            field_dict["type"] = type
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if completion_date_iso is not UNSET:
            field_dict["completionDateIso"] = completion_date_iso
        if start_date_iso is not UNSET:
            field_dict["startDateIso"] = start_date_iso
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if incl_hidden is not UNSET:
            field_dict["inclHidden"] = incl_hidden
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if find_result_access_mode is not UNSET:
            field_dict["findResultAccessMode"] = find_result_access_mode
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_result_access_mode import FindResultAccessMode
        from ..models.sord_z import SordZ
        from ..models.wf_type_z import WFTypeZ

        d = src_dict.copy()
        owner_ids = cast(List[str], d.pop("ownerIds", UNSET))

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        exclude_user_groups = d.pop("excludeUserGroups", UNSET)

        active_user_ids = cast(List[str], d.pop("activeUserIds", UNSET))

        over_time_limit = d.pop("overTimeLimit", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, WFTypeZ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WFTypeZ.from_dict(_type)

        template_id = d.pop("templateId", UNSET)

        completion_date_iso = d.pop("completionDateIso", UNSET)

        start_date_iso = d.pop("startDateIso", UNSET)

        user_ids = cast(List[str], d.pop("userIds", UNSET))

        incl_hidden = d.pop("inclHidden", UNSET)

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        _find_result_access_mode = d.pop("findResultAccessMode", UNSET)
        find_result_access_mode: Union[Unset, FindResultAccessMode]
        if isinstance(_find_result_access_mode, Unset):
            find_result_access_mode = UNSET
        else:
            find_result_access_mode = FindResultAccessMode.from_dict(_find_result_access_mode)

        incl_deleted = d.pop("inclDeleted", UNSET)

        find_workflow_info = cls(
            owner_ids=owner_ids,
            sord_z=sord_z,
            exclude_user_groups=exclude_user_groups,
            active_user_ids=active_user_ids,
            over_time_limit=over_time_limit,
            type=type,
            template_id=template_id,
            completion_date_iso=completion_date_iso,
            start_date_iso=start_date_iso,
            user_ids=user_ids,
            incl_hidden=incl_hidden,
            name=name,
            obj_id=obj_id,
            find_result_access_mode=find_result_access_mode,
            incl_deleted=incl_deleted,
        )

        find_workflow_info.additional_properties = d
        return find_workflow_info

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
