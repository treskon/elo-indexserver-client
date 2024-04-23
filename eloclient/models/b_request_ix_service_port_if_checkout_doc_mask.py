from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.doc_mask_z import DocMaskZ
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutDocMask")


@_attrs_define
class BRequestIXServicePortIFCheckoutDocMask:
    """
    Attributes:
        doc_mask_z (Union[Unset, DocMaskZ]): This class encapsulates the constants of the DocMaskC class.
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
        mask_id (Union[Unset, str]):
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    doc_mask_z: Union[Unset, "DocMaskZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    mask_id: Union[Unset, str] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_mask_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask_z, Unset):
            doc_mask_z = self.doc_mask_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        mask_id = self.mask_id

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_mask_z is not UNSET:
            field_dict["docMaskZ"] = doc_mask_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if mask_id is not UNSET:
            field_dict["maskId"] = mask_id
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.doc_mask_z import DocMaskZ
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _doc_mask_z = d.pop("docMaskZ", UNSET)
        doc_mask_z: Union[Unset, DocMaskZ]
        if isinstance(_doc_mask_z, Unset):
            doc_mask_z = UNSET
        else:
            doc_mask_z = DocMaskZ.from_dict(_doc_mask_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        mask_id = d.pop("maskId", UNSET)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        b_request_ix_service_port_if_checkout_doc_mask = cls(
            doc_mask_z=doc_mask_z,
            ci=ci,
            mask_id=mask_id,
            lock_z=lock_z,
        )

        b_request_ix_service_port_if_checkout_doc_mask.additional_properties = d
        return b_request_ix_service_port_if_checkout_doc_mask

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
