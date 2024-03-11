from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjKeyData")


@_attrs_define
class ObjKeyData:
    """<p>
    Internal use.
     </p>

        Attributes:
            obj_id (Union[Unset, int]): DB column: parentid
            id (Union[Unset, int]): DB column: okeyno
            name (Union[Unset, str]): DB column: okeyname
            data (Union[Unset, str]): DB column: okeydata
            udata (Union[Unset, str]): DB column: okeyudata
            sdata (Union[Unset, str]): DB column: okeysdata
            odouble (Union[Unset, float]): DB column: odouble
    """

    obj_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    udata: Union[Unset, str] = UNSET
    sdata: Union[Unset, str] = UNSET
    odouble: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        obj_id = self.obj_id
        id = self.id
        name = self.name
        data = self.data
        udata = self.udata
        sdata = self.sdata
        odouble = self.odouble

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data
        if udata is not UNSET:
            field_dict["udata"] = udata
        if sdata is not UNSET:
            field_dict["sdata"] = sdata
        if odouble is not UNSET:
            field_dict["odouble"] = odouble

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        obj_id = d.pop("objId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        data = d.pop("data", UNSET)

        udata = d.pop("udata", UNSET)

        sdata = d.pop("sdata", UNSET)

        odouble = d.pop("odouble", UNSET)

        obj_key_data = cls(
            obj_id=obj_id,
            id=id,
            name=name,
            data=data,
            udata=udata,
            sdata=sdata,
            odouble=odouble,
        )

        obj_key_data.additional_properties = d
        return obj_key_data

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
