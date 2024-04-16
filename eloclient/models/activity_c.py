from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_z import ActivityZ


T = TypeVar("T", bound="ActivityC")


@_attrs_define
class ActivityC:
    """Constants for class Activity.

    Attributes:
        mb_all (Union[Unset, ActivityZ]): Typed element selector for class Activity.
        mb_only_guid (Union[Unset, ActivityZ]): Typed element selector for class Activity.
        mb_activity_and_object_guid (Union[Unset, ActivityZ]): Typed element selector for class Activity.
    """

    mb_all: Union[Unset, "ActivityZ"] = UNSET
    mb_only_guid: Union[Unset, "ActivityZ"] = UNSET
    mb_activity_and_object_guid: Union[Unset, "ActivityZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_only_guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_guid, Unset):
            mb_only_guid = self.mb_only_guid.to_dict()

        mb_activity_and_object_guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_activity_and_object_guid, Unset):
            mb_activity_and_object_guid = self.mb_activity_and_object_guid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_only_guid is not UNSET:
            field_dict["mbOnlyGuid"] = mb_only_guid
        if mb_activity_and_object_guid is not UNSET:
            field_dict["mbActivityAndObjectGuid"] = mb_activity_and_object_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_z import ActivityZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, ActivityZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = ActivityZ.from_dict(_mb_all)

        _mb_only_guid = d.pop("mbOnlyGuid", UNSET)
        mb_only_guid: Union[Unset, ActivityZ]
        if isinstance(_mb_only_guid, Unset):
            mb_only_guid = UNSET
        else:
            mb_only_guid = ActivityZ.from_dict(_mb_only_guid)

        _mb_activity_and_object_guid = d.pop("mbActivityAndObjectGuid", UNSET)
        mb_activity_and_object_guid: Union[Unset, ActivityZ]
        if isinstance(_mb_activity_and_object_guid, Unset):
            mb_activity_and_object_guid = UNSET
        else:
            mb_activity_and_object_guid = ActivityZ.from_dict(_mb_activity_and_object_guid)

        activity_c = cls(
            mb_all=mb_all,
            mb_only_guid=mb_only_guid,
            mb_activity_and_object_guid=mb_activity_and_object_guid,
        )

        activity_c.additional_properties = d
        return activity_c

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
