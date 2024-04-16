from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.package_checkout_info import PackageCheckoutInfo
    from ..models.package_data_z import PackageDataZ


T = TypeVar("T", bound="BRequestPackageServiceCheckoutPackages")


@_attrs_define
class BRequestPackageServiceCheckoutPackages:
    """
    Attributes:
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
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        checkout_info (Union[Unset, PackageCheckoutInfo]): Describes checkout criteria for
            {@link PackageService#checkoutPackages(ClientInfo ci, PackageCheckoutInfo checkoutInfo, PackageDataZ packageZ,
            LockZ lockZ)}.

             EIX-1895
    """

    package_z: Union[Unset, "PackageDataZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    checkout_info: Union[Unset, "PackageCheckoutInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_z, Unset):
            package_z = self.package_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        checkout_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_info, Unset):
            checkout_info = self.checkout_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_z is not UNSET:
            field_dict["packageZ"] = package_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if checkout_info is not UNSET:
            field_dict["checkoutInfo"] = checkout_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.package_checkout_info import PackageCheckoutInfo
        from ..models.package_data_z import PackageDataZ

        d = src_dict.copy()
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

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        _checkout_info = d.pop("checkoutInfo", UNSET)
        checkout_info: Union[Unset, PackageCheckoutInfo]
        if isinstance(_checkout_info, Unset):
            checkout_info = UNSET
        else:
            checkout_info = PackageCheckoutInfo.from_dict(_checkout_info)

        b_request_package_service_checkout_packages = cls(
            package_z=package_z,
            ci=ci,
            lock_z=lock_z,
            checkout_info=checkout_info,
        )

        b_request_package_service_checkout_packages.additional_properties = d
        return b_request_package_service_checkout_packages

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
