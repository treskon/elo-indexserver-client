from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.report_options import ReportOptions


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinReportOptions")


@_attrs_define
class BRequestIXServicePortIFCheckinReportOptions:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        options (Union[Unset, ReportOptions]): This class contains the codes for the activities/processes that are to be
            protocolled in a report.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    options: Union[Unset, "ReportOptions"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if options is not UNSET:
            field_dict["options"] = options
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.report_options import ReportOptions

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _options = d.pop("options", UNSET)
        options: Union[Unset, ReportOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ReportOptions.from_dict(_options)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_service_port_if_checkin_report_options = cls(
            ci=ci,
            options=options,
            unlock_z=unlock_z,
        )

        b_request_ix_service_port_if_checkin_report_options.additional_properties = d
        return b_request_ix_service_port_if_checkin_report_options

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
