from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessMoveDocumentsToStoragePath")


@_attrs_define
class ProcessMoveDocumentsToStoragePath:
    """This class specifies the options for moving a document into another storage path.
    It is used as
     member in <code>ProcessInfo</code> and is interpreted in the functions
     <code>processFindResult</code> and <code>processTrees</code>.

        Attributes:
            path_id (Union[Unset, str]): Name or ID of the storage path
    """

    path_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path_id = self.path_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_id is not UNSET:
            field_dict["pathId"] = path_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path_id = d.pop("pathId", UNSET)

        process_move_documents_to_storage_path = cls(
            path_id=path_id,
        )

        process_move_documents_to_storage_path.additional_properties = d
        return process_move_documents_to_storage_path

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
