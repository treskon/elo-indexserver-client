from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hash_tag import HashTag


T = TypeVar("T", bound="BResult1535847981")


@_attrs_define
class BResult1535847981:
    """
    Attributes:
        result (Union[Unset, List['HashTag']]):
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, List["HashTag"]] = UNSET
    exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for componentsschemas_hash_set_of_hash_tag_item_data in self.result:
                componentsschemas_hash_set_of_hash_tag_item = componentsschemas_hash_set_of_hash_tag_item_data.to_dict()
                result.append(componentsschemas_hash_set_of_hash_tag_item)

        exception = self.exception

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hash_tag import HashTag

        d = src_dict.copy()
        result = []
        _result = d.pop("result", UNSET)
        for componentsschemas_hash_set_of_hash_tag_item_data in _result or []:
            componentsschemas_hash_set_of_hash_tag_item = HashTag.from_dict(
                componentsschemas_hash_set_of_hash_tag_item_data
            )

            result.append(componentsschemas_hash_set_of_hash_tag_item)

        exception = d.pop("exception", UNSET)

        b_result_1535847981 = cls(
            result=result,
            exception=exception,
        )

        b_result_1535847981.additional_properties = d
        return b_result_1535847981

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
