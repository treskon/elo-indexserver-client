from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_z import SubscriptionZ


T = TypeVar("T", bound="SubscriptionC")


@_attrs_define
class SubscriptionC:
    """
    Attributes:
        mb_all (Union[Unset, SubscriptionZ]):
    """

    mb_all: Union[Unset, "SubscriptionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscription_z import SubscriptionZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, SubscriptionZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = SubscriptionZ.from_dict(_mb_all)

        subscription_c = cls(
            mb_all=mb_all,
        )

        subscription_c.additional_properties = d
        return subscription_c

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
