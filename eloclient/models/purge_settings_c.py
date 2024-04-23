from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurgeSettingsC")


@_attrs_define
class PurgeSettingsC:
    """Constants for class PurgeSettings

    Attributes:
        compare_off (Union[Unset, int]): for fileCheckMode: no file comparison (not recommended)
        compare_content (Union[Unset, int]): for fileCheckMode: file comparision by file content
        start_every_hour (Union[Unset, int]): for startHour: when the purge task is starting and then every 60 minutes
        compare_size (Union[Unset, int]): for fileCheckMode: file comparison by file size
    """

    compare_off: Union[Unset, int] = UNSET
    compare_content: Union[Unset, int] = UNSET
    start_every_hour: Union[Unset, int] = UNSET
    compare_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compare_off = self.compare_off

        compare_content = self.compare_content

        start_every_hour = self.start_every_hour

        compare_size = self.compare_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compare_off is not UNSET:
            field_dict["COMPARE_OFF"] = compare_off
        if compare_content is not UNSET:
            field_dict["COMPARE_CONTENT"] = compare_content
        if start_every_hour is not UNSET:
            field_dict["START_EVERY_HOUR"] = start_every_hour
        if compare_size is not UNSET:
            field_dict["COMPARE_SIZE"] = compare_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compare_off = d.pop("COMPARE_OFF", UNSET)

        compare_content = d.pop("COMPARE_CONTENT", UNSET)

        start_every_hour = d.pop("START_EVERY_HOUR", UNSET)

        compare_size = d.pop("COMPARE_SIZE", UNSET)

        purge_settings_c = cls(
            compare_off=compare_off,
            compare_content=compare_content,
            start_every_hour=start_every_hour,
            compare_size=compare_size,
        )

        purge_settings_c.additional_properties = d
        return purge_settings_c

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
