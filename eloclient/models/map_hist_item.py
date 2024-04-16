from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="MapHistItem")


@_attrs_define
class MapHistItem:
    """This class provides the version information for a map attribute that has been modified.

    Attributes:
        hist_guid (Union[Unset, str]): GUID of the assigned SordHist object.
        value (Union[Unset, str]): Map value. An empty value means, that the map item has been deleted.
        blob_value (Union[Unset, FileData]): Class for the data contained in a file.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        key (Union[Unset, str]): Map key.
    """

    hist_guid: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    blob_value: Union[Unset, "FileData"] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hist_guid = self.hist_guid

        value = self.value

        blob_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.blob_value, Unset):
            blob_value = self.blob_value.to_dict()

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hist_guid is not UNSET:
            field_dict["histGuid"] = hist_guid
        if value is not UNSET:
            field_dict["value"] = value
        if blob_value is not UNSET:
            field_dict["blobValue"] = blob_value
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        hist_guid = d.pop("histGuid", UNSET)

        value = d.pop("value", UNSET)

        _blob_value = d.pop("blobValue", UNSET)
        blob_value: Union[Unset, FileData]
        if isinstance(_blob_value, Unset):
            blob_value = UNSET
        else:
            blob_value = FileData.from_dict(_blob_value)

        key = d.pop("key", UNSET)

        map_hist_item = cls(
            hist_guid=hist_guid,
            value=value,
            blob_value=blob_value,
            key=key,
        )

        map_hist_item.additional_properties = d
        return map_hist_item

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
