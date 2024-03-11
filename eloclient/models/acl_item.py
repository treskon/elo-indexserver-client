from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name import IdName


T = TypeVar("T", bound="AclItem")


@_attrs_define
class AclItem:
    """<p>
    Human readable ACL entry.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            access (Union[Unset, int]): Access mode. Bitset of LUR_*.
            id (Union[Unset, int]): ID of user, group, key.
            name (Union[Unset, str]): Name of user, group, key.
            type (Union[Unset, int]): Item type: user, group, key, ...
            and_groups (Union[Unset, List['IdName']]):
    """

    access: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    and_groups: Union[Unset, List["IdName"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access
        id = self.id
        name = self.name
        type = self.type
        and_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.and_groups, Unset):
            and_groups = []
            for and_groups_item_data in self.and_groups:
                and_groups_item = and_groups_item_data.to_dict()

                and_groups.append(and_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if and_groups is not UNSET:
            field_dict["andGroups"] = and_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.id_name import IdName

        d = src_dict.copy()
        access = d.pop("access", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        and_groups = []
        _and_groups = d.pop("andGroups", UNSET)
        for and_groups_item_data in _and_groups or []:
            and_groups_item = IdName.from_dict(and_groups_item_data)

            and_groups.append(and_groups_item)

        acl_item = cls(
            access=access,
            id=id,
            name=name,
            type=type,
            and_groups=and_groups,
        )

        acl_item.additional_properties = d
        return acl_item

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
