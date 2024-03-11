from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hash_map_to_integer import HashMapToInteger
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="LicenseCounter")


@_attrs_define
class LicenseCounter:
    """License counters of a user.

    Attributes:
        java_client (Union[Unset, int]):
        winwos_client (Union[Unset, int]):
        full_user (Union[Unset, int]):
        ix_user (Union[Unset, int]):
        deleted_user (Union[Unset, int]):
        free_user (Union[Unset, int]):
        user_info (Union[Unset, UserInfo]): <p>
            Data class containing the user information data for the user logged in to the Index server. User information
            includes
             ID, name, rights, parent, etc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        access_map (Union[Unset, HashMapToInteger]):
        sum_access (Union[Unset, int]):
        disabled (Union[Unset, bool]): True, if the user has been inactive for 30 days.
        count_type (Union[Unset, int]):
    """

    java_client: Union[Unset, int] = UNSET
    winwos_client: Union[Unset, int] = UNSET
    full_user: Union[Unset, int] = UNSET
    ix_user: Union[Unset, int] = UNSET
    deleted_user: Union[Unset, int] = UNSET
    free_user: Union[Unset, int] = UNSET
    user_info: Union[Unset, "UserInfo"] = UNSET
    access_map: Union[Unset, "HashMapToInteger"] = UNSET
    sum_access: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    count_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        java_client = self.java_client
        winwos_client = self.winwos_client
        full_user = self.full_user
        ix_user = self.ix_user
        deleted_user = self.deleted_user
        free_user = self.free_user
        user_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        access_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_map, Unset):
            access_map = self.access_map.to_dict()

        sum_access = self.sum_access
        disabled = self.disabled
        count_type = self.count_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if java_client is not UNSET:
            field_dict["JAVA_CLIENT"] = java_client
        if winwos_client is not UNSET:
            field_dict["WINWOS_CLIENT"] = winwos_client
        if full_user is not UNSET:
            field_dict["FULL_USER"] = full_user
        if ix_user is not UNSET:
            field_dict["IX_USER"] = ix_user
        if deleted_user is not UNSET:
            field_dict["DELETED_USER"] = deleted_user
        if free_user is not UNSET:
            field_dict["FREE_USER"] = free_user
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info
        if access_map is not UNSET:
            field_dict["accessMap"] = access_map
        if sum_access is not UNSET:
            field_dict["sumAccess"] = sum_access
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if count_type is not UNSET:
            field_dict["countType"] = count_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hash_map_to_integer import HashMapToInteger
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        java_client = d.pop("JAVA_CLIENT", UNSET)

        winwos_client = d.pop("WINWOS_CLIENT", UNSET)

        full_user = d.pop("FULL_USER", UNSET)

        ix_user = d.pop("IX_USER", UNSET)

        deleted_user = d.pop("DELETED_USER", UNSET)

        free_user = d.pop("FREE_USER", UNSET)

        _user_info = d.pop("userInfo", UNSET)
        user_info: Union[Unset, UserInfo]
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = UserInfo.from_dict(_user_info)

        _access_map = d.pop("accessMap", UNSET)
        access_map: Union[Unset, HashMapToInteger]
        if isinstance(_access_map, Unset):
            access_map = UNSET
        else:
            access_map = HashMapToInteger.from_dict(_access_map)

        sum_access = d.pop("sumAccess", UNSET)

        disabled = d.pop("disabled", UNSET)

        count_type = d.pop("countType", UNSET)

        license_counter = cls(
            java_client=java_client,
            winwos_client=winwos_client,
            full_user=full_user,
            ix_user=ix_user,
            deleted_user=deleted_user,
            free_user=free_user,
            user_info=user_info,
            access_map=access_map,
            sum_access=sum_access,
            disabled=disabled,
            count_type=count_type,
        )

        license_counter.additional_properties = d
        return license_counter

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
