from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CombineAclOptions")


@_attrs_define
class CombineAclOptions:
    """This class specifies additional options for compareAcl.

    Attributes:
        rhs_acl_str (Union[Unset, str]): Right operand for ACL operation in String representation.
        lhs_acl_str (Union[Unset, str]): Left operand for ACL operation in String representation.
    """

    rhs_acl_str: Union[Unset, str] = UNSET
    lhs_acl_str: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rhs_acl_str = self.rhs_acl_str

        lhs_acl_str = self.lhs_acl_str

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rhs_acl_str is not UNSET:
            field_dict["rhsAclStr"] = rhs_acl_str
        if lhs_acl_str is not UNSET:
            field_dict["lhsAclStr"] = lhs_acl_str

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rhs_acl_str = d.pop("rhsAclStr", UNSET)

        lhs_acl_str = d.pop("lhsAclStr", UNSET)

        combine_acl_options = cls(
            rhs_acl_str=rhs_acl_str,
            lhs_acl_str=lhs_acl_str,
        )

        combine_acl_options.additional_properties = d
        return combine_acl_options

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
