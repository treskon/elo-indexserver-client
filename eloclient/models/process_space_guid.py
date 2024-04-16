from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessSpaceGuid")


@_attrs_define
class ProcessSpaceGuid:
    """This class specifies the options for setting a sord's spaceGuid (i.e.
    GUID of the workspace it
     belongs to). It is used as member in <code>ProcessInfo</code> and is interpreted in the functions
     <code>processFindResult</code> and <code>processTrees</code>.

        Attributes:
            space_guid (Union[Unset, str]): New spaceGuid
            space_guids (Union[Unset, List[str]]):
    """

    space_guid: Union[Unset, str] = UNSET
    space_guids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        space_guid = self.space_guid

        space_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.space_guids, Unset):
            space_guids = self.space_guids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if space_guid is not UNSET:
            field_dict["spaceGuid"] = space_guid
        if space_guids is not UNSET:
            field_dict["spaceGuids"] = space_guids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        space_guid = d.pop("spaceGuid", UNSET)

        space_guids = cast(List[str], d.pop("spaceGuids", UNSET))

        process_space_guid = cls(
            space_guid=space_guid,
            space_guids=space_guids,
        )

        process_space_guid.additional_properties = d
        return process_space_guid

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
