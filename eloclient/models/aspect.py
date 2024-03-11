from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_aspect_line import MapToAspectLine


T = TypeVar("T", bound="Aspect")


@_attrs_define
class Aspect:
    """This class defines a keywording aspect.

    Attributes:
        id (Union[Unset, int]): Aspect ID. For a new aspect, this value is -1. This value cannot be changed for an
            existing aspect.
        name (Union[Unset, str]): Aspect name.
            <br>
             This must be a String of alpha-numeric characters between 'A' and 'Z', 'a' and 'z', '0' and '9'.<br>
             Additionally, it can contain the underscore '_' and the dot '.'.<br>
             Underscore and dot are not allowed for the first character of the name.
        lock_id (Union[Unset, int]): User ID that holds a lock on this object. If -1, the object is unlocked.
        lock_name (Union[Unset, str]): Name of the user that has locked the aspect. Read-only, ignored in checkinAspect.
        display_name (Union[Unset, str]): Locale specific name. Readonly. This value is the resolved {@link
            #translationKey}.
        translation_key (Union[Unset, str]): Translation key. Defines the {@link #displayName} as technical resource ID.
        lines (Union[Unset, MapToAspectLine]):
        guid (Union[Unset, str]): Aspect GUID.
        t_stamp (Union[Unset, str]): Timestamp of last modification.
        deleted (Union[Unset, bool]): Deleted status.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        package_name (Union[Unset, str]): Package name of Aspect.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    lock_id: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    translation_key: Union[Unset, str] = UNSET
    lines: Union[Unset, "MapToAspectLine"] = UNSET
    guid: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        lock_id = self.lock_id
        lock_name = self.lock_name
        display_name = self.display_name
        translation_key = self.translation_key
        lines: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines.to_dict()

        guid = self.guid
        t_stamp = self.t_stamp
        deleted = self.deleted
        t_stamp_sync = self.t_stamp_sync
        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if lines is not UNSET:
            field_dict["lines"] = lines
        if guid is not UNSET:
            field_dict["guid"] = guid
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_aspect_line import MapToAspectLine

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        lock_id = d.pop("lockId", UNSET)

        lock_name = d.pop("lockName", UNSET)

        display_name = d.pop("displayName", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        _lines = d.pop("lines", UNSET)
        lines: Union[Unset, MapToAspectLine]
        if isinstance(_lines, Unset):
            lines = UNSET
        else:
            lines = MapToAspectLine.from_dict(_lines)

        guid = d.pop("guid", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        deleted = d.pop("deleted", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        package_name = d.pop("packageName", UNSET)

        aspect = cls(
            id=id,
            name=name,
            lock_id=lock_id,
            lock_name=lock_name,
            display_name=display_name,
            translation_key=translation_key,
            lines=lines,
            guid=guid,
            t_stamp=t_stamp,
            deleted=deleted,
            t_stamp_sync=t_stamp_sync,
            package_name=package_name,
        )

        aspect.additional_properties = d
        return aspect

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
