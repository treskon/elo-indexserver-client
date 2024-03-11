from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.note_freehand import NoteFreehand
    from ..models.note_image import NoteImage
    from ..models.note_text import NoteText


T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    """<p>
    This helper class inherits all members from <code>NoteData</code> and adds a static member to access the bit
     constants for the <code>NoteData</code> members.
     </p>

        Attributes:
            t_stamp (Union[Unset, str]): Timestamp of the last change to the note. The format is JJJJ.MM.DD.hh.mm.
                ss
            x_pos (Union[Unset, int]): The position in the x axis when the note is displayed on a document in ELO.
                Taken from the top left corner of the
                 document.
                 <p>
                 For NoteC.TYPE_ANNOTATION_FREEHAND and NoteC.TYPE_ANNOTATION_HORIZONTAL_LINE the values XPos, YPos, Width,
                Height
                 describe the enveloping rectangle of the line including the line width. This values are computed by the
                Indexserver
                 if the note is stored.
                 </p>
            y_pos (Union[Unset, int]): The position in the Y axis when the note is displayed on a document in ELO.
                Taken from the top left corner of the
                 document.
            desc (Union[Unset, str]): The text for the note.
            guid (Union[Unset, str]): The GUID for the note.
            height (Union[Unset, int]): The height of the note (y axis), when displayed on a document in ELO.
            id (Union[Unset, int]): The unique id for the note.
            owner_id (Union[Unset, int]): The ID of the user who created the note. Administrators can set the ownerId to an
                arbitary user ID in checkinNotes.
                Set ownerName=&quot;&quot; in this case.
            page_no (Union[Unset, int]): The page number to which the note is attached.
            type (Union[Unset, int]): The note type.
            width (Union[Unset, int]): Width ( x axis) of the note when displayed on a document in ELO.
            create_date_iso (Union[Unset, str]): ISO encoded external (user defined) date.
            deleted (Union[Unset, bool]): True if the note is deleted, otherwise false.
            lock_id (Union[Unset, int]): The ID of the user that holds the lock or -1, if the note is not locked.
            lock_name (Union[Unset, str]): The user name that holds the lock or an empty string if the note is not locked.
            obj_id (Union[Unset, str]): Object ID of the associated Sord object or any of the ID specifiers that are valid
                for checkoutSord too.
                Functions
                 createNote and checkoutNotes return only numerical object IDs.
            owner_name (Union[Unset, str]): The name of the user that has created the note.
                Administrators can set the ownerName to an arbitary user name in
                 checkinNotes. Set ownerId=-1 in this case.
            acl (Union[Unset, str]): Access control list. Only used for notes of type TYPE_ANNOTATION_MARKER.
                Set member aclItems=null on check in
                 otherwise it is ignored.
            acl_items (Union[Unset, List['AclItem']]):
            color (Union[Unset, int]): RGB value. Undefined for notes of type TYPE_ANNOTATION_STAMP and
                TYPE_ANNOTATION_NOTE_WITHFONT.
            note_text (Union[Unset, NoteText]): This class conatins additional information for textual notes.
                NoteText objects can be used in NoteTemplate and Note
                 objects.
            note_image (Union[Unset, NoteImage]): This class contains additional information for image stamps.
            note_freehand (Union[Unset, NoteFreehand]): This class describes a freehand line annotation.
            access (Union[Unset, int]): Access rights for the current user. Read-only.
            delete_date_iso (Union[Unset, str]): The Note is deleted at this date. ClientInfo determines the Timezone.
                <p>
                 Is undefined if isDeleted() returns false.
                 </p>
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
    """

    t_stamp: Union[Unset, str] = UNSET
    x_pos: Union[Unset, int] = UNSET
    y_pos: Union[Unset, int] = UNSET
    desc: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    owner_id: Union[Unset, int] = UNSET
    page_no: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    lock_id: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    color: Union[Unset, int] = UNSET
    note_text: Union[Unset, "NoteText"] = UNSET
    note_image: Union[Unset, "NoteImage"] = UNSET
    note_freehand: Union[Unset, "NoteFreehand"] = UNSET
    access: Union[Unset, int] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp
        x_pos = self.x_pos
        y_pos = self.y_pos
        desc = self.desc
        guid = self.guid
        height = self.height
        id = self.id
        owner_id = self.owner_id
        page_no = self.page_no
        type = self.type
        width = self.width
        create_date_iso = self.create_date_iso
        deleted = self.deleted
        lock_id = self.lock_id
        lock_name = self.lock_name
        obj_id = self.obj_id
        owner_name = self.owner_name
        acl = self.acl
        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()

                acl_items.append(acl_items_item)

        color = self.color
        note_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_text, Unset):
            note_text = self.note_text.to_dict()

        note_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_image, Unset):
            note_image = self.note_image.to_dict()

        note_freehand: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_freehand, Unset):
            note_freehand = self.note_freehand.to_dict()

        access = self.access
        delete_date_iso = self.delete_date_iso
        t_stamp_sync = self.t_stamp_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if x_pos is not UNSET:
            field_dict["XPos"] = x_pos
        if y_pos is not UNSET:
            field_dict["YPos"] = y_pos
        if desc is not UNSET:
            field_dict["desc"] = desc
        if guid is not UNSET:
            field_dict["guid"] = guid
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if page_no is not UNSET:
            field_dict["pageNo"] = page_no
        if type is not UNSET:
            field_dict["type"] = type
        if width is not UNSET:
            field_dict["width"] = width
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if acl is not UNSET:
            field_dict["acl"] = acl
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if color is not UNSET:
            field_dict["color"] = color
        if note_text is not UNSET:
            field_dict["noteText"] = note_text
        if note_image is not UNSET:
            field_dict["noteImage"] = note_image
        if note_freehand is not UNSET:
            field_dict["noteFreehand"] = note_freehand
        if access is not UNSET:
            field_dict["access"] = access
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.note_freehand import NoteFreehand
        from ..models.note_image import NoteImage
        from ..models.note_text import NoteText

        d = src_dict.copy()
        t_stamp = d.pop("TStamp", UNSET)

        x_pos = d.pop("XPos", UNSET)

        y_pos = d.pop("YPos", UNSET)

        desc = d.pop("desc", UNSET)

        guid = d.pop("guid", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        page_no = d.pop("pageNo", UNSET)

        type = d.pop("type", UNSET)

        width = d.pop("width", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        deleted = d.pop("deleted", UNSET)

        lock_id = d.pop("lockId", UNSET)

        lock_name = d.pop("lockName", UNSET)

        obj_id = d.pop("objId", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        acl = d.pop("acl", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        color = d.pop("color", UNSET)

        _note_text = d.pop("noteText", UNSET)
        note_text: Union[Unset, NoteText]
        if isinstance(_note_text, Unset):
            note_text = UNSET
        else:
            note_text = NoteText.from_dict(_note_text)

        _note_image = d.pop("noteImage", UNSET)
        note_image: Union[Unset, NoteImage]
        if isinstance(_note_image, Unset):
            note_image = UNSET
        else:
            note_image = NoteImage.from_dict(_note_image)

        _note_freehand = d.pop("noteFreehand", UNSET)
        note_freehand: Union[Unset, NoteFreehand]
        if isinstance(_note_freehand, Unset):
            note_freehand = UNSET
        else:
            note_freehand = NoteFreehand.from_dict(_note_freehand)

        access = d.pop("access", UNSET)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        note = cls(
            t_stamp=t_stamp,
            x_pos=x_pos,
            y_pos=y_pos,
            desc=desc,
            guid=guid,
            height=height,
            id=id,
            owner_id=owner_id,
            page_no=page_no,
            type=type,
            width=width,
            create_date_iso=create_date_iso,
            deleted=deleted,
            lock_id=lock_id,
            lock_name=lock_name,
            obj_id=obj_id,
            owner_name=owner_name,
            acl=acl,
            acl_items=acl_items,
            color=color,
            note_text=note_text,
            note_image=note_image,
            note_freehand=note_freehand,
            access=access,
            delete_date_iso=delete_date_iso,
            t_stamp_sync=t_stamp_sync,
        )

        note.additional_properties = d
        return note

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
