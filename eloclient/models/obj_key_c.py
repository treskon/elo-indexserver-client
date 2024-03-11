from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjKeyC")


@_attrs_define
class ObjKeyC:
    """<p>
    Constants for the ObjKey class.
     </p>

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            dummy_key_id (Union[Unset, int]): This ID marks an ObjKey as Dummy.
    """

    dummy_key_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dummy_key_id = self.dummy_key_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dummy_key_id is not UNSET:
            field_dict["DUMMY_KEY_ID"] = dummy_key_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dummy_key_id = d.pop("DUMMY_KEY_ID", UNSET)

        obj_key_c = cls(
            dummy_key_id=dummy_key_id,
        )

        obj_key_c.additional_properties = d
        return obj_key_c

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
