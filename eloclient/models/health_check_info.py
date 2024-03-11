from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_check_info_type import HealthCheckInfoType
    from ..models.health_check_value_operation import HealthCheckValueOperation


T = TypeVar("T", bound="HealthCheckInfo")


@_attrs_define
class HealthCheckInfo:
    """This class represents one value for health check evaluation.

    Attributes:
        name (Union[Unset, str]): Value name.
        time_stamp (Union[Unset, str]):
        string_value (Union[Unset, str]): String value. Either this or {@link #doubleValue} has to be set.
        double_value (Union[Unset, float]): Numeric value. Either this value or {@link #stringValue} has to be set.
        sample_size (Union[Unset, str]): Sample size for mean values.
            If {@link #doubleValue} is a arithmetic mean, this value gives the number of the
             underlying samples. If {@link #stringValue} is set, this value has to be 0.
        min_value (Union[Unset, str]): Minimaler Wert für mean values.
            <p>
             EIX-1408
             </p>
        max_value (Union[Unset, str]): Maximaler Wert für mean values.
            <p>
             EIX-1408
             </p>
        operation (Union[Unset, HealthCheckValueOperation]): Defines the operation to process when updating a value.
        type (Union[Unset, HealthCheckInfoType]): Defines the type of the HealthCheck values. Depending on the type the
            evaluation differs. Either MMA, CNT or MSG.
    """

    name: Union[Unset, str] = UNSET
    time_stamp: Union[Unset, str] = UNSET
    string_value: Union[Unset, str] = UNSET
    double_value: Union[Unset, float] = UNSET
    sample_size: Union[Unset, str] = UNSET
    min_value: Union[Unset, str] = UNSET
    max_value: Union[Unset, str] = UNSET
    operation: Union[Unset, "HealthCheckValueOperation"] = UNSET
    type: Union[Unset, "HealthCheckInfoType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        time_stamp = self.time_stamp
        string_value = self.string_value
        double_value = self.double_value
        sample_size = self.sample_size
        min_value = self.min_value
        max_value = self.max_value
        operation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if sample_size is not UNSET:
            field_dict["sampleSize"] = sample_size
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if operation is not UNSET:
            field_dict["operation"] = operation
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.health_check_info_type import HealthCheckInfoType
        from ..models.health_check_value_operation import HealthCheckValueOperation

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        time_stamp = d.pop("timeStamp", UNSET)

        string_value = d.pop("stringValue", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        sample_size = d.pop("sampleSize", UNSET)

        min_value = d.pop("minValue", UNSET)

        max_value = d.pop("maxValue", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, HealthCheckValueOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = HealthCheckValueOperation.from_dict(_operation)

        _type = d.pop("type", UNSET)
        type: Union[Unset, HealthCheckInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = HealthCheckInfoType.from_dict(_type)

        health_check_info = cls(
            name=name,
            time_stamp=time_stamp,
            string_value=string_value,
            double_value=double_value,
            sample_size=sample_size,
            min_value=min_value,
            max_value=max_value,
            operation=operation,
            type=type,
        )

        health_check_info.additional_properties = d
        return health_check_info

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
