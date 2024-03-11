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
            archiving_mode (Union[Unset, int]): Archiving mode. Sort order and archiving mode share the same database
                column.
                If the mask is used for documents,
                 set <code>sortOrder=SordOrderC.NONE</code>. ELO 7.0: This value is only valid for document masks,
                 <code>documentMask=true</code>.
            encryption_set (Union[Unset, int]): Encryption set number.
            fulltext (Union[Unset, bool]): Document is or should be containted in the fultext database.
            sort_order (Union[Unset, int]): Sort order of child entries. Sort order and archiving mode share the same
                database column.
                If the mask is used for
                 folders, set <code>archivingMode=ArchivingModeC.NONE</code>. If both <code>sortOrder</code> and
                 <code>archivingMode</code> are set, <code>sortOrder</code> has precedence and <code>archivingMode</code> is
                 ignored. ELO 7.0: This value is only valid for folder masks, <code>folderMask=true</code>.
            document_mask (Union[Unset, bool]): Mask can be used to edit indexing information of a document.
            search_mask (Union[Unset, bool]): Mask can be used to search for indexing information.
            folder_mask (Union[Unset, bool]): Mask can be used to edit indexing information of a folder
            create_index_path (Union[Unset, bool]): If <code>DocMask.
                index</code> is defined, this option effects that the resulting archieve path is created, if it
                 does not exist.
            create_index_references_paths (Union[Unset, bool]): If <code>DocMask.
                index</code> is defined including reference paths, this option effects that the resulting
                 reference paths are created, if they do not exist.
            release_document (Union[Unset, bool]): Documents using this mask may be used as release notes
            document_container (Union[Unset, bool]): Folders indexed with this mask get the flag {@link
                SordDetails#documentContainer} set accordingly.
            translate_sord_name (Union[Unset, bool]): If <tt>true</tt> translate the sord's short description into or from
                the user language.
            enabled_by_parent (Union[Unset, bool]): Usage depends on the keywording form of the parent entry.
                This keywording form should only be used for a Sord, if
                 the keywording form of the parent Sord explicitly allows that in it's member
                 {@link DocMask#maskIdsForChildEntries}.
            inherit_acl_disabled (Union[Unset, bool]): Do not inherit permissions from parent Sords.
            keywording_relation_allowed (Union[Unset, bool]): Mask can be referenced from a DocMaskLine of type {@link
                DocMaskLineC#TYPE_RELATION}
    """

    archiving_mode: Union[Unset, int] = UNSET
    encryption_set: Union[Unset, int] = UNSET
    fulltext: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, int] = UNSET
    document_mask: Union[Unset, bool] = UNSET
    search_mask: Union[Unset, bool] = UNSET
    folder_mask: Union[Unset, bool] = UNSET
    create_index_path: Union[Unset, bool] = UNSET
    create_index_references_paths: Union[Unset, bool] = UNSET
    release_document: Union[Unset, bool] = UNSET
    document_container: Union[Unset, bool] = UNSET
    translate_sord_name: Union[Unset, bool] = UNSET
    enabled_by_parent: Union[Unset, bool] = UNSET
    inherit_acl_disabled: Union[Unset, bool] = UNSET
    keywording_relation_allowed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archiving_mode = self.archiving_mode
        encryption_set = self.encryption_set
        fulltext = self.fulltext
        sort_order = self.sort_order
        document_mask = self.document_mask
        search_mask = self.search_mask
        folder_mask = self.folder_mask
        create_index_path = self.create_index_path
        create_index_references_paths = self.create_index_references_paths
        release_document = self.release_document
        document_container = self.document_container
        translate_sord_name = self.translate_sord_name
        enabled_by_parent = self.enabled_by_parent
        inherit_acl_disabled = self.inherit_acl_disabled
        keywording_relation_allowed = self.keywording_relation_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archiving_mode is not UNSET:
            field_dict["archivingMode"] = archiving_mode
        if encryption_set is not UNSET:
            field_dict["encryptionSet"] = encryption_set
        if fulltext is not UNSET:
            field_dict["fulltext"] = fulltext
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if document_mask is not UNSET:
            field_dict["documentMask"] = document_mask
        if search_mask is not UNSET:
            field_dict["searchMask"] = search_mask
        if folder_mask is not UNSET:
            field_dict["folderMask"] = folder_mask
        if create_index_path is not UNSET:
            field_dict["createIndexPath"] = create_index_path
        if create_index_references_paths is not UNSET:
            field_dict["createIndexReferencesPaths"] = create_index_references_paths
        if release_document is not UNSET:
            field_dict["releaseDocument"] = release_document
        if document_container is not UNSET:
            field_dict["documentContainer"] = document_container
        if translate_sord_name is not UNSET:
            field_dict["translateSordName"] = translate_sord_name
        if enabled_by_parent is not UNSET:
            field_dict["enabledByParent"] = enabled_by_parent
        if inherit_acl_disabled is not UNSET:
            field_dict["inheritAclDisabled"] = inherit_acl_disabled
        if keywording_relation_allowed is not UNSET:
            field_dict["keywordingRelationAllowed"] = keywording_relation_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        archiving_mode = d.pop("archivingMode", UNSET)

        encryption_set = d.pop("encryptionSet", UNSET)

        fulltext = d.pop("fulltext", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        document_mask = d.pop("documentMask", UNSET)

        search_mask = d.pop("searchMask", UNSET)

        folder_mask = d.pop("folderMask", UNSET)

        create_index_path = d.pop("createIndexPath", UNSET)

        create_index_references_paths = d.pop("createIndexReferencesPaths", UNSET)

        release_document = d.pop("releaseDocument", UNSET)

        document_container = d.pop("documentContainer", UNSET)

        translate_sord_name = d.pop("translateSordName", UNSET)

        enabled_by_parent = d.pop("enabledByParent", UNSET)

        inherit_acl_disabled = d.pop("inheritAclDisabled", UNSET)

        keywording_relation_allowed = d.pop("keywordingRelationAllowed", UNSET)

        doc_mask_details = cls(
            archiving_mode=archiving_mode,
            encryption_set=encryption_set,
            fulltext=fulltext,
            sort_order=sort_order,
            document_mask=document_mask,
            search_mask=search_mask,
            folder_mask=folder_mask,
            create_index_path=create_index_path,
            create_index_references_paths=create_index_references_paths,
            release_document=release_document,
            document_container=document_container,
            translate_sord_name=translate_sord_name,
            enabled_by_parent=enabled_by_parent,
            inherit_acl_disabled=inherit_acl_disabled,
            keywording_relation_allowed=keywording_relation_allowed,
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
