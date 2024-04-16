from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="AclAccessInfo")


@_attrs_define
class AclAccessInfo:
    """This class contains the option for the methode getAclAccess

    Attributes:
        acl_items (Union[Unset, List['AclItem']]):
        obj_id (Union[Unset, str]):
        acl (Union[Unset, str]):
        parent_id (Union[Unset, str]): Parent's ID of the current object.
            (Useful to get the inherited ACLs of objects which haven't
             any ID yet, i.e. the ones being just added in archive.)
    """

    acl_items: Union[Unset, List["AclItem"]] = UNSET
    obj_id: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        obj_id = self.obj_id

        acl = self.acl

        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if acl is not UNSET:
            field_dict["acl"] = acl
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        obj_id = d.pop("objId", UNSET)

        acl = d.pop("acl", UNSET)

        parent_id = d.pop("parentId", UNSET)

        acl_access_info = cls(
            acl_items=acl_items,
            obj_id=obj_id,
            acl=acl,
            parent_id=parent_id,
        )

        acl_access_info.additional_properties = d
        return acl_access_info

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
