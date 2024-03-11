from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask import DocMask
    from ..models.document import Document
    from ..models.id_name import IdName
    from ..models.keyword import Keyword
    from ..models.mask_name import MaskName
    from ..models.note import Note
    from ..models.sord import Sord
    from ..models.sord_type import SordType


T = TypeVar("T", bound="EditInfo")


@_attrs_define
class EditInfo:
    """Contains data to edit the indexing information.
    Therfore it provides storage mask names, storage path names, marker
     names, document template names, replication set names, document version information, etc.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            doc_templates (Union[Unset, List['IdName']]):
            document (Union[Unset, Document]): Document object with identifier and version arrays for the document and
                attachments.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            keywords (Union[Unset, List['Keyword']]):
            marker_names (Union[Unset, List['IdName']]):
            mask (Union[Unset, DocMask]): <p>
                Contains the data for a storage mask.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mask_names (Union[Unset, List['MaskName']]):
            notes (Union[Unset, List['Note']]):
            path_names (Union[Unset, List['IdName']]):
            repl_names (Union[Unset, List['IdName']]):
            sord (Union[Unset, Sord]): <p>
                Indexing information of an archive entry.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            sord_types (Union[Unset, List['SordType']]):
    """

    doc_templates: Union[Unset, List["IdName"]] = UNSET
    document: Union[Unset, "Document"] = UNSET
    keywords: Union[Unset, List["Keyword"]] = UNSET
    marker_names: Union[Unset, List["IdName"]] = UNSET
    mask: Union[Unset, "DocMask"] = UNSET
    mask_names: Union[Unset, List["MaskName"]] = UNSET
    notes: Union[Unset, List["Note"]] = UNSET
    path_names: Union[Unset, List["IdName"]] = UNSET
    repl_names: Union[Unset, List["IdName"]] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    sord_types: Union[Unset, List["SordType"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_templates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.doc_templates, Unset):
            doc_templates = []
            for doc_templates_item_data in self.doc_templates:
                doc_templates_item = doc_templates_item_data.to_dict()

                doc_templates.append(doc_templates_item)

        document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        keywords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = []
            for keywords_item_data in self.keywords:
                keywords_item = keywords_item_data.to_dict()

                keywords.append(keywords_item)

        marker_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.marker_names, Unset):
            marker_names = []
            for marker_names_item_data in self.marker_names:
                marker_names_item = marker_names_item_data.to_dict()

                marker_names.append(marker_names_item)

        mask: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.to_dict()

        mask_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mask_names, Unset):
            mask_names = []
            for mask_names_item_data in self.mask_names:
                mask_names_item = mask_names_item_data.to_dict()

                mask_names.append(mask_names_item)

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()

                notes.append(notes_item)

        path_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.path_names, Unset):
            path_names = []
            for path_names_item_data in self.path_names:
                path_names_item = path_names_item_data.to_dict()

                path_names.append(path_names_item)

        repl_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.repl_names, Unset):
            repl_names = []
            for repl_names_item_data in self.repl_names:
                repl_names_item = repl_names_item_data.to_dict()

                repl_names.append(repl_names_item)

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        sord_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sord_types, Unset):
            sord_types = []
            for sord_types_item_data in self.sord_types:
                sord_types_item = sord_types_item_data.to_dict()

                sord_types.append(sord_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_templates is not UNSET:
            field_dict["docTemplates"] = doc_templates
        if document is not UNSET:
            field_dict["document"] = document
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if marker_names is not UNSET:
            field_dict["markerNames"] = marker_names
        if mask is not UNSET:
            field_dict["mask"] = mask
        if mask_names is not UNSET:
            field_dict["maskNames"] = mask_names
        if notes is not UNSET:
            field_dict["notes"] = notes
        if path_names is not UNSET:
            field_dict["pathNames"] = path_names
        if repl_names is not UNSET:
            field_dict["replNames"] = repl_names
        if sord is not UNSET:
            field_dict["sord"] = sord
        if sord_types is not UNSET:
            field_dict["sordTypes"] = sord_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask import DocMask
        from ..models.document import Document
        from ..models.id_name import IdName
        from ..models.keyword import Keyword
        from ..models.mask_name import MaskName
        from ..models.note import Note
        from ..models.sord import Sord
        from ..models.sord_type import SordType

        d = src_dict.copy()
        doc_templates = []
        _doc_templates = d.pop("docTemplates", UNSET)
        for doc_templates_item_data in _doc_templates or []:
            doc_templates_item = IdName.from_dict(doc_templates_item_data)

            doc_templates.append(doc_templates_item)

        _document = d.pop("document", UNSET)
        document: Union[Unset, Document]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = Document.from_dict(_document)

        keywords = []
        _keywords = d.pop("keywords", UNSET)
        for keywords_item_data in _keywords or []:
            keywords_item = Keyword.from_dict(keywords_item_data)

            keywords.append(keywords_item)

        marker_names = []
        _marker_names = d.pop("markerNames", UNSET)
        for marker_names_item_data in _marker_names or []:
            marker_names_item = IdName.from_dict(marker_names_item_data)

            marker_names.append(marker_names_item)

        _mask = d.pop("mask", UNSET)
        mask: Union[Unset, DocMask]
        if isinstance(_mask, Unset):
            mask = UNSET
        else:
            mask = DocMask.from_dict(_mask)

        mask_names = []
        _mask_names = d.pop("maskNames", UNSET)
        for mask_names_item_data in _mask_names or []:
            mask_names_item = MaskName.from_dict(mask_names_item_data)

            mask_names.append(mask_names_item)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        path_names = []
        _path_names = d.pop("pathNames", UNSET)
        for path_names_item_data in _path_names or []:
            path_names_item = IdName.from_dict(path_names_item_data)

            path_names.append(path_names_item)

        repl_names = []
        _repl_names = d.pop("replNames", UNSET)
        for repl_names_item_data in _repl_names or []:
            repl_names_item = IdName.from_dict(repl_names_item_data)

            repl_names.append(repl_names_item)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        sord_types = []
        _sord_types = d.pop("sordTypes", UNSET)
        for sord_types_item_data in _sord_types or []:
            sord_types_item = SordType.from_dict(sord_types_item_data)

            sord_types.append(sord_types_item)

        edit_info = cls(
            doc_templates=doc_templates,
            document=document,
            keywords=keywords,
            marker_names=marker_names,
            mask=mask,
            mask_names=mask_names,
            notes=notes,
            path_names=path_names,
            repl_names=repl_names,
            sord=sord,
            sord_types=sord_types,
        )

        edit_info.additional_properties = d
        return edit_info

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
