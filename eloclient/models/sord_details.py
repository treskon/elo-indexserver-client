from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SordDetails")


@_attrs_define
class SordDetails:
    """Objects of this class are data elements and control the values assigned to certain boolean
    properties(yes/no attributes).

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            repl_root (Union[Unset, bool]): True, if this object is a root folder for replication.
            workspace (Union[Unset, bool]): If <tt>true</tt> the sord is a workspace folder.
            limited_release_document (Union[Unset, bool]): Documents using this mask may be used as release notes
            arc_repl_enabled (Union[Unset, bool]): True, if replication is enabled for this archive.
            encryption_set (Union[Unset, int]): Encryption set number.
            fulltext_done (Union[Unset, bool]): Document is indexed in the fultext database.
            incomplete (Union[Unset, bool]): True, if a document or attachment version has been deleted.
            archiving_mode (Union[Unset, int]): Archiving mode.
                The possible values are:
                 <table border="2">
                 <tr>
                 <td>version controlled</td>
                 <td>ArchivingModeC.VERSION</td>
                 </tr>
                 <tr>
                 <td>read-only</td>
                 <td>ArchivingModeC.READONLY</td>
                 </tr>
                 <tr>
                 <td>read/write</td>
                 <td>ArchivingModeC.READWRITE</td>
                 </tr>
                 </table>
                 This value is only valid for document objects.
            inherit_acl_disabled (Union[Unset, bool]): Do not inherit permissions from parent Sord.
            document_container (Union[Unset, bool]): Folders can be marked as a document container by this flag.
                If true, clients are advised to
                 preview the first document in this folder on selection.
            sort_order (Union[Unset, int]): Sort order of child entries. This value is only valid for folder objects.
            fulltext (Union[Unset, bool]): Document is or should be containted in the fultext database.
            translate_sord_name (Union[Unset, bool]): If <tt>true</tt> translate the sord's short description into or from
                the user language.
            region (Union[Unset, bool]): If this sord is a folder, it establishes a region within the repository tree.
                <br>
                 This flag is only valid for sords with a mask of data organisation
                 {@link DocMaskC#DATA_ORGANISATION_ASPECT}.
            linked (Union[Unset, bool]): True, if this object has links to other Sords.
                This member is read-only and is ignored in
                 checkinSord and checkinDocEnd.
            linked_permanent (Union[Unset, bool]): True, if this object has permanent links to other Sords.
                This member is read-only and is
                 ignored in checkinSord and checkinDocEnd.
    """

    repl_root: Union[Unset, bool] = UNSET
    workspace: Union[Unset, bool] = UNSET
    limited_release_document: Union[Unset, bool] = UNSET
    arc_repl_enabled: Union[Unset, bool] = UNSET
    encryption_set: Union[Unset, int] = UNSET
    fulltext_done: Union[Unset, bool] = UNSET
    incomplete: Union[Unset, bool] = UNSET
    archiving_mode: Union[Unset, int] = UNSET
    inherit_acl_disabled: Union[Unset, bool] = UNSET
    document_container: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, int] = UNSET
    fulltext: Union[Unset, bool] = UNSET
    translate_sord_name: Union[Unset, bool] = UNSET
    region: Union[Unset, bool] = UNSET
    linked: Union[Unset, bool] = UNSET
    linked_permanent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repl_root = self.repl_root

        workspace = self.workspace

        limited_release_document = self.limited_release_document

        arc_repl_enabled = self.arc_repl_enabled

        encryption_set = self.encryption_set

        fulltext_done = self.fulltext_done

        incomplete = self.incomplete

        archiving_mode = self.archiving_mode

        inherit_acl_disabled = self.inherit_acl_disabled

        document_container = self.document_container

        sort_order = self.sort_order

        fulltext = self.fulltext

        translate_sord_name = self.translate_sord_name

        region = self.region

        linked = self.linked

        linked_permanent = self.linked_permanent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repl_root is not UNSET:
            field_dict["replRoot"] = repl_root
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if limited_release_document is not UNSET:
            field_dict["limitedReleaseDocument"] = limited_release_document
        if arc_repl_enabled is not UNSET:
            field_dict["arcReplEnabled"] = arc_repl_enabled
        if encryption_set is not UNSET:
            field_dict["encryptionSet"] = encryption_set
        if fulltext_done is not UNSET:
            field_dict["fulltextDone"] = fulltext_done
        if incomplete is not UNSET:
            field_dict["incomplete"] = incomplete
        if archiving_mode is not UNSET:
            field_dict["archivingMode"] = archiving_mode
        if inherit_acl_disabled is not UNSET:
            field_dict["inheritAclDisabled"] = inherit_acl_disabled
        if document_container is not UNSET:
            field_dict["documentContainer"] = document_container
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if fulltext is not UNSET:
            field_dict["fulltext"] = fulltext
        if translate_sord_name is not UNSET:
            field_dict["translateSordName"] = translate_sord_name
        if region is not UNSET:
            field_dict["region"] = region
        if linked is not UNSET:
            field_dict["linked"] = linked
        if linked_permanent is not UNSET:
            field_dict["linkedPermanent"] = linked_permanent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repl_root = d.pop("replRoot", UNSET)

        workspace = d.pop("workspace", UNSET)

        limited_release_document = d.pop("limitedReleaseDocument", UNSET)

        arc_repl_enabled = d.pop("arcReplEnabled", UNSET)

        encryption_set = d.pop("encryptionSet", UNSET)

        fulltext_done = d.pop("fulltextDone", UNSET)

        incomplete = d.pop("incomplete", UNSET)

        archiving_mode = d.pop("archivingMode", UNSET)

        inherit_acl_disabled = d.pop("inheritAclDisabled", UNSET)

        document_container = d.pop("documentContainer", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        fulltext = d.pop("fulltext", UNSET)

        translate_sord_name = d.pop("translateSordName", UNSET)

        region = d.pop("region", UNSET)

        linked = d.pop("linked", UNSET)

        linked_permanent = d.pop("linkedPermanent", UNSET)

        sord_details = cls(
            repl_root=repl_root,
            workspace=workspace,
            limited_release_document=limited_release_document,
            arc_repl_enabled=arc_repl_enabled,
            encryption_set=encryption_set,
            fulltext_done=fulltext_done,
            incomplete=incomplete,
            archiving_mode=archiving_mode,
            inherit_acl_disabled=inherit_acl_disabled,
            document_container=document_container,
            sort_order=sort_order,
            fulltext=fulltext,
            translate_sord_name=translate_sord_name,
            region=region,
            linked=linked,
            linked_permanent=linked_permanent,
        )

        sord_details.additional_properties = d
        return sord_details

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
