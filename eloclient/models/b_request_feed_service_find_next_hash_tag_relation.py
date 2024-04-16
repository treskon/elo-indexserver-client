from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.hash_tag_z import HashTagZ


T = TypeVar("T", bound="BRequestFeedServiceFindNextHashTagRelation")


@_attrs_define
class BRequestFeedServiceFindNextHashTagRelation:
    """
    Attributes:
        search_id (Union[Unset, str]):
        max_ (Union[Unset, int]):
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        hash_tag_z (Union[Unset, HashTagZ]):
        idx (Union[Unset, int]):
    """

    search_id: Union[Unset, str] = UNSET
    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    hash_tag_z: Union[Unset, "HashTagZ"] = UNSET
    idx: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_id = self.search_id

        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        hash_tag_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hash_tag_z, Unset):
            hash_tag_z = self.hash_tag_z.to_dict()

        idx = self.idx

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if hash_tag_z is not UNSET:
            field_dict["hashTagZ"] = hash_tag_z
        if idx is not UNSET:
            field_dict["idx"] = idx

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.hash_tag_z import HashTagZ

        d = src_dict.copy()
        search_id = d.pop("searchId", UNSET)

        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _hash_tag_z = d.pop("hashTagZ", UNSET)
        hash_tag_z: Union[Unset, HashTagZ]
        if isinstance(_hash_tag_z, Unset):
            hash_tag_z = UNSET
        else:
            hash_tag_z = HashTagZ.from_dict(_hash_tag_z)

        idx = d.pop("idx", UNSET)

        b_request_feed_service_find_next_hash_tag_relation = cls(
            search_id=search_id,
            max_=max_,
            ci=ci,
            hash_tag_z=hash_tag_z,
            idx=idx,
        )

        b_request_feed_service_find_next_hash_tag_relation.additional_properties = d
        return b_request_feed_service_find_next_hash_tag_relation

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
