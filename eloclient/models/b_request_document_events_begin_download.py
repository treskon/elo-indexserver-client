from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.up_download_event_info import UpDownloadEventInfo


T = TypeVar("T", bound="BRequestDocumentEventsBeginDownload")


@_attrs_define
class BRequestDocumentEventsBeginDownload:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        rw_info (Union[Unset, UpDownloadEventInfo]): This class describes a document stream (version, attachment,
            preview, fulltext, signature) being uploaded or
            downloaded in an event of {@link DocumentEvents}.
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    rw_info: Union[Unset, "UpDownloadEventInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        rw_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rw_info, Unset):
            rw_info = self.rw_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if rw_info is not UNSET:
            field_dict["rwInfo"] = rw_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.up_download_event_info import UpDownloadEventInfo

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _rw_info = d.pop("rwInfo", UNSET)
        rw_info: Union[Unset, UpDownloadEventInfo]
        if isinstance(_rw_info, Unset):
            rw_info = UNSET
        else:
            rw_info = UpDownloadEventInfo.from_dict(_rw_info)

        b_request_document_events_begin_download = cls(
            ec=ec,
            rw_info=rw_info,
        )

        b_request_document_events_begin_download.additional_properties = d
        return b_request_document_events_begin_download

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
