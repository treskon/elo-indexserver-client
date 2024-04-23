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
            name_translation_key (Union[Unset, str]): Translation key.
                Optional identifier in the localization property files or translations stored
                 via {@link IXServicePortIF#checkinTranslateTerms(ClientInfo, TranslateTerm[], LockZ)}.
            t_stamp (Union[Unset, str]): TStamp
            deleted (Union[Unset, bool]): Logically deleted.
            hidden (Union[Unset, bool]): This color should not be selectable in client applications.
                This color is reserved as marker
                 for technical purposes.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            display_name (Union[Unset, str]): Localized name. This read-only value is the localized {@link
                #nameTranslationKey}.
                If
                 {@link #nameTranslationKey} is empty, this value is set to {@link #name}.
            name (Union[Unset, str]): Colour name
            guid (Union[Unset, str]): GUID
            id (Union[Unset, int]): Colour number (ID).
            package_name (Union[Unset, str]): Package name of ColorData
            rgb (Union[Unset, int]): RGB value.
    """

    name_translation_key: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    package_name: Union[Unset, str] = UNSET
    rgb: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name_translation_key = self.name_translation_key

        t_stamp = self.t_stamp

        deleted = self.deleted

        hidden = self.hidden

        t_stamp_sync = self.t_stamp_sync

        display_name = self.display_name

        name = self.name

        guid = self.guid

        id = self.id

        package_name = self.package_name

        rgb = self.rgb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if rgb is not UNSET:
            field_dict["RGB"] = rgb

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name_translation_key = d.pop("nameTranslationKey", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        deleted = d.pop("deleted", UNSET)

        hidden = d.pop("hidden", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        package_name = d.pop("packageName", UNSET)

        rgb = d.pop("RGB", UNSET)

        color_data = cls(
            name_translation_key=name_translation_key,
            t_stamp=t_stamp,
            deleted=deleted,
            hidden=hidden,
            t_stamp_sync=t_stamp_sync,
            display_name=display_name,
            name=name,
            guid=guid,
            id=id,
            package_name=package_name,
            rgb=rgb,
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
