from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocHistory")


@_attrs_define
class DocHistory:
    """Document version data, e. g.
    document version ID and GUID, version comment, MD5 hash of document
     file. Internal use only.

        Attributes:
            doc_id (Union[Unset, int]): Document version ID.
                DB column: documentid
            doc_md5 (Union[Unset, str]): The MD5 hash of the document file.
                DB column: docmd5
            flags (Union[Unset, int]): MFG_BURNIN DB column: docflags
            sig_id (Union[Unset, int]): Document signature ID.
                DB column: docsignature
            language (Union[Unset, str]): Language of the document content.
                This value is estimated by ELO Textreader when the document is sent for fulltext extraction.
                 See {@link TranslateTermC#DEFAULT_LANGUAGES} for a list of language-tags.
            type (Union[Unset, int]): The type of this DocHistory makes the difference between attachments and document
                versions.
            version (Union[Unset, str]): The version number (like 1.0) of the document version.
                DB column: histversion
            nb_of_valid_signatures (Union[Unset, int]): Number of valid signatures.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            t_stamp (Union[Unset, str]): The last update time of the version in ISO format (with dots).
                DB column: doctstamp
            obj_id (Union[Unset, int]): Document version belongs to this object.
                DB column: objectid
            guid (Union[Unset, str]): GUID of the document version.
                DB column: docguid
            comment (Union[Unset, str]): The user can enter a comment that describes the version.
                DB column: histcomment
            user (Union[Unset, int]): The user who inserts the version into the archive.
                DB column: userid
            create_date (Union[Unset, int]): The version is created at this date. The value is an ELO date format.
                DB column: createdate
            status (Union[Unset, int]): Deleted versions have Status=1.
                DB column: docstatus
            delete_date (Union[Unset, int]): The version is deleted at this date. The value is an ELO date format.
                The value is zero, if
                 isDeleted() returns false.
    """

    doc_id: Union[Unset, int] = UNSET
    doc_md5: Union[Unset, str] = UNSET
    flags: Union[Unset, int] = UNSET
    sig_id: Union[Unset, int] = UNSET
    language: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    nb_of_valid_signatures: Union[Unset, int] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    user: Union[Unset, int] = UNSET
    create_date: Union[Unset, int] = UNSET
    status: Union[Unset, int] = UNSET
    delete_date: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_id = self.doc_id

        doc_md5 = self.doc_md5

        flags = self.flags

        sig_id = self.sig_id

        language = self.language

        type = self.type

        version = self.version

        nb_of_valid_signatures = self.nb_of_valid_signatures

        t_stamp_sync = self.t_stamp_sync

        t_stamp = self.t_stamp

        obj_id = self.obj_id

        guid = self.guid

        comment = self.comment

        user = self.user

        create_date = self.create_date

        status = self.status

        delete_date = self.delete_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if doc_md5 is not UNSET:
            field_dict["docMD5"] = doc_md5
        if flags is not UNSET:
            field_dict["flags"] = flags
        if sig_id is not UNSET:
            field_dict["sigId"] = sig_id
        if language is not UNSET:
            field_dict["language"] = language
        if type is not UNSET:
            field_dict["type"] = type
        if version is not UNSET:
            field_dict["version"] = version
        if nb_of_valid_signatures is not UNSET:
            field_dict["nbOfValidSignatures"] = nb_of_valid_signatures
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if comment is not UNSET:
            field_dict["comment"] = comment
        if user is not UNSET:
            field_dict["user"] = user
        if create_date is not UNSET:
            field_dict["createDate"] = create_date
        if status is not UNSET:
            field_dict["status"] = status
        if delete_date is not UNSET:
            field_dict["deleteDate"] = delete_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_id = d.pop("docId", UNSET)

        doc_md5 = d.pop("docMD5", UNSET)

        flags = d.pop("flags", UNSET)

        sig_id = d.pop("sigId", UNSET)

        language = d.pop("language", UNSET)

        type = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        nb_of_valid_signatures = d.pop("nbOfValidSignatures", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        obj_id = d.pop("objId", UNSET)

        guid = d.pop("guid", UNSET)

        comment = d.pop("comment", UNSET)

        user = d.pop("user", UNSET)

        create_date = d.pop("createDate", UNSET)

        status = d.pop("status", UNSET)

        delete_date = d.pop("deleteDate", UNSET)

        doc_history = cls(
            doc_id=doc_id,
            doc_md5=doc_md5,
            flags=flags,
            sig_id=sig_id,
            language=language,
            type=type,
            version=version,
            nb_of_valid_signatures=nb_of_valid_signatures,
            t_stamp_sync=t_stamp_sync,
            t_stamp=t_stamp,
            obj_id=obj_id,
            guid=guid,
            comment=comment,
            user=user,
            create_date=create_date,
            status=status,
            delete_date=delete_date,
        )

        doc_history.additional_properties = d
        return doc_history

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
