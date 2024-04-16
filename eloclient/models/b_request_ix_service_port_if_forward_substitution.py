from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.forward_substitution_info import ForwardSubstitutionInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFForwardSubstitution")


@_attrs_define
class BRequestIXServicePortIFForwardSubstitution:
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
        forward_substitution_info (Union[Unset, ForwardSubstitutionInfo]): Forward a substitution from the its current
            substitute to a new substitute.
            <p>
             A substitution can either be forwarded or transfered.
             </p>
             <p>
             <b>Forward a substitution</b>: The original substitution is not altered. An additional
             {@link Substitution} object is created by copying the original one and setting the new
             substitute.<br>
             <ul>
             <li>If {@link SubstitutionSettings#canBeActivatedManually} is set to <code>true</code>, an
             arbitrary number of SubstitutionPeriods (also 0) can be provided. The original ones are replaced
             with the new ones.
             <li>If {@link SubstitutionSettings#canBeActivatedManually} is set to <code>false</code>, all
             provided SubstitutionPeriods must be sub-periods of the original ones.
             </ul>
             Set {@link #transferSubstitution} to false to forward a substitution.
             </p>
             <p>
             <b>Transfer a substitution</b>: A new {@link Substitution} object is created by copying it from
             the original one, only replacing the {@link Substitution#substituteId} by the provided new
             substitute. The original substitution is deleted. Set {@link #transferSubstitution} to true to
             transfer a substitution.
             </p>
    """

    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    forward_substitution_info: Union[Unset, "ForwardSubstitutionInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        forward_substitution_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forward_substitution_info, Unset):
            forward_substitution_info = self.forward_substitution_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if forward_substitution_info is not UNSET:
            field_dict["forwardSubstitutionInfo"] = forward_substitution_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.forward_substitution_info import ForwardSubstitutionInfo
        from ..models.lock_z import LockZ

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

        _forward_substitution_info = d.pop("forwardSubstitutionInfo", UNSET)
        forward_substitution_info: Union[Unset, ForwardSubstitutionInfo]
        if isinstance(_forward_substitution_info, Unset):
            forward_substitution_info = UNSET
        else:
            forward_substitution_info = ForwardSubstitutionInfo.from_dict(_forward_substitution_info)

        b_request_ix_service_port_if_forward_substitution = cls(
            unlock_z=unlock_z,
            ci=ci,
            forward_substitution_info=forward_substitution_info,
        )

        b_request_ix_service_port_if_forward_substitution.additional_properties = d
        return b_request_ix_service_port_if_forward_substitution

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
