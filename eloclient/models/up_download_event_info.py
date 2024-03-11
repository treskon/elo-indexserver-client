from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord import Sord
    from ..models.up_download_kind import UpDownloadKind
    from ..models.up_download_usage import UpDownloadUsage


T = TypeVar("T", bound="UpDownloadEventInfo")


@_attrs_define
class UpDownloadEventInfo:
    """This class describes a document stream (version, attachment, preview, fulltext, signature) being uploaded or
    downloaded in an event of {@link DocumentEvents}.

        Attributes:
            kind (Union[Unset, UpDownloadKind]): This enum defines constants to distinguish between different kinds of file
                data assigned to a document.
            usage (Union[Unset, UpDownloadUsage]): This enumeration defines constants that describe, from where an event in
                {@link DocumentEvents} is called.
            sord (Union[Unset, Sord]): <p>
                Indexing information of an archive entry.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            doc_id (Union[Unset, int]): Document version ID.
                Only valid for
                 {@link DocumentEvents#beginDownload(de.elo.ix.client.IXServerEventsContext, UpDownloadEventInfo)}.
            offset (Union[Unset, str]): Document related stream should be downloaded starting at this position.
                Only valid for
                 {@link DocumentEvents#beginDownload(de.elo.ix.client.IXServerEventsContext, UpDownloadEventInfo)}. If the
                entire
                 stream should be read, {@link #offset} is 0 and {@link #length} is -1.
            length (Union[Unset, str]): Number of bytes to download from a document related stream.
                Only valid for
                 {@link DocumentEvents#beginDownload(de.elo.ix.client.IXServerEventsContext, UpDownloadEventInfo)}. If this
                element
                 is -1, read up to the end of the stream. If the entire stream should be read, {@link #offset} is 0 and
                 {@link #length} is -1.
            preliminary_test (Union[Unset, bool]): A preliminary test for a later uploaded stream.
                While uploading a content stream for a new document via
                 {@link de.elo.ix.client.IXConnectionIF#upload(String, java.io.File)} to the server, the related Sord object is
                 unknown. So the information that usually controls, whether a document processor shall handle the stream is
                 unavailable. To solve this situation, the uploaded stream is stored temporarily and the actual upload is
                deferred
                 to the function {@link de.elo.ix.client.IXServicePortIF#checkinDocEnd}. In order to know whether a stream
                should be
                 temporarily stored, function {@link de.elo.ix.client.IXServicePortIF#checkinDocBegin2} calls the event
                 {@link DocumentEvents#beginUpload}. The returned document processor is only checked to be non-null but is never
                 invoked. The document processor used to process the stream is requested in {@link
                IXServicePortIF#checkinDocEnd}.
    """

    kind: Union[Unset, "UpDownloadKind"] = UNSET
    usage: Union[Unset, "UpDownloadUsage"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    doc_id: Union[Unset, int] = UNSET
    offset: Union[Unset, str] = UNSET
    length: Union[Unset, str] = UNSET
    preliminary_test: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.to_dict()

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        doc_id = self.doc_id
        offset = self.offset
        length = self.length
        preliminary_test = self.preliminary_test

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if usage is not UNSET:
            field_dict["usage"] = usage
        if sord is not UNSET:
            field_dict["sord"] = sord
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if offset is not UNSET:
            field_dict["offset"] = offset
        if length is not UNSET:
            field_dict["length"] = length
        if preliminary_test is not UNSET:
            field_dict["preliminaryTest"] = preliminary_test

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord import Sord
        from ..models.up_download_kind import UpDownloadKind
        from ..models.up_download_usage import UpDownloadUsage

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, UpDownloadKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = UpDownloadKind.from_dict(_kind)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, UpDownloadUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = UpDownloadUsage.from_dict(_usage)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        doc_id = d.pop("docId", UNSET)

        offset = d.pop("offset", UNSET)

        length = d.pop("length", UNSET)

        preliminary_test = d.pop("preliminaryTest", UNSET)

        up_download_event_info = cls(
            kind=kind,
            usage=usage,
            sord=sord,
            doc_id=doc_id,
            offset=offset,
            length=length,
            preliminary_test=preliminary_test,
        )

        up_download_event_info.additional_properties = d
        return up_download_event_info

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
