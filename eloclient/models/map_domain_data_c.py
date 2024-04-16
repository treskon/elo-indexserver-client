from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapDomainDataC")


@_attrs_define
class MapDomainDataC:
    """<p>Bit constants for members of MapDomain</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_name (Union[Unset, int]): DB column: mapdname
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_name (Union[Unset, str]): DB column: mapdname
            mb_flags (Union[Unset, str]): DB column: mapdflags
    """

    ln_name: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_name = self.ln_name

        mb_all_members = self.mb_all_members

        mb_name = self.mb_name

        mb_flags = self.mb_flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_name = d.pop("lnName", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        map_domain_data_c = cls(
            ln_name=ln_name,
            mb_all_members=mb_all_members,
            mb_name=mb_name,
            mb_flags=mb_flags,
        )

        map_domain_data_c.additional_properties = d
        return map_domain_data_c

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
