from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.config_record import ConfigRecord


T = TypeVar("T", bound="BRequestConfigServiceCheckinConfigurations")


@_attrs_define
class BRequestConfigServiceCheckinConfigurations:
    """
    Attributes:
        config_records (Union[Unset, List['ConfigRecord']]):
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

    config_records: Union[Unset, List["ConfigRecord"]] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.config_records, Unset):
            config_records = []
            for componentsschemas_list_of_config_record_item_data in self.config_records:
                componentsschemas_list_of_config_record_item = (
                    componentsschemas_list_of_config_record_item_data.to_dict()
                )
                config_records.append(componentsschemas_list_of_config_record_item)

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_records is not UNSET:
            field_dict["configRecords"] = config_records
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.config_record import ConfigRecord

        d = src_dict.copy()
        config_records = []
        _config_records = d.pop("configRecords", UNSET)
        for componentsschemas_list_of_config_record_item_data in _config_records or []:
            componentsschemas_list_of_config_record_item = ConfigRecord.from_dict(
                componentsschemas_list_of_config_record_item_data
            )

            config_records.append(componentsschemas_list_of_config_record_item)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_config_service_checkin_configurations = cls(
            config_records=config_records,
            ci=ci,
        )

        b_request_config_service_checkin_configurations.additional_properties = d
        return b_request_config_service_checkin_configurations

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
