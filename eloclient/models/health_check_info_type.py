from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheckInfoType")


@_attrs_define
class HealthCheckInfoType:
    """Defines the type of the HealthCheck values. Depending on the type the evaluation differs.
    Either
     MMA, CNT or MSG.

        Attributes:
            mma (Union[Unset, HealthCheckInfoType]): Defines the type of the HealthCheck values. Depending on the type the
                evaluation differs.
                Either
                 MMA, CNT or MSG.
            msg (Union[Unset, HealthCheckInfoType]): Defines the type of the HealthCheck values. Depending on the type the
                evaluation differs.
                Either
                 MMA, CNT or MSG.
            cnt (Union[Unset, HealthCheckInfoType]): Defines the type of the HealthCheck values. Depending on the type the
                evaluation differs.
                Either
                 MMA, CNT or MSG.
    """

    mma: Union[Unset, "HealthCheckInfoType"] = UNSET
    msg: Union[Unset, "HealthCheckInfoType"] = UNSET
    cnt: Union[Unset, "HealthCheckInfoType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mma: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mma, Unset):
            mma = self.mma.to_dict()

        msg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.msg, Unset):
            msg = self.msg.to_dict()

        cnt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cnt, Unset):
            cnt = self.cnt.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mma is not UNSET:
            field_dict["MMA"] = mma
        if msg is not UNSET:
            field_dict["MSG"] = msg
        if cnt is not UNSET:
            field_dict["CNT"] = cnt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _mma = d.pop("MMA", UNSET)
        mma: Union[Unset, HealthCheckInfoType]
        if isinstance(_mma, Unset):
            mma = UNSET
        else:
            mma = HealthCheckInfoType.from_dict(_mma)

        _msg = d.pop("MSG", UNSET)
        msg: Union[Unset, HealthCheckInfoType]
        if isinstance(_msg, Unset):
            msg = UNSET
        else:
            msg = HealthCheckInfoType.from_dict(_msg)

        _cnt = d.pop("CNT", UNSET)
        cnt: Union[Unset, HealthCheckInfoType]
        if isinstance(_cnt, Unset):
            cnt = UNSET
        else:
            cnt = HealthCheckInfoType.from_dict(_cnt)

        health_check_info_type = cls(
            mma=mma,
            msg=msg,
            cnt=cnt,
        )

        health_check_info_type.additional_properties = d
        return health_check_info_type

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
