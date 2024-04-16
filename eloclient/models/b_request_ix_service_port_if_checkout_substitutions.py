from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_substitutions_info import CheckoutSubstitutionsInfo
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.substitution_z import SubstitutionZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutSubstitutions")


@_attrs_define
class BRequestIXServicePortIFCheckoutSubstitutions:
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
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        checkout_substitutions_info (Union[Unset, CheckoutSubstitutionsInfo]): This object is used to define which
            substitutions should be returned by
            {@link IXServicePortIF#checkoutSubstitutions}.

             <p>
             The elements in one list are always search with an OR operation. If various list are provided,
             they are connected using OR (default) (set {@link #andOperator} to true to use AND operator)
             </p>
        substitution_z (Union[Unset, SubstitutionZ]): This class encapsulates the constants of {@link SubstitutionC}
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    checkout_substitutions_info: Union[Unset, "CheckoutSubstitutionsInfo"] = UNSET
    substitution_z: Union[Unset, "SubstitutionZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        checkout_substitutions_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_substitutions_info, Unset):
            checkout_substitutions_info = self.checkout_substitutions_info.to_dict()

        substitution_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.substitution_z, Unset):
            substitution_z = self.substitution_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if checkout_substitutions_info is not UNSET:
            field_dict["checkoutSubstitutionsInfo"] = checkout_substitutions_info
        if substitution_z is not UNSET:
            field_dict["substitutionZ"] = substitution_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_substitutions_info import CheckoutSubstitutionsInfo
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.substitution_z import SubstitutionZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        _checkout_substitutions_info = d.pop("checkoutSubstitutionsInfo", UNSET)
        checkout_substitutions_info: Union[Unset, CheckoutSubstitutionsInfo]
        if isinstance(_checkout_substitutions_info, Unset):
            checkout_substitutions_info = UNSET
        else:
            checkout_substitutions_info = CheckoutSubstitutionsInfo.from_dict(_checkout_substitutions_info)

        _substitution_z = d.pop("substitutionZ", UNSET)
        substitution_z: Union[Unset, SubstitutionZ]
        if isinstance(_substitution_z, Unset):
            substitution_z = UNSET
        else:
            substitution_z = SubstitutionZ.from_dict(_substitution_z)

        b_request_ix_service_port_if_checkout_substitutions = cls(
            ci=ci,
            lock_z=lock_z,
            checkout_substitutions_info=checkout_substitutions_info,
            substitution_z=substitution_z,
        )

        b_request_ix_service_port_if_checkout_substitutions.additional_properties = d
        return b_request_ix_service_port_if_checkout_substitutions

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
