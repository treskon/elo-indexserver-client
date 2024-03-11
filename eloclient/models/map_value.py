from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="MapValue")


@_attrs_define
class MapValue:
    """This class represents map values.
    A map value is either a string, stored in member {@link KeyValue#value} of the
     super class. Or a map value is a BLOB available in {@link #blobValue}.

        Attributes:
            blob_value (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    blob_value: Union[Unset, "FileData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        blob_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.blob_value, Unset):
            blob_value = self.blob_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blob_value is not UNSET:
            field_dict["blobValue"] = blob_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        _blob_value = d.pop("blobValue", UNSET)
        blob_value: Union[Unset, FileData]
        if isinstance(_blob_value, Unset):
            blob_value = UNSET
        else:
            blob_value = FileData.from_dict(_blob_value)

        map_value = cls(
            blob_value=blob_value,
        )

        map_value.additional_properties = d
        return map_value

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
