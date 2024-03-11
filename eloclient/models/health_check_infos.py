from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_check_info import HealthCheckInfo


T = TypeVar("T", bound="HealthCheckInfos")


@_attrs_define
class HealthCheckInfos:
    """This class holds the values for health check evaluation.

    Attributes:
        infos (Union[Unset, List['HealthCheckInfo']]):
        archive_guid (Union[Unset, str]): Archive GUID.
        customer_license_key_hash (Union[Unset, str]): MD5 hash of license key.
            The part of the license key used to compute this hash can be obtained by
             <code><pre>conn.getServerInfo().getLicense().getSerno();</pre></code>
    """

    infos: Union[Unset, List["HealthCheckInfo"]] = UNSET
    archive_guid: Union[Unset, str] = UNSET
    customer_license_key_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.infos, Unset):
            infos = []
            for componentsschemas_list_of_health_check_info_item_data in self.infos:
                componentsschemas_list_of_health_check_info_item = (
                    componentsschemas_list_of_health_check_info_item_data.to_dict()
                )

                infos.append(componentsschemas_list_of_health_check_info_item)

        archive_guid = self.archive_guid
        customer_license_key_hash = self.customer_license_key_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if infos is not UNSET:
            field_dict["infos"] = infos
        if archive_guid is not UNSET:
            field_dict["archiveGuid"] = archive_guid
        if customer_license_key_hash is not UNSET:
            field_dict["customerLicenseKeyHash"] = customer_license_key_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.health_check_info import HealthCheckInfo

        d = src_dict.copy()
        infos = []
        _infos = d.pop("infos", UNSET)
        for componentsschemas_list_of_health_check_info_item_data in _infos or []:
            componentsschemas_list_of_health_check_info_item = HealthCheckInfo.from_dict(
                componentsschemas_list_of_health_check_info_item_data
            )

            infos.append(componentsschemas_list_of_health_check_info_item)

        archive_guid = d.pop("archiveGuid", UNSET)

        customer_license_key_hash = d.pop("customerLicenseKeyHash", UNSET)

        health_check_infos = cls(
            infos=infos,
            archive_guid=archive_guid,
            customer_license_key_hash=customer_license_key_hash,
        )

        health_check_infos.additional_properties = d
        return health_check_infos

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
