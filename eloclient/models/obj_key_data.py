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
            udata (Union[Unset, str]): DB column: okeyudata
            data (Union[Unset, str]): DB column: okeydata
            obj_id (Union[Unset, int]): DB column: parentid
            name (Union[Unset, str]): DB column: okeyname
            id (Union[Unset, int]): DB column: okeyno
            odouble (Union[Unset, float]): DB column: odouble
            sdata (Union[Unset, str]): DB column: okeysdata
    """

    udata: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    odouble: Union[Unset, float] = UNSET
    sdata: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        udata = self.udata

        data = self.data

        obj_id = self.obj_id

        name = self.name

        id = self.id

        odouble = self.odouble

        sdata = self.sdata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if udata is not UNSET:
            field_dict["udata"] = udata
        if data is not UNSET:
            field_dict["data"] = data
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if odouble is not UNSET:
            field_dict["odouble"] = odouble
        if sdata is not UNSET:
            field_dict["sdata"] = sdata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        udata = d.pop("udata", UNSET)

        data = d.pop("data", UNSET)

        obj_id = d.pop("objId", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        odouble = d.pop("odouble", UNSET)

        sdata = d.pop("sdata", UNSET)

        obj_key_data = cls(
            udata=udata,
            data=data,
            obj_id=obj_id,
            name=name,
            id=id,
            odouble=odouble,
            sdata=sdata,
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
