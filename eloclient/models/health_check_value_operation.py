from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheckValueOperation")


@_attrs_define
class HealthCheckValueOperation:
    """Defines the operation to process when updating a value.

    Attributes:
        compute_add (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a value.
        compute_maximum (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a
            value.
        compute_minimum (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a
            value.
        update_value (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a value.
        compute_mean (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a value.
    """

    compute_add: Union[Unset, "HealthCheckValueOperation"] = UNSET
    compute_maximum: Union[Unset, "HealthCheckValueOperation"] = UNSET
    compute_minimum: Union[Unset, "HealthCheckValueOperation"] = UNSET
    update_value: Union[Unset, "HealthCheckValueOperation"] = UNSET
    compute_mean: Union[Unset, "HealthCheckValueOperation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compute_add: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_add, Unset):
            compute_add = self.compute_add.to_dict()

        compute_maximum: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_maximum, Unset):
            compute_maximum = self.compute_maximum.to_dict()

        compute_minimum: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_minimum, Unset):
            compute_minimum = self.compute_minimum.to_dict()

        update_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_value, Unset):
            update_value = self.update_value.to_dict()

        compute_mean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_mean, Unset):
            compute_mean = self.compute_mean.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute_add is not UNSET:
            field_dict["COMPUTE_ADD"] = compute_add
        if compute_maximum is not UNSET:
            field_dict["COMPUTE_MAXIMUM"] = compute_maximum
        if compute_minimum is not UNSET:
            field_dict["COMPUTE_MINIMUM"] = compute_minimum
        if update_value is not UNSET:
            field_dict["UPDATE_VALUE"] = update_value
        if compute_mean is not UNSET:
            field_dict["COMPUTE_MEAN"] = compute_mean

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _compute_add = d.pop("COMPUTE_ADD", UNSET)
        compute_add: Union[Unset, HealthCheckValueOperation]
        if isinstance(_compute_add, Unset):
            compute_add = UNSET
        else:
            compute_add = HealthCheckValueOperation.from_dict(_compute_add)

        _compute_maximum = d.pop("COMPUTE_MAXIMUM", UNSET)
        compute_maximum: Union[Unset, HealthCheckValueOperation]
        if isinstance(_compute_maximum, Unset):
            compute_maximum = UNSET
        else:
            compute_maximum = HealthCheckValueOperation.from_dict(_compute_maximum)

        _compute_minimum = d.pop("COMPUTE_MINIMUM", UNSET)
        compute_minimum: Union[Unset, HealthCheckValueOperation]
        if isinstance(_compute_minimum, Unset):
            compute_minimum = UNSET
        else:
            compute_minimum = HealthCheckValueOperation.from_dict(_compute_minimum)

        _update_value = d.pop("UPDATE_VALUE", UNSET)
        update_value: Union[Unset, HealthCheckValueOperation]
        if isinstance(_update_value, Unset):
            update_value = UNSET
        else:
            update_value = HealthCheckValueOperation.from_dict(_update_value)

        _compute_mean = d.pop("COMPUTE_MEAN", UNSET)
        compute_mean: Union[Unset, HealthCheckValueOperation]
        if isinstance(_compute_mean, Unset):
            compute_mean = UNSET
        else:
            compute_mean = HealthCheckValueOperation.from_dict(_compute_mean)

        health_check_value_operation = cls(
            compute_add=compute_add,
            compute_maximum=compute_maximum,
            compute_minimum=compute_minimum,
            update_value=update_value,
            compute_mean=compute_mean,
        )

        health_check_value_operation.additional_properties = d
        return health_check_value_operation

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
