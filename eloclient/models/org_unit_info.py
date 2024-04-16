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
            t_stamp (Union[Unset, str]): Timestamp The format is JJJJ.MM.DD.hh.mm.
                ss
            name (Union[Unset, str]): OU name
            guid (Union[Unset, str]): GUID
            id (Union[Unset, int]): OU identifier
            ou_props (Union[Unset, List[str]]):
            desc (Union[Unset, str]): OU description.
    """

    t_stamp: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    ou_props: Union[Unset, List[str]] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp

        name = self.name

        guid = self.guid

        id = self.id

        ou_props: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ou_props, Unset):
            ou_props = self.ou_props

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if ou_props is not UNSET:
            field_dict["ouProps"] = ou_props
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t_stamp = d.pop("tStamp", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        ou_props = cast(List[str], d.pop("ouProps", UNSET))

        desc = d.pop("desc", UNSET)

        org_unit_info = cls(
            t_stamp=t_stamp,
            name=name,
            guid=guid,
            id=id,
            ou_props=ou_props,
            desc=desc,
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
