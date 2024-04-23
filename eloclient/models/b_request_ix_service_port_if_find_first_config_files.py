from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.config_file_z import ConfigFileZ
    from ..models.find_config_file_info import FindConfigFileInfo


T = TypeVar("T", bound="BRequestIXServicePortIFFindFirstConfigFiles")


@_attrs_define
class BRequestIXServicePortIFFindFirstConfigFiles:
    """
    Attributes:
        max_ (Union[Unset, int]):
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
        find_info (Union[Unset, FindConfigFileInfo]): This class describes the files to select from a postbox directory
            or from a configuration
            directory.
        config_file_z (Union[Unset, ConfigFileZ]): This class encapsulates the constants of ConfigFileC.
    """

    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    find_info: Union[Unset, "FindConfigFileInfo"] = UNSET
    config_file_z: Union[Unset, "ConfigFileZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        config_file_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config_file_z, Unset):
            config_file_z = self.config_file_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info
        if config_file_z is not UNSET:
            field_dict["configFileZ"] = config_file_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.config_file_z import ConfigFileZ
        from ..models.find_config_file_info import FindConfigFileInfo

        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindConfigFileInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindConfigFileInfo.from_dict(_find_info)

        _config_file_z = d.pop("configFileZ", UNSET)
        config_file_z: Union[Unset, ConfigFileZ]
        if isinstance(_config_file_z, Unset):
            config_file_z = UNSET
        else:
            config_file_z = ConfigFileZ.from_dict(_config_file_z)

        b_request_ix_service_port_if_find_first_config_files = cls(
            max_=max_,
            ci=ci,
            find_info=find_info,
            config_file_z=config_file_z,
        )

        b_request_ix_service_port_if_find_first_config_files.additional_properties = d
        return b_request_ix_service_port_if_find_first_config_files

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
