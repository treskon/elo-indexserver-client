from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubsInfo")


@_attrs_define
class SubsInfo:
    """This class contains information about a user that is being deputized by another user.

    Attributes:
        inherit_rights (Union[Unset, bool]): The deputy inherits the rights of the user if this member is true.
        subs_id (Union[Unset, int]): Deputy: the user that deputizes <code>userId</code>.
        active (Union[Unset, bool]): The deputy relationship is applied if this member is true.
            If false, the deputy does not
             currently act as the user but may activate the relationship by themself.
        subs_name (Union[Unset, str]): Deputy name. If this member is set <code>subsId</code> is ignored.
        user_name (Union[Unset, str]): User name. If this member is set <code>userId</code> is ignored.
        user_id (Union[Unset, int]): The user that is being deputized by <code>subsId</code>
    """

    inherit_rights: Union[Unset, bool] = UNSET
    subs_id: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = UNSET
    subs_name: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inherit_rights = self.inherit_rights

        subs_id = self.subs_id

        active = self.active

        subs_name = self.subs_name

        user_name = self.user_name

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inherit_rights is not UNSET:
            field_dict["inheritRights"] = inherit_rights
        if subs_id is not UNSET:
            field_dict["subsId"] = subs_id
        if active is not UNSET:
            field_dict["active"] = active
        if subs_name is not UNSET:
            field_dict["subsName"] = subs_name
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inherit_rights = d.pop("inheritRights", UNSET)

        subs_id = d.pop("subsId", UNSET)

        active = d.pop("active", UNSET)

        subs_name = d.pop("subsName", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        subs_info = cls(
            inherit_rights=inherit_rights,
            subs_id=subs_id,
            active=active,
            subs_name=subs_name,
            user_name=user_name,
            user_id=user_id,
        )

        subs_info.additional_properties = d
        return subs_info

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
