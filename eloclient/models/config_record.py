from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="ConfigRecord")


@_attrs_define
class ConfigRecord:
    """Objects of this class represent entries for configurations related to packages.

    Attributes:
        component (Union[Unset, str]): ELO module name or ID.
        instance_id (Union[Unset, str]): Instance ID for workspace.
            For workspace entries, this value is assigned to the related
             {@link Sord#getGuid()}.
        level (Union[Unset, int]): Layer level. This value defines the priority for the entry.
        acl_items (Union[Unset, List['AclItem']]):
        group_id (Union[Unset, str]): Groups related entries.
        id (Union[Unset, str]): Row ID. This ID is unique over all entries.
        package_name (Union[Unset, str]): Package name or GUID.
        acl (Union[Unset, str]): Access control in raw representation.
        value (Union[Unset, str]): Entry value. This value can hold up to {@link ConfigRecordC#MAX_VALUE_LENGTH}
            characters.
        key (Union[Unset, str]): Entry key.
    """

    component: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    group_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        component = self.component

        instance_id = self.instance_id

        level = self.level

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for componentsschemas_list_of_acl_item_item_data in self.acl_items:
                componentsschemas_list_of_acl_item_item = componentsschemas_list_of_acl_item_item_data.to_dict()
                acl_items.append(componentsschemas_list_of_acl_item_item)

        group_id = self.group_id

        id = self.id

        package_name = self.package_name

        acl = self.acl

        value = self.value

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if level is not UNSET:
            field_dict["level"] = level
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if acl is not UNSET:
            field_dict["acl"] = acl
        if value is not UNSET:
            field_dict["value"] = value
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        component = d.pop("component", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        level = d.pop("level", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for componentsschemas_list_of_acl_item_item_data in _acl_items or []:
            componentsschemas_list_of_acl_item_item = AclItem.from_dict(componentsschemas_list_of_acl_item_item_data)

            acl_items.append(componentsschemas_list_of_acl_item_item)

        group_id = d.pop("groupId", UNSET)

        id = d.pop("id", UNSET)

        package_name = d.pop("packageName", UNSET)

        acl = d.pop("acl", UNSET)

        value = d.pop("value", UNSET)

        key = d.pop("key", UNSET)

        config_record = cls(
            component=component,
            instance_id=instance_id,
            level=level,
            acl_items=acl_items,
            group_id=group_id,
            id=id,
            package_name=package_name,
            acl=acl,
            value=value,
            key=key,
        )

        config_record.additional_properties = d
        return config_record

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
