from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutSordPathInfo")


@_attrs_define
class CheckoutSordPathInfo:
    """
    Attributes:
        incl_ref_paths (Union[Unset, bool]):
    """

    incl_ref_paths: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incl_ref_paths = self.incl_ref_paths

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incl_ref_paths is not UNSET:
            field_dict["inclRefPaths"] = incl_ref_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incl_ref_paths = d.pop("inclRefPaths", UNSET)

        checkout_sord_path_info = cls(
            incl_ref_paths=incl_ref_paths,
        )

        checkout_sord_path_info.additional_properties = d
        return checkout_sord_path_info

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
