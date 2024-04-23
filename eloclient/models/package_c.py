from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_data_z import PackageDataZ


T = TypeVar("T", bound="PackageC")


@_attrs_define
class PackageC:
    """Constants for the class PackageDataC

    Attributes:
        mb_all (Union[Unset, PackageDataZ]): Type safe element selector for class PackageData.
        default_guid (Union[Unset, str]): Package default guid.
        mb_only_lock (Union[Unset, PackageDataZ]): Type safe element selector for class PackageData.
        mb_all_members (Union[Unset, str]): All valid member bits.
        mb_levels (Union[Unset, str]): Package level members.
    """

    mb_all: Union[Unset, "PackageDataZ"] = UNSET
    default_guid: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "PackageDataZ"] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_levels: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        default_guid = self.default_guid

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_all_members = self.mb_all_members

        mb_levels = self.mb_levels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if default_guid is not UNSET:
            field_dict["defaultGuid"] = default_guid
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_levels is not UNSET:
            field_dict["mbLevels"] = mb_levels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_data_z import PackageDataZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, PackageDataZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = PackageDataZ.from_dict(_mb_all)

        default_guid = d.pop("defaultGuid", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, PackageDataZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = PackageDataZ.from_dict(_mb_only_lock)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_levels = d.pop("mbLevels", UNSET)

        package_c = cls(
            mb_all=mb_all,
            default_guid=default_guid,
            mb_only_lock=mb_only_lock,
            mb_all_members=mb_all_members,
            mb_levels=mb_levels,
        )

        package_c.additional_properties = d
        return package_c

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
