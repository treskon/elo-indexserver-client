from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveRightsResult")


@_attrs_define
class ResolveRightsResult:
    """Class for the result of the IX-Function
    {@link IXServicePortIF#resolveRights(ClientInfo, UserInfo, ResolveRightsInfo)} .

        Attributes:
            right (Union[Unset, int]): The right the user got by {@link ResolveRightsResult#type}. Values will be of {@link
                AccessC}.FLAG_*.
            right2 (Union[Unset, int]): The right the user got by {@link ResolveRightsResult#type}. Values will be of {@link
                AccessC}.FLAG2_*.
            type (Union[Unset, int]): The kind of way the user got this right. See {@link ResolveRightsResultC} for valid
                values.
            members (Union[Unset, List[str]]):
    """

    right: Union[Unset, int] = UNSET
    right2: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    members: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        right = self.right
        right2 = self.right2
        type = self.type
        members: Union[Unset, List[str]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if right is not UNSET:
            field_dict["right"] = right
        if right2 is not UNSET:
            field_dict["right2"] = right2
        if type is not UNSET:
            field_dict["type"] = type
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        right = d.pop("right", UNSET)

        right2 = d.pop("right2", UNSET)

        type = d.pop("type", UNSET)

        members = cast(List[str], d.pop("members", UNSET))

        resolve_rights_result = cls(
            right=right,
            right2=right2,
            type=type,
            members=members,
        )

        resolve_rights_result.additional_properties = d
        return resolve_rights_result

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
