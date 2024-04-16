from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.move_documents_info import MoveDocumentsInfo


T = TypeVar("T", bound="BRequestIXServicePortIFMoveDocuments")


@_attrs_define
class BRequestIXServicePortIFMoveDocuments:
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
        move_documents_info (Union[Unset, MoveDocumentsInfo]): Parameter class of the function
            {@link IXServicePortIF#moveDocuments(ClientInfo, MoveDocumentsInfo)}.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    move_documents_info: Union[Unset, "MoveDocumentsInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        move_documents_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.move_documents_info, Unset):
            move_documents_info = self.move_documents_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if move_documents_info is not UNSET:
            field_dict["moveDocumentsInfo"] = move_documents_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.move_documents_info import MoveDocumentsInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _move_documents_info = d.pop("moveDocumentsInfo", UNSET)
        move_documents_info: Union[Unset, MoveDocumentsInfo]
        if isinstance(_move_documents_info, Unset):
            move_documents_info = UNSET
        else:
            move_documents_info = MoveDocumentsInfo.from_dict(_move_documents_info)

        b_request_ix_service_port_if_move_documents = cls(
            ci=ci,
            move_documents_info=move_documents_info,
        )

        b_request_ix_service_port_if_move_documents.additional_properties = d
        return b_request_ix_service_port_if_move_documents

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
