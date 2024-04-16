from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.system_info import SystemInfo


T = TypeVar("T", bound="BRequestSystemInformationLicenseReport")


@_attrs_define
class BRequestSystemInformationLicenseReport:
    """
    Attributes:
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
        si (Union[Unset, SystemInfo]): This class controls the report functions
            {@link SystemInformation#countDocsInStorePath(de.elo.ix.client.ClientInfo, SystemInfo)} and
             {@link SystemInformation#userReport(de.elo.ix.client.ClientInfo, SystemInfo)}.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    si: Union[Unset, "SystemInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        si: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.si, Unset):
            si = self.si.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if si is not UNSET:
            field_dict["si"] = si

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.system_info import SystemInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _si = d.pop("si", UNSET)
        si: Union[Unset, SystemInfo]
        if isinstance(_si, Unset):
            si = UNSET
        else:
            si = SystemInfo.from_dict(_si)

        b_request_system_information_license_report = cls(
            ci=ci,
            si=si,
        )

        b_request_system_information_license_report.additional_properties = d
        return b_request_system_information_license_report

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
