from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_z import NoteZ


T = TypeVar("T", bound="NoteC")


@_attrs_define
class NoteC:
    """<p>
    Constants for notes.
     </p>

        Attributes:
            type_annotation_line (Union[Unset, int]): Note type: reserved
            type_annotation_note (Union[Unset, int]): Note type: annotation text
            type_normal_acl (Union[Unset, int]): Note type: standard ACL
            type_annotation_filetext (Union[Unset, int]): Note type: reserved
            type_annotation_note_withfont (Union[Unset, int]): Draws a filled rectangular box on a document and displays
                text in the box.
            type_none (Union[Unset, int]): Note type: needed in FindByNotes to indicate typeless filtering
            type_annotation_rectangle (Union[Unset, int]): Note type: reserved
            mb_obj_id (Union[Unset, str]): Member objId.
            mb_only_lock (Union[Unset, NoteZ]): This class encapsulates the constants of the NoteC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            type_anotewg_note (Union[Unset, int]): Use TYPE_ANNOTATION_NOTE
            type_anotew_marker (Union[Unset, int]): Use TYPE_ANNOTATION_MARKER
            type_annotation_stamp (Union[Unset, int]): Adds a stamp, such as a received date for example, to a document.
                <p>
                 The font size in the client application has to be computed by FontInfo.height * 3.7 *
                 resolution_in_dpi/100
                 </p>
            type_personal (Union[Unset, int]): Note type: standard green note
            type_annotation_hollowrectangle (Union[Unset, int]): Note type: draws a hollow rectangle (frame) on a document.
            mb_all (Union[Unset, NoteZ]): This class encapsulates the constants of the NoteC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_note_text (Union[Unset, str]): Member noteText
            mb_lock_id (Union[Unset, str]): Member lockId
            mb_create_date_iso (Union[Unset, str]):
            type_annotation_horizontal_line (Union[Unset, int]): Note type: horizontal line.
            type_annotation_marker (Union[Unset, int]): Note type: highlighting rectange (filled) on the document.
                <p>
                 If the note is assigned the colour 0xC0C0C0 the note will be interpreted by ELODM. In this case
                 a black rectangle will painted on the document, using the note coordinates supplied, if the
                 note ACL does not contain sufficient read access rights for the current user. This allows
                 document contact to be blacked out for certain users The document must be a graphic based
                 document, eg. tiff, bmp etc.
                 </p>
            mb_note_image (Union[Unset, str]): Member noteImage
            type_annotation_stamp_new (Union[Unset, int]): Note type: adds a stamp, such as a received date for example, to
                a document.
                <p>
                 The font size in the client application has to be computed by FontInfo.height * 2.2 *
                 resolution_in_dpi/100
                 </p>
            color_annotation_marker_dm (Union[Unset, int]): This color is used for notes of type TYPE_ANNOTATION_MARKER to
                specify a black rectangle that
                is painted on the document by Document Manager.
            mb_note_freehand (Union[Unset, str]): Member noteFreehand
            mb_acl_items (Union[Unset, str]):
            type_annotation_text (Union[Unset, int]): Annotation with text but without a rectangle.
                <p>
                 The font size in the client application has to be computed by FontInfo.height * 3.7 *
                 resolution_in_dpi/100
                 </p>
            type_stamp (Union[Unset, int]): Note type: standard red note
            type_annotation_freehand (Union[Unset, int]): Note type: freehand line.
            type_annotation_filledrectangle (Union[Unset, int]): Note type: draws a filled coloured box on the document,
                over the existing document.
            type_normal (Union[Unset, int]): Note type: standard yellow note
            mb_deleted (Union[Unset, str]):
            mb_no_desc (Union[Unset, NoteZ]): This class encapsulates the constants of the NoteC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            type_annotation_strikeout (Union[Unset, int]): Note type: strike out text
    """

    type_annotation_line: Union[Unset, int] = UNSET
    type_annotation_note: Union[Unset, int] = UNSET
    type_normal_acl: Union[Unset, int] = UNSET
    type_annotation_filetext: Union[Unset, int] = UNSET
    type_annotation_note_withfont: Union[Unset, int] = UNSET
    type_none: Union[Unset, int] = UNSET
    type_annotation_rectangle: Union[Unset, int] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "NoteZ"] = UNSET
    type_anotewg_note: Union[Unset, int] = UNSET
    type_anotew_marker: Union[Unset, int] = UNSET
    type_annotation_stamp: Union[Unset, int] = UNSET
    type_personal: Union[Unset, int] = UNSET
    type_annotation_hollowrectangle: Union[Unset, int] = UNSET
    mb_all: Union[Unset, "NoteZ"] = UNSET
    mb_note_text: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    type_annotation_horizontal_line: Union[Unset, int] = UNSET
    type_annotation_marker: Union[Unset, int] = UNSET
    mb_note_image: Union[Unset, str] = UNSET
    type_annotation_stamp_new: Union[Unset, int] = UNSET
    color_annotation_marker_dm: Union[Unset, int] = UNSET
    mb_note_freehand: Union[Unset, str] = UNSET
    mb_acl_items: Union[Unset, str] = UNSET
    type_annotation_text: Union[Unset, int] = UNSET
    type_stamp: Union[Unset, int] = UNSET
    type_annotation_freehand: Union[Unset, int] = UNSET
    type_annotation_filledrectangle: Union[Unset, int] = UNSET
    type_normal: Union[Unset, int] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    mb_no_desc: Union[Unset, "NoteZ"] = UNSET
    type_annotation_strikeout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_annotation_line = self.type_annotation_line

        type_annotation_note = self.type_annotation_note

        type_normal_acl = self.type_normal_acl

        type_annotation_filetext = self.type_annotation_filetext

        type_annotation_note_withfont = self.type_annotation_note_withfont

        type_none = self.type_none

        type_annotation_rectangle = self.type_annotation_rectangle

        mb_obj_id = self.mb_obj_id

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        type_anotewg_note = self.type_anotewg_note

        type_anotew_marker = self.type_anotew_marker

        type_annotation_stamp = self.type_annotation_stamp

        type_personal = self.type_personal

        type_annotation_hollowrectangle = self.type_annotation_hollowrectangle

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_note_text = self.mb_note_text

        mb_lock_id = self.mb_lock_id

        mb_create_date_iso = self.mb_create_date_iso

        type_annotation_horizontal_line = self.type_annotation_horizontal_line

        type_annotation_marker = self.type_annotation_marker

        mb_note_image = self.mb_note_image

        type_annotation_stamp_new = self.type_annotation_stamp_new

        color_annotation_marker_dm = self.color_annotation_marker_dm

        mb_note_freehand = self.mb_note_freehand

        mb_acl_items = self.mb_acl_items

        type_annotation_text = self.type_annotation_text

        type_stamp = self.type_stamp

        type_annotation_freehand = self.type_annotation_freehand

        type_annotation_filledrectangle = self.type_annotation_filledrectangle

        type_normal = self.type_normal

        mb_deleted = self.mb_deleted

        mb_no_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_no_desc, Unset):
            mb_no_desc = self.mb_no_desc.to_dict()

        type_annotation_strikeout = self.type_annotation_strikeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_annotation_line is not UNSET:
            field_dict["TYPE_ANNOTATION_LINE"] = type_annotation_line
        if type_annotation_note is not UNSET:
            field_dict["TYPE_ANNOTATION_NOTE"] = type_annotation_note
        if type_normal_acl is not UNSET:
            field_dict["TYPE_NORMAL_ACL"] = type_normal_acl
        if type_annotation_filetext is not UNSET:
            field_dict["TYPE_ANNOTATION_FILETEXT"] = type_annotation_filetext
        if type_annotation_note_withfont is not UNSET:
            field_dict["TYPE_ANNOTATION_NOTE_WITHFONT"] = type_annotation_note_withfont
        if type_none is not UNSET:
            field_dict["TYPE_NONE"] = type_none
        if type_annotation_rectangle is not UNSET:
            field_dict["TYPE_ANNOTATION_RECTANGLE"] = type_annotation_rectangle
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if type_anotewg_note is not UNSET:
            field_dict["TYPE_ANOTEWG_NOTE"] = type_anotewg_note
        if type_anotew_marker is not UNSET:
            field_dict["TYPE_ANOTEW_MARKER"] = type_anotew_marker
        if type_annotation_stamp is not UNSET:
            field_dict["TYPE_ANNOTATION_STAMP"] = type_annotation_stamp
        if type_personal is not UNSET:
            field_dict["TYPE_PERSONAL"] = type_personal
        if type_annotation_hollowrectangle is not UNSET:
            field_dict["TYPE_ANNOTATION_HOLLOWRECTANGLE"] = type_annotation_hollowrectangle
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_note_text is not UNSET:
            field_dict["mbNoteText"] = mb_note_text
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if type_annotation_horizontal_line is not UNSET:
            field_dict["TYPE_ANNOTATION_HORIZONTAL_LINE"] = type_annotation_horizontal_line
        if type_annotation_marker is not UNSET:
            field_dict["TYPE_ANNOTATION_MARKER"] = type_annotation_marker
        if mb_note_image is not UNSET:
            field_dict["mbNoteImage"] = mb_note_image
        if type_annotation_stamp_new is not UNSET:
            field_dict["TYPE_ANNOTATION_STAMP_NEW"] = type_annotation_stamp_new
        if color_annotation_marker_dm is not UNSET:
            field_dict["COLOR_ANNOTATION_MARKER_DM"] = color_annotation_marker_dm
        if mb_note_freehand is not UNSET:
            field_dict["mbNoteFreehand"] = mb_note_freehand
        if mb_acl_items is not UNSET:
            field_dict["mbAclItems"] = mb_acl_items
        if type_annotation_text is not UNSET:
            field_dict["TYPE_ANNOTATION_TEXT"] = type_annotation_text
        if type_stamp is not UNSET:
            field_dict["TYPE_STAMP"] = type_stamp
        if type_annotation_freehand is not UNSET:
            field_dict["TYPE_ANNOTATION_FREEHAND"] = type_annotation_freehand
        if type_annotation_filledrectangle is not UNSET:
            field_dict["TYPE_ANNOTATION_FILLEDRECTANGLE"] = type_annotation_filledrectangle
        if type_normal is not UNSET:
            field_dict["TYPE_NORMAL"] = type_normal
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if mb_no_desc is not UNSET:
            field_dict["mbNoDesc"] = mb_no_desc
        if type_annotation_strikeout is not UNSET:
            field_dict["TYPE_ANNOTATION_STRIKEOUT"] = type_annotation_strikeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_z import NoteZ

        d = src_dict.copy()
        type_annotation_line = d.pop("TYPE_ANNOTATION_LINE", UNSET)

        type_annotation_note = d.pop("TYPE_ANNOTATION_NOTE", UNSET)

        type_normal_acl = d.pop("TYPE_NORMAL_ACL", UNSET)

        type_annotation_filetext = d.pop("TYPE_ANNOTATION_FILETEXT", UNSET)

        type_annotation_note_withfont = d.pop("TYPE_ANNOTATION_NOTE_WITHFONT", UNSET)

        type_none = d.pop("TYPE_NONE", UNSET)

        type_annotation_rectangle = d.pop("TYPE_ANNOTATION_RECTANGLE", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, NoteZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = NoteZ.from_dict(_mb_only_lock)

        type_anotewg_note = d.pop("TYPE_ANOTEWG_NOTE", UNSET)

        type_anotew_marker = d.pop("TYPE_ANOTEW_MARKER", UNSET)

        type_annotation_stamp = d.pop("TYPE_ANNOTATION_STAMP", UNSET)

        type_personal = d.pop("TYPE_PERSONAL", UNSET)

        type_annotation_hollowrectangle = d.pop("TYPE_ANNOTATION_HOLLOWRECTANGLE", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, NoteZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = NoteZ.from_dict(_mb_all)

        mb_note_text = d.pop("mbNoteText", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        type_annotation_horizontal_line = d.pop("TYPE_ANNOTATION_HORIZONTAL_LINE", UNSET)

        type_annotation_marker = d.pop("TYPE_ANNOTATION_MARKER", UNSET)

        mb_note_image = d.pop("mbNoteImage", UNSET)

        type_annotation_stamp_new = d.pop("TYPE_ANNOTATION_STAMP_NEW", UNSET)

        color_annotation_marker_dm = d.pop("COLOR_ANNOTATION_MARKER_DM", UNSET)

        mb_note_freehand = d.pop("mbNoteFreehand", UNSET)

        mb_acl_items = d.pop("mbAclItems", UNSET)

        type_annotation_text = d.pop("TYPE_ANNOTATION_TEXT", UNSET)

        type_stamp = d.pop("TYPE_STAMP", UNSET)

        type_annotation_freehand = d.pop("TYPE_ANNOTATION_FREEHAND", UNSET)

        type_annotation_filledrectangle = d.pop("TYPE_ANNOTATION_FILLEDRECTANGLE", UNSET)

        type_normal = d.pop("TYPE_NORMAL", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        _mb_no_desc = d.pop("mbNoDesc", UNSET)
        mb_no_desc: Union[Unset, NoteZ]
        if isinstance(_mb_no_desc, Unset):
            mb_no_desc = UNSET
        else:
            mb_no_desc = NoteZ.from_dict(_mb_no_desc)

        type_annotation_strikeout = d.pop("TYPE_ANNOTATION_STRIKEOUT", UNSET)

        note_c = cls(
            type_annotation_line=type_annotation_line,
            type_annotation_note=type_annotation_note,
            type_normal_acl=type_normal_acl,
            type_annotation_filetext=type_annotation_filetext,
            type_annotation_note_withfont=type_annotation_note_withfont,
            type_none=type_none,
            type_annotation_rectangle=type_annotation_rectangle,
            mb_obj_id=mb_obj_id,
            mb_only_lock=mb_only_lock,
            type_anotewg_note=type_anotewg_note,
            type_anotew_marker=type_anotew_marker,
            type_annotation_stamp=type_annotation_stamp,
            type_personal=type_personal,
            type_annotation_hollowrectangle=type_annotation_hollowrectangle,
            mb_all=mb_all,
            mb_note_text=mb_note_text,
            mb_lock_id=mb_lock_id,
            mb_create_date_iso=mb_create_date_iso,
            type_annotation_horizontal_line=type_annotation_horizontal_line,
            type_annotation_marker=type_annotation_marker,
            mb_note_image=mb_note_image,
            type_annotation_stamp_new=type_annotation_stamp_new,
            color_annotation_marker_dm=color_annotation_marker_dm,
            mb_note_freehand=mb_note_freehand,
            mb_acl_items=mb_acl_items,
            type_annotation_text=type_annotation_text,
            type_stamp=type_stamp,
            type_annotation_freehand=type_annotation_freehand,
            type_annotation_filledrectangle=type_annotation_filledrectangle,
            type_normal=type_normal,
            mb_deleted=mb_deleted,
            mb_no_desc=mb_no_desc,
            type_annotation_strikeout=type_annotation_strikeout,
        )

        note_c.additional_properties = d
        return note_c

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
