from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.document import Document
    from ..models.lock_z import LockZ
    from ..models.sord import Sord
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinDocsEnd")


@_attrs_define
class BRequestIXServicePortIFCheckinDocsEnd:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        sords (Union[Unset, List['Sord']]):
        sord_zs (Union[Unset, List['SordZ']]):
        documents (Union[Unset, List['Document']]):
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    sords: Union[Unset, List["Sord"]] = UNSET
    sord_zs: Union[Unset, List["SordZ"]] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        sords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sords, Unset):
            sords = []
            for sords_item_data in self.sords:
                sords_item = sords_item_data.to_dict()

                sords.append(sords_item)

        sord_zs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sord_zs, Unset):
            sord_zs = []
            for sord_zs_item_data in self.sord_zs:
                sord_zs_item = sord_zs_item_data.to_dict()

                sord_zs.append(sord_zs_item)

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()

                documents.append(documents_item)

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if sords is not UNSET:
            field_dict["sords"] = sords
        if sord_zs is not UNSET:
            field_dict["sordZs"] = sord_zs
        if documents is not UNSET:
            field_dict["documents"] = documents
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.document import Document
        from ..models.lock_z import LockZ
        from ..models.sord import Sord
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        sords = []
        _sords = d.pop("sords", UNSET)
        for sords_item_data in _sords or []:
            sords_item = Sord.from_dict(sords_item_data)

            sords.append(sords_item)

        sord_zs = []
        _sord_zs = d.pop("sordZs", UNSET)
        for sord_zs_item_data in _sord_zs or []:
            sord_zs_item = SordZ.from_dict(sord_zs_item_data)

            sord_zs.append(sord_zs_item)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_service_port_if_checkin_docs_end = cls(
            ci=ci,
            sords=sords,
            sord_zs=sord_zs,
            documents=documents,
            unlock_z=unlock_z,
        )

        b_request_ix_service_port_if_checkin_docs_end.additional_properties = d
        return b_request_ix_service_port_if_checkin_docs_end

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
