from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkin_doc_options import CheckinDocOptions
    from ..models.client_info import ClientInfo
    from ..models.document import Document
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinDocBegin2")


@_attrs_define
class BRequestIXServicePortIFCheckinDocBegin2:
    """
    Attributes:
        opts (Union[Unset, CheckinDocOptions]): This class defines options for the API function checkinDocBegin2.
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
        document (Union[Unset, Document]): Document object with identifier and version arrays for the document and
            attachments.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    opts: Union[Unset, "CheckinDocOptions"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    document: Union[Unset, "Document"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opts, Unset):
            opts = self.opts.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opts is not UNSET:
            field_dict["opts"] = opts
        if ci is not UNSET:
            field_dict["ci"] = ci
        if document is not UNSET:
            field_dict["document"] = document
        if sord is not UNSET:
            field_dict["sord"] = sord

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkin_doc_options import CheckinDocOptions
        from ..models.client_info import ClientInfo
        from ..models.document import Document
        from ..models.sord import Sord

        d = src_dict.copy()
        _opts = d.pop("opts", UNSET)
        opts: Union[Unset, CheckinDocOptions]
        if isinstance(_opts, Unset):
            opts = UNSET
        else:
            opts = CheckinDocOptions.from_dict(_opts)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _document = d.pop("document", UNSET)
        document: Union[Unset, Document]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = Document.from_dict(_document)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        b_request_ix_service_port_if_checkin_doc_begin_2 = cls(
            opts=opts,
            ci=ci,
            document=document,
            sord=sord,
        )

        b_request_ix_service_port_if_checkin_doc_begin_2.additional_properties = d
        return b_request_ix_service_port_if_checkin_doc_begin_2

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
