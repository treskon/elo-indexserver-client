from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.es_settings_obj import ESSettingsObj


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinEsSettings")


@_attrs_define
class BRequestIXServicePortIFCheckinEsSettings:
    """
    Attributes:
        settings (Union[Unset, ESSettingsObj]): <p>
            <b>checkoutEsSettings</b> returns the current IX instance name, a list of all available IX
             instances as well as one EsInstanceSettings object for every IX instance of the archive and one
             for the setting "_ALL". If there is no entry for a setting in the database, the default value is
             returned as value.
             </p>

             <p>
             <b>checkinEsSettings</b> writes entries for every EsInstanceSettings to the database:
             </p>
             <ul>
             <li>If a EsSettingsProperty member is null, nothing is written or deleted.
             <li>To delete a setting, the EsSettingsProperty member must be set, but its member 'value' must
             be set to 'null'
             </ul>
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

    settings: Union[Unset, "ESSettingsObj"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.es_settings_obj import ESSettingsObj

        d = src_dict.copy()
        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, ESSettingsObj]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ESSettingsObj.from_dict(_settings)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_checkin_es_settings = cls(
            settings=settings,
            ci=ci,
        )

        b_request_ix_service_port_if_checkin_es_settings.additional_properties = d
        return b_request_ix_service_port_if_checkin_es_settings

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
