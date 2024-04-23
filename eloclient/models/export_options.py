from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.master_data_e import MasterDataE


T = TypeVar("T", bound="ExportOptions")


@_attrs_define
class ExportOptions:
    """Options to import/export archive data for the replication.

    Attributes:
        time_stamp_start (Union[Unset, str]): This value applies to exports only.
            Objects modified before this timestamp will not be
             processed.
        include_master_data (Union[Unset, List['MasterDataE']]):
        package_guids (Union[Unset, List[str]]):
        time_stamp_end (Union[Unset, str]): This value applies to exports only.
            Objects modified after this timestamp will not be
             processed.
        compression_level (Union[Unset, int]): Enables compression mode. -1=no compression, 0/1=low compression,
            9=strong compression.
    """

    time_stamp_start: Union[Unset, str] = UNSET
    include_master_data: Union[Unset, List["MasterDataE"]] = UNSET
    package_guids: Union[Unset, List[str]] = UNSET
    time_stamp_end: Union[Unset, str] = UNSET
    compression_level: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_stamp_start = self.time_stamp_start

        include_master_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.include_master_data, Unset):
            include_master_data = []
            for componentsschemas_set_of_master_data_e_item_data in self.include_master_data:
                componentsschemas_set_of_master_data_e_item = componentsschemas_set_of_master_data_e_item_data.to_dict()
                include_master_data.append(componentsschemas_set_of_master_data_e_item)

        package_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.package_guids, Unset):
            package_guids = self.package_guids

        time_stamp_end = self.time_stamp_end

        compression_level = self.compression_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_stamp_start is not UNSET:
            field_dict["timeStampStart"] = time_stamp_start
        if include_master_data is not UNSET:
            field_dict["includeMasterData"] = include_master_data
        if package_guids is not UNSET:
            field_dict["packageGuids"] = package_guids
        if time_stamp_end is not UNSET:
            field_dict["timeStampEnd"] = time_stamp_end
        if compression_level is not UNSET:
            field_dict["compressionLevel"] = compression_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.master_data_e import MasterDataE

        d = src_dict.copy()
        time_stamp_start = d.pop("timeStampStart", UNSET)

        include_master_data = []
        _include_master_data = d.pop("includeMasterData", UNSET)
        for componentsschemas_set_of_master_data_e_item_data in _include_master_data or []:
            componentsschemas_set_of_master_data_e_item = MasterDataE.from_dict(
                componentsschemas_set_of_master_data_e_item_data
            )

            include_master_data.append(componentsschemas_set_of_master_data_e_item)

        package_guids = cast(List[str], d.pop("packageGuids", UNSET))

        time_stamp_end = d.pop("timeStampEnd", UNSET)

        compression_level = d.pop("compressionLevel", UNSET)

        export_options = cls(
            time_stamp_start=time_stamp_start,
            include_master_data=include_master_data,
            package_guids=package_guids,
            time_stamp_end=time_stamp_end,
            compression_level=compression_level,
        )

        export_options.additional_properties = d
        return export_options

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
