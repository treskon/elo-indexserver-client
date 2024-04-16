from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="DocVersion")


@_attrs_define
class DocVersion:
    """<p>
    Description: This class describes a document version, a document preview or a signature.
     </p>
     <p>
     Copyright: Copyright (c) 2002
     </p>
     <p>
     Organisation: ELO DIgital Office GmbH
     </p>

        Attributes:
            preview (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            path_id_2 (Union[Unset, int]): (to be defined)
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            preview_url (Union[Unset, str]): <p>
                URL to up-/download a document preview.
                 </p>
                 <p>
                 Applies to document version. Is empty for signature and preview and fulltextContent.
                 </p>
            encryption_set (Union[Unset, int]): ID of the encryption set. It's password is used to encrypt or decrypt the
                document.
                It a new
                 document or version should be checked in, this member must be set to Sord.details.encryptionSet
                 before checkinDocBegin is called. When this object is retrieved via IX it is always set to
                 Sord.details.encryptionSet.
                 <p>
                 Applies to document version. Is undefined for signature.
                 </p>
            language (Union[Unset, str]): Language of the document content.
                This value is estimated by ELO Textreader when the document is sent for fulltext extraction.
                 See {@link TranslateTermC#DEFAULT_LANGUAGES} for a list of language-tags.
            path_id (Union[Unset, int]): Storage path ID
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            owner_id (Union[Unset, int]): The owners user ID.
                <p>
                 Applies to document version. Is undefined for signature and preview and fulltextContent.
                 </p>
            relative_file_path (Union[Unset, str]): Relative file path for external file.
                This member specifies the location of the file relative
                 to a custom path. If {@link #pathId} does not refer a custom path, this member is empty and
                 ignored in {@link IXServicePortIF#checkinDocEnd(ClientInfo, Sord, SordZ, Document, LockZ)}.
            sig (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            access_date_iso (Union[Unset, str]): Last access date. ClientInfo determines the Timezone.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            owner_name (Union[Unset, str]): The owners user name. This value is read only (ignored in checkinDoc...).
                <p>
                 Applies to document version. Is undefined for signature and preview and fulltextContent.
                 </p>
            t_stamp (Union[Unset, str]): Document timestamp
                <p>
                 Applies to document version and signature. Is undefined for preview. (Is available for
                 fulltextContent)
                 </p>
                 The format is JJJJ.MM.DD.hh.mm.ss
            phys_path (Union[Unset, str]): Physical path
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
                 Set SordC.mbPhysPath or EditInfoC.mbPhysPath in the member selector passed to checkoutSord or
                 checkoutDoc to read the physical path.
            id (Union[Unset, int]): Document ID
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            content_type (Union[Unset, str]): Content-Type (MIME-Type).
            delete_date_iso (Union[Unset, str]): Delete date. ClientInfo determines the Timezone.
                <p>
                 Is undefined if isDeleted() returns false.
                 </p>
            ext (Union[Unset, str]): Document file extension (without ".
                ")
                 <p>
                 Applies to document version, signature and preview. Is readonly for fulltextContent.
                 </p>
                 This value has precedence before <code>contentType</code>.
            upload_result (Union[Unset, str]): Result from the ELODM if the document was uploaded.
                <p>
                 Applies to document version, signature, preview and fulltextContent.
                 </p>
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's ACLs last export by the replication.
            file_data (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            work_version (Union[Unset, bool]): Indicates whether the version is the current work version.
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            version (Union[Unset, str]): Version number
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            url (Union[Unset, str]): URL to up-/download
                <p>
                 Applies to document version, signature,preview and fulltextContent.
                 </p>
            update_date_iso (Union[Unset, str]): Last update date. ClientInfo determines the Timezone.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            deleted (Union[Unset, bool]): Indicates whether the version is logically deleted.
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            milestone (Union[Unset, bool]): Indicates whether the version is marked as a milestone version.
                <p>
                 Applies to document version. Is undefined for signature and preview and fulltextContent.
                 </p>
            size (Union[Unset, str]): File size.
            nb_of_valid_signatures (Union[Unset, int]): Number of valid signatures.
                This member holds the count of valid signatures in the signature
                 file. It is only valid for a DocVersion object that represents a signature (member
                 {@link #sig}). A value of zero means, that the signatures are unchecked. A number greater than
                 zero means, that all signatures are valid. In this case the member value is equal to the number
                 of signatures. If at least one signature is invalid, the value is less than zero. The number of
                 invalid signatures is thereby unknown. Client applications are responsible to check signatures.
                 The ELOix does not check signatures.
            create_date_iso (Union[Unset, str]): Create date. ClientInfo determines the Timezone.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            fulltext_content (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            guid (Union[Unset, str]): Document GUID.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            comment (Union[Unset, str]): Version comment
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            md5 (Union[Unset, str]): MD5 hash of the documet file.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
    """

    preview: Union[Unset, "DocVersion"] = UNSET
    path_id_2: Union[Unset, int] = UNSET
    preview_url: Union[Unset, str] = UNSET
    encryption_set: Union[Unset, int] = UNSET
    language: Union[Unset, str] = UNSET
    path_id: Union[Unset, int] = UNSET
    owner_id: Union[Unset, int] = UNSET
    relative_file_path: Union[Unset, str] = UNSET
    sig: Union[Unset, "DocVersion"] = UNSET
    access_date_iso: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    phys_path: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    ext: Union[Unset, str] = UNSET
    upload_result: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    file_data: Union[Unset, "FileData"] = UNSET
    work_version: Union[Unset, bool] = UNSET
    version: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    update_date_iso: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    milestone: Union[Unset, bool] = UNSET
    size: Union[Unset, str] = UNSET
    nb_of_valid_signatures: Union[Unset, int] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    fulltext_content: Union[Unset, "DocVersion"] = UNSET
    guid: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    md5: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        path_id_2 = self.path_id_2

        preview_url = self.preview_url

        encryption_set = self.encryption_set

        language = self.language

        path_id = self.path_id

        owner_id = self.owner_id

        relative_file_path = self.relative_file_path

        sig: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sig, Unset):
            sig = self.sig.to_dict()

        access_date_iso = self.access_date_iso

        owner_name = self.owner_name

        t_stamp = self.t_stamp

        phys_path = self.phys_path

        id = self.id

        content_type = self.content_type

        delete_date_iso = self.delete_date_iso

        ext = self.ext

        upload_result = self.upload_result

        t_stamp_sync = self.t_stamp_sync

        file_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_data, Unset):
            file_data = self.file_data.to_dict()

        work_version = self.work_version

        version = self.version

        url = self.url

        update_date_iso = self.update_date_iso

        deleted = self.deleted

        milestone = self.milestone

        size = self.size

        nb_of_valid_signatures = self.nb_of_valid_signatures

        create_date_iso = self.create_date_iso

        fulltext_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulltext_content, Unset):
            fulltext_content = self.fulltext_content.to_dict()

        guid = self.guid

        comment = self.comment

        md5 = self.md5

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview is not UNSET:
            field_dict["preview"] = preview
        if path_id_2 is not UNSET:
            field_dict["pathId2"] = path_id_2
        if preview_url is not UNSET:
            field_dict["previewUrl"] = preview_url
        if encryption_set is not UNSET:
            field_dict["encryptionSet"] = encryption_set
        if language is not UNSET:
            field_dict["language"] = language
        if path_id is not UNSET:
            field_dict["pathId"] = path_id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if relative_file_path is not UNSET:
            field_dict["relativeFilePath"] = relative_file_path
        if sig is not UNSET:
            field_dict["sig"] = sig
        if access_date_iso is not UNSET:
            field_dict["accessDateIso"] = access_date_iso
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if phys_path is not UNSET:
            field_dict["physPath"] = phys_path
        if id is not UNSET:
            field_dict["id"] = id
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso
        if ext is not UNSET:
            field_dict["ext"] = ext
        if upload_result is not UNSET:
            field_dict["uploadResult"] = upload_result
        if t_stamp_sync is not UNSET:
            field_dict["tStampSync"] = t_stamp_sync
        if file_data is not UNSET:
            field_dict["fileData"] = file_data
        if work_version is not UNSET:
            field_dict["workVersion"] = work_version
        if version is not UNSET:
            field_dict["version"] = version
        if url is not UNSET:
            field_dict["url"] = url
        if update_date_iso is not UNSET:
            field_dict["updateDateIso"] = update_date_iso
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if size is not UNSET:
            field_dict["size"] = size
        if nb_of_valid_signatures is not UNSET:
            field_dict["nbOfValidSignatures"] = nb_of_valid_signatures
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if fulltext_content is not UNSET:
            field_dict["fulltextContent"] = fulltext_content
        if guid is not UNSET:
            field_dict["guid"] = guid
        if comment is not UNSET:
            field_dict["comment"] = comment
        if md5 is not UNSET:
            field_dict["md5"] = md5

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        _preview = d.pop("preview", UNSET)
        preview: Union[Unset, DocVersion]
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = DocVersion.from_dict(_preview)

        path_id_2 = d.pop("pathId2", UNSET)

        preview_url = d.pop("previewUrl", UNSET)

        encryption_set = d.pop("encryptionSet", UNSET)

        language = d.pop("language", UNSET)

        path_id = d.pop("pathId", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        relative_file_path = d.pop("relativeFilePath", UNSET)

        _sig = d.pop("sig", UNSET)
        sig: Union[Unset, DocVersion]
        if isinstance(_sig, Unset):
            sig = UNSET
        else:
            sig = DocVersion.from_dict(_sig)

        access_date_iso = d.pop("accessDateIso", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        phys_path = d.pop("physPath", UNSET)

        id = d.pop("id", UNSET)

        content_type = d.pop("contentType", UNSET)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        ext = d.pop("ext", UNSET)

        upload_result = d.pop("uploadResult", UNSET)

        t_stamp_sync = d.pop("tStampSync", UNSET)

        _file_data = d.pop("fileData", UNSET)
        file_data: Union[Unset, FileData]
        if isinstance(_file_data, Unset):
            file_data = UNSET
        else:
            file_data = FileData.from_dict(_file_data)

        work_version = d.pop("workVersion", UNSET)

        version = d.pop("version", UNSET)

        url = d.pop("url", UNSET)

        update_date_iso = d.pop("updateDateIso", UNSET)

        deleted = d.pop("deleted", UNSET)

        milestone = d.pop("milestone", UNSET)

        size = d.pop("size", UNSET)

        nb_of_valid_signatures = d.pop("nbOfValidSignatures", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        _fulltext_content = d.pop("fulltextContent", UNSET)
        fulltext_content: Union[Unset, DocVersion]
        if isinstance(_fulltext_content, Unset):
            fulltext_content = UNSET
        else:
            fulltext_content = DocVersion.from_dict(_fulltext_content)

        guid = d.pop("guid", UNSET)

        comment = d.pop("comment", UNSET)

        md5 = d.pop("md5", UNSET)

        doc_version = cls(
            preview=preview,
            path_id_2=path_id_2,
            preview_url=preview_url,
            encryption_set=encryption_set,
            language=language,
            path_id=path_id,
            owner_id=owner_id,
            relative_file_path=relative_file_path,
            sig=sig,
            access_date_iso=access_date_iso,
            owner_name=owner_name,
            t_stamp=t_stamp,
            phys_path=phys_path,
            id=id,
            content_type=content_type,
            delete_date_iso=delete_date_iso,
            ext=ext,
            upload_result=upload_result,
            t_stamp_sync=t_stamp_sync,
            file_data=file_data,
            work_version=work_version,
            version=version,
            url=url,
            update_date_iso=update_date_iso,
            deleted=deleted,
            milestone=milestone,
            size=size,
            nb_of_valid_signatures=nb_of_valid_signatures,
            create_date_iso=create_date_iso,
            fulltext_content=fulltext_content,
            guid=guid,
            comment=comment,
            md5=md5,
        )

        doc_version.additional_properties = d
        return doc_version

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
