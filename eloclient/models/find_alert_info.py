from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindAlertInfo")


@_attrs_define
class FindAlertInfo:
    """Find criterias for selecting alerts.
    RESERVED

        Attributes:
            source_id (Union[Unset, str]): Find alerts created by this user, ID or name.
            incl_work_flow (Union[Unset, bool]): Find workflow notifications. Ignored, if <code>inclAll</code> is true.
            incl_subs (Union[Unset, bool]): Find notifications related to substitution rules. Ignored, if
                <code>inclAll</code> is true.
            dest_id (Union[Unset, str]): Find alerts sendet to this user, ID or name.
                Only main administrators can set this value to an
                 arbitary user ID. Other users can only set one of her or his groups or one of her or his
                 substituted users.
            time_iso (Union[Unset, str]): Find notifiations with this create date or in this date range.
                A date range must be separated
                 by "...".
            incl_reminder (Union[Unset, bool]): Find reminder notifications. Ignored, if <code>inclAll</code> is true.
            obj_id (Union[Unset, str]): Find notifications related to this object. For valid values see
                <code>checkoutSord</code>.
            incl_all (Union[Unset, bool]): Find all notification types.
                If this member is set, the other members related to notification
                 types are ignored.
            incl_alam (Union[Unset, bool]): Find alarm notifications. Ignored, if <code>inclAll</code> is true.
            incl_in_tray (Union[Unset, bool]): Find notifications related to the In Tray. Ignored, if <code>inclAll</code>
                is true.
            incl_others (Union[Unset, bool]): Find all other notifications that are not explicitly listed here.
                Ignored, if
                 <code>inclAll</code> is true.
    """

    source_id: Union[Unset, str] = UNSET
    incl_work_flow: Union[Unset, bool] = UNSET
    incl_subs: Union[Unset, bool] = UNSET
    dest_id: Union[Unset, str] = UNSET
    time_iso: Union[Unset, str] = UNSET
    incl_reminder: Union[Unset, bool] = UNSET
    obj_id: Union[Unset, str] = UNSET
    incl_all: Union[Unset, bool] = UNSET
    incl_alam: Union[Unset, bool] = UNSET
    incl_in_tray: Union[Unset, bool] = UNSET
    incl_others: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_id = self.source_id

        incl_work_flow = self.incl_work_flow

        incl_subs = self.incl_subs

        dest_id = self.dest_id

        time_iso = self.time_iso

        incl_reminder = self.incl_reminder

        obj_id = self.obj_id

        incl_all = self.incl_all

        incl_alam = self.incl_alam

        incl_in_tray = self.incl_in_tray

        incl_others = self.incl_others

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if incl_work_flow is not UNSET:
            field_dict["inclWorkFlow"] = incl_work_flow
        if incl_subs is not UNSET:
            field_dict["inclSubs"] = incl_subs
        if dest_id is not UNSET:
            field_dict["destId"] = dest_id
        if time_iso is not UNSET:
            field_dict["timeIso"] = time_iso
        if incl_reminder is not UNSET:
            field_dict["inclReminder"] = incl_reminder
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if incl_all is not UNSET:
            field_dict["inclAll"] = incl_all
        if incl_alam is not UNSET:
            field_dict["inclAlam"] = incl_alam
        if incl_in_tray is not UNSET:
            field_dict["inclInTray"] = incl_in_tray
        if incl_others is not UNSET:
            field_dict["inclOthers"] = incl_others

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_id = d.pop("sourceId", UNSET)

        incl_work_flow = d.pop("inclWorkFlow", UNSET)

        incl_subs = d.pop("inclSubs", UNSET)

        dest_id = d.pop("destId", UNSET)

        time_iso = d.pop("timeIso", UNSET)

        incl_reminder = d.pop("inclReminder", UNSET)

        obj_id = d.pop("objId", UNSET)

        incl_all = d.pop("inclAll", UNSET)

        incl_alam = d.pop("inclAlam", UNSET)

        incl_in_tray = d.pop("inclInTray", UNSET)

        incl_others = d.pop("inclOthers", UNSET)

        find_alert_info = cls(
            source_id=source_id,
            incl_work_flow=incl_work_flow,
            incl_subs=incl_subs,
            dest_id=dest_id,
            time_iso=time_iso,
            incl_reminder=incl_reminder,
            obj_id=obj_id,
            incl_all=incl_all,
            incl_alam=incl_alam,
            incl_in_tray=incl_in_tray,
            incl_others=incl_others,
        )

        find_alert_info.additional_properties = d
        return find_alert_info

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
