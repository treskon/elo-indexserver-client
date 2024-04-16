from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskDetails")


@_attrs_define
class DocMaskDetails:
    """This class contains a member of a <code>DocMask</code> object.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            keywording_relation_allowed (Union[Unset, bool]): Mask can be referenced from a DocMaskLine of type {@link
                DocMaskLineC#TYPE_RELATION}.
                <br>
                 If this mask has a data organisation {@link DocMaskC#DATA_ORGANISATION_ASPECT} the value
                 determines if it can be referenced by an AspectLine of type {@link AspectLineC#TYPE_RELATION}.
            enabled_by_parent (Union[Unset, bool]): Usage depends on the keywording form of the parent entry.
                This keywording form should only be
                 used for a Sord, if the keywording form of the parent Sord explicitly allows that in it's
                 member {@link DocMask#maskIdsForChildEntries}.
            encryption_set (Union[Unset, int]): Encryption set number.
            document_mask (Union[Unset, bool]): Mask can be used to edit indexing information of a document.
            release_document (Union[Unset, bool]): Documents using this mask may be used as release notes
            create_index_path (Union[Unset, bool]): If <code>DocMask.
                index</code> is defined, this option effects that the resulting archieve path
                 is created, if it does not exist.
            archiving_mode (Union[Unset, int]): Archiving mode. Sort order and archiving mode share the same database
                column.
                If the mask is
                 used for documents, set <code>sortOrder=SordOrderC.NONE</code>. ELO 7.0: This value is only
                 valid for document masks, <code>documentMask=true</code>.
            inherit_acl_disabled (Union[Unset, bool]): Do not inherit permissions from parent Sords.
            document_container (Union[Unset, bool]): Folders indexed with this mask get the flag {@link
                SordDetails#documentContainer} set
                accordingly.
            sort_order (Union[Unset, int]): Sort order of child entries. Sort order and archiving mode share the same
                database column.
                If
                 the mask is used for folders, set <code>archivingMode=ArchivingModeC.NONE</code>. If both
                 <code>sortOrder</code> and <code>archivingMode</code> are set, <code>sortOrder</code> has
                 precedence and <code>archivingMode</code> is ignored. ELO 7.0: This value is only valid for
                 folder masks, <code>folderMask=true</code>.
            search_mask (Union[Unset, bool]): Mask can be used to search for indexing information.
            fulltext (Union[Unset, bool]): Document is or should be containted in the fultext database.
            translate_sord_name (Union[Unset, bool]): If <tt>true</tt> translate the sord's short description into or from
                the user language.
            folder_mask (Union[Unset, bool]): Mask can be used to edit indexing information of a folder
            create_index_references_paths (Union[Unset, bool]): If <code>DocMask.
                index</code> is defined including reference paths, this option effects that
                 the resulting reference paths are created, if they do not exist.
            region (Union[Unset, bool]): Sords of this mask, in case they are a folder, establish a region within the
                repository
                tree.<br>
                 This flag is only valid for masks of data organisation.
                 {@link DocMaskC#DATA_ORGANISATION_ASPECT}.
    """

    keywording_relation_allowed: Union[Unset, bool] = UNSET
    enabled_by_parent: Union[Unset, bool] = UNSET
    encryption_set: Union[Unset, int] = UNSET
    document_mask: Union[Unset, bool] = UNSET
    release_document: Union[Unset, bool] = UNSET
    create_index_path: Union[Unset, bool] = UNSET
    archiving_mode: Union[Unset, int] = UNSET
    inherit_acl_disabled: Union[Unset, bool] = UNSET
    document_container: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, int] = UNSET
    search_mask: Union[Unset, bool] = UNSET
    fulltext: Union[Unset, bool] = UNSET
    translate_sord_name: Union[Unset, bool] = UNSET
    folder_mask: Union[Unset, bool] = UNSET
    create_index_references_paths: Union[Unset, bool] = UNSET
    region: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keywording_relation_allowed = self.keywording_relation_allowed

        enabled_by_parent = self.enabled_by_parent

        encryption_set = self.encryption_set

        document_mask = self.document_mask

        release_document = self.release_document

        create_index_path = self.create_index_path

        archiving_mode = self.archiving_mode

        inherit_acl_disabled = self.inherit_acl_disabled

        document_container = self.document_container

        sort_order = self.sort_order

        search_mask = self.search_mask

        fulltext = self.fulltext

        translate_sord_name = self.translate_sord_name

        folder_mask = self.folder_mask

        create_index_references_paths = self.create_index_references_paths

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywording_relation_allowed is not UNSET:
            field_dict["keywordingRelationAllowed"] = keywording_relation_allowed
        if enabled_by_parent is not UNSET:
            field_dict["enabledByParent"] = enabled_by_parent
        if encryption_set is not UNSET:
            field_dict["encryptionSet"] = encryption_set
        if document_mask is not UNSET:
            field_dict["documentMask"] = document_mask
        if release_document is not UNSET:
            field_dict["releaseDocument"] = release_document
        if create_index_path is not UNSET:
            field_dict["createIndexPath"] = create_index_path
        if archiving_mode is not UNSET:
            field_dict["archivingMode"] = archiving_mode
        if inherit_acl_disabled is not UNSET:
            field_dict["inheritAclDisabled"] = inherit_acl_disabled
        if document_container is not UNSET:
            field_dict["documentContainer"] = document_container
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if search_mask is not UNSET:
            field_dict["searchMask"] = search_mask
        if fulltext is not UNSET:
            field_dict["fulltext"] = fulltext
        if translate_sord_name is not UNSET:
            field_dict["translateSordName"] = translate_sord_name
        if folder_mask is not UNSET:
            field_dict["folderMask"] = folder_mask
        if create_index_references_paths is not UNSET:
            field_dict["createIndexReferencesPaths"] = create_index_references_paths
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keywording_relation_allowed = d.pop("keywordingRelationAllowed", UNSET)

        enabled_by_parent = d.pop("enabledByParent", UNSET)

        encryption_set = d.pop("encryptionSet", UNSET)

        document_mask = d.pop("documentMask", UNSET)

        release_document = d.pop("releaseDocument", UNSET)

        create_index_path = d.pop("createIndexPath", UNSET)

        archiving_mode = d.pop("archivingMode", UNSET)

        inherit_acl_disabled = d.pop("inheritAclDisabled", UNSET)

        document_container = d.pop("documentContainer", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        search_mask = d.pop("searchMask", UNSET)

        fulltext = d.pop("fulltext", UNSET)

        translate_sord_name = d.pop("translateSordName", UNSET)

        folder_mask = d.pop("folderMask", UNSET)

        create_index_references_paths = d.pop("createIndexReferencesPaths", UNSET)

        region = d.pop("region", UNSET)

        doc_mask_details = cls(
            keywording_relation_allowed=keywording_relation_allowed,
            enabled_by_parent=enabled_by_parent,
            encryption_set=encryption_set,
            document_mask=document_mask,
            release_document=release_document,
            create_index_path=create_index_path,
            archiving_mode=archiving_mode,
            inherit_acl_disabled=inherit_acl_disabled,
            document_container=document_container,
            sort_order=sort_order,
            search_mask=search_mask,
            fulltext=fulltext,
            translate_sord_name=translate_sord_name,
            folder_mask=folder_mask,
            create_index_references_paths=create_index_references_paths,
            region=region,
        )

        doc_mask_details.additional_properties = d
        return doc_mask_details

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
