from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_report_z import UserReportZ


T = TypeVar("T", bound="SystemInfo")


@_attrs_define
class SystemInfo:
    """This class controls the report functions
    {@link SystemInformation#countDocsInStorePath(de.elo.ix.client.ClientInfo, SystemInfo)} and
     {@link SystemInformation#userReport(de.elo.ix.client.ClientInfo, SystemInfo)}.

        Attributes:
            end_date (Union[Unset, str]): Select documents created before or on this date. This is an ISODate in UTC.
            user_report_mode (Union[Unset, str]):
            store_path_id (Union[Unset, int]): ID of the {@link StoreInfo} where the documents should be counted.
            report_mode (Union[Unset, UserReportZ]): <p>
                This class encapsulates the constants of <code>UserReportC</code>
                 </p>
            start_date (Union[Unset, str]): Select documents created on or after this date. This is an ISODate in UTC.
    """

    end_date: Union[Unset, str] = UNSET
    user_report_mode: Union[Unset, str] = UNSET
    store_path_id: Union[Unset, int] = UNSET
    report_mode: Union[Unset, "UserReportZ"] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_date = self.end_date

        user_report_mode = self.user_report_mode

        store_path_id = self.store_path_id

        report_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_mode, Unset):
            report_mode = self.report_mode.to_dict()

        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if user_report_mode is not UNSET:
            field_dict["userReportMode"] = user_report_mode
        if store_path_id is not UNSET:
            field_dict["storePathID"] = store_path_id
        if report_mode is not UNSET:
            field_dict["reportMode"] = report_mode
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_report_z import UserReportZ

        d = src_dict.copy()
        end_date = d.pop("endDate", UNSET)

        user_report_mode = d.pop("userReportMode", UNSET)

        store_path_id = d.pop("storePathID", UNSET)

        _report_mode = d.pop("reportMode", UNSET)
        report_mode: Union[Unset, UserReportZ]
        if isinstance(_report_mode, Unset):
            report_mode = UNSET
        else:
            report_mode = UserReportZ.from_dict(_report_mode)

        start_date = d.pop("startDate", UNSET)

        system_info = cls(
            end_date=end_date,
            user_report_mode=user_report_mode,
            store_path_id=store_path_id,
            report_mode=report_mode,
            start_date=start_date,
        )

        system_info.additional_properties = d
        return system_info

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
