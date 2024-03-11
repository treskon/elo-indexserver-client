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
            access_date_iso (Union[Unset, str]): Last access date. ClientInfo determines the Timezone.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            comment (Union[Unset, str]): Version comment
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            create_date_iso (Union[Unset, str]): Create date. ClientInfo determines the Timezone.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            deleted (Union[Unset, bool]): Indicates whether the version is logically deleted.
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            ext (Union[Unset, str]): Document file extension (without ".
                ")
                 <p>
                 Applies to document version, signature and preview. Is readonly for fulltextContent.
                 </p>
                 This value has precedence before <code>contentType</code>.
            content_type (Union[Unset, str]): Content-Type (MIME-Type).
            file_data (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            guid (Union[Unset, str]): Document GUID.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            id (Union[Unset, int]): Document ID
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            md5 (Union[Unset, str]): MD5 hash of the documet file.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            milestone (Union[Unset, bool]): Indicates whether the version is marked as a milestone version.
                <p>
                 Applies to document version. Is undefined for signature and preview and fulltextContent.
                 </p>
            owner_id (Union[Unset, int]): The owners user ID.
                <p>
                 Applies to document version. Is undefined for signature and preview and fulltextContent.
                 </p>
            owner_name (Union[Unset, str]): The owners user name. This value is read only (ignored in checkinDoc...).
                <p>
                 Applies to document version. Is undefined for signature and preview and fulltextContent.
                 </p>
            path_id (Union[Unset, int]): Storage path ID
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            path_id_2 (Union[Unset, int]): (to be defined)
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            phys_path (Union[Unset, str]): Physical path
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
                 Set SordC.mbPhysPath or EditInfoC.mbPhysPath in the member selector passed to checkoutSord or checkoutDoc to
                read
                 the physical path.
            preview_url (Union[Unset, str]): <p>
                URL to up-/download a document preview.
                 </p>
                 <p>
                 Applies to document version. Is empty for signature and preview and fulltextContent.
                 </p>
            sig (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            preview (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            size (Union[Unset, str]): File size.
            t_stamp (Union[Unset, str]): Document timestamp
                <p>
                 Applies to document version and signature. Is undefined for preview. (Is available for fulltextContent)
                 </p>
                 The format is JJJJ.MM.DD.hh.mm.ss
            update_date_iso (Union[Unset, str]): Last update date. ClientInfo determines the Timezone.
                <p>
                 Applies to document version and signature. Is undefined for preview and fulltextContent.
                 </p>
            upload_result (Union[Unset, str]): Result from the ELODM if the document was uploaded.
                <p>
                 Applies to document version, signature, preview and fulltextContent.
                 </p>
            url (Union[Unset, str]): URL to up-/download
                <p>
                 Applies to document version, signature,preview and fulltextContent.
                 </p>
            version (Union[Unset, str]): Version number
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            work_version (Union[Unset, bool]): Indicates whether the version is the current work version.
                <p>
                 Applies to document version. Is undefined for signature, preview and fulltextContent.
                 </p>
            encryption_set (Union[Unset, int]): ID of the encryption set. It's password is used to encrypt or decrypt the
                document.
                It a new document or version
                 should be checked in, this member must be set to Sord.details.encryptionSet before checkinDocBegin is called.
                When
                 this object is retrieved via IX it is always set to Sord.details.encryptionSet.
                 <p>
                 Applies to document version. Is undefined for signature.
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
            delete_date_iso (Union[Unset, str]): Delete date. ClientInfo determines the Timezone.
                <p>
                 Is undefined if isDeleted() returns false.
                 </p>
            nb_of_valid_signatures (Union[Unset, int]): Number of valid signatures. This member holds the count of valid
                signatures in the signature file.
                It is only valid
                 for a DocVersion object that represents a signature (member {@link #sig}). A value of zero means, that the
                 signatures are unchecked. A number greater than zero means, that all signatures are valid. In this case the
                member
                 value is equal to the number of signatures. If at least one signature is invalid, the value is less than zero.
                The
                 number of invalid signatures is thereby unknown. Client applications are responsible to check signatures. The
                ELOix
                 does not check signatures.
            relative_file_path (Union[Unset, str]): Relative file path for external file. This member specifies the location
                of the file relative to a custom path.
                If
                 {@link #pathId} does not refer a custom path, this member is empty and ignored in
                 {@link IXServicePortIF#checkinDocEnd(ClientInfo, Sord, SordZ, Document, LockZ)}.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's ACLs last export by the replication.
    """

    access_date_iso: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    ext: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    file_data: Union[Unset, "FileData"] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    md5: Union[Unset, str] = UNSET
    milestone: Union[Unset, bool] = UNSET
    owner_id: Union[Unset, int] = UNSET
    owner_name: Union[Unset, str] = UNSET
    path_id: Union[Unset, int] = UNSET
    path_id_2: Union[Unset, int] = UNSET
    phys_path: Union[Unset, str] = UNSET
    preview_url: Union[Unset, str] = UNSET
    sig: Union[Unset, "DocVersion"] = UNSET
    preview: Union[Unset, "DocVersion"] = UNSET
    size: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    update_date_iso: Union[Unset, str] = UNSET
    upload_result: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    work_version: Union[Unset, bool] = UNSET
    encryption_set: Union[Unset, int] = UNSET
    fulltext_content: Union[Unset, "DocVersion"] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    nb_of_valid_signatures: Union[Unset, int] = UNSET
    relative_file_path: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_date_iso = self.access_date_iso
        comment = self.comment
        create_date_iso = self.create_date_iso
        deleted = self.deleted
        ext = self.ext
        content_type = self.content_type
        file_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_data, Unset):
            file_data = self.file_data.to_dict()

        guid = self.guid
        id = self.id
        md5 = self.md5
        milestone = self.milestone
        owner_id = self.owner_id
        owner_name = self.owner_name
        path_id = self.path_id
        path_id_2 = self.path_id_2
        phys_path = self.phys_path
        preview_url = self.preview_url
        sig: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sig, Unset):
            sig = self.sig.to_dict()

        preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        size = self.size
        t_stamp = self.t_stamp
        update_date_iso = self.update_date_iso
        upload_result = self.upload_result
        url = self.url
        version = self.version
        work_version = self.work_version
        encryption_set = self.encryption_set
        fulltext_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulltext_content, Unset):
            fulltext_content = self.fulltext_content.to_dict()

        delete_date_iso = self.delete_date_iso
        nb_of_valid_signatures = self.nb_of_valid_signatures
        relative_file_path = self.relative_file_path
        t_stamp_sync = self.t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_date_iso is not UNSET:
            field_dict["accessDateIso"] = access_date_iso
        if comment is not UNSET:
            field_dict["comment"] = comment
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if ext is not UNSET:
            field_dict["ext"] = ext
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if file_data is not UNSET:
            field_dict["fileData"] = file_data
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if path_id is not UNSET:
            field_dict["pathId"] = path_id
        if path_id_2 is not UNSET:
            field_dict["pathId2"] = path_id_2
        if phys_path is not UNSET:
            field_dict["physPath"] = phys_path
        if preview_url is not UNSET:
            field_dict["previewUrl"] = preview_url
        if sig is not UNSET:
            field_dict["sig"] = sig
        if preview is not UNSET:
            field_dict["preview"] = preview
        if size is not UNSET:
            field_dict["size"] = size
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if update_date_iso is not UNSET:
            field_dict["updateDateIso"] = update_date_iso
        if upload_result is not UNSET:
            field_dict["uploadResult"] = upload_result
        if url is not UNSET:
            field_dict["url"] = url
        if version is not UNSET:
            field_dict["version"] = version
        if work_version is not UNSET:
            field_dict["workVersion"] = work_version
        if encryption_set is not UNSET:
            field_dict["encryptionSet"] = encryption_set
        if fulltext_content is not UNSET:
            field_dict["fulltextContent"] = fulltext_content
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso
        if nb_of_valid_signatures is not UNSET:
            field_dict["nbOfValidSignatures"] = nb_of_valid_signatures
        if relative_file_path is not UNSET:
            field_dict["relativeFilePath"] = relative_file_path
        if t_stamp_sync is not UNSET:
            field_dict["tStampSync"] = t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        access_date_iso = d.pop("accessDateIso", UNSET)

        comment = d.pop("comment", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        deleted = d.pop("deleted", UNSET)

        ext = d.pop("ext", UNSET)

        content_type = d.pop("contentType", UNSET)

        _file_data = d.pop("fileData", UNSET)
        file_data: Union[Unset, FileData]
        if isinstance(_file_data, Unset):
            file_data = UNSET
        else:
            file_data = FileData.from_dict(_file_data)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        md5 = d.pop("md5", UNSET)

        milestone = d.pop("milestone", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        path_id = d.pop("pathId", UNSET)

        path_id_2 = d.pop("pathId2", UNSET)

        phys_path = d.pop("physPath", UNSET)

        preview_url = d.pop("previewUrl", UNSET)

        _sig = d.pop("sig", UNSET)
        sig: Union[Unset, DocVersion]
        if isinstance(_sig, Unset):
            sig = UNSET
        else:
            sig = DocVersion.from_dict(_sig)

        _preview = d.pop("preview", UNSET)
        preview: Union[Unset, DocVersion]
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = DocVersion.from_dict(_preview)

        size = d.pop("size", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        update_date_iso = d.pop("updateDateIso", UNSET)

        upload_result = d.pop("uploadResult", UNSET)

        url = d.pop("url", UNSET)

        version = d.pop("version", UNSET)

        work_version = d.pop("workVersion", UNSET)

        encryption_set = d.pop("encryptionSet", UNSET)

        _fulltext_content = d.pop("fulltextContent", UNSET)
        fulltext_content: Union[Unset, DocVersion]
        if isinstance(_fulltext_content, Unset):
            fulltext_content = UNSET
        else:
            fulltext_content = DocVersion.from_dict(_fulltext_content)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        nb_of_valid_signatures = d.pop("nbOfValidSignatures", UNSET)

        relative_file_path = d.pop("relativeFilePath", UNSET)

        t_stamp_sync = d.pop("tStampSync", UNSET)

        doc_version = cls(
            access_date_iso=access_date_iso,
            comment=comment,
            create_date_iso=create_date_iso,
            deleted=deleted,
            ext=ext,
            content_type=content_type,
            file_data=file_data,
            guid=guid,
            id=id,
            md5=md5,
            milestone=milestone,
            owner_id=owner_id,
            owner_name=owner_name,
            path_id=path_id,
            path_id_2=path_id_2,
            phys_path=phys_path,
            preview_url=preview_url,
            sig=sig,
            preview=preview,
            size=size,
            t_stamp=t_stamp,
            update_date_iso=update_date_iso,
            upload_result=upload_result,
            url=url,
            version=version,
            work_version=work_version,
            encryption_set=encryption_set,
            fulltext_content=fulltext_content,
            delete_date_iso=delete_date_iso,
            nb_of_valid_signatures=nb_of_valid_signatures,
            relative_file_path=relative_file_path,
            t_stamp_sync=t_stamp_sync,
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
