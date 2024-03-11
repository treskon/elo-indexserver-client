from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HashTagRelation")


@_attrs_define
class HashTagRelation:
    """This class represents the relation between HashTags and Actions.

    Attributes:
        hashtag_guid (Union[Unset, str]): Guid of the HashTag.
        action_guid (Union[Unset, str]): Guid of the Action in which the HashTag is used.
        t_stamp (Union[Unset, str]): Timestamp for replication.
        status (Union[Unset, int]): Status.
    """

    hashtag_guid: Union[Unset, str] = UNSET
    action_guid: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hashtag_guid = self.hashtag_guid
        action_guid = self.action_guid
        t_stamp = self.t_stamp
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hashtag_guid is not UNSET:
            field_dict["hashtagGuid"] = hashtag_guid
        if action_guid is not UNSET:
            field_dict["actionGuid"] = action_guid
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hashtag_guid = d.pop("hashtagGuid", UNSET)

        action_guid = d.pop("actionGuid", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        status = d.pop("status", UNSET)

        hash_tag_relation = cls(
            hashtag_guid=hashtag_guid,
            action_guid=action_guid,
            t_stamp=t_stamp,
            status=status,
        )

        hash_tag_relation.additional_properties = d
        return hash_tag_relation

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
