from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.config_batch_data import ConfigBatchData


T = TypeVar("T", bound="BRequestConfigServiceCheckinConfigurationsBatch")


@_attrs_define
class BRequestConfigServiceCheckinConfigurationsBatch:
    """
    Attributes:
        config_batch_data (Union[Unset, ConfigBatchData]): Collects configuration data to be inserted, updated, or
            deleted.
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
    """

    config_batch_data: Union[Unset, "ConfigBatchData"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_batch_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_batch_data, Unset):
            config_batch_data = self.config_batch_data.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_batch_data is not UNSET:
            field_dict["configBatchData"] = config_batch_data
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.config_batch_data import ConfigBatchData

        d = src_dict.copy()
        _config_batch_data = d.pop("configBatchData", UNSET)
        config_batch_data: Union[Unset, ConfigBatchData]
        if isinstance(_config_batch_data, Unset):
            config_batch_data = UNSET
        else:
            config_batch_data = ConfigBatchData.from_dict(_config_batch_data)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_config_service_checkin_configurations_batch = cls(
            config_batch_data=config_batch_data,
            ci=ci,
        )

        b_request_config_service_checkin_configurations_batch.additional_properties = d
        return b_request_config_service_checkin_configurations_batch

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
