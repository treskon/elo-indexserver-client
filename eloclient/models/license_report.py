from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_counter import LicenseCounter
    from ..models.license_type import LicenseType


T = TypeVar("T", bound="LicenseReport")


@_attrs_define
class LicenseReport:
    """License report data evaluated by AdminConsole.

    Attributes:
        nb_of_ig_licenses (Union[Unset, int]): Number of ELO Internet Gateway users. This field is not used anymore.
        license_type (Union[Unset, LicenseType]): This enumeration defines constants for the license type.
            The license type is set during
             installation as production, test or development.
        counter_list (Union[Unset, List['LicenseCounter']]):
        nb_of_server_licenses (Union[Unset, int]): Number of server licenses. This field is not used anymore.
        serno (Union[Unset, str]): License key. This field is not used anymore.
        free_user (Union[Unset, int]):
        ix_user (Union[Unset, int]):
        report_mode (Union[Unset, int]): report period / access mode.
        full_user (Union[Unset, int]):
        deleted_user (Union[Unset, int]):
    """

    nb_of_ig_licenses: Union[Unset, int] = UNSET
    license_type: Union[Unset, "LicenseType"] = UNSET
    counter_list: Union[Unset, List["LicenseCounter"]] = UNSET
    nb_of_server_licenses: Union[Unset, int] = UNSET
    serno: Union[Unset, str] = UNSET
    free_user: Union[Unset, int] = UNSET
    ix_user: Union[Unset, int] = UNSET
    report_mode: Union[Unset, int] = UNSET
    full_user: Union[Unset, int] = UNSET
    deleted_user: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nb_of_ig_licenses = self.nb_of_ig_licenses

        license_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_type, Unset):
            license_type = self.license_type.to_dict()

        counter_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.counter_list, Unset):
            counter_list = []
            for componentsschemas_list_of_license_counter_item_data in self.counter_list:
                componentsschemas_list_of_license_counter_item = (
                    componentsschemas_list_of_license_counter_item_data.to_dict()
                )
                counter_list.append(componentsschemas_list_of_license_counter_item)

        nb_of_server_licenses = self.nb_of_server_licenses

        serno = self.serno

        free_user = self.free_user

        ix_user = self.ix_user

        report_mode = self.report_mode

        full_user = self.full_user

        deleted_user = self.deleted_user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nb_of_ig_licenses is not UNSET:
            field_dict["nbOfIgLicenses"] = nb_of_ig_licenses
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if counter_list is not UNSET:
            field_dict["counterList"] = counter_list
        if nb_of_server_licenses is not UNSET:
            field_dict["nbOfServerLicenses"] = nb_of_server_licenses
        if serno is not UNSET:
            field_dict["serno"] = serno
        if free_user is not UNSET:
            field_dict["freeUser"] = free_user
        if ix_user is not UNSET:
            field_dict["ixUser"] = ix_user
        if report_mode is not UNSET:
            field_dict["reportMode"] = report_mode
        if full_user is not UNSET:
            field_dict["fullUser"] = full_user
        if deleted_user is not UNSET:
            field_dict["deletedUser"] = deleted_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.license_counter import LicenseCounter
        from ..models.license_type import LicenseType

        d = src_dict.copy()
        nb_of_ig_licenses = d.pop("nbOfIgLicenses", UNSET)

        _license_type = d.pop("licenseType", UNSET)
        license_type: Union[Unset, LicenseType]
        if isinstance(_license_type, Unset):
            license_type = UNSET
        else:
            license_type = LicenseType.from_dict(_license_type)

        counter_list = []
        _counter_list = d.pop("counterList", UNSET)
        for componentsschemas_list_of_license_counter_item_data in _counter_list or []:
            componentsschemas_list_of_license_counter_item = LicenseCounter.from_dict(
                componentsschemas_list_of_license_counter_item_data
            )

            counter_list.append(componentsschemas_list_of_license_counter_item)

        nb_of_server_licenses = d.pop("nbOfServerLicenses", UNSET)

        serno = d.pop("serno", UNSET)

        free_user = d.pop("freeUser", UNSET)

        ix_user = d.pop("ixUser", UNSET)

        report_mode = d.pop("reportMode", UNSET)

        full_user = d.pop("fullUser", UNSET)

        deleted_user = d.pop("deletedUser", UNSET)

        license_report = cls(
            nb_of_ig_licenses=nb_of_ig_licenses,
            license_type=license_type,
            counter_list=counter_list,
            nb_of_server_licenses=nb_of_server_licenses,
            serno=serno,
            free_user=free_user,
            ix_user=ix_user,
            report_mode=report_mode,
            full_user=full_user,
            deleted_user=deleted_user,
        )

        license_report.additional_properties = d
        return license_report

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
