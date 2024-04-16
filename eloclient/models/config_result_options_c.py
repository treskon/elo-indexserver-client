from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_result_options import ConfigResultOptions


T = TypeVar("T", bound="ConfigResultOptionsC")


@_attrs_define
class ConfigResultOptionsC:
    """Predefined objects to be used as parameter in
    {@link ConfigService#checkoutConfigurations(de.elo.ix.client.ClientInfo, ConfigInfo, ConfigResultOptions)}.

        Attributes:
            default_exploded (Union[Unset, ConfigResultOptions]): This options control grouping of configuration entries
                returned by
                {@link ConfigService#checkoutConfigurations(de.elo.ix.client.ClientInfo, ConfigInfo, ConfigResultOptions)}.
            default (Union[Unset, ConfigResultOptions]): This options control grouping of configuration entries returned by
                {@link ConfigService#checkoutConfigurations(de.elo.ix.client.ClientInfo, ConfigInfo, ConfigResultOptions)}.
    """

    default_exploded: Union[Unset, "ConfigResultOptions"] = UNSET
    default: Union[Unset, "ConfigResultOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_exploded: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_exploded, Unset):
            default_exploded = self.default_exploded.to_dict()

        default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_exploded is not UNSET:
            field_dict["DEFAULT_EXPLODED"] = default_exploded
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_result_options import ConfigResultOptions

        d = src_dict.copy()
        _default_exploded = d.pop("DEFAULT_EXPLODED", UNSET)
        default_exploded: Union[Unset, ConfigResultOptions]
        if isinstance(_default_exploded, Unset):
            default_exploded = UNSET
        else:
            default_exploded = ConfigResultOptions.from_dict(_default_exploded)

        _default = d.pop("DEFAULT", UNSET)
        default: Union[Unset, ConfigResultOptions]
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = ConfigResultOptions.from_dict(_default)

        config_result_options_c = cls(
            default_exploded=default_exploded,
            default=default,
        )

        config_result_options_c.additional_properties = d
        return config_result_options_c

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
