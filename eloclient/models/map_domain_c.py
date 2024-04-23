from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapDomainC")


@_attrs_define
class MapDomainC:
    """This class defines constants for the predefined map tables.

    Attributes:
        domain_workflow_finished (Union[Unset, str]):
        domain_ft_options (Union[Unset, str]):
        domain_al_options (Union[Unset, str]): Smart Link configuration map domain name.
        domain_workflow_active (Union[Unset, str]):
        domain_sord (Union[Unset, str]):
        domain_dm_options (Union[Unset, str]):
        domain_eloxc (Union[Unset, str]): ELOxc configuration data.
        domain_ix_options (Union[Unset, str]):
        domain_am_options (Union[Unset, str]): Map domain name for reading AM options.
            EIX-2061
    """

    domain_workflow_finished: Union[Unset, str] = UNSET
    domain_ft_options: Union[Unset, str] = UNSET
    domain_al_options: Union[Unset, str] = UNSET
    domain_workflow_active: Union[Unset, str] = UNSET
    domain_sord: Union[Unset, str] = UNSET
    domain_dm_options: Union[Unset, str] = UNSET
    domain_eloxc: Union[Unset, str] = UNSET
    domain_ix_options: Union[Unset, str] = UNSET
    domain_am_options: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_workflow_finished = self.domain_workflow_finished

        domain_ft_options = self.domain_ft_options

        domain_al_options = self.domain_al_options

        domain_workflow_active = self.domain_workflow_active

        domain_sord = self.domain_sord

        domain_dm_options = self.domain_dm_options

        domain_eloxc = self.domain_eloxc

        domain_ix_options = self.domain_ix_options

        domain_am_options = self.domain_am_options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_workflow_finished is not UNSET:
            field_dict["DOMAIN_WORKFLOW_FINISHED"] = domain_workflow_finished
        if domain_ft_options is not UNSET:
            field_dict["DOMAIN_FT_OPTIONS"] = domain_ft_options
        if domain_al_options is not UNSET:
            field_dict["DOMAIN_AL_OPTIONS"] = domain_al_options
        if domain_workflow_active is not UNSET:
            field_dict["DOMAIN_WORKFLOW_ACTIVE"] = domain_workflow_active
        if domain_sord is not UNSET:
            field_dict["DOMAIN_SORD"] = domain_sord
        if domain_dm_options is not UNSET:
            field_dict["DOMAIN_DM_OPTIONS"] = domain_dm_options
        if domain_eloxc is not UNSET:
            field_dict["DOMAIN_ELOXC"] = domain_eloxc
        if domain_ix_options is not UNSET:
            field_dict["DOMAIN_IX_OPTIONS"] = domain_ix_options
        if domain_am_options is not UNSET:
            field_dict["DOMAIN_AM_OPTIONS"] = domain_am_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain_workflow_finished = d.pop("DOMAIN_WORKFLOW_FINISHED", UNSET)

        domain_ft_options = d.pop("DOMAIN_FT_OPTIONS", UNSET)

        domain_al_options = d.pop("DOMAIN_AL_OPTIONS", UNSET)

        domain_workflow_active = d.pop("DOMAIN_WORKFLOW_ACTIVE", UNSET)

        domain_sord = d.pop("DOMAIN_SORD", UNSET)

        domain_dm_options = d.pop("DOMAIN_DM_OPTIONS", UNSET)

        domain_eloxc = d.pop("DOMAIN_ELOXC", UNSET)

        domain_ix_options = d.pop("DOMAIN_IX_OPTIONS", UNSET)

        domain_am_options = d.pop("DOMAIN_AM_OPTIONS", UNSET)

        map_domain_c = cls(
            domain_workflow_finished=domain_workflow_finished,
            domain_ft_options=domain_ft_options,
            domain_al_options=domain_al_options,
            domain_workflow_active=domain_workflow_active,
            domain_sord=domain_sord,
            domain_dm_options=domain_dm_options,
            domain_eloxc=domain_eloxc,
            domain_ix_options=domain_ix_options,
            domain_am_options=domain_am_options,
        )

        map_domain_c.additional_properties = d
        return map_domain_c

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
