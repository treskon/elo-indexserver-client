from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="ProcessAcl")


@_attrs_define
class ProcessAcl:
    """This class is used to assign or remove ACLs to an object.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            and_acl_items (Union[Unset, List['AclItem']]):
            sub_acl (Union[Unset, str]): ACL to be added in raw database format. Ignored, if subAclItems is not null.
            and_acl (Union[Unset, str]): ACL to be added in raw database format. Ignored, if andAclItems is not null.
            add_acl_items (Union[Unset, List['AclItem']]):
            set_acl (Union[Unset, str]): ACL to be added in raw database format. Ignored, if setAclItems is not null.
            set_acl_items (Union[Unset, List['AclItem']]):
            add_acl (Union[Unset, str]): ACL to be added in raw database format. Ignored, if addAclItems is not null.
            sub_acl_items (Union[Unset, List['AclItem']]):
    """

    and_acl_items: Union[Unset, List["AclItem"]] = UNSET
    sub_acl: Union[Unset, str] = UNSET
    and_acl: Union[Unset, str] = UNSET
    add_acl_items: Union[Unset, List["AclItem"]] = UNSET
    set_acl: Union[Unset, str] = UNSET
    set_acl_items: Union[Unset, List["AclItem"]] = UNSET
    add_acl: Union[Unset, str] = UNSET
    sub_acl_items: Union[Unset, List["AclItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        and_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.and_acl_items, Unset):
            and_acl_items = []
            for and_acl_items_item_data in self.and_acl_items:
                and_acl_items_item = and_acl_items_item_data.to_dict()
                and_acl_items.append(and_acl_items_item)

        sub_acl = self.sub_acl

        and_acl = self.and_acl

        add_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_acl_items, Unset):
            add_acl_items = []
            for add_acl_items_item_data in self.add_acl_items:
                add_acl_items_item = add_acl_items_item_data.to_dict()
                add_acl_items.append(add_acl_items_item)

        set_acl = self.set_acl

        set_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.set_acl_items, Unset):
            set_acl_items = []
            for set_acl_items_item_data in self.set_acl_items:
                set_acl_items_item = set_acl_items_item_data.to_dict()
                set_acl_items.append(set_acl_items_item)

        add_acl = self.add_acl

        sub_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_acl_items, Unset):
            sub_acl_items = []
            for sub_acl_items_item_data in self.sub_acl_items:
                sub_acl_items_item = sub_acl_items_item_data.to_dict()
                sub_acl_items.append(sub_acl_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if and_acl_items is not UNSET:
            field_dict["andAclItems"] = and_acl_items
        if sub_acl is not UNSET:
            field_dict["subAcl"] = sub_acl
        if and_acl is not UNSET:
            field_dict["andAcl"] = and_acl
        if add_acl_items is not UNSET:
            field_dict["addAclItems"] = add_acl_items
        if set_acl is not UNSET:
            field_dict["setAcl"] = set_acl
        if set_acl_items is not UNSET:
            field_dict["setAclItems"] = set_acl_items
        if add_acl is not UNSET:
            field_dict["addAcl"] = add_acl
        if sub_acl_items is not UNSET:
            field_dict["subAclItems"] = sub_acl_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        and_acl_items = []
        _and_acl_items = d.pop("andAclItems", UNSET)
        for and_acl_items_item_data in _and_acl_items or []:
            and_acl_items_item = AclItem.from_dict(and_acl_items_item_data)

            and_acl_items.append(and_acl_items_item)

        sub_acl = d.pop("subAcl", UNSET)

        and_acl = d.pop("andAcl", UNSET)

        add_acl_items = []
        _add_acl_items = d.pop("addAclItems", UNSET)
        for add_acl_items_item_data in _add_acl_items or []:
            add_acl_items_item = AclItem.from_dict(add_acl_items_item_data)

            add_acl_items.append(add_acl_items_item)

        set_acl = d.pop("setAcl", UNSET)

        set_acl_items = []
        _set_acl_items = d.pop("setAclItems", UNSET)
        for set_acl_items_item_data in _set_acl_items or []:
            set_acl_items_item = AclItem.from_dict(set_acl_items_item_data)

            set_acl_items.append(set_acl_items_item)

        add_acl = d.pop("addAcl", UNSET)

        sub_acl_items = []
        _sub_acl_items = d.pop("subAclItems", UNSET)
        for sub_acl_items_item_data in _sub_acl_items or []:
            sub_acl_items_item = AclItem.from_dict(sub_acl_items_item_data)

            sub_acl_items.append(sub_acl_items_item)

        process_acl = cls(
            and_acl_items=and_acl_items,
            sub_acl=sub_acl,
            and_acl=and_acl,
            add_acl_items=add_acl_items,
            set_acl=set_acl,
            set_acl_items=set_acl_items,
            add_acl=add_acl,
            sub_acl_items=sub_acl_items,
        )

        process_acl.additional_properties = d
        return process_acl

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
