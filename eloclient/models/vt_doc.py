from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VtDoc")


@_attrs_define
class VtDoc:
    """Internal class.

    Attributes:
        obj_id (Union[Unset, int]): DB column: objid
        doc_id (Union[Unset, int]): DB column: objdoc
        code (Union[Unset, int]): DB column: vtcode
    """

    obj_id: Union[Unset, int] = UNSET
    doc_id: Union[Unset, int] = UNSET
    code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        obj_id = self.obj_id
        doc_id = self.doc_id
        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        obj_id = d.pop("objId", UNSET)

        doc_id = d.pop("docId", UNSET)

        code = d.pop("code", UNSET)

        vt_doc = cls(
            obj_id=obj_id,
            doc_id=doc_id,
            code=code,
        )

        vt_doc.additional_properties = d
        return vt_doc

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
