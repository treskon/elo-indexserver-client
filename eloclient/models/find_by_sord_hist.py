from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord_hist_key import SordHistKey


T = TypeVar("T", bound="FindBySordHist")


@_attrs_define
class FindBySordHist:
    """
    Attributes:
        hist_keys (Union[Unset, List['SordHistKey']]):
    """

    hist_keys: Union[Unset, List["SordHistKey"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hist_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hist_keys, Unset):
            hist_keys = []
            for hist_keys_item_data in self.hist_keys:
                hist_keys_item = hist_keys_item_data.to_dict()
                hist_keys.append(hist_keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hist_keys is not UNSET:
            field_dict["histKeys"] = hist_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord_hist_key import SordHistKey

        d = src_dict.copy()
        hist_keys = []
        _hist_keys = d.pop("histKeys", UNSET)
        for hist_keys_item_data in _hist_keys or []:
            hist_keys_item = SordHistKey.from_dict(hist_keys_item_data)

            hist_keys.append(hist_keys_item)

        find_by_sord_hist = cls(
            hist_keys=hist_keys,
        )

        find_by_sord_hist.additional_properties = d
        return find_by_sord_hist

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
