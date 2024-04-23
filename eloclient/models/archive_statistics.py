from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveStatistics")


@_attrs_define
class ArchiveStatistics:
    """Characteristic properties of the archive.

    Attributes:
        max_obj_id (Union[Unset, int]): Last object ID.
        max_doc_id (Union[Unset, int]): Last document (version) ID.
    """

    max_obj_id: Union[Unset, int] = UNSET
    max_doc_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_obj_id = self.max_obj_id

        max_doc_id = self.max_doc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_obj_id is not UNSET:
            field_dict["maxObjId"] = max_obj_id
        if max_doc_id is not UNSET:
            field_dict["maxDocId"] = max_doc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_obj_id = d.pop("maxObjId", UNSET)

        max_doc_id = d.pop("maxDocId", UNSET)

        archive_statistics = cls(
            max_obj_id=max_obj_id,
            max_doc_id=max_doc_id,
        )

        archive_statistics.additional_properties = d
        return archive_statistics

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
