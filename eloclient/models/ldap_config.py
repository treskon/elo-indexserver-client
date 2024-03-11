from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain import Domain


T = TypeVar("T", bound="LdapConfig")


@_attrs_define
class LdapConfig:
    """Configuration data for LDAP plugin.

    Attributes:
        read_auto_config (Union[Unset, LdapConfig]): Configuration data for LDAP plugin.
        read_config (Union[Unset, LdapConfig]): Configuration data for LDAP plugin.
        name (Union[Unset, str]): Configuration name. Optional configuration name.
        create_new_user (Union[Unset, bool]): If authentication succeeds, create a new ELO user if she does not already
            exist.
        assign_groups (Union[Unset, bool]): If authentication succeeds, update the user's memberships in ELO groups.
        not_responsible_for_user_or_group_ids (Union[Unset, List[str]]):
        domains (Union[Unset, List['Domain']]):
        enabled (Union[Unset, bool]): Enable/disable authentication via LDAP.
    """

    read_auto_config: Union[Unset, "LdapConfig"] = UNSET
    read_config: Union[Unset, "LdapConfig"] = UNSET
    name: Union[Unset, str] = UNSET
    create_new_user: Union[Unset, bool] = UNSET
    assign_groups: Union[Unset, bool] = UNSET
    not_responsible_for_user_or_group_ids: Union[Unset, List[str]] = UNSET
    domains: Union[Unset, List["Domain"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        read_auto_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.read_auto_config, Unset):
            read_auto_config = self.read_auto_config.to_dict()

        read_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.read_config, Unset):
            read_config = self.read_config.to_dict()

        name = self.name
        create_new_user = self.create_new_user
        assign_groups = self.assign_groups
        not_responsible_for_user_or_group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.not_responsible_for_user_or_group_ids, Unset):
            not_responsible_for_user_or_group_ids = self.not_responsible_for_user_or_group_ids

        domains: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for componentsschemas_list_of_domain_item_data in self.domains:
                componentsschemas_list_of_domain_item = componentsschemas_list_of_domain_item_data.to_dict()

                domains.append(componentsschemas_list_of_domain_item)

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_auto_config is not UNSET:
            field_dict["READ_AUTO_CONFIG"] = read_auto_config
        if read_config is not UNSET:
            field_dict["READ_CONFIG"] = read_config
        if name is not UNSET:
            field_dict["name"] = name
        if create_new_user is not UNSET:
            field_dict["createNewUser"] = create_new_user
        if assign_groups is not UNSET:
            field_dict["assignGroups"] = assign_groups
        if not_responsible_for_user_or_group_ids is not UNSET:
            field_dict["notResponsibleForUserOrGroupIds"] = not_responsible_for_user_or_group_ids
        if domains is not UNSET:
            field_dict["domains"] = domains
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain import Domain

        d = src_dict.copy()
        _read_auto_config = d.pop("READ_AUTO_CONFIG", UNSET)
        read_auto_config: Union[Unset, LdapConfig]
        if isinstance(_read_auto_config, Unset):
            read_auto_config = UNSET
        else:
            read_auto_config = LdapConfig.from_dict(_read_auto_config)

        _read_config = d.pop("READ_CONFIG", UNSET)
        read_config: Union[Unset, LdapConfig]
        if isinstance(_read_config, Unset):
            read_config = UNSET
        else:
            read_config = LdapConfig.from_dict(_read_config)

        name = d.pop("name", UNSET)

        create_new_user = d.pop("createNewUser", UNSET)

        assign_groups = d.pop("assignGroups", UNSET)

        not_responsible_for_user_or_group_ids = cast(List[str], d.pop("notResponsibleForUserOrGroupIds", UNSET))

        domains = []
        _domains = d.pop("domains", UNSET)
        for componentsschemas_list_of_domain_item_data in _domains or []:
            componentsschemas_list_of_domain_item = Domain.from_dict(componentsschemas_list_of_domain_item_data)

            domains.append(componentsschemas_list_of_domain_item)

        enabled = d.pop("enabled", UNSET)

        ldap_config = cls(
            read_auto_config=read_auto_config,
            read_config=read_config,
            name=name,
            create_new_user=create_new_user,
            assign_groups=assign_groups,
            not_responsible_for_user_or_group_ids=not_responsible_for_user_or_group_ids,
            domains=domains,
            enabled=enabled,
        )

        ldap_config.additional_properties = d
        return ldap_config

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
