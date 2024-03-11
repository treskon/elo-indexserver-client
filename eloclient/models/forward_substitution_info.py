from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.substitution_period import SubstitutionPeriod


T = TypeVar("T", bound="ForwardSubstitutionInfo")


@_attrs_define
class ForwardSubstitutionInfo:
    """Forward a substitution from the its current substitute to a new substitute.
    <p>
     A substitution can either be forwarded or transfered.
     </p>
     <p>
     <b>Forward a substitution</b>: The original substitution is not altered. An additional {@link Substitution} object
    is
     created by copying the original one and setting the new substitute.<br>
     <ul>
     <li>If {@link SubstitutionSettings#canBeActivatedManually} is set to <code>true</code>, an arbitrary number of
     SubstitutionPeriods (also 0) can be provided. The original ones are replaced with the new ones.
     <li>If {@link SubstitutionSettings#canBeActivatedManually} is set to <code>false</code>, all provided
     SubstitutionPeriods must be sub-periods of the original ones.
     </ul>
     Set {@link #transferSubstitution} to false to forward a substitution.
     </p>
     <p>
     <b>Transfer a substitution</b>: A new {@link Substitution} object is created by copying it from the original one,
     only replacing the {@link Substitution#substituteId} by the provided new substitute. The original substitution is
     deleted. Set {@link #transferSubstitution} to true to transfer a substitution.
     </p>

        Attributes:
            substitution_guid (Union[Unset, str]): GUID of substitution to be forwarded or transfered.
            new_substitute_id (Union[Unset, int]): <p>
                Id of the new substitute.
                 </p>
                 <p>
                 This value is ignored if {@link #newSubstituteName} is set.
                 </p>
            new_substitute_name (Union[Unset, str]): <p>
                User name of the new substitute.
                 </p>
                 <p>
                 {@link #newSubstituteId} is ignored if this member is set.
                 </p>
            substitution_periods (Union[Unset, List['SubstitutionPeriod']]):
            transfer_substitution (Union[Unset, bool]): Define if the substitution should be forwarded or transfered.
                </p>
    """

    substitution_guid: Union[Unset, str] = UNSET
    new_substitute_id: Union[Unset, int] = UNSET
    new_substitute_name: Union[Unset, str] = UNSET
    substitution_periods: Union[Unset, List["SubstitutionPeriod"]] = UNSET
    transfer_substitution: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substitution_guid = self.substitution_guid
        new_substitute_id = self.new_substitute_id
        new_substitute_name = self.new_substitute_name
        substitution_periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitution_periods, Unset):
            substitution_periods = []
            for componentsschemas_list_of_substitution_period_item_data in self.substitution_periods:
                componentsschemas_list_of_substitution_period_item = (
                    componentsschemas_list_of_substitution_period_item_data.to_dict()
                )

                substitution_periods.append(componentsschemas_list_of_substitution_period_item)

        transfer_substitution = self.transfer_substitution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substitution_guid is not UNSET:
            field_dict["substitutionGuid"] = substitution_guid
        if new_substitute_id is not UNSET:
            field_dict["newSubstituteId"] = new_substitute_id
        if new_substitute_name is not UNSET:
            field_dict["newSubstituteName"] = new_substitute_name
        if substitution_periods is not UNSET:
            field_dict["substitutionPeriods"] = substitution_periods
        if transfer_substitution is not UNSET:
            field_dict["transferSubstitution"] = transfer_substitution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.substitution_period import SubstitutionPeriod

        d = src_dict.copy()
        substitution_guid = d.pop("substitutionGuid", UNSET)

        new_substitute_id = d.pop("newSubstituteId", UNSET)

        new_substitute_name = d.pop("newSubstituteName", UNSET)

        substitution_periods = []
        _substitution_periods = d.pop("substitutionPeriods", UNSET)
        for componentsschemas_list_of_substitution_period_item_data in _substitution_periods or []:
            componentsschemas_list_of_substitution_period_item = SubstitutionPeriod.from_dict(
                componentsschemas_list_of_substitution_period_item_data
            )

            substitution_periods.append(componentsschemas_list_of_substitution_period_item)

        transfer_substitution = d.pop("transferSubstitution", UNSET)

        forward_substitution_info = cls(
            substitution_guid=substitution_guid,
            new_substitute_id=new_substitute_id,
            new_substitute_name=new_substitute_name,
            substitution_periods=substitution_periods,
            transfer_substitution=transfer_substitution,
        )

        forward_substitution_info.additional_properties = d
        return forward_substitution_info

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
