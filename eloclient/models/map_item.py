from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.b_stream_reference import BStreamReference


T = TypeVar("T", bound="MapItem")


@_attrs_define
class MapItem:
    """Internal class.

    Attributes:
        id (Union[Unset, str]): Map id.
        key (Union[Unset, str]): Map key.
        value (Union[Unset, str]): Map value.
        content_type (Union[Unset, str]): Content Type.
        blob_data (Union[Unset, BStreamReference]):
    """

    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    blob_data: Union[Unset, "BStreamReference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        value = self.value
        content_type = self.content_type
        blob_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.blob_data, Unset):
            blob_data = self.blob_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if blob_data is not UNSET:
            field_dict["blobData"] = blob_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.b_stream_reference import BStreamReference

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        content_type = d.pop("contentType", UNSET)

        _blob_data = d.pop("blobData", UNSET)
        blob_data: Union[Unset, BStreamReference]
        if isinstance(_blob_data, Unset):
            blob_data = UNSET
        else:
            blob_data = BStreamReference.from_dict(_blob_data)

        map_item = cls(
            id=id,
            key=key,
            value=value,
            content_type=content_type,
            blob_data=blob_data,
        )

        map_item.additional_properties = d
        return map_item

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
