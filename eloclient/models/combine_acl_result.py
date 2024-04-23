from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="CombineAclResult")


@_attrs_define
class CombineAclResult:
    """This class contains the results returned by the function combineAcl.

    Attributes:
        difference_acl_str (Union[Unset, str]): String representation of AclItem array difference.
        compare_ignore_access_code (Union[Unset, int]): Compare result by ignoring the member AclItem.access. Negative
            if ACL lhs is less than rhs.
            Posiitve if ACL lhs is greater than rhs. Zero if ACLs are equal.
        compare_code (Union[Unset, int]): Compare result. Negative if ACL lhs is less than rhs. Positive if ACL lhs is
            greater than rhs.
            Zero if ACLs are equal.
        intersection (Union[Unset, List['AclItem']]):
        difference (Union[Unset, List['AclItem']]):
        inverse_difference (Union[Unset, List['AclItem']]):
        sum_ (Union[Unset, List['AclItem']]):
        inverse_difference_acl_str (Union[Unset, str]): String representation of AclItem array inverseDifference.
        intersection_acl_str (Union[Unset, str]): String representation of AclItem array intersection.
        space_intersection (Union[Unset, List['AclItem']]):
        sum_acl_str (Union[Unset, str]): String representation of AclItem array sum.
        space_intersection_str (Union[Unset, str]): String representation of AclItem array {@link #spaceIntersection}.
    """

    difference_acl_str: Union[Unset, str] = UNSET
    compare_ignore_access_code: Union[Unset, int] = UNSET
    compare_code: Union[Unset, int] = UNSET
    intersection: Union[Unset, List["AclItem"]] = UNSET
    difference: Union[Unset, List["AclItem"]] = UNSET
    inverse_difference: Union[Unset, List["AclItem"]] = UNSET
    sum_: Union[Unset, List["AclItem"]] = UNSET
    inverse_difference_acl_str: Union[Unset, str] = UNSET
    intersection_acl_str: Union[Unset, str] = UNSET
    space_intersection: Union[Unset, List["AclItem"]] = UNSET
    sum_acl_str: Union[Unset, str] = UNSET
    space_intersection_str: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        difference_acl_str = self.difference_acl_str

        compare_ignore_access_code = self.compare_ignore_access_code

        compare_code = self.compare_code

        intersection: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.intersection, Unset):
            intersection = []
            for intersection_item_data in self.intersection:
                intersection_item = intersection_item_data.to_dict()
                intersection.append(intersection_item)

        difference: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.difference, Unset):
            difference = []
            for difference_item_data in self.difference:
                difference_item = difference_item_data.to_dict()
                difference.append(difference_item)

        inverse_difference: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inverse_difference, Unset):
            inverse_difference = []
            for inverse_difference_item_data in self.inverse_difference:
                inverse_difference_item = inverse_difference_item_data.to_dict()
                inverse_difference.append(inverse_difference_item)

        sum_: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sum_, Unset):
            sum_ = []
            for sum_item_data in self.sum_:
                sum_item = sum_item_data.to_dict()
                sum_.append(sum_item)

        inverse_difference_acl_str = self.inverse_difference_acl_str

        intersection_acl_str = self.intersection_acl_str

        space_intersection: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.space_intersection, Unset):
            space_intersection = []
            for space_intersection_item_data in self.space_intersection:
                space_intersection_item = space_intersection_item_data.to_dict()
                space_intersection.append(space_intersection_item)

        sum_acl_str = self.sum_acl_str

        space_intersection_str = self.space_intersection_str

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if difference_acl_str is not UNSET:
            field_dict["differenceAclStr"] = difference_acl_str
        if compare_ignore_access_code is not UNSET:
            field_dict["compareIgnoreAccessCode"] = compare_ignore_access_code
        if compare_code is not UNSET:
            field_dict["compareCode"] = compare_code
        if intersection is not UNSET:
            field_dict["intersection"] = intersection
        if difference is not UNSET:
            field_dict["difference"] = difference
        if inverse_difference is not UNSET:
            field_dict["inverseDifference"] = inverse_difference
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if inverse_difference_acl_str is not UNSET:
            field_dict["inverseDifferenceAclStr"] = inverse_difference_acl_str
        if intersection_acl_str is not UNSET:
            field_dict["intersectionAclStr"] = intersection_acl_str
        if space_intersection is not UNSET:
            field_dict["spaceIntersection"] = space_intersection
        if sum_acl_str is not UNSET:
            field_dict["sumAclStr"] = sum_acl_str
        if space_intersection_str is not UNSET:
            field_dict["spaceIntersectionStr"] = space_intersection_str

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        difference_acl_str = d.pop("differenceAclStr", UNSET)

        compare_ignore_access_code = d.pop("compareIgnoreAccessCode", UNSET)

        compare_code = d.pop("compareCode", UNSET)

        intersection = []
        _intersection = d.pop("intersection", UNSET)
        for intersection_item_data in _intersection or []:
            intersection_item = AclItem.from_dict(intersection_item_data)

            intersection.append(intersection_item)

        difference = []
        _difference = d.pop("difference", UNSET)
        for difference_item_data in _difference or []:
            difference_item = AclItem.from_dict(difference_item_data)

            difference.append(difference_item)

        inverse_difference = []
        _inverse_difference = d.pop("inverseDifference", UNSET)
        for inverse_difference_item_data in _inverse_difference or []:
            inverse_difference_item = AclItem.from_dict(inverse_difference_item_data)

            inverse_difference.append(inverse_difference_item)

        sum_ = []
        _sum_ = d.pop("sum", UNSET)
        for sum_item_data in _sum_ or []:
            sum_item = AclItem.from_dict(sum_item_data)

            sum_.append(sum_item)

        inverse_difference_acl_str = d.pop("inverseDifferenceAclStr", UNSET)

        intersection_acl_str = d.pop("intersectionAclStr", UNSET)

        space_intersection = []
        _space_intersection = d.pop("spaceIntersection", UNSET)
        for space_intersection_item_data in _space_intersection or []:
            space_intersection_item = AclItem.from_dict(space_intersection_item_data)

            space_intersection.append(space_intersection_item)

        sum_acl_str = d.pop("sumAclStr", UNSET)

        space_intersection_str = d.pop("spaceIntersectionStr", UNSET)

        combine_acl_result = cls(
            difference_acl_str=difference_acl_str,
            compare_ignore_access_code=compare_ignore_access_code,
            compare_code=compare_code,
            intersection=intersection,
            difference=difference,
            inverse_difference=inverse_difference,
            sum_=sum_,
            inverse_difference_acl_str=inverse_difference_acl_str,
            intersection_acl_str=intersection_acl_str,
            space_intersection=space_intersection,
            sum_acl_str=sum_acl_str,
            space_intersection_str=space_intersection_str,
        )

        combine_acl_result.additional_properties = d
        return combine_acl_result

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
