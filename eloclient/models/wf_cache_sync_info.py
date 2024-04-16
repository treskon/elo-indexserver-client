from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFCacheSyncInfo")


@_attrs_define
class WFCacheSyncInfo:
    """This class is used to synchronize the workflow cache.

    Attributes:
        tstamp (Union[Unset, str]): Workflow timestamp.
        flow_id (Union[Unset, int]): Workflow ID.
        hash_ (Union[Unset, int]): Checksum on workflow data.
    """

    tstamp: Union[Unset, str] = UNSET
    flow_id: Union[Unset, int] = UNSET
    hash_: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tstamp = self.tstamp

        flow_id = self.flow_id

        hash_ = self.hash_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tstamp is not UNSET:
            field_dict["tstamp"] = tstamp
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tstamp = d.pop("tstamp", UNSET)

        flow_id = d.pop("flowId", UNSET)

        hash_ = d.pop("hash", UNSET)

        wf_cache_sync_info = cls(
            tstamp=tstamp,
            flow_id=flow_id,
            hash_=hash_,
        )

        wf_cache_sync_info.additional_properties = d
        return wf_cache_sync_info

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
