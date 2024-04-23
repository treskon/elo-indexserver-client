from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.doc_mask import DocMask
    from ..models.doc_mask_z import DocMaskZ
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinDocMask")


@_attrs_define
class BRequestIXServicePortIFCheckinDocMask:
    """
    Attributes:
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        doc_mask (Union[Unset, DocMask]): <p>
            Contains the data for a storage mask.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
    """

    unlock_z: Union[Unset, "LockZ"] = UNSET
    doc_mask: Union[Unset, "DocMask"] = UNSET
    doc_mask_z: Union[Unset, "DocMaskZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        doc_mask: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask, Unset):
            doc_mask = self.doc_mask.to_dict()

        doc_mask_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask_z, Unset):
            doc_mask_z = self.doc_mask_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if doc_mask is not UNSET:
            field_dict["docMask"] = doc_mask
        if doc_mask_z is not UNSET:
            field_dict["docMaskZ"] = doc_mask_z
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.doc_mask import DocMask
        from ..models.doc_mask_z import DocMaskZ
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _doc_mask = d.pop("docMask", UNSET)
        doc_mask: Union[Unset, DocMask]
        if isinstance(_doc_mask, Unset):
            doc_mask = UNSET
        else:
            doc_mask = DocMask.from_dict(_doc_mask)

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

        b_request_ix_service_port_if_checkin_doc_mask = cls(
            unlock_z=unlock_z,
            doc_mask=doc_mask,
            doc_mask_z=doc_mask_z,
            ci=ci,
        )

        b_request_ix_service_port_if_checkin_doc_mask.additional_properties = d
        return b_request_ix_service_port_if_checkin_doc_mask

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
