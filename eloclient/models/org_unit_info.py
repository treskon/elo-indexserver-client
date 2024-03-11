from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgUnitInfo")


@_attrs_define
class OrgUnitInfo:
    """<p>
    Data class containing organizational unit information data. Information includes ID, name, etc.
     </p>
     <p>
     Copyright: Copyright (c) 2013
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            id (Union[Unset, int]): OU identifier
            name (Union[Unset, str]): OU name
            desc (Union[Unset, str]): OU description.
            ou_props (Union[Unset, List[str]]):
            t_stamp (Union[Unset, str]): Timestamp The format is JJJJ.MM.DD.hh.mm.
                ss
            guid (Union[Unset, str]): GUID
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    ou_props: Union[Unset, List[str]] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        desc = self.desc
        ou_props: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ou_props, Unset):
            ou_props = self.ou_props

        t_stamp = self.t_stamp
        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if desc is not UNSET:
            field_dict["desc"] = desc
        if ou_props is not UNSET:
            field_dict["ouProps"] = ou_props
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        desc = d.pop("desc", UNSET)

        ou_props = cast(List[str], d.pop("ouProps", UNSET))

        t_stamp = d.pop("tStamp", UNSET)

        guid = d.pop("guid", UNSET)

        org_unit_info = cls(
            id=id,
            name=name,
            desc=desc,
            ou_props=ou_props,
            t_stamp=t_stamp,
            guid=guid,
        )

        org_unit_info.additional_properties = d
        return org_unit_info

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
