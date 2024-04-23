from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteOrgUnitInfo")


@_attrs_define
class DeleteOrgUnitInfo:
    """Objects of this class specify the selection criteria for <code>deleteOrgUnits</code>.
    OU IDs or
     names can be set or both.

     <p>
     Copyright: Copyright (c) 2013
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            names (Union[Unset, List[str]]):
            ids (Union[Unset, List[int]]):
    """

    names: Union[Unset, List[str]] = UNSET
    ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if names is not UNSET:
            field_dict["names"] = names
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        names = cast(List[str], d.pop("names", UNSET))

        ids = cast(List[int], d.pop("ids", UNSET))

        delete_org_unit_info = cls(
            names=names,
            ids=ids,
        )

        delete_org_unit_info.additional_properties = d
        return delete_org_unit_info

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
