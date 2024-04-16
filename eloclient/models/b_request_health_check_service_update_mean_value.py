from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestHealthCheckServiceUpdateMeanValue")


@_attrs_define
class BRequestHealthCheckServiceUpdateMeanValue:
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
        name (Union[Unset, str]):
        mean_value (Union[Unset, float]):
        sample_size (Union[Unset, str]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    name: Union[Unset, str] = UNSET
    mean_value: Union[Unset, float] = UNSET
    sample_size: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        name = self.name

        mean_value = self.mean_value

        sample_size = self.sample_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if name is not UNSET:
            field_dict["name"] = name
        if mean_value is not UNSET:
            field_dict["meanValue"] = mean_value
        if sample_size is not UNSET:
            field_dict["sampleSize"] = sample_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        name = d.pop("name", UNSET)

        mean_value = d.pop("meanValue", UNSET)

        sample_size = d.pop("sampleSize", UNSET)

        b_request_health_check_service_update_mean_value = cls(
            ci=ci,
            name=name,
            mean_value=mean_value,
            sample_size=sample_size,
        )

        b_request_health_check_service_update_mean_value.additional_properties = d
        return b_request_health_check_service_update_mean_value

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
