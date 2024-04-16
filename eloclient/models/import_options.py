from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.b_stream_reference import BStreamReference
    from ..models.conflict_handling_e import ConflictHandlingE


T = TypeVar("T", bound="ImportOptions")


@_attrs_define
class ImportOptions:
    """Internal class.

    Attributes:
        upload_stream (Union[Unset, BStreamReference]):
        packages_imported (Union[Unset, bool]): Import packages.
        conflict_handling (Union[Unset, ConflictHandlingE]): FIXME: add javadoc
    """

    upload_stream: Union[Unset, "BStreamReference"] = UNSET
    packages_imported: Union[Unset, bool] = UNSET
    conflict_handling: Union[Unset, "ConflictHandlingE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.upload_stream, Unset):
            upload_stream = self.upload_stream.to_dict()

        packages_imported = self.packages_imported

        conflict_handling: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conflict_handling, Unset):
            conflict_handling = self.conflict_handling.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_stream is not UNSET:
            field_dict["uploadStream"] = upload_stream
        if packages_imported is not UNSET:
            field_dict["packagesImported"] = packages_imported
        if conflict_handling is not UNSET:
            field_dict["conflictHandling"] = conflict_handling

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.b_stream_reference import BStreamReference
        from ..models.conflict_handling_e import ConflictHandlingE

        d = src_dict.copy()
        _upload_stream = d.pop("uploadStream", UNSET)
        upload_stream: Union[Unset, BStreamReference]
        if isinstance(_upload_stream, Unset):
            upload_stream = UNSET
        else:
            upload_stream = BStreamReference.from_dict(_upload_stream)

        packages_imported = d.pop("packagesImported", UNSET)

        _conflict_handling = d.pop("conflictHandling", UNSET)
        conflict_handling: Union[Unset, ConflictHandlingE]
        if isinstance(_conflict_handling, Unset):
            conflict_handling = UNSET
        else:
            conflict_handling = ConflictHandlingE.from_dict(_conflict_handling)

        import_options = cls(
            upload_stream=upload_stream,
            packages_imported=packages_imported,
            conflict_handling=conflict_handling,
        )

        import_options.additional_properties = d
        return import_options

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
