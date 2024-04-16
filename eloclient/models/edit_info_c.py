from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_info_z import EditInfoZ


T = TypeVar("T", bound="EditInfoC")


@_attrs_define
class EditInfoC:
    """<p>
    Constants to read data for editing the indexing information of an archive entry
     </p>

        Attributes:
            mb_note_members (Union[Unset, str]): Return notes in checkoutSord and checkoutDoc.
            mb_basic_data (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_sord_notes (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_mask_names (Union[Unset, str]): Mask names.
            mb_only_id (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_marker_names (Union[Unset, str]): Marker names (colors).
            mb_sord (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_sord_preview_small_content (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC
                class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_all_members_lazy (Union[Unset, str]): As {@link #mbAllMembers} but provides {@link EditInfo#mask}, {@link
                EditInfo#sordTypes} and
                {@link EditInfo#keywords} for lazy loading.
            mb_only_lock (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_all_members (Union[Unset, str]): All members: indexing information + basic data + document + attachment +
                signature
            mb_sord_doc_att (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_attachment_members (Union[Unset, str]): Information to download the attachment of the archive entry.
            mb_phys_path (Union[Unset, str]): Return the physical path of the document in checkoutDoc.
                This requires a request to Document
                 Mangager.
            mb_attachment (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_all (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_document_members (Union[Unset, str]): Information to download the document of the archive entry.
            mb_mask (Union[Unset, str]): Complete data of the mask of the specified object.
            mb_sord_types_jpg (Union[Unset, str]): List of Sord types (labels, icons, extensions corresponding to
                Sord.type).
                Icon images are
                 returned in JPEG format.
            mb_aspect_infos (Union[Unset, str]): Aspect infos.
            mb_sord_content_stream (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_sord_doc_small_content (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC
                class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_notes (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_sord_doc_att_content_stream (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC
                class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_sord_doc (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_preview_members (Union[Unset, str]): Return document preview in checkoutDoc
            mb_sord_lean (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_signature_members (Union[Unset, str]): Information to download the signature of the archive entry.
            mb_repl_names (Union[Unset, str]): Names of all replication sets.
            mb_path_names (Union[Unset, str]): Path names.
            mb_doc_templates (Union[Unset, str]): RESERVED. Document templates.
            mb_document (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
                EditInfo also returns a Sord object
                 and a SordZ member is included to control the Sord data returned.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_keyword_members (Union[Unset, str]): Return keywords in checkoutSord and checkoutDoc.
    """

    mb_note_members: Union[Unset, str] = UNSET
    mb_basic_data: Union[Unset, "EditInfoZ"] = UNSET
    mb_sord_notes: Union[Unset, "EditInfoZ"] = UNSET
    mb_mask_names: Union[Unset, str] = UNSET
    mb_only_id: Union[Unset, "EditInfoZ"] = UNSET
    mb_marker_names: Union[Unset, str] = UNSET
    mb_sord: Union[Unset, "EditInfoZ"] = UNSET
    mb_sord_preview_small_content: Union[Unset, "EditInfoZ"] = UNSET
    mb_all_members_lazy: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "EditInfoZ"] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_sord_doc_att: Union[Unset, "EditInfoZ"] = UNSET
    mb_attachment_members: Union[Unset, str] = UNSET
    mb_phys_path: Union[Unset, str] = UNSET
    mb_attachment: Union[Unset, "EditInfoZ"] = UNSET
    mb_all: Union[Unset, "EditInfoZ"] = UNSET
    mb_document_members: Union[Unset, str] = UNSET
    mb_mask: Union[Unset, str] = UNSET
    mb_sord_types_jpg: Union[Unset, str] = UNSET
    mb_aspect_infos: Union[Unset, str] = UNSET
    mb_sord_content_stream: Union[Unset, "EditInfoZ"] = UNSET
    mb_sord_doc_small_content: Union[Unset, "EditInfoZ"] = UNSET
    mb_notes: Union[Unset, "EditInfoZ"] = UNSET
    mb_sord_doc_att_content_stream: Union[Unset, "EditInfoZ"] = UNSET
    mb_sord_doc: Union[Unset, "EditInfoZ"] = UNSET
    mb_preview_members: Union[Unset, str] = UNSET
    mb_sord_lean: Union[Unset, "EditInfoZ"] = UNSET
    mb_signature_members: Union[Unset, str] = UNSET
    mb_repl_names: Union[Unset, str] = UNSET
    mb_path_names: Union[Unset, str] = UNSET
    mb_doc_templates: Union[Unset, str] = UNSET
    mb_document: Union[Unset, "EditInfoZ"] = UNSET
    mb_keyword_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_note_members = self.mb_note_members

        mb_basic_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_basic_data, Unset):
            mb_basic_data = self.mb_basic_data.to_dict()

        mb_sord_notes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_notes, Unset):
            mb_sord_notes = self.mb_sord_notes.to_dict()

        mb_mask_names = self.mb_mask_names

        mb_only_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_id, Unset):
            mb_only_id = self.mb_only_id.to_dict()

        mb_marker_names = self.mb_marker_names

        mb_sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord, Unset):
            mb_sord = self.mb_sord.to_dict()

        mb_sord_preview_small_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_preview_small_content, Unset):
            mb_sord_preview_small_content = self.mb_sord_preview_small_content.to_dict()

        mb_all_members_lazy = self.mb_all_members_lazy

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_all_members = self.mb_all_members

        mb_sord_doc_att: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_doc_att, Unset):
            mb_sord_doc_att = self.mb_sord_doc_att.to_dict()

        mb_attachment_members = self.mb_attachment_members

        mb_phys_path = self.mb_phys_path

        mb_attachment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_attachment, Unset):
            mb_attachment = self.mb_attachment.to_dict()

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_document_members = self.mb_document_members

        mb_mask = self.mb_mask

        mb_sord_types_jpg = self.mb_sord_types_jpg

        mb_aspect_infos = self.mb_aspect_infos

        mb_sord_content_stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_content_stream, Unset):
            mb_sord_content_stream = self.mb_sord_content_stream.to_dict()

        mb_sord_doc_small_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_doc_small_content, Unset):
            mb_sord_doc_small_content = self.mb_sord_doc_small_content.to_dict()

        mb_notes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_notes, Unset):
            mb_notes = self.mb_notes.to_dict()

        mb_sord_doc_att_content_stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_doc_att_content_stream, Unset):
            mb_sord_doc_att_content_stream = self.mb_sord_doc_att_content_stream.to_dict()

        mb_sord_doc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_doc, Unset):
            mb_sord_doc = self.mb_sord_doc.to_dict()

        mb_preview_members = self.mb_preview_members

        mb_sord_lean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_sord_lean, Unset):
            mb_sord_lean = self.mb_sord_lean.to_dict()

        mb_signature_members = self.mb_signature_members

        mb_repl_names = self.mb_repl_names

        mb_path_names = self.mb_path_names

        mb_doc_templates = self.mb_doc_templates

        mb_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_document, Unset):
            mb_document = self.mb_document.to_dict()

        mb_keyword_members = self.mb_keyword_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_note_members is not UNSET:
            field_dict["mbNoteMembers"] = mb_note_members
        if mb_basic_data is not UNSET:
            field_dict["mbBasicData"] = mb_basic_data
        if mb_sord_notes is not UNSET:
            field_dict["mbSordNotes"] = mb_sord_notes
        if mb_mask_names is not UNSET:
            field_dict["mbMaskNames"] = mb_mask_names
        if mb_only_id is not UNSET:
            field_dict["mbOnlyId"] = mb_only_id
        if mb_marker_names is not UNSET:
            field_dict["mbMarkerNames"] = mb_marker_names
        if mb_sord is not UNSET:
            field_dict["mbSord"] = mb_sord
        if mb_sord_preview_small_content is not UNSET:
            field_dict["mbSordPreviewSmallContent"] = mb_sord_preview_small_content
        if mb_all_members_lazy is not UNSET:
            field_dict["mbAllMembersLazy"] = mb_all_members_lazy
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_sord_doc_att is not UNSET:
            field_dict["mbSordDocAtt"] = mb_sord_doc_att
        if mb_attachment_members is not UNSET:
            field_dict["mbAttachmentMembers"] = mb_attachment_members
        if mb_phys_path is not UNSET:
            field_dict["mbPhysPath"] = mb_phys_path
        if mb_attachment is not UNSET:
            field_dict["mbAttachment"] = mb_attachment
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_document_members is not UNSET:
            field_dict["mbDocumentMembers"] = mb_document_members
        if mb_mask is not UNSET:
            field_dict["mbMask"] = mb_mask
        if mb_sord_types_jpg is not UNSET:
            field_dict["mbSordTypesJPG"] = mb_sord_types_jpg
        if mb_aspect_infos is not UNSET:
            field_dict["mbAspectInfos"] = mb_aspect_infos
        if mb_sord_content_stream is not UNSET:
            field_dict["mbSordContentStream"] = mb_sord_content_stream
        if mb_sord_doc_small_content is not UNSET:
            field_dict["mbSordDocSmallContent"] = mb_sord_doc_small_content
        if mb_notes is not UNSET:
            field_dict["mbNotes"] = mb_notes
        if mb_sord_doc_att_content_stream is not UNSET:
            field_dict["mbSordDocAttContentStream"] = mb_sord_doc_att_content_stream
        if mb_sord_doc is not UNSET:
            field_dict["mbSordDoc"] = mb_sord_doc
        if mb_preview_members is not UNSET:
            field_dict["mbPreviewMembers"] = mb_preview_members
        if mb_sord_lean is not UNSET:
            field_dict["mbSordLean"] = mb_sord_lean
        if mb_signature_members is not UNSET:
            field_dict["mbSignatureMembers"] = mb_signature_members
        if mb_repl_names is not UNSET:
            field_dict["mbReplNames"] = mb_repl_names
        if mb_path_names is not UNSET:
            field_dict["mbPathNames"] = mb_path_names
        if mb_doc_templates is not UNSET:
            field_dict["mbDocTemplates"] = mb_doc_templates
        if mb_document is not UNSET:
            field_dict["mbDocument"] = mb_document
        if mb_keyword_members is not UNSET:
            field_dict["mbKeywordMembers"] = mb_keyword_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.edit_info_z import EditInfoZ

        d = src_dict.copy()
        mb_note_members = d.pop("mbNoteMembers", UNSET)

        _mb_basic_data = d.pop("mbBasicData", UNSET)
        mb_basic_data: Union[Unset, EditInfoZ]
        if isinstance(_mb_basic_data, Unset):
            mb_basic_data = UNSET
        else:
            mb_basic_data = EditInfoZ.from_dict(_mb_basic_data)

        _mb_sord_notes = d.pop("mbSordNotes", UNSET)
        mb_sord_notes: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_notes, Unset):
            mb_sord_notes = UNSET
        else:
            mb_sord_notes = EditInfoZ.from_dict(_mb_sord_notes)

        mb_mask_names = d.pop("mbMaskNames", UNSET)

        _mb_only_id = d.pop("mbOnlyId", UNSET)
        mb_only_id: Union[Unset, EditInfoZ]
        if isinstance(_mb_only_id, Unset):
            mb_only_id = UNSET
        else:
            mb_only_id = EditInfoZ.from_dict(_mb_only_id)

        mb_marker_names = d.pop("mbMarkerNames", UNSET)

        _mb_sord = d.pop("mbSord", UNSET)
        mb_sord: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord, Unset):
            mb_sord = UNSET
        else:
            mb_sord = EditInfoZ.from_dict(_mb_sord)

        _mb_sord_preview_small_content = d.pop("mbSordPreviewSmallContent", UNSET)
        mb_sord_preview_small_content: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_preview_small_content, Unset):
            mb_sord_preview_small_content = UNSET
        else:
            mb_sord_preview_small_content = EditInfoZ.from_dict(_mb_sord_preview_small_content)

        mb_all_members_lazy = d.pop("mbAllMembersLazy", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, EditInfoZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = EditInfoZ.from_dict(_mb_only_lock)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        _mb_sord_doc_att = d.pop("mbSordDocAtt", UNSET)
        mb_sord_doc_att: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_doc_att, Unset):
            mb_sord_doc_att = UNSET
        else:
            mb_sord_doc_att = EditInfoZ.from_dict(_mb_sord_doc_att)

        mb_attachment_members = d.pop("mbAttachmentMembers", UNSET)

        mb_phys_path = d.pop("mbPhysPath", UNSET)

        _mb_attachment = d.pop("mbAttachment", UNSET)
        mb_attachment: Union[Unset, EditInfoZ]
        if isinstance(_mb_attachment, Unset):
            mb_attachment = UNSET
        else:
            mb_attachment = EditInfoZ.from_dict(_mb_attachment)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, EditInfoZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = EditInfoZ.from_dict(_mb_all)

        mb_document_members = d.pop("mbDocumentMembers", UNSET)

        mb_mask = d.pop("mbMask", UNSET)

        mb_sord_types_jpg = d.pop("mbSordTypesJPG", UNSET)

        mb_aspect_infos = d.pop("mbAspectInfos", UNSET)

        _mb_sord_content_stream = d.pop("mbSordContentStream", UNSET)
        mb_sord_content_stream: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_content_stream, Unset):
            mb_sord_content_stream = UNSET
        else:
            mb_sord_content_stream = EditInfoZ.from_dict(_mb_sord_content_stream)

        _mb_sord_doc_small_content = d.pop("mbSordDocSmallContent", UNSET)
        mb_sord_doc_small_content: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_doc_small_content, Unset):
            mb_sord_doc_small_content = UNSET
        else:
            mb_sord_doc_small_content = EditInfoZ.from_dict(_mb_sord_doc_small_content)

        _mb_notes = d.pop("mbNotes", UNSET)
        mb_notes: Union[Unset, EditInfoZ]
        if isinstance(_mb_notes, Unset):
            mb_notes = UNSET
        else:
            mb_notes = EditInfoZ.from_dict(_mb_notes)

        _mb_sord_doc_att_content_stream = d.pop("mbSordDocAttContentStream", UNSET)
        mb_sord_doc_att_content_stream: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_doc_att_content_stream, Unset):
            mb_sord_doc_att_content_stream = UNSET
        else:
            mb_sord_doc_att_content_stream = EditInfoZ.from_dict(_mb_sord_doc_att_content_stream)

        _mb_sord_doc = d.pop("mbSordDoc", UNSET)
        mb_sord_doc: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_doc, Unset):
            mb_sord_doc = UNSET
        else:
            mb_sord_doc = EditInfoZ.from_dict(_mb_sord_doc)

        mb_preview_members = d.pop("mbPreviewMembers", UNSET)

        _mb_sord_lean = d.pop("mbSordLean", UNSET)
        mb_sord_lean: Union[Unset, EditInfoZ]
        if isinstance(_mb_sord_lean, Unset):
            mb_sord_lean = UNSET
        else:
            mb_sord_lean = EditInfoZ.from_dict(_mb_sord_lean)

        mb_signature_members = d.pop("mbSignatureMembers", UNSET)

        mb_repl_names = d.pop("mbReplNames", UNSET)

        mb_path_names = d.pop("mbPathNames", UNSET)

        mb_doc_templates = d.pop("mbDocTemplates", UNSET)

        _mb_document = d.pop("mbDocument", UNSET)
        mb_document: Union[Unset, EditInfoZ]
        if isinstance(_mb_document, Unset):
            mb_document = UNSET
        else:
            mb_document = EditInfoZ.from_dict(_mb_document)

        mb_keyword_members = d.pop("mbKeywordMembers", UNSET)

        edit_info_c = cls(
            mb_note_members=mb_note_members,
            mb_basic_data=mb_basic_data,
            mb_sord_notes=mb_sord_notes,
            mb_mask_names=mb_mask_names,
            mb_only_id=mb_only_id,
            mb_marker_names=mb_marker_names,
            mb_sord=mb_sord,
            mb_sord_preview_small_content=mb_sord_preview_small_content,
            mb_all_members_lazy=mb_all_members_lazy,
            mb_only_lock=mb_only_lock,
            mb_all_members=mb_all_members,
            mb_sord_doc_att=mb_sord_doc_att,
            mb_attachment_members=mb_attachment_members,
            mb_phys_path=mb_phys_path,
            mb_attachment=mb_attachment,
            mb_all=mb_all,
            mb_document_members=mb_document_members,
            mb_mask=mb_mask,
            mb_sord_types_jpg=mb_sord_types_jpg,
            mb_aspect_infos=mb_aspect_infos,
            mb_sord_content_stream=mb_sord_content_stream,
            mb_sord_doc_small_content=mb_sord_doc_small_content,
            mb_notes=mb_notes,
            mb_sord_doc_att_content_stream=mb_sord_doc_att_content_stream,
            mb_sord_doc=mb_sord_doc,
            mb_preview_members=mb_preview_members,
            mb_sord_lean=mb_sord_lean,
            mb_signature_members=mb_signature_members,
            mb_repl_names=mb_repl_names,
            mb_path_names=mb_path_names,
            mb_doc_templates=mb_doc_templates,
            mb_document=mb_document,
            mb_keyword_members=mb_keyword_members,
        )

        edit_info_c.additional_properties = d
        return edit_info_c

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
