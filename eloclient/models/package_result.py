from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_data import PackageData


T = TypeVar("T", bound="PackageResult")


@_attrs_define
class PackageResult:
    """Result of the function
    {@link PackageService#checkoutPackages(ClientInfo ci, PackageCheckoutInfo checkoutInfo, PackageDataZ packageZ, LockZ
    lockZ)}

     EIX-1895

        Attributes:
            package_data_list (Union[Unset, List['PackageData']]):
    """

    package_data_list: Union[Unset, List["PackageData"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_data_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.package_data_list, Unset):
            package_data_list = []
            for componentsschemas_list_of_package_data_item_data in self.package_data_list:
                componentsschemas_list_of_package_data_item = componentsschemas_list_of_package_data_item_data.to_dict()
                package_data_list.append(componentsschemas_list_of_package_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_data_list is not UNSET:
            field_dict["packageDataList"] = package_data_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_data import PackageData

        d = src_dict.copy()
        package_data_list = []
        _package_data_list = d.pop("packageDataList", UNSET)
        for componentsschemas_list_of_package_data_item_data in _package_data_list or []:
            componentsschemas_list_of_package_data_item = PackageData.from_dict(
                componentsschemas_list_of_package_data_item_data
            )

            package_data_list.append(componentsschemas_list_of_package_data_item)

        package_result = cls(
            package_data_list=package_data_list,
        )

        package_result.additional_properties = d
        return package_result

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
