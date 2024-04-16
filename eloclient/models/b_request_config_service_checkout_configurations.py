from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.config_info import ConfigInfo
    from ..models.config_result_options import ConfigResultOptions


T = TypeVar("T", bound="BRequestConfigServiceCheckoutConfigurations")


@_attrs_define
class BRequestConfigServiceCheckoutConfigurations:
    """
    Attributes:
        config_result_options (Union[Unset, ConfigResultOptions]): This options control grouping of configuration
            entries returned by
            {@link ConfigService#checkoutConfigurations(de.elo.ix.client.ClientInfo, ConfigInfo, ConfigResultOptions)}.
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        config_info (Union[Unset, ConfigInfo]): This class defines select criteria for reading configuration data.
    """

    config_result_options: Union[Unset, "ConfigResultOptions"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    config_info: Union[Unset, "ConfigInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_result_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_result_options, Unset):
            config_result_options = self.config_result_options.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        config_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_info, Unset):
            config_info = self.config_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_result_options is not UNSET:
            field_dict["configResultOptions"] = config_result_options
        if ci is not UNSET:
            field_dict["ci"] = ci
        if config_info is not UNSET:
            field_dict["configInfo"] = config_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.config_info import ConfigInfo
        from ..models.config_result_options import ConfigResultOptions

        d = src_dict.copy()
        _config_result_options = d.pop("configResultOptions", UNSET)
        config_result_options: Union[Unset, ConfigResultOptions]
        if isinstance(_config_result_options, Unset):
            config_result_options = UNSET
        else:
            config_result_options = ConfigResultOptions.from_dict(_config_result_options)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _config_info = d.pop("configInfo", UNSET)
        config_info: Union[Unset, ConfigInfo]
        if isinstance(_config_info, Unset):
            config_info = UNSET
        else:
            config_info = ConfigInfo.from_dict(_config_info)

        b_request_config_service_checkout_configurations = cls(
            config_result_options=config_result_options,
            ci=ci,
            config_info=config_info,
        )

        b_request_config_service_checkout_configurations.additional_properties = d
        return b_request_config_service_checkout_configurations

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
