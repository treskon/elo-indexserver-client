from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.health_check_info import HealthCheckInfo


T = TypeVar("T", bound="BRequestHealthCheckServiceUpdateAll")


@_attrs_define
class BRequestHealthCheckServiceUpdateAll:
    """
    Attributes:
        hcis (Union[Unset, List['HealthCheckInfo']]):
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

    hcis: Union[Unset, List["HealthCheckInfo"]] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hcis: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hcis, Unset):
            hcis = []
            for componentsschemas_list_of_health_check_info_item_data in self.hcis:
                componentsschemas_list_of_health_check_info_item = (
                    componentsschemas_list_of_health_check_info_item_data.to_dict()
                )
                hcis.append(componentsschemas_list_of_health_check_info_item)

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hcis is not UNSET:
            field_dict["hcis"] = hcis
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.health_check_info import HealthCheckInfo

        d = src_dict.copy()
        hcis = []
        _hcis = d.pop("hcis", UNSET)
        for componentsschemas_list_of_health_check_info_item_data in _hcis or []:
            componentsschemas_list_of_health_check_info_item = HealthCheckInfo.from_dict(
                componentsschemas_list_of_health_check_info_item_data
            )

            hcis.append(componentsschemas_list_of_health_check_info_item)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_health_check_service_update_all = cls(
            hcis=hcis,
            ci=ci,
        )

        b_request_health_check_service_update_all.additional_properties = d
        return b_request_health_check_service_update_all

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
