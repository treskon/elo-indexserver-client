from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkSordInfo")


@_attrs_define
class LinkSordInfo:
    """Additional parameters for function {@link IXServicePortIF#linkSords2}

    Attributes:
        link_permanent (Union[Unset, bool]): If true, Sords will be linked permanently.
            The new links between the provided Sords cannot be
             deleted.
    """

    link_permanent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link_permanent = self.link_permanent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_permanent is not UNSET:
            field_dict["linkPermanent"] = link_permanent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        link_permanent = d.pop("linkPermanent", UNSET)

        link_sord_info = cls(
            link_permanent=link_permanent,
        )

        link_sord_info.additional_properties = d
        return link_sord_info

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
