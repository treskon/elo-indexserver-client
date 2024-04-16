from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.delete_options import DeleteOptions
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFDeleteSord")


@_attrs_define
class BRequestIXServicePortIFDeleteSord:
    """
    Attributes:
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        delete_options (Union[Unset, DeleteOptions]): This class contains options for deleting archive SORDs using the
            deleteSord function.
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
        obj_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
    """

    unlock_z: Union[Unset, "LockZ"] = UNSET
    delete_options: Union[Unset, "DeleteOptions"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    obj_id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        delete_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete_options, Unset):
            delete_options = self.delete_options.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        obj_id = self.obj_id

        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if delete_options is not UNSET:
            field_dict["deleteOptions"] = delete_options
        if ci is not UNSET:
            field_dict["ci"] = ci
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.delete_options import DeleteOptions
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _delete_options = d.pop("deleteOptions", UNSET)
        delete_options: Union[Unset, DeleteOptions]
        if isinstance(_delete_options, Unset):
            delete_options = UNSET
        else:
            delete_options = DeleteOptions.from_dict(_delete_options)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        obj_id = d.pop("objId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        b_request_ix_service_port_if_delete_sord = cls(
            unlock_z=unlock_z,
            delete_options=delete_options,
            ci=ci,
            obj_id=obj_id,
            parent_id=parent_id,
        )

        b_request_ix_service_port_if_delete_sord.additional_properties = d
        return b_request_ix_service_port_if_delete_sord

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
