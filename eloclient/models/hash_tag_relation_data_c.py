from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HashTagRelationDataC")


@_attrs_define
class HashTagRelationDataC:
    """<p>Bit constants for members of HashTagRelation</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_action_guid (Union[Unset, int]): Column length: Guid of the Action in which the HashTag is used.
                DB column: actionguid
            mb_status (Union[Unset, str]): Member bit: Status.
                DB column: status
            ln_hashtag_guid (Union[Unset, int]): Column length: Guid of the HashTag.
                DB column: hashtagguid
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp for replication.
                DB column: tstamp
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_action_guid (Union[Unset, str]): Member bit: Guid of the Action in which the HashTag is used.
                DB column: actionguid
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp for replication.
                DB column: tstamp
            mb_hashtag_guid (Union[Unset, str]): Member bit: Guid of the HashTag.
                DB column: hashtagguid
    """

    ln_action_guid: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    ln_hashtag_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_action_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_hashtag_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_action_guid = self.ln_action_guid

        mb_status = self.mb_status

        ln_hashtag_guid = self.ln_hashtag_guid

        mb_t_stamp = self.mb_t_stamp

        mb_all_members = self.mb_all_members

        mb_action_guid = self.mb_action_guid

        ln_t_stamp = self.ln_t_stamp

        mb_hashtag_guid = self.mb_hashtag_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_action_guid is not UNSET:
            field_dict["lnActionGuid"] = ln_action_guid
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if ln_hashtag_guid is not UNSET:
            field_dict["lnHashtagGuid"] = ln_hashtag_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_action_guid is not UNSET:
            field_dict["mbActionGuid"] = mb_action_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_hashtag_guid is not UNSET:
            field_dict["mbHashtagGuid"] = mb_hashtag_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_action_guid = d.pop("lnActionGuid", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        ln_hashtag_guid = d.pop("lnHashtagGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_action_guid = d.pop("mbActionGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_hashtag_guid = d.pop("mbHashtagGuid", UNSET)

        hash_tag_relation_data_c = cls(
            ln_action_guid=ln_action_guid,
            mb_status=mb_status,
            ln_hashtag_guid=ln_hashtag_guid,
            mb_t_stamp=mb_t_stamp,
            mb_all_members=mb_all_members,
            mb_action_guid=mb_action_guid,
            ln_t_stamp=ln_t_stamp,
            mb_hashtag_guid=mb_hashtag_guid,
        )

        hash_tag_relation_data_c.additional_properties = d
        return hash_tag_relation_data_c

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
