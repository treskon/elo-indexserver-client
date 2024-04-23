from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.copy_sord_z import CopySordZ


T = TypeVar("T", bound="CopySordC")


@_attrs_define
class CopySordC:
    """Constants to copy or move archive entries, or to create a logical link.
    These constants are used as parameters in the
     copySord function.
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            bset_reference (Union[Unset, str]): Create a logical link.
            bset_copy_with_notes_type_personal (Union[Unset, str]): Copy archive entry with personal notes (CURRENTLY NOT
                SUPPORTED!).
            bset_copy_with_notes_type_stamp (Union[Unset, str]): Copy archive entry with stamps (CURRENTLY NOT SUPPORTED!).
            bset_copy_with_document_versions (Union[Unset, str]): Copy archive entry with document versions (CURRENTLY NOT
                SUPPORTED!).
            bset_copy_with_notes_type_normal (Union[Unset, str]): Copy archive entry with notes (CURRENTLY NOT SUPPORTED!).
            bset_copy_with_documents (Union[Unset, str]): Copy archive entry with documents (CURRENTLY NOT SUPPORTED!).
            bset_copy_with_attachments (Union[Unset, str]): Copy archive entry with attachments (CURRENTLY NOT SUPPORTED!).
            copy (Union[Unset, CopySordZ]): This class encapsulates the constants of the CopySordsC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_copy (Union[Unset, str]): Reserved. Use ProcessCopyElements and processTrees to copy an archive structure.
            bset_move (Union[Unset, str]): Move an archive entry.
            move (Union[Unset, CopySordZ]): This class encapsulates the constants of the CopySordsC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            reference (Union[Unset, CopySordZ]): This class encapsulates the constants of the CopySordsC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_copy_with_attachment_versions (Union[Unset, str]): Copy archive entry with attachment versions (CURRENTLY
                NOT SUPPORTED!).
            bset_copy_with_children (Union[Unset, str]): Copy archive entry with children (CURRENTLY NOT SUPPORTED!).
    """

    bset_reference: Union[Unset, str] = UNSET
    bset_copy_with_notes_type_personal: Union[Unset, str] = UNSET
    bset_copy_with_notes_type_stamp: Union[Unset, str] = UNSET
    bset_copy_with_document_versions: Union[Unset, str] = UNSET
    bset_copy_with_notes_type_normal: Union[Unset, str] = UNSET
    bset_copy_with_documents: Union[Unset, str] = UNSET
    bset_copy_with_attachments: Union[Unset, str] = UNSET
    copy: Union[Unset, "CopySordZ"] = UNSET
    bset_copy: Union[Unset, str] = UNSET
    bset_move: Union[Unset, str] = UNSET
    move: Union[Unset, "CopySordZ"] = UNSET
    reference: Union[Unset, "CopySordZ"] = UNSET
    bset_copy_with_attachment_versions: Union[Unset, str] = UNSET
    bset_copy_with_children: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_reference = self.bset_reference

        bset_copy_with_notes_type_personal = self.bset_copy_with_notes_type_personal

        bset_copy_with_notes_type_stamp = self.bset_copy_with_notes_type_stamp

        bset_copy_with_document_versions = self.bset_copy_with_document_versions

        bset_copy_with_notes_type_normal = self.bset_copy_with_notes_type_normal

        bset_copy_with_documents = self.bset_copy_with_documents

        bset_copy_with_attachments = self.bset_copy_with_attachments

        copy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy, Unset):
            copy = self.copy.to_dict()

        bset_copy = self.bset_copy

        bset_move = self.bset_move

        move: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.move, Unset):
            move = self.move.to_dict()

        reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict()

        bset_copy_with_attachment_versions = self.bset_copy_with_attachment_versions

        bset_copy_with_children = self.bset_copy_with_children

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_reference is not UNSET:
            field_dict["bsetREFERENCE"] = bset_reference
        if bset_copy_with_notes_type_personal is not UNSET:
            field_dict["bsetCOPY_WITH_NOTES_TYPE_PERSONAL"] = bset_copy_with_notes_type_personal
        if bset_copy_with_notes_type_stamp is not UNSET:
            field_dict["bsetCOPY_WITH_NOTES_TYPE_STAMP"] = bset_copy_with_notes_type_stamp
        if bset_copy_with_document_versions is not UNSET:
            field_dict["bsetCOPY_WITH_DOCUMENT_VERSIONS"] = bset_copy_with_document_versions
        if bset_copy_with_notes_type_normal is not UNSET:
            field_dict["bsetCOPY_WITH_NOTES_TYPE_NORMAL"] = bset_copy_with_notes_type_normal
        if bset_copy_with_documents is not UNSET:
            field_dict["bsetCOPY_WITH_DOCUMENTS"] = bset_copy_with_documents
        if bset_copy_with_attachments is not UNSET:
            field_dict["bsetCOPY_WITH_ATTACHMENTS"] = bset_copy_with_attachments
        if copy is not UNSET:
            field_dict["COPY"] = copy
        if bset_copy is not UNSET:
            field_dict["bsetCOPY"] = bset_copy
        if bset_move is not UNSET:
            field_dict["bsetMOVE"] = bset_move
        if move is not UNSET:
            field_dict["MOVE"] = move
        if reference is not UNSET:
            field_dict["REFERENCE"] = reference
        if bset_copy_with_attachment_versions is not UNSET:
            field_dict["bsetCOPY_WITH_ATTACHMENT_VERSIONS"] = bset_copy_with_attachment_versions
        if bset_copy_with_children is not UNSET:
            field_dict["bsetCOPY_WITH_CHILDREN"] = bset_copy_with_children

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.copy_sord_z import CopySordZ

        d = src_dict.copy()
        bset_reference = d.pop("bsetREFERENCE", UNSET)

        bset_copy_with_notes_type_personal = d.pop("bsetCOPY_WITH_NOTES_TYPE_PERSONAL", UNSET)

        bset_copy_with_notes_type_stamp = d.pop("bsetCOPY_WITH_NOTES_TYPE_STAMP", UNSET)

        bset_copy_with_document_versions = d.pop("bsetCOPY_WITH_DOCUMENT_VERSIONS", UNSET)

        bset_copy_with_notes_type_normal = d.pop("bsetCOPY_WITH_NOTES_TYPE_NORMAL", UNSET)

        bset_copy_with_documents = d.pop("bsetCOPY_WITH_DOCUMENTS", UNSET)

        bset_copy_with_attachments = d.pop("bsetCOPY_WITH_ATTACHMENTS", UNSET)

        _copy = d.pop("COPY", UNSET)
        copy: Union[Unset, CopySordZ]
        if isinstance(_copy, Unset):
            copy = UNSET
        else:
            copy = CopySordZ.from_dict(_copy)

        bset_copy = d.pop("bsetCOPY", UNSET)

        bset_move = d.pop("bsetMOVE", UNSET)

        _move = d.pop("MOVE", UNSET)
        move: Union[Unset, CopySordZ]
        if isinstance(_move, Unset):
            move = UNSET
        else:
            move = CopySordZ.from_dict(_move)

        _reference = d.pop("REFERENCE", UNSET)
        reference: Union[Unset, CopySordZ]
        if isinstance(_reference, Unset):
            reference = UNSET
        else:
            reference = CopySordZ.from_dict(_reference)

        bset_copy_with_attachment_versions = d.pop("bsetCOPY_WITH_ATTACHMENT_VERSIONS", UNSET)

        bset_copy_with_children = d.pop("bsetCOPY_WITH_CHILDREN", UNSET)

        copy_sord_c = cls(
            bset_reference=bset_reference,
            bset_copy_with_notes_type_personal=bset_copy_with_notes_type_personal,
            bset_copy_with_notes_type_stamp=bset_copy_with_notes_type_stamp,
            bset_copy_with_document_versions=bset_copy_with_document_versions,
            bset_copy_with_notes_type_normal=bset_copy_with_notes_type_normal,
            bset_copy_with_documents=bset_copy_with_documents,
            bset_copy_with_attachments=bset_copy_with_attachments,
            copy=copy,
            bset_copy=bset_copy,
            bset_move=bset_move,
            move=move,
            reference=reference,
            bset_copy_with_attachment_versions=bset_copy_with_attachment_versions,
            bset_copy_with_children=bset_copy_with_children,
        )

        copy_sord_c.additional_properties = d
        return copy_sord_c

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
