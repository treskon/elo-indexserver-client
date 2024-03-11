from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColorData")


@_attrs_define
class ColorData:
    """<p>
    Colours for marking entries in the archive.
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            rgb (Union[Unset, int]): RGB value.
            id (Union[Unset, int]): Colour number (ID).
            name (Union[Unset, str]): Colour name
            guid (Union[Unset, str]): GUID
            t_stamp (Union[Unset, str]): TStamp
            deleted (Union[Unset, bool]): Logically deleted.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            hidden (Union[Unset, bool]): This color should not be selectable in client applications.
                This color is reserved as marker for technical
                 purposes.
            package_name (Union[Unset, str]): Package name of ColorData
    """

    rgb: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rgb = self.rgb
        id = self.id
        name = self.name
        guid = self.guid
        t_stamp = self.t_stamp
        deleted = self.deleted
        t_stamp_sync = self.t_stamp_sync
        hidden = self.hidden
        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rgb is not UNSET:
            field_dict["RGB"] = rgb
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rgb = d.pop("RGB", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        deleted = d.pop("deleted", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        hidden = d.pop("hidden", UNSET)

        package_name = d.pop("packageName", UNSET)

        color_data = cls(
            rgb=rgb,
            id=id,
            name=name,
            guid=guid,
            t_stamp=t_stamp,
            deleted=deleted,
            t_stamp_sync=t_stamp_sync,
            hidden=hidden,
            package_name=package_name,
        )

        color_data.additional_properties = d
        return color_data

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
