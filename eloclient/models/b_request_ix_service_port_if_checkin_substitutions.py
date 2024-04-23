from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_substitutions_info import CheckinSubstitutionsInfo
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.substitution_z import SubstitutionZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinSubstitutions")


@_attrs_define
class BRequestIXServicePortIFCheckinSubstitutions:
    """
    Attributes:
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
        checkin_substitutions_info (Union[Unset, CheckinSubstitutionsInfo]): Object to define substitutions to be
            checked in.
            <p>
             Substitutions which do not have a {@link Substitution#guid} are new substitutions. If a
             {@link Substitution#guid} is set, the corresponding substitution is updated.
             </p>
        substitution_z (Union[Unset, SubstitutionZ]): This class encapsulates the constants of {@link SubstitutionC}
    """

    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    checkin_substitutions_info: Union[Unset, "CheckinSubstitutionsInfo"] = UNSET
    substitution_z: Union[Unset, "SubstitutionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        checkin_substitutions_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkin_substitutions_info, Unset):
            checkin_substitutions_info = self.checkin_substitutions_info.to_dict()

        substitution_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.substitution_z, Unset):
            substitution_z = self.substitution_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if checkin_substitutions_info is not UNSET:
            field_dict["checkinSubstitutionsInfo"] = checkin_substitutions_info
        if substitution_z is not UNSET:
            field_dict["substitutionZ"] = substitution_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_substitutions_info import CheckinSubstitutionsInfo
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.substitution_z import SubstitutionZ

        d = src_dict.copy()
        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _checkin_substitutions_info = d.pop("checkinSubstitutionsInfo", UNSET)
        checkin_substitutions_info: Union[Unset, CheckinSubstitutionsInfo]
        if isinstance(_checkin_substitutions_info, Unset):
            checkin_substitutions_info = UNSET
        else:
            checkin_substitutions_info = CheckinSubstitutionsInfo.from_dict(_checkin_substitutions_info)

        _substitution_z = d.pop("substitutionZ", UNSET)
        substitution_z: Union[Unset, SubstitutionZ]
        if isinstance(_substitution_z, Unset):
            substitution_z = UNSET
        else:
            substitution_z = SubstitutionZ.from_dict(_substitution_z)

        b_request_ix_service_port_if_checkin_substitutions = cls(
            unlock_z=unlock_z,
            ci=ci,
            checkin_substitutions_info=checkin_substitutions_info,
            substitution_z=substitution_z,
        )

        b_request_ix_service_port_if_checkin_substitutions.additional_properties = d
        return b_request_ix_service_port_if_checkin_substitutions

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
