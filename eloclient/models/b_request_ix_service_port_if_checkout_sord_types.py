from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.sord_type_z import SordTypeZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutSordTypes")


@_attrs_define
class BRequestIXServicePortIFCheckoutSordTypes:
    """
    Attributes:
        sord_type_z (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        sord_type_ids (Union[Unset, List[int]]):
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
    """

    sord_type_z: Union[Unset, "SordTypeZ"] = UNSET
    sord_type_ids: Union[Unset, List[int]] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sord_type_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_type_z, Unset):
            sord_type_z = self.sord_type_z.to_dict()

        sord_type_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.sord_type_ids, Unset):
            sord_type_ids = self.sord_type_ids

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sord_type_z is not UNSET:
            field_dict["sordTypeZ"] = sord_type_z
        if sord_type_ids is not UNSET:
            field_dict["sordTypeIds"] = sord_type_ids
        if ci is not UNSET:
            field_dict["ci"] = ci
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.sord_type_z import SordTypeZ

        d = src_dict.copy()
        _sord_type_z = d.pop("sordTypeZ", UNSET)
        sord_type_z: Union[Unset, SordTypeZ]
        if isinstance(_sord_type_z, Unset):
            sord_type_z = UNSET
        else:
            sord_type_z = SordTypeZ.from_dict(_sord_type_z)

        sord_type_ids = cast(List[int], d.pop("sordTypeIds", UNSET))

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

        b_request_ix_service_port_if_checkout_sord_types = cls(
            sord_type_z=sord_type_z,
            sord_type_ids=sord_type_ids,
            ci=ci,
            lock_z=lock_z,
        )

        b_request_ix_service_port_if_checkout_sord_types.additional_properties = d
        return b_request_ix_service_port_if_checkout_sord_types

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
