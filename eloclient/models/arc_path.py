from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name import IdName


T = TypeVar("T", bound="ArcPath")


@_attrs_define
class ArcPath:
    """Archive path.

    Attributes:
        path (Union[Unset, List['IdName']]):
        path_as_string (Union[Unset, str]): Path as string. The first charachter is the path separator.
    """

    path: Union[Unset, List["IdName"]] = UNSET
    path_as_string: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item = path_item_data.to_dict()
                path.append(path_item)

        path_as_string = self.path_as_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if path_as_string is not UNSET:
            field_dict["pathAsString"] = path_as_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.id_name import IdName

        d = src_dict.copy()
        path = []
        _path = d.pop("path", UNSET)
        for path_item_data in _path or []:
            path_item = IdName.from_dict(path_item_data)

            path.append(path_item)

        path_as_string = d.pop("pathAsString", UNSET)

        arc_path = cls(
            path=path,
            path_as_string=path_as_string,
        )

        arc_path.additional_properties = d
        return arc_path

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
