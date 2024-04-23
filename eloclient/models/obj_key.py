from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjKey")


@_attrs_define
class ObjKey:
    """This class wraps the ObjKeyData class to provide a convenient way to access the index lines that
    have multiple columns. Unlike ObjKeyData the getData and setData functions work with String
     arrays inspite of single String objects.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            data (Union[Unset, List[str]]):
            name (Union[Unset, str]): The group name of the index line
            obj_id (Union[Unset, int]): The ELO object ID this object belongs to
            display_data (Union[Unset, List[str]]):
            id (Union[Unset, int]): ID of the index line
    """

    data: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    display_data: Union[Unset, List[str]] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        name = self.name

        obj_id = self.obj_id

        display_data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.display_data, Unset):
            display_data = self.display_data

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if name is not UNSET:
            field_dict["name"] = name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if display_data is not UNSET:
            field_dict["displayData"] = display_data
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = cast(List[str], d.pop("data", UNSET))

        name = d.pop("name", UNSET)

        obj_id = d.pop("objId", UNSET)

        display_data = cast(List[str], d.pop("displayData", UNSET))

        id = d.pop("id", UNSET)

        obj_key = cls(
            data=data,
            name=name,
            obj_id=obj_id,
            display_data=display_data,
            id=id,
        )

        obj_key.additional_properties = d
        return obj_key

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
