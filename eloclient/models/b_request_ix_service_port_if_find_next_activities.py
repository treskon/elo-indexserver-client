from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_z import ActivityZ
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFFindNextActivities")


@_attrs_define
class BRequestIXServicePortIFFindNextActivities:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        search_id (Union[Unset, str]):
        idx (Union[Unset, int]):
        max_ (Union[Unset, int]):
        activity_z (Union[Unset, ActivityZ]): Typed element selector for class Activity.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    search_id: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    max_: Union[Unset, int] = UNSET
    activity_z: Union[Unset, "ActivityZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        search_id = self.search_id
        idx = self.idx
        max_ = self.max_
        activity_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity_z, Unset):
            activity_z = self.activity_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if max_ is not UNSET:
            field_dict["max"] = max_
        if activity_z is not UNSET:
            field_dict["activityZ"] = activity_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_z import ActivityZ
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        search_id = d.pop("searchId", UNSET)

        idx = d.pop("idx", UNSET)

        max_ = d.pop("max", UNSET)

        _activity_z = d.pop("activityZ", UNSET)
        activity_z: Union[Unset, ActivityZ]
        if isinstance(_activity_z, Unset):
            activity_z = UNSET
        else:
            activity_z = ActivityZ.from_dict(_activity_z)

        b_request_ix_service_port_if_find_next_activities = cls(
            ci=ci,
            search_id=search_id,
            idx=idx,
            max_=max_,
            activity_z=activity_z,
        )

        b_request_ix_service_port_if_find_next_activities.additional_properties = d
        return b_request_ix_service_port_if_find_next_activities

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
