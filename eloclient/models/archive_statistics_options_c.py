from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveStatisticsOptionsC")


@_attrs_define
class ArchiveStatisticsOptionsC:
    """An object of this class controls the function getArchiveStatistics.

    Attributes:
        mb_max_doc_id (Union[Unset, str]): Find the maximum document (version) ID
        mb_max_obj_id (Union[Unset, str]): Find the maximum object ID
    """

    mb_max_doc_id: Union[Unset, str] = UNSET
    mb_max_obj_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_max_doc_id = self.mb_max_doc_id

        mb_max_obj_id = self.mb_max_obj_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_max_doc_id is not UNSET:
            field_dict["mbMaxDocId"] = mb_max_doc_id
        if mb_max_obj_id is not UNSET:
            field_dict["mbMaxObjId"] = mb_max_obj_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_max_doc_id = d.pop("mbMaxDocId", UNSET)

        mb_max_obj_id = d.pop("mbMaxObjId", UNSET)

        archive_statistics_options_c = cls(
            mb_max_doc_id=mb_max_doc_id,
            mb_max_obj_id=mb_max_obj_id,
        )

        archive_statistics_options_c.additional_properties = d
        return archive_statistics_options_c

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
