from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord import Sord


T = TypeVar("T", bound="SordPath")


@_attrs_define
class SordPath:
    """
    Attributes:
        sords (Union[Unset, List['Sord']]):
    """

    sords: Union[Unset, List["Sord"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sords, Unset):
            sords = []
            for componentsschemas_list_of_sord_item_data in self.sords:
                componentsschemas_list_of_sord_item = componentsschemas_list_of_sord_item_data.to_dict()

                sords.append(componentsschemas_list_of_sord_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sords is not UNSET:
            field_dict["sords"] = sords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord import Sord

        d = src_dict.copy()
        sords = []
        _sords = d.pop("sords", UNSET)
        for componentsschemas_list_of_sord_item_data in _sords or []:
            componentsschemas_list_of_sord_item = Sord.from_dict(componentsschemas_list_of_sord_item_data)

            sords.append(componentsschemas_list_of_sord_item)

        sord_path = cls(
            sords=sords,
        )

        sord_path.additional_properties = d
        return sord_path

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
