from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubstitutionStatus")


@_attrs_define
class SubstitutionStatus:
    """The substitution status is used to inform if a substitution is currently deactivated or
    activated. If activated, it also informs how it was activated (either by a
     {@link SubstitutionPeriod} or manually)

        Attributes:
            deactivated (Union[Unset, SubstitutionStatus]): The substitution status is used to inform if a substitution is
                currently deactivated or
                activated. If activated, it also informs how it was activated (either by a
                 {@link SubstitutionPeriod} or manually)
            activated_by_period (Union[Unset, SubstitutionStatus]): The substitution status is used to inform if a
                substitution is currently deactivated or
                activated. If activated, it also informs how it was activated (either by a
                 {@link SubstitutionPeriod} or manually)
            activated_manually (Union[Unset, SubstitutionStatus]): The substitution status is used to inform if a
                substitution is currently deactivated or
                activated. If activated, it also informs how it was activated (either by a
                 {@link SubstitutionPeriod} or manually)
    """

    deactivated: Union[Unset, "SubstitutionStatus"] = UNSET
    activated_by_period: Union[Unset, "SubstitutionStatus"] = UNSET
    activated_manually: Union[Unset, "SubstitutionStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deactivated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deactivated, Unset):
            deactivated = self.deactivated.to_dict()

        activated_by_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activated_by_period, Unset):
            activated_by_period = self.activated_by_period.to_dict()

        activated_manually: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activated_manually, Unset):
            activated_manually = self.activated_manually.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deactivated is not UNSET:
            field_dict["DEACTIVATED"] = deactivated
        if activated_by_period is not UNSET:
            field_dict["ACTIVATED_BY_PERIOD"] = activated_by_period
        if activated_manually is not UNSET:
            field_dict["ACTIVATED_MANUALLY"] = activated_manually

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _deactivated = d.pop("DEACTIVATED", UNSET)
        deactivated: Union[Unset, SubstitutionStatus]
        if isinstance(_deactivated, Unset):
            deactivated = UNSET
        else:
            deactivated = SubstitutionStatus.from_dict(_deactivated)

        _activated_by_period = d.pop("ACTIVATED_BY_PERIOD", UNSET)
        activated_by_period: Union[Unset, SubstitutionStatus]
        if isinstance(_activated_by_period, Unset):
            activated_by_period = UNSET
        else:
            activated_by_period = SubstitutionStatus.from_dict(_activated_by_period)

        _activated_manually = d.pop("ACTIVATED_MANUALLY", UNSET)
        activated_manually: Union[Unset, SubstitutionStatus]
        if isinstance(_activated_manually, Unset):
            activated_manually = UNSET
        else:
            activated_manually = SubstitutionStatus.from_dict(_activated_manually)

        substitution_status = cls(
            deactivated=deactivated,
            activated_by_period=activated_by_period,
            activated_manually=activated_manually,
        )

        substitution_status.additional_properties = d
        return substitution_status

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
