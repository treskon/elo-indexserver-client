from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapDataC")


@_attrs_define
class MapDataC:
    """Constant class for MapData

    Attributes:
        ln_value (Union[Unset, int]): Maximum length of map item value.
        ln_blob (Union[Unset, int]): Maximum length of blob value.
            1048576 Bytes
        ln_key (Union[Unset, int]): Maximum length of map item key.
        ln_id (Union[Unset, int]): Maximum length of map id.
    """

    ln_value: Union[Unset, int] = UNSET
    ln_blob: Union[Unset, int] = UNSET
    ln_key: Union[Unset, int] = UNSET
    ln_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_value = self.ln_value

        ln_blob = self.ln_blob

        ln_key = self.ln_key

        ln_id = self.ln_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if ln_blob is not UNSET:
            field_dict["lnBlob"] = ln_blob
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_value = d.pop("lnValue", UNSET)

        ln_blob = d.pop("lnBlob", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        ln_id = d.pop("lnId", UNSET)

        map_data_c = cls(
            ln_value=ln_value,
            ln_blob=ln_blob,
            ln_key=ln_key,
            ln_id=ln_id,
        )

        map_data_c.additional_properties = d
        return map_data_c

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
