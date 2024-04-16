from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgUnitInfoC")


@_attrs_define
class OrgUnitInfoC:
    """<p>
    Constants related to organizational unit information.
     </p>
     <p>
     Copyright: Copyright (c) 2013
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            max_org_units (Union[Unset, int]): Maximum number of OUs.
            ln_name (Union[Unset, int]): Maximum OU name length
            mb_id (Union[Unset, str]): Member bit {@link OrgUnitInfo#id}
            mb_desc (Union[Unset, str]): Member bit {@link OrgUnitInfo#desc}
            mb_ou_props (Union[Unset, str]): Member bit {@link OrgUnitInfo#ouProps}
            mb_t_stamp (Union[Unset, str]): Member bit {@link OrgUnitInfo#tStamp}
            ln_ou_prop (Union[Unset, int]): Maximum OU property length
            mb_guid (Union[Unset, str]): Member bit {@link OrgUnitInfo#guid}
            ln_desc (Union[Unset, int]): Maximum OU desc length
            mb_name (Union[Unset, str]): Member bit {@link OrgUnitInfo#name}
            max_ou_prop (Union[Unset, int]): Maximum number of OU properties.
    """

    max_org_units: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_desc: Union[Unset, str] = UNSET
    mb_ou_props: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_ou_prop: Union[Unset, int] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_desc: Union[Unset, int] = UNSET
    mb_name: Union[Unset, str] = UNSET
    max_ou_prop: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_org_units = self.max_org_units

        ln_name = self.ln_name

        mb_id = self.mb_id

        mb_desc = self.mb_desc

        mb_ou_props = self.mb_ou_props

        mb_t_stamp = self.mb_t_stamp

        ln_ou_prop = self.ln_ou_prop

        mb_guid = self.mb_guid

        ln_desc = self.ln_desc

        mb_name = self.mb_name

        max_ou_prop = self.max_ou_prop

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_org_units is not UNSET:
            field_dict["MAX_ORG_UNITS"] = max_org_units
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_desc is not UNSET:
            field_dict["mbDesc"] = mb_desc
        if mb_ou_props is not UNSET:
            field_dict["mbOuProps"] = mb_ou_props
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_ou_prop is not UNSET:
            field_dict["lnOuProp"] = ln_ou_prop
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_desc is not UNSET:
            field_dict["lnDesc"] = ln_desc
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if max_ou_prop is not UNSET:
            field_dict["MAX_OU_PROP"] = max_ou_prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_org_units = d.pop("MAX_ORG_UNITS", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_desc = d.pop("mbDesc", UNSET)

        mb_ou_props = d.pop("mbOuProps", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_ou_prop = d.pop("lnOuProp", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_desc = d.pop("lnDesc", UNSET)

        mb_name = d.pop("mbName", UNSET)

        max_ou_prop = d.pop("MAX_OU_PROP", UNSET)

        org_unit_info_c = cls(
            max_org_units=max_org_units,
            ln_name=ln_name,
            mb_id=mb_id,
            mb_desc=mb_desc,
            mb_ou_props=mb_ou_props,
            mb_t_stamp=mb_t_stamp,
            ln_ou_prop=ln_ou_prop,
            mb_guid=mb_guid,
            ln_desc=ln_desc,
            mb_name=mb_name,
            max_ou_prop=max_ou_prop,
        )

        org_unit_info_c.additional_properties = d
        return org_unit_info_c

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
