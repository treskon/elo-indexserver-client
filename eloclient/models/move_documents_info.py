from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveDocumentsInfo")


@_attrs_define
class MoveDocumentsInfo:
    """Parameter class of the function
    {@link IXServicePortIF#moveDocuments(ClientInfo, MoveDocumentsInfo)}.

        Attributes:
            source_path_id (Union[Unset, str]): ID of the source storage path.
            end_date (Union[Unset, str]): End date.
            start_date (Union[Unset, str]): Start date.
            target_path_id (Union[Unset, str]): ID of the target storage path.
    """

    source_path_id: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    target_path_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_path_id = self.source_path_id

        end_date = self.end_date

        start_date = self.start_date

        target_path_id = self.target_path_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_path_id is not UNSET:
            field_dict["sourcePathId"] = source_path_id
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if target_path_id is not UNSET:
            field_dict["targetPathId"] = target_path_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_path_id = d.pop("sourcePathId", UNSET)

        end_date = d.pop("endDate", UNSET)

        start_date = d.pop("startDate", UNSET)

        target_path_id = d.pop("targetPathId", UNSET)

        move_documents_info = cls(
            source_path_id=source_path_id,
            end_date=end_date,
            start_date=start_date,
            target_path_id=target_path_id,
        )

        move_documents_info.additional_properties = d
        return move_documents_info

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
