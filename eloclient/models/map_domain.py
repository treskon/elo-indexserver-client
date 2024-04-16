from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapDomain")


@_attrs_define
class MapDomain:
    """This class contains the information of a map domain.
    A map is a set of key value pairs and can be
     addressed by a map domain name and a map ID. All maps with the same domain name are stored in the
     same database tables. These maps are distinguished by their ID, which can be an arbitary string.
     A map can be attached to a Sord object by setting the map ID to the Sord ID. Attached maps are
     deleted, when the Sord object is finally deleted. Furthermore they can be copied with the Sord
     object.

        Attributes:
            replicate (Union[Unset, bool]): This value is true, if the map items should be replicated with the associated
                Sord object.
            name (Union[Unset, str]): Map domain name.
                This can be a user definined name or one of the predefined names in
                 MapDomainC. The value is internally used as part of a database table name. Thus only
                 alphanumeric characters are allowed.
            copy (Union[Unset, bool]): This value is true, if the map items should be copied when the associated Sord object
                is
                copied.
            history (Union[Unset, bool]): This value is true, if a history should be maintained for map items.
                A history is always
                 available for {@link MapDomainC#DOMAIN_SORD} and {@link MapDomainC#DOMAIN_WORKFLOW_ACTIVE}.
    """

    replicate: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    copy: Union[Unset, bool] = UNSET
    history: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        replicate = self.replicate

        name = self.name

        copy = self.copy

        history = self.history

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replicate is not UNSET:
            field_dict["replicate"] = replicate
        if name is not UNSET:
            field_dict["name"] = name
        if copy is not UNSET:
            field_dict["copy"] = copy
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        replicate = d.pop("replicate", UNSET)

        name = d.pop("name", UNSET)

        copy = d.pop("copy", UNSET)

        history = d.pop("history", UNSET)

        map_domain = cls(
            replicate=replicate,
            name=name,
            copy=copy,
            history=history,
        )

        map_domain.additional_properties = d
        return map_domain

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
