from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.delete_substitutions_info import DeleteSubstitutionsInfo
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFDeleteSubstitutions")


@_attrs_define
class BRequestIXServicePortIFDeleteSubstitutions:
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
        delete_substitutions_info (Union[Unset, DeleteSubstitutionsInfo]): Define which substitutions should be deleted.
    """

    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    delete_substitutions_info: Union[Unset, "DeleteSubstitutionsInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        delete_substitutions_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete_substitutions_info, Unset):
            delete_substitutions_info = self.delete_substitutions_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if delete_substitutions_info is not UNSET:
            field_dict["deleteSubstitutionsInfo"] = delete_substitutions_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.delete_substitutions_info import DeleteSubstitutionsInfo
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

        _delete_substitutions_info = d.pop("deleteSubstitutionsInfo", UNSET)
        delete_substitutions_info: Union[Unset, DeleteSubstitutionsInfo]
        if isinstance(_delete_substitutions_info, Unset):
            delete_substitutions_info = UNSET
        else:
            delete_substitutions_info = DeleteSubstitutionsInfo.from_dict(_delete_substitutions_info)

        b_request_ix_service_port_if_delete_substitutions = cls(
            unlock_z=unlock_z,
            ci=ci,
            delete_substitutions_info=delete_substitutions_info,
        )

        b_request_ix_service_port_if_delete_substitutions.additional_properties = d
        return b_request_ix_service_port_if_delete_substitutions

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
