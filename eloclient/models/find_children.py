from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindChildren")


@_attrs_define
class FindChildren:
    """This class controls the search for child objects of an archive entry.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            parent_id (Union[Unset, str]): Search child objects of the parent entry with this object ID or GUID.
            end_level (Union[Unset, int]): Search child objects up to this level below parentId.
                A value of 0 or 1 means, that only the
                 sub entries directly under the parent are included. Set this value to -1, to search over all
                 levels. In this case the level is internally constrained to 32 to avoid an endless loop, if the
                 tree under the parent contains recursive references.
            main_parent (Union[Unset, bool]): Include only main parent relations.
    """

    parent_id: Union[Unset, str] = UNSET
    end_level: Union[Unset, int] = UNSET
    main_parent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_id = self.parent_id

        end_level = self.end_level

        main_parent = self.main_parent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if end_level is not UNSET:
            field_dict["endLevel"] = end_level
        if main_parent is not UNSET:
            field_dict["mainParent"] = main_parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parent_id = d.pop("parentId", UNSET)

        end_level = d.pop("endLevel", UNSET)

        main_parent = d.pop("mainParent", UNSET)

        find_children = cls(
            parent_id=parent_id,
            end_level=end_level,
            main_parent=main_parent,
        )

        find_children.additional_properties = d
        return find_children

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
