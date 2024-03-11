from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindResultAccessMode")


@_attrs_define
class FindResultAccessMode:
    """This constants are used to control the caching of find results.

    Attributes:
        random (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of find results.
        sequential (Union[Unset, FindResultAccessMode]): This constants are used to control the caching of find results.
    """

    random: Union[Unset, "FindResultAccessMode"] = UNSET
    sequential: Union[Unset, "FindResultAccessMode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        random: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.random, Unset):
            random = self.random.to_dict()

        sequential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sequential, Unset):
            sequential = self.sequential.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if random is not UNSET:
            field_dict["RANDOM"] = random
        if sequential is not UNSET:
            field_dict["SEQUENTIAL"] = sequential

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _random = d.pop("RANDOM", UNSET)
        random: Union[Unset, FindResultAccessMode]
        if isinstance(_random, Unset):
            random = UNSET
        else:
            random = FindResultAccessMode.from_dict(_random)

        _sequential = d.pop("SEQUENTIAL", UNSET)
        sequential: Union[Unset, FindResultAccessMode]
        if isinstance(_sequential, Unset):
            sequential = UNSET
        else:
            sequential = FindResultAccessMode.from_dict(_sequential)

        find_result_access_mode = cls(
            random=random,
            sequential=sequential,
        )

        find_result_access_mode.additional_properties = d
        return find_result_access_mode

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
