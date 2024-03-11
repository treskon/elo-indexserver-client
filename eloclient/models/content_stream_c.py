from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentStreamC")


@_attrs_define
class ContentStreamC:
    """Constants related to {@link ContentStream}.

    Attributes:
        content_length_unknown (Union[Unset, str]): Pseudo content length for streams of unknown size.
    """

    content_length_unknown: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_length_unknown = self.content_length_unknown

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_length_unknown is not UNSET:
            field_dict["CONTENT_LENGTH_UNKNOWN"] = content_length_unknown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_length_unknown = d.pop("CONTENT_LENGTH_UNKNOWN", UNSET)

        content_stream_c = cls(
            content_length_unknown=content_length_unknown,
        )

        content_stream_c.additional_properties = d
        return content_stream_c

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
