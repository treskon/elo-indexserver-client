from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord_path import SordPath


T = TypeVar("T", bound="SordPaths")


@_attrs_define
class SordPaths:
    """
    Attributes:
        sord_paths (Union[Unset, List['SordPath']]):
    """

    sord_paths: Union[Unset, List["SordPath"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sord_paths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sord_paths, Unset):
            sord_paths = []
            for componentsschemas_list_of_sord_path_item_data in self.sord_paths:
                componentsschemas_list_of_sord_path_item = componentsschemas_list_of_sord_path_item_data.to_dict()
                sord_paths.append(componentsschemas_list_of_sord_path_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sord_paths is not UNSET:
            field_dict["sordPaths"] = sord_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord_path import SordPath

        d = src_dict.copy()
        sord_paths = []
        _sord_paths = d.pop("sordPaths", UNSET)
        for componentsschemas_list_of_sord_path_item_data in _sord_paths or []:
            componentsschemas_list_of_sord_path_item = SordPath.from_dict(componentsschemas_list_of_sord_path_item_data)

            sord_paths.append(componentsschemas_list_of_sord_path_item)

        sord_paths = cls(
            sord_paths=sord_paths,
        )

        sord_paths.additional_properties = d
        return sord_paths

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
