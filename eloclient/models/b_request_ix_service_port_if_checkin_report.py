from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_report_info import CheckinReportInfo
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.report_info import ReportInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinReport")


@_attrs_define
class BRequestIXServicePortIFCheckinReport:
    """
    Attributes:
        reserved (Union[Unset, CheckinReportInfo]): Objects of this class specify the selection criteria for
            <code>checkinReport</code>.
            <p>
             Copyright: Copyright (c) 2014
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
        report (Union[Unset, ReportInfo]): This class describes a report/protocol entry for an action carried out in the
            archive.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    reserved: Union[Unset, "CheckinReportInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    report: Union[Unset, "ReportInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reserved: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reserved, Unset):
            reserved = self.reserved.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        report: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if ci is not UNSET:
            field_dict["ci"] = ci
        if report is not UNSET:
            field_dict["report"] = report
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_report_info import CheckinReportInfo
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.report_info import ReportInfo

        d = src_dict.copy()
        _reserved = d.pop("reserved", UNSET)
        reserved: Union[Unset, CheckinReportInfo]
        if isinstance(_reserved, Unset):
            reserved = UNSET
        else:
            reserved = CheckinReportInfo.from_dict(_reserved)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _report = d.pop("report", UNSET)
        report: Union[Unset, ReportInfo]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = ReportInfo.from_dict(_report)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        b_request_ix_service_port_if_checkin_report = cls(
            reserved=reserved,
            ci=ci,
            report=report,
            lock_z=lock_z,
        )

        b_request_ix_service_port_if_checkin_report.additional_properties = d
        return b_request_ix_service_port_if_checkin_report

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
