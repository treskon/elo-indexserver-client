from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByAcl")


@_attrs_define
class FindByAcl:
    """Find objects by ACL

    Attributes:
        distinct_acl (Union[Unset, bool]): Return a list of unique ACL entries.
            The ACL entries are wrapped in arbitary Sord objects which are returned in
             FindResult.sords. This functionality can be combinded with a FindChildren object to return all ACLs used in a
            sub
             tree.
        acls (Union[Unset, List[str]]):
    """

    distinct_acl: Union[Unset, bool] = UNSET
    acls: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distinct_acl = self.distinct_acl
        acls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.acls, Unset):
            acls = self.acls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distinct_acl is not UNSET:
            field_dict["distinctAcl"] = distinct_acl
        if acls is not UNSET:
            field_dict["acls"] = acls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        distinct_acl = d.pop("distinctAcl", UNSET)

        acls = cast(List[str], d.pop("acls", UNSET))

        find_by_acl = cls(
            distinct_acl=distinct_acl,
            acls=acls,
        )

        find_by_acl.additional_properties = d
        return find_by_acl

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
