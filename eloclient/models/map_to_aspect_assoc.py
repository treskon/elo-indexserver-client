from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.aspect_assoc import AspectAssoc


T = TypeVar("T", bound="MapToAspectAssoc")


@_attrs_define
class MapToAspectAssoc:
    """ """

    additional_properties: Dict[str, "AspectAssoc"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect_assoc import AspectAssoc

        d = src_dict.copy()
        map_to_aspect_assoc = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AspectAssoc.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        map_to_aspect_assoc.additional_properties = additional_properties
        return map_to_aspect_assoc

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AspectAssoc":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AspectAssoc") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
