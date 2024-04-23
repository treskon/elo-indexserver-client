from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Cardinality")


@_attrs_define
class Cardinality:
    """Aspect cardinality.

    Attributes:
        optional (Union[Unset, Cardinality]): Aspect cardinality.
        optional_many (Union[Unset, Cardinality]): Aspect cardinality.
        mandatory (Union[Unset, Cardinality]): Aspect cardinality.
        mandatory_many (Union[Unset, Cardinality]): Aspect cardinality.
    """

    optional: Union[Unset, "Cardinality"] = UNSET
    optional_many: Union[Unset, "Cardinality"] = UNSET
    mandatory: Union[Unset, "Cardinality"] = UNSET
    mandatory_many: Union[Unset, "Cardinality"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        optional: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.optional, Unset):
            optional = self.optional.to_dict()

        optional_many: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.optional_many, Unset):
            optional_many = self.optional_many.to_dict()

        mandatory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mandatory, Unset):
            mandatory = self.mandatory.to_dict()

        mandatory_many: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mandatory_many, Unset):
            mandatory_many = self.mandatory_many.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if optional is not UNSET:
            field_dict["OPTIONAL"] = optional
        if optional_many is not UNSET:
            field_dict["OPTIONAL_MANY"] = optional_many
        if mandatory is not UNSET:
            field_dict["MANDATORY"] = mandatory
        if mandatory_many is not UNSET:
            field_dict["MANDATORY_MANY"] = mandatory_many

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _optional = d.pop("OPTIONAL", UNSET)
        optional: Union[Unset, Cardinality]
        if isinstance(_optional, Unset):
            optional = UNSET
        else:
            optional = Cardinality.from_dict(_optional)

        _optional_many = d.pop("OPTIONAL_MANY", UNSET)
        optional_many: Union[Unset, Cardinality]
        if isinstance(_optional_many, Unset):
            optional_many = UNSET
        else:
            optional_many = Cardinality.from_dict(_optional_many)

        _mandatory = d.pop("MANDATORY", UNSET)
        mandatory: Union[Unset, Cardinality]
        if isinstance(_mandatory, Unset):
            mandatory = UNSET
        else:
            mandatory = Cardinality.from_dict(_mandatory)

        _mandatory_many = d.pop("MANDATORY_MANY", UNSET)
        mandatory_many: Union[Unset, Cardinality]
        if isinstance(_mandatory_many, Unset):
            mandatory_many = UNSET
        else:
            mandatory_many = Cardinality.from_dict(_mandatory_many)

        cardinality = cls(
            optional=optional,
            optional_many=optional_many,
            mandatory=mandatory,
            mandatory_many=mandatory_many,
        )

        cardinality.additional_properties = d
        return cardinality

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
