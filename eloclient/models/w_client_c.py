from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WClientC")


@_attrs_define
class WClientC:
    """
    Attributes:
        new_version (Union[Unset, int]):
        work_version_changed (Union[Unset, int]):
    """

    new_version: Union[Unset, int] = UNSET
    work_version_changed: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_version = self.new_version

        work_version_changed = self.work_version_changed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_version is not UNSET:
            field_dict["NEW_VERSION"] = new_version
        if work_version_changed is not UNSET:
            field_dict["WORK_VERSION_CHANGED"] = work_version_changed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_version = d.pop("NEW_VERSION", UNSET)

        work_version_changed = d.pop("WORK_VERSION_CHANGED", UNSET)

        w_client_c = cls(
            new_version=new_version,
            work_version_changed=work_version_changed,
        )

        w_client_c.additional_properties = d
        return w_client_c

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
