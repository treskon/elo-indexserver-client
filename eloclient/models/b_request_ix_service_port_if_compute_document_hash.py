from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.compute_document_hash_info import ComputeDocumentHashInfo


T = TypeVar("T", bound="BRequestIXServicePortIFComputeDocumentHash")


@_attrs_define
class BRequestIXServicePortIFComputeDocumentHash:
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
        compute_info (Union[Unset, ComputeDocumentHashInfo]): This class defines the parameters for computing a document
            file hash by
            {@link IXServicePortIF#computeDocumentHash(ClientInfo, ComputeDocumentHashInfo)}.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    compute_info: Union[Unset, "ComputeDocumentHashInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        compute_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_info, Unset):
            compute_info = self.compute_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if compute_info is not UNSET:
            field_dict["computeInfo"] = compute_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.compute_document_hash_info import ComputeDocumentHashInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _compute_info = d.pop("computeInfo", UNSET)
        compute_info: Union[Unset, ComputeDocumentHashInfo]
        if isinstance(_compute_info, Unset):
            compute_info = UNSET
        else:
            compute_info = ComputeDocumentHashInfo.from_dict(_compute_info)

        b_request_ix_service_port_if_compute_document_hash = cls(
            ci=ci,
            compute_info=compute_info,
        )

        b_request_ix_service_port_if_compute_document_hash.additional_properties = d
        return b_request_ix_service_port_if_compute_document_hash

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
