from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SordHistC")


@_attrs_define
class SordHistC:
    """Constanst for class SordHist.

    Attributes:
        src_igw (Union[Unset, int]): History entry created by ELO Internet Gateway.
        src_sync (Union[Unset, int]): History entry created by ELO Archive Synchronisation.
        src_ole (Union[Unset, int]): History entry created by ELO Automation Interface.
        src_xml (Union[Unset, int]): History entry created by ELO XML Importer
        src_none (Union[Unset, int]): History entry created by unknown program.
        src_sap (Union[Unset, int]): History entry created by ELO SAPALINK.
        src_client (Union[Unset, int]): History entry created by ELO Windows Client.
        src_repl (Union[Unset, int]): History entry created by ELO Replication.
        src_ix (Union[Unset, int]): History entry created by Indexserver.
    """

    src_igw: Union[Unset, int] = UNSET
    src_sync: Union[Unset, int] = UNSET
    src_ole: Union[Unset, int] = UNSET
    src_xml: Union[Unset, int] = UNSET
    src_none: Union[Unset, int] = UNSET
    src_sap: Union[Unset, int] = UNSET
    src_client: Union[Unset, int] = UNSET
    src_repl: Union[Unset, int] = UNSET
    src_ix: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        src_igw = self.src_igw

        src_sync = self.src_sync

        src_ole = self.src_ole

        src_xml = self.src_xml

        src_none = self.src_none

        src_sap = self.src_sap

        src_client = self.src_client

        src_repl = self.src_repl

        src_ix = self.src_ix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if src_igw is not UNSET:
            field_dict["SRC_IGW"] = src_igw
        if src_sync is not UNSET:
            field_dict["SRC_SYNC"] = src_sync
        if src_ole is not UNSET:
            field_dict["SRC_OLE"] = src_ole
        if src_xml is not UNSET:
            field_dict["SRC_XML"] = src_xml
        if src_none is not UNSET:
            field_dict["SRC_NONE"] = src_none
        if src_sap is not UNSET:
            field_dict["SRC_SAP"] = src_sap
        if src_client is not UNSET:
            field_dict["SRC_CLIENT"] = src_client
        if src_repl is not UNSET:
            field_dict["SRC_REPL"] = src_repl
        if src_ix is not UNSET:
            field_dict["SRC_IX"] = src_ix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        src_igw = d.pop("SRC_IGW", UNSET)

        src_sync = d.pop("SRC_SYNC", UNSET)

        src_ole = d.pop("SRC_OLE", UNSET)

        src_xml = d.pop("SRC_XML", UNSET)

        src_none = d.pop("SRC_NONE", UNSET)

        src_sap = d.pop("SRC_SAP", UNSET)

        src_client = d.pop("SRC_CLIENT", UNSET)

        src_repl = d.pop("SRC_REPL", UNSET)

        src_ix = d.pop("SRC_IX", UNSET)

        sord_hist_c = cls(
            src_igw=src_igw,
            src_sync=src_sync,
            src_ole=src_ole,
            src_xml=src_xml,
            src_none=src_none,
            src_sap=src_sap,
            src_client=src_client,
            src_repl=src_repl,
            src_ix=src_ix,
        )

        sord_hist_c.additional_properties = d
        return sord_hist_c

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
