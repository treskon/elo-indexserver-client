from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByFulltextCtrlC")


@_attrs_define
class FindByFulltextCtrlC:
    """Constants for {@link FindByFulltextCtrl}.
    EIX-2773

        Attributes:
            key_tr (Union[Unset, str]): Textreader uses this value as {@link FindByFulltextCtrl#profileKeyPrefix}.
            key_ft_plugin (Union[Unset, str]): ELOftPlugin uses this value as {@link FindByFulltextCtrl#profileKeyPrefix}.
    """

    key_tr: Union[Unset, str] = UNSET
    key_ft_plugin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_tr = self.key_tr

        key_ft_plugin = self.key_ft_plugin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_tr is not UNSET:
            field_dict["KEY_TR"] = key_tr
        if key_ft_plugin is not UNSET:
            field_dict["KEY_FT_PLUGIN"] = key_ft_plugin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_tr = d.pop("KEY_TR", UNSET)

        key_ft_plugin = d.pop("KEY_FT_PLUGIN", UNSET)

        find_by_fulltext_ctrl_c = cls(
            key_tr=key_tr,
            key_ft_plugin=key_ft_plugin,
        )

        find_by_fulltext_ctrl_c.additional_properties = d
        return find_by_fulltext_ctrl_c

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
