from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.package_data import PackageData
    from ..models.package_data_z import PackageDataZ


T = TypeVar("T", bound="BRequestPackageServiceCheckinPackage")


@_attrs_define
class BRequestPackageServiceCheckinPackage:
    """
    Attributes:
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        data (Union[Unset, PackageData]): This class defines a package.
            EIX-1895
        package_z (Union[Unset, PackageDataZ]): Type safe element selector for class PackageData.
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

    unlock_z: Union[Unset, "LockZ"] = UNSET
    data: Union[Unset, "PackageData"] = UNSET
    package_z: Union[Unset, "PackageDataZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        package_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_z, Unset):
            package_z = self.package_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if data is not UNSET:
            field_dict["data"] = data
        if package_z is not UNSET:
            field_dict["packageZ"] = package_z
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.package_data import PackageData
        from ..models.package_data_z import PackageDataZ

        d = src_dict.copy()
        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PackageData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PackageData.from_dict(_data)

        _package_z = d.pop("packageZ", UNSET)
        package_z: Union[Unset, PackageDataZ]
        if isinstance(_package_z, Unset):
            package_z = UNSET
        else:
            package_z = PackageDataZ.from_dict(_package_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_package_service_checkin_package = cls(
            unlock_z=unlock_z,
            data=data,
            package_z=package_z,
            ci=ci,
        )

        b_request_package_service_checkin_package.additional_properties = d
        return b_request_package_service_checkin_package

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
