from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask_z import DocMaskZ


T = TypeVar("T", bound="DocMaskC")


@_attrs_define
class DocMaskC:
    """<p>
    Constants related to class <code>DocMask</code>. Some of the <code>MFG_</code> values are used in
     the member <code>Flags</code> of class <code>Sord</code> too. Each member of this class with
     prefix "mb" has a corresponding member in class <code>DocMask</code>
     </p>
     *
     </p>

        Attributes:
            mb_transitive_children (Union[Unset, str]): Member bit for {@link DocMask#transitiveChildren}.
            mb_sort_order_not_archiving_mode (Union[Unset, str]): Member bit: this bit should be set if the Mask is to be
                used for structure elements and not for
                documents. The effect is that the member DocMask.details.sortOrder is filled instead of
                 DocMask.details.archivingMode.
            guid_email (Union[Unset, str]): Predefined GUID for keywording form "EMail".
            mb_aspect_assocs (Union[Unset, str]): Member bit for {@link DocMask#aspectAssocs}.
            mb_lines (Union[Unset, str]):
            guid_basic (Union[Unset, str]): Predefined GUID for keywording form "Freie Eingabe".
            mb_details (Union[Unset, str]):
            ln_acl (Union[Unset, int]): ACL length
            mb_inherit_from_masks (Union[Unset, str]): Member bit for {@link DocMask#inheritFromMasks}.
            mb_doc_acl_items (Union[Unset, str]):
            data_organisation_table (Union[Unset, int]): Store index values in columns of a dedicated table.
            guid_ms_sharepoint_document (Union[Unset, str]): Prefefined GUID for a keywording form for MS Sharepoint
                documents.
            max_mask_ids_for_child_entries (Union[Unset, int]): Maximum number of keywording form IDs for {@link
                DocMask#maskIdsForChildEntries}.
            guid_user_folder (Union[Unset, str]): Predefined GUID for the keywording form used by user folders.
            mb_mask_lines (Union[Unset, str]): Member bit: read or write index lines.
            mb_only_lock (Union[Unset, DocMaskZ]): This class encapsulates the constants of the DocMaskC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_all_members (Union[Unset, str]): Member bit: read or write all elements.
            mb_acl (Union[Unset, str]): Member bit: ACL
            mb_deletion_deadline (Union[Unset, str]): Member bit for {@link DocMask#deletionDeadline}.
            mb_all (Union[Unset, DocMaskZ]): This class encapsulates the constants of the DocMaskC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            data_organisation_objkeys (Union[Unset, int]): Store index values as key-value-pairs in the objkeys table.
            guid_folder (Union[Unset, str]): Predefined GUID for the keywording form used for folders by default.
            guid_contact (Union[Unset, str]): Predefined GUID for keywording form "Kontakt".
            guid_eloscripts (Union[Unset, str]): Predefined GUID for the keywording form used for scripts.
            mb_acl_items (Union[Unset, str]): Member bit: use the ACL items in the member DocMask.aclItems and DocMask.
                docAclItems for
                 reading and writing.
            guid_structure_element (Union[Unset, str]): Predefined GUID for keywording form "Strukturelement".
            data_organisation_aspect (Union[Unset, int]): Keywording form is based on aspects.
            mb_deleted (Union[Unset, str]):
            guid_search (Union[Unset, str]): Predefined GUID for the keywording form used to search entries regardless of
                their storage
                mask.
    """

    mb_transitive_children: Union[Unset, str] = UNSET
    mb_sort_order_not_archiving_mode: Union[Unset, str] = UNSET
    guid_email: Union[Unset, str] = UNSET
    mb_aspect_assocs: Union[Unset, str] = UNSET
    mb_lines: Union[Unset, str] = UNSET
    guid_basic: Union[Unset, str] = UNSET
    mb_details: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_inherit_from_masks: Union[Unset, str] = UNSET
    mb_doc_acl_items: Union[Unset, str] = UNSET
    data_organisation_table: Union[Unset, int] = UNSET
    guid_ms_sharepoint_document: Union[Unset, str] = UNSET
    max_mask_ids_for_child_entries: Union[Unset, int] = UNSET
    guid_user_folder: Union[Unset, str] = UNSET
    mb_mask_lines: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "DocMaskZ"] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    mb_deletion_deadline: Union[Unset, str] = UNSET
    mb_all: Union[Unset, "DocMaskZ"] = UNSET
    data_organisation_objkeys: Union[Unset, int] = UNSET
    guid_folder: Union[Unset, str] = UNSET
    guid_contact: Union[Unset, str] = UNSET
    guid_eloscripts: Union[Unset, str] = UNSET
    mb_acl_items: Union[Unset, str] = UNSET
    guid_structure_element: Union[Unset, str] = UNSET
    data_organisation_aspect: Union[Unset, int] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    guid_search: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_transitive_children = self.mb_transitive_children

        mb_sort_order_not_archiving_mode = self.mb_sort_order_not_archiving_mode

        guid_email = self.guid_email

        mb_aspect_assocs = self.mb_aspect_assocs

        mb_lines = self.mb_lines

        guid_basic = self.guid_basic

        mb_details = self.mb_details

        ln_acl = self.ln_acl

        mb_inherit_from_masks = self.mb_inherit_from_masks

        mb_doc_acl_items = self.mb_doc_acl_items

        data_organisation_table = self.data_organisation_table

        guid_ms_sharepoint_document = self.guid_ms_sharepoint_document

        max_mask_ids_for_child_entries = self.max_mask_ids_for_child_entries

        guid_user_folder = self.guid_user_folder

        mb_mask_lines = self.mb_mask_lines

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_all_members = self.mb_all_members

        mb_acl = self.mb_acl

        mb_deletion_deadline = self.mb_deletion_deadline

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        data_organisation_objkeys = self.data_organisation_objkeys

        guid_folder = self.guid_folder

        guid_contact = self.guid_contact

        guid_eloscripts = self.guid_eloscripts

        mb_acl_items = self.mb_acl_items

        guid_structure_element = self.guid_structure_element

        data_organisation_aspect = self.data_organisation_aspect

        mb_deleted = self.mb_deleted

        guid_search = self.guid_search

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_transitive_children is not UNSET:
            field_dict["mbTransitiveChildren"] = mb_transitive_children
        if mb_sort_order_not_archiving_mode is not UNSET:
            field_dict["mbSortOrderNotArchivingMode"] = mb_sort_order_not_archiving_mode
        if guid_email is not UNSET:
            field_dict["GUID_EMAIL"] = guid_email
        if mb_aspect_assocs is not UNSET:
            field_dict["mbAspectAssocs"] = mb_aspect_assocs
        if mb_lines is not UNSET:
            field_dict["mbLines"] = mb_lines
        if guid_basic is not UNSET:
            field_dict["GUID_BASIC"] = guid_basic
        if mb_details is not UNSET:
            field_dict["mbDetails"] = mb_details
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_inherit_from_masks is not UNSET:
            field_dict["mbInheritFromMasks"] = mb_inherit_from_masks
        if mb_doc_acl_items is not UNSET:
            field_dict["mbDocAclItems"] = mb_doc_acl_items
        if data_organisation_table is not UNSET:
            field_dict["DATA_ORGANISATION_TABLE"] = data_organisation_table
        if guid_ms_sharepoint_document is not UNSET:
            field_dict["GUID_MS_SHAREPOINT_DOCUMENT"] = guid_ms_sharepoint_document
        if max_mask_ids_for_child_entries is not UNSET:
            field_dict["MAX_MASK_IDS_FOR_CHILD_ENTRIES"] = max_mask_ids_for_child_entries
        if guid_user_folder is not UNSET:
            field_dict["GUID_USER_FOLDER"] = guid_user_folder
        if mb_mask_lines is not UNSET:
            field_dict["mbMaskLines"] = mb_mask_lines
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if mb_deletion_deadline is not UNSET:
            field_dict["mbDeletionDeadline"] = mb_deletion_deadline
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if data_organisation_objkeys is not UNSET:
            field_dict["DATA_ORGANISATION_OBJKEYS"] = data_organisation_objkeys
        if guid_folder is not UNSET:
            field_dict["GUID_FOLDER"] = guid_folder
        if guid_contact is not UNSET:
            field_dict["GUID_CONTACT"] = guid_contact
        if guid_eloscripts is not UNSET:
            field_dict["GUID_ELOSCRIPTS"] = guid_eloscripts
        if mb_acl_items is not UNSET:
            field_dict["mbAclItems"] = mb_acl_items
        if guid_structure_element is not UNSET:
            field_dict["GUID_STRUCTURE_ELEMENT"] = guid_structure_element
        if data_organisation_aspect is not UNSET:
            field_dict["DATA_ORGANISATION_ASPECT"] = data_organisation_aspect
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if guid_search is not UNSET:
            field_dict["GUID_SEARCH"] = guid_search

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask_z import DocMaskZ

        d = src_dict.copy()
        mb_transitive_children = d.pop("mbTransitiveChildren", UNSET)

        mb_sort_order_not_archiving_mode = d.pop("mbSortOrderNotArchivingMode", UNSET)

        guid_email = d.pop("GUID_EMAIL", UNSET)

        mb_aspect_assocs = d.pop("mbAspectAssocs", UNSET)

        mb_lines = d.pop("mbLines", UNSET)

        guid_basic = d.pop("GUID_BASIC", UNSET)

        mb_details = d.pop("mbDetails", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_inherit_from_masks = d.pop("mbInheritFromMasks", UNSET)

        mb_doc_acl_items = d.pop("mbDocAclItems", UNSET)

        data_organisation_table = d.pop("DATA_ORGANISATION_TABLE", UNSET)

        guid_ms_sharepoint_document = d.pop("GUID_MS_SHAREPOINT_DOCUMENT", UNSET)

        max_mask_ids_for_child_entries = d.pop("MAX_MASK_IDS_FOR_CHILD_ENTRIES", UNSET)

        guid_user_folder = d.pop("GUID_USER_FOLDER", UNSET)

        mb_mask_lines = d.pop("mbMaskLines", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, DocMaskZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = DocMaskZ.from_dict(_mb_only_lock)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        mb_deletion_deadline = d.pop("mbDeletionDeadline", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, DocMaskZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = DocMaskZ.from_dict(_mb_all)

        data_organisation_objkeys = d.pop("DATA_ORGANISATION_OBJKEYS", UNSET)

        guid_folder = d.pop("GUID_FOLDER", UNSET)

        guid_contact = d.pop("GUID_CONTACT", UNSET)

        guid_eloscripts = d.pop("GUID_ELOSCRIPTS", UNSET)

        mb_acl_items = d.pop("mbAclItems", UNSET)

        guid_structure_element = d.pop("GUID_STRUCTURE_ELEMENT", UNSET)

        data_organisation_aspect = d.pop("DATA_ORGANISATION_ASPECT", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        guid_search = d.pop("GUID_SEARCH", UNSET)

        doc_mask_c = cls(
            mb_transitive_children=mb_transitive_children,
            mb_sort_order_not_archiving_mode=mb_sort_order_not_archiving_mode,
            guid_email=guid_email,
            mb_aspect_assocs=mb_aspect_assocs,
            mb_lines=mb_lines,
            guid_basic=guid_basic,
            mb_details=mb_details,
            ln_acl=ln_acl,
            mb_inherit_from_masks=mb_inherit_from_masks,
            mb_doc_acl_items=mb_doc_acl_items,
            data_organisation_table=data_organisation_table,
            guid_ms_sharepoint_document=guid_ms_sharepoint_document,
            max_mask_ids_for_child_entries=max_mask_ids_for_child_entries,
            guid_user_folder=guid_user_folder,
            mb_mask_lines=mb_mask_lines,
            mb_only_lock=mb_only_lock,
            mb_all_members=mb_all_members,
            mb_acl=mb_acl,
            mb_deletion_deadline=mb_deletion_deadline,
            mb_all=mb_all,
            data_organisation_objkeys=data_organisation_objkeys,
            guid_folder=guid_folder,
            guid_contact=guid_contact,
            guid_eloscripts=guid_eloscripts,
            mb_acl_items=mb_acl_items,
            guid_structure_element=guid_structure_element,
            data_organisation_aspect=data_organisation_aspect,
            mb_deleted=mb_deleted,
            guid_search=guid_search,
        )

        doc_mask_c.additional_properties = d
        return doc_mask_c

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
