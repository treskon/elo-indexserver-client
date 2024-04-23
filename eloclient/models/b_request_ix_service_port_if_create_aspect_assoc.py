from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cardinality import Cardinality
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCreateAspectAssoc")


@_attrs_define
class BRequestIXServicePortIFCreateAspectAssoc:
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
        aspect_id (Union[Unset, str]):
        cardinality (Union[Unset, Cardinality]): Aspect cardinality.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    name: Union[Unset, str] = UNSET
    aspect_id: Union[Unset, str] = UNSET
    cardinality: Union[Unset, "Cardinality"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        name = self.name

        aspect_id = self.aspect_id

        cardinality: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cardinality, Unset):
            cardinality = self.cardinality.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if name is not UNSET:
            field_dict["name"] = name
        if aspect_id is not UNSET:
            field_dict["aspectId"] = aspect_id
        if cardinality is not UNSET:
            field_dict["cardinality"] = cardinality

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cardinality import Cardinality
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        name = d.pop("name", UNSET)

        aspect_id = d.pop("aspectId", UNSET)

        _cardinality = d.pop("cardinality", UNSET)
        cardinality: Union[Unset, Cardinality]
        if isinstance(_cardinality, Unset):
            cardinality = UNSET
        else:
            cardinality = Cardinality.from_dict(_cardinality)

        b_request_ix_service_port_if_create_aspect_assoc = cls(
            ci=ci,
            name=name,
            aspect_id=aspect_id,
            cardinality=cardinality,
        )

        b_request_ix_service_port_if_create_aspect_assoc.additional_properties = d
        return b_request_ix_service_port_if_create_aspect_assoc

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
