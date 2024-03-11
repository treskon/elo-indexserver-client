from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hash_tag_z import HashTagZ


T = TypeVar("T", bound="HashTagC")


@_attrs_define
class HashTagC:
    """Constants for class HashTag

    Attributes:
        mb_all (Union[Unset, HashTagZ]):
        mb_guid (Union[Unset, HashTagZ]):
        mb_last_used (Union[Unset, HashTagZ]):
    """

    mb_all: Union[Unset, "HashTagZ"] = UNSET
    mb_guid: Union[Unset, "HashTagZ"] = UNSET
    mb_last_used: Union[Unset, "HashTagZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_guid, Unset):
            mb_guid = self.mb_guid.to_dict()

        mb_last_used: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_last_used, Unset):
            mb_last_used = self.mb_last_used.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_last_used is not UNSET:
            field_dict["mbLastUsed"] = mb_last_used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hash_tag_z import HashTagZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, HashTagZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = HashTagZ.from_dict(_mb_all)

        _mb_guid = d.pop("mbGuid", UNSET)
        mb_guid: Union[Unset, HashTagZ]
        if isinstance(_mb_guid, Unset):
            mb_guid = UNSET
        else:
            mb_guid = HashTagZ.from_dict(_mb_guid)

        _mb_last_used = d.pop("mbLastUsed", UNSET)
        mb_last_used: Union[Unset, HashTagZ]
        if isinstance(_mb_last_used, Unset):
            mb_last_used = UNSET
        else:
            mb_last_used = HashTagZ.from_dict(_mb_last_used)

        hash_tag_c = cls(
            mb_all=mb_all,
            mb_guid=mb_guid,
            mb_last_used=mb_last_used,
        )

        hash_tag_c.additional_properties = d
        return hash_tag_c

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
