from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurgeSettings")


@_attrs_define
class PurgeSettings:
    """This class represents the purge settings of the ELOdm purge task

    Attributes:
        exclude_path_ids (Union[Unset, List[int]]):
        day_limit (Union[Unset, int]): Original documents older than the specified number of days are deleted (0 or
            higher), e.g.
            0
             for no limit, 1 for 24 hours, 365 for a year
        start_hour (Union[Unset, int]): When processing should take place: <br>
            START_EVERY_HOUR: when the purge task is starting and then every 60 minutes <br>
             0 to 23: hour of the day, such as 8:00 p.m.
        file_check_mode (Union[Unset, int]): The original and the backup document can be compared before cleanup.
            Possible values (1 to 3)
             are defined in PurgeSettingsC.
        path_id (Union[Unset, int]): Possible path restriction for filing paths: <br>
            0: include all paths <br>
             1 and higher: only include a path with this ID where documents should be deleted
    """

    exclude_path_ids: Union[Unset, List[int]] = UNSET
    day_limit: Union[Unset, int] = UNSET
    start_hour: Union[Unset, int] = UNSET
    file_check_mode: Union[Unset, int] = UNSET
    path_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exclude_path_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.exclude_path_ids, Unset):
            exclude_path_ids = self.exclude_path_ids

        day_limit = self.day_limit

        start_hour = self.start_hour

        file_check_mode = self.file_check_mode

        path_id = self.path_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_path_ids is not UNSET:
            field_dict["excludePathIds"] = exclude_path_ids
        if day_limit is not UNSET:
            field_dict["dayLimit"] = day_limit
        if start_hour is not UNSET:
            field_dict["startHour"] = start_hour
        if file_check_mode is not UNSET:
            field_dict["fileCheckMode"] = file_check_mode
        if path_id is not UNSET:
            field_dict["pathId"] = path_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exclude_path_ids = cast(List[int], d.pop("excludePathIds", UNSET))

        day_limit = d.pop("dayLimit", UNSET)

        start_hour = d.pop("startHour", UNSET)

        file_check_mode = d.pop("fileCheckMode", UNSET)

        path_id = d.pop("pathId", UNSET)

        purge_settings = cls(
            exclude_path_ids=exclude_path_ids,
            day_limit=day_limit,
            start_hour=start_hour,
            file_check_mode=file_check_mode,
            path_id=path_id,
        )

        purge_settings.additional_properties = d
        return purge_settings

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
