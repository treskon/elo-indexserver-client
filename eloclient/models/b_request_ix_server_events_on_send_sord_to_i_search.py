from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask import DocMask
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServerEventsOnSendSordToISearch")


@_attrs_define
class BRequestIXServerEventsOnSendSordToISearch:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mask (Union[Unset, DocMask]): <p>
            Contains the data for a storage mask.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        fulltext (Union[Unset, str]):
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    mask: Union[Unset, "DocMask"] = UNSET
    fulltext: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        mask: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.to_dict()

        fulltext = self.fulltext

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if sord is not UNSET:
            field_dict["sord"] = sord
        if mask is not UNSET:
            field_dict["mask"] = mask
        if fulltext is not UNSET:
            field_dict["fulltext"] = fulltext

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask import DocMask
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.sord import Sord

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        _mask = d.pop("mask", UNSET)
        mask: Union[Unset, DocMask]
        if isinstance(_mask, Unset):
            mask = UNSET
        else:
            mask = DocMask.from_dict(_mask)

        fulltext = d.pop("fulltext", UNSET)

        b_request_ix_server_events_on_send_sord_to_i_search = cls(
            ec=ec,
            sord=sord,
            mask=mask,
            fulltext=fulltext,
        )

        b_request_ix_server_events_on_send_sord_to_i_search.additional_properties = d
        return b_request_ix_server_events_on_send_sord_to_i_search

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
