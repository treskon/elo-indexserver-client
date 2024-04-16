from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.translate_term import TranslateTerm


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinTranslateTerms")


@_attrs_define
class BRequestIXServicePortIFCheckinTranslateTerms:
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
        tterms (Union[Unset, List['TranslateTerm']]):
    """

    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    tterms: Union[Unset, List["TranslateTerm"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        tterms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tterms, Unset):
            tterms = []
            for tterms_item_data in self.tterms:
                tterms_item = tterms_item_data.to_dict()
                tterms.append(tterms_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if tterms is not UNSET:
            field_dict["tterms"] = tterms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.translate_term import TranslateTerm

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

        tterms = []
        _tterms = d.pop("tterms", UNSET)
        for tterms_item_data in _tterms or []:
            tterms_item = TranslateTerm.from_dict(tterms_item_data)

            tterms.append(tterms_item)

        b_request_ix_service_port_if_checkin_translate_terms = cls(
            unlock_z=unlock_z,
            ci=ci,
            tterms=tterms,
        )

        b_request_ix_service_port_if_checkin_translate_terms.additional_properties = d
        return b_request_ix_service_port_if_checkin_translate_terms

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
